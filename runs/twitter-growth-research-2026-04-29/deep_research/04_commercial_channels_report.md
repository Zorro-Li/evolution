# Agent API 商业渠道补充报告

调研日期：2026-04-29  
适用阶段：团队尚未正式成立公司，产品处于 V1 验证和试点前后。  
核心目标：找到愿意给真实任务、真实账单、真实反馈、未来预算的人。

## 1. 商业渠道优先级

当前最该做的商业渠道排序：

| 优先级 | 渠道 | 当前目标 | 成交形态 |
|---|---|---|---|
| P0 | Design Partner / 试点客户 | 拿真实任务和账单数据 | 免费试点、低价试点、LOI |
| P0 | 创始人直销 | 找到高频 Agent 用户和预算方 | 访谈、POC、预付费 |
| P1 | 集成伙伴 | 借已有工具和服务商触达客户 | 分成、联合方案、转介绍 |
| P1 | PLG 自助 API | 让开发者自己试用 | 免费额度、按量计费 |
| P2 | GitHub / VS Code / Slack / Atlassian Marketplace | 做入口和长尾获客 | 插件安装、API 转化 |
| P2 | 云市场 AWS / Azure / GCP | 进入企业采购流程 | Marketplace 私有报价、年度合同 |
| P3 | VC / 大厂 / 校友背书渠道 | 建立信任和引荐 | 投资、合作、试点引荐 |

## 2. 当前阶段主打法：Design Partner

现在团队尚未确定是否成立公司，最稳的商业动作是找 10-20 个 design partners。目标是验证真实痛点和付费意愿，同时避免过早进入复杂采购。

### 目标客户

| 客户类型 | 为什么适合 | 怎么找 |
|---|---|---|
| 高频 Agent 开发者 | 每天跑 Claude Code、Codex、Cursor、OpenHands，能直接感知 token 成本。 | X 回复区、GitHub issue、AI 工具 Discord、朋友介绍。 |
| AI coding / Agent 工具团队 | 自己有用户和长任务场景，token 成本直接影响毛利。 | X 上找 founder、DevRel、infra lead。 |
| AI 应用创业团队 | 有调研、浏览器自动化、客服、数据处理类 Agent 工作流。 | Product Hunt、HN、Indie Hackers、X。 |
| 企业内部 AI 平台团队 | token 量大，有治理、安全、预算问题。 | 校友、VC、大厂朋友、云服务销售引荐。 |
| AI 自动化服务商/咨询公司 | 有客户项目，愿意用新工具降低交付成本。 | LinkedIn、X、微信群、飞书群。 |
| 跨境电商/运营自动化团队 | 长调研、上架、客服、数据处理任务多。 | 国内社群、服务商、朋友介绍。 |

### 给 design partner 的 offer

推荐话术：

```text
我们在做一个长任务 Agent API 层，目标是把复杂任务里的 token 成本显著降下来。

现在找 10 个高频 Agent 用户做私密 benchmark：
- 你给 3-5 个真实长任务
- 我们跑前后对比
- 输出 token、成本、耗时、成功率报告
- 你的数据默认匿名

如果结果能稳定省钱，再谈试点和价格。
```

### Design Partner 成功标准

| 指标 | 目标 |
|---|---|
| 有效访谈 | 20 个 |
| 真实任务样本 | 50 个 |
| 愿意进入试点 | 10 个 |
| 愿意付费 | 3-5 个 |
| 明确预算线索 | 3 个 |
| 可公开匿名 case | 5 个 |

## 3. 创始人直销

创始人直销是当前商业渠道的主线。早期销售的目标是学习、定位和找到高价值 ICP，收入是第二层结果。

### 直销流程

| 阶段 | 动作 | 退出标准 |
|---|---|---|
| 线索列表 | 手动整理 100 个目标账号。 | 每个账号有联系人、场景假设、触达渠道。 |
| 个性化触达 | 每天发 10 条 DM/邮件。 | 每条都提到对方真实场景。 |
| 发现访谈 | 30 分钟诊断当前任务和账单。 | 拿到任务类型、成本、频率、现有方案。 |
| Benchmark POC | 跑 3-5 个任务对比。 | 形成 ROI 表和风险清单。 |
| 试点 | 2-4 周小范围接入。 | 有使用频率、节省金额、稳定性反馈。 |
| 商业化 | 按节省金额、调用量、任务量报价。 | 对方有预算 owner 和采购路径。 |

### 资格判断

| 维度 | 合格信号 |
|---|---|
| Need | 已经在跑长任务 Agent，或正在搭建 Agent workflow。 |
| Cost | 每月 token / API / Agent 工具支出超过 500 美元。 |
| Urgency | 正在因为成本、上下文、失败率影响上线。 |
| Authority | 能找到 founder、CTO、AI lead、platform lead。 |
| Data | 能提供匿名任务样本或测试环境。 |
| Risk | 能接受早期产品试点边界。 |

