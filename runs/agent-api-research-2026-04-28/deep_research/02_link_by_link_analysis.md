# 02 逐链接分析报告

日期：2026-04-28  
目的：逐个分析资料台账中的关键链接，拆解“他们怎么做这项工作”

## 1. OpenAI

### S01 / S02：API 数据使用与数据控制

链接：

- https://openai.com/policies/api-data-usage-policies/
- https://platform.openai.com/docs/models/how-we-use-your-data/

他们怎么做：

- 将 API / business 数据和消费级产品数据分开说明。
- 强调 API 输入输出默认排除训练。
- 提供企业隐私、安全、合规和数据控制选项。
- 对数据保留、abuse monitoring、ZDR 等能力做分层。

可参考做法：

- 我们需要把 `raw prompt`、`agent trace`、`billing metadata` 分开定义。
- 默认承诺用户输入输出排除训练。
- 提供 ZDR 或 Local Audit 作为隐私敏感用户入口。

### S03：Prompt Caching

链接：https://platform.openai.com/docs/guides/prompt-caching

他们怎么做：

- 将缓存作为 API 原生能力，用户可以通过返回字段看到 cached tokens。
- 价值表达聚焦成本和延迟。
- 机制层面关注 prefix 复用，适合长上下文、多轮任务。

可参考做法：

- 我们的报告必须显示 `重复上下文`、`可缓存前缀`、`缓存命中失败`。
- Benchmark 输出中加入 cached token 和 billable token。

### S04：Business Terms

链接：https://openai.com/en-US/policies/business-terms/

他们怎么做：

- 通过商业条款定义客户内容、输出使用、责任限制、赔偿和服务边界。
- 对高风险使用、用户责任、合规义务做条款化。

可参考做法：

- 试点协议需要写清：用户负责审核输出，用户负责备份，破坏性操作需要确认。
- 责任上限和间接损失排除要进入 V0 合同草案。

### S05 / S06：Codex

链接：

- https://openai.com/codex
- https://platform.openai.com/docs/codex/overview

他们怎么做：

- 把 Codex 包装成 cloud software engineering agent。
- 支持代码任务、PR、review、CLI / cloud workflow。
- 核心用户是开发者和工程团队。

可参考做法：

- 我们的 ICP 可以直接围绕 Codex / Claude Code 高频用户。
- Token Audit 报告可以按 coding task trace 设计。

## 2. Anthropic / Claude Code

### S07 / S08：Claude Code 数据使用与合规

链接：

- https://docs.anthropic.com/en/docs/claude-code/data-usage
- https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance

他们怎么做：

- 按个人、商业、API key、ZDR 等场景说明数据保留。
- 说明 Claude Code 可能收集的反馈、transcripts、usage 数据。
- 对企业合规和区域可用性做专门页面。

可参考做法：

- 我们需要按 Local Audit、BYOK Proxy、Hosted API 三种路径写数据流。
- 每种路径都写：哪些数据进入服务器、保存多久、谁能访问、能否删除。

### S09：Anthropic Prompt Caching

链接：https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching

他们怎么做：

- 将长上下文 prompt 拆成可缓存部分和新请求部分。
- 显示 cache write 与 cache read 的不同成本。
- 明确适用场景：长文档、多轮对话、工具使用、agent workflow。

可参考做法：

- 我们可以把“长任务 agent 成本下降”拆成 cache write、cache read、重复上下文减少三块。
- 用户报告里给出 cache-read 机会，而非只给总节省比例。

### S10：Anthropic Commercial Terms

链接：https://www.anthropic.com/legal/commercial-terms

他们怎么做：

- 把客户内容、输出、使用责任、服务限制、责任限制写成商业条款。
- 对模型输出的准确性和适用性保留用户审核义务。

可参考做法：

- 我们的 Hosted API 需要清楚区分：优化建议、模型输出、实际执行动作。
- 试点协议应将“执行动作”放在用户确认后发生。

### S42 / S43：Claude Code 产品与 Agentic Coding

链接：

- https://claude.com/product/claude-code
- https://claude.com/blog/introduction-to-agentic-coding

他们怎么做：

- 宣传重点是自然语言驱动 coding workflow。
- 强调 terminal、IDE、GitHub、long-running task。
- 用“agentic coding”教育市场。

可参考做法：

- 我们不需要教育用户什么是 Agent，需要接住已有 Claude Code 用户。
- 访谈问题直接围绕“最近一次长任务怎么跑、哪里烧钱、哪里失败”。

## 3. 云平台：AWS / Google

### S11：AWS Bedrock Data Protection

链接：https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html

他们怎么做：

- 直接承诺 customer content 用于模型调用，不用于训练。
- 强调 prompts / completions 不分发给模型提供方。
- 通过 IAM、KMS、VPC、CloudTrail 等云安全体系承接企业信任。

可参考做法：

- 企业版本需要“子处理方披露 + 加密 + audit log + 最小权限”。
- 当前阶段用 AWS 级别承诺作参照，先在文档里写清我们能做到的范围。

### S12 / S13：Google Vertex AI / Gemini Context Caching

