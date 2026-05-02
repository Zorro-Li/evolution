---
title: GEO citation absorption research and commercialization
type: report
tags:
  - geo
  - ai-search
  - citation-absorption
  - commercial-research
created: 2026-04-30
sources:
  - https://x.com/yaojingang/status/2049298176935690588
  - https://arxiv.org/abs/2604.25707
  - https://github.com/yaojingang/geo-citation-lab
  - https://yaojingang.github.io/geo-citation-lab/
---

# GEO 引用吸收研究与商业化方案

结论：可以做 GEO，而且更适合做成“AI 引用吸收测量 + 证据页生产闭环”，先从海外英文内容和出海公司切入。

这篇论文和数据源的价值在于把 GEO 从观点变成可测量流程：`Prompt -> 搜索触发 -> 来源选择 -> 页面抓取 -> 72 维特征 -> 引用影响力分数 -> 内容改写建议`。

## 1. 原始资料台账

### X 原帖

作者姚金刚发布的信息：

- 论文：`From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms`
- arXiv：`2604.25707`
- 作者：Zhang Kai、Yao Jingang
- 数据：2026 年 3 月最新样本
- 规模：`602` 条 Prompt、`21,143` 条有效引用、`23,745` 条 AI 抓取/特征记录
- 数据源：`geo-citation-lab`

### 论文

arXiv 页面给出的摘要重点：

- GEO 应分成两段测量：
  - `citation selection`：平台是否触发搜索、选择哪些来源。
  - `citation absorption`：被引用页面是否真的贡献语言、证据、结构或事实支持。
- 数据覆盖 ChatGPT、Google AI Overview / Gemini、Perplexity。
- 样本包括 `602` controlled prompts、`21,143` valid search-layer citations、`23,745` citation-level feature records、`18,151` fetched pages、`72` features。
- 中心发现：引用宽度和引用深度会分离。Perplexity 和 Google 引用更多，ChatGPT 引用更少但单条引用吸收更深。

### 数据仓库

仓库：`https://github.com/yaojingang/geo-citation-lab`

本地克隆位置：

`/Users/lizongru/codex/进化/runs/geo-research-2026-04-30/geo-citation-lab`

关键文件：

- `01-prompt/`：602 条实验 Prompt。
- `02-data/*results_with_prompt.csv`：搜索触发与来源层数据。
- `02-data/features_all_platforms_72.csv`：引用影响力层数据，23,745 行、72 列。
- `03-pipeline/`：批量查询、解析、抓取、特征提取、影响力分析脚本。
- `04-repet/final_report.md`：完整报告。
- `QUICK_REPORT.md`：3 分钟摘要。

仓库 README 的快照口径：

| 指标 | 数值 |
| --- | ---: |
| Prompt 总数 | 602 |
| A/B/C/D 四层实验 | 432 / 60 / 60 / 50 |
| 平台数量 | 3 |
| 搜索层有效引用行数 | 21,143 |
| 引用影响力特征行数 | 23,745 |
| 特征维度 | 72 |
| 成功抓取引用页面 | 18,151 |
| 抓取成功率 | 76.44% |

## 2. 数据结构

### 搜索层 CSV

文件：

- `chatgpt_results_with_prompt.csv`
- `Google_results_with_prompt.csv`
- `perplexity_results_with_prompt.csv`

核心字段：

- `文件名`
- `prompt`
- `是否触发搜索`
- `引用域名`
- `网站标题(Title)`
- `网站描述(Description)`
- `域名评级(Domain Rank)`
- `语言(Language)`
- `国家(Country)`
- `最终评级(Final_DR)`
- `网站类型`

用途：

- 看 Prompt 是否触发联网搜索。
- 看每个平台倾向引用哪些域名、语言、国家、网站类型。
- 做 Prompt 级引用数量统计。
- 找公司或品牌在哪些提示词下进入或缺席候选池。

### 引用影响力层 CSV

文件：

`features_all_platforms_72.csv`

本地验证结果：

| 文件 | 行数 | 列数 |
| --- | ---: | ---: |
| `features_all_platforms_72.csv` | 23,745 | 72 |
| `chatgpt_features.csv` | 4,494 | 72 |
| `google_features.csv` | 8,476 | 72 |
| `perplexity_features.csv` | 10,775 | 72 |

