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

## 2026-04-28 - behavior

- Rule: 调研型任务执行三步走并留痕：1) 原始资料台账，记录所有找到的内容和链接；2) 逐链接分析，说明每个对象怎么做、证据是什么；3) 综合报告，总结方法、对应公司、可参考做法和建议。
- Reason: 用户明确纠正：调研必须像员工一样工作，中间步骤也要留存文档。

## 2026-05-02 - behavior

- Rule: 每次复杂任务开始前，先用 gbrain search 检索本地上下文；每次对话产生可复用的研究方案、复盘、技能蒸馏或重要决策时，用 gbrain put 写入本地知识库。
- Reason: 用户明确要求 Codex 自己加入 Jarvis 进化流程

## 2026-05-02 - behavior

- Rule: 每天 23:50 自动运行 daily_evolution_publish.py --push，把新获取的 Jarvis 资料和 GBrain markdown 导出提交并推送到 GitHub。
- Reason: 用户明确要求每天自动上传新获取资料到 GitHub，尤其是 GBrain

## 2026-05-02 - behavior

- Rule: X/Twitter 创作者研究任务每天优先用 Computer Use 操作 Safari 的 soro 登录态，从关注列表增量覆盖 AI 与美国相关博主；每个创作者产出来源台账、推文归档、强项拆解、skill 蒸馏和 GBrain 入库；API、付款、密钥和身份验证步骤停在官方页面并邮件升级给用户处理。
- Reason: 用户明确提出长期进化任务

## 2026-05-02 - behavior

- Rule: 查公司、公司调研、竞品分析、尽调、行业/财务/新闻侧公司研究任务，优先使用本地 /Users/lizongru/codex/进化/tools/company-research-agent，并先检索 gbrain slug company-research-agent-tool 获取运行方式。
- Reason: 用户明确要求安装 company-research-agent 并在查公司时使用
