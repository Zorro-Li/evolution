# Gensyn 逐链接分析

## 1. 官方 docs：项目定义

Gensyn 的官方定义可以压成一句话：

> Gensyn 是一个 machine intelligence network，把训练、推理、评估、支付和验证放到开放网络里协调。

核心结构：
- Training Pipeline：通过本地偏好调优、分布式学习、公开市场评估，让模型在应用和设备中持续学习。
- Verification System：通过确定性复现和经济仲裁验证 ML 工作。
- Blockchain Protocol：记录资源所有权、量化 ML 工作、执行验证、支撑 evaluation markets 和通用智能合约应用。

直播解释：
- 当前 AI 的资源在少数云厂商和模型公司手里。
- Gensyn 的叙事是把算力、数据、模型评估和支付机制变成开放市场。
- 它把 AI 基础设施从“公司内部系统”推向“可参与、可验证、可支付、可组合”的协议层。

## 2. 官网：当前主网状态

官网展示 Delphi “Live on Mainnet”。这适合放在开场 5 分钟内，用来强调今晚直播的时效性：

- 2026-04-22：Gensyn 发布 Delphi。
- 2026-04-29：$AI / AIGENSYN 交易与路线图消息密集出现。
- 直播当晚 20:00 UTC+8 已处在 TGE/交易热度窗口。

## 3. Delphi：讲清楚“信息市场”

Delphi 的重点：
- 人类和 AI agents 一起交易预测。
- 结果由可验证 AI oracles 链上结算。
- 市场创建者可以围绕细分话题创建市场。
- 交易、结算、收入分配发生在开放网络里。

讲法建议：

“Polymarket 更偏事件结果交易，Delphi 进一步把 AI oracle 和创作者经济接进来。它想做的是信息市场：创作者负责提出问题和聚集社区，交易者贡献判断，AI oracle 负责结算，链上负责支付和审计。”

## 4. REE / Judge / Verde：讲清楚技术护城河

REE 的核心价值：
- AI 输出可复现。
- 每次运行生成 receipt，绑定输入、模型、配置和输出。
- 对方可以验证 receipt，也可以在自己硬件上重跑。

Judge 的核心价值：
- 将 AI evaluation 变成可验证流程。
- 解决 opaque API 和模型版本漂移带来的信任问题。
- 适合服务 Delphi 的“AI 判断结果”场景。

直播表达：

“Gensyn 的关键技术卖点是可验证 AI。预测市场最怕结算黑箱，AI evaluation 最怕模型更新、API 变动和环境漂移。REE 和 Judge 让输出、评分、结算都能留下可复现的证据。”

## 5. RL Swarm / CodeAssist / BlockAssist：讲清楚产品矩阵

RL Swarm：
- 开源 P2P 协同强化学习框架。
- 节点可以在消费级硬件或数据中心硬件上参与。
- 适合讲“开放训练网络”的底层实验。

CodeAssist：
- 本地运行、本地学习的 AI coding assistant。
- 从真实编码行为中学习：保留、修改、删除都是偏好信号。
- 适合讲“训练数据来自真实交互，并且隐私留在本地”。

BlockAssist：
- Minecraft 场景中的 assistance learning。
- 从用户游戏行为学习。
- 适合用作观众能理解的例子：“AI 可以从人工标注和行为轨迹里同时学习偏好。”

Judge：
- 可验证 AI evaluation。
- 可作为 Delphi settlement 的前置技术演示。

## 6. Tokenomics：官方版本

官方 docs 数据：
- Total supply：10,000,000,000 $AI
- Community Treasury：40.4%
- Investors：29.6%
- Team：25%
- Community Sale：3%
- Testnet Rewards：2%

解锁：
- Public Sale：TGE 解锁，美国买家和自愿锁仓买家 12 个月锁仓。
- Community Treasury：20% TGE 解锁，其余 36 个月线性解锁。
- Team / Investors：12 个月 cliff + 24 个月线性解锁。

直播重点：
- 价值捕获点：compute payments、staking & verification、evaluation markets、governance。
- Docs 明确提到交易收入会通过 programmatic buy and burn 累积到 $AI。
- 团队 + 投资人合计 54.6%，这是估值和二级市场风险讨论里的关键点。

## 7. 融资与估值

已核验：
- 2023 年 Series A：$43M，a16z crypto 领投。
- 2023 年时累计融资超过 $50M。
- The Block 报道 seed / pre-seed 超过 $7M。
- 官方 sale 页面披露 2025 年 10 月 $17M 小规模私募轮，a16z 领投，$1B FDV。

直播表达：

“Gensyn 的资本背景属于 crypto + AI 里比较硬的一档：a16z crypto 领投 Series A，后续又以 $1B FDV 参与 2025 年私募轮；CoinFund、Galaxy、Eden Block、Maven 11 等也在投资人列表里。”

## 8. Polymarket 与交易观察

截至调研时，Polymarket Gensyn 页面显示：
- 热门问题：Gensyn FDV above ___ one day after launch?
- $200M 档概率：98%
- 页面显示相关主题有约 $1M 交易量和 $86.1K 流动性。

直播分析角度：
- 市场已经把 “FDV 超 $200M” 定价为高概率。
- 关键观察位从 “$200M 高概率” 转向 “$500M / $1B 附近的承接强度”。
- 公售估值上限 $1B FDV，对应 $0.10/token，是今晚讨论估值锚点。
- 若二级开盘低于 $1B FDV，观众会关注是否回到私募轮锚点。
- 若二级快速高于 $1B FDV，观众会关注流通、锁仓、交易深度和 Delphi 真实使用数据。

## 9. 竞品对比框架

| 项目 | 核心定位 | 与 Gensyn 的差异点 | 直播结论 |
|---|---|---|---|
| Bittensor / TAO | 去中心化智能市场 / subnet 经济 | 更像 AI 任务与模型输出的激励网络，生态更成熟，复杂度更高。 | Gensyn 可以对标为更聚焦“训练、验证、信息市场”的新协议。 |
| Akash / AKT | 去中心化云计算市场 | 偏通用算力租赁。 | Gensyn 的差异在 ML workflow 和验证机制。 |
| Render / RENDER | GPU 渲染与算力网络 | 强在图形渲染、GPU 供给与创作者场景。 | Gensyn 更偏 AI 训练与 evaluation。 |
| io.net / IO | GPU 资源聚合与云服务 | 偏 DePIN 算力调度。 | Gensyn 的重点是训练证明、评估市场、AI oracle。 |
| Ritual / Nous / Sentient | 去中心化 AI 协议与开放模型生态 | 更偏模型、推理、开放智能体或 AI 产权叙事。 | Gensyn 的强点在“可验证机器学习工作 + 信息市场结算”。 |

## 10. 直播风险措辞

适合说：
- “这是项目研究和市场观察。”
- “估值锚点来自公开 sale 页面和预测市场。”
- “今晚最值得跟踪的是交易深度、初始 FDV、Delphi 活跃度、官方 listing 节奏。”
- “项目强在叙事、资本、技术路线；风险集中在真实收入、真实用量、团队/投资人占比和二级流动性。”

避免把未经核验的社区数据当成官方数据：
- 175,000 模型、40,000 节点、2,000,000 模型等数据需要官方仪表盘或团队确认。
- 69.3% / 29.7% / 1% 的 burn 分配需要官方出处。
- 合约地址要以官方 listing 页面、官网或链上浏览器为准。
