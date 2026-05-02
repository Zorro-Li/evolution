# 03 综合方法报告

日期：2026-04-28  
目的：总结各家公司怎么做，我们能参考什么，下一步怎么执行

## 1. 最终判断

当前方向值得继续做 14 天深度验证。产品形态优先级：

1. Local Token Audit。
2. BYOK Optimization Proxy。
3. Hosted Long-task Agent API。
4. Enterprise Self-hosted / VPC。

最窄切口：

> 给 Claude Code / Codex / OpenClaw / 自研 Agent 高频用户做一次本地 Token Audit，找出长任务为什么烧钱，并给出可验证的降本路径。

核心原因：

- X/Twitter 已出现真实成本痛点、dashboard、compact 调参、计费异常、YC 背书竞品。
- 官方模型商都在做 prompt/context caching，说明成本优化方向成立。
- AI Infra 产品已经教育用户接受 gateway、observability、routing、budget、cache。
- 隐私信任门槛很高，Local Audit 是当前最低阻力入口。

## 2. 方法库：别人怎么做

### 方法 1：API / 企业数据排除训练

代表公司：

- OpenAI
- Anthropic
- AWS Bedrock
- Cursor
- GitHub Copilot

他们怎么做：

- 把 API / enterprise 数据与消费级数据分开。
- 明确输入输出默认排除训练。
- 企业提供 ZDR、SOC 2、DPA、SSO、audit log。
- 对子处理方和模型商做披露。

我们参考：

- V0 隐私说明第一句话写：用户输入、输出、代码、trace 默认排除训练。
- 三档数据路径：Local Audit、BYOK Proxy、Hosted API。
- Hosted API 上线前准备 Trust & Privacy 单页。

### 方法 2：短留存 + 用户删除权

代表公司：

- CloudConvert
- Smallpdf
- iLovePDF
- OpenAI / Anthropic ZDR

他们怎么做：

- 上传文件处理后短期删除。
- 日志保留期单独说明。
- 用户可以手动删除。
- 企业用户可签 DPA 或 ZDR。

我们参考：

- Local Audit：raw data 不离开本地。
- BYOK Proxy：raw prompt 默认 24 小时删除，trace metadata 保留 30 天。
- Hosted API：默认短留存，企业 ZDR。
- UI 和文档里展示“删除任务数据”按钮。

### 方法 3：Prompt / Context Caching

代表公司：

- OpenAI
- Anthropic
- Google Gemini

他们怎么做：

- 识别长 prompt 或上下文 prefix。
- 缓存重复上下文。
- 返回 cached tokens 或 cache read/write 指标。
- 用成本和延迟作为核心价值。

我们参考：

- Token Audit 报告必须拆出：
  - 重复上下文。
  - 可缓存前缀。
  - cache miss 原因。
  - cache hit 后账单变化。
- Benchmark 表里加入 `cached_tokens`。

### 方法 4：Gateway / Proxy

代表公司：

- Portkey
- Helicone
- LiteLLM
- Compresr

他们怎么做：

- 统一模型 API 入口。
- 提供 routing、fallback、retries、cache、budget、rate limit。
- 用 proxy 方式降低接入成本。
- 部分产品提供 self-hosted 或 BYOK。

我们参考：

- 第二阶段做 BYOK Optimization Proxy。
- 支持 OpenAI / Anthropic / Google / OpenRouter。
- 内部优先做 4 个功能：模型路由、缓存建议、预算告警、trace attribution。

### 方法 5：Observability / Trace / Eval

代表公司：

- LangSmith
- Helicone
- Braintrust
- Langfuse

他们怎么做：

- 记录 agent runs、tool calls、tokens、latency、cost。
- 提供 trace tree，帮助定位失败步骤。
- 把 eval 和 observability 结合。
- 让工程团队调试生产 agent。

我们参考：

- Token Audit 报告按 trace tree 输出。
- 每一步标注：模型、输入、输出、工具调用、成本、重复上下文、优化建议。
- 成本下降必须同时评估质量。

