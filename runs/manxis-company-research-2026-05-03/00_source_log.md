# ManXis 公司调研来源台账

日期：2026-05-03

## 本地上下文

| 来源 | 关键信息 |
|---|---|
| `runs/agent-api-research-2026-04-28/agent_api_preincorporation_research.md` | ManXis 当前最窄切口是 Agent Token Audit + Optimization Layer，目标用户是 Claude Code / Codex / 自研 Agent 高频用户、小团队 AI 工程负责人、AI agency / 自动化服务商。 |
| `runs/gstack-office-hours/token-compression-agent-framework-2026-04-28.md` | 先卖 Local Token Audit，再包装为 agent framework。需要 before/after token、成本、成功率、运行时间、重试次数。 |
| `runs/twitter-growth-research-2026-04-29/deep_research/04_commercial_channels_report.md` | 当前商业渠道优先 design partner、创始人直销、集成伙伴、PLG。 |
| `runs/twitter-growth-research-2026-04-29/deep_research/05_account_content_playbook.md` | ManXis 对外表达应收窄到 long-task agent API / token cost / context control / private benchmark beta。 |

## 工具状态

| 工具 | 状态 | 影响 |
|---|---|---|
| `company-research-agent` | 已安装；当前 shell 未发现 `TAVILY_API_KEY`、`GEMINI_API_KEY`、`OPENAI_API_KEY`。 | 本轮使用该 agent 的公司/行业/财务/新闻框架，结合公开官方资料手动生成报告。 |
| `competitive-intel` skill | 已读取；本机未发现 `bdata` CLI。 | 本轮用官方网页、文档、公开新闻和已有本地调研代替 Bright Data 抓取。 |

## 公开来源

| 公司 / 类别 | 链接 | 用途 |
|---|---|---|
| Compresr | https://www.ycombinator.com/companies/compresr | 直接竞品：YC 公司，定位为通过智能上下文压缩提升 long-context LLM 性能。 |
| Compresr | https://compresr.ai/docs/gateway | 直接竞品：展示 agentic proxy、Claude Code、OpenClaw、OpenHands 等接入方式。 |
| The Token Company | https://www.ycombinator.com/companies/the-token-company | 直接竞品：YC 公司，定位为 intelligent compression to eliminate context bloat。 |
| Helicone | https://www.helicone.ai/ | AI gateway / observability：成本、调试、请求日志、agent 可观测性。 |
| Helicone docs | https://docs.helicone.ai/gateway/concepts/prompt-caching | 竞品能力：prompt caching、cache hit、cache control。 |
| Portkey | https://portkey.ai/ | AI gateway：routing、fallbacks、guardrails、observability。 |
| Portkey cache | https://portkey.ai/docs/product/ai-gateway-streamline-llm-integrations/cache-simple-and-semantic | 竞品能力：simple cache、semantic cache、cache metrics。 |
| Langfuse | https://langfuse.com/ | Open-source LLM engineering platform：traces、evals、prompt management、metrics。 |
| LangSmith | https://www.langchain.com/langsmith | Agent engineering：observability、evaluation、deployment。 |
| Braintrust | https://www.braintrust.dev/ | AI eval / prompt / observability 平台，对 ManXis 的质量评估闭环有参考价值。 |
| Cursor | https://cursor.com/ | 目标客户 / 集成对象：AI code editor 和 coding agent 用户入口。 |
| Cursor docs | https://docs.cursor.com/en/background-agents | 目标客户 / 场景：Background Agents，长任务和多上下文执行。 |
| Replit Agent | https://replit.com/agent | 目标客户 / 对标：从自然语言构建 app 的 agent，涉及多轮生成和工具调用。 |
| Cognition Devin | https://devin.ai/ | 目标客户 / 高端对标：AI software engineer，企业长任务 agent 场景。 |
| Lindy | https://www.lindy.ai/ | 目标客户：AI employees / workflow automation，多任务 agent 工作流。 |
| OpenAI Prompt Caching | https://openai.com/index/api-prompt-caching/ | 平台级替代方案：自动缓存重复 prompt token，说明成本优化是基础平台能力。 |
| Anthropic Prompt Caching | https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching | 平台级替代方案：Claude prompt caching，影响 ManXis 的差异化表达。 |
| AWS Bedrock Prompt Caching | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html | 平台级替代方案：企业云平台缓存能力。 |

