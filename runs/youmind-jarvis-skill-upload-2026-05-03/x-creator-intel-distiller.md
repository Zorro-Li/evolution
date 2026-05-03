# X 创作者情报蒸馏

ID: `x-creator-intel-distiller`

## Description

把 X/Twitter 创作者拆成来源台账、账号强项、可复用工作流、Skill 草稿和 GBrain 页面。用于持续学习 AI、产品、增长、投资和 Agent 高信号账号。

## Sources

- `/Users/lizongru/.codex/skills/x-creator-distiller/SKILL.md`
- `runs/x-creator-watch/2026-05-02/05_skill_distillation.md`
- `runs/x-creator-watch/2026-05-03/03_skill_distillation.md`

## Instruction

# X 创作者情报蒸馏

你的目标是把一个 X/Twitter 创作者变成本地可用的知识资产。

## 输入
- X handle 或主页 URL。
- 用户关心的方向：AI、Agent、LLMOps、增长、投资、内容、产品、工程。
- 可访问的资料：profile、帖子、线程、外链、GitHub、博客、产品页。

## 工作流
1. 建来源台账：保存 profile URL、帖子 URL、外链、可见指标、采集日期。
2. 抽账号定位：他做什么、强在哪里、服务谁、凭什么可信。
3. 拆内容结构：选题、证据、语言、产品入口、互动方式。
4. 拆能力模型：他反复使用的判断流程、资料来源、筛选标准、输出模板。
5. 生成 Skill：触发条件、输入、步骤、输出格式、失败模式。
6. 入库：保存到 `runs/x-creator-watch/YYYY-MM-DD/`，再写 GBrain 摘要。
7. 下一步：给用户一个可执行动作，例如关注、对标、触达、复刻工作流、安装 Skill。

## 输出格式
```markdown
# Creator Intelligence: @handle

## Source Ledger
| Source | URL | Evidence | Date |

## What They Are Good At

## Repeatable Workflow
1.
2.
3.

## Skill Draft
- Trigger:
- Inputs:
- Steps:
- Output:
- Failure modes:

## Jarvis Use
- Where to store:
- Next action:
```

## 验收
- 每个判断都有 URL 或可见证据。
- Skill 不是人格模仿，而是工作流提炼。
- 长引用留在本地，公开材料用短锚点和原创总结。
