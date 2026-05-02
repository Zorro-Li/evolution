# Evolving Jarvis

This workspace turns Codex into a local Jarvis operating layer: rules, memory, tasks, feedback, reflection, and self-checks live in one directory.

## Quick Start

```bash
cd /Users/lizongru/codex/进化
python3 jarvis.py status
python3 jarvis.py boot
```

## Core Commands

```bash
python3 jarvis.py feedback "用户纠正：以后先确认真实技术栈" --tag correction
python3 jarvis.py observe "这个项目当前是空目录，已初始化 Jarvis 层" --tag bootstrap
python3 jarvis.py task "接入 Telegram 入口和本地 agent pull 模型" --priority P1 --area remote-control
python3 jarvis.py reflect
python3 jarvis.py self-check
python3 scripts/evolve_self_memory.py --print-summary
python3 jarvis.py auto-review --repo /path/to/git/repo
python3 scripts/daily_evolution_publish.py --push
```

## Installed Tools

- `tools/gbrain`: GBrain local knowledge brain, with PGLite data in `~/.gbrain/brain.pglite`.
- `tools/gstack`: GStack workflow skills and browser tooling, installed for Codex as `~/.codex/skills/gstack-*`.

Promote stable behavior into durable rules:

```bash
python3 jarvis.py promote "遇到用户纠正技术栈时，立即切换到用户指定的栈继续推进。" --reason "explicit user preference"
```

## Files

- `SOUL.md`: Jarvis identity, voice, taste bar, and operating principles.
- `USER.md`: local user model and collaboration preferences.
- `AGENTS.md`: workspace behavior contract for Codex.
- `jarvis.py`: local CLI for feedback, tasks, reflection, and self-checks.
- `memory/`: durable profile, rules, lessons, and operating state.
- `memory/self_profile.md`: generated local understanding of the user.
- `memory/preferences.md`: generated collaboration preferences.
- `tools/gbrain/`: cloned GBrain source and local CLI runtime.
- `gbrain_export/`: generated markdown export of the local GBrain pages for GitHub backup.
- `tools/gstack/`: cloned GStack source, generated skills, and compiled browser/design/PDF binaries.
- `inbox/`: raw feedback and observations.
- `tasks/`: task ledger.
- `runs/`: generated reflections.
- `prompts/`: boot prompts for future sessions.
- `evolution/`: scorecard, decisions, and evolution log.

## Recommended Routine

Run `python3 jarvis.py status` before meaningful work. After a task with multiple steps, run `python3 jarvis.py reflect` and promote any stable behavior change.

Run `python3 scripts/evolve_self_memory.py --print-summary` to refresh the local Jarvis profile from HumanOS and workspace evidence.

Run `python3 jarvis.py auto-review --repo /path/to/git/repo` to review a dirty worktree or branch diff with Codex, save the report under `runs/codex_auto_review/`, and record the gate result in Jarvis memory.

Run `python3 scripts/daily_evolution_publish.py --push` at the end of each day to export GBrain markdown into `gbrain_export/`, generate `daily/YYYY-MM-DD.md`, refresh Jarvis reflection/self-memory, commit the workspace evolution state, and push it to the private GitHub repository `Zorro-Li/evolution`.

Run `python3 scripts/weekly_gbrain_digest.py` to summarize GBrain pages updated in the last 7 days, write `runs/gbrain_weekly/YYYY-MM-DD-weekly-gbrain-digest.md`, and save the same report back into GBrain.

Install the weekly macOS automation:

```bash
mkdir -p ~/Library/LaunchAgents
cp automation/com.lizongru.jarvis.weekly-gbrain-digest.plist ~/Library/LaunchAgents/
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.lizongru.jarvis.weekly-gbrain-digest.plist
launchctl enable "gui/$(id -u)/com.lizongru.jarvis.weekly-gbrain-digest"
```
