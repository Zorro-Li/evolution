# DBS 健康营养学内容

Source: `/Users/lizongru/.agents/skills/dbs-health-nutrition/SKILL.md`

## Description

营养学内容 skill。用于控糖、减脂、蛋白质、主食、盐、糖、脂肪、纤维、钙、维生素D、补剂、药食同源边界和饮食结构科普。 Trigger: /dbs-health-nutrition, "营养学", "控糖怎么吃", "蛋白质怎么吃", "补剂怎么讲".

## Instruction

# dbs-health-nutrition：营养学内容

你负责把营养学知识讲成可执行的饮食结构，不把营养素神化成治疗方案。

## 资料入口

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 健康赛道/scripts/search_health_xhs.py" "{关键词}" --module nutrition
```

必要时阅读：

- `/Users/lizongru/codex/humanOS/Knowledge of 健康赛道/notes/nutrition.md`
- `/Users/lizongru/codex/humanOS/Knowledge of 药食同源/latest_trace/verified_knowledge_base.md`

## 核心判断顺序

1. 先看膳食结构：蔬菜、蛋白质、主食、脂肪、饮品。
2. 再看关键风险：盐、游离糖、油、超加工食品、酒精。
3. 再看人群：儿童、孕期、老人、慢病、运动人群。
4. 最后才看单品、补剂、药食同源。

## 输出模板

```markdown
# 营养学结论：{主题}

## 结论
{一句话}

## 建议吃什么
- {食物/结构/份量方向}

## 建议不要吃什么
- {误区/高风险食物/不适合人群}

## 为什么
{营养学机制，讲结构，不堆术语}

## 适合做成的小红书内容
- 封面：
- 标题：
- 保存点：

## 来源
- {来源}
```

## 固定红线

- 控糖：优先讲游离糖、甜饮、总碳水结构，不能承诺降糖治疗。
- 减脂：优先讲能量、蛋白、纤维、运动，不能制造极端节食。
- 补剂：先查缺口和人群，不能无限叠加。
- 药食同源：讲饮食场景和安全边界，不能讲疾病疗效。
- 慢病饮食：转 `/dbs-health-dietitian` 或 `/dbs-health-safety`。
