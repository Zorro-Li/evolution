# Capitalist Codex Task Dispatch

日期：2026-05-03

## 投资人原则

Codex 的时间只投到能产生资产、收入、渠道或护城河的任务。每个任务必须留下可复用文件、可验证指标和下一步商业动作。

## P0 任务

| # | 任务 | 预期回报 | 执行命令 / 产物 | 验收标准 | 最小验证 | 现在优先级 |
|---:|---|---|---|---|---|---|
| 1 | 上传 Jarvis/Codex 自有归纳 Skill 到 youMind | 把进化 workspace 的拆解能力变成外部分发资产，增加获客入口 | `runs/youmind-jarvis-skill-upload-2026-05-03/payloads.json` + youMind 创建 13 个 Skill | youMind “我的技能”出现 13 个 Jarvis Skill，名称和指令完整；DBS/dontbesilent 全部排除 | 搜索 `Jarvis 进化 Skill 总入口` 能打开 | Skill 是可传播产品，先占分发入口 |
| 2 | Jarvis Skill 商品化 landing copy | 把自有 Skill 从工具变成付费咨询入口 | `runs/jarvis-youpublish-2026-05-03/landing.md` | 产出 1 页销售页、3 个套餐、10 条转化 FAQ | `rg \"套餐\" runs/jarvis-youpublish-2026-05-03/landing.md` | 上传 Skill 后需要承接流量 |
| 3 | ManXis Local Token Audit 销售冲刺 | 用 $500 pilot 验证真实付费 | `runs/manxis-outbound-2026-05-03/first_20_messages.md` | 20 条定制私信，5 个 P0 线索有个性化理由 | `wc -l first_20_messages.md` + 手动检查前 3 条 | 当前已有线索包，缺触达 |
| 4 | Helicone / Langfuse trace import spec | 让 ManXis 可吃现有 LLM observability 数据 | `runs/manxis-trace-import-spec-2026-05-03/spec.md` | 定义输入字段、隐私处理、样例 JSONL、审计输出 | `python3 -m json.tool sample_trace.jsonl` 或样例解析脚本通过 | 设计伙伴最容易提供 trace |
| 5 | company-research-agent Codex provider 稳定化 | 把 demo 变成可重复工具 | `tools/company-research-agent/CODEX_PROVIDER.md` + smoke test | 单命令启动、单命令提交公司、失败状态清晰 | `curl -s http://127.0.0.1:8000/` 返回 Alive | 当前 demo 已跑通，需要工程化 |

## P1 任务

| # | 任务 | 预期回报 | 执行命令 / 产物 | 验收标准 | 最小验证 | 现在优先级 |
|---:|---|---|---|---|---|---|
| 6 | YouMind Skill 发布运营台账 | 把技能上传变成可复盘增长实验 | `runs/youmind-jarvis-skill-upload-2026-05-03/upload_log.md` | 每个 Skill 有 URL、状态、标签、下一步动作 | 13 行状态表 | 批量上传后要知道哪个能带来点击 |
| 7 | Jarvis 总入口改成 youMind 友好版 | 减少用户进入后的迷路率 | `runs/youmind-jarvis-skill-upload-2026-05-03/jarvis-ywm-optimized.md` | 总入口明确 8 类问题和路由方式 | 300 字描述 + 指令能独立工作 | youMind 用户需要简单入口 |
| 8 | X 创作者 Skill 第二批蒸馏 | 扩大 Jarvis 可调用商业知识库 | `runs/x-creator-watch/2026-05-03/` | 至少 4 个创作者：来源、分析、Skill、GBrain payload | `rg \"Installed skill\" runs/x-creator-watch/2026-05-03` | 持续增加外部脑力杠杆 |
| 9 | Jarvis / ManXis 交叉销售路径 | 让自有拆解 Skill 导向 Token Audit | `runs/jarvis-manxis-cross-sell-2026-05-03/playbook.md` | 5 个场景、5 条转化句、3 个报价入口 | `rg \"Token Audit\" playbook.md` | 两条业务线可以互相供血 |
| 10 | Jarvis 远程执行最小队列 | 让资本家任务能异步压给 Codex | `tools/local-agent-queue/` | 本地 queue JSONL、worker、结果回写 Markdown | `python3 worker.py --once` 成功处理样例任务 | 当前任务派发还靠手动，队列能放大执行 |

## 推荐今日执行顺序

1. 完成 Jarvis 自有 Skill 的 youMind 上传。
2. 写 `upload_log.md`，记录每个 Skill 的 URL。
3. 做 ManXis 前 20 条触达消息。
4. 写 Helicone/Langfuse trace import spec。
5. 把 company-research-agent 的 smoke test 固化成脚本。
