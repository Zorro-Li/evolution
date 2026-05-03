# Skill Distillation: @goodside

## Purpose

Use Riley Goodside as a source for frontier-model edge tests, especially multimodal prompts with verifiable structure.

## Workflow

1. Start at `https://x.com/goodside/highlights`.
2. Capture posts that combine image generation with checkable external semantics: SVG, QR, writing systems, clocks, chess, maps, diagrams, source references, or code.
3. Archive the prompt, the expected hidden structure, the visible result description, and metrics.
4. Classify each post by capability: text rendering, symbolic reasoning, image-grounded code, QR/OCR, spatial reasoning, reference lookup, or tool-generated intermediate artifact.
5. Convert the post into a local QA prompt with pass/fail checks.

## Output Template

```markdown
## Goodside Benchmark

- Source:
- Capability tested:
- Prompt shape:
- Hidden structure:
- Verification method:
- Failure notes:
- Local Jarvis test:
```

## Failure Modes

- Saving only the funny surface of the image.
- Missing the hidden verification target.
- Ignoring Riley's notes about failed simpler prompts.
