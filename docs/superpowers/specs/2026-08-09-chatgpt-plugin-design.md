# ChatGPT Plugin Design

## Goal
Transform the fork into a public-ready, skills-only ChatGPT/Codex plugin that preserves the useful stable engineering and productivity workflows while removing repository-development noise.

## Scope
- Keep all 25 upstream promoted skills from `skills/engineering` and `skills/productivity`.
- Promote the existing router into `engineering-workflow-guide`, a model-invoked Skill that lets ChatGPT choose the narrowest useful specialist automatically.
- Keep each promoted skill directory intact, including `agents/openai.yaml`, support files, and deterministic scripts.
- Exclude `misc`, `in-progress`, and `deprecated` from the public plugin.
- Remove Claude-only marketplace metadata, changesets, npm release plumbing, source-development docs, and local harness linking scripts from the final public tree.
- Preserve MIT attribution and record the exact upstream commit used for the curation.

## Architecture
Use a skills-only plugin. The final `skills/` directory is flat: every immediate child is a valid Skill, which satisfies the single-path Codex plugin manifest and avoids generated duplicates or symlinks. `engineering-workflow-guide` owns routing and replaces the branded manual-only `ask-matt` surface. `setup-matt-pocock-skills` is adapted to `setup-engineering-workflows`.

## Public package
The package contains `.codex-plugin/plugin.json`, `skills/`, square SVG branding, README, LICENSE, THIRD_PARTY_NOTICES, PRIVACY, TERMS, SUPPORT, provenance metadata, and stdlib-only validation/package scripts. No MCP, hooks, telemetry, credentials, node_modules, source-only buckets, or Claude plugin metadata ship.

## Portability changes
- Rewrite cross-skill prose away from Claude slash-command assumptions where necessary.
- Update setup guidance to prefer `AGENTS.md` on OpenAI surfaces and avoid creating `CLAUDE.md` as a requirement.
- Keep user-invoked skills non-implicit through existing `agents/openai.yaml` policy.
- Keep model-invoked descriptions rich enough for discovery, but make the new guide the fallback router for ambiguous engineering/productivity tasks.

## Safety and quality gates
- No offensive-security specialist or exploit workflow is introduced.
- Scan for secrets, absolute user paths, telemetry bootstraps, `.DS_Store`, symlinks, and source-development directories.
- Validate every Skill frontmatter and OpenAI metadata.
- Verify guide/catalog coverage equals packaged skills.
- Run Plugin Autopilot validation, deterministic double packaging, archive inspection, and isolated Codex install smoke.
- Push through a feature branch, open a PR, inspect CI, then merge without force-pushing.
