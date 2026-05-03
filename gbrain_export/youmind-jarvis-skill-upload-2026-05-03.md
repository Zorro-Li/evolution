---
type: concept
title: Youmind Jarvis Skill Upload 2026 05 03
---

# YouMind Jarvis Skill Upload Pack

日期：2026-05-03

范围：只上传 Jarvis/Codex 在 `/Users/lizongru/codex/进化` 中归纳出的自有 Skill；DBS/dontbesilent 全部排除。

总数：13

| # | Skill ID | YouMind 标题 | 描述字数 | 指令字数 |
|---:|---|---|---:|---:|
| 1 | `jarvis-evolution-router` | Jarvis 进化 Skill 总入口 | 82 | 818 |
| 2 | `x-creator-intel-distiller` | X 创作者情报蒸馏 | 86 | 809 |
| 3 | `company-competitor-research` | 公司研究与竞品拆解 | 96 | 693 |
| 4 | `manxis-token-audit` | ManXis Token Audit | 101 | 796 |
| 5 | `llmops-gateway-design` | LLMOps Gateway 拆解 | 92 | 828 |
| 6 | `document-agent-workflow` | 文档 Agent 工作流拆解 | 91 | 687 |
| 7 | `agent-control-plane` | Agent 控制平面拆解 | 92 | 830 |
| 8 | `ancestral-agent-workflow` | 老祖宗 Agent 工作法 | 55 | 487 |
| 9 | `crypto-history-as-mirror` | 币圈以史为鉴 | 62 | 531 |
| 10 | `ai-supply-chain-bottleneck-research` | AI 供应链瓶颈研究 | 68 | 989 |
| 11 | `manxis-x-growth-playbook` | ManXis X 增长拆解 | 66 | 695 |
| 12 | `frontier-model-qa` | 前沿模型 QA 拆解 | 76 | 601 |
| 13 | `agent-memory-context` | Agent 记忆与上下文边界拆解 | 79 | 785 |

## 上传顺序

1. `Jarvis 进化 Skill 总入口`。
2. X 创作者、公司研究、ManXis、LLMOps、文档 Agent、Agent 控制平面。
3. 老祖宗 Agent 工作法、币圈以史为鉴、供应链、增长、模型 QA、记忆边界。

## 验证

```bash
python3 - <<'PY'
import json
from pathlib import Path
p = Path('/Users/lizongru/codex/进化/runs/youmind-jarvis-skill-upload-2026-05-03/payloads.json')
items = json.loads(p.read_text(encoding='utf-8'))
print(len(items), len({x['id'] for x in items}))
PY
```
