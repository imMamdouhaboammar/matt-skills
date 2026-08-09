# Matt Skills Curated

A curated, ChatGPT/Codex-ready distribution of Matt Pocock's MIT-licensed engineering and productivity Skills, maintained by Mamdouh Aboammar.

## What ships

The plugin contains 25 focused Skills under one native `skills/` root. `engineering-workflow-guide` is model-invoked and routes ambiguous engineering or productivity work to the narrowest useful specialist. User-controlled orchestration Skills keep implicit invocation disabled through their `agents/openai.yaml` policy.

Core workflows cover requirements discovery, specs, tickets, implementation, TDD, debugging, code review, domain modeling, architecture, research, triage, prototyping, merge conflict resolution, setup, handoffs, teaching, and writing for agents.

## What does not ship

The public package intentionally excludes upstream `misc`, `in-progress`, and `deprecated` buckets, Claude marketplace metadata, changesets, npm release plumbing, local harness linking scripts, and source-development notes. Those are repository-maintenance concerns rather than ChatGPT plugin capabilities.

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
