# ADR-0004: Adopt the v4-derived lesson standard and generation workflow

**Status:** Accepted  
**Date:** 2026-08-10  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** All future governed generation of interactive lesson artifacts from source notes  
**Supersedes / superseded by:** none

## Context and problem

Four generations of the AIML-4 Module 2 interactive notes (historical v1, CAN-2026-0001, CAN-2026-0002, CAN-2026-0003) demonstrated that the repository's generic governance machinery (quality loop, records, rubric) successfully controls *process*, but does not by itself control *learning quality*: v2 and v3 were generated under identical pinned inputs yet both shipped recognition-only assessment, and v1–v3 all propagated source defects a learner would trip on. The redesign that became v4 introduced a set of pedagogical decisions (dependency-rule sequencing, prediction gates, faded worked examples, constructed-response assessment, layered provenance labels, adversarial post-generation audit) that lived only inside the artifact and its run records. Without codification, the next lesson could silently regress.

## Decision

Adopt the v4-derived standard as the default for all governed lesson generation:

1. `docs/01-product/lesson-standard.md` — the Lesson Consistency Contract (required/recommended/conditional/forbidden), canonical lesson anatomy, content-generation rules (explain-before-use, coverage requirement), interaction philosophy, assessment philosophy, progression model, ML-connection framework, additional-knowledge policy, and the visual design system.
2. `docs/03-workflows/lesson-generation-workflow.md` — the phased generation workflow with five mandatory audits, mapped to existing record types (SRC/CM/LP/XS/RUN/EVAL/MEM).
3. `library/patterns/lesson-patterns.md` — the reusable pattern catalog (implementation patterns, kept separate from the permanent principles).
4. `library/prompts/prm-generator-lesson-standard@0.1.0.md` — the generation prompt card, registered in **Draft** status pending the prompt-promotion process; `library/prompts/README.md` is amended to permit Draft registration during Stage 1 (previously Approved-only), mirroring the Experimental-status pattern already used by `docs/03-workflows/quality-loop.md`.
5. `library/rubrics/lesson-qa-checklist.md` — a verification checklist (not a scoring rubric; the evaluation framework remains the sole gate authority).
6. `records/memory/mem-2026-0003` — promotion of the two audit gates discovered during the v4 adversarial audit into standing practice.

## Decision drivers

- Learning quality over feature novelty (principle 1); evaluate before retrying (principle 4); compose narrow roles and documents (principle 6); prefer explicit contracts to tacit coordination (principle 7); earn complexity (principle 12).
- Evidence: comparative audits of v1–v3; EVAL-2026-0001; EVAL-2026-0002 incl. Revision 1 (0 blockers, 3 majors, 11 minors — all repaired); RUN-20260804-0001/0002 and RUN-20260810-0001 reflections; MEM-2026-0001/0002.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Keep generic docs only; each lesson re-derives pedagogy | Zero new documents | Demonstrated regression risk (v2/v3 assessment failure); prompt snapshots instead of cards | Rejected |
| B. Encode the standard as build-time code/schemas now | Enforcement is mechanical | Premature implementation (charter non-goal; Stage 2+ scope); freezes patterns before lesson 2 exists | Rejected for now; revisit at Stage 2 |
| C. Codify as documents + prompt card + checklist (chosen) | Reviewable, linkable, revisable; matches repository's documentation-first phase | Requires discipline to keep standard and artifacts in sync | Selected |

## Consequences

- Positive: future lessons inherit a tested quality bar; generation prompts are versioned assets; audits are repeatable; the pattern library compounds.
- Negative/operational: every lesson generation must budget for the five audits; the standard must be revised through review when evidence contradicts it.
- Educational: the standard encodes an evidence-based pedagogy (retrieval practice, prediction, fading) — if learner-pilot evidence later contradicts a rule, the rule changes, not the evidence.
- Reversibility: fully reversible — supersede this ADR and deprecate the documents; v1–v4 artifacts and records are unaffected.

## Evidence and validation

The standard's rules cite their evidence inline (variant audits, EVAL records, memory items, learning-science references gathered in RUN-20260810-0001). Validation so far is artifact-level, not learner-level: no efficacy claim is made. First real validation event: generation of the second module's lesson under this standard, then comparing its audit results to v4's.

## Rollback or migration plan

Supersede this ADR with a new decision; mark the three documents Deprecated; retained records remain valid evidence of the approach tried.

## Review evidence

Recorded retrospectively on 2026-08-13 per the review policy's status-accuracy rule: this ADR was reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-10 under a solo-maintainer self-review — the practice later codified as the Stage 1 solo-maintainer path. Scope inspected: the lesson standard, the lesson-generation workflow, the pattern catalog, the prompt card, the QA checklist, and MEM-2026-0003. Evidence considered: EVAL-2026-0001 and EVAL-2026-0002 (including Revision 1), the RUN-20260804-0001/0002 and RUN-20260810-0001 reflections, the comparative audits of v1–v3, and MEM-2026-0001/0002. Decision: accept. Limitation: non-independent self-review — the same operator authored the v4 artifact and records being codified, and no second reviewer exists at Stage 1.

## Review trigger/date

Review after the next two governed lesson generations or by 2026-11-04, whichever comes first; also review immediately if a learner pilot contradicts a codified rule.
