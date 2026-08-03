# Prompt Versioning and Promotion

## Version semantics

Use `major.minor.patch` for approved prompt cards.

- **Major:** changes role authority, safety behavior, input/output contract, or intended task scope.
- **Minor:** adds supported behavior, improves instructions, or expands tested cases without breaking the contract.
- **Patch:** clarifies wording or fixes a defect while preserving behavior and contract.

Draft cards use a unique draft identifier and never silently replace an approved version. Prompt bundles record the exact version of every composed card.

## Lifecycle

`draft` → `experimental` → `approved` → `deprecated` → `retired`.

Experimental cards have a hypothesis, owner, test corpus, time/budget limit, and rollback path. Approved cards require benchmark evidence, review, known limitations, and migration guidance. Deprecated cards remain reproducible; retired cards remain traceable but cannot start new production runs.

## Compatibility and regression

Any change to prompt input fields, output fields, required evidence, tool authority, or evaluator interpretation triggers compatibility review. Maintain a frozen regression suite containing straightforward, ambiguous, adversarial, accessibility-sensitive, and domain-specific cases. Promotion requires no unreviewed regression on release-critical dimensions.
