---
type: concept
title: Manxis Target Company Research 2026 05 03
---

# ManXis 目标公司与触达计划

日期：2026-05-03

## 核心判断

ManXis 当前应找“已经有长任务 agent trace 的公司”，优先级高于泛行业公司。最值钱的客户信号是：长任务、重复上下文、工具调用多、失败重试多、月度 LLM/agent 成本超过 500 美元、有能力分享匿名 trace。

## ICP 排序

| 优先级 | ICP | 代表对象 | 为什么现在找 |
|---|---|---|---|
| P0 | Coding agent 高频团队 | Cursor-heavy startup、Claude Code/Codex 重度用户、AI coding agency | 任务可复现，token 成本可量化，before/after 容易展示。 |
| P0 | LLM observability / trace 用户 | Helicone、Langfuse、LangSmith 用户 | 已经有日志和 trace，能快速做 Token Audit。 |
| P0 | AI automation agency | 给客户交付 agent workflow 的团队 | 成本直接影响毛利，愿意用工具降交付成本。 |
| P1 | AI workflow SaaS | Lindy、Gumloop、Zapier agents、n8n AI workflow 生态 | 多客户、多工具、多上下文，成本压力会随规模放大。 |
| P1 | AI app builder / coding product | Replit Agent、Bolt、Lovable、v0 类产品团队 | 任务形态直观，适合 benchmark 和公开案例。 |
| P2 | 企业内部 AI 平台团队 | 金融、法律、客服、运营自动化平台组 | 预算更大，采购和安全周期更长。 |

## 第一批公司名单

### 竞品研究

| 公司 | 目标动作 | 产出 |
|---|---|---|
| Compresr | 拆官网、docs、YC 页面、接入方式、claim。 | 竞品卡、差异化表、可复制文案。 |
| The Token Company | 拆 context bloat 定义、场景覆盖、市场话术。 | ManXis 问题定义升级稿。 |

### 集成和渠道研究

| 公司 | 目标动作 | 产出 |
|---|---|---|
| Helicone | 研究 trace/cost/cache 数据结构和用户入口。 | Helicone trace audit 集成方案。 |
| Langfuse | 研究 open-source/self-hosted 机制和 trace export。 | Langfuse import + audit 方案。 |
| LangSmith | 研究 agent eval、trace、dataset、deployment 流程。 | LangSmith-heavy team outbound list。 |
| Portkey | 研究 gateway/cache/budget 企业包装。 | ManXis gateway-compatible enterprise pitch。 |

### Design partner 研究

| 公司 / 群体 | 目标动作 | 产出 |
|---|---|---|
| Cursor-heavy startup | 找 30 个公开分享 Cursor / Claude Code 工作流的人。 | 30 人名单 + 10 条个性化 DM。 |
| AI automation agency | 找 20 个接 AI 自动化项目的团队。 | 20 家名单 + ROI 话术。 |
| Lindy / Gumloop / Zapier agents 生态 | 找 workflow automation 用户和服务商。 | 业务 agent 成本审计 offer。 |
| Replit/Bolt/Lovable/v0 用户群 | 找公开 app-builder agent 长任务案例。 | app-builder benchmark 任务集。 |

## 触达话术

### 给 coding agent 用户

```text
Saw you’re using Cursor / Claude Code / Codex for long-running coding tasks.

We’re building ManXis, a token audit and context optimization layer for long-task agents.

If you have one expensive repo task, we can run a private before/after report:
- token footprint
- cost
- runtime
- retries
- quality risks

Default: local/redacted trace only.
```

### 给 AI agency

```text
You probably run similar agent workflows across multiple client projects.

ManXis audits where those workflows waste tokens:
repeated context, verbose tool outputs, weak memory boundaries, failed retries.

The output is a cost report plus workflow patches.
```

### 给 LLM observability 用户

```text
If you already have Helicone / Langfuse / LangSmith traces, ManXis can use them as input.

We return a token waste map:
which context repeats, which tool outputs should be compressed, which steps cause retries, and where caching can hit.
```

## 14 天执行计划

| 天数 | 动作 | 验收 |
|---|---|---|
| Day 1 | 完成 Compresr / The Token Company 深拆。 | 2 张竞品卡 + 差异化表。 |
| Day 2 | 选 3 个内部 benchmark 任务。 | baseline tokens/cost/runtime/quality。 |
| Day 3-4 | 整理 50 个目标联系人。 | 每个联系人有来源、场景假设、触达理由。 |
| Day 5-7 | 每天发 10 条个性化 DM。 | 30 条 DM，5 个回复。 |
| Day 8-10 | 做 5 个 discovery call。 | 每个 call 拿到任务类型、成本、现有方案、隐私限制。 |
| Day 11-13 | 跑 3 个本地/匿名 Token Audit。 | 3 份 before/after 报告。 |
| Day 14 | 定价和复盘。 | 1 个愿意付费或继续试点的客户。 |

## 筛选标准

合格 lead 需要满足 3 个以上：

- 每周运行长任务 agent。
- 单任务超过 50k tokens 或 20 次模型/工具调用。
- 月 LLM / agent 成本超过 500 美元。
- 有失败重试、上下文丢失、compact 后质量下降问题。
- 愿意提供 redacted trace 或本地运行样本。
- 能找到 founder、CTO、AI lead、platform lead。

## 推荐动作

先做 30 个 Cursor / Claude Code / Codex 高频用户名单，再做 Helicone / Langfuse / LangSmith 用户集成方案。ManXis 当前需要真实 trace 和付费意愿，直接面向长任务 agent 用户拿证据。
