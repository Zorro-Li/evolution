# Agent API 商业化与上线策略：分模块调研报告

日期：2026-04-28  
依据：2026-04-27 22:40 会议记录  
阶段：立项前调研  
建议周期：14 天  

## 0. 总结论

当前最值得推进的是 **Agent Token Audit + Optimization Layer**，先做立项前验证，再讨论公司化、正式售卖和融资。

推荐顺序：

1. 先用 Local Token Audit 拿真实用户 trace 和账单。
2. 再验证 BYOK Proxy 的接入体验。
3. 最后评估 Hosted API 的产品化和法律责任。

核心判断：

- “长任务 Agent 成本优化”是真问题。
- “托管 API”体验最好，隐私和责任压力最大。
- “Local Audit / BYOK”最适合作为早期验证入口。
- “省 80% token”适合做钩子，立项判断要看可复现 benchmark 和真实付费。
- X/Twitter 是当前 AI 产品调研和宣发的主渠道，已用 Computer Use 实际读取相关证据。

## 1. 核心结论调研：V1 是否应该围绕 Token 成本下降

### 结论

V1 应该围绕 “长任务 Token 成本显著下降” 建立验证，不宜同时加入记忆增强、并行搜索、上下文工程全套叙事。

### 证据

| 来源 | 事实 | 含义 |
|---|---|---|
| OpenAI Prompt Caching | 官方文档称 prompt caching 可降低延迟和 input token 成本，API 返回 `cached_tokens` | 成本优化是模型商明确支持的方向 |
| Anthropic Prompt Caching | 官方称长 prompt 场景可减少成本和延迟 | Claude 生态目标用户已被教育 |
| Google Gemini Context Caching | Gemini API 支持显式 context caching | 长上下文复用是跨模型商需求 |
| X/Twitter - OpenClaw | 用户文章记录默认配置每天 35-40 美元，优化后同负载下降 65-70% | 成本痛点有真实传播样本 |
| X/Twitter - YC Compresr | YC 宣传 Compresr 可压缩 long context、降低 cost/latency，并接入 Claude Code / OpenClaw | 方向已有 YC 背书竞品 |

来源：

