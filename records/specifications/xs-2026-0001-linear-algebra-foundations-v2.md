# XS-2026-0001: Interactive notes candidate `linear-algebra-foundations-v2.html`

**Status:** Approved for Stage 1 private-pilot generation<br>
**Source concept model:** [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md)<br>
**Learning plan:** [LP-2026-0001](../plans/lp-2026-0001-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 Module 2 learner; basic algebra and 2D coordinates; no prior linear algebra<br>
**Artifact family:** Single-file interactive HTML notes (static, no build step, no external runtime dependencies)<br>
**Learning outcomes:** All nine outcomes of LP-2026-0001; artifact-specific addition: the learner manipulates each core object (vector, projection, transformation) at least once before its self-check.

## Learner problem and teaching strategy

The learner can read formulas but cannot yet *see* them. The artifact turns each source definition into a small manipulable model, following LP-2026-0001's worked-example → guided-practice → check loop. A visible banner states the artifact is a Stage 1 private-pilot candidate, not a public release, so no learner or reviewer can mistake its status.

## Content and evidence map

Seven sections mirror the source's parts; every factual statement traces to CM-2026-0001 atomic claims (cell anchors to SRC-2026-0001).

| Section | Source cells | Claims used | Interactive |
| --- | --- | --- | --- |
| 1. Foundations and notation | 3–19 | 1–8 | Summation expander (choose n and vector values; see expanded sum and total); step-through proof of dot-product linearity |
| 2. Vector spaces and geometry | 20–28 | 9–13 | Linear-combination explorer: two 2D vectors with scalar sliders; canvas shows the resultant; parallel-vs-non-parallel toggle demonstrates span |
| 3. Core operations | 29–34 | 14–16 | Dot-product and norm calculator: editable 2D vectors; shows Σxᵢyᵢ, ‖x‖₁, ‖x‖₂, cos θ, angle, and the sign interpretation |
| 4. Projections and least squares | 35–45 | 17–19 | Projection explorer (proj_y(x) drawn with x̂ and e) and a least-squares demo fitting a line to five fixed points via the normal equation, with residuals drawn |
| 5. Matrices and transformations | 46–56 | 20–24 | 2×2 matrix-vector transformer on a grid with a reference shape; presets for identity, rotation, scaling, and a symmetric matrix; AB ≠ BA toggle compares orders |
| 6. Rank and independence | 57–61 | 25–26 | Independence checker for two/three 2D vectors (determinant test) with rank readout and multicollinearity note |
| 7. ML connections and interview | 62–63 | 27 | Source's connection table rendered accessibly; three interview prompts with hidden-then-revealed answers |

Constructed numeric examples (summation values, least-squares points, transformation presets) are labeled "constructed example" in the UI; they are teaching aids, not source quotations.

## Learning sequence

Linear scroll through sections 1–7 in plan order, with a sticky section nav and a progress indicator. Each section: definition card → worked/constructed example → interactive → self-check. The interview proof in section 1 and the interview prompts in section 7 are collapsed by default (optional depth).

## Interaction and feedback specification

- All inputs are native range/number/radio controls with labels; every change recomputes and redraws immediately and updates the text readout (dual channel: visual + numeric).
- Self-checks are radio groups with a "Check" button; feedback states correct/incorrect plus the governing rule in text; no attempt limits, no scoring persistence.
- Canvas states: initial (default vectors), interacting (live update), and reset (button restores defaults). No error states are reachable; inputs are clamped to sane ranges.
- No network calls, analytics, or storage; the page works fully offline after load.

## Visual/representation rationale

- Vectors as arrows on a 2D grid (standard geometric convention); projection shown as a solid arrow for x̂ and a dashed segment for e, matching the source's decomposition x = x̂ + e.
- Transformations shown on a unit grid with a reference triangle so distortion, rotation, and reflection are visible.
- Single accent hue per section with neutral grays; sign of dot product encoded by label and icon, never color alone.
- Math rendered in styled HTML (sub/superscripts, fraction and radical markup) so it is selectable, zoomable, and screen-reader exposed as text; no image-based formulas.

## Assessment and misconception checks

Self-checks target the plan's outcomes and the concept model's misconception list: dot-product sign vs. orthogonality (outcome 3), commutativity of matrix multiplication (outcome 8), exact-vs-approximate solution for Ax = b (outcome 7), and redundancy vs. basis (outcome 5). Feedback quotes the governing rule rather than only marking right/wrong.

## Accessibility and inclusion plan

- Landmarks (`header`, `nav`, `main`, `section`, `footer`), skip-to-content link, logical heading order, focus-visible styles.
- Every canvas has `role="img"`, an aria label, and an adjacent live text summary (`aria-live="polite"`) carrying the same numbers the canvas shows.
- Sliders have text labels and value readouts; all functionality is keyboard reachable; no hover-only or drag-only interactions.
- Honors `prefers-reduced-motion` (transitions disabled); contrast targets WCAG AA for text; minimum body text 16 px; content reflows at 320 px width.

## Performance/responsiveness intent

Single HTML file, zero external requests, system font stack, inline CSS/JS under ~100 KB target; canvases redraw only on input; layout is fluid with a max-width reading column. Usable offline, on mobile, and in print (print stylesheet collapses interactives to their text summaries).

## Acceptance criteria and evaluation dimensions

- Renders without console errors from `file://` with no network; all seven sections, seven interactives, and all self-checks functional.
- Every section's factual content traces to CM-2026-0001 claims; constructed examples are labeled.
- Evaluated against the ten default dimensions and provisional gates of the [evaluation framework](../../docs/06-evaluation/evaluation-framework.md) as a Stage 1 private pilot; a non-independent review caps disposition at `private-pilot-complete` and sets public-release eligibility to `ineligible` regardless of scores.
