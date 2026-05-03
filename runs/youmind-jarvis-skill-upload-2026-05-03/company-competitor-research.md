# 公司研究与竞品拆解

ID: `company-competitor-research`

## Description

用本地 company-research-agent 和 Codex 生成公司调研、竞品卡、差异化表和目标客户判断。适合研究 AI 基础设施、Agent、LLMOps、SaaS 和投融资公司。

## Sources

- `tools/company-research-agent/CODEX_PROVIDER.md`
- `runs/manxis-company-research-2026-05-03/01_company_reports.md`
- `runs/manxis-company-research-demo-2026-05-03/README.md`

## Instruction

# 公司研究与竞品拆解

你的目标是把一家公司拆成商业判断，而不是资料拼贴。

## 输入
- 公司名、官网、行业、所在地。
- 研究目的：竞品、客户、集成伙伴、投资标的、销售线索。

## 工作流
1. 确定公司类型：直接竞品、相邻基础设施、目标客户、渠道伙伴、投资标的。
2. 收集来源：官网、docs、pricing、YC/Crunchbase/LinkedIn/GitHub、新闻、客户案例。
3. 拆公司概况：产品、目标市场、商业模式、团队信号。
4. 拆行业位置：市场类别、直接竞品、替代方案、差异化、挑战。
5. 拆商业健康：融资、定价、客户、使用量、开源/社区、收入线索。
6. 产出战略判断：为什么重要、风险缺口、后续追问。
7. 写入本地：`runs/company-research-YYYY-MM-DD/`，必要时入 GBrain。

## 输出格式
```markdown
# {Company} Research Report

## Company Overview
## Industry Overview
## Financial Overview
## News
## Strategic Read
### Why It Matters
### Risks / Gaps
### Questions For Follow-Up
## References
```

## 验收
- 至少 8 个来源 URL。
- 不确定的融资、收入、客户数据标为“unclear”。
- 最后必须给出 ManXis/Jarvis 可执行动作：学习、触达、集成或规避。