### 方法 6：Compact / Memory Optimization

代表对象：

- Claude Code 社区
- OpenClaw 社区
- Compresr
- QMD / local search 工具

他们怎么做：

- 裁剪工具输出。
- 会话记忆写入本地文件。
- 用 compact window 控制长上下文。
- 用本地搜索替代全文塞入。

我们参考：

- Local Audit 检测：
  - 工具输出过长。
  - session history 重复加载。
  - 全文档塞入。
  - compact 太晚触发。
  - local retrieval 缺失。
- 报告给出 compact threshold 建议。

### 方法 7：Model Routing / Tiering

代表对象：

- Portkey
- OpenRouter
- OpenClaw 用户实践
- Helicone / LiteLLM

他们怎么做：

- 简单任务走便宜模型。
- 复杂任务走强模型。
- reasoning 模型限制在高价值步骤。
- heartbeat、classification、parsing 走 cheap / local 模型。

我们参考：

- Audit 报告给出任务复杂度分层。
- 标出“高价模型浪费步骤”。
- 推荐 cheap model / local model / strong model 的路由规则。

### 方法 8：异常账单处理

代表对象：

- Anthropic / Hermes.md 事件
- OpenAI / API usage dashboard
- Infra 产品的 budget alert

他们怎么做：

- 提供 usage dashboard。
- 出现异常时退款或 credits。
- 用 budget、rate limit、alert 限制损失。

我们参考：

- Proxy 阶段加入：
  - daily spend cap。
  - per-task spend cap。
  - abnormal token spike alert。
  - manual approval over threshold。
- 条款中写清计费异常处理机制。

## 3. 公司方法对照表

| 公司/产品 | 他们解决什么 | 他们怎么做 | 我们参考什么 |
|---|---|---|---|
| OpenAI | API 数据信任、prompt caching、Codex | 数据排除训练、Business Terms、cached token 指标 | 数据政策、责任条款、benchmark 指标 |
| Anthropic | Claude Code、prompt caching、ZDR | 商业用户数据保留、Claude Code 文档、cache read/write | Claude Code 用户调研、缓存报告 |
| AWS Bedrock | 企业隐私 | 不训练、不分发、云安全体系 | 企业版隐私标杆 |
| Google Vertex / Gemini | 数据治理和 context caching | 数据治理文档、context cache | 长上下文缓存策略 |
| Cursor | coding tool 企业信任 | Privacy Mode、SOC 2、ZDR、server-side prompt building 说明 | Trust & Privacy 页面结构 |
| GitHub Copilot | coding assistant 信任 | Trust Center | 集中式信任文档 |
| Helicone | LLM observability / gateway | trace、cost、cache、agent debugging | 成本可视化和 gateway 心智 |
| Portkey | AI Gateway | routing、fallback、cache、budget | BYOK Proxy 功能结构 |
| LiteLLM | 开源 proxy | virtual keys、budget、cache、self-hosted | 开源替代方案与自托管路线 |
| LangSmith | agent trace / eval | observability、tracing、evaluation | trace-level 成本归因 |
| Braintrust | eval / observability 分类 | 市场教育、工具对比 | 市场分类语言 |
| Compresr | 长上下文压缩 | agentic proxy、Claude Code / OpenClaw 接入 | 直接竞品，提示差异化 |
| CloudConvert | 文件上传信任 | 短留存、删除权、安全页、条款 | prompt/trace 短留存文案 |
| Smallpdf | 文件安全 | 一小时删除、ISO/GDPR | 简洁隐私承诺 |
| iLovePDF | 文件处理安全 | 两小时删除、TLS | 明确保留期 |
| Devin | 企业 AI engineer | 企业接入和安全 | 长期企业产品参考 |

## 4. 我们应该采用的组合方案

### 阶段 1：Local Token Audit

目标：

- 拿真实 trace。
- 避开隐私阻力。
- 建立 first proof。

交付物：

- CLI 或手工模板。
- Markdown audit report。
- before/after cost table。
- 优化建议 checklist。

报告字段：

