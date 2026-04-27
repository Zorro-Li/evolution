# X/Twitter 调研证据

日期：2026-04-28  
采集方式：Computer Use 实际访问 X/Twitter 页面  
说明：6551 X API 返回 `insufficient quota`，本次改用 Safari 登录态手动搜索和读取。

## 搜索词

- `"Claude Code" "token" cost`
- `"AI agent" "token usage"`
- `"Claude Code" "compact" token`
- OpenClaw Cost Optimization Playbook
- Garry Tan 主页近期 agent/GStack 相关内容

## 高价值证据

| 来源 | 链接 | 观察 | 对项目的意义 |
|---|---|---|---|
| Y Combinator | https://x.com/ycombinator/status/2026811140010045847 | YC 宣传 Compresr：缩短 long context，提升 accuracy，降低 cost/latency，可接入 Claude Code / OpenClaw / agentic proxy | 长上下文压缩已是明确创业方向；竞品存在，定位需要避开泛泛 compression |
| Prajwal Tomar | https://x.com/PrajwalTomar_/status/2027387894399422775 | OpenClaw 成本优化文章：默认配置每天 35-40 美元，优化后同一负载下降 65-70%；方案包括模型分层、本地搜索、session memory compact、本地模型、OpenRouter | 成本下降有强传播性；用户理解“默认配置烧钱”这个叙事 |
| Nyk | https://x.com/nyk_builderz/status/2028722212375761311 | Mission Control Local Mode 展示 Claude Code session stats、跨项目 token usage、订阅感知 cost display | 本地 token/cost dashboard 已有需求；Local Audit 是低信任成本入口 |
| Tom Dorr | https://x.com/tom_doerr/status/2022061117434896721 | OpenClaw dashboard 用于监控 AI agent activity 和 token usage | agent 可观测性正在从日志走向 token/cost 监控 |
| Berryxia.AI | https://x.com/berryxia/status/2039342944797577583 | Claude Code compact 讨论：MicroCompact、Session Memory Compact、Legacy Compact；每轮裁剪工具输出可省 5-15K tokens | “compact”是目标用户已理解的语言；可作为访谈关键词 |
| Tw93 | https://x.com/HiTw93/status/2045629549577371814 | Claude Code Max 配置建议在 1M context window 的 40% 触发 compact，用于保持长任务响应和上下文 | 用户已经在手动调 compact 阈值，说明自动调参有空间 |
| Teknium / Om Patel | https://x.com/Teknium/status/2048576507786956973 | Hermes.md 事件：Claude Code / Hermes Agent 相关上下文触发额外计费，用户单日损失 200 美元，Anthropic 后续退款/credits | 计费异常和误路由是核心风险；需要审计、告警、责任边界 |
| 0xMarioNawfal | https://x.com/RoundtableSpace/status/2036408939126907066 | AI agent 少用 tokens 的 prompt 获得 8 万+浏览，内容强调 token usage visibility 和成本优化 | 大众化 AI 受众也关心 token efficiency，但高质量用户需要筛选 |
| bolt.new | https://x.com/boltdotnew/status/1848822514090446962 | AI agent 升级公开宣传 reduce token usage 和 code truncation issues | “减少 token usage”能作为成熟产品 release note 里的正式卖点 |

## 结论

X 上的证据支持三个判断：

1. 成本痛点真实存在，尤其在 Claude Code / OpenClaw / agent workflow 的高频用户里。
2. 用户已经在主动找 compact、model routing、local search、dashboard、token visibility 等解决方案。
3. 最优早期入口是 Local Token Audit + Optimization Report，随后才是托管 API。

下一步 X 调研应补 100 个候选用户列表：发过 Claude Code、OpenClaw、GStack、token usage、compact、agent dashboard、LLM gateway 相关内容的人优先。

