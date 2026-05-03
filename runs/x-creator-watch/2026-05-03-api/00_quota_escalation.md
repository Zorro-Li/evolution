# 6551 API Quota Escalation

Run: `runs/x-creator-watch/2026-05-03-api`
Time: 2026-05-03

## Status

The 6551 API token is configured and working, but the current quota is insufficient for continued batch capture.

Working endpoints:

- `POST https://ai.6551.io/open/twitter_user_info`
- `POST https://ai.6551.io/open/twitter_search` with `fromUser`

Observed blocker:

- HTTP `402`
- Error: `insufficient quota`

Token / quota page from local `opentwitter` skill:

- `https://6551.io/mcp`

Safari note:

- Opening `https://6551.io/mcp` encountered site-side routing / Cloudflare behavior in the current browser session.

## Email Draft

To: `zongru001103@gmail.com`

Subject: 6551 API quota needed for X creator watch automation

Body:

The 6551 API integration for the X creator watch is implemented in `/Users/lizongru/codex/进化/scripts/x_6551_capture.py`.

The current token can call profile/search endpoints, but batch capture stopped because 6551 returned HTTP 402 `insufficient quota`.

Please open `https://6551.io/mcp`, upgrade or add quota, then tell Codex to rerun:

```bash
python3 scripts/x_6551_capture.py \
  --registry runs/x-creator-watch/2026-05-02/00_following_registry.md \
  --categories AI_CORE,US_STOCKS_MACRO \
  --skip-existing-run runs/x-creator-watch/2026-05-02 \
  --run-dir runs/x-creator-watch/$(date +%F)-api \
  --limit 50 \
  --max-results 20 \
  --product Latest
```
