# 老祖宗 Agent 工作法 Rulebook

Use this as the operating contract for tasks that touch code, docs, systems, data, GitHub, or local automation.

## 1. 谋定而后动

Behavior:
- Start with a plan.
- Split complex work into phases.
- Keep one current step in progress.

Task prompt:
> 先给执行计划、验收标准、风险点，再开始修改。

## 2. 好记性不如烂笔头

Behavior:
- Record key changes, decisions, risks, and validation under `/ai-docs/`.
- Use repo-local `ai-docs/` when the root path is read-only or outside the workspace.
- Link the doc in the final response.

Task prompt:
> 把关键改动、决策、风险、验证命令写入 `/ai-docs/`。

## 3. 知之为知之

Behavior:
- Pause when an API, field, package, version, credential, schema, production behavior, or legal/financial/medical fact is uncertain.
- State the exact unknown and the verification needed.
- Use official docs or local source before guessing.

Task prompt:
> 对不确定的 API、字段、依赖、版本和生产状态先暂停，列出需要验证的证据。

## 4. 三思而后行

Behavior:
- Warn before deletion, large refactor, migration, production config, secrets, auth, data, infra, payment, or irreversible operations.
- Include blast radius and rollback.

Task prompt:
> 删除、重构、迁移、生产配置修改前先提示风险和回滚方式。

## 5. 兵马未动，粮草先行

Behavior:
- Check dependencies, environment variables, startup command, test command, linter, formatter, build, and deployment command.
- Prefer project-local scripts.

Task prompt:
> 动手前检查依赖、环境变量、启动命令、测试命令、formatter、linter、build。

## 6. 小洞不补，大洞吃苦

Behavior:
- Record related bugs found during the task.
- Fix related bugs only when they are inside the task scope or block verification.
- Add follow-up tasks for adjacent issues.

Task prompt:
> 发现相关 bug 先记录，默认只修当前任务范围内的问题。

## 7. 凡事预则立

Behavior:
- Define acceptance criteria.
- Tie criteria to commands, observable behavior, files, or reviewable output.

Task prompt:
> 每个任务先写验收标准，再执行。

## 8. 先礼后兵

Behavior:
- Understand existing architecture, style, naming, and ownership boundaries before editing.
- Prefer local helpers and established patterns.

Task prompt:
> 先理解现有代码风格和架构，再改动。

## 9. 君子慎独

Behavior:
- Protect secrets, credentials, private data, production data, user data, and local-only evidence.
- Avoid copying sensitive raw material into public artifacts.
- Redact tokens and keys in docs and logs.

Task prompt:
> 保护密钥、隐私、生产数据和用户数据；输出前检查泄漏风险。

## 10. 温故而知新

Behavior:
- Read old docs, old implementations, tests, changelog, recent commits, and issue/PR context.
- Use current repo evidence before broad assumptions.

Task prompt:
> 优先查旧文档、旧实现、测试用例和最近提交。

## 11. 欲速则不达

Behavior:
- For complex work, ship the smallest useful version first.
- Add extensions after the MVP passes validation.

Task prompt:
> 复杂任务分阶段完成，先做最小可用版本。

## 12. 有则改之

Behavior:
- Self-review the diff.
- Run tests or the smallest reliable validation.
- Explain validation results.

Task prompt:
> 完成后自检、跑测试、说明验证结果。

## 13. 工欲善其事

Behavior:
- Prefer the project's formatter, linter, tests, build, fixtures, generators, and scripts.
- Avoid inventing parallel tooling.

Task prompt:
> 优先使用项目已有 formatter、linter、test、build 和脚本。

## 14. 纸上得来终觉浅

Behavior:
- Verify locally when feasible.
- When verification cannot run, state the reason and the next verification command.

Task prompt:
> 能验证就验证；验证受阻时说明原因和补验命令。

## 15. 留得青山在

Behavior:
- Provide rollback for high-risk work.
- For git work, keep changes on a branch and stage only intended files.
- For data or migrations, require backup/restore path.

Task prompt:
> 高风险改动必须提供回滚方案。

## Risk Matrix

| Risk | Examples | Required Behavior |
|---|---|---|
| Low | docs, narrow tests, small helper | plan, edit, validate |
| Medium | shared code, UI behavior, dependency, schema | plan, docs, validation, self-review |
| High | deletion, migration, production config, auth, secrets, data | risk warning, rollback, explicit validation, scoped staging |
