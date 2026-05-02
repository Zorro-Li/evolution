---
type: automation-rule
title: X Creator Distillation Automation
created_at: '2026-05-02T00:00:00.000Z'
tags:
  - automation
  - creators
  - jarvis
  - skills
  - twitter
  - x
---

# X Creator Distillation Automation

User instruction: run a daily long-term task that uses Safari with the logged-in X account soro to inspect the following list, focus on AI creators and US-related bloggers, archive accessible tweets, analyze what each creator does and why they are strong, and distill reusable workflows into skills.

Operating setup:

- Codex cron: daily-x-creator-distillation.
- Schedule: daily at 09:30 Asia/Shanghai.
- Workspace: /Users/lizongru/codex/进化.
- Skill: /Users/lizongru/.codex/skills/x-creator-distiller/SKILL.md.
- Runbook: automation/x-creator-watch.md.
- Output root: runs/x-creator-watch/YYYY-MM-DD/.
- Escalation email: zongru001103@gmail.com.

Required daily outputs:

- following registry
- source ledger
- creator analysis
- tweet/archive data when accessible
- skill distillation
- optional installed creator skill under /Users/lizongru/.codex/skills/x-creator-<handle>/
- compact GBrain synthesis
- Jarvis observation

Escalation rule: stop at official X API, payment, API key, credit-card, identity-verification, or account-approval pages, leave Safari open, create an escalation note, and email zongru001103@gmail.com with URL, reason, required action, and local run path.
