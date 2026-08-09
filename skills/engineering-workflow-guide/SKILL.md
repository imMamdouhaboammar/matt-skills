---
name: engineering-workflow-guide
description: Use first when an engineering or productivity task could fit multiple workflows, when the user asks what to do next, or when a task spans planning, implementation, debugging, review, architecture, research, setup, or handoff. Route to the smallest useful skill set and avoid overlapping workflows.
---

# Engineering Workflow Guide

Route work before executing it when the best specialist is not already obvious.

1. Read `references/catalog.md`.
2. Classify the user's actual job, not just keywords.
3. Choose one primary skill. Add a second only when it owns a distinct phase or quality gate.
4. Prefer the narrowest skill that fully covers the current job.
5. Use `setup-engineering-workflows` first when repository-level issue tracking or domain-doc conventions are required but not configured.
6. When the user already named a skill, use it unless it clearly conflicts with the task or higher-priority instructions.
7. For multi-phase work, state the route briefly, then execute the first applicable phase. Do not invoke overlapping skills for ceremony.

## Common routes

- New feature, still fuzzy: `grill-with-docs` -> `to-spec` -> `to-tickets` -> `implement`
- Small concrete behavior: `tdd`
- Hard bug or performance regression: `diagnosing-bugs` -> `tdd`
- Review a branch or PR: `code-review`
- Architecture quality: `improve-codebase-architecture` or `codebase-design`
- Huge multi-session effort: `wayfinder` -> `to-spec` -> `to-tickets`
- Primary-source investigation: `research`
- Continue work elsewhere: `handoff`
- Human-only setup or dashboard steps: `wizard`
- Repeated operational work -> `workflow-designer`
- Git operation with destructive potential -> `git-safety-guardrails`
- Repository commit-time checks -> `setup-pre-commit`
- TypeScript package boundaries -> `setup-ts-deep-modules`
- Course or workshop exercises -> `scaffold-exercises`
- Long-form writing from raw material -> `writing-fragments` -> `writing-shape` or `writing-beats`

Completion criterion: the selected route names the smallest set of packaged skills needed for the task, and every selected skill exists in the catalog.
