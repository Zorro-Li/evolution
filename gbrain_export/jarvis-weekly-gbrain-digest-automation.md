---
type: automation
title: Jarvis Weekly GBrain Digest Automation
created_at: '2026-05-02'
tags:
  - automation
  - gbrain
  - jarvis
  - weekly-digest
---

# Jarvis Weekly GBrain Digest Automation

Purpose: summarize all GBrain pages updated in the last 7 days and save the weekly digest back into GBrain.

Implemented files:

- `/Users/lizongru/codex/进化/scripts/weekly_gbrain_digest.py`
- `/Users/lizongru/codex/进化/automation/com.lizongru.jarvis.weekly-gbrain-digest.plist`
- `/Users/lizongru/codex/进化/runs/gbrain_weekly/2026-05-02-weekly-gbrain-digest.md`

Runtime behavior:

- Runs `gbrain list --limit 500`.
- Filters pages updated in the last 7 days.
- Reads each page with `gbrain get`.
- Builds a Markdown digest grouped by page type.
- Writes the local report to `runs/gbrain_weekly/`.
- Saves the same report as `weekly-gbrain-digest-YYYY-MM-DD` using `gbrain put`.

Schedule:

- macOS launchd label: `com.lizongru.jarvis.weekly-gbrain-digest`
- Time: every Monday at 09:10 local time.

Verification:

- `python3 -m py_compile scripts/weekly_gbrain_digest.py`
- `python3 scripts/weekly_gbrain_digest.py`
- `gbrain get weekly-gbrain-digest-2026-05-02`
- `launchctl print gui/501/com.lizongru.jarvis.weekly-gbrain-digest`

Related pages: [[jarvis-gbrain-evolution-rule]], [[weekly-gbrain-digest-2026-05-02]], [[workspace-readme]]
