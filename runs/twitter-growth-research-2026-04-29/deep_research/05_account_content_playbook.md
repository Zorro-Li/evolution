# ManXis Twitter/X 账号内容运营手册

调研日期：2026-04-29  
账号对象：
- 增长创始人：[@xiaoyuZorro](https://x.com/xiaoyuZorro)
- 项目账号：[@Manxis_Lab](https://x.com/Manxis_Lab)
- 技术创始人：技术博士账号，确认 handle 后替换到文档

当前观察：
- `@xiaoyuZorro`：约 1,181 关注者，已经绑定 ManXis，近期发过 YC-Bench / token 成本内容。
- `@Manxis_Lab`：0 帖、2 关注者，bio 是泛 AI Agent 表达，适合马上收窄到长任务 Agent API / token 成本 / 上下文控制。

## 1. 三个账号的分工

| 账号 | 核心任务 | 内容关键词 | 最重要目标 |
|---|---|---|---|
| @xiaoyuZorro | 增长、用户、商业、叙事、招募 design partner | token 账单、用户痛点、试点、创业过程、AI Agent 市场 | 拿到真实任务样本和用户关系 |
| 技术博士 | 技术可信度、benchmark、架构、实验、论文/工程判断 | benchmark、context engineering、agent framework、failure analysis、system design | 让技术人相信这个团队真懂 |
| @Manxis_Lab | 官方证据、demo、release、FAQ、转化 | demo、API、benchmark、privacy、docs、waitlist | 把流量转成试用和试点 |

一句话分工：

```text
xiaoyuZorro 负责让人感兴趣。
技术博士负责让人相信。
ManXis Lab 负责让人行动。
```

## 2. 账号定位

### @xiaoyuZorro

当前 bio 可以优化成：

```text
Co-founder & growth @Manxis_Lab
Building infra for long-running AI agents.
Token cost, agent workflows, GTM.
Looking for expensive agent tasks to benchmark.
```

中文人设：

```text
ManXis 增长负责人。专门找高频 Agent 用户、真实长任务和高 token 账单，把产品从实验推向试点。
```

你账号的内容调性：
- 真实、直接、有创业现场感。
- 可以讲中文，也要逐步增加英文。
- 多问问题，多找人，多转发用户反馈。
- 用“我正在找真实任务”替代“我们很厉害”。

### 技术博士账号

建议 bio：

```text
Building long-running AI agent infra @Manxis_Lab.
Researching context engineering, token efficiency, and reliable agent workflows.
PhD in [field].
```

技术博士的内容调性：
- 技术深、证据硬、表达克制。
- 每条内容尽量有实验、图、日志、代码片段或论文观点。
- 少发泛泛的 AI 感慨，多发“我测了什么，发现了什么”。
- 英文优先，中文可同步翻译。

### @Manxis_Lab

当前项目号 bio 建议改成：

```text
Long-task Agent API.
Cut token waste and control context for coding/research agents.
Private benchmark beta.
Built by @xiaoyuZorro + [tech handle].
```

项目账号的内容调性：
- 官方、清晰、可验证。
- 每条都服务 demo、benchmark、waitlist、docs、FAQ。
- 少发抽象愿景，多发前后对比。

## 3. 三个账号分别发什么

### 你发什么：增长创始人账号

你发 6 类内容：

| 类型 | 内容 | 目的 | 频率 |
|---|---|---|---|
| 用户问题 | “谁在用 Agent 跑长任务？最贵的一次花了多少钱？” | 找样本 | 每天 1 条 |
| 创业过程 | “今天我们测了 YC-Bench，单轮结果很好，多轮还在拉。” | 建信任 | 每天 1 条 |
| 商业判断 | “Agent 产品的毛利会被 token 成本吃掉。” | 吸引 founder/CTO | 每周 3 条 |
| 案例转述 | “一个用户的长调研任务，从 $X 降到 $Y。” | 社交证明 | 每周 2 条 |
| 试点招募 | “找 10 个高频 Agent 用户跑私密 benchmark。” | 转化 | 每周 2 条 |
| 竞品评论 | Cursor、Claude Code、Codex、LangChain 更新点评。 | 进入讨论流 | 每天回复/转发 |

你账号的开局帖：

```text
我们在做 ManXis，一个面向长任务 AI Agent 的 API 层。

现在重点很简单：把长任务里的 token 浪费压下去。

合伙人跑 YC-Bench 单任务时，token 可以压到非常低；多轮任务平均还有很多坑。

我接下来会公开记录：
- 哪些任务能省
- 哪些任务省不了
- token 成本怎么测
- 找 10 个真实用户任务做 benchmark
```

你账号的征集帖：

```text
找 10 个高频 Agent 用户。

如果你经常用 Cursor / Claude Code / Codex / LangChain 跑长任务，且 token 账单已经开始肉疼，可以把一个匿名任务发我。

我们用 ManXis 跑 before/after benchmark，给你一份 token、成本、耗时、成功率对比。
```

你账号的观点帖：

```text
Agent 的下一轮竞争会很现实：谁能把长任务跑稳，谁能把账单压住。

短 prompt demo 很容易惊艳。
真正贵的是多轮、长上下文、多工具、多文件任务。

我们现在只盯这个问题。
```

### 技术博士发什么：技术创始人账号

博士发 6 类内容：

| 类型 | 内容 | 目的 | 频率 |
|---|---|---|---|
| Benchmark | YC-Bench、coding task、research task 的实验设置和结果。 | 技术可信度 | 每周 2 条 |
| 架构解释 | 长任务为什么浪费 token；上下文怎么压缩；任务状态如何保存。 | 教育市场 | 每周 2 条 |
| Failure analysis | 哪些任务失败、为什么失败、多轮为什么难。 | 可信和专业 | 每周 1-2 条 |
| Research notes | 论文、系统设计、agent memory、context engineering。 | 技术权威 | 每周 2 条 |
| Code/log snippets | 局部日志、伪代码、图表。 | 可验证 | 每周 2 条 |
| 技术问答 | 回复 Cursor / LangChain / Vercel / OpenAI 相关技术讨论。 | 进入社交图谱 | 每天 10-20 条回复 |

博士账号第一条帖：

```text
I’m building the technical layer behind @Manxis_Lab.

The problem we care about:
long-running agents repeat context, re-derive state, and burn tokens across multi-step workflows.

We are benchmarking ways to reduce token usage while keeping task quality stable.

I’ll share experiments, failures, and architecture notes here.
```

博士账号 benchmark 帖：

```text
Benchmark note:

Task: YC-Bench [task name]
Baseline: [tokens], [cost], [result]
ManXis run: [tokens], [cost], [result]

What worked:
- [point 1]
- [point 2]

What still fails:
- [point 1]
- [point 2]
```

博士账号技术解释帖：

```text
Why long-running agents waste tokens:

1. Repeating full context across steps
2. Re-explaining task state to every tool call
3. Keeping irrelevant history alive
4. Losing compact intermediate representations
5. Re-running exploration after context drift

The hard part is preserving useful state while deleting noise.
```

博士账号 failure 帖：

```text
A result we did not like:

Single-turn benchmark looked great.
Multi-turn performance dropped.

Reason:
the agent saved tokens in early steps, but lost important state later.

Token reduction without state preservation is a fake win.
We are changing the evaluation around this.
```

## 4. 项目账号发什么：@Manxis_Lab

项目账号发 7 类内容：

| 类型 | 内容 | 目的 | 频率 |
|---|---|---|---|
| Launch foundation | 我们是谁、解决什么、适合谁。 | 建立账号基础 | 第一周 3 条 |
| Demo | 任务前后对比视频/截图。 | 让用户看懂 | 每周 1-2 条 |
| Benchmark | 标准任务表、token/cost/质量。 | 证明效果 | 每周 2 条 |
| Release | 新功能、新集成、新模型支持。 | 持续存在感 | 每周 1 条 |
| FAQ | 隐私、日志、安全、误操作、价格。 | 降低顾虑 | 每周 1 条 |
| Use case | coding、research、多文件、多工具场景。 | 场景转化 | 每周 2 条 |
| Design partner CTA | 招募试点用户。 | 转化 | 每周 2 条 |

项目账号第一条帖：

```text
Introducing ManXis Lab.

We are building an API layer for long-running AI agents.

Our first goal:
reduce token waste in complex coding and research workflows while preserving task quality.

We are now running private benchmarks with early users.
```

项目账号第二条帖：

```text
What we measure:

- token usage
- estimated cost
- task completion
- output quality
- failure modes
- multi-turn stability

A lower token bill only matters when the task still works.
```

项目账号第三条帖：

```text
Looking for private benchmark partners.

Best fit:
- coding agents
- research agents
- multi-step browser/API workflows
- teams already spending heavily on tokens

Send us one expensive long-running task.
We’ll return a before/after report.
```

项目账号 benchmark 帖：

```text
Benchmark result #001

Task: [task]
Baseline: [tokens] / [$cost]
ManXis: [tokens] / [$cost]
Reduction: [x%]

Quality: [pass/fail/notes]

Full setup below.
```

项目账号 FAQ 帖：

```text
FAQ: Do we store user prompts?

Private benchmark mode:
- task data is used only for the benchmark
- logs can be anonymized
- public case studies require explicit approval
- deletion requests are supported

We are designing privacy as a product feature.
```

## 5. 三个账号怎么配合

### 标准传播链路

1. 博士发技术实验。
2. 你转发，翻译成用户痛点和商业价值。
3. 项目号转发，整理成官方 benchmark。
4. 你在评论区招募下一个真实任务。

示例：

```text
博士：发布 YC-Bench token 对比。
你：这就是我们为什么做 ManXis，长任务账单会吃掉 Agent 产品毛利。
项目号：Benchmark #001: YC-Bench task, token reduced by X%.
你评论：找 10 个更真实的任务继续测，DM 我。
```

### Launch thread 分工

| 时间 | 账号 | 内容 |
|---|---|---|
| T-3 天 | 你 | 为什么长任务 token 成本是问题。 |
| T-2 天 | 博士 | 技术实验：一个任务如何省 token。 |
| T-1 天 | 项目号 | 明天发布 private benchmark beta。 |
| T 日 | 项目号 | 正式 launch thread + demo。 |
| T 日 | 你 | 创始人叙事 + 招募 design partner。 |
| T 日 | 博士 | 技术拆解 + benchmark 细节。 |
| T+1 | 项目号 | FAQ：隐私、安全、适用场景。 |
| T+2 | 你 | 回复汇总 + 用户问题。 |

## 6. 第一周具体排期

### Day 1

| 账号 | 发什么 |
|---|---|
| 项目号 | Introducing ManXis Lab。 |
| 你 | 为什么我们盯长任务 token 成本。 |
| 博士 | 技术问题定义：long-running agents waste tokens。 |

### Day 2

| 账号 | 发什么 |
|---|---|
| 项目号 | What we measure：token、cost、quality、failure。 |
| 你 | 找 10 个高频 Agent 用户。 |
| 博士 | YC-Bench 单任务实验记录。 |

### Day 3

| 账号 | 发什么 |
|---|---|
| 项目号 | Private benchmark partner 招募。 |
| 你 | 评论 Cursor / Claude Code / LangChain 相关帖子 20 条。 |
| 博士 | 为什么多轮任务更难。 |

### Day 4

| 账号 | 发什么 |
|---|---|
| 项目号 | Benchmark #001。 |
| 你 | 把 benchmark 翻译成“每月能省多少钱”。 |
| 博士 | failure analysis：单轮好、多轮差的原因。 |

### Day 5

| 账号 | 发什么 |
|---|---|
| 项目号 | FAQ：隐私和日志。 |
| 你 | 用户访谈记录：高频 Agent 用户真正痛点。 |
| 博士 | context engineering 技术解释。 |

### Day 6

| 账号 | 发什么 |
|---|---|
| 项目号 | Use case：coding agent 长任务。 |
| 你 | 招募企业/团队试点。 |
| 博士 | 回复技术讨论，少发主帖。 |

### Day 7

| 账号 | 发什么 |
|---|---|
| 项目号 | 一周 benchmark 汇总。 |
| 你 | 一周创业复盘：哪些假设被验证。 |
| 博士 | 一周技术复盘：下一步怎么测。 |

## 7. 内容比例

### @xiaoyuZorro

| 内容 | 比例 |
|---|---|
| 用户痛点和提问 | 30% |
| 创业过程和复盘 | 25% |
| 商业判断和市场观察 | 20% |
| benchmark 解读 | 15% |
| 个人可信度和关系 | 10% |

### 技术博士

| 内容 | 比例 |
|---|---|
| benchmark 和实验 | 35% |
| 技术解释 | 25% |
| failure analysis | 20% |
| 论文/系统笔记 | 10% |
| 回复和技术互动 | 10% |

### @Manxis_Lab

| 内容 | 比例 |
|---|---|
| demo / benchmark | 40% |
| release / product update | 20% |
| use case | 15% |
| FAQ / trust | 15% |
| design partner CTA | 10% |

## 8. 当前账号需要马上改的地方

### @xiaoyuZorro

建议把 bio 里的中文身份和英文身份统一。当前 “growth” 和“软件工程师”混在一起，最好突出增长负责人和 ManXis。

推荐：

```text
Co-founder & growth @Manxis_Lab
Long-running AI agents | token cost | agent workflows
Looking for expensive agent tasks to benchmark
ex-@billion_global | vyper 中文社区
```

### @Manxis_Lab

当前 “next-generation AI Agents / general-purpose agentic intelligence” 太泛。建议改成具体问题。

推荐：

```text
Long-task Agent API.
Reduce token waste and control context for coding/research agents.
Private benchmark beta.
Built by @xiaoyuZorro + [tech handle].
```

项目号第一周必须发 5-7 条基础内容。0 帖状态会降低信任和转化。

### 技术博士

如果账号还没开始做，第一天只做三件事：

1. 改 bio，绑定 `@Manxis_Lab`。
2. 发第一条 technical mission。
3. 连续 3 天回复 Cursor / LangChain / Vercel / Claude Code / Codex 相关技术讨论。

## 9. 衡量标准

第一阶段别盯粉丝，盯商业信号。

| 指标 | 7 天目标 | 30 天目标 |
|---|---:|---:|
| 真实任务样本 | 5 | 30 |
| design partner 对话 | 3 | 15 |
| benchmark case | 2 | 10 |
| 项目号关注者 | 50 | 300 |
| 你账号新增关注 | 100 | 500 |
| 博士账号新增关注 | 50 | 300 |
| DM 有效回复 | 5 | 30 |

## 10. 最小执行原则

每天只做 4 件事：

1. 项目号发 1 条证据。
2. 你发 1 条用户/商业/试点相关内容。
3. 博士发 1 条技术/实验/回复。
4. 三个账号一起在评论区找目标用户。
