---
name: setup-pre-commit
description: Use when a JavaScript or TypeScript repository needs reliable pre-commit quality checks with Husky and lint-staged, while preserving the repository's package manager, formatter, existing hooks, and test/typecheck conventions.
---

# Setup Pre-Commit

Set up a fast pre-commit path with Husky v9 and lint-staged without overwriting existing repository conventions.

## Process

1. Detect the package manager from the lockfile and `packageManager` field. Inspect existing `.husky/`, lint-staged config, formatter config, and `package.json` scripts.
2. Preserve existing hooks and `prepare`/install lifecycle behavior. Merge changes rather than replacing unrelated commands.
3. Install missing development dependencies using the detected package manager: `husky`, `lint-staged`, and a formatter only when the repository already uses or explicitly wants one.
4. Initialize Husky with the package-manager equivalent of `husky init` when `.husky/` is not already configured. Husky v9 uses `prepare: "husky"` for npm/pnpm/bun flows; respect package-manager-specific lifecycle conventions already present in the repository.
5. Configure lint-staged for **staged files only**. Prefer the formatter/linter commands already used by the repo. Avoid inventing a new Prettier configuration when another formatter is authoritative.
6. Keep the pre-commit hook reasonably fast. Run full typecheck/tests only when the repository already treats commit-time execution as acceptable; otherwise keep expensive checks in CI and use narrow staged checks locally.
7. Verify the hook file, lint-staged config, lifecycle script, and executable behavior. Exercise the hook on a harmless staged change or run the exact hook commands directly.
8. Report what runs at pre-commit versus what remains CI-only.

Completion criterion: a normal commit runs the repository-approved staged checks, existing hooks remain intact, and the setup does not impose a new formatter or expensive full-suite command without evidence that the repo wants it.
