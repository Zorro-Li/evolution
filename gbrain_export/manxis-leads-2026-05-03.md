---
type: concept
title: Manxis Leads 2026 05 03
---

# ManXis 设计伙伴线索包

日期：2026-05-03

## 目标

这份线索包服务 ManXis 的第一轮付费验证：用 `Local Token Audit` 找到愿意提供真实长任务 trace 的设计伙伴，交付 token 浪费地图、before/after 成本表和 workflow patch。

## 线索结构

| 字段 | 用途 |
|---|---|
| `priority` | `P0` 代表第一批触达，`P1` 代表第二批扩展。 |
| `segment` | 线索所属买方场景。 |
| `contact` | X handle 或公司账号。 |
| `company_project` | 关联公司、项目或生态位。 |
| `evidence_link` | 触达前核验入口。 |
| `scenario_hypothesis` | 为什么对方会有 token 浪费痛点。 |
| `audit_offer` | 对应的审计切入点。 |
| `first_message` | 第一条 DM / email 草稿。 |
| `source` | 来源：X following registry 或公司研究。 |

## 第一批 P0

| 顺序 | 对象 | 切入点 |
|---|---|---|
| 1 | @helicone_ai / Helicone | 用 Helicone request logs 做 trace audit。 |
| 2 | @PortkeyAI / Portkey | 把 gateway traces 转成 token waste map。 |
| 3 | @hwchase17 / LangChain | 用 LangSmith agent traces 验证 ManXis。 |
| 4 | @llama_index / LlamaIndex | 审计 RAG context bloat 和检索冗余。 |
| 5 | @nicdunz / Codex Mission Control | 找 Codex 长任务 power user trace。 |
| 6 | @dani_avila7 / Claude Code Skills | 审计 subagent / skill / hook workflow。 |
| 7 | @adocomplete / Claude Code community | 招募 Claude Code 高成本长任务样本。 |
| 8 | @openclaw / OpenClaw | 审计 workflow automation 的工具输出膨胀。 |
| 9 | Cursor / Anysphere | 审计多文件 coding-agent repo task。 |
| 10 | Compresr / The Token Company | 做竞品语言和定位拆解。 |

## 执行节奏

| 天数 | 动作 | 成功标准 |
|---|---|---|
| D1 | 触达 10 个 P0，全部用一条定制消息。 | 3 个回复。 |
| D2 | 给有回复的人发隐私 checklist 和 trace 输入格式。 | 1 条真实 trace。 |
| D3-D4 | 交付第一份 `Local Token Audit`。 | 报告里有可核验 savings claim。 |
| D5 | 要 2 个介绍或进入 paid pilot。 | 1 个 $500 pilot。 |

## 直接命令

```bash
python3 - <<'PY'
import csv
from pathlib import Path

path = Path("/Users/lizongru/codex/进化/runs/manxis-leads-2026-05-03/leads.csv")
with path.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    if row["priority"] == "P0":
        print(f'{row["contact"]} | {row["company_project"]} | {row["first_message"]}')
PY
```

## 推荐动作

今天先触达 Helicone、Portkey、LangSmith/LangChain、LlamaIndex、Codex Mission Control 这 5 类对象。它们已有 trace、cost、latency、eval 或 gateway 语境，最容易接受 `one trace in, audit report out` 的试点。
