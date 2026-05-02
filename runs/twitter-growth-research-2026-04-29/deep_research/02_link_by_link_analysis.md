# Twitter 增长与宣传渠道调研：02 逐链接分析

调研日期：2026-04-29  
分析口径：每个来源单独拆解“它怎么拿流量、它怎么建立信任、我们能借鉴什么”。

## A01 X Ads campaign objectives

链接：https://business.x.com/en/advertising/campaign-types.html

**它怎么工作**

X Ads 以目标组织预算：覆盖、互动、视频观看、网站流量、App 安装、转化等。对早期 AI infra 产品，最有价值的目标通常是网站流量、帖子互动、视频观看和关注者增长。广告适合放大已经被自然流量验证过的内容。

**我们能借鉴**

先用自然帖测试表达，找到点击率、收藏率、回复质量较好的素材，再把同一素材做小预算放大。V1 阶段优先投放“demo 视频 + benchmark 图 + waitlist/文档链接”，少投品牌口号。

## A02 X Ads 信息说明

链接：https://business.x.com/en/help/troubleshooting/how-twitter-ads-work.html

**它怎么工作**

X 明确把广告标记出来，并让用户看到广告原因与控制选项。B2B 开发者用户对广告信任度敏感，广告落地页需要有技术细节、benchmark、隐私说明和可试用入口。

**我们能借鉴**

付费投放承接页需要包含可验证证据：任务前后 token 对比、任务类型、模型版本、运行环境、失败案例、安全说明。广告文案可以强，但证据页需要硬。

## A03 X Premium

链接：https://help.x.com/en/using-x/x-premium

**它怎么工作**

Premium 能增强账号基础能力：认证、长文、长视频、编辑、部分曝光相关能力。对创业项目，认证本身也是信任信号，尤其在用户要把任务和数据交给团队时。

**我们能借鉴**

创始人账号和项目账号都应开通 Premium。创始人账号使用长文讲产品理念、技术复盘和行业观察；项目账号使用长视频和长帖承载 demo、benchmark 和 release note。

## A04 X Verified Organizations

链接：https://help.x.com/en/using-x/verified-organizations

**它怎么工作**

组织认证把项目账号、创始人账号、员工账号连接在同一品牌体系下。这个机制对小团队的价值在于降低“野生项目”的不确定感。

**我们能借鉴**

产品进入公开收费前，项目账号应完成组织认证。创始人账号 bio 绑定项目账号，项目账号 bio 绑定官网、docs、security/privacy 页面。

## A05 X recommendation algorithm open source repo

链接：https://github.com/twitter/the-algorithm

**它怎么工作**

X 推荐机制围绕互动、关注关系、内容特征和账号关系传播。对新账号而言，早期最有效的杠杆是高质量回复、被大账号互动、收藏型内容、可转发的观点和可复用资料。

**我们能借鉴**

增长动作应从“发帖”扩展为“进入别人的讨论”。创始人每天需要在 Cursor、LangChain、Vercel、OpenAI、Claude Code、YC、AI infra 相关讨论下输出具体观点，让目标用户先在评论区看见我们。

## A06 Product Hunt Launch

链接：https://www.producthunt.com/launch

**它怎么工作**

Product Hunt 适合把已有素材集中释放：产品页、视频、截图、maker 评论、FAQ、早期用户反馈。PH 流量更像一次 launch 事件，需要前置预热和当天动员。

**我们能借鉴**

V1 首次公开可做 Product Hunt，但需要先准备：1 分钟 demo、对比图、真实 benchmark、免费试用、maker 评论、FAQ、隐私说明。PH 当天由创始人账号负责个人叙事，项目账号负责 demo、FAQ 和评论区答疑。

## A07 Hacker News Guidelines

链接：https://news.ycombinator.com/newsguidelines.html

**它怎么工作**

HN 用户偏好技术含量、真实经验、具体数据和可验证实现。泛营销标题容易被冷处理；扎实的工程复盘和可复现实验更容易得到讨论。

**我们能借鉴**

HN 发帖建议走技术故事：`Show HN: We cut token usage for long-running coding agents by 80%`。帖子正文给清晰实验设置、任务类型、失败边界、隐私设计和 GitHub benchmark harness。

## A08 Hacker News Show HN

链接：https://news.ycombinator.com/showhn.html

**它怎么工作**

Show HN 是产品展示频道，适合开发者工具、基础设施、开源工具和 demo。评论区质量高，能直接获得用户质疑和需求。

**我们能借鉴**

公开 demo 后 1-2 周内发 Show HN。团队要安排 24 小时评论区值班，把问题分成“产品需求、信任风险、技术质疑、商业化建议”四类。

## A09 GitHub Topics

链接：https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics

**它怎么工作**

GitHub Topics 帮助仓库进入相关主题页和搜索结果。AI infra 项目即使核心闭源，也可以开源 benchmark、SDK、examples 或 token-cost calculator。

**我们能借鉴**

