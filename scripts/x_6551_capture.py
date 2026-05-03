#!/usr/bin/env python3
"""Capture X/Twitter creator profile and recent tweets through the 6551 API.

The script intentionally uses only endpoints currently available in the local
opentwitter skill:
- /open/twitter_user_info
- /open/twitter_search with fromUser
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any


BASE_URL = "https://ai.6551.io"
SOURCE_METHOD = "6551 twitter_search/fromUser"


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def handle_slug(handle: str) -> str:
    return handle.strip().lstrip("@").replace("/", "_")


def normalize_handle(handle: str) -> str:
    value = handle.strip()
    if not value:
        raise ValueError("empty handle")
    return value if value.startswith("@") else f"@{value}"


def parse_created_at(value: str | None) -> str | None:
    if not value:
        return None
    try:
        return parsedate_to_datetime(value).isoformat()
    except (TypeError, ValueError):
        return None


def post_json(token: str, endpoint: str, payload: dict[str, Any], timeout: int = 40) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}{endpoint}",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            parsed = None
        return {
            "success": False,
            "http_status": exc.code,
            "error": parsed.get("error") if isinstance(parsed, dict) else raw or str(exc),
            "raw_error": parsed if isinstance(parsed, dict) else raw,
        }
    except urllib.error.URLError as exc:
        return {
            "success": False,
            "error": str(exc.reason),
        }

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "non_json_response",
            "raw": raw,
        }


def load_registry(path: Path, categories: set[str] | None) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    row_re = re.compile(r"^\|\s*(\d+)\s*\|\s*(@[^| ]+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*(.*?)\s*\|\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = row_re.match(line)
        if not match:
            continue
        row, handle, name, category, reason = match.groups()
        category = category.strip()
        if categories and category not in categories:
            continue
        rows.append(
            {
                "row": row.strip(),
                "handle": normalize_handle(handle),
                "name": name.strip(),
                "category": category,
                "reason": reason.strip(),
            }
        )
    return rows


def parse_skip_roots(values: list[str] | None) -> list[Path]:
    roots: list[Path] = []
    for value in values or []:
        for item in value.split(","):
            item = item.strip()
            if item:
                roots.append(Path(item))
    return roots


def exists_in_skip_roots(handle: str, roots: list[Path]) -> bool:
    slug = handle_slug(handle)
    return any((root / "handles" / slug).exists() for root in roots)


def build_targets(args: argparse.Namespace) -> list[dict[str, str]]:
    by_handle: dict[str, dict[str, str]] = {}
    categories = set(args.categories.split(",")) if args.categories else None

    if args.registry:
        for row in load_registry(Path(args.registry), categories):
            by_handle[row["handle"].lower()] = row

    if args.handles:
        for handle in re.split(r"[\s,]+", args.handles.strip()):
            if not handle:
                continue
            normalized = normalize_handle(handle)
            key = normalized.lower()
            by_handle.setdefault(
                key,
                {
                    "row": "",
                    "handle": normalized,
                    "name": "",
                    "category": "MANUAL",
                    "reason": "manual handle input",
                },
            )

    skip_roots = parse_skip_roots(args.skip_existing_run)
    targets = [
        row
        for row in by_handle.values()
        if args.force or not exists_in_skip_roots(row["handle"], skip_roots)
    ]
    if args.offset:
        targets = targets[args.offset :]
    if args.limit:
        targets = targets[: args.limit]
    return targets


def normalize_profile(handle: str, category: str, reason: str, response: dict[str, Any], captured_at: str) -> dict[str, Any]:
    data = response.get("data") if isinstance(response.get("data"), dict) else {}
    return {
        "captured_at": captured_at,
        "source": "6551 twitter_user_info",
        "handle": handle_slug(handle),
        "profile_url": f"https://x.com/{handle_slug(handle)}",
        "category": category,
        "registry_reason": reason,
        "user_id": data.get("userId"),
        "screen_name": data.get("screenName"),
        "name": data.get("name"),
        "description": data.get("description"),
        "followers_count": data.get("followersCount"),
        "following_count": data.get("friendsCount"),
        "statuses_count": data.get("statusesCount"),
        "verified": data.get("verified"),
        "profile_image_url": data.get("profileImageUrl"),
        "api_success": response.get("success"),
        "api_usage": response.get("usage"),
        "api_error": response.get("error"),
    }


def classify_tweet(item: dict[str, Any]) -> str:
    if item.get("isReply"):
        return "reply"
    if item.get("isQuote"):
        return "quote"
    if item.get("isRetweet"):
        return "retweet"
    return "post"


def normalize_tweet(handle: str, item: dict[str, Any], captured_at: str) -> dict[str, Any]:
    tw_id = str(item.get("id") or "")
    return {
        "id": tw_id,
        "url": f"https://x.com/{handle_slug(handle)}/status/{tw_id}" if tw_id else None,
        "captured_at": captured_at,
        "date": parse_created_at(item.get("createdAt")),
        "created_at_raw": item.get("createdAt"),
        "post_type": classify_tweet(item),
        "text": item.get("text"),
        "language": item.get("language"),
        "metrics": {
            "reposts": item.get("retweetCount"),
            "likes": item.get("favoriteCount"),
            "replies": item.get("replyCount"),
            "views": item.get("viewCount"),
        },
        "handle": item.get("userScreenName") or handle_slug(handle),
        "name": item.get("userName"),
        "user_id": item.get("userIdStr"),
        "followers_count": item.get("userFollowers"),
        "verified": item.get("userVerified"),
        "conversation_id": item.get("conversationId"),
        "reply_id": item.get("replyId"),
        "quote_id": item.get("quoteId"),
        "mentions": item.get("mentions"),
        "source_method": SOURCE_METHOD,
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_profile_md(path: Path, profile: dict[str, Any]) -> None:
    lines = [
        f"# @{profile['handle']} Profile",
        "",
        f"- Name: {profile.get('name') or ''}",
        f"- Handle: `@{profile['handle']}`",
        f"- X URL: `https://x.com/{profile['handle']}`",
        f"- Category: {profile.get('category') or ''}",
        f"- Bio: {profile.get('description') or ''}",
        f"- Followers: {profile.get('followers_count')}",
        f"- Following: {profile.get('following_count')}",
        f"- Posts: {profile.get('statuses_count')}",
        f"- Verified: {profile.get('verified')}",
        f"- Capture method: 6551 API",
        f"- Captured: {profile.get('captured_at')}",
        "",
        "## Registry Reason",
        "",
        profile.get("registry_reason") or "",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def capture_target(args: argparse.Namespace, token: str, target: dict[str, str]) -> dict[str, Any]:
    captured_at = now_local_iso()
    handle = target["handle"]
    username = handle_slug(handle)
    handle_dir = Path(args.run_dir) / "handles" / username
    raw_dir = handle_dir / "raw"

    if handle_dir.exists() and not args.force:
        return {
            "handle": handle,
            "category": target.get("category"),
            "status": "skipped_exists",
            "tweets": None,
            "dir": str(handle_dir),
        }

    profile_response = post_json(token, "/open/twitter_user_info", {"username": username})
    search_payload: dict[str, Any] = {
        "fromUser": username,
        "maxResults": args.max_results,
        "product": args.product,
        "excludeReplies": args.exclude_replies,
        "excludeRetweets": args.exclude_retweets,
    }
    if args.since_date:
        search_payload["sinceDate"] = args.since_date
    if args.until_date:
        search_payload["untilDate"] = args.until_date

    search_response = post_json(token, "/open/twitter_search", search_payload)

    write_json(raw_dir / "profile_response.json", profile_response)
    write_json(raw_dir / "search_response.json", search_response)

    profile = normalize_profile(handle, target.get("category", ""), target.get("reason", ""), profile_response, captured_at)
    write_json(raw_dir / "profile_snapshot.json", profile)
    write_profile_md(handle_dir / "profile.md", profile)

    data = search_response.get("data")
    raw_tweets = data if isinstance(data, list) else []
    if args.exclude_replies:
        raw_tweets = [item for item in raw_tweets if not item.get("isReply")]
    if args.exclude_retweets:
        raw_tweets = [item for item in raw_tweets if not item.get("isRetweet")]
    tweets = [normalize_tweet(handle, item, captured_at) for item in raw_tweets[: args.max_results]]
    write_jsonl(raw_dir / "tweets.jsonl", tweets)

    return {
        "handle": handle,
        "category": target.get("category"),
        "status": "ok" if profile_response.get("success") and search_response.get("success") else "api_error",
        "profile_success": profile_response.get("success"),
        "search_success": search_response.get("success"),
        "profile_error": profile_response.get("error"),
        "search_error": search_response.get("error"),
        "tweets": len(tweets),
        "dir": str(handle_dir),
        "usage": {
            "profile": profile_response.get("usage"),
            "search": search_response.get("usage"),
        },
    }


def write_ledger(run_dir: Path, results: list[dict[str, Any]], args: argparse.Namespace) -> None:
    path = run_dir / "6551_capture_ledger.md"
    total_tweets = sum(row.get("tweets") or 0 for row in results)
    lines = [
        "# 6551 X Capture Ledger",
        "",
        f"Captured: {now_local_iso()}",
        f"Endpoint base: `{BASE_URL}`",
        f"Profile endpoint: `/open/twitter_user_info`",
        f"Tweet endpoint: `/open/twitter_search` with `fromUser`",
        f"Product: `{args.product}`",
        f"Max results per handle: `{args.max_results}`",
        f"Total handles in invocation: {len(results)}",
        f"Total normalized tweets: {total_tweets}",
        "",
        "## Results",
        "",
        "| Handle | Category | Status | Tweets | Output | Error |",
        "|---|---|---|---:|---|---|",
    ]
    for row in results:
        errors = "; ".join(str(item) for item in [row.get("profile_error"), row.get("search_error")] if item)
        output = row.get("dir", "")
        lines.append(
            f"| `{row.get('handle')}` | {row.get('category') or ''} | {row.get('status')} | {row.get('tweets') or 0} | `{output}` | {errors} |"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture X creators through 6551 API.")
    parser.add_argument("--registry", help="Markdown registry file to read handles from.")
    parser.add_argument("--handles", help="Comma or whitespace separated handles.")
    parser.add_argument("--categories", default="AI_CORE,US_STOCKS_MACRO", help="Registry categories to include.")
    parser.add_argument("--run-dir", default=f"runs/x-creator-watch/{datetime.now().date().isoformat()}")
    parser.add_argument(
        "--skip-existing-run",
        action="append",
        help="Run directory whose handles/<handle> outputs should be skipped. Can be repeated or comma separated.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Limit target count after offset.")
    parser.add_argument("--offset", type=int, default=0, help="Skip N selected targets.")
    parser.add_argument("--max-results", type=int, default=20, help="Local max tweets to retain per handle.")
    parser.add_argument("--product", default="Latest", choices=["Latest", "Top"])
    parser.add_argument("--since-date", help="YYYY-MM-DD")
    parser.add_argument("--until-date", help="YYYY-MM-DD")
    parser.add_argument("--include-replies", action="store_false", dest="exclude_replies", help="Keep replies.")
    parser.add_argument("--include-retweets", action="store_false", dest="exclude_retweets", help="Keep retweets.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing handle output.")
    parser.add_argument("--dry-run", action="store_true", help="Print selected handles and exit.")
    parser.add_argument("--no-stop-on-quota", action="store_false", dest="stop_on_quota", help="Continue after HTTP 402 quota errors.")
    parser.add_argument("--sleep", type=float, default=0.25, help="Seconds between handles.")
    args = parser.parse_args()

    targets = build_targets(args)
    if not targets:
        print("No targets selected.", file=sys.stderr)
        return 2

    if args.dry_run:
        for target in targets:
            print(f"{target['handle']}\t{target.get('category','')}\t{target.get('name','')}")
        return 0

    token = os.environ.get("TWITTER_TOKEN")
    if not token:
        print("TWITTER_TOKEN is required.", file=sys.stderr)
        return 2

    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    for index, target in enumerate(targets, start=1):
        print(f"[{index}/{len(targets)}] capturing {target['handle']}", file=sys.stderr)
        result = capture_target(args, token, target)
        results.append(result)
        quota_error = result.get("profile_error") == "insufficient quota" or result.get("search_error") == "insufficient quota"
        if args.stop_on_quota and quota_error:
            print("Stopping after insufficient quota response from 6551.", file=sys.stderr)
            break
        if args.sleep and index < len(targets):
            time.sleep(args.sleep)

    write_ledger(run_dir, results, args)
    errors = [row for row in results if row.get("status") == "api_error"]
    print(json.dumps({"handles": len(results), "errors": len(errors), "run_dir": str(run_dir)}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
