# Agent API 立项前调研报告

日期：2026-04-28  
阶段：立项前调研  
目标：判断“面向长任务 Agent 的 Token 成本优化 API / 加速层”是否值得继续投入

## 1. 结论

建议继续做低成本验证，周期 14 天，目标是拿到真实用户的 Token 账单、长任务失败记录、隐私顾虑和付费意愿。

本次调研包包含四个附件：

- `x_twitter_evidence.md`：Computer Use 实际读取的 X/Twitter 证据。
- `privacy_competitor_matrix.md`：隐私、法律、竞品矩阵。
- `benchmark_protocol.md`：Token 成本优化 benchmark 协议。
- `user_research_plan.md`：用户招募、访谈和评分计划。

当前方向有真实机会，理由是：

- 长任务 Agent 的 Token 成本、上下文重复、计划反复修改、agent trace 成本已经是公开讨论问题。
- OpenAI、Anthropic、Google、AWS 都已经把 prompt/context caching 作为成本优化能力，说明“复用上下文降低成本”是主流方向。
- Helicone、Portkey、LangSmith、LiteLLM 等 AI Infra 产品已经教育市场接受 gateway、observability、routing、cache、budget controls。
- 用户信任门槛很高，产品一旦经过团队服务器，就必须正面解决隐私、日志、误操作、责任边界。

当前最窄切入口：

> Agent Token Audit + Optimization Layer：帮 Claude Code / Codex / 自研 Agent 用户找出 Token 浪费点，并在长任务中压缩重复上下文、提升缓存命中率、降低账单。

这个定位比“新 Agent API”更容易验证，因为用户可以拿当前账单和任务记录直接对比。

## 2. Skill 路由

本次调研按以下 Skill 思路执行：

- GStack / office-hours：判断产品想法是否值得推进，重点看需求真实性、现状替代方案、最窄切口。
- DBS / diagnosis：消解商业问题，重点识别概念陷阱、事实前提和错误假设。
- DBS / benchmark：做竞品对标，拆出可模仿的包装方式、计费方式和信任机制。
- conducting-user-interviews：设计用户访谈，优先收集真实行为故事。
- pricing-strategist：判断 API、包月、自带 Key、托管 Key 的定价变量。
- competitive-strategist：建立竞品分层和对外 positioning。
- opentwitter + Computer Use：优先从 X/Twitter 搜索 AI 宣发、用户痛点和竞品话术；本次 6551 API 返回 `insufficient quota`，已改用 Computer Use 实际打开 X 页面读取搜索结果和具体帖子。

## 3. GStack Office Hours 判断

### 3.1 需求现实

需求成立的用户集中在三类：

| 用户 | 当前行为 | 痛点强度 |
|---|---|---|
| Claude Code / Codex 高频开发者 | 每天长时间跑 coding agent | Token、限额、上下文重复、计划迭代成本 |
| 小团队 AI 工程负责人 | 把 Agent 接入内部流程 | 成本不可控、日志敏感、失败难复盘 |
| AI agency / 自动化服务商 | 给客户交付 agent workflow | 每个客户上下文重复、利润被 API 成本吃掉 |

公开信号：

