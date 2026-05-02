# Ancestral Agent Knowledge Base Expansion

Date: 2026-05-02
Owner: Codex
Risk: Low

## Goal

完善 `ancestral-agent-workflow` Skill，把中国古籍、史籍、历史故事、寓言故事、成语故事、隐性知识/默会知识理论转化成一套可复用的 AI/Agent 工作法知识库。

## Acceptance Criteria

- Skill 入口保留轻量导航，详细知识进入 `references/`。
- 知识库覆盖古籍来源地图、隐性知识理论、故事到 Agent 模式映射、100 条核心总结、词单。
- 推特“隐性知识/默会知识”讨论转化成 Agent 设计方法，并保留可追溯链接。
- 本地安装目录 `/Users/lizongru/.codex/skills/ancestral-agent-workflow` 同步更新。
- 通过 Skill quick validation，且目标文件无 Markdown 占位符。

## Context Checked

- `skills/ancestral-agent-workflow/SKILL.md`
- `skills/ancestral-agent-workflow/references/rulebook.md`
- `skills/ancestral-agent-workflow/references/doc-template.md`
- `/Users/lizongru/.codex/skills/.system/skill-creator/SKILL.md`
- `git status -sb`
- `TWITTER_TOKEN` presence for X/Twitter search

## Source Notes

- Chinese Text Project: `https://ctext.org/`
- Chinese Text Project Library: `https://ctext.org/library.pl?if=en`
- Stanford Encyclopedia of Philosophy, know-how: `https://plato.stanford.edu/entries/knowledge-how/`
- X/Twitter examples:
  - `https://x.com/dontbesilent/status/2040834122168545788`
  - `https://x.com/dontbesilent/status/2046539549120369044`
  - `https://x.com/howie_serious/status/1981201523301634427`
  - `https://x.com/wangray/status/2040630983742107847`
  - `https://x.com/immersivetran/status/2013854732398535073`
  - `https://x.com/TradercBTC/status/1998276577285812412`
  - `https://x.com/knowledgefxg/status/1927024504133271755`

## Plan

1. 更新 Skill 入口，增加知识库导航。
2. 新增古籍来源地图，覆盖经史子集、史籍、兵家、法家、道家、墨家、寓言成语和历史故事。
3. 新增隐性知识/默会知识理论，将其转为 Agent 的上下文、示例、反馈和师承机制。
4. 新增故事到 Agent 工作流映射。
5. 提炼 100 条核心总结，并据此生成词单。
6. 同步本地 Skill，运行验证，提交并推送。

## Decisions

- 详细知识放入 `references/`，保持 `SKILL.md` 可快速加载。
- 使用“来源 -> 隐性逻辑 -> Agent 行为 -> 触发条件 -> 失败模式”的结构，方便 Agent 在任务中检索和套用。
- 将“隐性知识”处理为可表达但尚未结构化的经验，将“默会知识”处理为需要示例、反馈、观察和复盘才能稳定迁移的经验。
- 把成语故事当作压缩过的失败案例和执行原则，服务任务设计、风险识别、协作规范和复盘。

## Changes

- `skills/ancestral-agent-workflow/SKILL.md`: 增加知识库导航和触发描述。
- `skills/ancestral-agent-workflow/references/knowledge-base-index.md`: 新增知识库索引。
- `skills/ancestral-agent-workflow/references/classical-source-map.md`: 新增古籍和故事来源地图。
- `skills/ancestral-agent-workflow/references/tacit-knowledge-theory.md`: 新增隐性知识/默会知识到 Agent 设计的转化框架。
- `skills/ancestral-agent-workflow/references/story-to-agent-patterns.md`: 新增历史故事、寓言、成语到 Agent 工作流的映射。
- `skills/ancestral-agent-workflow/references/core-100.md`: 新增 100 条核心总结。
- `skills/ancestral-agent-workflow/references/lexicon.md`: 新增词单。

## Risks

- 古籍材料范围很大：用来源地图和模式表覆盖高频可迁移素材，后续可继续扩充专门主题。
- 推特讨论会随时间变化：保留 tweet URL 和当前检索时间语境。
- 过度堆砌典故会降低 Agent 可执行性：每条材料都落到 Agent 行为和失败模式。

## Validation

```bash
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ancestral-agent-workflow
python3 /Users/lizongru/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lizongru/.codex/skills/ancestral-agent-workflow
python3 - <<'PY'
from pathlib import Path
for p in [Path('skills/ancestral-agent-workflow/references/core-100.md'), Path('/Users/lizongru/.codex/skills/ancestral-agent-workflow/references/core-100.md')]:
    nums=[int(line[:3]) for line in p.read_text().splitlines() if len(line)>=4 and line[:3].isdigit() and line[3]=='.']
    print(p, len(nums), nums[:1], nums[-1:])
PY
rg -n "TODO|\[TODO\]" skills/ancestral-agent-workflow /Users/lizongru/.codex/skills/ancestral-agent-workflow
git diff --check -- skills/ancestral-agent-workflow ai-docs/agent-workflow/2026-05-02-ancestral-agent-knowledge-base.md
```

Result:

```text
Skill is valid!
Installed Skill is valid!
core-100.md count: 100 locally and 100 in installed Skill.
Placeholder scan: no matches.
git diff --check: clean.
```

## Rollback

- `git revert <commit>` 可恢复本次知识库扩展。

## Follow-ups

- 可继续把每个典故扩展成独立案例卡，加入正例、反例、Prompt 模板和验收清单。