72 维字段可以分成六类：

- 回答上下文：`question`、`question_type`、`answer_word_count`、`total_citations`。
- 引用身份：`url`、`display_name`、`domain`、`domain_tld`、`domain_type`。
- 页面结构：`cit_word_count`、`cit_heading_total`、`cit_paragraph_count`、`cit_list_density`。
- 内容体裁：`cit_has_numbers`、`cit_has_definition`、`cit_has_qa_format`、`cit_has_howto`、`cit_has_comparison`。
- 语义对齐：`emb_answer_cit_cosine`、`emb_question_cit_cosine`、`llm_relevance_score`、`llm_content_quality`。
- 结果变量：`ref_count`、`first_position_ratio`、`paragraph_coverage_ratio`、`tfidf_cosine`、`bigram_overlap`、`trigram_overlap`、`influence_score`。

影响力分数：

```text
influence_score =
    0.20 × min(ref_count / 3, 1)
  + 0.15 × (1 - first_position_ratio)
  + 0.20 × paragraph_coverage_ratio
  + 0.25 × tfidf_cosine
  + 0.20 × (bigram_overlap + trigram_overlap) / 2
```

这个分数衡量页面被模型真正用进回答的程度，超越来源列表出现次数。

## 3. 核心发现

### 平台差异

| 平台 | 观测 Prompt | 触发搜索 Prompt | 触发率 | 平均引用数 |
| --- | ---: | ---: | ---: | ---: |
| ChatGPT | 587 | 579 | 98.64% | 6.88 |
| Google | 602 | 600 | 99.67% | 12.06 |
| Perplexity | 602 | 602 | 100.00% | 16.35 |

引用影响力层，本地用 CSV 复核：

| 平台 | 特征行 | 抓取成功 | 抓取成功率 | 平均影响力 | 中位影响力 |
| --- | ---: | ---: | ---: | ---: | ---: |
| ChatGPT | 4,494 | 3,323 | 73.94% | 0.2713 | 0.2611 |
| Google | 8,476 | 6,385 | 75.33% | 0.0584 | 0.0515 |
| Perplexity | 10,775 | 8,443 | 78.36% | 0.0646 | 0.0333 |

解释：

- ChatGPT 是深读型平台，引用少，单条来源吸收深。
- Google 是对题型平台，语义匹配、标题和定义结构更关键。
- Perplexity 是广覆盖平台，更适合模块化、综合型页面。

### 内容结构

高影响力页面的典型形态：

| 指标 | Top 25% | Bottom 25% | 倍数 |
| --- | ---: | ---: | ---: |
| 词数 | 1,943.30 | 169.82 | 11.44x |
| 标题总数 | 10.59 | 0.85 | 12.50x |
| 段落数 | 47.49 | 8.34 | 5.69x |
| 列表密度 | 0.428 | 0.048 | 8.94x |
| 回答-引用语义相似度 | 0.570 | 0.247 | 2.31x |
| LLM 相关性评分 | 3.535 | 1.856 | 1.90x |

### 内容体裁

本地用 CSV 复核的布尔特征：

| 特征 | True 平均影响力 | False 平均影响力 | 提升 |
| --- | ---: | ---: | ---: |
| 含代码 | 0.1747 | 0.0988 | +76.88% |
| 含数字/统计 | 0.1171 | 0.0725 | +61.55% |
| 含定义句式 | 0.1252 | 0.0795 | +57.33% |
| 含对比内容 | 0.1389 | 0.0894 | +55.28% |
| 含 how-to | 0.1296 | 0.0918 | +41.20% |
| 含 Q&A 格式 | 0.0947 | 0.1005 | -5.74% |

实操结论：

- 页面需要定义、数字、对比、步骤。
- 目标篇幅优先做到 `1000-3000` 词。
- 小节标题贴近用户真实子问题。
- Q&A 形式本身价值弱，证据密度和可抽取结构才是核心。

### 来源候选池

三平台默认候选池高度集中：