- Y Combinator 在 X 上宣传 Compresr，卖点是压缩长上下文来提升 LLM 准确率、降低成本和延迟，并强调可接入 Claude Code / OpenClaw / agentic proxy。来源：[Y Combinator on X](https://x.com/ycombinator/status/2026811140010045847)
- X 上的 OpenClaw 成本优化文章记录：默认配置让作者每天花 35-40 美元，调整后同一工作负载成本下降 65-70%，并列出 model tiering、本地搜索、session memory compact、本地模型、auto-route 等方案。来源：[Prajwal Tomar on X](https://x.com/PrajwalTomar_/status/2027387894399422775)
- X 上已有 Claude Code token usage dashboard 产品：本地模式显示 session stats、跨项目 token usage、subscription-aware cost display。来源：[Nyk on X](https://x.com/nyk_builderz/status/2028722212375761311)
- X 上有 AI agent token usage dashboard：用于监控 agent activity 和 token usage，说明成本监控已成为 agent 工具生态的一类需求。来源：[Tom Dorr on X](https://x.com/tom_doerr/status/2022061117434896721)
- X 上的 Claude Code compact 讨论把超长会话拆成 MicroCompact、Session Memory Compact、Legacy Compact，并提到每轮裁剪工具输出可省 5-15K tokens。来源：[Berryxia.AI on X](https://x.com/berryxia/status/2039342944797577583)
- X 上有人分享 Claude Code Max 配置：在 1M context window 的 40% 触发 compact，用于保持长任务速度和上下文。来源：[Tw93 on X](https://x.com/HiTw93/status/2045629549577371814)
- Garry Tan 转发的 Hermes.md 事件显示，Claude Code / Hermes Agent 相关命名触发额外计费，有用户一天损失 200 美元，Anthropic 后续提供退款和 credits。来源：[Teknium on X](https://x.com/Teknium/status/2048576507786956973)
- X 上有针对 AI agent 的“少用 tokens”prompt，强调 token usage visibility、成本优化和质量不下降，浏览量超过 8 万。来源：[0xMarioNawfal on X](https://x.com/RoundtableSpace/status/2036408939126907066)
- bolt.new 曾把减少 token usage 与 code truncation issues 作为 AI agent 升级卖点。来源：[bolt.new on X](https://x.com/boltdotnew/status/1848822514090446962)

判断：需求存在，强度需要通过 10-15 个真实用户访谈确认。公开讨论能证明“大家关心成本”，还需要证明“他们愿意为第三方优化层付费”。

### 3.2 现有替代方案

| 替代方案 | 用户怎么做 | 对我们意味着什么 |
|---|---|---|
| 模型商自带 prompt caching | OpenAI、Anthropic、Google 都有缓存机制 | 单纯“缓存”已经被平台覆盖，需要做跨工具、跨任务、可解释优化 |
| 人工 compact / 总结 | Claude Code `/compact`、手写摘要、减少上下文 | 用户已接受上下文压缩，但人工成本高 |
| LLM gateway | Helicone、Portkey、LiteLLM | Gateway 形态已被市场教育，可以借这个品类表达 |
| Observability | LangSmith、Langfuse、Helicone | 成本可视化是刚需，但优化闭环仍有空间 |
| 自带 API Key | 用户用自己的 OpenAI/Anthropic Key | 隐私信任更容易，体验更复杂 |
| 自建 agent framework | LangGraph、CrewAI、自研编排 | 高级用户可自己做，普通团队需要托管服务 |

### 3.3 最窄切口

当前最适合验证的 offer：

> 给 10 个高频 Agent 用户做一次 Token Audit：接入他们的一段真实长任务 trace，输出 before/after Token footprint、浪费来源、可压缩上下文、缓存命中策略和预估节省金额。

交付形式：

- 一份 Token 消耗报告。
- 一个 SDK / proxy demo。
- 一套最佳实践配置。
- 一段真实任务前后对比视频。

判断：先卖 audit，比先卖 API 更容易收集数据和建立信任。

## 4. DBS 商业诊断

### 4.1 需要消解的问题

原问题容易滑向“要不要成立公司、怎么融资、怎么上线”。当前真正需要回答的是：

> 是否存在一个愿意为了长任务 Agent 成本下降付费的明确用户群。

公司化、融资、股权、正式上线都属于后置变量。当前主线是调研。

### 4.2 关键概念拆解

| 概念 | 可操作定义 | 当前缺口 |
|---|---|---|
| 长任务 | 单任务运行超过 10 分钟，或上下文超过 50k tokens，或调用 20 次以上模型/工具 | 需要真实 trace 样本 |
| Token 成本下降 80% | 在同一任务、同一模型等级、同一质量标准下，总账单下降 80% | 需要 benchmark protocol |
| 任务性能提升 | 成功率、耗时、人工介入次数、返工次数改善 | 需要评估 rubric |
| 用户信任 | 用户愿意让代码/文档/业务上下文经过服务 | 需要隐私条款、架构选项、试点访谈 |
| 技术壁垒 | 竞品复刻成本、数据闭环、优化策略、工作流集成 | 需要从“算法”转为“数据+集成+评估闭环” |

### 4.3 当前事实前提

需要验证的事实：

- 80% 成本下降是否稳定出现在 5 个以上任务类型。
- 成本下降是否来自可复用机制，而非测试样本偶然性。
- 输出质量是否维持，避免“省钱但任务变差”。
- 用户当前账单是否足够痛，个人用户和企业用户分开判断。
- 用户是否愿意为第三方 proxy/API 让渡上下文。

### 4.4 商业判断

当前方向的核心障碍是信任和归因：

- 信任问题：用户会问 Prompt、代码、上下文、日志会在哪里存、存多久、谁能看。
- 归因问题：用户会问节省来自你们的优化，还是模型商 prompt caching 自带能力。
- 责任问题：Agent 误删文件、跑坏数据库、提交错误代码时，用户会问责任归属。

当前策略：

- 调研先以 Token Audit 和本地/自带 Key 版本建立信任。
- API 托管版本作为后续形态。
- 企业版本提供 ZDR、VPC/self-hosted、日志脱敏、危险操作确认。

## 5. 竞品与替代方案

### 5.1 模型商与基础平台

| 产品 | 相关能力 | 信任机制 | 对我们启发 |
|---|---|---|---|
| OpenAI API / Codex | Codex 云端并行 coding agent；API prompt caching | API 数据默认排除训练；企业隐私、SOC 2、加密、ZDR 选项 | 需要提供数据控制、缓存透明度、企业安全说法 |
| Anthropic Claude / Claude Code | 终端/IDE/GitHub agentic coding；prompt caching；ZDR | 商业产品默认排除训练；Claude Code 商业用户标准 30 天保留，ZDR 可用 | Claude Code 用户是最强目标用户之一 |
| Google Vertex AI / Gemini | 上下文缓存、长上下文、ZDR 配置 | Vertex AI 默认训练限制，缓存/日志有清晰保留说明 | 文档要写清每类数据保留期 |
| AWS Bedrock | 模型访问、guardrails、VPC/PrivateLink | 不存储或记录 prompts/completions；不与模型商共享；不用于训练 | 企业客户会期待这一级别的隐私承诺 |

来源：

- OpenAI Enterprise Privacy：[openai.com/policies/api-data-usage-policies](https://openai.com/policies/api-data-usage-policies/)
- OpenAI Business Terms：[openai.com/policies/business-terms](https://openai.com/en-US/policies/business-terms/)
- OpenAI Prompt Caching：[platform.openai.com/docs/guides/prompt-caching](https://platform.openai.com/docs/guides/prompt-caching)
- Anthropic Privacy Center：[privacy.anthropic.com](https://privacy.anthropic.com/en/articles/7996868-i-want-to-opt-out-of-my-prompts-and-results-being-used-for-training-models)
- Anthropic Claude Code data usage：[docs.anthropic.com](https://docs.anthropic.com/es/docs/claude-code/data-usage)
- Anthropic Claude Code legal：[docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance)
- Anthropic prompt caching：[docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- AWS Bedrock data protection：[docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- Google Vertex AI data governance：[cloud.google.com](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance)
- Gemini context caching：[ai.google.dev](https://ai.google.dev/gemini-api/docs/caching/)

### 5.2 Agent 产品

| 产品 | 定位 | 可能竞争点 | 我们的差异机会 |
|---|---|---|---|
| Claude Code | 终端、IDE、GitHub coding agent | 原生上下文理解和 workflow | 面向 Claude Code trace 的成本优化 |
| OpenAI Codex | 云端/本地 coding agent，并行任务 | 自带模型和云环境 | 跨 Codex + Claude + 自研 agent 的成本层 |
| Cursor Agents / Bugbot | IDE 内 agent、background agent、PR review | 已有强用户入口 | 给 Cursor-heavy team 做 token/cost audit |
| Devin | 企业 AI software engineer | 企业交付和安全 | 作为高价企业对标，启发安全与责任边界 |

来源：

- Claude Code product：[claude.com/product/claude-code](https://claude.com/product/claude-code/)
- Claude agentic coding：[claude.com/blog/introduction-to-agentic-coding](https://claude.com/blog/introduction-to-agentic-coding)
- OpenAI Codex：[openai.com/codex](https://openai.com/codex)
- OpenAI Codex overview：[platform.openai.com/docs/codex/overview](https://platform.openai.com/docs/codex/overview)
- Cursor Background Agents：[docs.cursor.com/en/background-agents](https://docs.cursor.com/en/background-agents)
- Cursor Security：[cursor.com/security](https://cursor.com/security/)
- Devin Enterprise：[docs.devin.ai/enterprise/get-started](https://docs.devin.ai/enterprise/get-started)

### 5.3 AI Infra / Gateway / Observability

| 产品 | 对外卖点 | 可模仿点 | 避免点 |
|---|---|---|---|
| Helicone | LLM observability、AI gateway、agent debugging、cost tracking | 直接说 cost tracking、agent debugging、0% markup | 单纯观测会变成 feature，不够尖锐 |
| Portkey | AI Gateway、routing、fallback、cache、budget/rate limits | 用 gateway 类目承接信任 | 需要避免和成熟 gateway 正面拼全功能 |
| LangSmith | tracing、debugging、evaluating、monitoring LLM/agent behavior | 企业会认可 trace + eval | 价格和日志敏感问题会被用户关注 |
| LiteLLM | open-source proxy、budget、routing、fallback | 自带 Key / self-hosted 方向 | 开源替代强，闭源 API 要提供更强结果 |

来源：

- Helicone platform overview：[docs.helicone.ai](https://docs.helicone.ai/getting-started/platform-overview)
- Helicone prompt caching：[docs.helicone.ai](https://docs.helicone.ai/gateway/concepts/prompt-caching)
- Portkey AI Gateway：[portkey.ai/docs/product/ai-gateway](https://portkey.ai/docs/product/ai-gateway)
- LangSmith Observability：[docs.langchain.com](https://docs.langchain.com/oss/python/langchain/observability)

### 5.4 PDF / 文件转换 SaaS 的隐私包装

文件转换 SaaS 适合作为隐私文案参考，因为它们同样要让用户上传敏感文件。

| 产品 | 隐私承诺 | 可借鉴 |
|---|---|---|
| CloudConvert | 文件上传到服务器临时存储，用户可手动删除，最晚 24 小时删除；日志 180 天 | 明确写文件保留期、日志保留期、用户删除权 |
| Smallpdf | 多数工具处理后一小时删除文件，TLS，ISO 27001/GDPR/CCPA | 用短保留期降低焦虑 |
| iLovePDF | 文件处理后两小时内自动永久删除，可手动删除 | 删除时间窗口可以成为信任要素 |

来源：

- CloudConvert Privacy：[cloudconvert.com/privacy](https://cloudconvert.com/privacy)
- CloudConvert Terms：[cloudconvert.com/terms](https://cloudconvert.com/terms)
- CloudConvert Security：[cloudconvert.com/security](https://cloudconvert.com/security)
- Smallpdf Support/Security：[smallpdf.com/support](https://smallpdf.com/support)
- iLovePDF Security：[ilovepdf.com/help/security](https://www.ilovepdf.com/help/security)

## 6. 隐私、法律与责任风险

### 6.1 竞品常见处理方式

| 风险 | 竞品处理 | 我们 V0 文档建议 |
|---|---|---|
| 用户数据训练模型 | 商业/API 数据默认排除训练 | 明确写：用户输入、输出、代码、文档默认排除训练 |
| 数据保留 | 30 天、24 小时、1 小时、ZDR 等分层 | 免费/试点 7 天；付费默认 30 天；企业 ZDR |
| 日志 | 用于 abuse monitoring、debugging、billing | 日志字段分层：billing metadata、trace metadata、raw prompt 分开 |
| 模型商转发 | Cursor、gateway 产品会转发到模型商 | 明确列出子处理方和模型商 |
| 输出责任 | OpenAI 要求客户负责评估输出准确性和适用性 | 用户负责审核输出和执行结果；高风险操作需要确认 |
| 损害赔偿 | 常见做法是排除间接损害，责任上限绑定过去 6-12 个月费用 | 试点协议写责任上限、间接损失排除、用户备份义务 |
| 误删文件/破坏数据 | SaaS 条款常要求用户保留副本 | Agent 执行前提醒用户保持备份，并为破坏性动作加确认 |

### 6.2 V0 隐私架构建议

提供三种模式：

| 模式 | 数据路径 | 用户信任成本 | 适用场景 |
|---|---|---|---|
| Local Audit | 用户本地运行脚本生成脱敏 token report | 最低 | 早期访谈、隐私敏感用户 |
| BYOK Proxy | 用户自带模型 Key，我们只做优化/路由 | 中等 | 开发者、小团队 |
| Hosted API | 我们托管模型 Key 和优化层 | 最高 | 体验优先、非敏感任务 |

优先顺序：Local Audit -> BYOK Proxy -> Hosted API。

### 6.3 V0 安全控制清单

最低安全能力：

- TLS 传输。
- API key 加密存储。
- raw prompt 默认短保留。
- trace 与 billing metadata 分离。
- 日志脱敏：secret、token、private key、password、cookie、数据库连接串。
- `.gitignore` / `.cursorignore` / `.agentignore` 支持。
- 用户可删除任务数据。
- 删除、覆盖、部署、数据库写入、外部付款等危险操作必须显式确认。
- 每次任务输出操作日志，用户可审计。
- 企业选项：ZDR、self-hosted/VPC、SSO、audit log、DPA。

### 6.4 责任边界条款草案

建议试点协议包含：

- 用户保留输入数据和代码的必要权利。
- 用户负责审核输出和执行结果。
- 用户负责备份重要文件、数据库和生产环境。
- 服务按试点状态提供，结果质量和连续可用性有限承诺。
- 对间接损失、利润损失、业务中断、数据损失设责任排除。
- 总责任上限绑定用户过去 3-12 个月实际支付费用。
- 破坏性操作需要用户确认，确认记录进入审计日志。

这部分需要律师复核，当前版本只作为产品和调研输入。

## 7. 宣发与包装调研

### 7.1 推荐包装

主定位：

> Token efficiency layer for long-running AI agents.

中文：

> 面向长任务 Agent 的 Token 成本优化层。

备选表达：

- Agent Token Audit
- Long-task Agent API
- Context Optimization Layer
- Prompt Cache Optimizer for Agent Workflows
- AI Agent Cost Control Gateway

### 7.2 对外卖点顺序

建议按这个顺序讲：

1. 成本：长任务 Token 账单下降。
2. 可解释：告诉你哪些上下文在浪费钱。
3. 集成：兼容 Claude Code、Codex、自研 Agent。
4. 隐私：Local Audit、BYOK、ZDR/self-hosted 选项。
5. 质量：任务成功率和人工介入次数一起评估。

### 7.3 传播渠道

| 渠道 | 当前价值 | 用法 |
|---|---|---|
| X/Twitter | AI 产品全球宣发主阵地 | 搜索痛点、找 KOL、发 benchmark 图 |
| Hacker News | 工程师真实性强 | 发技术复盘和可复现实验 |
| Reddit | 用户抱怨更直接 | 搜 ClaudeCode、Codex、AI_Agents、LangChain |
| GitHub | 找高频 agent / skill 作者 | 找 design partner |
| 微信公众号/技术社群 | 国内技术传播 | 中文案例和团队试点 |
| 小红书/抖音 | 适合轻量科普 | 当前优先级低 |
| 线下会议 | 建关系 | 适合找第一批用户，不作为主路径 |

### 7.4 X/Twitter 搜索策略

优先关键词：

- `Claude Code token cost`
- `Claude Code expensive`
- `Codex token usage`
- `prompt caching agent cost`
- `context engineering tokens`
- `AI agent observability token usage`
- `LangSmith token usage`
- `LLM gateway cost tracking`
- `Claude Code compact`
- `OpenClaw save tokens`
- `AI agent API bill`

中文关键词：

- `Claude Code 贵`
- `Claude Code token`
- `AI Agent token 成本`
- `上下文工程 token`
- `Agent 账单`
- `大模型 API 账单`

优先账号类型：

- Claude Code / Codex 重度用户。
- LangChain / Helicone / Portkey / LiteLLM 官方和创始人。
- AI coding KOL。
- GTM / AI agency operator。
- 企业 AI infra 工程师。
- 开源 agent framework 维护者。

判断标准：

- 提到真实账单金额、tokens、session 数、任务时长。
- 提到具体失败场景：context overflow、limits、rate limit、trace 太大、工具调用失控。
- 提到已有 workaround：compact、cache、summary、proxy、routing、self-hosted。
- 评论区有人附和，或有人询问工具/方案。

### 7.5 X/Twitter 已读证据摘要

| 方向 | 证据 | 判断 |
|---|---|---|
| 长上下文压缩 | YC 宣传 Compresr：压缩 long context，接入 Claude Code / OpenClaw / agentic proxy | 这条赛道已经有 YC 背书竞品，说明方向成立，也说明需要更清晰差异 |
| 成本痛点 | OpenClaw 用户从每天 35-40 美元压到 65-70% 成本下降 | “长任务省钱”卖点可被用户理解，成本下降有传播性 |
| 成本监控 | Mission Control / OpenClaw dashboard 展示 session stats、token usage、cost display | audit/dashboard 是自然入口 |
| Compact 机制 | Claude Code compact 讨论中出现 MicroCompact、Session Memory Compact、Legacy Compact | 用户已接受上下文压缩概念，产品可以复用语言 |
| 事故风险 | Hermes.md 事件造成单日 200 美元额外计费，后续退款/credits | 计费异常、路由异常、命名误判是责任边界重点 |
| 产品宣发 | bolt.new 用 reduce token usage 和 code truncation issues 宣传 agent 升级 | Token usage 是成熟产品可公开讲的产品卖点 |

本次 X 调研结论：对外文案不要只说“省 80% token”。更强表达是“找出长任务 Agent 为什么烧钱，并给出可验证的账单下降路径”。这更像 audit + optimization workflow，天然适合先用服务式调研验证。

## 8. 用户画像

### 8.1 优先用户

| ICP | 识别信号 | 痛点 | 付费可能 |
|---|---|---|---|
| Agent 高频独立开发者 | X 上晒 Claude Code/Codex 工作流；GitHub 有 agent tooling repo | 限额、token、长任务效率 | 中 |
| AI agency operator | 给客户做 automation/agent | API 成本吃利润、客户数据敏感 | 高 |
| 小团队 CTO / AI lead | 内部已有 agent 自动化 | 成本、审计、隐私、失败复盘 | 高 |
| DevTools 创业团队 | 产品里嵌入 coding/research agent | 单位经济模型 | 高 |
| 研究/eval 团队 | 跑大规模 agent eval/benchmark | eval 成本高、trace 巨大 | 中高 |

### 8.2 暂缓用户

| 用户 | 原因 |
|---|---|
| 低频个人用户 | 账单痛感弱，愿意折腾免费 workaround |
| 泛 AI 兴趣用户 | 需求不稳定，反馈噪音高 |
| 超大企业安全团队 | 销售周期长，当前调研阶段接入成本高 |
| 完全离线/强监管团队 | 需要 self-hosted/VPC，当前工程量高 |

## 9. 用户访谈计划

### 9.1 样本目标

14 天内完成：

- 15 个有效访谈。
- 5 个愿意提供真实 trace 或账单截图的用户。
- 3 个愿意试用 Local Audit 的用户。
- 1 个愿意付费做 Token Audit 的用户。

有效访谈定义：

- 受访者过去 30 天真实使用过 Claude Code、Codex、Cursor Agent、LangGraph、CrewAI、自研 Agent 中至少一种。
- 能说出最近一次长任务的具体过程。
- 能提供大概 token / 账单 / 限额 / 时间成本信息。

### 9.2 访谈问题

开场：

1. 你最近一次让 Agent 做超过 10 分钟的任务是什么？
2. 当时用了什么工具？Claude Code、Codex、Cursor、LangGraph、自研？
3. 你能从头到尾讲一遍那次任务怎么跑的吗？

行为事实：

4. 任务跑了多久？
5. 你中间人工介入了几次？
6. 它读了哪些文件、文档或上下文？
7. 有没有重新规划、重新读取项目、重复解释背景？
8. 最后成功了吗？失败在哪里？

成本事实：

9. 你能看到那次任务消耗了多少 tokens 或多少钱吗？
10. 你最近一个月 AI coding / agent API 大概花多少钱？
11. 哪一次账单让你明显觉得贵？
12. 你做过哪些省 token 的动作？

隐私事实：

13. 哪些数据你敢发给第三方服务？
14. 哪些数据你只接受本地处理？
15. 你现在对 Claude Code / Codex / Cursor 的隐私信任来自哪里？
16. 如果一个第三方 API 能省 50%-80% token，你会担心什么？

付费测试：

17. 如果我们只本地分析你的 trace，告诉你哪里浪费 token，你愿意试吗？
18. 如果 audit 后预计每月省 500 美元，你愿意为一次报告付多少钱？
19. 你更愿意按次 audit、按月订阅、按节省金额分成，还是按 API 用量付费？
20. 你愿意现在给一个真实任务样本让我们测吗？

观察任务：

21. 能不能屏幕共享，展示一次你怎么启动长任务？
22. 能不能打开你的 usage / billing 页面，只看金额和 token，不看隐私内容？
23. 能不能展示一段失败 trace？

### 9.3 访谈记录模板

```md
受访者：
角色：
工具：
最近 30 天使用频率：
月 AI/Agent 成本：

最近一次长任务：
- 任务目标：
- 工具：
- 时长：
- 人工介入：
- 成功/失败：
- 失败原因：
- 大概 token / 金额：

当前 workaround：
- compact / summary：
- prompt caching：
- 自写脚本：
- observability：
- gateway：

隐私边界：
- 可上传：
- 只接受本地：
- 需要企业条款：

付费信号：
- 愿意提供 trace：是/否
- 愿意试 Local Audit：是/否
- 愿意付费 audit：是/否
- 可接受价格：

原话摘录：
- 

判断：
- 痛点强度：高/中/低
- 成交可能：高/中/低
- 推荐下一步：
```

## 10. 计费模式判断

当前阶段只调研，不定价上线。

建议访谈时测试 4 个价格模型：

| 模式 | 适用阶段 | 优点 | 风险 |
|---|---|---|---|
| 一次性 Token Audit | 立项前/试点 | 最容易成交，信任成本低 | 不形成持续收入 |
| BYOK 月费 | 早期产品 | 隐私压力较低，用户账单透明 | 用户配置复杂 |
| Hosted API usage-based | 成熟产品 | 接入简单，价值随用量增长 | 隐私、法律、模型商转售条款压力大 |
| 节省分成 | 企业试点 | 和价值绑定强 | 计算复杂，争议多 |

推荐先测试：

- 免费：1 次脱敏 Local Audit，换访谈和案例。
- 付费试点：$300-$1,000 / 次 Token Audit。
- 团队试点：$1,000-$3,000 / 月，包含 audit、优化配置、周报。

成功信号：

- 有人愿意提供真实账单。
- 有人愿意跑本地脚本。
- 有人愿意为 audit 付费。
- 有人愿意把它接进现有 Agent workflow。

## 11. 14 天执行计划

### Day 1-2：证据整理

- 整理 20 条 X/Twitter 痛点证据。
- 整理 10 个竞品文案和隐私条款。
- 做一页竞品矩阵。
- 定义 benchmark protocol。

### Day 3-5：用户招募

- 从 X、GitHub、HN、Reddit 找 100 个候选用户。
- 发 30 条私信或邮件。
- 约 10 个访谈。
- 准备 Local Audit 脚本说明。

### Day 6-10：访谈与样本

- 完成 10-15 场访谈。
- 拿 5 个真实 trace / 账单 / 任务记录。
- 标注痛点：成本、失败、隐私、重复上下文、限额。
- 记录原话和截图证据。

### Day 11-12：报告与判断

- 输出用户画像。
- 输出需求强度评分。
- 输出隐私阻力评分。
- 输出计费模式排序。
- 输出是否继续做 V1 的建议。

### Day 13-14：决策会材料

- 10 页以内立项判断 PPT。
- 1 页 benchmark 摘要。
- 1 页隐私风险摘要。
- 1 页用户访谈摘要。
- 1 页下一步建议。

## 12. 决策门槛

进入 V1 的门槛：

- 至少 10 场有效访谈。
- 至少 5 个用户明确表示 token 成本/限额是当前痛点。
- 至少 3 个用户愿意提供 trace 或账单。
- 至少 1 个用户愿意付费做 Token Audit。
- 至少 3 个任务类型能稳定复现 50% 以上成本下降。
- 输出质量评分不低于 baseline。

暂缓 V1 的信号：

- 用户只表达兴趣，没人提供 trace。
- 成本痛点只存在于少数极端用户。
- 用户更信任模型商原生 caching。
- 隐私阻力导致用户只接受本地工具。
- 80% 成本下降无法跨任务稳定复现。

## 13. 团队当前分工

当前只做调研分工：

| 方向 | 工作 | 交付 |
|---|---|---|
| X/Twitter 调研 | 搜痛点、KOL、竞品话术 | 20 条证据 + 账号名单 |
| 隐私法律调研 | OpenAI、Anthropic、Cursor、PDF SaaS 条款 | 条款对比表 |
| 竞品调研 | 模型商、Agent、Infra、Gateway | 竞品矩阵 |
| 用户访谈 | 找 15 个高频 Agent 用户 | 访谈记录 |
| Benchmark 设计 | 定义任务、指标、对照方法 | benchmark protocol |
| 汇总判断 | 判断是否进入 V1 | 立项判断报告 |

## 14. 当前推荐动作

明天就做三件事：

1. 确定 5 个 benchmark 任务：coding refactor、repo QA、long doc analysis、multi-agent search、agent eval。
2. 从 X/Twitter 和 GitHub 拉 100 个候选用户，先私信 30 个。
3. 做一个 Local Token Audit 模板，先让用户本地跑，避开早期隐私信任障碍。

推荐决策：继续调研 14 天，主线从“卖 API”改成“验证 Token Audit + Optimization Layer”，用真实 trace 和账单判断是否进入 V1。
