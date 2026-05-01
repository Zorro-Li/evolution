# 从 HiTw93 / Tw93 吸收的知识体系

## 核心判断

Tw93 的知识体系可以压缩成一句话：用开源产品把 AI Coding、Agent、学习、写作、macOS 工具链变成日常可运行系统。

他关注的重点是“可运行”：终端能跑、skill 能跑、文档能交付、学习能发布、工具能开箱、Agent 能持续完成任务。

## 知识地图

### 1. AI Coding

AI Coding 是一种工作流能力。它要求使用者会写清目标、提供上下文、限定边界、理解基本技术名词、看懂错误、判断结果。

可复制做法：

- 每个项目根目录放 AGENTS.md / CLAUDE.md。
- 复杂任务先做 plan。
- 需求写成背景、目标、范围、边界、边缘情况、验收标准。
- 每次交付跑验证命令。
- 高频动作沉淀成 skill。

### 2. Skill 化工程习惯

Waza 的核心是把工程师的隐性流程显性化。`think` 对应方案设计，`check` 对应交付前审查，`hunt` 对应系统调试，`learn` 对应研究到产出，`write` 对应表达质量，`health` 对应 agent 配置体检。

可复制做法：

- 把每个 recurring workflow 写成一个 skill folder。
- 每个 skill 包含触发条件、输入要求、执行步骤、输出格式、验证方式。
- skill 之间手动串联，保留人的判断点。
- 用 `/health` 思路定期审计本地 Jarvis 的规则、memory、工具、hooks。

### 3. Agent 和 Harness

Tw93 对 Agent 的理解接近系统工程：模型只是其中一层，真正决定长期任务质量的是 harness、环境、工具返回、记忆、上下文编辑、日志和验证。

可复制做法：

- Agent 启动时读取项目状态、目录、规则、任务。
- 每次工具调用保留输入输出和判断依据。
- 长任务中维护 compact 保留项：架构决策、已改文件、当前进度、待办。
- 本地 agent 用明确队列、权限、回调和 memory update 串起来。
- 对 agent 输出做独立 review，而非让执行者自证完成。

### 4. 学习工作流

他的学习方式是 publish-driven learning。先收集高质量一手材料，再整理成研究仓库，过滤材料，构建地图，写大纲，补全内容，用 AI 找缺口和收紧表达，最后发布。

可复制做法：

- 新领域先建 source ledger。
- 所有材料转 Markdown 或可检索文本。
- 先删弱资料，再写结构。
- 每篇学习输出都要变成可公开报告或内部手册。
- AI 用于清理、对比、翻译、结构校验和缺口审查。

### 5. 产品方法

他的产品线有一致口味：小、快、开箱即用、默认体验好、面向真实工作流、用开源传播、频繁发布、带人格化叙事。

可复制做法：

- 产品先抓一个具体痛点：终端摩擦、文档排版、磁盘清理、网页打包、Markdown 写作。
- 第一版追求可用闭环。
- 发布说明写具体用户收益和真实场景。
- 把产品做成 family：命名、角色、用途、视觉叙事统一。
- 用 GitHub README、X 长推、博客长文组成传播链。

### 6. LLM 训练理解

他对模型进步的解释是 pipeline 视角：预训练提供基础，数据配方塑造能力分布，系统约束锁定成本和上下文，后训练让模型可用，eval / reward 决定优化方向，agent training 把环境和工具纳入训练目标，distillation 和 deployment 决定真实产品体验。

可复制做法：

- 分析模型能力时看训练流水线，而非只看参数和榜单。
- 评估 agent 时看任务轨迹、环境一致性、工具稳定性、上下文摘要质量。
- 把 reward / grader / eval 当成产品规格的一部分。
- 用真实任务、成本、稳定性、失败恢复衡量模型价值。

## 对 Jarvis 的直接吸收

### 立刻可用规则

- 每个研究任务生成三件套：source ledger、link-by-link analysis、synthesis report。
- 每个执行任务先读 workspace rules 和 operating state。
- 每个复杂任务保留 compact priority：决策、已改文件、进度、TODO。
- 每个 agent 输出都要附验证证据。
- 每个重复流程最终沉淀为 skill。

### Jarvis Skill 候选

- `jarvis-think`: 需求澄清、边界、验收标准、执行计划。
- `jarvis-read`: URL / PDF / GitHub / X 内容清洗成 Markdown。
- `jarvis-learn`: source ledger -> link analysis -> synthesis。
- `jarvis-check`: diff、测试、破坏性操作、规则一致性审查。
- `jarvis-health`: AGENTS、memory、skills、tasks、hooks、API token 状态体检。
- `jarvis-ship`: 运行验证、记录 observation、done task、reflect、更新报告。

## 最值得照搬的 10 条

1. 用开源项目验证观点。
2. 把个人工作流产品化。
3. 把工程习惯 skill 化。
4. 把学习变成输出流程。
5. 把文档交付当成产品能力。
6. 把 AGENTS.md / CLAUDE.md 当作 agent 入职文档。
7. 把 Agent 视为 model + harness + tools + memory + eval 的系统。
8. 把发布节奏写成持续叙事。
9. 把复杂工具做成零配置默认体验。
10. 把社区反馈接入下一轮产品迭代。

## 对你当前 workspace 的建议

优先把 `jarvis-learn` 和 `jarvis-health` 做成正式 skill。前者复用本次调研三件套流程，后者复用 Waza `/health` 的思想，定期审计 Jarvis 的 AGENTS、memory、tasks、rules、available skills、last reflection 和验证能力。

