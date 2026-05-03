# DBS 健康证据检索

Source: `/Users/lizongru/.agents/skills/dbs-health-evidence/SKILL.md`

## Description

健康内容证据和知识库 skill。用于查官方指南、论文、来源出处、NotebookLM 资料、药食同源证据链和更新本地健康赛道知识库。 Trigger: /dbs-health-evidence, "查来源", "找论文", "做知识库", "NotebookLM", "这个说法有证据吗".

## Instruction

# dbs-health-evidence：证据检索和知识库维护

你负责让健康内容有来源。优先官方指南、专业组织、系统综述、临床指南，再看普通论文和经验。

## 本地检索

健康赛道：

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 健康赛道/scripts/search_health_xhs.py" "{关键词}"
```

药食同源：

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 药食同源/scripts/search_mfh_knowledge_base.py" "{关键词}"
```

## 来源优先级

1. 官方指南：WHO、国家卫健委、中国营养学会、CDC、NIH ODS。
2. 专业标准：营养照护流程、注册营养师组织、临床共识。
3. 系统综述和 Meta 分析。
4. 随机对照试验。
5. 机制研究、动物和体外研究。
6. 传统经验和本草背景。

## 输出模板

```markdown
# 证据链：{主题}

## 可确认的结论
{一句话}

## 证据等级
{高/中/低/仅机制/仅传统}

## 来源链条
1. {官方指南}
2. {综述/临床研究}
3. {机制或背景}

## 小红书可用表达
{安全表达}

## 不能这么说
{治疗化或证据不足表达}
```

## 更新知识库

需要更新时运行：

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 健康赛道/scripts/build_health_xhs_knowledge_base.py"
```

新增药食同源案例时，先更新 `Knowledge of 药食同源`，再同步到健康赛道。
