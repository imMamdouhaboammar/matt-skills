---
name: setup-ts-deep-modules
description: Use when a TypeScript repository should enforce package entry points, hidden implementation folders, tests through public interfaces, and cycle checks with dependency-cruiser, especially in a flat packages directory or monorepo.
---

# Setup TypeScript Deep Modules

Use dependency-cruiser to make each package expose a small public surface while keeping implementation details private.

## Process

1. Inspect the repository first:
   - package manager and TypeScript version
   - package/workspace layout
   - existing dependency-cruiser or architecture checks
   - public entry-point conventions (`exports`, root files, barrel files, package manifests)
2. Choose the package root from evidence. Do not force `src/packages` when the repository already uses another layout.
3. Install `dependency-cruiser` as a dev dependency when missing.
4. If no configuration exists, copy `dependency-cruiser.config.cjs` to the repo root and set `PACKAGES_ROOT`. If a config already exists, merge the boundary rules into it rather than replacing it.
5. Enforce these properties:
   - external code reaches package root entry points, not nested internals
   - a package can use its own internals freely
   - tests exercise packages through public entry points, except private test fixtures within the same test area
   - test folders remain private to production code
   - dependency cycles fail the check
6. Keep package layering rules separate. Add them only when the repository has an actual layering policy.
7. Add `lint:boundaries` using the repository's package manager and include it in the existing CI/check path.
8. Prove the rules: clean run passes, a temporary deep import fails for the intended rule, revert it, clean run passes again.
9. Document the package boundary convention next to the governed packages and add a short context pointer to `AGENTS.md` or the repository's existing agent instruction file.

Use the repository's actual TypeScript/dependency-cruiser behavior as the final authority. Current dependency-cruiser supports forbidden rules, circular checks, TypeScript configuration, and CLI enforcement.

Completion criterion: the boundary check is wired into normal verification and has demonstrated pass -> intentional violation fail -> pass behavior.