| 平台 | 官网 | 新闻 | 行业垂类 |
| --- | ---: | ---: | ---: |
| ChatGPT | 34.22% | 31.17% | 22.13% |
| Google | 46.35% | 18.99% | 22.00% |
| Perplexity | 44.07% | 16.07% | 18.99% |

组合占比：

- ChatGPT：87.52%
- Google：87.34%
- Perplexity：79.12%

进入候选池的优先级：

- 权威官网
- 新闻媒体
- 行业垂类站点
- 英文内容
- US 或全球化域名环境

## 4. 我们自己怎么做 GEO

### 4.1 可复现研究版

目标：复现论文方法，用在任意公司、品牌或产品上。

流程：

1. 生成 Prompt 矩阵。
   - 主问题：事实、对比、聚合、解释、决策。
   - 触发强度：低、中、高。
   - 时效性：稳定、近期、实时。
   - 语言：英文、中文、目标市场语言。
   - 风格：自然提问、要求来源、专家角色。
2. 对 ChatGPT、Google AI Overview / Gemini、Perplexity 批量提问。
3. 保存每次回答全文、引用 URL、引用顺序、是否触发搜索。
4. 抽取引用域名、标题、描述、国家、语言、DR、网站类型。
5. 抓取每个引用 URL 的正文。
6. 为每个页面生成 72 维特征。
7. 计算 `influence_score`。
8. 输出 GEO 报告：
   - 品牌出现率
   - 域名引用率
   - 引用位置
   - 吸收深度
   - 缺失 Prompt
   - 竞品占位
   - 内容结构改造建议

### 4.2 商业产品版

产品主线：

`客户网站/品牌 -> 高意图 Prompt 库 -> 三平台采样 -> 引用/吸收分析 -> 内容 Brief -> 证据页生成/改写 -> 再测`

核心模块：

1. Prompt Lab
   - 根据客户产品、行业、竞品和购买场景生成 200-1000 条 Prompt。
   - Prompt 按 funnel 分类：认知、比较、采购、风险、替代、价格、使用场景。
2. AI Search Runner
   - 批量调用或授权采集 ChatGPT、Gemini / Google AI Overview、Perplexity。
   - 保存回答、引用、时间、地区、语言、账号环境。
3. Citation Parser
   - 抽取引用 URL、域名、位置、展示名称。
   - 标记客户、竞品、媒体、论坛、百科、垂类站点。
4. Page Fetcher
   - 抓取被引用页面正文。
   - 解析标题、段落、列表、表格、图片、代码、链接。
5. Absorption Scorer
   - 复用论文的 `influence_score`。
   - 增加品牌相关指标：`brand_mentioned`、`brand_sentiment`、`competitor_displaced`、`buying_intent_stage`。
6. Content Brief Generator
   - 输出可执行页面结构：
     - 1 句定义
     - 3-5 个数据点
     - 1 个对比表
     - 1 个步骤块
     - 1 个适用边界
     - 3-8 个可引用证据源
7. Re-test Loop
   - 发布或改写后每周重测。
   - 看候选池进入率和吸收分是否提升。

### 4.3 最小 MVP

第一版做成服务型工具，先少量客户手工交付：

- 输入：客户官网、产品页、5 个竞品、目标国家、目标语言。
- 自动生成：300 条高意图 Prompt。
- 覆盖平台：ChatGPT、Perplexity、Google/Gemini 先选可稳定采集的两个。
- 采样频率：每周 1 次。
- 输出：
  - `AI Visibility Score`
  - `Citation Share`
  - `Absorption Score`
  - `Competitor Share`
  - `Missing Evidence Pages`
  - `10 个优先内容 Brief`

MVP 交付价格：

- 诊断报告：`$2,000-$5,000 / 次`
- 月度监控：`$1,000-$3,000 / 月`
- 诊断 + 内容生产：`$5,000-$20,000 / 月`

产品化之后：

- SMB self-serve：`$199-$499 / 月`
- Growth team：`$1,000-$3,000 / 月`
- Enterprise：`$20,000+ / 年`

## 5. GStack / office-hours 判断

核心目标：找到一个小切口，让客户愿意为“AI 搜索里被看见、被引用、被吸收”付费。

需求现实：

