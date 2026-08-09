---
name: workflow-designer
description: Use when a recurring task, operational routine, content process, review loop, or personal/team workflow should be turned into an implementable specification with triggers, inputs, actions, human checkpoints, outputs, failure handling, and ownership.
---

# Workflow Designer

Turn repeated work into an implementable workflow specification. Use the user's real tools and terminology; do not force automation where a manual step is better.

## Process

1. Identify one repeated job worth specifying. If several jobs are mixed together, split them before detailing steps.
2. Capture the current reality in `WORKFLOW-NOTES.md` when durable workspace notes are useful: tools, channels, terminology, constraints, and known failure cases.
3. Interview only for information that changes implementation. Attach a recommended default to each unresolved design question.
4. Write one file per workflow under `workflows/<slug>.md` with:
   - purpose and owner
   - trigger: event, schedule, or explicit manual start
   - required inputs and access
   - ordered actions
   - human checkpoints, if any, with the exact decision the human makes
   - outputs and where they are stored or sent
   - idempotency/retry expectations
   - failure and escalation behavior
   - privacy or credential constraints
   - observability: what proves a run succeeded
   - acceptance criteria for implementation
5. Prefer event triggers over polling when the actual platform supports them, but do not invent webhook availability.
6. Push human review later only when earlier automation is low-risk and reversible. Keep checkpoints earlier when irreversible writes, money, legal commitments, publication, or sensitive decisions are involved.
7. Mark every unresolved dependency explicitly. A workflow is not implementation-ready while a required decision is hidden in prose.

Completion criterion: an implementer can build the workflow without inventing trigger semantics, data sources, approvals, destinations, or failure behavior.
