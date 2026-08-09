# Matt Skills Curated

A curated, ChatGPT/Codex-ready distribution of Matt Pocock's MIT-licensed engineering and productivity Skills, maintained by Mamdouh Aboammar.

## What ships

The plugin contains 34 focused Skills under one native `skills/` root. `engineering-workflow-guide` is model-invoked and routes ambiguous engineering or productivity work to the narrowest useful specialist. All 34 packaged Skills are model-invoked so ChatGPT or Codex can route from the guide into the selected specialist automatically. External writes and tool actions still follow the permissions and confirmation rules of the active host.

Core workflows cover requirements discovery, specs, tickets, implementation, TDD, debugging, review, domain modeling, architecture, research, triage, Git safety, pre-commit quality, TypeScript package boundaries, workflow design, handoffs, teaching, exercise scaffolding, agent documentation, and long-form writing.

## What does not ship

The public package evaluates upstream `misc` and `in-progress` capabilities individually. Useful workflows are adapted and promoted into the flat public `skills/` root. The Claude-only background handoff is excluded because the portable `handoff` Skill already covers the durable handoff job, and the upstream deprecated bucket is empty. Claude marketplace metadata, changesets, npm release plumbing, local harness linking scripts, and source-development notes remain excluded as repository-maintenance material.

## Architecture

This is a skills-only plugin. It has no MCP server, remote service, telemetry, or plugin-owned credential store. Skills use the tools and permissions already available in the current ChatGPT or Codex session.

## Validate

```bash
python3 scripts/validate_plugin.py
python3 scripts/package_plugin.py /tmp/matt-skills-curated-a.zip
python3 scripts/package_plugin.py /tmp/matt-skills-curated-b.zip
cmp /tmp/matt-skills-curated-a.zip /tmp/matt-skills-curated-b.zip
```

## Source and attribution

The curated source snapshot is recorded in `source-provenance.json`. Original work is Copyright 2026 Matt Pocock and licensed under MIT. This fork adapts packaging, routing, portability, and public-plugin metadata; it does not claim original authorship of the upstream Skills.

See `THIRD_PARTY_NOTICES.md`, `PRIVACY.md`, `TERMS.md`, and `SUPPORT.md` for public distribution details.