推荐开源三个轻量资产：`agent-token-benchmark`、`long-agent-cost-calculator`、`agent-api-examples`。Topics 使用 `ai-agents`、`llmops`、`developer-tools`、`token-optimization`、`benchmark`。

## A10 GitHub community profile

链接：https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-community-profiles-for-public-repositories

**它怎么工作**

GitHub community profile 是开发者信任资产：README、License、Contributing、Security、Code of Conduct 会影响开发者是否愿意试用和贡献 issue。

**我们能借鉴**

即使核心闭源，公开仓库也要完整：README 放动图和结果表；Security 写明数据处理边界；Issues 用模板收集任务类型、模型、token 前后对比。

## A11 GitHub releases

链接：https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

**它怎么工作**

Releases 将版本更新固化成可传播节点。开发者工具的每次 release 可以被 X、HN、Discord、newsletter 再传播。

**我们能借鉴**

每周一次 release note：`new benchmark`, `new integration`, `new safety mode`, `new case study`。项目账号发简短帖，创始人账号发“为什么这个更新重要”的解释帖。

## A12 Reddit Reddiquette

链接：https://support.reddithelp.com/hc/en-us/articles/205926439-Reddiquette

**它怎么工作**

Reddit 社区重视真实参与和社区语境。AI 产品自推容易触发抵触，技术复盘、开源小工具、问题求助更自然。

**我们能借鉴**

Reddit 适合发“我做了一个 token cost benchmark harness，想找真实 long-agent traces 测试”这类帖子。渠道优先考虑 r/LocalLLaMA、r/MachineLearning、r/programming、r/ClaudeAI、r/OpenAI、r/SideProject，并按社区规则调整。

## B01 Cursor 项目账号

链接：https://x.com/cursor_ai

**观察证据**

页面显示约 36 万关注者。Bio 直接定位“best way to code with AI”。置顶 Cursor 3 发布视频约 241 万展示、8,907 喜欢、2,739 收藏。近期同一天连续发布 `/multitask`、multi-root workspaces、下载链接、GPT-5.5 模型可用和折扣。

**它怎么拿流量**

Cursor 把项目账号做成“发布机器”：大版本用强视频，小功能拆成多条短 demo，模型合作用 benchmark 数字和折扣制造即时转化。它把“产品更新”变成一组可被转发的具体能力。

**我们能借鉴**

我们的项目账号要学习 Cursor 的连发结构：主发布帖给 60-90 秒视频和核心结果；后续 3-5 条拆 feature，例如 token cost dashboard、任务恢复、上下文压缩、失败保护、SDK 用法。每条都要独立成立，带图或视频。

## B02 LangChain 项目账号

链接：https://x.com/LangChain

**观察证据**

页面显示约 24.7 万关注者。Bio 定位为 agent engineering platform。置顶是 Interrupt 线下大会，强调 1,000+ builders、Harrison Chase、Andrew Ng、企业案例和 workshops。近期发布 LangSmith 获得联邦市场 Awardable status。

**它怎么拿流量**

LangChain 从开源工具升级为平台，账号内容围绕社区大会、企业部署、政府/大客户背书、生态账号矩阵。它把技术社区、企业信任和线下活动连接起来。

**我们能借鉴**

我们当前阶段可以先做“小型线上 Interrupt”：每周一次 long-agent case teardown，邀请 2-3 个高频 Agent 用户讲任务。项目账号发活动，创始人账号发观点，参与者转发形成第一层传播。

## B03 Helicone 项目账号

链接：https://x.com/helicone_ai

**观察证据**

页面显示约 5,714 关注者。Bio 是 LLMOps platform、AI Gateway、LLM Observability、fully open-source。置顶强调 1 API key、100+ models、0% markup、open source，并引用创始人的 Product Hunt launch 帖。

**它怎么拿流量**

Helicone 适合小团队参考：一个极简价值主张反复出现，项目账号引用创始人 launch，借 Product Hunt 形成集中传播。账号也会转发生态和用户相关内容。

**我们能借鉴**

我们的 V1 需要一句类似的硬表达：`Long-agent API layer. Same task, up to 80% lower token cost.` 项目账号置顶要引用创始人 launch thread，并让创始人讲实验、路线、隐私承诺。

## B04 Portkey 项目账号

链接：https://x.com/PortkeyAI

**观察证据**

页面显示约 1,855 关注者。Bio 面向 production AI。置顶是 $15M Series A；近期转发团队成员介绍 CLI：一个命令配置 Claude Code 或 Codex 到 Portkey gateway；同时推 Agent Gateway webinar。

**它怎么拿流量**

Portkey 的项目账号更偏 B2B：融资背书、团队成员技术帖、webinar、CLI 使用方式。它把企业可信度和开发者可操作性放在一起。

**我们能借鉴**

我们可以采用“团队成员技术帖 + 项目账号转发”的打法。每个成员负责一个主题：benchmark、privacy、安全、SDK、demo。项目账号统一放大。

## B05 LlamaIndex 项目账号

链接：https://x.com/llama_index

**观察证据**