### 外呼模板

```text
Saw you’re using [Cursor/Claude Code/Codex/LangChain] for long-running agent work.

We’re testing an API layer that reduces token usage on long tasks by up to 80% in some cases.

If you have 2-3 expensive agent tasks, I can run a private before/after benchmark and send back the token/cost report.
```

## 4. 集成伙伴渠道

集成伙伴比广告更适合当前产品，因为他们已经拥有客户信任和使用场景。

### 最值得找的伙伴

| 伙伴类型 | 价值 | 合作方式 |
|---|---|---|
| AI 自动化服务商 | 有客户项目和长任务需求。 | 他们交付，我们提供底层 token 优化层。 |
| Agent 工具开发者 | 有用户和 API/插件入口。 | SDK 集成、联合 demo、收入分成。 |
| 开发者工具 KOL | 有高频 AI coding 用户。 | 试用、benchmark、赞助、联盟返佣。 |
| DevRel / 社区主理人 | 有目标社群。 | 线上分享、案例征集、私密试点。 |
| 云服务 / infra 顾问 | 企业客户有预算。 | 转介绍、联合 POC、服务费分成。 |
| AI 教育/训练营 | 学员正在试工具。 | 课程案例、工具额度、训练营合作。 |

### 分成建议

| 渠道 | 分成 |
|---|---|
| KOL / 推荐人 | 首年收入 10%-20% |
| 服务商 | 项目毛利 20%-40%，或客户订阅首年 15%-25% |
| 技术集成伙伴 | 按用量分成 10%-30% |
| 企业引荐人 | 成交后一次性 success fee |

## 5. PLG 自助 API 渠道

PLG 是未来的规模化渠道，当前只能做最小版本。它需要 docs、API key、billing、dashboard、示例和安全页。

### 最小 PLG 配置

| 模块 | 必须有的内容 |
|---|---|
| Landing page | 一句话价值、demo 视频、benchmark 图、waitlist。 |
| Docs | 5 分钟接入、API 示例、错误码、限制。 |
| Free credits | 让开发者跑 1-3 个长任务。 |
| Dashboard | token before/after、节省金额、任务日志。 |
| Security page | 数据处理、日志保留、加密、删除、免责边界。 |
| Pricing | 按量计费 + 企业联系。 |

### PLG 转销售触发点

| 信号 | 动作 |
|---|---|
| 单用户每周跑 10+ 长任务 | 创始人主动联系。 |
| 单组织出现 3+ 用户 | 询问团队试点。 |
| 月节省金额超过 500 美元 | 提供 Pro/Team 方案。 |
| 任务涉及企业数据 | 转企业安全评估。 |
| API 错误或失败率高 | 主动支持并收集场景。 |

## 6. Marketplace 渠道

Marketplace 适合后期企业成交和采购提速。它本身提供的冷启动流量有限，主要价值是让客户用已有云预算购买，减少采购阻力。

### AWS Marketplace

来源：
- AWS SaaS product guidelines: https://docs.aws.amazon.com/marketplace/latest/userguide/saas-guidelines.html
- AWS ISV Seller Journey: https://aws.amazon.com/marketplace/partners/seller-journey/getting-started/
- AWS Marketplace List & Sell Program: https://aws.amazon.com/partners/programs/saas-factory/

**适合时机**

当我们有 3-5 个企业试点、明确安全架构、可计量用量、稳定账单系统后，再做 AWS Marketplace。

**原因**

AWS SaaS guidelines 要求产品计费、注册、使用状态、支持、架构说明等都能通过 Marketplace 机制承接。Agent API 涉及客户数据，架构图、least privilege、数据处理边界都要提前准备。

### Microsoft Marketplace

来源：
- SaaS offer planning: https://learn.microsoft.com/en-us/azure/marketplace/plan-saas-offer
- Microsoft Marketplace product direction: https://blogs.microsoft.com/blog/2025/09/25/introducing-microsoft-marketplace-thousands-of-solutions-millions-of-customers-one-marketplace/

**适合时机**

当目标客户集中在 Microsoft / Azure / Copilot / 企业办公生态时，Microsoft Marketplace 很有价值。

**适合打法**

把产品包装成企业 AI Agent 成本治理、Agent workflow infra、long-running agent control layer。

### Google Cloud Marketplace

来源：
- Google Cloud Marketplace SaaS products: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas

**适合时机**

目标客户使用 Google Cloud、BigQuery、Vertex AI、Workspace Agent 场景时，可以考虑。

### GitHub Marketplace

