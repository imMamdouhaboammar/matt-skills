---
name: setup-engineering-workflows
description: Configure a repository for these engineering skills by recording issue-tracker conventions, triage labels, and domain-document locations. Run once before repository workflows that depend on those conventions.
disable-model-invocation: true
---

# Setup Engineering Workflows

Create the small amount of repository-local context the other engineering skills depend on.

## 1. Inspect

Read the repository before writing anything:
- `git remote -v` and `.git/config`
- root `AGENTS.md` if present
- `CONTEXT.md` or `CONTEXT-MAP.md`
- `docs/adr/`, `docs/agents/`, and `.scratch/`
- monorepo signals such as workspaces or populated `packages/`
- whether the `triage` skill is available

## 2. Resolve conventions

Use evidence to choose defaults, and ask only when the repository does not settle the choice.

### Issue tracker
Prefer GitHub when the remote is GitHub. Otherwise preserve an existing tracker convention. Local markdown under `.scratch/<feature>/` is the portable fallback. Record the result in `docs/agents/issue-tracker.md`.

### Triage labels
When `triage` is available, default to: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Preserve existing equivalent labels rather than creating duplicates. Record the mapping in `docs/agents/triage-labels.md`.

### Domain docs
Default to one root `CONTEXT.md` plus `docs/adr/`. Use a multi-context `CONTEXT-MAP.md` only when the repository is genuinely multi-package or already uses that layout. Record the rule in `docs/agents/domain.md`.

## 3. Write

Update the existing root `AGENTS.md`, or create one if the repository has no agent instruction file. Add or update an `## Agent skills` section that points to the files in `docs/agents/` without duplicating their content.

Never overwrite unrelated user instructions. Update an existing generated section in place.

## 4. Verify

Read the files back and confirm:
- the issue tracker can be located from the recorded rule
- triage labels map one-to-one when triage is enabled
- domain docs have one unambiguous location
- `AGENTS.md` contains exactly one `## Agent skills` section

Completion criterion: repository conventions are explicit enough that `to-spec`, `to-tickets`, `triage`, `wayfinder`, `domain-modeling`, and `grill-with-docs` can operate without guessing where project state belongs.
