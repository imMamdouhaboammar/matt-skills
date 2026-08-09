---
name: git-safety-guardrails
description: Use when a repository needs explicit safeguards around destructive or irreversible Git operations, especially force pushes, hard resets, cleans, destructive restores, branch deletion, or history rewrites.
---

# Git Safety Guardrails

Add repository-local guidance and optional command classification for Git operations that can destroy work or rewrite shared history.

## Process

1. Inspect `AGENTS.md`, contribution docs, branch protection guidance, and the current Git workflow before changing anything.
2. Preserve existing repository policy. Add only missing safety rules.
3. Classify Git commands into:
   - `allow`: read-only or ordinary local operations such as status, diff, log, add, normal commit, fetch, or creating a new branch.
   - `review`: operations that can discard local work or rewrite history, such as `reset --hard`, `clean -f`, destructive checkout/restore, deleting a branch with `-D`, force push, or rebasing published work.
4. For `review` operations, inspect the current state and explain the concrete impact before execution. Follow the host's approval and confirmation rules. Prefer a reversible alternative when it achieves the same goal.
5. If the user wants durable repository guidance, add a compact `Git safety` section to `AGENTS.md` rather than installing host-specific hooks.
6. If a local command classifier is useful, use `scripts/classify_git_command.py`. It is advisory and does not bypass host permissions.

## Durable policy template

Record only the rules the repository actually needs. Typical examples:

- inspect `git status` and relevant diffs before any destructive cleanup
- preserve unrelated worktree changes
- do not force-push, hard reset, clean untracked files, delete branches forcefully, or discard the whole worktree without explicit user approval
- do not rewrite shared history when a normal follow-up commit is sufficient
- never force-push over unrelated remote history

Completion criterion: risky Git operations have an explicit review path, ordinary Git work remains unobstructed, and no host-specific hook is required for the policy to be discoverable.
