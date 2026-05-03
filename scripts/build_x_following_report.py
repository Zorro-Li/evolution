#!/usr/bin/env python3
"""Build a category report from the X following registry."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


CATEGORY_ORDER = [
    "AI_CORE",
    "US_STOCKS_MACRO",
    "CRYPTO_WEB3",
    "PRODUCT_GROWTH",
    "OTHER",
]

CATEGORY_NOTES = {
    "AI_CORE": "AI labs, model researchers, agent builders, AI infra, AI product builders.",
    "US_STOCKS_MACRO": "US stocks, macro, global capital markets, semiconductors, equity research.",
    "CRYPTO_WEB3": "Crypto, DeFi, wallets, exchanges, Web3 funds, prediction markets.",
    "PRODUCT_GROWTH": "Founders, GTM, growth, indie products, creator business.",
    "OTHER": "Lifestyle, art, generic accounts, unclear or weakly related accounts.",
}


def parse_registry(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pattern = re.compile(r"^\|\s*(\d+)\s*\|\s*(@[^| ]+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*(.*?)\s*\|\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        row, handle, name, category, reason = match.groups()
        rows.append(
            {
                "row": row.strip(),
                "handle": handle.strip(),
                "name": name.strip(),
                "category": category.strip(),
                "reason": reason.strip(),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["row", "handle", "name", "category", "reason"])
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| Row | Handle | Name | Reason |",
        "|---:|---|---|---|",
    ]
    for row in rows:
        reason = row["reason"].replace("|", "/")
        name = row["name"].replace("|", "/")
        lines.append(f"| {row['row']} | `{row['handle']}` | {name} | {reason} |")
    return lines


def write_report(path: Path, rows: list[dict[str, str]], registry: Path, csv_path: Path) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["category"]].append(row)

    counts = Counter(row["category"] for row in rows)
    total = len(rows)
    now = datetime.now().astimezone().isoformat(timespec="seconds")

    lines: list[str] = [
        "# X Following Category Report",
        "",
        f"Generated: {now}",
        f"Source registry: `{registry}`",
        f"CSV export: `{csv_path}`",
        f"Total following accounts classified: {total}",
        "",
        "## Executive Summary",
        "",
        "| Category | Count | Share | Definition |",
        "|---|---:|---:|---|",
    ]
    for category in CATEGORY_ORDER:
        count = counts.get(category, 0)
        share = f"{count / total:.1%}" if total else "0.0%"
        lines.append(f"| {category} | {count} | {share} | {CATEGORY_NOTES.get(category, '')} |")

    focus = grouped.get("AI_CORE", []) + grouped.get("US_STOCKS_MACRO", [])
    lines.extend(
        [
            "",
            "## Priority Watch Scope",
            "",
            f"- AI_CORE + US_STOCKS_MACRO: {len(focus)} accounts",
            "- These are the primary accounts for the current X creator watch task.",
            "- CRYPTO_WEB3 is large and can be processed as a separate market/crypto watchlist.",
            "- PRODUCT_GROWTH is useful for GTM, founder, and creator-business signal.",
            "",
            "## Full Category Lists",
            "",
        ]
    )

    for category in CATEGORY_ORDER:
        category_rows = grouped.get(category, [])
        lines.extend(
            [
                f"### {category} ({len(category_rows)})",
                "",
                CATEGORY_NOTES.get(category, ""),
                "",
            ]
        )
        lines.extend(markdown_table(category_rows))
        lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build report from X following registry.")
    parser.add_argument("--registry", default="runs/x-creator-watch/2026-05-02/00_following_registry.md")
    parser.add_argument("--out", default="runs/x-creator-watch/2026-05-02/06_following_category_report.md")
    parser.add_argument("--csv", default="runs/x-creator-watch/2026-05-02/06_following_category_report.csv")
    args = parser.parse_args()

    registry = Path(args.registry)
    rows = parse_registry(registry)
    if not rows:
        raise SystemExit(f"No registry rows found in {registry}")

    csv_path = Path(args.csv)
    report_path = Path(args.out)
    write_csv(csv_path, rows)
    write_report(report_path, rows, registry, csv_path)
    print(f"wrote {report_path}")
    print(f"wrote {csv_path}")
    print(f"rows {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
