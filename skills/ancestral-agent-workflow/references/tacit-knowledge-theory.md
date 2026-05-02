# 隐性知识与默会知识：Agent 设计框架

## Source Entry Points

- Stanford Encyclopedia of Philosophy, know-how: `https://plato.stanford.edu/entries/knowledge-how/`
- Chinese Text Project: `https://ctext.org/`
- X/Twitter discussion examples:
  - `https://x.com/dontbesilent/status/2040834122168545788`
  - `https://x.com/dontbesilent/status/2046539549120369044`
  - `https://x.com/howie_serious/status/1981201523301634427`
  - `https://x.com/wangray/status/2040630983742107847`
  - `https://x.com/immersivetran/status/2013854732398535073`
  - `https://x.com/TradercBTC/status/1998276577285812412`
  - `https://x.com/knowledgefxg/status/1927024504133271755`

## Three Knowledge Types

| Type | Definition | Agent Encoding |
|---|---|---|
| 显性知识 | 已经写清楚的规则、文档、接口、字段、命令、清单 | README、API docs、tests、schemas、runbooks、prompt rules |
| 隐性知识 | 原则上可以表达，当前存在于经验、习惯、判断、案例和口头传承中 | rubric、checklist、examples、anti-patterns、acceptance criteria、decision records |
| 默会知识 | 高度依赖场景、手感、审美、时机和分寸，难以完整语言化 | demonstrations、shadowing、review comments、side-by-side examples、feedback loops、postmortems |

## Twitter-Derived Understanding

The X/Twitter discussion around "隐性知识库" points to a practical AI problem: models often know public facts, yet lack the user's private operating context, taste, judgment boundaries, and accumulated workflows.

Extracted working principles:

- `dontbesilent`: separates implicit knowledge and tacit knowledge by expressibility. For Agent design, first convert expressible implicit knowledge into documents, then capture tacit judgment through examples and feedback.
- `howie_serious`: points out that effective workflows such as article title writing contain hidden SOPs, experience, thinking, and summaries. For Agent design, every repeated workflow should become a documented playbook with examples.
- `wangray`: emphasizes practice, apprenticeship, and indwelling. For Agent design, memory should include worked examples and review traces, since pure rules miss lived judgment.
- `immersivetran`: highlights observation of experts in real scenes. For Agent design, include real task transcripts, before/after diffs, and critique.
- `TradercBTC`: notes that vague domain concepts cause AI to fill gaps with default assumptions. For Agent design, ambiguous terms require definitions, boundary examples, and pause rules.
- `knowledgefxg`: frames expertise as heavily dependent on hidden knowledge. For Agent design, ask what an expert checks silently before acting.

## Ancient Wisdom Bridge

| Ancient Form | Knowledge Type | Agent Form |
|---|---|---|
| 祖训 | Explicit + implicit | Operating principles and guardrails |
| 师承 | Tacit | Demonstrations, correction loops, review comments |
| 家书 | Implicit | Decision records, tone, standards, values |
| 史鉴 | Implicit | Failure case library and pattern recognition |
| 成语 | Compressed implicit | Trigger phrase for recurring failure modes |
| 寓言 | Scenario-based tacit | Short simulation that exposes judgment |
| 兵法 | Conditional explicit | Strategy rules with terrain, timing, risk |
| 礼制 | Explicit | Roles, permissions, ceremony, handoff |
| 修身 | Tacit + implicit | Self-discipline, honesty, restraint |

## Tacit Knowledge Base Model

An effective Agent knowledge base has five layers:

1. **Context layer**: user goals, domain, stack, vocabulary, constraints, current state.
2. **Rule layer**: mandatory behaviors, permissions, escalation points, forbidden actions.
3. **Example layer**: good outputs, bad outputs, diffs, reviews, before/after edits.
4. **Judgment layer**: tradeoff rules, taste, timing, scope boundaries, risk thresholds.
5. **Memory layer**: task notes, postmortems, durable preferences, repeated corrections.

## Conversion Pipeline

```text
experience -> story -> principle -> trigger -> checklist -> example -> feedback -> memory -> rule
```

| Step | Question | Artifact |
|---|---|---|
| Experience | What did the expert do silently? | Observation note |
| Story | What incident reveals the pattern? | Case card |
| Principle | What rule transfers across tasks? | One-line rule |
| Trigger | When should the Agent remember it? | Trigger phrase |
| Checklist | What should the Agent actually do? | Action list |
| Example | What does good/bad look like? | Paired examples |
| Feedback | How is behavior corrected? | Review comment |
| Memory | Where is it stored? | `ai-docs/`, memory, Skill reference |
| Rule | When stable, how is it promoted? | Skill rule or AGENTS.md rule |

## Agent-As-Colleague Design

Treat the Agent like a capable teammate who needs onboarding:

- Give the same background a human colleague would need.
- Share local conventions, current branch, known risks, decision history, and examples.
- Give ownership boundaries and escalation rules.
- Ask for a plan, acceptance criteria, and rollback on consequential work.
- Require evidence when facts are uncertain.
- Review outcomes, then store corrections in durable memory.

## Hidden Knowledge Capture Prompts

Use these prompts when converting a user's implicit knowledge:

- "What would an expert check before starting?"
- "What mistake has happened before in similar work?"
- "What words in this domain have fuzzy boundaries?"
- "What does a good final answer look like?"
- "What would make this output feel wrong even if technically correct?"
- "What should the Agent do when evidence is missing?"
- "Which action requires explicit approval?"
- "What should be recorded for the next Agent?"
- "What example should future Agents imitate?"
- "What example should future Agents avoid?"

## Failure Modes

| Failure Mode | Description | Countermeasure |
|---|---|---|
| 默认补全 | Agent fills vague gaps from generic patterns | Define terms and require evidence for ambiguous concepts |
| 纸上谈兵 | Rules exist without real validation | Add commands, examples, screenshots, diffs, tests |
| 守株待兔 | Old success becomes rigid rule | Add context and freshness checks |
| 刻舟求剑 | Old marker survives after environment changes | Re-check paths, versions, APIs, state |
| 滥竽充数 | Work appears done because format exists | Tie output to acceptance criteria and verification |
| 画蛇添足 | Extra polish harms a complete task | Stop at acceptance unless user expands scope |
| 三人成虎 | Repeated claims become false certainty | Track original source and confidence |
| 掩耳盗铃 | Risk is hidden by avoiding logs/tests | Run checks and show evidence |

## Promotion Rules

Promote knowledge into durable rules when:

- The user explicitly corrects Agent behavior.
- The same failure appears twice.
- A task requires repeated domain-specific judgment.
- A hidden checklist materially improves quality.
- A missing rule could cause data loss, security exposure, or public mistake.

Keep one-off context as task notes until it repeats or becomes clearly durable.
