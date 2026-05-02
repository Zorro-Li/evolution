# 01 原始资料台账

日期：2026-04-28  
目的：记录本次 Agent API 商业化与上线策略调研中找到的全部有效资料  
工作规则：先留痕，再分析，再总结

## A. 资料范围

本轮围绕会议记录中的 8 个问题搜集资料：

1. API 模式的隐私、安全、法律风险。
2. 用户自带 API Key 与平台托管 API 的取舍。
3. 长任务 Token 成本优化的技术与包装方式。
4. 闭源 Agent / AI Infra 产品的宣发方式。
5. 第一批用户画像和真实痛点。
6. 信任背书、企业安全、责任边界。
7. 会议、比赛、X/Twitter、GitHub 等渠道价值。
8. 进入 V1 前需要验证的 benchmark 和付费信号。

## B. 原始资料清单

| ID | 类型 | 公司/来源 | 链接 | 找到的内容 | 保存原因 |
|---|---|---|---|---|---|
| S01 | 官方文档 | OpenAI | https://openai.com/policies/api-data-usage-policies/ | API / business 数据默认排除训练，提供企业隐私承诺 | 参考 API 数据使用政策 |
| S02 | 官方文档 | OpenAI | https://platform.openai.com/docs/models/how-we-use-your-data | 说明 API 数据如何用于训练、保留和安全控制 | 参考用户数据处理说法 |
| S03 | 官方文档 | OpenAI | https://platform.openai.com/docs/guides/prompt-caching | Prompt caching 可降低成本和延迟，并返回 cached token 信息 | 参考 Token 成本优化的官方机制 |
| S04 | 官方条款 | OpenAI | https://openai.com/en-US/policies/business-terms/ | Business Terms 包含责任限制、赔偿、输出责任等条款 | 参考法律责任边界 |
| S05 | 官方产品 | OpenAI | https://openai.com/codex | Codex 是云端 software engineering agent，可并行处理任务 | 参考目标用户和竞品形态 |
| S06 | 官方文档 | OpenAI | https://platform.openai.com/docs/codex/overview | Codex CLI / cloud task / code review workflow | 参考 Agent 接入场景 |
| S07 | 官方文档 | Anthropic | https://docs.anthropic.com/en/docs/claude-code/data-usage | Claude Code 数据使用和保留，商业用户、ZDR、开发者政策 | 参考 Claude Code 用户会关心的问题 |
| S08 | 官方文档 | Anthropic | https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance | Claude Code legal / compliance / regional 和数据说明 | 参考法律与合规说明 |
| S09 | 官方文档 | Anthropic | https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching | Prompt caching 机制、缓存写入/读取、成本和延迟 | 参考缓存产品化说法 |
| S10 | 官方条款 | Anthropic | https://www.anthropic.com/legal/commercial-terms | Commercial Terms 涵盖客户内容、输出责任、责任限制 | 参考 API 商业条款 |
| S11 | 官方安全 | AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html | Bedrock 说明 prompts/completions 不用于训练，不分发给模型商 | 企业隐私标杆 |
| S12 | 官方治理 | Google Cloud | https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance | Vertex AI 生成式 AI 数据治理、训练使用、日志和配置 | 企业数据治理标杆 |
| S13 | 官方文档 | Google Gemini | https://ai.google.dev/gemini-api/docs/caching/ | Gemini context caching 支持长上下文缓存 | 参考跨模型商上下文缓存 |
| S14 | 官方安全 | Cursor | https://cursor.com/security/ | Privacy Mode、SOC 2、数据训练、模型商 ZDR、代码隐私 | 参考开发者工具的信任包装 |
| S15 | 官方企业页 | Cursor | https://cursor.com/enterprise | Enterprise privacy mode、团队管理、安全特性 | 参考企业版本包装 |
| S16 | 官方文档 | Cursor | https://docs.cursor.com/en/background-agents | Background Agents 的任务运行方式 | 参考 agent 产品形态 |
| S17 | 官方信任 | GitHub Copilot | https://docs.github.com/en/copilot/reference/copilot-trust-center | Copilot Trust Center 说明数据、隐私、安全 | 参考 coding assistant 信任文档 |
| S18 | 官方隐私 | GitHub | https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement | GitHub Privacy Statement | 参考平台隐私政策 |
| S19 | 官方文档 | Helicone | https://docs.helicone.ai/getting-started/platform-overview | LLM observability、gateway、成本、trace、agent debugging | 参考 AI Infra 包装 |
| S20 | 官方文档 | Helicone | https://docs.helicone.ai/features/advanced-usage/caching | Caching 特性 | 参考 gateway 层缓存 |
| S21 | 官方文档 | Portkey | https://portkey.ai/docs/product/ai-gateway | AI Gateway、routing、fallback、cache、budget | 参考 gateway 功能矩阵 |
| S22 | 官方文档 | LiteLLM | https://docs.litellm.ai/docs/proxy/virtual_keys | Proxy、virtual keys、budget、rate limits | 参考 BYOK / proxy 管理 |
| S23 | 官方文档 | LiteLLM | https://docs.litellm.ai/docs/proxy/caching | Proxy caching | 参考 open-source 替代方案 |
| S24 | 官方文档 | LangSmith | https://docs.langchain.com/oss/python/langchain/observability | Tracing、observability、agent debugging | 参考 trace 侧产品 |
| S25 | 官方产品 | LangSmith | https://www.langchain.com/langsmith | Agent observability / eval / deployment workflow | 参考 AI agent 监控定位 |
| S26 | 官方文章 | Braintrust | https://www.braintrust.dev/articles/best-ai-observability-tools-2026 | AI observability 产品对比 | 参考市场分类和买方语言 |
| S27 | 官方文档 | Compresr | https://compresr.ai/docs/gateway | Gateway / long context compression / agentic proxy | 直接竞品，对标重点 |
| S28 | X/Twitter | Y Combinator | https://x.com/ycombinator/status/2026811140010045847 | YC 宣传 Compresr：压缩 long context，接入 Claude Code / OpenClaw | 证明赛道已有公开竞品 |
| S29 | X/Twitter | Prajwal Tomar | https://x.com/PrajwalTomar_/status/2027387894399422775 | OpenClaw 成本优化攻略：每天 35-40 美元降到 65-70% 成本下降 | 真实用户痛点和传播模板 |
| S30 | X/Twitter | Nyk | https://x.com/nyk_builderz/status/2028722212375761311 | Mission Control Local Mode：Claude Code session stats、token usage、cost display | 本地 Token dashboard 方向 |
| S31 | X/Twitter | Tom Dorr | https://x.com/tom_doerr/status/2022061117434896721 | OpenClaw dashboard：monitoring AI agent activity and token usage | 观察 agent token usage 的需求 |
| S32 | X/Twitter | Berryxia.AI | https://x.com/berryxia/status/2039342944797577583 | Claude Code compact 三层机制讨论，MicroCompact 每轮省 5-15K tokens | Compact 语言和机制参考 |
| S33 | X/Twitter | Tw93 | https://x.com/HiTw93/status/2045629549577371814 | Claude Code Max compact window 配置建议 | 用户手动调参行为 |
| S34 | X/Twitter | Teknium / Om Patel | https://x.com/Teknium/status/2048576507786956973 | Hermes.md 事件造成单日 200 美元额外计费，Anthropic 提供退款/credits | 计费异常与责任边界案例 |
| S35 | X/Twitter | 0xMarioNawfal | https://x.com/RoundtableSpace/status/2036408939126907066 | 用 prompt 让 AI agent 少用 tokens，强调 token visibility | 大众市场对 token efficiency 的兴趣 |
| S36 | X/Twitter | bolt.new | https://x.com/boltdotnew/status/1848822514090446962 | 产品更新公开宣传 reduce token usage & code truncation issues | 成熟产品的宣发语言 |
| S37 | 隐私条款 | CloudConvert | https://cloudconvert.com/privacy | 文件临时存储、手动删除、24 小时删除、日志 180 天 | 文件 SaaS 信任机制 |
| S38 | 安全页 | CloudConvert | https://cloudconvert.com/security | ISO、加密、数据中心、安全措施 | 安全背书写法 |
| S39 | 支持/安全 | Smallpdf | https://smallpdf.com/support | 文件删除、加密、GDPR、ISO 27001 | 短留存文案参考 |
| S40 | 安全页 | iLovePDF | https://www.ilovepdf.com/help/security | 文件处理后两小时内删除，TLS，加密 | 上传敏感数据的信任文案 |
| S41 | 官方条款 | CloudConvert | https://cloudconvert.com/terms | 用户责任、服务责任、限制条款 | 免责和责任边界参考 |
| S42 | 官方产品 | Claude Code | https://claude.com/product/claude-code | Agentic coding product | 目标用户场景 |
| S43 | 官方文章 | Claude | https://claude.com/blog/introduction-to-agentic-coding | Agentic coding 工作方式和 best practices | 宣发和用户教育参考 |
| S44 | 官方文档 | Devin | https://docs.devin.ai/enterprise/get-started | 企业 AI software engineer 和企业接入 | 高价企业产品参考 |