链接：

- https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance
- https://ai.google.dev/gemini-api/docs/caching/

他们怎么做：

- 将数据治理、训练用途、缓存、日志、企业设置放在官方文档里。
- Context caching 作为长上下文复用机制。

可参考做法：

- 我们需要把 context cache 从“技术点”变成“账单优化项”。
- Benchmark 里给出：缓存前成本、缓存后成本、缓存命中条件。

## 4. Cursor / GitHub Copilot

### S14 / S15 / S16：Cursor Security / Enterprise / Background Agents

链接：

- https://cursor.com/security/
- https://cursor.com/enterprise
- https://docs.cursor.com/en/background-agents

他们怎么做：

- 用 Privacy Mode、SOC 2、模型商 ZDR、团队管理承接企业信任。
- 透明说明 prompt-building、code indexing 等流程。
- Background Agents 让 coding task 后台运行，强化 agent 工作流。

可参考做法：

- 我们需要承认服务端参与优化层，并明确每一步数据去向。
- 对企业用户，Privacy Mode / ZDR / audit log 是必备语言。

### S17 / S18：GitHub Copilot Trust Center / Privacy

链接：

- https://docs.github.com/en/copilot/reference/copilot-trust-center
- https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement

他们怎么做：

- 把 Copilot 的数据处理、安全、合规、企业控制集中到 Trust Center。
- 用官方统一页面降低采购和安全审查成本。

可参考做法：

- 我们也需要一个 `Trust & Privacy` 单页，覆盖训练、保留、删除、子处理方、责任边界。

## 5. AI Infra / Gateway / Observability

### S19 / S20：Helicone

链接：

- https://docs.helicone.ai/getting-started/platform-overview
- https://docs.helicone.ai/features/advanced-usage/caching

他们怎么做：

- 定位为 LLM observability + AI gateway。
- 功能包括 tracing、cost tracking、prompt management、caching、rate limits、agent debugging。
- 入口通常是 SDK / proxy，价值是看见成本和调试问题。

可参考做法：

- 我们可以借用 gateway 心智，但早期聚焦 Token Audit。
- 报告里输出 trace-level cost attribution，而非只做 dashboard。

### S21：Portkey AI Gateway

链接：https://portkey.ai/docs/product/ai-gateway

他们怎么做：

- 统一多模型 API gateway。
- 提供 routing、fallback、cache、retries、budget、observability。
- 面向生产环境 LLM app。

可参考做法：

- BYOK Proxy 可以学习 Portkey 的功能分层。
- 我们的差异在长任务 agent trace 优化，避免变成通用 gateway。

### S22 / S23：LiteLLM Proxy

链接：

- https://docs.litellm.ai/docs/proxy/virtual_keys
- https://docs.litellm.ai/docs/proxy/caching

他们怎么做：

- 开源 proxy 统一 100+ LLM API。
- 支持 virtual keys、budget、rate limits、routing、cache。
- 自带 self-hosted 心智。

可参考做法：

- 开源 proxy 是强替代方案。
- 我们需要提供 audit、recommendation、workflow-specific optimization，而非只做代理。

### S24 / S25：LangSmith

链接：

- https://docs.langchain.com/oss/python/langchain/observability
- https://www.langchain.com/langsmith

他们怎么做：

- 核心是 tracing、observability、evaluation、deployment feedback。
- 关注 agent runs、tool calls、latency、token usage、quality。
- 面向工程团队和 AI app 团队。

可参考做法：

- 我们的 Token Audit 应该输出 trace tree：哪一步烧钱、哪一步可缓存、哪一步模型太贵。
- 质量评估要和成本评估并列，避免“省钱导致输出变差”。

### S26：Braintrust AI Observability

链接：https://www.braintrust.dev/articles/best-ai-observability-tools-2026

他们怎么做：

- 用 observability / eval / prompt management 的框架描述市场。
- 强调调试、评估、监控、实验。

可参考做法：

- 我们的市场定位属于 observability + optimization 的交叉，不属于纯 prompt caching。

## 6. 直接竞品与 X/Twitter 信号

### S27 / S28：Compresr

链接：

- https://compresr.ai/docs/gateway
- https://x.com/ycombinator/status/2026811140010045847

他们怎么做：

- 定位为 long context reduction / compression。
- 通过 agentic proxy 接入 Claude Code / OpenClaw / agent workflow。
- YC 用“better accuracy, cost, latency”和“Make every token count”宣传。

可参考做法：

- 直接竞品已经占据“long context compression”心智。
- 我们更适合从 Token Audit 切入，先告诉用户哪里浪费，再给 optimization layer。

### S29：OpenClaw Cost Optimization Playbook

链接：https://x.com/PrajwalTomar_/status/2027387894399422775

他们怎么做：

- 用真实账单开头：每天 35-40 美元，月化超过 1000 美元。
- 给出 65-70% 成本下降。
- 方法拆成 model tiering、QMD 本地搜索、session memory compact、thinking token 控制、本地模型、免费搜索、OpenRouter auto-route、便宜 heartbeat。