页面显示约 11.3 万关注者。Bio 现在聚焦 AI Document OCR 和 LlamaParse。近期帖子把 OCR 格式问题拆成视觉 cues、benchmark 问题；另一个帖子写贷款收入核验自动化，给出具体行业场景和技术栈。

**它怎么拿流量**

LlamaIndex 从泛 AI 框架转向更具体的“文档 OCR + 场景应用”。帖子用业务痛点开场，再接技术方案和链接，适合被目标用户收藏。

**我们能借鉴**

我们的内容应把“省 token”翻译成场景：`大型重构任务`、`多仓库代码修改`、`长调研报告`、`企业知识库 Agent`、`跨工具自动化`。每个场景都给前后账单和任务质量。

## B06 Vercel 项目账号

链接：https://x.com/vercel

**观察证据**

页面显示约 42.2 万关注者。Bio 是 Agentic Infrastructure。近期安全公告帖约 1050 万展示，后续连续更新调查、合作方、风险边界和建议。账号页面还直接展示招聘卡片。

**它怎么拿流量**

Vercel 的账号承担信任沟通：遇到高风险事件时，把信息拆成多条、链接到官方知识库、引用合作方。透明度本身形成传播。

**我们能借鉴**

做 Agent API 涉及用户数据和误操作风险，项目账号必须提前具备“信任沟通模板”：隐私页、安全事件响应页、状态页、变更日志。公开透明会直接影响转化。

## C01 Harrison Chase 创始人账号

链接：https://x.com/hwchase17

**观察证据**

页面显示约 10.1 万关注者。Bio 挂 LangChain 和 careers。置顶长文《Continual learning for AI agents》约 50 万展示、2,079 收藏。近期发帖询问用户想看哪些 deepagents examples，并转发团队成员的 production 系列。

**它怎么拿流量**

Harrison 的打法是“技术教育 + 用户共创 + 团队放大”。长文建立技术权威，开放问题吸引真实需求，转发团队内容形成组织声量。

**我们能借鉴**

创始人账号要每周写一篇长文：`Why long-running agents waste tokens`、`How to benchmark token cost reduction`、`Context engineering patterns for long tasks`。每天发一次开放问题，收集用户任务样本。

## C02 Garry Tan 创始人账号

链接：https://x.com/garrytan

**观察证据**

页面显示约 77.5 万关注者。Bio 聚合 YC、Garryslist、GStack、GBrain。置顶是长期世界观，近期转发 GStack/GBrain 用户使用、GitHub 链接和生态评价。

**它怎么拿流量**

Garry 用强个人世界观承接项目推广。项目出现时，内容看起来是个人长期信念的延伸；用户发的使用反馈被他转发，形成“用户证明 -> 创始人放大 -> 更多用户试用”的循环。

**我们能借鉴**

创始人账号需要先有长期叙事：`long tasks are the real test of agent infra`。每当用户/朋友试用后发结果，创始人账号转发并补充洞察，项目账号再整理成 case study。

## C03 swyx 创始人/意见领袖账号

链接：https://x.com/swyx

**观察证据**

页面显示约 15.5 万关注者。Bio 聚合多个社区和项目：AI Engineer、Latent Space、Temporal、Cognition。置顶是长期游戏清单，近期内容包含技术、社区、播客、个人生活和跨平台导流。

**它怎么拿流量**

swyx 的增长来自长期内容资产和社区身份。账号内容覆盖观点、活动、播客、人设和社群，使他在 AI Engineer 语境里持续被看见。

**我们能借鉴**

创始人账号可以做“long-agent engineering”垂类，不追求泛 AI 热点。每周固定输出一份小型知识资产：案例拆解、术语解释、benchmark 解读、工具清单。

## C04 Guillermo Rauch 创始人账号

链接：https://x.com/rauchg

**观察证据**

页面显示约 46.1 万关注者。Bio 直接写 Vercel CEO。近期发帖提出 coding agents 是重要基础能力，并转发 Vercel Developers 的 AI Gateway 模型发布。

**它怎么拿流量**

Guillermo 用创始人账号输出大判断，用项目/开发者账号承接具体产品发布。观点帖扩大心智，项目帖负责转化。

**我们能借鉴**

创始人账号负责提出“长任务 Agent 会成为下一代 AI infra 入口”的判断；项目账号负责证明“我们在 token 成本、任务连续性、上下文压缩上解决了具体问题”。

## C05 levelsio 创始人账号

链接：https://x.com/levelsio

**观察证据**

页面显示约 85.9 万关注者。Bio 展示多个产品月收入。置顶 #vibejam，包含赞助方、奖金、截止时间、每日游戏精选和视频。近期高频发布产品进展、域名、视频和用户互动。

**它怎么拿流量**

levelsio 把透明收入、连续构建、挑战赛、赞助商和用户作品连接起来。账号像一个持续运行的活动现场。

**我们能借鉴**

我们可以做 `Long Agent Cost Challenge`：邀请用户提交一段长任务 trace 或任务描述，团队用 V1 跑对比，公开前后 token、成本、成功率。每周选 3 个案例发帖。
