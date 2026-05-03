# DBS 健康小红书内容

Source: `/Users/lizongru/.agents/skills/dbs-health-xhs-content/SKILL.md`

## Description

小红书健康内容 skill。用于健康赛道选题、图文结构、短视频开头、标题、人设、内容诊断、产品化路径和笔记审核。 Trigger: /dbs-health-xhs-content, "健康小红书", "健康内容怎么做", "帮我做选题", "这篇笔记怎么改".

## Instruction

# dbs-health-xhs-content：健康小红书内容系统

你负责把健康知识转成小红书内容。参考 `dbs-content` 和 `dbs-hook`：先判断内容本身有没有价值，再处理标题、开头和形式。

## 资料入口

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 健康赛道/scripts/search_health_xhs.py" "{关键词}" --module xhs_content
```

必要时阅读：

- `/Users/lizongru/.agents/skills/dbs-content/SKILL.md`
- `/Users/lizongru/.agents/skills/dbs-hook/SKILL.md`
- `/Users/lizongru/codex/humanOS/Knowledge of 健康赛道/notes/xhs_content.md`

## 内容诊断流程

### Phase 1：选题值不值得做

判断：

- 是否有明确人群
- 是否有真实痛点
- 是否能给具体动作
- 是否有来源支撑
- 是否有治疗化风险

### Phase 2：形式匹配

| 内容类型 | 推荐形式 |
|---|---|
| 清单、替换表、步骤 | 图文 |
| 误区纠正、观点、边界 | 口播短视频 |
| 证据链、复杂解释 | 图文长卡 |
| 营养师服务流程 | 图文 + 主页合集 |
| 产品化工具 | 模板/表格/清单 |

### Phase 3：健康笔记结构

```markdown
# {标题}

## 先给结论
{一句话}

## 适合谁
{人群}

## 怎么做
{3-5个动作}

## 不要怎么做
{误区和禁忌}

## 为什么
{机制，3-5句}

## 来源
{官方指南/论文/知识库}
```

## 开头公式

健康内容开头 = 人群 + 具体错误 + 可信度。

例：

- “90%控糖失败，不是米饭问题，是饮料和酱料问题。”
- “成年人最便宜的保养，不是补剂，是先睡够7小时。”
- “靠谱营养师不会上来甩食谱，会先问你这7件事。”

## 红线

遇到治疗化、疾病、用药、孕期、儿童、慢病内容，先转 `/dbs-health-safety` 审核。
