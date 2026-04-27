# 用户调研计划：Agent Token Audit

日期：2026-04-28  
目标：验证谁真的为长任务 Agent Token 成本付费

## 1. 招募目标

14 天内找：

- 100 个候选用户。
- 30 个私信/邮件触达。
- 15 个有效访谈。
- 5 个真实 trace / 账单 / session 样本。
- 3 个 Local Audit 试用。
- 1 个付费 audit 意向。

## 2. 候选用户来源

| 来源 | 搜索词 | 目标 |
|---|---|---|
| X/Twitter | Claude Code token cost | 晒账单、讨论成本的人 |
| X/Twitter | Claude Code compact | 手动优化上下文的人 |
| X/Twitter | OpenClaw cost / token | OpenClaw 高频用户 |
| X/Twitter | AI agent token usage | 做 dashboard / observability 的人 |
| GitHub | Claude Code skill / OpenClaw / GStack | agent workflow 作者 |
| HN / Reddit | Claude Code expensive / API bill | 抱怨成本和限制的人 |
| 技术社群 | Claude Code / Codex / Cursor Agent | 国内重度用户 |

## 3. ICP 优先级

P0：

- Claude Code / Codex / OpenClaw 每周使用 10 小时以上。
- 有 API 账单或 Max 订阅。
- 最近一个月遇到过 token、context、limit、cost 问题。
- 愿意展示一段脱敏 trace。

P1：

- AI agency / 自动化服务商。
- 小团队 CTO / AI infra 负责人。
- 做 agent observability / workflow tooling 的开发者。

P2：

- AI KOL。
- 泛 AI 重度用户。
- 低频 coding agent 用户。

## 4. 私信模板

英文：

```text
Hey, saw your post about Claude Code / agent token usage.

We are researching why long-running agents burn tokens and where the waste actually comes from: repeated context, tool outputs, model routing, compact timing, cached token misses.

Would you be open to a 20-min call? We are not pitching a product. We are collecting real traces and bills to understand whether a local Token Audit is useful.

If useful, we can send back a short report showing where your agent likely wastes tokens and what can be reduced.
```

中文：

```text
看到你之前聊 Claude Code / Agent token / 上下文成本。

我们现在在做一个立项前调研，想搞清楚长任务 Agent 到底为什么烧 token：重复上下文、工具输出、模型路由、compact 时机、缓存没命中。

方便约 20 分钟聊一下吗？现在不是推产品，只想收集真实任务、账单和失败案例。可以只看脱敏数据。

如果有价值，我们会回给你一份简短 Token Audit，告诉你哪里可能在浪费 token。
```

## 5. 访谈问题

### 最近一次真实任务

1. 你最近一次让 Agent 跑超过 10 分钟的任务是什么？
2. 用了什么工具？
3. 它读了哪些上下文？
4. 中间你介入了几次？
5. 最后成功了吗？

### 成本

6. 你知道那次大概消耗多少 token 或多少钱吗？
7. 你最近一个月 Agent / AI coding 成本大概多少？
8. 哪一次让你觉得“这个成本不合理”？
9. 你现在怎么省 token？

### 隐私

10. 哪些数据你能给第三方服务？
11. 哪些数据必须本地处理？
12. BYOK、Local Audit、Hosted API 你更接受哪个？

### 付费

13. 如果本地 audit 能指出 30%-80% 的浪费来源，你愿意试吗？
14. 如果每月能省 500 美元，你愿意为一次 audit 付多少？
15. 你愿意现在提供一段脱敏 trace 吗？

## 6. 访谈评分

| 维度 | 高 | 中 | 低 |
|---|---|---|---|
| 痛点强度 | 有真实账单/限额/失败 | 有感知但无数据 | 只是兴趣 |
| 数据可得性 | 能给 trace/账单 | 能口述 | 不愿提供 |
| 隐私阻力 | 可 Local Audit | 只能本地看 | 完全不能碰 |
| 付费意愿 | 愿意付 audit | 愿意试用 | 只愿免费 |
| 传播价值 | 有公开影响力 | 小圈子影响力 | 无 |

## 7. 决策标准

继续做 V1：

- 10 个访谈里至少 5 个痛点强度高。
- 至少 3 个愿意给 trace。
- 至少 1 个愿意付费 audit。
- 隐私阻力主要能通过 Local Audit / BYOK 解决。

暂停：

- 用户只想要开源脚本。
- 用户不愿给任何数据。
- 成本痛点低于开发复杂度。
- 用户认为模型商原生 caching 足够。