来源：
- GitHub Marketplace docs: https://docs.github.com/marketplace
- Creating apps for GitHub Marketplace: https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace?apiVersion=2022-11-28

**适合时机**

如果我们做 GitHub App：自动分析 PR、压缩代码任务上下文、给 coding agent 提供任务缓存和 token report，就可以上 GitHub Marketplace。

**商业价值**

GitHub Marketplace 更像 developer entry point。它适合获客、安装和试用，企业大单仍要靠 founder-led sales 或 marketplace 私有报价承接。

### VS Code / Visual Studio Marketplace

来源：
- VS Code Extension Marketplace: https://code.visualstudio.com/docs/configure/extensions/extension-marketplace
- Visual Studio extension publishing: https://learn.microsoft.com/en-us/visualstudio/extensibility/walkthrough-publishing-a-visual-studio-extension?view=visualstudio

**适合时机**

如果产品有本地 Agent、IDE 插件、token cost panel、任务上下文压缩入口，可以做 VS Code extension。

**商业价值**

这是开发者分发渠道，适合承接 coding agent 用户。插件免费，API 按量收费。

### Slack / Atlassian Marketplace

来源：
- Slack app approval docs: https://docs.slack.dev/admins/managing-app-approvals
- Atlassian Marketplace: https://developer.atlassian.com/platform/marketplace/

**适合时机**

当产品进入企业 workflow，例如 Linear/Jira/Slack 触发长任务 Agent、自动生成 PR、自动调研和报告时，再做。

## 7. 商业包装

商业表达应围绕账单和风险：

| 目标用户 | 表达方式 |
|---|---|
| 开发者 | Same task, fewer tokens. |
| AI founder | Improve gross margin on agent workflows. |
| CTO | Control long-running agent cost and context growth. |
| 企业平台团队 | Agent cost governance and reliability layer. |
| 服务商 | Deliver more AI automation projects with lower runtime cost. |

### ROI 公式

```text
月 Agent token 成本 = 每天任务数 × 单任务平均成本 × 30
节省金额 = 月 Agent token 成本 × 节省比例
可收费金额 = 节省金额 × 10%-30%
```

示例：

```text
每天 100 个长任务
单任务平均 $3
月成本 = $9,000
节省 60% = $5,400
我们收节省金额的 20% = $1,080/月
```

## 8. 价格渠道组合

| 阶段 | 价格方式 | 目的 |
|---|---|---|
| Design Partner | 免费 / $100-$500/月 | 换真实任务、反馈、case。 |
| Early Access | $499-$1,999/月 + usage | 验证付费和支持成本。 |
| Self-serve API | 免费额度 + 按量计费 | 扩大开发者试用。 |
| Team | $2,000-$10,000/月 | 面向小团队和 AI 产品团队。 |
| Enterprise | 年度合同 + SLA + 安全评估 | 面向企业平台团队。 |

## 9. 未来 30 天商业执行计划

| 周期 | 任务 | 产出 |
|---|---|---|
| 第 1 周 | 建立 100 个商业线索表。 | ICP、联系人、当前工具、可能痛点。 |
| 第 1 周 | 发 50 条高质量 DM/邮件。 | 10-15 个回复。 |
| 第 2 周 | 做 15 场 discovery call。 | 痛点、预算、任务样本、购买路径。 |
| 第 2 周 | 跑 10 个 benchmark POC。 | 10 份 ROI 小报告。 |
| 第 3 周 | 签 5 个 design partner。 | 试点范围、数据边界、反馈节奏。 |
| 第 3 周 | 找 5 个集成伙伴。 | 联合 demo 或转介绍机制。 |
| 第 4 周 | 把 3 个试点转成 early access 付费。 | 收费验证和报价区间。 |
| 第 4 周 | 形成商业材料包。 | one-pager、ROI calculator、security FAQ、POC template。 |

## 10. 商业材料包

必须准备 5 个文件：

| 材料 | 用途 |
|---|---|
| One-pager | 让对方 60 秒理解价值。 |
| Benchmark report template | 每个 POC 都能输出可比较结果。 |
| ROI calculator | 把 token 节省转成预算。 |
| Security / privacy FAQ | 回答企业最担心的问题。 |
| POC plan | 明确 2-4 周试点目标、数据、成功标准。 |

## 11. 当前最具体的动作

今天开始做三件事：

1. 建一个 100 人商业线索表，分成 Agent 高频用户、AI 应用团队、AI infra 团队、服务商、企业 AI 平台团队。
2. 发第一批 30 条人工 DM，目标是拿 10 个真实长任务样本。
3. 做一个 ROI calculator，把“token 成本下降 80%”翻译成“每月能省多少钱、我们能收多少钱”。

