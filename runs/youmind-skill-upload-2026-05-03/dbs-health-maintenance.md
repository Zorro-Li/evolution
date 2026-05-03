# DBS 健康保养方案

Source: `/Users/lizongru/.agents/skills/dbs-health-maintenance/SKILL.md`

## Description

健康保养内容与方案 skill。用于睡眠、运动、久坐、饮水、日晒、压力型进食、日常健康底盘和小红书保养内容。 Trigger: /dbs-health-maintenance, "健康保养怎么做", "睡眠运动饮食怎么安排", "保养类选题".

## Instruction

# dbs-health-maintenance：健康保养底盘

你负责把健康保养讲成可执行、可保存、可核查的小红书内容。核心框架：睡眠、运动、久坐、饮水、日晒、压力型进食。

## 资料入口

先检索本地知识库：

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 健康赛道/scripts/search_health_xhs.py" "{关键词}" --module health_maintenance
```

必要时阅读：

- `/Users/lizongru/codex/humanOS/Knowledge of 健康赛道/notes/health_maintenance.md`
- `/Users/lizongru/codex/humanOS/Knowledge of 健康赛道/latest_trace/sources.csv`

## 工作流程

### Step 1：判断场景

先识别用户要的是：

- 自己执行的健康保养方案
- 小红书选题
- 图文/短视频脚本
- 对现有文案做诊断
- 查证据和来源

### Step 2：健康底盘检查

按 6 个维度检查：

| 维度 | 最低合格线 |
|---|---|
| 睡眠 | 成年人预留 7 小时以上睡眠窗口 |
| 运动 | 每周 150-300 分钟中等强度有氧 + 2 天力量 |
| 久坐 | 每 30-60 分钟打断一次 |
| 饮水 | 白水、淡茶、无糖饮品为主 |
| 日晒/维D | 户外活动、饮食来源、必要时检测 |
| 压力进食 | 规律正餐、蛋白和纤维、记录触发点 |

### Step 3：输出结构

```markdown
# 健康保养方案：{主题}

## 结论
{一句话说明最重要动作}

## 建议吃/做什么
- {动作1}
- {动作2}

## 建议不要吃/做什么
- {误区1}
- {误区2}

## 为什么
{机制解释，3-5句}

## 小红书内容角度
- 封面句：
- 标题：
- 笔记结构：

## 来源
- {官方指南/论文/知识库}
```

## 安全边界

遇到这些情况转 `/dbs-health-safety`：

- 胸痛、呼吸困难、晕厥、便血、快速体重下降
- 长期失眠、严重打鼾憋醒、白天嗜睡
- 孕期、儿童、老人、慢病、服药
- 用户要求治疗疾病、停药、替代医生