- AI 搜索正在影响 B2B SaaS、AI 工具、跨境电商、金融、医疗、教育的发现链路。
- 传统 SEO 工具擅长 Google SERP 排名和关键词流量。
- 新需求是回答层面的“谁被模型引用、谁的话被模型吸收、竞品为什么被提到”。

最窄 wedge：

`出海公司英文内容的 AI 引用吸收诊断`

理由：

- 他们有英文内容预算。
- 他们在海外市场缺少品牌心智。
- 他们在 ChatGPT、Perplexity、Gemini 里的出现与竞品对比更容易被老板理解。
- 论文数据证明英文、US、官网/新闻/垂类站点仍是高权重环境。

未来扩展：

- 从一次性诊断扩展到月度监控。
- 从监控扩展到内容 Brief。
- 从 Brief 扩展到托管式内容生产。
- 从内容生产扩展到 PR/媒体/行业垂类分发。

## 6. DBS 商业诊断

### 6.1 真问题

用户原始问题聚焦商业化可行性。

成立的问题：

`企业愿意为 AI 搜索中的可见度、引用份额、竞品对比和内容改写建议付多少钱？`

真正卖点：

- 老板能看懂：品牌在 ChatGPT / Perplexity / Google AI Overview 里的出现情况。
- 市场团队能执行：哪些页面该写、怎么写、发到哪里。
- 内容团队能交付：页面结构、字数、数据点、对比块、步骤块都有明确标准。
- 代理商能复用：同一套报告可以服务多个客户。

### 6.2 产品形态

建议采用三层产品：

1. GEO Audit
   - 一次性诊断。
   - 适合早期现金流。
   - 交付物是 PDF/Notion/网页报告 + 10 个内容 Brief。
2. GEO Monitoring
   - 月度订阅。
   - 追踪品牌、竞品、Prompt、引用域名和吸收分。
   - 适合产品化。
3. GEO Content Ops
   - 高客单托管服务。
   - 包含页面改写、英文证据页、媒体/垂类分发。
   - 适合先赚钱。

### 6.3 商业模式判断

优先做 B2B 服务 + 软件辅助。

原因：

- 现在市场教育成本高，纯 SaaS 容易被客户当成“又一个仪表盘”。
- 报告和内容改写能直接绑定 ROI。
- 数据采集有平台不稳定性，服务交付更容易吸收波动。
- 企业真正买的是“我该怎么改”，仪表盘只是证据。

### 6.4 对标

当前国外已有 AI search visibility / GEO 工具，说明市场教育已经开始：

- Profound：AI search visibility and answer-engine analytics。
- Ahrefs Brand Radar：监测品牌在 AI Overviews、ChatGPT、Perplexity 等环境的提及。
- Peec AI：AI search visibility platform。
- Otterly AI：AI search monitoring for ChatGPT、Google AI Overviews、Perplexity。

可模仿点：

- Dashboard：品牌/竞品出现率、Prompt 级结果、平台对比。
- Alert：竞品突然变强、品牌消失、负面答案出现。
- Prompt library：行业问题库。
- Content recommendation：把监控结果转成内容任务。

差异化切口：

- 用论文里的 citation absorption 指标做更深一层的“引用吸收分”。
- 面向出海公司，交付英文内容改写和外部发布建议。
- 把 GEO 与内容生产闭环打通，覆盖排名监控、内容 Brief、改写和复测。

## 7. 可以面向哪些公司

### 第一优先级：出海 AI / SaaS 公司

画像：

- 有英文官网和内容预算。
- 目标客户会用 ChatGPT、Perplexity、Gemini 做产品调研。
- 竞品比较型 Prompt 很多。

例子：

- AI 工具：Monica、Genspark、Manus、MiniMax、DeepSeek 生态产品、Kimi 海外产品线。
- SaaS / DevTool：API、数据库、监控、安全、客服、CRM、自动化、设计协作工具。
- 中国出海 SaaS：协作、客服、营销自动化、跨境运营工具。

卖法：

- 先做“AI 搜索里，竞品为什么比你更容易被推荐”的报告。
- 给 10 个高意图 Prompt：`best X for Y`、`X vs competitor`、`alternatives to X`、`which tool should I use for Y`。
- 输出 10 个英文证据页 Brief。

