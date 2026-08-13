# XS-2026-0002: Interactive notes candidate `linear-algebra-foundations-v4.html`

**Status:** Approved for Stage 1 governed generation
**Source concept model:** [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md)
**Learning plan:** [LP-2026-0002](../plans/lp-2026-0002-linear-algebra-foundations.md)
**Target learner and prerequisites:** AIML-4 Module 2 relearner; basic algebra and 2D coordinates; no assumed fluency in math terminology
**Artifact family:** Single-file interactive HTML notes (static, no build step, zero external runtime dependencies)
**Learning outcomes:** All eleven outcomes of LP-2026-0002; every computational concept is practiced through a faded worked-example ladder, and every unit check contains at least one constructed-response item.

## Learner problem and teaching strategy

The learner's diagnosed failure mode is recognition without understanding: formulas look familiar but cannot be explained, connected, or used. The three prior variants all presented and let the learner play, but none required retrieval, computation, prediction, or explanation. This candidate therefore invests its complexity budget in the assessment-and-scaffolding layer: prediction-gated reveals, faded worked-example ladders, misconception-targeted distractors, mixed-format retrieval checks, an interleaved mastery check with confidence calibration, and a local weak-topic review list. A visible banner states the artifact is a Stage 1 governed candidate, not a public release.

## Content and evidence map

Nine teaching units re-sequence the source's seven parts per LP-2026-0002; every factual statement traces to CM-2026-0001 atomic claims or is labeled Foundation/Supplemental.

| Unit | Source cells | Key interactives | Practice/assessment |
| --- | --- | --- | --- |
| 0 Start here | — | concept-map SVG, layer legend | loop instructions |
| 1 Quantities (scalar/vector/matrix) | 3–10 | vector builder (numbers → arrow) | check: classify + explain (free text) |
| 2 Compact math (Σ, transpose, f, wᵀx+b as weighted sum) | 12–19 (part) | summation expander, transpose flip, linear-model lab | Σ ladder; check: numeric Σ + 2 MCQ |
| 3 Combining vectors (ops, linear combination, span, basis, dimension) | 20–28 | prediction gate; linear-combination explorer with span lattice + parallel collapse | check: numeric combo + basis MCQ + explain |
| 4 Measuring (L2, L1 norms) | 32 | norm explorer (straight line vs city-block path) | norm ladder; check: numeric L2 + L1-vs-L2 MCQ |
| 5 Comparing (dot product, cos θ bridge, orthogonality, wᵀx reveal, linearity proof) | 29–34, 19 (moved, flagged) | prediction gate; dot/angle lab with arc, orthogonal-pair and opposite buttons | dot ladder; proof stepper; check: numeric dot + sign MCQ + explain (magnitude confound) |
| 6 Projection → decomposition → least squares | 35–45 | prediction gate; projection explorer (right-angle marker, live e·y = 0, x̂ + e = x); least-squares lab (residual area squares, live normal-equation trace, outlier toggle, autoscaled canvas) | projection ladder; check: numeric projection + why-squared MCQ |
| 7 Matrices as transformations (Ax, AB≠BA, I, ᵀ, symmetric, eigenvector extension) | 46–56, 63 (eigen row) | transformation lab with grid warp + 6 presets incl. collapse; AB-vs-BA computed live | debug-the-math (row/column error); check: numeric Ax + order MCQ |
| 8 Independence & rank (area test, multicollinearity, invertibility loop-closure) | 57–61, 45 (condition) | independence checker with parallelogram area | check: independence MCQ + rank MCQ + explain (duplicate features) |
| 9 ML connections + mastery | 62–63 | source connection table with "where you saw it" column; matching warm-up | 10-item interleaved mastery check with confidence tags; localStorage review list |
| Glossary | all | 32 entries rendered from one reusable JS data source; clickable terms throughout | — |

Constructed numeric examples are labeled "constructed example"; source examples keep "source" tags; the two opaque source figures (cells 38, 42) appear as transcribed, annotated formulas, never as redistributed images.

