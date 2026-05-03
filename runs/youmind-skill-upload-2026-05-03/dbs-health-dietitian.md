# DBS 健康营养师内容

Source: `/Users/lizongru/.agents/skills/dbs-health-dietitian/SKILL.md`

## Description

营养师相关内容 skill。用于营养师账号定位、营养咨询流程、饮食评估、24小时回顾、ADIME、食谱边界、转诊信号和专业服务设计。 Trigger: /dbs-health-dietitian, "营养师", "营养咨询", "怎么做营养师账号", "饮食评估".

## Instruction

# dbs-health-dietitian：营养师方法和服务流程

你负责把营养师相关内容做成专业、克制、可执行的账号资产。核心原则：先评估，再建议；先闭环，再食谱。

## 资料入口

```bash
"Knowledge of 心理学/.venv/bin/python" "Knowledge of 健康赛道/scripts/search_health_xhs.py" "{关键词}" --module dietitian
```

必要时阅读：

- `/Users/lizongru/codex/humanOS/Knowledge of 健康赛道/notes/dietitian.md`

## 核心框架

### ADIME

| 阶段 | 要做什么 |
|---|---|
| Assessment | 身高体重、腰围、病史、用药、饮食记录、运动、睡眠、目标、预算 |
| Diagnosis | 营养问题，不做医学诊断 |
| Intervention | 饮食结构、行为目标、环境调整 |
| Monitoring/Evaluation | 指标、周期、复盘 |

### 24小时饮食回顾

必须记录：

- 时间
- 食物和饮料
- 份量
- 烹调方式
- 品牌/外食店
- 饥饿感和情绪

## 输出模板

```markdown
# 营养师内容/服务设计：{主题}

## 先问什么
- {评估问题}

## 能给什么建议
- {饮食结构}
- {行为目标}

## 不能做什么
- {医疗诊断/停药/治疗承诺}

## 小红书表达
- 封面：
- 标题：
- 正文结构：

## 来源
- {专业来源}
```

## 转诊信号

出现不明原因体重快速下降、吞咽困难、便血、持续呕吐、严重水肿、低血糖、胸痛、妊娠并发症、儿童生长异常，直接建议就医或多学科处理。
