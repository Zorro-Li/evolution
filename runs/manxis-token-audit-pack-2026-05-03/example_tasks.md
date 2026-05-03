# ManXis Benchmark Example Tasks

## Task 1: Coding Agent Repo Change

| Field | Value |
|---|---|
| User goal | Modify a real repository feature across 3-5 files and run tests. |
| Why expensive | Agent repeatedly reads files, runs commands, captures long logs, retries after test failures. |
| Baseline metrics | tokens, cost, runtime, command count, retries, test pass/fail. |
| ManXis patch | File-summary cache, tool-output reducer, test-log summarizer, compact threshold. |
| Success | Same tests pass with fewer tokens and comparable runtime. |

## Task 2: Company Research Agent Report

| Field | Value |
|---|---|
| User goal | Generate a current company research report with references. |
| Why expensive | Search results, web pages, duplicated facts, report editing, reference formatting. |
| Baseline metrics | tokens per source, report tokens, edit-pass tokens, sources used. |
| ManXis patch | Source ledger compression, briefing schema, reference-preserving final sweep. |
| Success | Report keeps source coverage and strategic read with lower context footprint. |

## Task 3: Browser / Workflow Automation Agent

| Field | Value |
|---|---|
| User goal | Use browser or tool calls to complete a multi-step operational workflow. |
| Why expensive | Screenshots, DOM text, retries, verbose tool returns, state re-derivation. |
| Baseline metrics | tool calls, observation tokens, failed branches, human interventions. |
| ManXis patch | State ledger, observation reducer, action/result schema, retry cutoff. |
| Success | Task completes with fewer observations inserted into context and fewer retries. |
