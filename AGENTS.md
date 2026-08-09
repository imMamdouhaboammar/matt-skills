# Repository maintenance

This repository is the public source for the `matt-skills-curated` ChatGPT/Codex plugin.

- `skills/` is flat and contains only public, curated Skills.
- Every Skill must have `SKILL.md` and `agents/openai.yaml`.
- User-invoked Skills must pair `disable-model-invocation: true` with `policy.allow_implicit_invocation: false`.
- `engineering-workflow-guide` is the model-invoked router and its catalog must cover every other packaged Skill exactly once.
- Keep upstream provenance and MIT attribution accurate.
- Keep beta, deprecated, harness-specific marketplace, telemetry, credentials, symlinks, and generated duplicate Skills out of the public tree.
- Run `python3 scripts/validate_plugin.py` and deterministic double packaging before committing a release.