### 第二优先级：跨境电商和 DTC 品牌

画像：

- 有 Shopify/Amazon/独立站。
- 买家会用 AI 问“最好的 XX 产品”“XX vs YY”“哪个品牌适合某场景”。
- 产品页和内容页可以快速改。

例子：

- 消费电子、智能硬件、户外、母婴、家居、宠物、护肤。
- 品牌例子：Anker、DJI、Roborock、EcoFlow、Ugreen、Baseus 这类有海外内容资产的公司。

卖法：

- 做“AI Buyer Journey Audit”。
- 监控购买意图 Prompt 下的品牌出现率。
- 改写产品页、对比页、选购指南、FAQ。

### 第三优先级：SEO / PR / 内容营销代理商

画像：

- 已经有客户和月费。
- 正在被客户问 AI 搜索怎么做。
- 需要一个新产品包装来涨价。

例子：

- SEO agency
- PR agency
- Content marketing agency
- B2B growth agency
- 出海营销代理商

卖法：

- 白标 GEO Audit。
- 提供 Prompt library + scoring engine + report template。
- 代理商负责客户关系和内容执行。

### 第四优先级：高客单信息密集行业

画像：

- 客单价高。
- 决策前搜索和比较强。
- 内容需要权威性和证据。

类别：

- 金融科技、券商、支付、保险。
- 医疗健康、诊所、保健品、康养服务。
- 教育、留学、职业培训。
- 法律、财税、企业服务。

卖法：

- 强调合规和事实引用。
- 把内容页做成定义、数据、对比、步骤、边界条件。
- 输出可审查的证据源和改写记录。

## 8. 具体落地计划

### 第 1 周：做可卖 Demo

1. 选 1 个行业：AI SaaS 或跨境电商。
2. 选 3 个品牌 + 5 个竞品。
3. 生成 200 条英文高意图 Prompt。
4. 手动或半自动采集 ChatGPT、Perplexity、Gemini / Google AI Overview 结果。
5. 复用 `features_all_platforms_72.csv` 的字段设计，做第一版 scoring。
6. 输出 20 页报告模板。

### 第 2-3 周：做第一个付费试点

1. 找 20 家出海 AI/SaaS/跨境公司市场负责人。
2. 免费给每家公司跑 10 条 Prompt 的 mini audit。
3. 用结果约 30 分钟诊断电话。
4. 报价完整诊断：`$2,000-$5,000`。
5. 交付 300 Prompt + 竞品报告 + 10 个内容 Brief。

### 第 4-6 周：沉淀产品

1. 把 Prompt 生成、引用解析、页面抓取、评分做成 CLI。
2. 把报告模板做成 HTML。
3. 把内容 Brief 做成可复用结构。
4. 设计月度监控计划。
5. 把最有效的客户案例做成销售页。

### 第 7-12 周：扩展成服务产品

1. 上线 3 档产品：
   - GEO Audit
   - GEO Monitoring
   - GEO Content Ops
2. 每个行业沉淀 Prompt 包。
3. 和 SEO/PR 代理商做白标合作。
4. 建立客户前后对比指标：
   - Brand mention share
   - Citation share
   - Absorption score
   - Competitor displacement
   - Evidence page coverage

## 9. 风险与边界

### 数据采集风险

AI 平台输出会随账号、地区、时间、上下文变化。报告需要保存采集时间、地区、模型、账号状态和原始回答。

### Google AI Overview 风险

Google AI Overview 的稳定采集难度高。早期可以优先做 ChatGPT + Perplexity，再逐步接入 Google/Gemini。

### 因果风险

相关性高的内容特征可以指导改写，但发布后是否提升引用需要复测。产品必须做 re-test loop。

### 合规风险

医疗、金融、法律内容需要事实审核和免责声明。产品应输出证据链和修改记录，减少夸大承诺。

## 10. 推荐执行

先做 `出海 AI/SaaS GEO Audit`。

第一版卖的是报告和内容 Brief，工具只服务交付。等跑出 3-5 个付费案例，再把采集、评分、报告生成产品化。
