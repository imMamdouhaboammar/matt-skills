---
name: scaffold-exercises
description: Use when a course, workshop, tutorial, or training repository needs new exercise folders, problem/solution/explainer variants, starter files, numbering, or lint-ready scaffolding that follows the repository's own conventions.
---

# Scaffold Exercises

Create exercise structure from the repository's existing conventions instead of assuming one course framework.

## Process

1. Inspect the repository for existing exercise roots, numbering, naming, variants, lint commands, starter files, and examples.
2. Treat an existing nearby exercise as the primary template. If the repository has no convention, use this portable fallback:
   - section: `NN-section-name/`
   - exercise: `NN.NN-exercise-name/`
   - variants only when useful: `problem/`, `solution/`, `explainer/`
   - each created variant gets a non-empty `README.md`
3. Parse the requested plan into sections, exercises, and variants before creating files. Detect duplicate numbers or names first.
4. Create only the files needed for a valid scaffold. Do not fabricate lesson content to make the tree look complete.
5. When moving existing exercises, preserve history with `git mv` when Git is available.
6. Run the repository's actual exercise/content lint if one exists. Examples include project-specific CLIs, markdown link checks, typecheck, or test commands. Do not require a tool that the repository does not use.
7. Fix broken links, duplicate numbering, missing required files, or invalid naming until the repository's checks pass.

Completion criterion: the new exercise tree follows the local course conventions, contains no placeholder-only junk beyond explicitly requested stubs, and passes the repository checks that govern exercise content.
