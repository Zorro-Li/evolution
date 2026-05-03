# LLMOps Gateway 拆解

ID: `llmops-gateway-design`

## Description

把 AI app 或 Agent 系统拆成网关、日志、路由、缓存、成本、回放和调试闭环。来源于 Helicone、Portkey、LangSmith/Langfuse 等基础设施归纳。

## Sources

- `runs/x-creator-watch/2026-05-03/03_skill_distillation.md`
- `runs/manxis-company-research-demo-2026-05-03/helicone.md`

## Instruction

# LLMOps Gateway 拆解

你的目标是把一个 LLM/Agent 产品设计成可观测、可治理、可控成本的生产系统。

## 输入
- 当前模型调用方式。
- 模型和 provider 列表。
- 用户/session 标识。
- prompt 版本、工具调用、成本、延迟和错误信息。
- 自托管、隐私、合规或企业部署要求。

## 工作流
1. 保持 OpenAI-compatible 客户端接口，降低迁移成本。
2. 把请求路由到统一 gateway。
3. 记录 request、response、model、provider、latency、cost、user/session、prompt version、error。
4. 定义 fallback、retry、rate limit、budget、cache 策略。
5. 增加 replay/debug workflow，能复盘失败请求。
6. 为运营者提供 dashboards：cost、latency、error、sessions、prompts、models。
7. 把高风险动作放进 approval tier 和 audit log。

## 输出格式
```markdown
## LLMOps Gateway Plan
- Client interface:
- Gateway endpoint:
- Providers:
- Observability fields:
- Routing/fallback:
- Cache/budget:
- Debug workflow:
- Security risks:
- Verification command:
```

## 验收
- 单个请求能从 user/session 追到 model/provider 和最终输出。
- provider 切换不需要改业务层。
- 每个成本/安全规则都有可观察计数器。
