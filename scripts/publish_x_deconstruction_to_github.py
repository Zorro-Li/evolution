#!/usr/bin/env python3
"""Publish X creator deconstruction outputs to GitHub.

Default behavior stages public-safe deconstruction artifacts only:
- run-level Markdown / CSV reports
- per-handle profile.md, analysis.md, skill.md

Raw tweet/API archives remain local unless --include-raw is provided.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_EXTRA_PATHS = [
    "automation/x-creator-watch.md",
    "scripts/x_6551_capture.py",
    "scripts/build_x_following_report.py",
    "scripts/publish_x_deconstruction_to_github.py",
]


def run(cmd: list[str], *, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        check=check,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def git_root() -> Path:
    result = run(["git", "rev-parse", "--show-toplevel"], capture=True)
    return Path(result.stdout.strip())


def current_branch() -> str:
    result = run(["git", "branch", "--show-current"], capture=True)
    branch = result.stdout.strip()
    if not branch:
        raise SystemExit("Cannot publish from a detached HEAD.")
    return branch


def ensure_remote(remote: str) -> None:
    result = run(["git", "remote"], capture=True)
    remotes = {line.strip() for line in result.stdout.splitlines() if line.strip()}
    if remote not in remotes:
        raise SystemExit(f"Git remote `{remote}` does not exist.")


def existing_staged_files() -> list[str]:
    result = run(["git", "diff", "--cached", "--name-only"], capture=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def public_run_files(run_dir: Path) -> list[Path]:
    files: list[Path] = []
    files.extend(sorted(run_dir.glob("*.md")))
    files.extend(sorted(run_dir.glob("*.csv")))
    for handle_dir in sorted((run_dir / "handles").glob("*")):
        if not handle_dir.is_dir():
            continue
        for name in ("profile.md", "analysis.md", "skill.md"):
            path = handle_dir / name
            if path.exists():
                files.append(path)
    return files


def raw_run_files(run_dir: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in ("**/*.json", "**/*.jsonl", "**/*.tsv", "**/*.html"):
        files.extend(sorted(run_dir.glob(pattern)))
    return files


def normalize_existing(paths: list[str], root: Path) -> list[Path]:
    existing: list[Path] = []
    for value in paths:
        path = Path(value)
        if not path.is_absolute():
            path = root / path
        if path.exists():
            existing.append(path)
    return existing


def rel(path: Path, root: Path) -> str:
    return str(path.resolve().relative_to(root.resolve()))


def chunked(values: list[str], size: int = 100) -> list[list[str]]:
    return [values[index : index + size] for index in range(0, len(values), size)]


def stage(paths: list[str]) -> None:
    for batch in chunked(paths):
        run(["git", "add", "--", *batch])


def staged_summary() -> str:
    result = run(["git", "diff", "--cached", "--stat"], capture=True)
    return result.stdout.strip()


def has_staged_changes() -> bool:
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Commit and push X creator deconstruction outputs.")
    parser.add_argument("--run-dir", default="runs/x-creator-watch/2026-05-02")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default=None)
    parser.add_argument("--message", default=None)
    parser.add_argument("--include-raw", action="store_true", help="Also upload raw JSON/JSONL/HTML exports.")
    parser.add_argument("--no-extra-paths", action="store_true", help="Skip automation/scripts from the commit.")
    parser.add_argument("--extra-path", action="append", default=[], help="Additional path to include.")
    parser.add_argument("--allow-existing-staged", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-push", action="store_true")
    args = parser.parse_args()

    root = git_root()
    run_dir = (root / args.run_dir).resolve()
    if not run_dir.exists():
        raise SystemExit(f"Run directory does not exist: {run_dir}")

    ensure_remote(args.remote)
    branch = args.branch or current_branch()

    staged_before = existing_staged_files()
    if staged_before and not args.allow_existing_staged:
        raise SystemExit(
            "Existing staged changes detected. Commit or unstage them first, or pass --allow-existing-staged.\n"
            + "\n".join(staged_before)
        )

    candidates = public_run_files(run_dir)
    if args.include_raw:
        candidates.extend(raw_run_files(run_dir))
    if not args.no_extra_paths:
        candidates.extend(normalize_existing(DEFAULT_EXTRA_PATHS, root))
    candidates.extend(normalize_existing(args.extra_path, root))

    rel_paths = sorted({rel(path, root) for path in candidates if path.exists()})
    if not rel_paths:
        print("No publishable files found.")
        return 0

    print(f"Selected {len(rel_paths)} files for GitHub publish.")
    for path in rel_paths[:80]:
        print(path)
    if len(rel_paths) > 80:
        print(f"... {len(rel_paths) - 80} more files")

    if args.dry_run:
        return 0

    stage(rel_paths)
    if not has_staged_changes():
        print("No staged changes to commit.")
        return 0

    print(staged_summary())
    message = args.message or f"Publish X creator deconstruction outputs: {run_dir.name}"
    run(["git", "commit", "-m", message])
    if not args.no_push:
        run(["git", "push", args.remote, branch])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
