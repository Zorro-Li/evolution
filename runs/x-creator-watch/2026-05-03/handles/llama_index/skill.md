# x-creator-llama-index

Use this skill to analyze LlamaIndex/LlamaParse signals and turn document-heavy AI workflows into local agent skills.

## Trigger

Use when the user mentions document OCR, PDFs, RAG quality, LlamaIndex, LlamaParse, LlamaCloud, MCP for document processing, document benchmarks, or agent workflows over files.

## Inputs

- Document set.
- Target task.
- Desired schema.
- Retrieval/action requirements.
- Known failure dimensions.
- Eval sample.

## Steps

1. Identify document type and downstream task.
2. Split the workflow into parse, classify, extract, index, retrieve, act, and evaluate.
3. Choose local, SDK, API, MCP, or cloud parsing surface.
4. Define page/citation/confidence output fields.
5. Build a small benchmark around real failure cases.
6. Run extraction on a sample and inspect failure modes.
7. Package the procedure as a reusable local workflow.

## Output

Return a document-agent plan with sources, schema, parser choice, eval checks, failure modes, and next automation.

## Validation

- Every output field traces to a source location or confidence.
- Every workflow has an eval set.
- Every recommendation maps to a concrete document operation.

