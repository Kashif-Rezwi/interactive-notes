# ADR-0005: Adopt class packages within multi-session modules

**Status:** Rejected  
**Date:** 2026-08-11  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** `content/` layout for all courses whose modules contain multiple taught sessions (classes)  
**Supersedes / superseded by:** none — the supersession claim over [ADR-0001](0001-content-package-layout.md) below was part of the proposal and never took effect (see Reversal note)


## Context and problem

ADR-0001 defined `content/<course>/<module>/{sources,generated}` assuming one taught unit per module. The owner's actual course (AIML-4) has **modules containing multiple classes**: Module 2 "Math & Statistics for ML" contains "Mathematical Foundations & Linear Algebra Fundamentals" (class 1, already packaged), "Probability Basics" (class 2, forthcoming), and more. The existing package `module-02-mathematical-foundations-linear-algebra/` was in reality a *class* package mislabeled as a *module*, which would force either overlong flat names (`module-02-probability-basics` pretending to be a module) or loss of the real module grouping — and the cross-class knowledge-graph and cumulative-review plans need a module level to live at.

## Decision

1. Content layout becomes three-level wherever a module has multiple classes:
   `content/<course-slug>/<module-slug>/<class-slug>/{README.md, sources/, generated/}`.
2. Module slug: `module-NN-<module-title>` using the course's official module number (e.g. `module-02-math-statistics-for-ml`). Class slug: `class-NN-<class-title>` using the course's class ordering (e.g. `class-02-probability-basics`).
3. A module README indexes its class packages and carries module-level information only; each class package remains the leaf package of the content-package convention (sources, generated, navigable README).
4. Single-class subjects may keep module-as-leaf layout; do not restructure them speculatively.
5. Record and artifact **identities are path-independent and do not change** (SRC/CM/LP/XS/CAN/RUN/EVAL/MEM IDs, note-slugs, generated filenames). Only *links* to moved paths are updated.
6. This ADR authorizes a one-time **mechanical link repair** in existing records that reference the old class-1 path (`module-02-mathematical-foundations-linear-algebra`): link targets change, evidence content does not. The repair commit, this ADR, and unchanged file hashes together preserve traceability. Records remain append-only for evidence content.

## Decision drivers

- The owner's stated course structure; repository-map rule that directories express responsibility; ADR-0001's purpose (discoverable, format-neutral, preserved material) is better served by reflecting the real course shape.
- The lesson standard's cross-lesson continuity (§11) needs a module level for cumulative maps/review.
- Artifact byte preservation: HTML artifacts contain no repo paths, so the move changes zero artifact bytes and zero recorded hashes.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Keep flat packages per class (`module-02-…`, `module-03-…` regardless of true module boundaries) | No move; no ADR | Misrepresents the course; module-level grouping and future cumulative features have no home; naming drifts from official numbering | Rejected |
| B. Three-level layout with mechanical link repair (chosen) | Faithful structure; scalable to module 3+; cheap, auditable repair (12 links in 8 files) | One-time link edits in records; convention doc update | Selected |
| C. Move files, leave old links broken or add stub redirects | Zero record edits | Broken or confusing provenance trails; violates the repository's link-integrity expectation | Rejected |
| D. Supersede every affected record with new records | Strictest append-only reading | Bureaucratic noise; obscures rather than preserves evidence | Rejected (mechanical link repair is authorized by this ADR instead) |

## Consequences

- Positive: structure matches the course; Probability Basics and future classes have a governed home; module-level knowledge-graph and cumulative-review features have a defined location; generated-artifact naming (`<note-slug>-v<N>`) is unaffected.
- Operational: any tooling or links assuming two-level depth must be checked (none exist at Stage 1 beyond the repaired links).
- Reversibility: fully reversible by reverting the move commit; no evidence content was altered.

## Evidence and validation

Post-move verification: repo-wide link check (zero broken references); SHA-256 of all preserved files (source notebook and four HTML candidates) re-verified unchanged; convention acceptance criteria re-checked. Recorded in the move commit.

## Rollback or migration plan

Revert the move commit; restore the two-level convention text; mark this ADR Superseded.

## Review trigger/date

Review when the first module-3 package is created (structure stress test) or by 2026-11-04.

## Reversal note (2026-08-11)

This draft was written and marked **Accepted** in an uncommitted working session on 2026-08-11 and was **rejected the same day, before ever being committed to a branch or activated**. The class-package split it authorizes existed only transiently in the working tree and was reversed; no commit on any branch contains the three-level layout.

**Rejection rationale:** the split added directory depth without new evidence value at Stage 1. A multi-session module is adequately represented by the existing leaf package: the module README remains the single navigation surface mapping each class to its files, class identity lives in `records/` and README rows, and files are disambiguated by `<note-slug>-v<N>` filenames. Cross-class knowledge-graph and cumulative-review needs (the draft's strongest driver) are record/library concerns, not directory concerns, and can be revisited when they materialize.

**Effect:** [ADR-0001](0001-content-package-layout.md) remains fully in force; the supersession claimed in this draft never took effect. AIML-4 Module 2 retains a single package whose `sources/` and `generated/` are shared by all classes. This rejection is recorded in the [content-package convention change history](../02-system/content-package-convention.md).

This file is preserved, per the repository's traceability principle, so the rejected alternative and its reasoning remain inspectable; its body above is the recovered draft unchanged except for the Status and Supersedes lines in the header.