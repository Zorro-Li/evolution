# Crypto History As Mirror Skill Notes

Date: 2026-05-02

## Goal

Turn `/Users/lizongru/Downloads/华语币圈经典2010-2024全集by刘明卖星星的人.pdf` into a durable "以史为鉴" Skill for crypto history, boom-bust analysis, rug-risk analogies, cycle positioning, and project due diligence.

## Created Skill

Repository path: `/Users/lizongru/codex/进化/skills/crypto-history-as-mirror`

Local install path: `/Users/lizongru/.codex/skills/crypto-history-as-mirror`

Files:
- `SKILL.md`: trigger, source stack, workflow, output format.
- `references/pdf-knowledge-map.md`: detailed PDF knowledge map with page anchors and domain tags.
- `references/crypto-rise-fall-2010-2024.md`: 2010-2024 crypto rise-fall cycle narrative.
- `references/due-diligence-playbook.md`: fast and deep analysis templates.
- `agents/openai.yaml`: UI metadata and default prompt.

## Boundary Correction

User clarified this is separate from the "老祖宗祖训扩展到 AI/Agent" Skill. This Skill now only covers crypto history, cycle analysis, historical analogies, rug-risk lessons, and due diligence.

Separated folder:

```text
skills/crypto-history-as-mirror
```

The AI/Agent workflow Skill lives separately:

```text
skills/ancestral-agent-workflow
```

## Updated Companion Skill

Path: `/Users/lizongru/.codex/skills/crypto-rug-analysis/SKILL.md`

Change:
- Added a cross-reference to `$crypto-history-as-mirror` for full cycle history and PDF knowledge-base work.

## Core Use

Prompt:

```text
Use $crypto-history-as-mirror to analyze <project/topic> through crypto history, boom-bust patterns, and rug-risk lessons.
```

Output target:
- Historical position
- Rise driver
- Decline trigger
- Closest analogs
- Incentive skeleton
- Evidence gaps
- Execution recommendation

## Notes

The root path `/ai-docs` was read-only in this environment, so this durable note was saved under the workspace path `ai-docs/crypto/`.

## Validation

```bash
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lizongru/codex/进化/skills/crypto-history-as-mirror
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lizongru/.codex/skills/crypto-history-as-mirror
```
