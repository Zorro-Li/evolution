# 隐私、法律与竞品矩阵

日期：2026-04-28  
用途：立项前调研附件

## 1. 竞品分层

| 层级 | 产品 | 用户心智 | 与本项目关系 |
|---|---|---|---|
| 模型商 | OpenAI API / Codex | 官方模型和 coding agent | 数据政策、缓存、责任条款对标 |
| 模型商 | Anthropic Claude / Claude Code | agentic coding 标杆 | 目标用户高度重合 |
| 云平台 | AWS Bedrock | 企业安全、模型托管 | 企业隐私承诺标杆 |
| 云平台 | Google Vertex AI / Gemini | 长上下文、缓存、企业治理 | context caching 和数据治理对标 |
| Agent 产品 | Cursor Agents / Bugbot | IDE 内 coding agent | 目标用户和场景重合 |
| Agent 产品 | Devin | 企业 AI software engineer | 企业级责任、安全、采购对标 |
| Infra | Helicone | LLM observability / gateway | 监控、成本、cache、rate limit 对标 |
| Infra | Portkey | AI gateway | routing、fallback、budget、cache 对标 |
| Infra | LangSmith | tracing / eval / observability | trace + evaluation 对标 |
| Infra | LiteLLM | open-source proxy | BYOK / self-hosted 替代方案 |
| 文件 SaaS | CloudConvert / Smallpdf / iLovePDF | 上传敏感文件也能建立信任 | 文件保留期、删除权、短留存文案对标 |

## 2. 隐私承诺对标

| 产品 | 数据训练 | 数据保留 | 企业选项 | 来源 |
|---|---|---|---|---|
| OpenAI API | API / business 数据默认排除训练 | API 平台有数据保留和 ZDR 选项 | Enterprise privacy、SOC 2、SAML SSO、ZDR | https://openai.com/policies/api-data-usage-policies/ |
| Anthropic API / Claude Code | 商业服务默认排除训练 | Claude Code 商业用户标准 30 天保留；ZDR 可用 | Compliance API、Bedrock/Vertex 路径 | https://docs.anthropic.com/es/docs/claude-code/data-usage |
| AWS Bedrock | prompts/completions 不用于训练 | 官方称不存储或记录 prompts/completions | VPC、IAM、KMS、PrivateLink | https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html |
| Google Vertex AI | 默认有明确数据治理边界 | 支持 context cache、logs、ZDR 配置 | Google Cloud 企业安全体系 | https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance |
| Cursor | Privacy Mode / enterprise security | 代码和 prompt 处理有模式差异 | Enterprise、SOC 2、privacy mode | https://cursor.com/security/ |
| CloudConvert | 文件处理需要临时上传 | 可手动删除，最晚 24 小时删除；日志 180 天 | GDPR、DPA | https://cloudconvert.com/privacy |
| Smallpdf | 文件处理后短时间删除 | 多数文件 1 小时后删除 | ISO 27001、GDPR、CCPA | https://smallpdf.com/support |
| iLovePDF | 文件自动删除 | 处理后两小时内删除 | TLS、GDPR | https://www.ilovepdf.com/help/security |

## 3. V0 隐私方案

推荐三档：

| 档位 | 数据路径 | 默认保留 | 目标用户 |
|---|---|---|---|
| Local Audit | 用户本地跑脚本，生成脱敏 token report | raw data 不离开本机 | 早期访谈、高隐私用户 |
| BYOK Proxy | 用户自带模型 Key，经优化层路由 | raw prompt 7 天，metadata 30 天 | 开发者、小团队 |
| Hosted API | 团队托管模型 Key 和优化层 | raw prompt 可配置，企业 ZDR | 体验优先用户 |

## 4. 试点条款必须覆盖

- 用户输入、输出、代码、文档默认排除训练。
- 明确列出子处理方：OpenAI、Anthropic、Google、AWS、日志服务、云服务商。
- raw prompt、trace、billing metadata 分别定义。
- 用户可删除任务数据。
- 企业客户可要求 ZDR、self-hosted/VPC、DPA、audit log。
- 用户负责审核输出、执行结果和备份。
- 破坏性操作需要显式确认。
- 总责任上限绑定已付费用。
- 间接损失、利润损失、业务中断、数据损失设责任排除。

## 5. 当前判断

立项前调研阶段优先用 Local Audit，降低隐私阻力。BYOK Proxy 是早期产品形态，Hosted API 是后续体验优化形态。

