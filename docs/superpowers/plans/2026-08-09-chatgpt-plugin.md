# ChatGPT Plugin Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `matt-skills` into a mature, public-ready skills-only ChatGPT/Codex plugin.

**Architecture:** Flatten only the 25 promoted upstream skills into a single plugin `skills/` root and add one model-invoked router. Keep skill-local support files intact, remove source-development buckets/tooling from the final tree, and add self-contained validation, packaging, legal, provenance, branding, and CI.

**Tech Stack:** Agent Skills format, `.codex-plugin/plugin.json`, YAML skill UI metadata, Python 3 stdlib validation/package scripts, GitHub Actions, Codex CLI smoke tests.

## Global Constraints
- Architecture is `skills-only`; no MCP or app server.
- Public package contains exactly the curated stable skills with the router adapted in place.
- Preserve MIT attribution to Matt Pocock and identify the fork maintainer separately.
- No symlinks, secrets, telemetry, absolute local paths, Claude marketplace metadata, beta/deprecated buckets, or generated duplicate skills.
- Plugin Directory listing fields obey current OpenAI limits verified on 2026-08-09.

---

### Task 1: Freeze curation and restructure skills
- [ ] Record upstream commit and the exact 25 promoted skill slugs.
- [ ] Move promoted skill directories to immediate children of `skills/`.
- [ ] Remove non-promoted buckets and bucket README caches.
- [ ] Run a structural assertion for 25 stable skills and zero duplicates.

### Task 2: Add routing and portability adaptations
- [ ] Rename `ask-matt` to model-invoked `engineering-workflow-guide` with a focused routing catalog.
- [ ] Rename `setup-matt-pocock-skills` to `setup-engineering-workflows` and update all cross-skill references.
- [ ] Adapt setup guidance to OpenAI/AGENTS.md semantics while keeping behavior intact.
- [ ] Verify every guide/catalog route points to an existing packaged skill.

### Task 3: Build production plugin surface
- [ ] Create `.codex-plugin/plugin.json` version `1.0.0`.
- [ ] Add square SVG logo and composer icon.
- [ ] Replace upstream-oriented README with installation, capability map, routing, safety, attribution, and development gates.
- [ ] Add LICENSE, THIRD_PARTY_NOTICES.md, PRIVACY.md, TERMS.md, SUPPORT.md, and `source-provenance.json`.

### Task 4: Remove repository-development noise
- [ ] Remove `.claude-plugin`, `.changeset`, `.out-of-scope`, source-only `.agents`, npm release files, old docs, and local linking/version scripts.
- [ ] Keep only files needed for plugin execution, public documentation, validation, packaging, and CI.
- [ ] Assert the final root allowlist and scan for forbidden directories/files.

### Task 5: Add self-contained gates and CI
- [ ] Add `scripts/validate_plugin.py` for curation, metadata, safety, dependency, and root-shape checks.
- [ ] Add deterministic `scripts/package_plugin.py`.
- [ ] Add `.github/workflows/ci.yml` running validation and double-package hash comparison.
- [ ] Run local validation and fix every failure.

### Task 6: External validation, smoke, and GitHub integration
- [ ] Run ChatGPT Plugin Autopilot validator.
- [ ] Build twice with Plugin Autopilot packager and require byte-identical archives.
- [ ] Install the exact artifact into an isolated Codex home and verify all 25 curated skills plus router metadata.
- [ ] Commit, push feature branch, open PR, inspect checks, merge after green, and verify `main` remotely.
