# Benchmark 协议：长任务 Agent Token 成本优化

日期：2026-04-28  
用途：验证“Token 成本下降”是否稳定成立

## 1. 核心问题

要验证的不是“某一次省了很多 token”，而是：

- 同一任务类型下，成本下降是否稳定。
- 输出质量是否保持。
- 人工介入次数是否下降。
- 失败率是否没有上升。
- 节省是否来自我们的优化，而非模型商原生缓存偶然命中。

## 2. 指标

| 指标 | 定义 |
|---|---|
| input tokens | 所有模型调用输入 token 总量 |
| output tokens | 所有模型调用输出 token 总量 |
| cached tokens | 平台缓存命中 token |
| billable cost | 按模型商价格计算的总成本 |
| wall time | 任务从启动到完成时间 |
| tool calls | 工具调用次数 |
| retry count | 重试/返工次数 |
| human interventions | 人工介入次数 |
| completion quality | 人工或 rubric 评分，1-5 |
| pass/fail | 任务是否达到预设完成条件 |

## 3. 任务集

| 任务 | 描述 | 适合验证的浪费点 |
|---|---|---|
| Repo refactor | 中型 repo 做跨文件重构并跑测试 | 重复读文件、长上下文、tool output |
| Bug investigation | 给定失败日志，让 agent 找根因并修复 | 反复搜索、无效上下文、工具调用膨胀 |
| Long document analysis | 分析多份长文档并输出决策报告 | 全文塞入、检索不足、摘要重复 |
| Multi-step research | 搜索 10+ 来源并综合报告 | 搜索结果冗余、重复摘要、trace 过长 |
| Agent eval run | 对同一 workflow 跑 20 个 case | 重复 system prompt、重复上下文、模型选择不当 |

## 4. 对照组

每个任务跑三组：

| 组别 | 配置 | 目的 |
|---|---|---|
| Baseline | 用户原始 agent 配置 | 获取真实当前成本 |
| Manual Best Practice | 人工 compact、模型分层、减少上下文 | 对比用户自己能做到多少 |
| Optimized Layer | 我们的 audit/optimization layer | 验证增量价值 |

## 5. 成功门槛

进入 V1 的最低门槛：

- 3 个任务类型成本下降 50% 以上。
- 至少 1 个任务类型成本下降 80% 以上。
- completion quality 不低于 baseline。
- pass rate 不低于 baseline。
- human interventions 不高于 baseline。
- 每个任务能解释节省来源：上下文压缩、缓存命中、模型路由、工具输出裁剪、本地检索。

## 6. 报告模板

```md
# Benchmark Case: {任务名称}

## 任务背景
- repo / 数据规模：
- 模型：
- agent 工具：
- 完成标准：

## 结果对比
| 组别 | input | output | cached | cost | time | retries | quality | pass |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Baseline | | | | | | | | |
| Manual Best Practice | | | | | | | | |
| Optimized Layer | | | | | | | | |

## 节省来源
- 

## 失败/风险
- 

## 判断
- 是否可作为公开案例：
- 是否支持 V1：
```

## 7. 推荐执行顺序

1. 先拿 2 个内部任务跑 baseline。
2. 再拿 3 个用户真实 trace 跑 Local Audit。
3. 最后只公开脱敏后的 before/after 图。