可参考做法：

- 这是最好的宣传模板：先讲账单，再讲设置，再讲节省。
- 我们可以把这些变成 audit checklist。

### S30 / S31：Token Usage Dashboard

链接：

- https://x.com/nyk_builderz/status/2028722212375761311
- https://x.com/tom_doerr/status/2022061117434896721

他们怎么做：

- 展示 Claude Code session stats、token usage、subscription-aware cost display。
- 做本地 dashboard，无需 gateway。

可参考做法：

- Local Audit 的第一版可以是 CLI + markdown report。
- 后续做 dashboard 也有市场信号。

### S32 / S33：Claude Code Compact 讨论

链接：

- https://x.com/berryxia/status/2039342944797577583
- https://x.com/HiTw93/status/2045629549577371814

他们怎么做：

- 社区拆解 compact pipeline：MicroCompact、Session Memory Compact、Legacy Compact。
- 用户通过环境变量调整 compact window。

可参考做法：

- 用户已经理解 compact 语言。
- Optimization Report 可以给 compact threshold 建议。

### S34：Hermes.md 计费异常事件

链接：https://x.com/Teknium/status/2048576507786956973

他们怎么做：

- 社区公开讨论命名/提交历史触发额外计费。
- Anthropic 通过退款和 credits 修复信任。

可参考做法：

- 我们需要异常账单检测。
- 条款中写清计费异常处理和 refund policy。

### S35 / S36：大众化 Token Efficiency 宣发

链接：

- https://x.com/RoundtableSpace/status/2036408939126907066
- https://x.com/boltdotnew/status/1848822514090446962

他们怎么做：

- 用“use less tokens”“reduce token usage & code truncation issues”作为公开卖点。
- 面向大众 AI 用户和产品更新。

可参考做法：

- Token usage 可以公开讲。
- 开发者受众需要更具体：账单、trace、缓存、路由、compact。

## 7. PDF / 文件 SaaS 信任机制

### S37 / S38 / S41：CloudConvert

链接：

- https://cloudconvert.com/privacy
- https://cloudconvert.com/security
- https://cloudconvert.com/terms

他们怎么做：

- 明确文件保留期：处理文件可手动删除，最晚短期删除。
- 日志保留期单独说明。
- 安全页讲加密、认证、基础设施。
- 条款中强调用户文件、责任边界和服务限制。

可参考做法：

- 我们的 prompt / trace 也要写保留期和手动删除。
- 日志保留期与 raw prompt 保留期分开。

### S39：Smallpdf

链接：https://smallpdf.com/support

他们怎么做：

- 用“一小时删除”“GDPR/CCPA/ISO 27001”等语言降低上传焦虑。
- 帮用户快速理解文件安全。

可参考做法：

- 我们可以提供“默认 24 小时删除 raw trace，metadata 保留 30 天”的简单文案。

### S40：iLovePDF

链接：https://www.ilovepdf.com/help/security

他们怎么做：

- 明确处理后两小时内删除文件。
- 强调 TLS、加密和用户删除。

可参考做法：

- 对 Local Audit 外的 Hosted API，短留存是最直接信任机制。

## 8. Devin 企业产品

### S44：Devin Enterprise

链接：https://docs.devin.ai/enterprise/get-started

他们怎么做：

- 把 AI software engineer 包装成企业级产品。
- 关注组织接入、权限、任务管理和企业安全。

可参考做法：

- 这类产品证明企业愿意为 agent 工作流付费。
- 当前团队阶段适合先服务开发者和小团队，等案例充分后再走企业。

## 9. 逐链接分析结论

| 方法 | 谁在做 | 他们怎么做 | 我们参考什么 |
|---|---|---|---|
| 数据排除训练 | OpenAI、Anthropic、AWS、Cursor | 明确 API / enterprise 数据不进训练 | 默认承诺输入输出排除训练 |
| ZDR / 短留存 | OpenAI、Anthropic、Cursor、PDF SaaS | 分层数据保留，企业可 ZDR | Local Audit、BYOK、Hosted 分层 |
| Prompt/context caching | OpenAI、Anthropic、Google | 原生缓存，降低成本和延迟 | 把缓存机会写进 Token Audit |
| Gateway | Portkey、Helicone、LiteLLM、Compresr | 统一模型入口、路由、cache、budget | BYOK Proxy 学习 gateway 能力 |
| Observability | LangSmith、Helicone、Braintrust | trace、tool calls、cost、eval | 输出 trace-level cost attribution |
| Compact | Claude Code 社区、OpenClaw 社区 | 裁剪工具输出、session memory、阈值配置 | 给 compact threshold 建议 |
| Model routing | Portkey、OpenRouter、OpenClaw 用户 | 简单任务走便宜模型，复杂任务走强模型 | Audit 报告标注模型浪费 |
| Local mode | Mission Control、OpenClaw dashboard | 本地读 session stats 和 token usage | 立项前优先做 Local Audit |
| 责任边界 | OpenAI、Anthropic、CloudConvert | 用户审核、备份、责任上限、间接损失排除 | 写试点条款 |