## C. 资料分组

| 分组 | 对应 ID | 解决的问题 |
|---|---|---|
| 数据隐私与法律责任 | S01, S02, S04, S07, S08, S10, S11, S12, S14, S17, S37-S41 | API 经过服务器时如何建立信任和免责 |
| Token 成本优化机制 | S03, S09, S13, S20, S21, S23, S27-S36 | 如何降低长任务成本 |
| Agent 产品与用户场景 | S05, S06, S16, S42, S43, S44 | 目标用户和竞品形态 |
| AI Infra / Gateway / Observability | S19-S26 | 如何包装成可卖的 infra 服务 |
| 宣发与市场信号 | S28-S36, S43 | X/Twitter 和官方产品如何讲这件事 |

## D. 当前资料缺口

| 缺口 | 说明 | 下一步 |
|---|---|---|
| 真实用户账单 | 公开资料有案例，团队仍需要目标用户的真实账单和 trace | 按 `user_research_plan.md` 约访谈 |
| Compresr 具体定价 | 公开信息重点在能力和 YC 宣发，价格细节需要继续挖 | 继续查官网、X、Product Hunt |
| 企业采购条款 | 当前多为公开隐私/安全页，缺少具体 DPA 样本 | 后续找模板律师或企业合同样本 |
| 用户付费意愿 | X 上有兴趣和痛点，缺少 WTP 数据 | 访谈中测试 audit 付费 |

## E. 留痕说明

- X/Twitter API 返回 `insufficient quota`，已改用 Computer Use 打开 Safari 登录态读取 X 搜索结果和帖子。
- 具体 X 证据已单独记录在 `x_twitter_evidence.md`。
- 核心链接做过可用性抽查：Anthropic、AWS、Cursor、Helicone、Portkey、LiteLLM、LangSmith、CloudConvert、iLovePDF 返回 200；OpenAI 官方页对 `curl` 返回 403，但通过 web open 可访问并跳转到 Enterprise Privacy / developers docs；Google Cloud 对 `curl` 返回 000，但通过 web open 可访问并跳转到 Vertex AI zero data retention 文档。
- 本文件只做资料台账，逐链接分析见 `02_link_by_link_analysis.md`。
