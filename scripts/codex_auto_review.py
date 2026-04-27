#!/usr/bin/env python3
"""Run Codex review for a target git repo and archive the result."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = ROOT / "runs" / "codex_auto_review"
EVENT_LOG = ROOT / "evolution" / "evolution_log.jsonl"
OBSERVATIONS = ROOT / "inbox" / "observations.jsonl"
DEFAULT_PROMPT = (
    "Focus on correctness, security, data loss, regression risk, and missing tests. "
    "Report only actionable findings and use priority markers like [P1] or [P2]."
)


class ReviewError(Exception):
    """Expected failure with a user-readable message."""


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


def run_command(args: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=str(cwd), text=True, capture_output=True)
    if check and result.returncode != 0:
        command = " ".join(shlex.quote(part) for part in args)
        detail = (result.stderr or result.stdout or "").strip()
        raise ReviewError(f"Command failed ({result.returncode}): {command}\n{detail}")
    return result


def git(args: list[str], repo: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run_command(["git", *args], cwd=repo, check=check)


def git_output(args: list[str], repo: Path, check: bool = True) -> str:
    return git(args, repo, check=check).stdout.strip()


def resolve_repo(path: Path) -> Path:
    if not path.exists():
        raise ReviewError(f"Repo path does not exist: {path}")
    result = run_command(["git", "rev-parse", "--show-toplevel"], cwd=path, check=False)
    if result.returncode != 0:
        raise ReviewError(f"Path is not inside a git repo: {path}")
    return Path(result.stdout.strip()).resolve()


def rev_exists(repo: Path, rev: str) -> bool:
    result = git(["rev-parse", "--verify", "--quiet", rev], repo, check=False)
    return result.returncode == 0


def detect_base(repo: Path, explicit: str | None) -> str | None:
    if explicit:
        if not rev_exists(repo, explicit):
            raise ReviewError(f"Base branch/rev not found: {explicit}")
        return explicit

    origin_head = git(["symbolic-ref", "--short", "refs/remotes/origin/HEAD"], repo, check=False)
    if origin_head.returncode == 0:
        candidate = origin_head.stdout.strip()
        if candidate and rev_exists(repo, candidate):
            return candidate

    for candidate in ("origin/main", "origin/master", "main", "master", "trunk"):
        if rev_exists(repo, candidate):
            return candidate
    return None


def has_uncommitted(repo: Path) -> bool:
    return bool(git_output(["status", "--porcelain", "--untracked-files=all"], repo))


def has_base_diff(repo: Path, base: str | None) -> bool:
    if not base:
        return False
    result = git(["diff", "--quiet", f"{base}...HEAD"], repo, check=False)
    if result.returncode == 1:
        return True
    if result.returncode == 0:
        return False
    fallback = git(["diff", "--quiet", base], repo, check=False)
    return fallback.returncode == 1


def choose_mode(args: argparse.Namespace, repo: Path, base: str | None) -> tuple[str, str]:
    if args.commit:
        return "commit", f"commit {args.commit}"
    if args.mode == "uncommitted":
        return "uncommitted", "explicit uncommitted mode"
    if args.mode == "base":
        if not base:
            raise ReviewError("Base mode needs --base or a detectable main/master branch")
        return "base", f"explicit base mode against {base}"

    dirty = has_uncommitted(repo)
    branch_diff = has_base_diff(repo, base)
    if dirty:
        return "uncommitted", "dirty worktree detected"
    if branch_diff:
        return "base", f"branch diff detected against {base}"
    return "none", "no uncommitted or base-branch diff detected"


def build_codex_command(
    codex_bin: str,
    args: argparse.Namespace,
    mode: str,
    base: str | None,
) -> list[str]:
    command = [codex_bin, "review"]

    if mode == "commit":
        command.extend(["--commit", args.commit])
    elif mode == "uncommitted":
        command.append("--uncommitted")
    elif mode == "base":
        if not base:
            raise ReviewError("Base mode selected without a base branch")
        command.extend(["--base", base])
    else:
        raise ReviewError("No reviewable changes found")

    if args.reasoning_effort:
        command.extend(["-c", f'model_reasoning_effort="{args.reasoning_effort}"'])
    if args.web_search:
        command.extend(["--enable", "web_search_cached"])
    if args.prompt:
        command.append(args.prompt)
    return command


def parse_gate(output: str) -> dict[str, Any]:
    priorities = re.findall(r"\[P([0-3])\]", output)
    critical = sum(1 for item in priorities if item in {"0", "1"})
    return {
        "gate": "fail" if critical else "pass",
        "critical_findings": critical,
        "findings": len(priorities),
        "priorities": priorities,
    }


def write_report(
    repo: Path,
    command: list[str],
    metadata: dict[str, Any],
    stdout: str,
    stderr: str,
) -> Path:
    stamp = now().strftime("%Y%m%d-%H%M%S")
    safe_repo = re.sub(r"[^A-Za-z0-9_.-]+", "-", repo.name).strip("-") or "repo"
    report_dir = REPORT_ROOT / f"{stamp}-{safe_repo}"
    report_dir.mkdir(parents=True, exist_ok=True)

    metadata_path = report_dir / "metadata.json"
    stdout_path = report_dir / "review.md"
    stderr_path = report_dir / "stderr.txt"

    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    stderr_path.write_text(stderr, encoding="utf-8")

    rendered_command = " ".join(shlex.quote(part) for part in command)
    lines = [
        "# Codex Auto Review",
        "",
        f"- created_at: {metadata['created_at']}",
        f"- repo: {repo}",
        f"- mode: {metadata['mode']}",
        f"- base: {metadata.get('base') or 'n/a'}",
        f"- commit: {metadata.get('commit') or 'n/a'}",
        f"- gate: {metadata['gate']}",
        f"- findings: {metadata['findings']}",
        f"- critical_findings: {metadata['critical_findings']}",
        f"- command: `{rendered_command}`",
        "",
        "## Codex Output",
        "",
        stdout.strip() or "(empty output)",
        "",
    ]
    stdout_path.write_text("\n".join(lines), encoding="utf-8")
    return report_dir


def record_result(metadata: dict[str, Any]) -> None:
    append_jsonl(
        EVENT_LOG,
        {
            "id": new_id("evt"),
            "created_at": now_iso(),
            "kind": "codex_auto_review",
            "payload": metadata,
        },
    )
    append_jsonl(
        OBSERVATIONS,
        {
            "id": new_id("obs"),
            "created_at": now_iso(),
            "source": "codex_auto_review",
            "tag": "automation",
            "text": (
                "Codex auto review "
                f"{metadata['gate']} for {metadata['repo']} "
                f"({metadata['mode']}, findings={metadata['findings']}, report={metadata['report_dir']})."
            ),
        },
    )


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Codex auto review and archive a gate report.")
    parser.add_argument("--repo", default=".", help="Target git repo path.")
    parser.add_argument("--base", default="", help="Base branch/rev for branch review.")
    parser.add_argument("--commit", default="", help="Review a single commit SHA.")
    parser.add_argument("--mode", choices=["auto", "base", "uncommitted"], default="auto")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="Custom review instructions.")
    parser.add_argument("--timeout", type=int, default=300, help="Codex review timeout in seconds.")
    parser.add_argument("--reasoning-effort", default="xhigh", help="Codex reasoning effort config.")
    parser.add_argument("--no-web-search", action="store_true", help="Skip cached web search feature.")
    parser.add_argument("--dry-run", action="store_true", help="Print target command without running Codex.")
    parser.add_argument("--no-record", action="store_true", help="Skip Jarvis observation/event recording.")
    parser.add_argument("--no-fail-on-findings", action="store_true", help="Exit 0 even when P0/P1 findings exist.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    args.web_search = not args.no_web_search

    try:
        codex_bin = shutil.which("codex")
        if not codex_bin:
            raise ReviewError("Codex CLI not found. Install it with: npm install -g @openai/codex")

        repo = resolve_repo(Path(args.repo).expanduser().resolve())
        base = detect_base(repo, args.base or None)
        mode, reason = choose_mode(args, repo, base)
        command = build_codex_command(codex_bin, args, mode, base)
        rendered_command = " ".join(shlex.quote(part) for part in command)

        if args.dry_run:
            print("Codex auto-review dry run")
            print(f"- repo: {repo}")
            print(f"- mode: {mode}")
            print(f"- reason: {reason}")
            print(f"- base: {base or 'n/a'}")
            print(f"- command: {rendered_command}")
            return 0

        result = subprocess.run(command, cwd=str(repo), text=True, capture_output=True, timeout=args.timeout)
        gate = parse_gate(result.stdout)
        metadata = {
            "created_at": now_iso(),
            "repo": str(repo),
            "mode": mode,
            "reason": reason,
            "base": base,
            "commit": args.commit or None,
            "command": command,
            "codex_returncode": result.returncode,
            **gate,
        }
        report_dir = write_report(repo, command, metadata, result.stdout, result.stderr)
        metadata["report_dir"] = str(report_dir)
        (report_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        if not args.no_record:
            record_result(metadata)

        print("Codex auto-review complete")
        print(f"- gate: {metadata['gate']}")
        print(f"- findings: {metadata['findings']}")
        print(f"- critical_findings: {metadata['critical_findings']}")
        print(f"- report: {report_dir}")

        if result.returncode != 0:
            return result.returncode
        if metadata["gate"] == "fail" and not args.no_fail_on_findings:
            return 2
        return 0
    except subprocess.TimeoutExpired:
        print(f"Codex review timed out after {args.timeout}s", file=sys.stderr)
        return 124
    except ReviewError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
