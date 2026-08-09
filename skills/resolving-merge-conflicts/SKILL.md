---
name: resolving-merge-conflicts
description: "Use when you need to resolve an in-progress git merge/rebase conflict."
---

1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk when intent is clear.** Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off. Do **not** invent new behaviour. If intent is unclear, stop and ask for direction. If safe resolution is impossible or the user wants to discard the operation, obtain explicit approval before running `git merge --abort` or `git rebase --abort`, then stop rather than forcing a resolution.

4. Discover the project's **automated checks** and run them — typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage everything and commit. If rebasing, continue the rebase process until all commits are rebased.
