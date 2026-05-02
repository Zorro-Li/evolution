#!/usr/bin/env python3
"""Generate a weekly GBrain digest and save it back into GBrain."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
TZ = ZoneInfo("Asia/Shanghai")
DEFAULT_LIMIT = 500


@dataclass(frozen=True)
class Page:
    slug: str
    page_type: str
    updated_at: datetime
    title: str


def gbrain_path() -> str:
    candidates = [
        shutil.which("gbrain"),
        str(Path.home() / ".bun" / "bin" / "gbrain"),
        "/opt/homebrew/bin/gbrain",
        "/usr/local/bin/gbrain",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise SystemExit("gbrain executable was not found")


def run_gbrain(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PATH"] = os.pathsep.join(
        [
            str(Path.home() / ".bun" / "bin"),
            "/opt/homebrew/bin",
            "/usr/local/bin",
            env.get("PATH", ""),
        ]
    )
    result = subprocess.run(
        [gbrain_path(), *args],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check and result.returncode != 0:
        print(result.stdout, end="")
        raise SystemExit(result.returncode)
    return result


def now_local() -> datetime:
    return datetime.now(TZ)


def parse_gbrain_date(value: str, reference: datetime) -> datetime | None:
    try:
        parsed = datetime.strptime(f"{value} {reference.year}", "%a %b %d %Y")
    except ValueError:
        return None
    parsed = parsed.replace(tzinfo=TZ)
    if parsed.date() > reference.date() + timedelta(days=1):
        parsed = parsed.replace(year=reference.year - 1)
    return parsed


def list_pages(limit: int, reference: datetime) -> list[Page]:
    output = run_gbrain(["list", "--limit", str(limit)]).stdout
    pages: list[Page] = []
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        slug, page_type, updated_text, title = parts[0], parts[1], parts[2], parts[3]
        updated_at = parse_gbrain_date(updated_text, reference)
        if updated_at:
            pages.append(Page(slug=slug, page_type=page_type, updated_at=updated_at, title=title))
    return pages


def strip_frontmatter(content: str) -> str:
    if not content.startswith("---\n"):
        return content
    end = content.find("\n---", 4)
    if end == -1:
        return content
    return content[end + 4 :].lstrip()


def extract_tags(content: str) -> list[str]:
    if not content.startswith("---\n"):
        return []
    end = content.find("\n---", 4)
    if end == -1:
        return []
    tags: list[str] = []
    in_tags = False
    for line in content[4:end].splitlines():
        stripped = line.strip()
        if stripped == "tags:":
            in_tags = True
            continue
        if in_tags and stripped.startswith("- "):
            tags.append(stripped[2:].strip().strip('"\''))
            continue
        if in_tags and stripped and not stripped.startswith("- "):
            in_tags = False
    return tags


def first_lines(content: str, limit: int = 3) -> list[str]:
    body = strip_frontmatter(content)
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("---"):
            continue
        lines.append(compact(stripped, 180))
        if len(lines) >= limit:
            break
    return lines


def headings(content: str, limit: int = 4) -> list[str]:
    body = strip_frontmatter(content)
    found: list[str] = []
    for line in body.splitlines():
        match = re.match(r"^#{2,3}\s+(.+)$", line.strip())
        if match:
            found.append(match.group(1).strip())
        if len(found) >= limit:
            break
    return found


def compact(text: str, limit: int = 220) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 3].rstrip() + "..."


def page_content(slug: str) -> str:
    result = run_gbrain(["get", slug], check=False)
    if result.returncode != 0:
        return ""
    return result.stdout


def page_block(page: Page) -> list[str]:
    content = page_content(page.slug)
    tags = extract_tags(content)
    lines = [
        f"- `{page.slug}` ({page.page_type}, {page.updated_at.date().isoformat()}): {page.title}",
    ]
    if tags:
        lines.append(f"  - tags: {', '.join(tags[:8])}")
    page_headings = headings(content)
    if page_headings:
        lines.append(f"  - headings: {', '.join(page_headings)}")
    snippets = first_lines(content)
    if snippets:
        lines.append(f"  - signal: {' / '.join(snippets)}")
    return lines


def build_report(pages: list[Page], start: datetime, end: datetime, scanned_count: int) -> str:
    by_type = Counter(page.page_type for page in pages)
    generated = now_local().isoformat(timespec="seconds")
    report_date = end.date().isoformat()
    lines = [
        "---",
        f'title: "Weekly GBrain Digest - {report_date}"',
        'type: "weekly-digest"',
        f'generated_at: "{generated}"',
        f'period_start: "{start.date().isoformat()}"',
        f'period_end: "{end.date().isoformat()}"',
        "tags:",
        "  - gbrain",
        "  - weekly-digest",
        "  - jarvis",
        "---",
        "",
        f"# Weekly GBrain Digest - {report_date}",
        "",
        f"Period: {start.date().isoformat()} to {end.date().isoformat()}",
        "",
        "## Coverage",
        "",
        f"- Pages scanned: {scanned_count}",
        f"- Pages updated in period: {len(pages)}",
        f"- Type mix: {', '.join(f'{key}={value}' for key, value in sorted(by_type.items())) or 'none'}",
        "",
    ]

    if not pages:
        lines.extend(["## New Knowledge", "", "- No GBrain pages were updated in this period.", ""])
        return "\n".join(lines)

    lines.extend(["## New Knowledge And Technology", ""])
    for page_type in sorted(by_type):
        lines.extend([f"### {page_type}", ""])
        for page in [item for item in pages if item.page_type == page_type]:
            lines.extend(page_block(page))
        lines.append("")

    lines.extend(
        [
            "## Retrieval Commands",
            "",
            "```bash",
            f'gbrain search "weekly digest {report_date}"',
            "gbrain list --limit 50",
            "gbrain stats",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_report(report: str, date_text: str) -> Path:
    out_dir = ROOT / "runs" / "gbrain_weekly"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{date_text}-weekly-gbrain-digest.md"
    path.write_text(report, encoding="utf-8")
    return path


def put_report(report: str, date_text: str) -> None:
    slug = f"weekly-gbrain-digest-{date_text}"
    run_gbrain(["put", slug, "--content", report])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a weekly GBrain digest.")
    parser.add_argument("--date", default="", help="YYYY-MM-DD; defaults to today in Asia/Shanghai")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--no-put", action="store_true", help="write local report only")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    end = datetime.fromisoformat(args.date).replace(tzinfo=TZ) if args.date else now_local()
    start = end - timedelta(days=args.days - 1)
    pages = list_pages(args.limit, end)
    matched = [page for page in pages if start.date() <= page.updated_at.date() <= end.date()]
    matched.sort(key=lambda page: (page.updated_at, page.page_type, page.slug), reverse=True)

    report = build_report(matched, start, end, len(pages))
    path = write_report(report, end.date().isoformat())
    if not args.no_put:
        put_report(report, end.date().isoformat())
    print(f"Wrote {path.relative_to(ROOT)}")
    if not args.no_put:
        print(f"Saved weekly-gbrain-digest-{end.date().isoformat()} to GBrain")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
