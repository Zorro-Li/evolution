---
type: concept
title: Manxis Company Research Demo 2026 05 03
---

# ManXis Company Research Demo

日期：2026-05-03

## 目标

这个 demo 验证 ManXis 可以把原本依赖 API key 的 Agent 调用改成调用本地 Codex CLI。公司研究请求通过 FastAPI 进入后端，后端把研究 prompt 发给本机 Codex，Codex 使用 web search 生成报告并回传给同一个 `/research/{job_id}/report` 接口。

## 本轮产物

| 公司 | 文件 | 字符数 | 用途 |
|---|---:|---:|---|
| Compresr | `compresr.md` | 10265 | 直接竞品：context compression / token savings。 |
| The Token Company | `the-token-company.md` | 9887 | 直接竞品：LLM input compression middleware。 |
| Helicone | `helicone.md` | 9324 | 相关生态：LLM observability / gateway traces。 |

## 运行方式

```bash
cd /Users/lizongru/codex/进化/tools/company-research-agent
MANXIS_RESEARCH_PROVIDER=codex \
MANXIS_CODEX_CWD=/Users/lizongru/codex/进化/tools/company-research-agent \
.venv/bin/python -m uvicorn application:app --host 127.0.0.1 --port 8000
```

## 验证方式

```bash
curl -s http://127.0.0.1:8000/
```

期望输出：

```json
{"message":"Alive"}
```

## 战略判断

第一批公司研究应围绕 token compression、LLM observability、AI gateway 和 coding-agent workflow 展开。ManXis 的差异化切入点是读取真实 trace，输出 token waste attribution、质量风险和 workflow patch；Compresr 和 The Token Company 证明买方已经理解“上下文膨胀会烧钱”，Helicone 证明 trace/observability 是天然输入源。
