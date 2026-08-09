---
name: migrate-to-shoehorn
description: Use when TypeScript tests rely on unsafe `as` or `as unknown as` assertions for fixtures and the user wants to migrate those test-only values to `@total-typescript/shoehorn` with explicit intent.
---

# Migrate to Shoehorn

Use `@total-typescript/shoehorn` to make intentionally partial or malformed **test data** explicit. Do not introduce Shoehorn into production code.

Current API:

- `fromPartial<T>(value)`: deeply partial test fixture, with excess-property checking
- `fromAny<T>(value)`: deliberately malformed data for negative-path tests
- `fromExact<T>(value)`: full exact fixture when the test should satisfy the complete type

## Process

1. Confirm the affected files are tests or test fixtures.
2. Detect the package manager and existing dependency policy. Add `@total-typescript/shoehorn` using that package manager if it is not already present.
3. Locate suspicious assertions in test code. Do not replace every `as` mechanically; determine what each assertion is expressing.
4. Choose the helper by intent:
   - partial but structurally meaningful fixture -> `fromPartial`
   - deliberately invalid shape or value -> `fromAny`
   - complete strict fixture -> `fromExact`
5. Prefer call-site inference when it is clear. Use an explicit generic when a standalone fixture needs a stable target type.
6. Remove obsolete assertions and add imports without changing runtime behavior.
7. Run the repository typecheck and the narrowest relevant test suite.
8. Search the changed test files again for the original unsafe assertion pattern and review any survivors intentionally.

## Guardrails

- Keep Shoehorn test-only.
- Preserve tests that intentionally exercise invalid runtime input.
- Do not use `fromAny` merely to silence a type error that should be fixed.
- Do not migrate production casts into a testing utility.

Completion criterion: changed tests express fixture intent through the appropriate Shoehorn helper, typecheck passes, and the relevant tests still validate the same behavior.