## Learning sequence

Linear scroll through units 0–9 with sticky nav; progress dots fill on *cleared checks*, not on scroll. Each unit follows Learn → Predict → Explore → Practice → Check → Connect (LP-2026-0002). The linearity proof is collapsed optional depth placed after the dot product (source ordering defect repaired).

## Interaction and feedback specification

- Native range/number/radio/select controls with labels; every change recomputes and redraws immediately and updates a text readout (dual channel).
- Prediction gates: the three explorer widgets stay hidden until the learner commits to a prediction; feedback references the commitment.
- Ladder hints never auto-open; tier 1 = strategy, tier 2 = first step.
- Check feedback states the governing rule for every miss; mastery adds confidence tags and flags confident misses as high-value.
- Widgets are guarded against degenerate states (zero vector in projection lab); canvases autoscale so no point can leave the visible area (v2 outlier defect repaired).
- No network calls, analytics, or remote storage; progress persists in localStorage with a visible reset control.

## Visual/representation rationale

- Vectors as arrows on a 2D grid; span as a lattice that collapses; norms as straight-line vs city-block paths; projection as solid shadow + dashed leftover + right-angle marker; least-squares errors as squares whose *area* is the squared error (V1's best idea, kept); transformations as warped grid + reference triangle; independence as parallelogram area.
- Math rendered as styled HTML (sub/superscripts, fraction and radical markup) — selectable, zoomable, screen-reader exposed as text; no image-based formulas; the radical uses a true vinculum (v3's fake overline repaired).
- Calm, single-accent design; layer badges and provenance tags carry the layer system; no gamification chrome.

## Assessment and misconception checks

Misconceptions targeted explicitly: basis ≠ unit/perpendicular; span collapse under parallel vectors (U3); sign wiping in norms (U4); magnitude confound of the dot product (U5); projection leftover orthogonality (U6); row-vs-column matrix product (U7 debug); "different vectors ≠ independent" and rank ≠ column count (U8). Mastery item 5 is a transfer scenario (embedding search) and item 9 is explanation, per LP-2026-0002 outcome 11.

## Accessibility and inclusion plan

- Landmarks, skip link, heading order, focus-visible, keyboard-operable native controls; no drag-only or hover-only interaction.
- Canvas: role="img" + aria-label + adjacent readout via aria-describedby; readouts are not aria-live (slider chatter repair); equivalent numbers always present as text.
- Color never sole encoder; prefers-reduced-motion; contrast targets WCAG AA; body text ≥ 16 px; usable at 320 px; print stylesheet with per-widget default-state notes.

## Performance/responsiveness intent

Single HTML file, zero external requests, system fonts, inline CSS/JS; canvases redraw only on input; devicePixelRatio-crisp rendering with aspect-preserving view windows. Verified 172,736 bytes.

## Acceptance criteria and evaluation dimensions

- Renders from file:// with no console errors and no network; all 12 widgets, 3 gates, 4 ladders, 8 checks, matching, and mastery check functional.
- All numeric examples machine-recomputed (44 recomputations) and all widget default readouts verified under a DOM/canvas stub.
- Evaluated against the ten default dimensions of the [evaluation framework](../../docs/06-evaluation/evaluation-framework.md) as a Stage 1 pilot; non-independent review caps disposition at private-pilot-complete with public-release eligibility ineligible regardless of scores.

## Retrospective note — current build identity (2026-08-13)

The Performance section's "Verified 172,736 bytes" records the pre-revision build (SHA-256 `22b4047e…f445d6`). The build evaluated at closure is 177,439 bytes, SHA-256 `c1430e9eed7686c123b6acf4bd995e67dc1b57f2ad9c2d2103e4d0623dd4c624` (EVAL-2026-0002, Revision 1). The specification's performance intent (single file, zero external requests, input-driven redraws) is unaffected. Append-only note; the specification body is unchanged.
