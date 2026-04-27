#!/usr/bin/env python3
"""Generate and publish the daily Jarvis evolution snapshot."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, time
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
TZ = ZoneInfo("Asia/Shanghai")
DEFAULT_REPO_URL = "git@github.com:Zorro-Li/evolution.git"

TRACKED_PATHS = [
    ".gbrain-source",
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "SOUL.md",
    "USER.md",
    "daily",
    "evals",
    "evolution",
    "inbox",
    "jarvis.py",
    "jarvis.yaml",
    "memory",
    "prompts",
    "runs",
    "scripts",
    "tasks",
]


def run(cmd: list[str], *, check: bool = False) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check and result.returncode != 0:
        print(result.stdout, end="")
        raise SystemExit(result.returncode)
    return result


def today_local() -> str:
    return datetime.now(TZ).date().isoformat()


def now_local() -> str:
    return datetime.now(TZ).isoformat(timespec="seconds")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                rows.append(json.loads(stripped))
    return rows


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=TZ)
    return parsed.astimezone(TZ)


def rows_for_date(rows: list[dict[str, Any]], date: str) -> list[dict[str, Any]]:
    start = datetime.combine(datetime.fromisoformat(date).date(), time.min, TZ)
    end = datetime.combine(datetime.fromisoformat(date).date(), time.max, TZ)
    matched: list[dict[str, Any]] = []
    for row in rows:
        timestamp = row.get("created_at") or row.get("updated_at") or row.get("completed_at")
        parsed = parse_dt(timestamp)
        if parsed and start <= parsed <= end:
            matched.append(row)
    return matched


def compact(text: str, limit: int = 260) -> str:
    cleaned = " ".join(str(text).split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 3] + "..."


def rules_for_date(date: str) -> list[str]:
    path = ROOT / "memory" / "rules.md"
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: list[str] = []
    current: list[str] = []
    in_section = False
    for line in lines:
        if line.startswith("## "):
            if current:
                sections.append("\n".join(current).strip())
            in_section = line.startswith(f"## {date} ")
            current = [line] if in_section else []
        elif in_section:
            current.append(line)
    if current:
        sections.append("\n".join(current).strip())
    return sections


def latest_matching(pattern: str) -> str:
    matches = sorted(ROOT.glob(pattern))
    if not matches:
        return "none"
    return str(matches[-1].relative_to(ROOT))


def section_from_rows(title: str, rows: list[dict[str, Any]], text_key: str = "text") -> list[str]:
    lines = [f"## {title}", ""]
    if not rows:
        lines.append("- none")
        return lines
    for row in rows:
        identifier = row.get("id", "unknown")
        tag = row.get("tag") or row.get("area") or row.get("priority") or "general"
        text = compact(row.get(text_key, ""))
        lines.append(f"- `{identifier}` [{tag}] {text}")
    return lines


def build_report(date: str, refresh_output: str, self_check_output: str) -> Path:
    feedback = rows_for_date(read_jsonl(ROOT / "inbox" / "feedback.jsonl"), date)
    observations = rows_for_date(read_jsonl(ROOT / "inbox" / "observations.jsonl"), date)
    tasks_today = rows_for_date(read_jsonl(ROOT / "tasks" / "tasks.jsonl"), date)
    done_tasks = [row for row in tasks_today if row.get("status") == "done"]
    open_tasks = [row for row in read_jsonl(ROOT / "tasks" / "tasks.jsonl") if row.get("status") == "open"]
    promoted_rules = rules_for_date(date)

    lines = [
        f"# Daily Evolution - {date}",
        "",
        f"Generated: {now_local()}",
        "",
        "## Today Learned",
        "",
    ]
    if feedback or observations or promoted_rules or done_tasks:
        if feedback:
            lines.extend(f"- Correction: {compact(row.get('text', ''))}" for row in feedback)
        if promoted_rules:
            for section in promoted_rules:
                rule_lines = [line for line in section.splitlines() if line.startswith("- Rule:")]
                if rule_lines:
                    lines.append(f"- Rule promoted: {compact(rule_lines[0].removeprefix('- Rule:').strip())}")
        if observations:
            lines.extend(f"- Observation: {compact(row.get('text', ''))}" for row in observations[-8:])
        if done_tasks:
            lines.extend(f"- Task completed: {compact(row.get('text', ''))}" for row in done_tasks)
    else:
        lines.append("- No new Jarvis learning events were captured today.")

    lines.extend(["", *section_from_rows("Corrections", feedback)])
    lines.extend(["", *section_from_rows("Observations", observations[-12:])])
    lines.extend(["", "## Promoted Rules", ""])
    if promoted_rules:
        for section in promoted_rules:
            rule_lines = [line for line in section.splitlines() if line.startswith("- Rule:") or line.startswith("- Reason:")]
            lines.extend(rule_lines or [compact(section)])
    else:
        lines.append("- none")

    lines.extend(["", "## Tasks", ""])
    if done_tasks:
        for row in done_tasks:
            lines.append(f"- done `{row.get('id')}` {compact(row.get('text', ''))}")
    else:
        lines.append("- done: none")
    if open_tasks:
        for row in sorted(open_tasks, key=lambda item: item.get("priority", "P2"))[:6]:
            lines.append(f"- open `{row.get('id')}` {row.get('priority', 'P1')} {compact(row.get('text', ''))}")
    else:
        lines.append("- open: none")

    lines.extend(
        [
            "",
            "## Generated Artifacts",
            "",
            f"- reflection: `{latest_matching(f'runs/{date}-reflection.md')}`",
            f"- proposal: `{latest_matching(f'evolution/proposals/{date}-proposal.md')}`",
            f"- self-memory snapshot: `{latest_matching('evolution/self_memory/*/self_profile.md')}`",
            "",
            "## Verification",
            "",
            "```text",
            compact(self_check_output, 1200),
            "```",
            "",
            "## Self-Memory Refresh",
            "",
            "```text",
            compact(refresh_output, 1200),
            "```",
            "",
        ]
    )

    path = ROOT / "daily" / f"{date}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def ensure_git(repo_url: str, branch: str) -> None:
    if not (ROOT / ".git").exists():
        run(["git", "init"], check=True)
    run(["git", "branch", "-M", branch], check=True)
    remotes = run(["git", "remote"]).stdout.splitlines()
    if "origin" not in remotes:
        run(["git", "remote", "add", "origin", repo_url], check=True)
    else:
        current = run(["git", "remote", "get-url", "origin"]).stdout.strip()
        if current != repo_url:
            run(["git", "remote", "set-url", "origin", repo_url], check=True)


def commit_snapshot(date: str, repo_url: str, branch: str) -> bool:
    ensure_git(repo_url, branch)
    existing = [path for path in TRACKED_PATHS if (ROOT / path).exists()]
    run(["git", "add", "--", *existing], check=True)
    diff = run(["git", "diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        print("No changes to commit.")
        return False
    run(["git", "commit", "-m", f"chore: daily evolution {date}"], check=True)
    return True


def publish(args: argparse.Namespace) -> int:
    date = args.date or today_local()

    reflect = run([sys.executable, "jarvis.py", "reflect", "--days", "1", "--date", date])
    if reflect.returncode != 0:
        print(reflect.stdout, end="")
        return reflect.returncode

    if args.skip_self_memory_refresh:
        refresh_output = "skipped"
    else:
        refresh = run([sys.executable, "scripts/evolve_self_memory.py", "--print-summary"])
        refresh_output = refresh.stdout

    self_check = run([sys.executable, "jarvis.py", "self-check"])
    report_path = build_report(date, refresh_output, self_check.stdout)
    print(f"Wrote {report_path.relative_to(ROOT)}")
    if self_check.returncode != 0:
        print(self_check.stdout, end="")
        return self_check.returncode

    changed = commit_snapshot(date, args.repo_url, args.branch)
    if args.push:
        push = run(["git", "push", "-u", args.remote, args.branch])
        print(push.stdout, end="")
        if push.returncode != 0:
            return push.returncode
    elif changed:
        print("Snapshot committed locally. Push skipped.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Publish the daily Jarvis evolution snapshot.")
    parser.add_argument("--date", default="", help="YYYY-MM-DD; defaults to Asia/Shanghai today")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--push", action="store_true", help="push to GitHub after committing")
    parser.add_argument("--skip-self-memory-refresh", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    return publish(build_parser().parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