| 字段 | 内容 |
|---|---|
| Task summary | 任务类型、工具、模型、时长 |
| Token footprint | input、output、cached、cost |
| Waste sources | 重复上下文、工具输出、全文塞入、model mismatch、cache miss |
| Risk | 隐私数据、secret 泄露、异常账单 |
| Recommendations | compact、routing、local search、cache、budget |
| Estimated savings | 保守、中性、激进三档 |

### 阶段 2：BYOK Optimization Proxy

目标：

- 用户自带 Key。
- 我们提供优化层。
- 低信任成本验证持续使用。

核心功能：

- Model routing。
- Prompt/context cache guidance。
- Tool output trimming。
- Budget alerts。
- Trace-level cost attribution。

### 阶段 3：Hosted Long-task Agent API

目标：

- 降低接入门槛。
- 做成可售卖 API。

上线前置条件：

- Trust & Privacy 页面。
- 试点条款。
- 子处理方列表。
- 删除权。
- ZDR / enterprise option。
- 异常账单处理流程。

### 阶段 4：Enterprise Self-hosted / VPC

目标：

- 服务高隐私客户。
- 提供高客单价版本。

需要能力：

- Self-hosted deployment。
- SSO / RBAC。
- Audit log。
- DPA。
- Dedicated support。

## 5. 产品包装建议

主包装：

> Agent Token Audit

副标题：

> Find where long-running agents burn tokens, then reduce repeated context, cache misses, bad routing, and tool-output waste.

中文：

> 找出长任务 Agent 为什么烧钱，再减少重复上下文、缓存未命中、错误路由和工具输出浪费。

避免的包装：

- 新模型。
- 通用 Agent 平台。
- 泛泛的上下文工程框架。

理由：

- 新模型需要极高信任和技术证明。
- 通用 Agent 平台竞争太宽。
- Token Audit 可以用真实账单和 trace 验证。

## 6. 14 天执行任务

### Day 1：来源补全

- 补 20 条 X/Twitter 证据。
- 补 Compresr、Helicone、Portkey、LiteLLM 的价格和安全页。
- 形成 100 个候选用户名单。

### Day 2-3：用户触达

- 发 30 条私信。
- 目标：约 10 场访谈。
- 优先对象：Claude Code / OpenClaw / GStack / Codex 高频用户。

### Day 4-7：访谈和 trace

- 完成 8-10 场访谈。
- 拿 3 个 trace 或账单截图。
- 记录隐私阻力和付费意愿。

### Day 8-10：Local Audit 样例

- 做 3 个 audit report。
- 输出 before/after token footprint。
- 标注节省来源。

### Day 11-12：Benchmark

- 用 `benchmark_protocol.md` 跑 2 个内部任务。
- 加上 3 个用户样本。
- 计算成本下降和质量变化。

### Day 13-14：决策材料

- 汇总用户痛点。
- 汇总付费意愿。
- 汇总隐私阻力。
- 给出 V1 / 继续调研 / 暂缓判断。

## 7. 进入 V1 的判断门槛

进入 V1：

- 15 场访谈里至少 5 个高痛点用户。
- 至少 3 个用户愿意提供 trace。
- 至少 1 个用户愿意为 audit 付费。
- 3 个任务类型稳定降本 50% 以上。
- 1 个任务类型降本 80% 以上。
- 输出质量不低于 baseline。

继续调研：

- 痛点存在，但付费意愿不足。
- trace 数量不足。
- 隐私阻力高，但 Local Audit 仍能推进。

暂缓：

- 用户只要免费开源脚本。
- 用户拒绝提供任何 trace。
- 成本下降无法稳定复现。
- 用户认为模型商原生缓存已经够用。

## 8. 最后建议

当前团队应把问题从“是否卖 Agent API”改成：

> 是否能通过 Local Token Audit 在 14 天内证明：高频 Agent 用户有明确账单痛点、愿意提供 trace、愿意为降本结果付费。

下一步先做两件事：

1. 建立 100 个候选用户名单。
2. 做 3 个 Local Token Audit 样例。

