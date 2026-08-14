# RUN-20260813-0001: Linear algebra foundations v5 — pipeline regeneration test

**Status:** Pilot complete<br>
**Date:** 2026-08-13<br>
**Owner:** Repository maintainer<br>
**Profile:** Stage 1 five-profile model (Coordinator/Creator/Reviewer/Steward/Owner; non-independent)<br>
**Purpose:** regenerate the Class 1 interactive note from scratch — source notebook + current governed workflow only — as a live test of the pipeline (no reuse of CM-2026-0001, LP-2026-0001/0002, XS-2026-0001/0002, or the v2–v4 artifacts).

## Inputs (pinned identities)

| Input | Identity | Note |
| --- | --- | --- |
| Source | SRC-2026-0001, SHA-256 `23c6f4eb…f94445` (63 markdown cells) | reused per P0 |
| Concept model | [CM-2026-0002](../concepts/cm-2026-0002-linear-algebra-foundations.md) | authored fresh this run |
| Learning plan | [LP-2026-0003](../plans/lp-2026-0003-linear-algebra-foundations.md) | authored fresh this run |
| Experience spec | [XS-2026-0003](../specifications/xs-2026-0003-linear-algebra-foundations-v5.md) | authored fresh this run |
| Prompt card | prm-generator-lesson-standard@0.3.0, SHA-256 digest `4b3bc46fabda` | first governed use of @0.3.0 (colophon contract) |
| Prior artifacts | v1–v4 | not read, not consulted |

## Generation events

- P0 intake: source authorization confirmed (SRC record exists); learner = AIML-4 student, basic algebra + 2-D plotting only; scope = all 63 cells; class ordinal 1; filename per `<note-slug>-v<N>` → `linear-algebra-foundations-v5.html`.
- P1–P3: CM/LP/XS authored from the source only; three source-order defects repaired and labeled (R1 independence-before-basis, R2 matrices-before-least-squares, R3 proof-after-dot-product).
- P4 generation: single HTML artifact, zero external requests, standard colophon + provenance header comment per @0.3.0.

**Iteration counts (ADR-0006):** generation iterations **1**; in-generation corrections **1** (Σ-superscript display for n=1, caught in self-verification, fixed, syntax re-verified); revision cycles **0**.

## Candidate

Candidate: [`linear-algebra-foundations-v5.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v5.html), SHA-256 `2191b088440d60717b4d88830698d60ac81f919a8e841d719fd93ccc177dfb1c`, 78,026 bytes, zero external runtime dependencies. Stable identity: CAN-2026-0004 (the filename version is display only).

## Verification evidence (P5 five audits)

1. **Coverage:** 63/63 cells dispositioned; matrix ships in [EVAL-2026-0003](../evaluations/eval-2026-0003-linear-algebra-foundations-v5.md) Appendix A. PASS.
2. **Mathematical:** 35/35 independent scripted recomputations PASS (every answer key, ladder rung, widget default, AB/BA products, projection identity, least-squares fit m=1.1/c=1.0/SSE=0.70); all widget results computed live; edge guards verified (zero-vector projection, parallel span, cos clamp). PASS.
3. **Dependency order:** read-in-order pass with an empty taught-so-far set; no use-before-explain after the three labeled repairs; transpose appears in Unit 1 notation as a forward-reference promise only. PASS.
4. **Pedagogical:** anatomy present in every unit; 2 prediction gates (span collapse, negative dot product) per P-01 limits; ladders for Σ/dot/norm; misconception distractors from CM-2026-0002; labels on every block. PASS.
5. **Technical & behavioral:** `node --check` PASS; zero external refs (the six `url(#ar)` are internal SVG markers); 134 ids unique; all anchors/aria/data-wiring/glossary refs resolve (scripted); 15/15 grade buttons wired; grading/tolerance/verdict/routing paths simulated PASS; contrast measured for 15 text/background pairs — worst 5.07:1, AA PASS; reduced-motion honored; colophon per standard (new checklist item) PASS; no-JS: gated content hidden by JS only, glossary static. PASS.

## Decision and approvers

**Final candidate identity at closure:** SHA-256 `2191b088440d60717b4d88830698d60ac81f919a8e841d719fd93ccc177dfb1c`, 78,026 bytes (single build; no revisions).
**Decision:** closed as `private-pilot-complete` — evaluation [EVAL-2026-0003](../evaluations/eval-2026-0003-linear-algebra-foundations-v5.md) passed all numeric gates diagnostically under non-independent review; public-release eligibility remains **ineligible** (ADR-0003).

## Reflection and memory disposition

The pipeline regenerated a complete, audit-passing lesson from source alone without consulting prior records or artifacts — the strongest Stage 1 evidence yet that the workflow is executable end-to-end. Memory disposition: no new MEM items (existing MEM-2026-0001/0002/0003 were applied, not extended); pattern catalog unchanged (P-01/02/03/04/10/11/12/13 re-applied as specified; no failures observed); checklist unchanged (the colophon item added 2026-08-13 was exercised). Recorded in records/README scoreboard: third completed pilot, third evaluated candidate — the calibration fallback (3 distinct candidates, 1 source package, limited evidence) is now satisfiable.

## Retrospective appendix (2026-08-14) — erratum and re-verification

- **Erratum (wording only):** verification evidence item 4 states "ladders for Σ/dot/norm"; the artifact ships one dot-product ladder plus a single norm rung (see the EVAL-2026-0003 retrospective appendix and [EVAL-2026-0005](../evaluations/eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md)). No audit outcome, score, or disposition changes.
- **Re-verification:** [EVAL-2026-0005](../evaluations/eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md) reproduced this ledger's mechanical claims exactly (SHA-256, 134 unique ids, 15/15 grade-button wiring, 5.07:1 worst measured contrast, syntax PASS, zero external refs).
