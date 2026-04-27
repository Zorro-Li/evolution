# Durable Rules

## 2026-04-26 - voice

- Rule: Use direct positive claims. Put the answer first and keep context useful.
- Reason: Workspace instruction.

## 2026-04-26 - execution

- Rule: For implementation requests, inspect the local workspace, make the smallest complete change, and verify it with a command.
- Reason: Codex should act as a local execution agent.

## 2026-04-26 - evolution

- Rule: Capture explicit user corrections as feedback and promote repeated corrections into durable rules.
- Reason: Jarvis improves through operational memory.

## 2026-04-26 - execution

- Rule: 网页抓取任务优先使用 Computer Use 实际访问页面；替代抓取方式需要用户确认
- Reason: fb_ddba73353c correction

## 2026-04-27 - evolution

- Rule: 每次 self-evolution 运行对比 latest 与 previous snapshot，仅上报有意义的 profile/rule 变化
- Reason: automation: compare self-memory snapshots

## 2026-04-27 - behavior

- Rule: 思考和规划问题时按五个部分输出：核心目标、需求、规则、用户参与方式、落实计划；落实计划必须拆成 to-do list。
- Reason: 用户明确给出后续思考框架

## 2026-04-28 - behavior

- Rule: 在任务开始时主动判断是否适用已安装 Skill；涉及产品想法/是否值得做/计划评审优先考虑 garrytan/gstack 的 office-hours、plan-ceo-review、plan-eng-review、design-review、qa、review 等；涉及商业模式、对标、内容、执行力、概念拆解优先走 DBS/dontbesilent 路由。
- Reason: 用户明确要求必须学会判断 Skill 使用，并掌握 garryten Skill 与 DBS。

## 2026-04-28 - behavior

- Rule: AI 产品宣发、用户痛点和竞品调研优先把 Twitter/X 作为一线信息源；公开网页、官方文档、HN/Reddit 作为交叉验证来源。
- Reason: 用户明确指出 X 是全球最大、多语种 AI 宣传平台，后续调研要优先搜索。

## 2026-04-28 - behavior

- Rule: X/Twitter 调研中，如果 API 不可用、额度不足或结果不足，优先使用 Computer Use 实际访问 X/Twitter 页面读取和核验证据。
- Reason: 用户明确纠正：x api 做不到就用 computer use 自己去读。