- [OpenAI Prompt Caching](https://platform.openai.com/docs/guides/prompt-caching)
- [Anthropic Prompt Caching](https://www.anthropic.com/news/prompt-caching)
- [Gemini Context Caching](https://ai.google.dev/gemini-api/docs/caching/)
- [YC on Compresr](https://x.com/ycombinator/status/2026811140010045847)
- [OpenClaw Cost Optimization Playbook](https://x.com/PrajwalTomar_/status/2027387894399422775)

### 判断

“成本下降”是 V1 最强卖点，因为用户可以直接用账单验证。记忆增强、并行搜索、上下文工程可以作为成本下降的实现路径，先放在产品内部，不放在首屏宣传。

### 建议

V1 的一句话定义：

> Long-task Agent Token Audit: find where your agent burns tokens and show a verified path to lower cost.

中文：

> 长任务 Agent Token 审计：找出你的 Agent 为什么烧钱，并给出可验证的降本路径。

## 2. API 模式调研：优势、隐私、安全、法律风险

### 结论

API 模式适合中长期产品化，当前阶段适合先做 Local Audit 和 BYOK Proxy。Hosted API 在体验上最顺，风险集中在数据、日志、误操作和责任边界。

### 证据

| 公司/产品 | 数据政策 | 可借鉴点 |
|---|---|---|
| OpenAI API | API 数据默认不用于训练；有 Modified Abuse Monitoring 和 Zero Data Retention | 写清训练用途、日志用途、ZDR 条件 |
| Anthropic Claude Code | 商业组织 API key 可配置 ZDR；Claude Code 标准有数据保留说明 | Claude Code 用户会问清 ZDR 和保留期 |
| AWS Bedrock | 官方称 prompts/completions 不用于训练，不分发给第三方 | 企业客户会期待同等表述 |
| Cursor Enterprise | Privacy Mode 下代码不用于训练，并和模型提供商有 ZDR 协议；prompt-building 发生在 Cursor 服务器 | 透明说明服务器参与程度很重要 |
| CloudConvert / Smallpdf / iLovePDF | 上传文件后短期删除，清楚写保留期 | 文件型 SaaS 的信任文案可复用 |

来源：

- [OpenAI data controls](https://platform.openai.com/docs/models/how-we-use-your-data/)
- [OpenAI enterprise privacy](https://openai.com/policies/api-data-usage-policies/)
- [Anthropic Claude Code data usage](https://docs.anthropic.com/en/docs/claude-code/data-usage)
- [Anthropic ZDR](https://privacy.anthropic.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to)
- [AWS Bedrock data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [Cursor Enterprise](https://cursor.com/enterprise)
- [Cursor Security](https://cursor.com/security/)
- [CloudConvert Privacy](https://cloudconvert.com/privacy)
- [Smallpdf Support](https://smallpdf.com/support)
- [iLovePDF Security](https://www.ilovepdf.com/help/security)

### 风险拆解

| 风险 | 用户会问什么 | V0 应对 |
|---|---|---|
| Prompt/代码经过服务器 | 你们能看到我的代码吗 | Local Audit 优先，BYOK 次之，Hosted API 后置 |
| 日志泄露 | 你们保存哪些原始数据 | raw prompt、trace metadata、billing metadata 分层 |
| 模型商转发 | 数据去了哪些第三方 | 列出 OpenAI / Anthropic / Google / AWS 等子处理方 |
| 误删文件 | Agent 删除文件谁负责 | 破坏性动作必须确认，用户保留备份责任 |
| 业务损失 | 输出错导致损失谁赔 | 试点协议写责任上限、间接损失排除 |
| 服务器被攻击 | 数据被偷怎么办 | 加密、短保留、脱敏、最小权限、审计日志 |

### 建议

当前不要直接做完整 Hosted API 售卖。先提供三档方案：

| 档位 | 数据路径 | 调研阶段价值 |
|---|---|---|
| Local Audit | 用户本地跑脚本，输出脱敏 token report | 最适合拿第一批数据 |
| BYOK Proxy | 用户自带 API Key，团队提供优化层 | 适合开发者试点 |
| Hosted API | 团队托管模型 Key 和路由 | 适合后续体验验证 |

## 3. 用户自带 API vs 团队托管 API 调研

### 结论

早期验证主推 BYOK 和 Local Audit，长期产品保留 Hosted API。BYOK 降低信任成本，Hosted API 提升转化率。

### 对比

| 模式 | 优点 | 风险 | 适合阶段 |
|---|---|---|---|
| Local Audit | 数据不出本地，用户最容易接受 | 无持续调用收入 | 立项前调研 |
| BYOK Proxy | 用户账单透明，隐私责任较轻 | 配置复杂，用户体验弱 | 试点 |
| Hosted API | 接入最简单，商业化最顺 | 隐私、法律、转售、账单责任重 | V1/V2 |
| Self-hosted / VPC | 企业最信任 | 工程和销售成本高 | 企业阶段 |

### 市场证据

- Cursor 的安全页明确说明 prompt-building 发生在服务器，同时提供 Privacy Mode 和模型商 ZDR 说明。这说明用户接受服务器参与，但前提是说明清楚。
- AWS Bedrock 通过“不训练、不分发、云安全体系”承接企业信任。早期团队难以直接达到这个信任水平。
- PDF SaaS 普遍用“短保留期 + 手动删除 + 加密传输”建立上传信任。

### 建议

调研问卷必须测试这三个问题：

1. 你愿意让 raw prompt / 代码经过第三方服务器吗？
2. 你更接受 Local Audit、BYOK Proxy、Hosted API 哪一种？
3. 如果 Hosted API 能省 50%-80% 成本，你需要什么安全承诺？

## 4. 技术壁垒与包装方式调研

### 结论

对外包装应该卖结果和审计能力，内部技术路线保持抽象。最适合的类别是 **Agent Cost Control / Context Optimization / Token Audit**。

### 竞品与替代方案

| 类别 | 代表产品 | 卖点 | 对我们的启发 |
|---|---|---|---|
| Context compression | Compresr | 压缩 long context，降低 cost/latency | 直接竞品，需要差异化 |
| Native caching | OpenAI / Anthropic / Google | prompt/context caching | 证明方向成立，也构成替代方案 |
| Gateway | Portkey / Helicone / LiteLLM | routing、fallback、cache、budget | API gateway 心智成熟 |
| Observability | LangSmith / Braintrust / Langfuse | tracing、eval、cost analytics | 成本可视化和 trace 分析是刚需 |
| Agent dashboard | Mission Control / OpenClaw dashboard | session stats、token usage | Local dashboard 是可行入口 |

来源：

- [Compresr docs](https://compresr.ai/docs/gateway)
- [Helicone platform overview](https://docs.helicone.ai/getting-started/platform-overview)
- [Helicone caching](https://docs.helicone.ai/features/advanced-usage/caching)
- [LangSmith Observability](https://docs.langchain.com/oss/python/langchain/observability)
- [LangSmith product](https://www.langchain.com/langsmith)
- [Braintrust observability guide](https://www.braintrust.dev/articles/best-ai-observability-tools-2026)

### 可宣传表达

优先：

- Agent Token Audit
- Context Optimization Layer
- Agent Cost Control Gateway
- Token Efficiency Layer for Long-running Agents

暂缓：

- 新模型
- 新框架
- 通用 Agent 平台

### 判断

技术壁垒的核心来自四件事：

1. 真实 trace 数据。
2. 成本归因能力。
3. 和 Claude Code / Codex / OpenClaw / Cursor 的接入能力。
4. 优化后质量不下降的 benchmark。

### 建议

外部表达：

> We analyze your agent traces and show exactly where repeated context, tool output, model routing, and cache misses are wasting money.

中文：

> 我们分析你的 Agent trace，告诉你重复上下文、工具输出、模型路由和缓存未命中在哪里浪费钱。

## 5. 宣发与上线节奏调研

### 结论

当前宣发重点放在 X/Twitter 和技术社群。5 月 6 日武汉会议适合作为线下关系节点，适合找访谈对象和潜在设计伙伴。

### 渠道判断

| 渠道 | 当前价值 | 推荐动作 |
|---|---|---|
| X/Twitter | AI 产品宣发和痛点发现主阵地 | 每天搜关键词，收集痛点和候选用户 |
| GitHub | 找真实 agent workflow 作者 | 搜 Claude Code skill、OpenClaw、GStack、LangGraph repo |
| Hacker News | 技术验证和公开 launch | 等有 benchmark 再发 |
| Reddit | 找抱怨和失败案例 | 搜 ClaudeAI、ClaudeCode、AI_Agents、LLMDevs |
| 微信/技术群 | 国内第一批用户 | 发调研帖和招募帖 |
| 5 月 6 日会议 | 线下社交 | 带 1 页说明和访谈问题 |
| WAIC / 创业赛 | 背书和曝光 | 等有 Demo 和真实案例再投 |
| 黑客松 | 开源压力较大 | 适合做 demo，不适合暴露核心实现 |

### X/Twitter 已读证据

见附件：[x_twitter_evidence.md](/Users/lizongru/codex/进化/runs/agent-api-research-2026-04-28/x_twitter_evidence.md)

已读到的核心信号：

- YC 宣传 Compresr。
- OpenClaw 用户公开写成本优化攻略。
- Claude Code compact 有中文和英文讨论。
- token usage dashboard 已出现。
- Hermes.md 事件造成额外计费争议。

### 建议

当前宣发形式是“调研招募”，避免正式产品发布。

招募标题：

> Looking for Claude Code / OpenClaw power users whose agents burn too many tokens.

中文：

> 招募 Claude Code / OpenClaw 重度用户：如果你的 Agent 长任务很烧 token，我们想帮你做一次本地 Token Audit。

## 6. 背书、信任与投资调研

### 结论

当前最大难点是信任背书。最现实的背书来自真实用户案例、公开 benchmark、开源/本地 audit 工具、设计伙伴。

### 信任来源排序

| 背书方式 | 当前可行性 | 价值 |
|---|---|---|
| 真实 before/after 案例 | 高 | 最直接 |
| 脱敏 benchmark | 高 | 技术用户认可 |
| Local Audit 工具 | 高 | 降低隐私焦虑 |
| 设计伙伴 | 中高 | 证明需求 |
| VC / 大厂背书 | 中 | 后续价值大 |
| 创业比赛奖项 | 中 | 宣传价值 |
| 企业安全认证 | 低 | 当前阶段成本高 |

### 判断

信任建立路径：

1. 数据不出本地。
2. 先给用户一份有用报告。
3. 用报告换访谈、trace 和案例。
4. 用案例推动 BYOK Proxy。
5. 用 BYOK 试点推动 Hosted API。

### 建议

调研阶段不要把 VC 和收购作为主线。当前要拿三类材料：

- 3 个真实 Token Audit 案例。
- 1 个愿意公开名字或匿名行业的设计伙伴。
- 1 份可复现实验报告。

## 7. 用户画像与市场判断调研

### 结论

优先用户是 Claude Code / Codex / OpenClaw 高频用户、AI agency operator、小团队 AI infra 负责人。个人重度用户适合早期验证，企业团队适合后续付费。

### 用户分层

| 用户 | 识别信号 | 痛点 | 付费可能 |
|---|---|---|---|
| Claude Code / Codex 高频用户 | X 上晒 workflow、成本、compact 配置 | 限额、账单、长任务上下文 | 中 |
| OpenClaw / GStack 用户 | 跑本地 agent、改配置、用 skills | 默认配置烧钱、工具调用多 | 中高 |
| AI agency | 给客户交付 automation | API 成本吃利润、重复搭建 | 高 |
| 小团队 CTO / AI lead | 内部 Agent 跑生产流程 | 成本、审计、安全、失败复盘 | 高 |
| DevTools 团队 | 产品内置 agent | 单位经济模型和产品毛利 | 高 |
| 研究/eval 团队 | 大量跑 agent benchmark | eval 成本和 trace 数据 | 中高 |

### 访谈样本目标

14 天内：

- 100 个候选用户。
- 30 个触达。
- 15 场访谈。
- 5 个真实 trace / 账单。
- 3 个 Local Audit 试用。
- 1 个付费 audit 意向。

### 建议

优先从 X 搜这批关键词：

- `Claude Code token cost`
- `Claude Code compact`
- `OpenClaw cost`
- `AI agent token usage`
- `agent dashboard token`
- `LLM gateway cost`
- `context compression Claude Code`

## 8. 分工安排调研

### 结论

当前分工只做调研。每个人的交付物要能进入最终立项判断。

### 推荐分工

| 方向 | 交付物 | 判断标准 |
|---|---|---|
| X/Twitter 调研 | 20 条痛点证据 + 100 个候选用户 | 有真实账单、tokens、失败案例 |
| 竞品调研 | 10 个竞品矩阵 | 能说清定位、价格、隐私、入口 |
| 隐私法律调研 | 条款对比 + V0 风险清单 | 覆盖数据保留、训练、日志、责任上限 |
| 用户访谈 | 15 份访谈记录 | 至少 5 个高痛点用户 |
| Benchmark 设计 | 5 个任务协议 | 能复现成本和质量指标 |
| 汇总判断 | 10 页以内决策材料 | 明确继续、暂缓、换方向 |

### 已完成附件

- [privacy_competitor_matrix.md](/Users/lizongru/codex/进化/runs/agent-api-research-2026-04-28/privacy_competitor_matrix.md)
- [benchmark_protocol.md](/Users/lizongru/codex/进化/runs/agent-api-research-2026-04-28/benchmark_protocol.md)
- [user_research_plan.md](/Users/lizongru/codex/进化/runs/agent-api-research-2026-04-28/user_research_plan.md)

## 9. 待解决问题逐项调研结论

| 问题 | 当前调研结论 | 下一步 |
|---|---|---|
| API 模式下隐私如何保护 | Local Audit / BYOK / Hosted API 三档分层 | 写 V0 隐私说明 |
| 数据经过服务器如何建立信任 | 短保留、ZDR、脱敏、子处理方披露、删除权 | 做 privacy one-pager |
| Agent 误操作如何免责 | 用户审核输出、备份责任、危险操作确认、责任上限 | 做试点协议草案 |
| 服务器安全如何设计 | TLS、加密、最小权限、日志分层、secret 脱敏 | 做安全 checklist |
| API 计费、包月、混合模式 | 先 audit 收费，再 BYOK 月费，Hosted API 后置 | 访谈测试 WTP |
| 包装成什么 | Agent Token Audit / Context Optimization Layer | 用 X 测标题 |
| 第一批用户从哪里来 | X + GitHub + 技术群 | 先拉 100 人名单 |
| 是否参加会议/比赛 | 会议做访谈，比赛等 demo | 5 月 6 日带调研单页 |
| 收益、股权、分红 | 当前阶段暂缓 | 有付费和投入后再定 |

## 10. 下一步计划调研

### 14 天调研计划

第 1-2 天：

- X/Twitter 补 20 条证据。
- GitHub 拉 50 个 agent workflow 作者。
- 完成竞品矩阵。

第 3-5 天：

- 发 30 条私信。
- 约 10 场访谈。
- 定 5 个 benchmark 任务。

第 6-10 天：

- 完成 10-15 场访谈。
- 拿 5 个 trace / 账单 / session 样本。
- 做 3 份 Local Token Audit。

第 11-12 天：

- 汇总痛点强度。
- 汇总隐私阻力。
- 汇总付费意愿。
- 跑内部 benchmark。

第 13-14 天：

- 形成决策材料。
- 判断进入 V1、继续调研、换包装、暂缓。

### 进入 V1 的门槛

- 15 场访谈里至少 5 个高痛点用户。
- 至少 3 个用户愿意给 trace。
- 至少 1 个用户愿意为 audit 付费。
- 至少 3 个任务类型能稳定降本 50% 以上。
- 至少 1 个任务类型能达到 80% 降本。
- 输出质量不低于 baseline。

### 当前推荐

今天开始执行：

1. 用 X/Twitter 搜关键词，建立 100 个候选用户表。
2. 用 `user_research_plan.md` 的私信模板触达 30 人。
3. 用 `benchmark_protocol.md` 先跑 2 个内部任务。
4. 用 `privacy_competitor_matrix.md` 写一页隐私说明。

## 11. 最终判断

这个方向值得继续调研 14 天。当前产品形态优先级是：

1. Local Token Audit。
2. BYOK Optimization Proxy。
3. Hosted Long-task Agent API。
4. Enterprise Self-hosted / VPC。

当前最关键任务是拿真实 trace 和账单。没有真实 trace，80% 成本下降只能作为技术假设。有真实 trace、可复现 benchmark、愿意付费的用户，才进入 V1。

