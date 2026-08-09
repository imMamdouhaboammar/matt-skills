# Issue tracker: Local Markdown

Use repository-local Markdown under `.scratch/` when no remote tracker convention is established.

## Conventions

- One effort per directory: `.scratch/<effort>/`.
- The spec is `.scratch/<effort>/spec.md` when one exists.
- Tickets are `.scratch/<effort>/issues/<NN>-<slug>.md`, numbered from `01`.
- A ticket records `Status: open|claimed|resolved`, `Assignee: <owner>` when claimed, optional `Blocked by: NN, NN`, and `Type: research|prototype|grilling|task` when used by wayfinder.
- Conversation history appends under `## Comments`.

## Skill phrases

- **publish to the issue tracker**: create the appropriate file under `.scratch/<effort>/`.
- **fetch the relevant ticket**: read the referenced ticket file.

## Wayfinding operations

- **Map**: `.scratch/<effort>/map.md`.
- **Child**: `.scratch/<effort>/issues/<NN>-<slug>.md`; numeric order is map order.
- **Blocking**: a child is blocked until every numbered ticket in `Blocked by:` has `Status: resolved`.
- **Frontier**: scan children in numeric order and choose the first open, unblocked, unclaimed ticket.
- **Claim**: atomically create `.scratch/<effort>/.claims/<NN>/` with `mkdir`. If creation fails, another session owns the claim, so skip it. Write the current session owner into `.claims/<NN>/owner`, set `Status: claimed` and `Assignee: <owner>` in the ticket, then reread both files and verify they agree before doing work. If verification fails, abandon the claim and skip the ticket.
- **Resolve**: append the result under `## Answer`, set `Status: resolved`, then append a Decisions-so-far entry that links the ticket title to its relative `issues/<NN>-<slug>.md` file and follows it with a one-line gist. Remove the claim directory only after the resolved state is safely written.
- **Abandon**: if a claimed session intentionally gives up, restore `Status: open`, clear `Assignee`, then remove its own claim directory. Never remove another owner's claim.
