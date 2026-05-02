#!/usr/bin/env python3
"""Generate better Codex thread titles and optionally write them back."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import shutil
import sqlite3
import subprocess
import sys
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CODEX_HOME = Path.home() / ".codex"
DEFAULT_STATE_DB = DEFAULT_CODEX_HOME / "state_5.sqlite"
DEFAULT_SESSION_INDEX = DEFAULT_CODEX_HOME / "session_index.jsonl"
RUN_ROOT = ROOT / "runs" / "codex_thread_renames"
OBSERVATIONS = ROOT / "inbox" / "observations.jsonl"


class RenameError(Exception):
    """Expected failure with a user-readable message."""


@dataclass(frozen=True)
class ThreadRow:
    id: str
    title: str
    rollout_path: Path
    updated_at_ms: int
    archived: bool
    first_user_message: str


def now() -> datetime:
    return datetime.now(timezone.utc).astimezone()


def now_iso() -> str:
    return now().isoformat(timespec="seconds")


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_threads(db_path: Path, include_archived: bool, limit: int | None) -> list[ThreadRow]:
    if not db_path.exists():
        raise RenameError(f"Codex state DB not found: {db_path}")

    where = "" if include_archived else "where archived = 0"
    limit_sql = "" if limit is None else "limit ?"
    sql = f"""
        select id, title, rollout_path, updated_at_ms, archived, first_user_message
        from threads
        {where}
        order by updated_at_ms desc, id desc
        {limit_sql}
    """
    params: tuple[int, ...] = () if limit is None else (limit,)

    with sqlite3.connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()

    return [
        ThreadRow(
            id=str(row[0]),
            title=str(row[1] or ""),
            rollout_path=Path(str(row[2] or "")).expanduser(),
            updated_at_ms=int(row[3] or 0),
            archived=bool(row[4]),
            first_user_message=str(row[5] or ""),
        )
        for row in rows
    ]


def content_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        for key in ("text", "input_text", "output_text"):
            value = item.get(key)
            if isinstance(value, str):
                parts.append(value)
                break
    return "\n".join(parts)


def event_text(payload: dict[str, Any]) -> tuple[str, str] | None:
    event_type = payload.get("type")
    if event_type == "user_message":
        text = payload.get("message")
        return ("user", text) if isinstance(text, str) else None
    if event_type == "agent_message":
        text = payload.get("message")
        return ("assistant", text) if isinstance(text, str) else None
    return None


def response_text(payload: dict[str, Any]) -> tuple[str, str] | None:
    if payload.get("type") != "message":
        return None
    role = payload.get("role")
    if role not in {"user", "assistant"}:
        return None
    text = content_text(payload.get("content"))
    return (str(role), text) if text else None


def read_rollout_excerpt(thread: ThreadRow, max_chars: int) -> str:
    messages: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()

    if thread.first_user_message:
        messages.append(("user", thread.first_user_message))
        seen.add(("user", thread.first_user_message))

    if thread.rollout_path.exists():
        with thread.rollout_path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue

                item: tuple[str, str] | None = None
                row_type = row.get("type")
                payload = row.get("payload")
                if isinstance(payload, dict):
                    if row_type == "event_msg":
                        item = event_text(payload)
                    elif row_type == "response_item":
                        item = response_text(payload)

                if not item:
                    continue
                role, text = item
                text = re.sub(r"\s+", " ", text).strip()
                if not text:
                    continue
                marker = (role, text)
                if marker in seen:
                    continue
                seen.add(marker)
                messages.append(marker)
                if len(messages) >= 18:
                    break

    if not messages:
        return thread.title

    excerpt_parts: list[str] = []
    total = 0
    for role, text in messages:
        remaining = max_chars - total
        if remaining <= 0:
            break
        piece = f"{role}: {text[:remaining]}"
        excerpt_parts.append(piece)
        total += len(piece)
    return "\n".join(excerpt_parts).strip()


def heuristic_title(thread: ThreadRow, excerpt: str) -> str:
    source = thread.first_user_message or excerpt or thread.title
    source = re.sub(r"https?://\S+", "", source)
    source = re.sub(r"[$`*_#>\[\]{}()<>]", "", source)
    source = re.sub(r"\s+", " ", source).strip(" \t\r\n,.:;!?，。；：！？")
    if len(source) <= 24:
        return source or thread.title
    return source[:24].strip(" \t\r\n,.:;!?，。；：！？")


def build_title_prompt(thread: ThreadRow, excerpt: str) -> str:
    payload = {
        "thread_id": thread.id,
        "current_title": thread.title,
        "conversation_excerpt": excerpt,
    }
    return (
        "Create one concise Codex conversation title from the conversation excerpt.\n"
        "Rules:\n"
        "- Return exactly one JSON object: {\"title\":\"...\"}\n"
        "- Title language should match the user's main language.\n"
        "- Use 4 to 18 Chinese characters when Chinese fits; English product names are allowed.\n"
        "- Prefer a concrete project, task, artifact, or decision.\n"
        "- Avoid generic words like help, question, conversation, chat, todo.\n"
        "- Avoid URLs, quotes, emoji, and punctuation unless the punctuation is part of a product name.\n"
        "- Do not explain.\n\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
    )


def parse_codex_title(raw: str) -> str:
    text = raw.strip()
    try:
        data = json.loads(text)
        title = data.get("title")
        if isinstance(title, str):
            return title
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", text, re.S)
    if match:
        try:
            data = json.loads(match.group(0))
            title = data.get("title")
            if isinstance(title, str):
                return title
        except json.JSONDecodeError:
            pass

    return text.splitlines()[-1] if text.splitlines() else ""


def sanitize_title(title: str, fallback: str) -> str:
    title = title.strip().strip("\"'`")
    title = re.sub(r"[\r\n\t]+", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    title = re.sub(r"https?://\S+", "", title).strip()
    title = title.strip(" \t\r\n,.:;!?，。；：！？")
    if not title:
        title = fallback
    if len(title) > 40:
        title = title[:40].strip(" \t\r\n,.:;!?，。；：！？")
    return title


def run_codex_title(
    codex_bin: str,
    thread: ThreadRow,
    excerpt: str,
    cwd: Path,
    timeout: int,
    model: str,
    reasoning_effort: str,
) -> str:
    command = [
        codex_bin,
        "exec",
        "--ephemeral",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "-C",
        str(cwd),
    ]
    if model:
        command.extend(["--model", model])
    if reasoning_effort:
        command.extend(["-c", f'model_reasoning_effort="{reasoning_effort}"'])
    command.append("-")

    result = subprocess.run(
        command,
        input=build_title_prompt(thread, excerpt),
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        rendered = " ".join(shlex.quote(part) for part in command)
        detail = (result.stderr or result.stdout or "").strip()
        raise RenameError(f"Codex title generation failed ({result.returncode}): {rendered}\n{detail}")
    return sanitize_title(parse_codex_title(result.stdout), fallback=thread.title)


def build_plan(
    threads: list[ThreadRow],
    args: argparse.Namespace,
    report_dir: Path,
) -> list[dict[str, Any]]:
    codex_bin = shutil.which("codex")
    if not args.no_codex and not codex_bin:
        raise RenameError("Codex CLI not found. Install it or run with --no-codex for heuristic titles.")

    plan: list[dict[str, Any]] = []
    for index, thread in enumerate(threads, start=1):
        excerpt = read_rollout_excerpt(thread, args.max_chars)
        if args.no_codex:
            proposed = sanitize_title(heuristic_title(thread, excerpt), fallback=thread.title)
            method = "heuristic"
        else:
            assert codex_bin is not None
            proposed = run_codex_title(
                codex_bin=codex_bin,
                thread=thread,
                excerpt=excerpt,
                cwd=ROOT,
                timeout=args.timeout,
                model=args.model,
                reasoning_effort=args.reasoning_effort,
            )
            method = "codex"

        row = {
            "thread_id": thread.id,
            "current_title": thread.title,
            "proposed_title": proposed,
            "changed": proposed != thread.title,
            "archived": thread.archived,
            "updated_at_ms": thread.updated_at_ms,
            "rollout_path": str(thread.rollout_path),
            "method": method,
        }
        plan.append(row)
        append_jsonl(report_dir / "rename_plan.jsonl", row)
        print(
            f"[{index}/{len(threads)}] {thread.id} | "
            f"{thread.title!r} -> {proposed!r}"
        )
    return plan


def backup_sqlite(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(source) as src, sqlite3.connect(target) as dst:
        src.backup(dst)


def backup_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def apply_sqlite_titles(db_path: Path, plan: list[dict[str, Any]]) -> int:
    changed = [row for row in plan if row["changed"]]
    with sqlite3.connect(db_path) as conn:
        conn.executemany(
            "update threads set title = ? where id = ?",
            [(row["proposed_title"], row["thread_id"]) for row in changed],
        )
    return len(changed)


def apply_session_index(index_path: Path, plan: list[dict[str, Any]]) -> int:
    if not index_path.exists():
        return 0

    titles = {row["thread_id"]: row["proposed_title"] for row in plan if row["changed"]}
    updated = 0
    new_lines: list[str] = []
    with index_path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                new_lines.append(line)
                continue
            thread_id = row.get("id")
            if isinstance(thread_id, str) and thread_id in titles:
                row["thread_name"] = titles[thread_id]
                updated += 1
            new_lines.append(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    index_path.write_text("".join(new_lines), encoding="utf-8")
    return updated


def write_markdown_report(report_dir: Path, plan: list[dict[str, Any]], applied: bool) -> None:
    rows = [
        "# Codex Thread Rename Plan",
        "",
        f"- created_at: {now_iso()}",
        f"- applied: {str(applied).lower()}",
        f"- total: {len(plan)}",
        f"- changed: {sum(1 for row in plan if row['changed'])}",
        "",
        "| Thread | Current | Proposed | Method |",
        "| --- | --- | --- | --- |",
    ]
    for row in plan:
        current = str(row["current_title"]).replace("|", "\\|")
        proposed = str(row["proposed_title"]).replace("|", "\\|")
        rows.append(f"| `{row['thread_id']}` | {current} | {proposed} | {row['method']} |")
    (report_dir / "rename_plan.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def record_observation(report_dir: Path, plan: list[dict[str, Any]], applied: bool) -> None:
    append_jsonl(
        OBSERVATIONS,
        {
            "id": new_id("obs"),
            "created_at": now_iso(),
            "source": "codex_thread_rename",
            "tag": "automation",
            "text": (
                "Codex thread rename "
                f"{'applied' if applied else 'previewed'} "
                f"{sum(1 for row in plan if row['changed'])}/{len(plan)} titles "
                f"(report={report_dir})."
            ),
        },
    )


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Use Codex to rename Codex conversation titles.")
    parser.add_argument("--state-db", default=str(DEFAULT_STATE_DB), help="Path to Codex state SQLite DB.")
    parser.add_argument("--session-index", default=str(DEFAULT_SESSION_INDEX), help="Path to session_index.jsonl.")
    parser.add_argument("--limit", type=int, default=10, help="Number of newest threads to process. Use 0 for all.")
    parser.add_argument("--all", action="store_true", help="Process all matching threads.")
    parser.add_argument("--include-archived", action="store_true", help="Include archived threads.")
    parser.add_argument("--apply", action="store_true", help="Write proposed titles back to Codex state.")
    parser.add_argument("--no-codex", action="store_true", help="Use a local heuristic instead of codex exec.")
    parser.add_argument("--timeout", type=int, default=120, help="Per-thread codex exec timeout in seconds.")
    parser.add_argument("--max-chars", type=int, default=5000, help="Maximum conversation excerpt characters.")
    parser.add_argument("--model", default="", help="Optional Codex model override.")
    parser.add_argument("--reasoning-effort", default="low", help="Codex reasoning effort for title generation.")
    parser.add_argument("--no-record", action="store_true", help="Skip Jarvis observation recording.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    limit = None if args.all or args.limit == 0 else args.limit
    if limit is not None and limit < 0:
        parser.error("--limit must be 0 or a positive integer")

    state_db = Path(args.state_db).expanduser().resolve()
    session_index = Path(args.session_index).expanduser().resolve()
    report_dir = RUN_ROOT / now().strftime("%Y%m%d-%H%M%S")
    report_dir.mkdir(parents=True, exist_ok=True)

    try:
        threads = read_threads(state_db, include_archived=args.include_archived, limit=limit)
        if not threads:
            raise RenameError("No Codex threads matched the selection.")

        plan = build_plan(threads, args, report_dir)
        applied = False
        if args.apply:
            backup_dir = report_dir / "backup"
            backup_sqlite(state_db, backup_dir / state_db.name)
            if session_index.exists():
                backup_file(session_index, backup_dir / session_index.name)
            sqlite_updates = apply_sqlite_titles(state_db, plan)
            index_updates = apply_session_index(session_index, plan)
            applied = True
            print(f"Applied updates: sqlite={sqlite_updates}, session_index={index_updates}")

        write_markdown_report(report_dir, plan, applied=applied)
        if not args.no_record:
            record_observation(report_dir, plan, applied=applied)

        print(f"Report: {report_dir}")
        print("Mode: apply" if applied else "Mode: preview")
        return 0
    except subprocess.TimeoutExpired:
        print(f"Codex title generation timed out after {args.timeout}s", file=sys.stderr)
        return 124
    except RenameError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
