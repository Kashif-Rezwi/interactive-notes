# XS-2026-0003: Interactive notes v5 — linear algebra foundations (regeneration test)

**Status:** Approved<br>
**Supersedes / iteration position:** Iteration 1 — original (fresh from LP-2026-0003; approval scope: Stage 1 governed generation)<br>
**Source concept model:** [CM-2026-0002](../concepts/cm-2026-0002-linear-algebra-foundations.md)<br>
**Learning plan:** [LP-2026-0003](../plans/lp-2026-0003-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** per LP<br>
**Artifact family:** single-file interactive HTML lesson (zero external requests, file://-capable)

**Learning outcomes:** per LP-2026-0003 (10 outcomes, each exercised).

## Learner problem and teaching strategy

A beginner meets dense notation with no causal model. Strategy per LP: intuition-first Learn, committed Predict on the two counterintuitive reveals, goal-directed Explore, faded Practice ladders, retrieval Checks, mechanism-level Connect.

## Content and evidence map

U0 orientation+concept map · U1 cells 3–17 · U2 cells 20–28 + 57–59 (R1) · U3 cells 29–34 + 18–19 (R3) · U4 cells 46–56 (R2) · U5 cells 35–45 (incl. transcribed opaque figures 38/42) · U6 cells 60–61 · U7 cells 62–63 · U8 mastery/review · glossary. Layered labels + provenance tags on every block per standard §1.1.

## Learning sequence

Per LP. Sticky unit nav with completion dots (cleared checks, never scroll). Concept map revisited at U7 close.

## Interaction and feedback specification

- U1: Σ-expander (n slider 1–4, live expansion+total); data-matrix explorer (rows×cols sliders, live grid + samples/features reading).
- U2: span explorer (sliders set u, v, scalars a,b; live resultant a·u+b·v on canvas; **prediction gate: span when v ∥ u**); independence verdict live (ratio test, no determinant term).
- U3: dot-product explorer (two vectors; live x·y, ‖x‖, ‖y‖, θ, cosθ; **prediction gate: negative dot product**); norm comparator (L1 vs L2 readouts); orthogonality indicator.
- U4: transformation playground (preset 2×2 matrices: rotation 90°, scale, shear-x, reflect; applied to a triangle on canvas, live coordinates); AB-vs-BA comparator (A=[[1,2],[0,1]], B=[[1,0],[3,1]], both products computed live); transpose builder (2×3 → 3×2 grid live).
- U5: projection explorer (live proj_b(a), residual, right-angle marker, residual·b=0 verification readout); least-squares fitter (4 fixed points (1,2),(2,3),(3,5),(4,5); slope/intercept via live 2×2 normal-equation solve; residuals + SSE readouts).
- U6: rank inspector (preset matrices: full-rank [[2,1],[1,1]] vs rank-1 [[2,4],[1,2]]; column-multiple test live; redundancy verdict).
- All canvases: adjacent text equivalents via aria-describedby carrying the same numbers.

## Visual/representation rationale

Standard §10 token set: ink/paper neutrals + one accent + semantic good/bad/warn; system fonts, mono readouts; badge system; widget cards with EXPLORE tag + goal strip; dashed predict blocks; 16px minimum body; nothing animated without learner action.

## Assessment and misconception checks

Per LP assessment plan. Distractors from CM misconception list (AB=BA, parallel-span, zero-dot-means-zero-vector, rank=column count, exact-solution belief).

## Accessibility and inclusion plan

Per LP + standard §1.1; colophon per standard (brand + AI-honesty lines); header comment carries provenance identity.

## Performance/responsiveness intent

Single file, inline CSS/JS, canvases redraw on input only, readable at 320px, works from file://, localStorage with in-memory fallback + reset.

## Acceptance criteria and evaluation dimensions

Passes the five audits (QA checklist incl. the colophon item) with no Critical/Major open; evaluation per the framework's 10 dimensions; closes `private-pilot-complete` at best under non-independent review (ADR-0003).
