# HiTw93 / Tw93 逐对象分析

## 1. X 账号画像

[@HiTw93](https://x.com/HiTw93) 的公开定位是独立开源产品作者和 AI Coding 工作流实践者。简介直接列出 Kaku、Mole、Pake、MiaoYan，推文内容进一步扩展到 Waza、Kami、Weekly、Maple、nanobot、Claude Code / Codex 工作流、Agent 架构和 LLM 训练。

他的内容结构很清晰：用产品证明观点，用长文沉淀方法，用推文完成发布、传播、反馈收集和社区协作。

## 2. Kaku

来源：[GitHub Kaku](https://github.com/tw93/Kaku)、`raw/README_Kaku.md`、X 推文样本。

Kaku 是面向 AI Coding 的 macOS 终端，核心价值是开箱即用、零配置、AI 工具友好。README 把 Kaku 定义为 WezTerm 的深度定制分支，强调轻量、快速、默认体验、AI 错误修复、自然语言转命令，以及 Claude Code、Codex、Gemini CLI 等工具配置管理。

可吸收知识：

- AI Coding 的入口体验要先解决终端恐惧和环境摩擦。
- 面向 AI 的开发环境要把 shell、Git、文件管理、分屏、错误修复、模型配置放在同一工作台里。
- 默认配置是产品能力：字体、主题、快捷键、错误提示、内置工具都能降低上手成本。
- 终端可以成为 Agent runtime 的本地壳层，而非单纯命令输入器。

## 3. Waza

来源：[GitHub Waza](https://github.com/tw93/Waza)、`raw/README_Waza.md`、X 推文样本。

Waza 把工程习惯封装为 Claude / Codex 可运行的 skills。README 中列出 8 个核心技能：`think`、`design`、`check`、`hunt`、`write`、`learn`、`read`、`health`。它的关键思想是把优秀工程师已经知道的习惯变成可重复调用的执行协议。

可吸收知识：

- Skill 的价值在于把抽象能力变成稳定流程。
- 好 skill 先定义使用时机，再定义输出和验证方式。
- `/think -> implement -> /check` 是功能开发的基础链路。
- `/hunt -> fix -> /check` 是缺陷处理的基础链路。
- `/read -> /learn -> /write` 是研究和写作的基础链路。
- `/health` 把 agent 配置、规则、skills、hooks、MCP 行为做成可审计对象。

## 4. Kami

来源：[GitHub Kami](https://github.com/tw93/Kami)、X 推文样本、推文外链。

Kami 是 AI 时代的文档排版系统，定位为让 AI 生成内容变得清晰、可读、可打印、可分享。高互动推文显示它覆盖 one-pager、resume、portfolio、letter、long docs、slides、多语言、图表、打印场景。

可吸收知识：

- AI 内容的下一层竞争是表达质量和视觉交付。
- 文档工具可以围绕约束语言、版式系统、图表系统、打印输出组织能力。
- 对 AI 生成内容而言，写得出只是第一步；能被读、能被转发、能被交付才产生外部价值。

## 5. Mole

来源：[GitHub Mole](https://github.com/tw93/Mole)、X 推文样本。

Mole 是 macOS 清理和优化工具，GitHub stars 接近 50K。推文反复强调安全清理、开发者缓存、AI coding agent 缓存、浏览器缓存、卸载残留、系统状态、自动优化。

可吸收知识：

- 工具型产品的增长来自具体痛点：磁盘空间、缓存垃圾、卸载残留、系统状态不可见。
- 清理类工具的信任核心是安全边界、可解释范围、可恢复心智。
- 发布节奏可以围绕版本号、codename、具体清理对象和安全改进形成稳定叙事。

## 6. Pake

来源：[GitHub Pake](https://github.com/tw93/Pake)、X 推文样本。

Pake 的定位是一条命令把网页打包成桌面应用。它对 AI 产品特别有用：先用 Web 快速验证市场，再用 Pake 打包为 macOS、Windows、Linux 桌面应用。

可吸收知识：

- AI 产品的早期路线可以是 Web-first，再做桌面外壳。
- 桌面打包能力能把分发、驻留、系统入口、品牌感一次性提升。
- 面向个人开发者的工具要把“交付”这一步压缩到一条命令。

## 7. MiaoYan

来源：[GitHub MiaoYan](https://github.com/tw93/MiaoYan)、X 推文样本。

MiaoYan 是面向工程师的本地 Markdown 写作工具，强调轻量、native macOS、稳定预览、国际化、沙盒和公证。推文中的定位偏向“在 AI 工作流旁边保留一个安静、可搜索、可沉淀的写作空间”。

可吸收知识：

- AI 写作生态需要一个长期可信的本地写作底座。
- Markdown、稳定预览、本地文件、系统级体验仍是工程师写作工具的核心。
- 写作产品的差异化来自稳定、安静、低干扰、可沉淀。

## 8. AI Coding 长文

来源：[You Don't Know AI Coding](https://tw93.fun/en/2026-04-26/ai-coding.html)。

这篇文章面向非技术人讲 AI Coding 的入门路径。核心路线是：先克服命令行入口，再补足轻量技术素养，然后用 CLAUDE.md 写清项目背景和规则，再用精确需求、Plan mode、验收标准和小工具项目推进实践。

可吸收知识：

- 非技术人使用 AI Coding 的关键能力是需求清晰度、基础技术识别、结果判断。
- CLAUDE.md / AGENTS.md 是 agent 的项目入职文档。
- 需求要包含背景、目标、范围、边界、边缘情况、验收标准。
- 最好的入门项目是 software for one：只为自己解决真实问题的小软件。
- 复杂任务先同步计划，再进入执行。

## 9. 学习工作流长文

来源：[How I Turn Learning Into a Workflow in the AI Era](https://tw93.fun/en/2026-04-06/learn.html)。

这篇文章把学习拆成工程化流程：收集高质量资料、转成 Markdown、清理分类、过滤材料、构建领域地图、写大纲、逐节补全、用 AI 收紧结构和发现缺口、自审、发布。它的重点是把输入变成输出。

可吸收知识：

- 学习深度来自产出，而非资料消费量。
- AI 适合收集、转换、清理、翻译、对比、精修。
- 人的职责是选材、判断、结构、耐心、标准。
- 学习流程可以像代码流程一样被 skill 化。

## 10. LLM 训练长文

来源：[You Don't Know LLM Training](https://tw93.fun/en/2026-04-03/llm.html)。

这篇文章把 LLM 能力来源拆成训练流水线：预训练、数据工程、系统和架构、后训练、eval / grader / reward、agent training、harness、distillation、deployment。核心判断是用户感知到的模型提升大量来自预训练之后的环节。

可吸收知识：

- 模型能力是权重、数据配方、系统约束、后训练、评估奖励、部署策略的共同结果。
- Agent 训练的核心变量是环境质量、工具稳定性、任务轨迹、奖励设计和 harness。
- Harness 是模型外部的控制程序，决定模型看到什么、如何使用工具、如何维护上下文。
- 生产流量、长任务摘要、环境回放、轨迹日志都可以成为训练和优化信号。

