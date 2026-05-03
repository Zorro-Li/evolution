---
type: concept
title: X Creator Geekbb Keep Codex Fast 2026 05 03
---

# GBrain Payload: x-creator-geekbb-keep-codex-fast-2026-05-03

Tags: x-creator, codex, local-state, maintenance, jarvis, skill
Source run: `/Users/lizongru/codex/进化/runs/x-creator-watch/2026-05-03`

## Compact Synthesis

`@geekbb` surfaced a high-engagement Codex local-state pain: heavy users accumulate chats, worktrees, logs, and stale config until Codex feels slow. The linked project `vibeforge1111/keep-codex-fast` packages the pain into a backup-first Codex skill with report-only inspection, handoff-first continuity, archive-based cleanup, and post-apply verification.

## Evidence

- X post: https://x.com/geekbb/status/2050786115427402050
- Visible metrics at capture: 5 replies, 40 reposts, 301 likes, 484 bookmarks, 31,519 views.
- GitHub repo: https://github.com/vibeforge1111/keep-codex-fast
- GitHub metadata: 439 stars, MIT license, created 2026-05-02, updated 2026-05-03.
- Reply signal: `.codex/sessions/` and large JSONL files are named by users as concrete slowdown sources.

## Jarvis Lesson

Codex maintenance should be a first-class local workflow:

1. read-only report first
2. handoff docs before archiving important old chats
3. backup before apply
4. archive with manifest and restore path
5. verify with the same report
6. recurring reminders stay report-only

## Installed / Packaged Skill

- Installed local skill: `/Users/lizongru/.codex/skills/codex-state-maintenance/SKILL.md`
- YouMind pack file: `/Users/lizongru/codex/进化/runs/youmind-jarvis-skill-upload-2026-05-03/codex-state-maintenance.md`

## Next Action

Add a Jarvis P1 task to build a local read-only Codex state report before any cleanup command exists. The first implementation should report sizes and candidates only, then generate handoff docs for active repo chats.
