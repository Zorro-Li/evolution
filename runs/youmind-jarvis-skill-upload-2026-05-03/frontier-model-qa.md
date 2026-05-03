# 前沿模型 QA 拆解

ID: `frontier-model-qa`

## Description

把模型能力展示转成可复现测试：prompt、输出、验证目标、失败模式和本地 pass/fail。适合多模态、图像、SVG、QR、文本渲染和推理边界测试。

## Sources

- `runs/x-creator-watch/2026-05-02/handles/goodside/skill.md`
- `runs/x-creator-watch/2026-05-02/handles/BoyuanChen0/skill.md`

## Instruction

# 前沿模型 QA 拆解

你的目标是把模型展示、截图、prompt 和 viral demo 转成可复现的能力测试。

## 输入
- 模型、prompt、输出截图/文件、声称能力、验证目标。

## 工作流
1. 提取 claim：模型被说成能做什么。
2. 拆任务类型：SVG、QR、字形、棋局、时钟、地图、图表、文本渲染、引用查找、视觉推理。
3. 固定 prompt 和运行条件：模型、参数、工具、输入、输出格式。
4. 设计外部验证：扫码、OCR、编译、像素检查、规则校验、人工 spot check。
5. 写失败模式：局部正确、视觉幻觉、文本错字、布局错位、隐藏信息失败、不可复现。
6. 保存测试资产：prompt、output、screenshot、verification command。

## 输出格式
```markdown
## Model QA Case
- Claim:
- Prompt:
- Model/tool:
- Output artifact:
- Verification target:
- Pass criteria:
- Failure modes:
- Reproduction command:
```

## 验收
- 每个能力 claim 有独立验证方法。
- 视觉任务至少有截图或像素/结构检查。
- 不把 demo 热度当成能力证据。
