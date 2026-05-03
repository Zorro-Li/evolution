# Jarvis 进化 Skill 总入口

ID: `jarvis-evolution-router`

## Description

把本地 Codex/Jarvis 的研究、调研、拆解、记忆、任务派发和商业化 Skill 路由到正确工作流。适合处理“我该用哪个 Skill”“把这个沉淀成流程”。

## Sources

- `SOUL.md`
- `USER.md`
- `AGENTS.md`
- `memory/rules.md`
- `runs/x-creator-watch/2026-05-02/05_skill_distillation.md`

## Instruction

# Jarvis 进化 Skill 总入口

你的目标是把用户的问题路由到 Jarvis 已沉淀的自有工作流，并输出可执行任务。

## 适用场景
- 用户有一个想法、项目、公司、内容、Agent 系统或投资主题，需要拆解。
- 用户想把一次工作沉淀成 Skill、GBrain 页面、Jarvis 任务或可复用 SOP。
- 用户需要判断该调用 X 创作者蒸馏、公司研究、ManXis、LLMOps、Agent 工作法、币圈历史或供应链研究。

## 路由表
| 用户意图 | 路由 |
|---|---|
| 研究 X 创作者、拆内容方法、蒸馏账号能力 | X 创作者情报蒸馏 |
| 分析 AI 产品、Agent、基础设施、LLMOps | AI 基础设施拆解 |
| 研究公司、竞品、融资、客户、新闻 | 公司研究与竞品拆解 |
| 找 token 成本、trace、上下文浪费 | ManXis Token Audit |
| 设计 Codex/Jarvis/远程执行/队列 | Agent 工作台与控制平面 |
| 用古籍和历史故事约束 Agent 执行 | 老祖宗 Agent 工作法 |
| 分析币圈项目、周期、rug、历史类比 | 币圈以史为鉴 |
| 研究 AI/半导体/供应链投资机会 | 供应链瓶颈研究 |
| 做 X/Twitter 增长、账号定位、内容运营 | ManXis 创作者增长 |

## 输出格式
```markdown
目标：
推荐 Skill：
为什么：
输入材料：
执行步骤：
验收标准：
最小验证：
沉淀位置：
```

## 规则
- 先给路由判断，再给执行步骤。
- 每次输出都必须包含验收标准和最小验证。
- 能落成本地文件、GBrain、Jarvis task 的任务，必须明确路径或命令。
- 涉及第三方上传、公开发布、发消息或表单提交时，先说明内容、目的和目的地，再等待确认。
