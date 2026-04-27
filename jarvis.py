#!/usr/bin/env python3
"""Local evolution layer for this Jarvis workspace."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import uuid
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent

DIRS = [
    "memory",
    "evolution",
    "evolution/proposals",
    "tasks",
    "runs",
    "inbox",
    "prompts",
    "evals",
]

PATHS = {
    "feedback": ROOT / "inbox" / "feedback.jsonl",
    "observations": ROOT / "inbox" / "observations.jsonl",
    "tasks": ROOT / "tasks" / "tasks.jsonl",
    "rules": ROOT / "memory" / "rules.md",
    "lessons": ROOT / "memory" / "lessons.md",
    "state": ROOT / "memory" / "operating_state.md",
    "evolution_log": ROOT / "evolution" / "evolution_log.jsonl",
}

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "jarvis.py",
    "jarvis.yaml",
    "memory/profile.md",
    "memory/self_profile.md",
    "memory/preferences.md",
    "memory/rules.md",
    "memory/operating_state.md",
    "memory/lessons.md",
    "evolution/scorecard.md",
    "evolution/decision_log.md",
    "prompts/session_boot.md",
    "prompts/jarvis_system.md",
    "evals/self_check.md",
    "scripts/evolve_self_memory.py",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today() -> str:
    return datetime.now().date().isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def ensure_dirs() -> None:
    for directory in DIRS:
        (ROOT / directory).mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def append_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for index, line in enumerate(handle, start=1):
            stripped = line.strip()
            if stripped:
                try:
                    rows.append(json.loads(stripped))
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{path}:{index}: invalid JSONL: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    tmp.replace(path)


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def recent_rows(rows: list[dict[str, Any]], days: int) -> list[dict[str, Any]]:
    cutoff = datetime.now(timezone.utc).astimezone() - timedelta(days=days)
    recent: list[dict[str, Any]] = []
    for row in rows:
        timestamp = row.get("created_at") or row.get("updated_at") or row.get("completed_at")
        if not timestamp:
            continue
        try:
            parsed = datetime.fromisoformat(timestamp)
        except ValueError:
            continue
        if parsed >= cutoff:
            recent.append(row)
    return recent


def log_event(kind: str, payload: dict[str, Any]) -> None:
    append_jsonl(
        PATHS["evolution_log"],
        {
            "id": new_id("evt"),
            "created_at": now_iso(),
            "kind": kind,
            "payload": payload,
        },
    )


def cmd_init(_: argparse.Namespace) -> int:
    ensure_dirs()
    for key in ["feedback", "observations", "tasks", "evolution_log"]:
        PATHS[key].touch(exist_ok=True)
    print("Jarvis workspace initialized.")
    return 0


def cmd_status(_: argparse.Namespace) -> int:
    ensure_dirs()
    feedback = read_jsonl(PATHS["feedback"])
    observations = read_jsonl(PATHS["observations"])
    tasks = read_jsonl(PATHS["tasks"])
    open_tasks = [task for task in tasks if task.get("status", "open") == "open"]
    done_tasks = [task for task in tasks if task.get("status") == "done"]
    recent_feedback = recent_rows(feedback, 7)
    recent_observations = recent_rows(observations, 7)
    reflections = sorted((ROOT / "runs").glob("*-reflection.md"))
    last_reflection = reflections[-1].name if reflections else "none"

    print("Jarvis status")
    print(f"- open_tasks: {len(open_tasks)}")
    print(f"- done_tasks: {len(done_tasks)}")
    print(f"- feedback_7d: {len(recent_feedback)}")
    print(f"- observations_7d: {len(recent_observations)}")
    print(f"- last_reflection: {last_reflection}")
    print("")
    print("Next concrete action")
    if open_tasks:
        top = sorted(open_tasks, key=lambda row: row.get("priority", "P2"))[0]
        print(f"- Work task {top['id']}: {top['text']}")
    else:
        print("- Capture the next correction, task, or outcome as soon as it appears.")
    return 0


def cmd_boot(_: argparse.Namespace) -> int:
    parts = [
        ("SESSION BOOT", ROOT / "prompts" / "session_boot.md"),
        ("AGENTS", ROOT / "AGENTS.md"),
        ("PROFILE", ROOT / "memory" / "profile.md"),
        ("RULES", ROOT / "memory" / "rules.md"),
        ("OPERATING STATE", ROOT / "memory" / "operating_state.md"),
    ]
    for title, path in parts:
        print(f"\n# {title}\n")
        content = read_text(path).strip()
        print(content if content else f"{path.name} is empty.")
    return 0


def cmd_feedback(args: argparse.Namespace) -> int:
    text = " ".join(args.text).strip()
    row = {
        "id": new_id("fb"),
        "created_at": now_iso(),
        "source": args.source,
        "tag": args.tag,
        "text": text,
    }
    append_jsonl(PATHS["feedback"], row)
    log_event("feedback_captured", {"feedback_id": row["id"], "tag": args.tag})
    print(f"Captured feedback {row['id']}.")
    return 0


def cmd_observe(args: argparse.Namespace) -> int:
    text = " ".join(args.text).strip()
    row = {
        "id": new_id("obs"),
        "created_at": now_iso(),
        "source": args.source,
        "tag": args.tag,
        "text": text,
    }
    append_jsonl(PATHS["observations"], row)
    log_event("observation_captured", {"observation_id": row["id"], "tag": args.tag})
    print(f"Captured observation {row['id']}.")
    return 0


def cmd_task(args: argparse.Namespace) -> int:
    text = " ".join(args.text).strip()
    row = {
        "id": new_id("task"),
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "priority": args.priority,
        "area": args.area,
        "status": "open",
        "text": text,
    }
    append_jsonl(PATHS["tasks"], row)
    log_event("task_created", {"task_id": row["id"], "priority": args.priority, "area": args.area})
    print(f"Created task {row['id']}.")
    return 0


def cmd_done(args: argparse.Namespace) -> int:
    tasks = read_jsonl(PATHS["tasks"])
    found = False
    for task in tasks:
        if task.get("id") == args.task_id:
            task["status"] = "done"
            task["updated_at"] = now_iso()
            task["completed_at"] = now_iso()
            if args.note:
                task["note"] = args.note
            found = True
            break
    if not found:
        print(f"Task not found: {args.task_id}", file=sys.stderr)
        return 1
    write_jsonl(PATHS["tasks"], tasks)
    log_event("task_done", {"task_id": args.task_id, "note": args.note or ""})
    print(f"Marked done {args.task_id}.")
    return 0


def cmd_promote(args: argparse.Namespace) -> int:
    rule = " ".join(args.rule).strip()
    entry = (
        f"\n## {today()} - {args.area}\n\n"
        f"- Rule: {rule}\n"
        f"- Reason: {args.reason}\n"
    )
    append_text(PATHS["rules"], entry)
    log_event("rule_promoted", {"area": args.area, "rule": rule, "reason": args.reason})
    print("Promoted rule.")
    return 0


def cmd_reflect(args: argparse.Namespace) -> int:
    ensure_dirs()
    feedback = recent_rows(read_jsonl(PATHS["feedback"]), args.days)
    observations = recent_rows(read_jsonl(PATHS["observations"]), args.days)
    tasks = recent_rows(read_jsonl(PATHS["tasks"]), args.days)

    tags = Counter(row.get("tag", "general") for row in feedback + observations)
    open_tasks = [task for task in read_jsonl(PATHS["tasks"]) if task.get("status", "open") == "open"]
    done_tasks = [task for task in tasks if task.get("status") == "done"]

    date = args.date or today()
    path = ROOT / "runs" / f"{date}-reflection.md"
    proposal_path = ROOT / "evolution" / "proposals" / f"{date}-proposal.md"

    lines = [
        f"# Jarvis Reflection - {date}",
        "",
        f"Window: last {args.days} day(s)",
        "",
        "## Signals",
        "",
        f"- feedback: {len(feedback)}",
        f"- observations: {len(observations)}",
        f"- done_tasks: {len(done_tasks)}",
        f"- open_tasks: {len(open_tasks)}",
        "",
        "## Top Tags",
        "",
    ]
    if tags:
        lines.extend(f"- {tag}: {count}" for tag, count in tags.most_common())
    else:
        lines.append("- none")

    lines.extend(["", "## Recent Feedback", ""])
    if feedback:
        lines.extend(f"- {row['id']}: {row['text']}" for row in feedback[-10:])
    else:
        lines.append("- none")

    lines.extend(["", "## Recent Observations", ""])
    if observations:
        lines.extend(f"- {row['id']}: {row['text']}" for row in observations[-10:])
    else:
        lines.append("- none")

    lines.extend(["", "## Recommended Promotions", ""])
    correction_count = sum(1 for row in feedback if row.get("tag") == "correction")
    if correction_count:
        lines.append("- Review correction-tagged feedback and promote durable behavior into `memory/rules.md`.")
    else:
        lines.append("- Keep observing; no correction pattern has crossed the promotion threshold.")

    lines.extend(["", "## Next Actions", ""])
    if open_tasks:
        for task in sorted(open_tasks, key=lambda row: row.get("priority", "P2"))[:5]:
            lines.append(f"- {task['priority']} {task['id']}: {task['text']}")
    else:
        lines.append("- Add the next concrete Jarvis capability as a tracked task.")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    proposal = [
        f"# Evolution Proposal - {date}",
        "",
        "## Candidate Changes",
        "",
        "- Promote explicit user corrections into `memory/rules.md`.",
        "- Update `AGENTS.md` when a rule affects every future Codex turn in this workspace.",
        "- Keep one-off facts in `inbox/observations.jsonl` until repeated.",
        "",
        "## Evidence",
        "",
    ]
    if feedback or observations:
        for row in (feedback + observations)[-10:]:
            proposal.append(f"- {row.get('id')}: [{row.get('tag')}] {row.get('text')}")
    else:
        proposal.append("- No new evidence in the selected window.")
    proposal_path.write_text("\n".join(proposal) + "\n", encoding="utf-8")

    log_event("reflection_written", {"path": str(path.relative_to(ROOT)), "proposal": str(proposal_path.relative_to(ROOT))})
    print(f"Wrote {path.relative_to(ROOT)}")
    print(f"Wrote {proposal_path.relative_to(ROOT)}")
    return 0


def validate() -> list[str]:
    errors: list[str] = []
    for directory in DIRS:
        if not (ROOT / directory).is_dir():
            errors.append(f"missing directory: {directory}")
    for filename in REQUIRED_FILES:
        if not (ROOT / filename).is_file():
            errors.append(f"missing file: {filename}")
    for key in ["feedback", "observations", "tasks", "evolution_log"]:
        try:
            read_jsonl(PATHS[key])
        except ValueError as exc:
            errors.append(str(exc))
    agents = read_text(ROOT / "AGENTS.md")
    if "Evolution Loop" not in agents:
        errors.append("AGENTS.md missing Evolution Loop")
    if "Use direct positive claims" not in agents:
        errors.append("AGENTS.md missing voice rule")
    return errors


def cmd_self_check(_: argparse.Namespace) -> int:
    errors = validate()
    if errors:
        print("Jarvis self-check failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Jarvis self-check passed")
    return 0


def cmd_auto_review(args: argparse.Namespace) -> int:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "codex_auto_review.py"),
        "--repo",
        args.repo,
        "--mode",
        args.mode,
        "--timeout",
        str(args.timeout),
    ]
    if args.base:
        command.extend(["--base", args.base])
    if args.commit:
        command.extend(["--commit", args.commit])
    if args.prompt:
        command.extend(["--prompt", args.prompt])
    if args.no_web_search:
        command.append("--no-web-search")
    if args.dry_run:
        command.append("--dry-run")
    if args.no_record:
        command.append("--no-record")
    if args.no_fail_on_findings:
        command.append("--no-fail-on-findings")
    return subprocess.call(command)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evolving Jarvis local CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create required directories")
    init.set_defaults(func=cmd_init)

    status = sub.add_parser("status", help="show current operating status")
    status.set_defaults(func=cmd_status)

    boot = sub.add_parser("boot", help="print boot context for a new session")
    boot.set_defaults(func=cmd_boot)

    feedback = sub.add_parser("feedback", help="capture user feedback or corrections")
    feedback.add_argument("text", nargs="+")
    feedback.add_argument("--source", default="user")
    feedback.add_argument("--tag", default="general")
    feedback.set_defaults(func=cmd_feedback)

    observe = sub.add_parser("observe", help="capture an operational observation")
    observe.add_argument("text", nargs="+")
    observe.add_argument("--source", default="self")
    observe.add_argument("--tag", default="general")
    observe.set_defaults(func=cmd_observe)

    task = sub.add_parser("task", help="create a tracked task")
    task.add_argument("text", nargs="+")
    task.add_argument("--priority", choices=["P0", "P1", "P2"], default="P1")
    task.add_argument("--area", default="general")
    task.set_defaults(func=cmd_task)

    done = sub.add_parser("done", help="mark a task complete")
    done.add_argument("task_id")
    done.add_argument("--note", default="")
    done.set_defaults(func=cmd_done)

    promote = sub.add_parser("promote", help="promote a stable behavior into rules")
    promote.add_argument("rule", nargs="+")
    promote.add_argument("--reason", required=True)
    promote.add_argument("--area", default="behavior")
    promote.set_defaults(func=cmd_promote)

    reflect = sub.add_parser("reflect", help="write a reflection and evolution proposal")
    reflect.add_argument("--days", type=int, default=7)
    reflect.add_argument("--date", default="")
    reflect.set_defaults(func=cmd_reflect)

    self_check = sub.add_parser("self-check", help="validate the Jarvis workspace")
    self_check.set_defaults(func=cmd_self_check)

    auto_review = sub.add_parser("auto-review", help="run Codex review and archive a gate report")
    auto_review.add_argument("--repo", default=".", help="target git repo path")
    auto_review.add_argument("--base", default="", help="base branch/rev for branch review")
    auto_review.add_argument("--commit", default="", help="review a single commit SHA")
    auto_review.add_argument("--mode", choices=["auto", "base", "uncommitted"], default="auto")
    auto_review.add_argument("--prompt", default="", help="custom review instructions")
    auto_review.add_argument("--timeout", type=int, default=300, help="Codex review timeout in seconds")
    auto_review.add_argument("--no-web-search", action="store_true", help="skip cached web search feature")
    auto_review.add_argument("--dry-run", action="store_true", help="print command without running Codex")
    auto_review.add_argument("--no-record", action="store_true", help="skip Jarvis observation/event recording")
    auto_review.add_argument("--no-fail-on-findings", action="store_true", help="exit 0 even on P0/P1 findings")
    auto_review.set_defaults(func=cmd_auto_review)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
