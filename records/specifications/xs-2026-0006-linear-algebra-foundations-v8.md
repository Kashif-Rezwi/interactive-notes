# XS-2026-0006: Interactive notes candidate `linear-algebra-foundations-v8.html` (CAN-2026-0007)

**Status:** Approved<br>
**Approval scope:** Stage 1 governed generation (declared here per ADR-0007, not in the status value)<br>
**Supersedes / iteration position:** Iteration 3 — supersedes [XS-2026-0005](../specifications/xs-2026-0005-linear-algebra-foundations-v7.md) (same unchanged source and validated interaction contract; this iteration adds the ADR-0013 per-widget viewport declarations and the lesson-standard §10 design-system conformance contract, and ports the artifact's engineering base from CAN-2026-0006's collapsed canvas architecture to the benchmark makeView architecture of [BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md), per the [EVAL-2026-0007](../evaluations/eval-2026-0007-linear-algebra-foundations-v4-v7-qa-design-audit.md) remediation plan: P0 canvas engine, P1 navigation shell, P2 visual/UX polish — while preserving every v7 pedagogical innovation per its action item P2.4)<br>
**Source concept model:** [CM-2026-0005](../concepts/cm-2026-0005-linear-algebra-foundations.md)<br>
**Learning plan:** [LP-2026-0006](../plans/lp-2026-0006-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 student; basic algebra + 2-D plotting; no prior linear algebra<br>
**Artifact family:** Single-file interactive HTML notes; zero external runtime dependencies; file://-functional<br>
**Learning outcomes:** All twelve outcomes of LP-2026-0006; every computational skill has its own faded ladder; every unit check contains ≥1 constructed-response item.

## Learner problem and teaching strategy

The learner meets linear algebra as notation soup: formulas recognized, nothing explainable. The candidate invests its complexity budget in depth that carries learning — per-unit ledes and worked numeric examples before any widget, signature manipulable visuals, prediction gates with real consequences, one full faded ladder per computational skill, misconception-named callouts and distractors, an interleaved mastery check with confidence calibration, and a local review list. This build is a **remediation run**: its success bar is (a) the reference-depth pedagogy of CAN-2026-0006 reproduced intact, and (b) the canvas engineering standard (ADR-0013) and design-system contracts (lesson standard §10) that CAN-2026-0006 violated — the regression class of [MEM-2026-0005](../memory/mem-2026-0005-canvas-responsiveness-and-design-drift.md), whose remedy this run field-tests for the first time.

## Content and evidence map

Ten teaching units re-sequence the source's seven parts per LP-2026-0006 (repairs R1–R3 labeled in-artifact). Every factual statement traces to CM-2026-0005 claims or is labeled FOUNDATION/DEEP DIVE/EXTENSION/constructed. The unit table (unit → source cells → lede → signature visual → arc → callouts → check mix) is identical to XS-2026-0005's, restated here by reference: U0 orientation with branched SVG concept map; U1 quantities (cells 3–10, M1/M2); U2 compact math (11–17, M3, opens wᵀx arc); U3 combining vectors (20–24, M4/M5, gate G1); U4 independence/basis/dimension (57–59 R1 + 25–28, M6/M7); U5 measuring (31–32, M8); U6 comparing (29–34 + 18–19 R3, M9/M10, gate G2, wᵀx payoff); U7 matrices move space (46–56 R2, M11); U8 projections & least squares (35–45, M12/M13, gate G3, closes linear-model arc); U9 rank (60–61, M14/M15, closes (AᵀA)⁻¹ loop); U10 synthesis + matching warm-up + 11-item mastery + review list; glossary (40 terms, 6 fields each).

## Learning sequence

U0 → U1 … U10 → glossary → review/next-steps → colophon. Sticky unit nav with completion dots driven by cleared checks (never scroll) and an IntersectionObserver-driven aria-current active state. Locked sequence is the LP's; no unit may be skipped by the artifact.

## Interaction and feedback specification (conformance contract)

Every widget below ships; every Explore-badged widget has ≥1 learner-manipulable variable; canvases pair with a live numeric text equivalent; inputs are bounded (sliders/min-max) or the canvas autoscales per the declared rule, so nothing renders off-canvas; multi-entity canvases carry a `.legend-inline` color legend. All values are computed live in the page's script — nothing hard-coded that can be computed.

**Canvas engineering contract (ADR-0013, binding on every canvas):** the canonical responsive `makeView(canvasId, xMin, xMax, yMin, yMax)` pattern — `clientWidth` re-measured at every draw, DPR-scaled backing store, CSS height computed from the mathematical aspect ratio, all coordinates through the normalized `X(x)`/`Y(y)` transforms, one `window.addEventListener("resize", draw)` per canvas widget (9 canvases → 9 listeners), no reading of HTML width/height attributes for layout, no hardcoded pixel-offset transforms, signed angular difference with wrapping for angle arcs. Canvas CSS baseline `canvas.viz{width:100%;height:auto;…}` on every canvas.

| # | Widget (unit) | Manipulable variables | Stated goal | Degenerate guard | Bounds / scaling | Viewport (`xMin, xMax, yMin, yMax`) |
| --- | --- | --- | --- | --- | --- | --- |
| W1 | Matrix-shape explorer (U1, canvas) | rows m, cols n (sliders) | "Build a matrix for 4 samples × 2 features" | min 1 each | m 1–6, n 1–4 | grid-units: (−2.6, 9.4, −1.3, 9.7); cell 2.2×1.5 units, row 0 at top |
| W2 | Σ-expander (U2, text) | n (slider); term rule (i / 2i / i²) | "Make the sum exceed 50" | n ≥ 1 | n 1–8 | no canvas |
| W3 | Weighted-sum lab (U2, text) | w₁, w₂, x₁, x₂, b (sliders) | "Reach f(x) = 10" | none needed | ±10 each | no canvas |
| W4 | Span lattice (U3, canvas, **gated G1**) | v₁, v₂ direction (angle sliders) | "Collapse the lattice to a line, then restore the plane" | parallel snap within ~5° reported as collapse | fixed lengths 2.5/2; angles 0–350° step 10 | (−9.5, 9.5, −9.5, 9.5) — lattice extremes 2·2.5+2·2 = 9 ≤ 9.5 |
| W5 | Zero-hunt tester (U4, canvas) | scalars a, b (sliders); pair preset toggle | "Hit (0,0) without setting both sliders to 0" | both-zero state named trivial | a,b ∈ [−2,2] step 0.5 | autoscale square (−R, R, −R, R), R = 2.1·max_c(|v1_c|+|v2_c|) per pair (ind 6.3 / dep 12.6) — declared autoscale rule; extremes bounded by slider bounds |
| W6 | Norm comparator (U5, canvas) | endpoint (x, y) sliders | "Find a point where L1 is nearly double L2" | zero vector noted | x,y ∈ [−6,6] step 0.5 | (−6.8, 6.8, −6.8, 6.8) |
| W7 | Dot/angle lab (U6, canvas, **gated G2**) | v, w components (number inputs); double-v button | "Make them orthogonal; then make the dot product negative" | zero-length input guarded with teaching note | components ∈ [−5,5] step 0.5 | (−5.8, 5.8, −5.8, 5.8); angle arc uses signed angular difference with wrapping (ADR-0013 §5) |
| W8 | Transformation playground (U7, canvas) | four 2×2 entries (sliders); 6 presets incl. collapse | "Turn the square into a flat line" | singular preset labeled | entries ∈ [−2,2] step 0.5 | autoscale square (−R, R, −R, R), R = 1.05·max(2.6, 2·max(column abs-sums)) ≤ 8.4 — declared autoscale rule |
| W9 | AB-vs-BA comparator (U7, text) | entries of A and B (number inputs) | "Find a pair where AB and BA share no entry" | none needed | entries ∈ {0,1,2,3} | no canvas |
| W10 | Transpose builder (U7, canvas) | entries of a 2×3 A (number inputs); click a cell to pair | "Predict which cell pairs swap" | — | entries ∈ [−9,9] | layout-units: (0, 64, 0, 26); cell 5.4 units; click points converted back through the viewport transform |
| W11 | Projection explorer (U8, canvas, **gated G3**) | x and y components (number inputs) | "Make the leftover vanish; then make it as long as possible" | y ≈ 0 blocked with teaching note | components ∈ [−5,5] step 0.5 | (−7.5, 7.5, −7.5, 7.5); target line extended to ±7.5 within viewport |
| W12 | Least-squares lab (U8, canvas) | y₁…y₄ of four points (sliders, x fixed 1–4); outlier preset | "Drive SSE under 0.5; then place an outlier and watch the line chase it" | vertical fit impossible (x distinct by construction) | y ∈ [0,8] step 0.5; fit-line drawing clamped to y ∈ [0,9] | (−0.7, 5.7, −1.0, 9.6) — asymmetric positive-quadrant viewport; all coordinates through X/Y transforms; residual squares are screen-space squares with an edge-direction guard |
| W13 | Rank inspector (U9, text) | six entries of a 3×2 matrix (number inputs) | "Force rank 1 without zeroing a column" | zero column called out | entries ∈ [−4,4] step 1 | no canvas |

Static-demo decisions: none — all 13 widgets are manipulable.

**Prediction gates (P-01, three):** G1 (U3, span of a parallel pair: plane / line / point), G2 (U6, sign of the dot product when θ > 90°: positive / zero / negative), G3 (U8, the leftover's direction: along y / perpendicular to y / opposite x). The manipulable (W4/W7/W11) is hidden by JS until commitment; feedback differentiates per chosen option and quotes the commitment. No-JS readers see the content (hidden by JS only).

**Faded ladders (P-02, four — one per skill):** L1 Σ-expansion (U2; worked Σ[5,3,8,1]=17 → completion Σᵢ₌₁⁴ 2i → independent Σᵢ₌₁³ (i+1)); L2 norms (U5; worked ‖[3,4]‖₂=5, ‖[3,4]‖₁=7 → completion ‖[6,8]‖ → independent ‖[−1,2,2]‖); L3 dot product (U6; worked [1,2]·[3,4]=11 → completion [2,−1]·[4,3] → independent [1,0,−2]·[3,5,1]); L4 projection (U8; worked proj of [2,2] onto [4,0] → completion [3,4] onto [1,0] → independent [2,3] onto [1,1]). Hints tiered (strategy → first step), never auto-open; rung 3 never copies rung 1's numbers.

**Self-verifying readouts:** W11 recomputes e·y = 0 and x̂ + e = x live; W12 recomputes SSE and shows m, c from the normal equation; W8 shows where e₁, e₂ land (columns of A).

**Design-system conformance contract (lesson standard §10):** the §10.1 pinned `:root` token set verbatim (21 custom properties); body at font-size ≥ 16px, line-height ≥ 1.6, `-webkit-font-smoothing: antialiased`, warm `--paper` (#f7f6f2); sticky nav = frosted glass (`background: rgba(247,246,242,.94); backdrop-filter: blur(6px)`), single-line horizontal scroll (`overflow-x: auto; scrollbar-width: thin`, never `flex-wrap: wrap`), pill links, `.topnav a[aria-current="true"]` active styling driven by IntersectionObserver, completion dots; left-aligned header with `.kicker`, `h1`, `.sub`, and a `.head-meta` row of `.chip` chips (duration, unit count, offline, local progress); every slider/input labeled with its mathematical purpose (subscript notation, e.g. `a₁ (scale v₁)`) and every control carrying an accessible name; `.legend-inline` swatches on all 9 canvases (W1, W4, W5, W6, W7, W8, W10, W11, W12 — W1 included for its samples/features color split; all nine render more than one visual entity). **Documented deliberate variation (MEM-2026-0005 allowance):** the U0 concept-map SVG retains CAN-2026-0006's categorical node palette — a categorical coding the pinned token set does not cover, not design drift.

**Glossary term set (from CM-2026-0005; every entry six fields — simple / precise / intuition / example / related / where-it-appears):** scalar, vector, matrix, feature, sample, function, linear model, weights, bias, summation (Σ), index, transpose, norm, ℝⁿ, vector space, linear combination, span, basis, dimension, linear independence, dependent vectors, zero vector, dot product, orthogonality, L2 norm, L1 norm, cosine similarity, projection, residual, orthogonal decomposition, least squares, normal equation, matrix multiplication, identity matrix, symmetric matrix, rank, full rank, multicollinearity, embedding, PCA (40 terms). In-lesson dotted terms link to entries via a focus-managed popover without losing place.

**Concept map (branched dependency graph, not a sequence strip):** nodes {quantities: scalar/vector/matrix; Σ-notation; linear model (weighted sum); add & scale; linear combination; span; independence; basis; dimension; norms; dot product; orthogonality; projection; least squares; matrices as transformations; matrix multiplication; transpose; normal equation; rank; wᵀx reveal}; edges are needed-to-understand arrows incl. branches: {vectors→norms→dot product→projection→least squares}; {add & scale→linear combination→span→independence→basis→dimension}; {independence→rank}; {matrices→multiplication→transpose→normal equation→least squares}; {dot product→wᵀx reveal→linear model}; {rank→(AᵀA)⁻¹ note}. Rendered as SVG in U0 and revisited, fully readable, in U10.

## Visual/representation rationale

Token set per the standard's §10.1 pinned visual design system (ink/paper/line neutrals, one accent, semantic good/bad/warn, badge colors core/foundation/deep/ml/ext); badge system CLASS CORE/FOUNDATION/DEEP DIVE/ML LINK/EXTENSION + provenance tags (source/constructed/supplemental); callouts info/warn/good/ml/misconception; widget cards with EXPLORE tag and goal strip; check blocks with CHECK/MASTERY tags; predict blocks dashed; ladder rungs; print-note pattern; `.legend-inline` canvas legends. Vectors as arrows; span as a collapsing lattice; norms as city-block vs straight line; projection as shadow + dashed leftover + right-angle marker; squared error as shaded squares; matrices as warped grids; rank as a greying dependent column. Math as styled selectable HTML (true radical vinculum); no image formulas; no autoplay; motion only on learner action, disabled under reduced-motion.

## Assessment and misconception checks

Per LP-2026-0006: 9 unit checks each with ≥1 CR item and governing-rule feedback; distractors encode M1–M15; each unit's misconception alert is a visible callout. Mastery = 11 interleaved items with fresh numbers (Σᵢ₌₁⁴ i²; [4,−2]·[1,3]; ‖[2,−3,6]‖₂; proj [5,2] onto [3,0]; parallel-span reasoning; AB≠BA pipeline reasoning; duplicate-feature transfer; planted signed-L1 error-identification; orthogonal MCQ; rank MCQ; explain Aᵀ item), three-level confidence tags, confident-miss routing to the localStorage review list with a next-day return invitation.

## Accessibility and inclusion plan

Standard §1.1 baseline exactly as LP-2026-0006 declares: landmarks, skip link, heading order, focus-visible, native keyboard-operable controls; canvas role="img" + aria-label + adjacent readout via aria-describedby (readouts not aria-live — slider-chatter repair); every input control carries an accessible name (aria-label or associated label — repairs v7's unlabeled number inputs); color never sole encoder (labels/dashes/text); reduced-motion honored; measured AA contrast ≥ 4.5:1 for body text; print stylesheet with per-widget default-state notes; readable at 320 px; storage-unavailable fallback with visible reset.

## Performance/responsiveness intent

Single HTML file, zero external requests, system font stack, inline CSS/JS; canvases redraw only on input and on window resize (ADR-0013 contract); target richness band ≈ reference implementation (CAN-2026-0003, 178,020 bytes) — depth, not bloat, governed by standard §7.

## Acceptance criteria and evaluation dimensions

- Renders from file:// with no console errors and no network; all 13 widgets, 3 gates, 4 ladders, 9 unit checks, matching, and the 11-item mastery check functional (handler-level simulation).
- Every number machine-recomputed (worked examples, ladder rungs, widget defaults, mastery keys); all widget results live-computed.
- XS-conformance: this contract verified element-for-element at P5 (every widget variable, gate behavior, ladder rung, glossary field, concept-map edge, every canvas viewport against its declared `xMin/xMax/yMin/yMax`, resize-listener count ≥ canvas count, legend presence, token count ≥ 20, nav/header/label contracts); LP reveal arcs pay off where named.
- Evaluated against the ten framework dimensions as a Stage 1 pilot; non-independent review caps disposition at private-pilot-complete, public-release eligibility ineligible (ADR-0003). Remediation judgment is against EVAL-2026-0007's P0/P1/P2 action checklist plus the 2026-08-13 QA-checklist depth items and the standard rubric.

## Conformance checklist (depth-calibration contract)

- [x] Every widget declares learner-manipulable variable(s) or explicit "static demo" justification (13 manipulable, 0 static)
- [x] Every canvas widget declares input bounding (sliders, min/max) or autoscaling parameters
- [x] **Every canvas widget declares its mathematical viewport (`xMin`, `xMax`, `yMin`, `yMax`) for the P5 `makeView` conformance sweep (ADR-0013 §2)** — W1, W4, W6, W7, W11, W12 fixed; W5, W8 declared autoscale rules with bounded maxima; W10 layout-units
- [x] Exhaustive glossary term set listed from the CM (40 terms, 6 fields each)
- [x] Concept map declares explicit dependency nodes and directed edges (multi-branch graph)
- [x] Every LP-planned ladder, prediction gate, and reveal arc has a specified element
- [x] Canvas text equivalents specified for every visual component
