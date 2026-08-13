# XS-2026-0004: Interactive notes candidate `linear-algebra-foundations-v6.html` (CAN-2026-0005)

**Status:** Approved<br>
**Approval scope:** Stage 1 governed generation (declared here per ADR-0007, not in the status value)<br>
**Supersedes / iteration position:** Iteration 1 — original<br>
**Source concept model:** [CM-2026-0003](../concepts/cm-2026-0003-linear-algebra-foundations.md)<br>
**Learning plan:** [LP-2026-0004](../plans/lp-2026-0004-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 student; basic algebra + 2-D plotting; no prior linear algebra
**Artifact family:** Single-file interactive HTML notes; zero external runtime dependencies; file://-functional
**Learning outcomes:** All twelve outcomes of LP-2026-0004; every computational skill has its own faded ladder; every unit check contains ≥1 constructed-response item.

## Learner problem and teaching strategy

The learner meets linear algebra as notation soup: formulas recognized, nothing explainable. The candidate invests its complexity budget in depth that carries learning — per-unit ledes and worked numeric examples before any widget, signature manipulable visuals, prediction gates with real consequences, one full faded ladder per computational skill, misconception-named callouts and distractors, an interleaved mastery check with confidence calibration, and a local review list. This build is the prompt-card @0.4.0 comparison run: its success bar is the reference implementation's depth (CAN-2026-0003), not rule-floor compliance (the CAN-2026-0004 failure class, MEM-2026-0004).

## Content and evidence map

Ten teaching units re-sequence the source's seven parts per LP-2026-0004 (repairs R1–R3 labeled in-artifact). Every factual statement traces to CM-2026-0003 claims or is labeled FOUNDATION/DEEP DIVE/EXTENSION/constructed.

| Unit | Source cells | Lede | Signature visual | Arc | Callouts | Check (mix; CR = constructed response) |
| --- | --- | --- | --- | --- | --- | --- |
| U0 Start here | — | How these notes teach you | Concept-map SVG (branched dependency graph) | shows all arcs | — | — |
| U1 Quantities | 3–10 | Every dataset is three shapes of numbers | Matrix-shape explorer | — | M1, M2 | classify MCQ + numeric features-count CR + explain CR (order) |
| U2 Compact math | 11–17 | Compression for long sums | Σ-expander | opens wᵀx arc (payoff U6) | M3 | Σ numeric CR + weighted-sum MCQ + Σ-meaning MCQ |
| U3 Combining vectors | 20–24 | Paint a plane — or just a line | Span lattice | — | M4, M5 | combination numeric CR + span MCQ |
| U4 Independence, basis, dimension | 57–59 (R1), 25–28 | A basis is a team with no redundant member | Zero-hunt tester | — | M6, M7 | independence MCQ + dimension numeric CR + basis MCQ |
| U5 Measuring | 31–32 | Two honest answers to "how long?" | L1 path vs L2 line | — | M8 | L2 numeric CR + L1 numeric CR + use-case MCQ |
| U6 Comparing | 29–34, 18–19 (R3) | One number for agreement | Dot/angle lab | **wᵀx payoff** | M9 (+cosine callout), M10 | dot numeric CR + sign MCQ + explain CR (confound) |
| U7 Matrices move space | 46–56 (R2) | A matrix is a verb | Warped grid + unit square | — | M11 | Ax numeric CR + AB≠BA MCQ + transpose MCQ |
| U8 Projections & least squares | 35–45 | Geometry picks the least-wrong line | Squared-error squares | closes linear-model arc | M12, M13 | projection c numeric CR + why-squared MCQ + residual MCQ |
| U9 Rank & redundancy | 60–61 | Redundancy has a number | Rank inspector | closes (AᵀA)⁻¹ loop | M14, M15 | rank numeric CR + multicollinearity MCQ |
| U10 Synthesis + mastery | 62–63 | Everything, pointed at ML | Concept map revisited | all arcs reviewed | — | matching warm-up + 11-item mastery |
| Glossary | all | — | — | — | — | — |

## Learning sequence

U0 → U1 … U10 in the order above → glossary → review/next-steps → colophon. Sticky unit nav with completion dots driven by cleared checks (never scroll). Locked sequence is the LP's; no unit may be skipped by the artifact.

## Interaction and feedback specification (conformance contract)

Every widget below ships; every Explore-badged widget has ≥1 learner-manipulable variable; canvases pair with a live numeric text equivalent; inputs are bounded (sliders/min-max) or the canvas autoscales, so nothing renders off-canvas; multi-entity canvases carry a color legend. All values are computed live in the page's script — nothing hard-coded that can be computed.

| # | Widget (unit) | Manipulable variables | Stated goal | Degenerate guard | Bounds / scaling |
| --- | --- | --- | --- | --- | --- |
| W1 | Matrix-shape explorer (U1) | rows m, cols n (sliders) | "Build a matrix for 4 samples × 2 features" | min 1 each | m 1–6, n 1–4 |
| W2 | Σ-expander (U2) | n (slider); term rule (i / 2i / i²) | "Make the sum exceed 50" | n ≥ 1 | n 1–8 |
| W3 | Weighted-sum lab (U2) | w₁, w₂, x₁, x₂, b (sliders) | "Reach f(x) = 10" | none needed | ±10 each |
| W4 | Span lattice (U3, **gated G1**) | v₁, v₂ direction (angle sliders) | "Collapse the lattice to a line, then restore the plane" | parallel snap within 2° warns | fixed lengths, angles 0–350° step 10 |
| W5 | Zero-hunt tester (U4) | scalars a, b (sliders); pair preset toggle | "Hit (0,0) without setting both sliders to 0" | both-zero state named trivial | a,b ∈ [−3,3] step 0.5 |
| W6 | Norm comparator (U5) | endpoint (x, y) sliders | "Find a point where L1 is nearly double L2" | zero vector noted | x,y ∈ [−6,6] step 0.5 |
| W7 | Dot/angle lab (U6, **gated G2**) | v, w endpoints (sliders); double-length button | "Make them orthogonal; then make the dot product negative" | zero-length input blocked | components ∈ [−5,5] step 0.5 |
| W8 | Transformation playground (U7) | four 2×2 entries (sliders); 6 presets incl. collapse | "Turn the square into a flat line" | singular preset labeled | entries ∈ [−2,2] step 0.5 |
| W9 | AB-vs-BA comparator (U7) | entries of A and B (sliders) | "Find a pair where AB and BA share no entry" | none needed | entries ∈ {0,1,2,3} |
| W10 | Transpose builder (U7) | entries of a 2×3 A (number inputs, bounded) | "Predict which cell pairs swap" | — | entries ∈ [−9,9] |
| W11 | Projection explorer (U8, **gated G3**) | x and y endpoint sliders | "Make the leftover vanish; then make it as long as possible" | y = 0 blocked with teaching note | components ∈ [−5,5] step 0.5 |
| W12 | Least-squares lab (U8) | y₁…y₄ of four points (sliders, x fixed 1–4); outlier preset | "Drive SSE under 1; then place an outlier and watch the line chase it" | vertical fit impossible (x distinct by construction) | y ∈ [0,8] step 0.5; canvas autoscale |
| W13 | Rank inspector (U9) | six entries of a 3×2 matrix (sliders) | "Force rank 1 without zeroing a column" | zero column called out | entries ∈ [−4,4] step 1 |

Static-demo decisions: none — all 13 widgets are manipulable. (The CAN-2026-0004 contrast case was a zero-input least-squares demo badged Explore; W12 is fully manipulable.)

**Prediction gates (P-01, three):** G1 (U3, span of a parallel pair: plane / line / point), G2 (U6, sign of the dot product when θ > 90°: positive / zero / negative), G3 (U8, the leftover's direction: along y / perpendicular to y / opposite x). The manipulable (W4/W7/W11) is hidden by JS until commitment; feedback differentiates per chosen option and quotes the commitment. No-JS readers see the content (hidden by JS only).

**Faded ladders (P-02, four — one per skill):** L1 Σ-expansion (U2; worked Σ[5,3,8,1]=17 → completion Σᵢ₌₁⁴ 2i → independent Σᵢ₌₁³ (i+1)); L2 norms (U5; worked ‖[3,4]‖₂=5, ‖[3,4]‖₁=7 → completion ‖[6,8]‖ → independent ‖[−1,2,2]‖); L3 dot product (U6; worked [1,2]·[3,4]=11 → completion [2,−1]·[4,3] → independent [1,0,−2]·[3,5,1]); L4 projection (U8; worked proj of [2,2] onto [4,0] → completion [3,4] onto [1,0] → independent [2,3] onto [1,1]). Hints tiered (strategy → first step), never auto-open; rung 3 never copies rung 1's numbers.

**Self-verifying readouts:** W11 recomputes e·y = 0 and x̂ + e = x live; W12 recomputes SSE and shows m, c from the normal equation; W8 shows where e₁, e₂ land (columns of A).

**Glossary term set (from CM-2026-0003; every entry six fields — simple / precise / intuition / example / related / where-it-appears):** scalar, vector, matrix, feature, sample, function, linear model, weights, bias, summation (Σ), index, transpose, norm, ℝⁿ, vector space, linear combination, span, basis, dimension, linear independence, dependent vectors, zero vector, dot product, orthogonality, L2 norm, L1 norm, cosine similarity, projection, residual, orthogonal decomposition, least squares, normal equation, matrix multiplication, identity matrix, symmetric matrix, rank, full rank, multicollinearity, embedding, PCA (40 terms). In-lesson dotted terms link to entries without losing place (popover or jump with back-link).

**Concept map (branched dependency graph, not a sequence strip):** nodes {quantities: scalar/vector/matrix; Σ-notation; linear model (weighted sum); add & scale; linear combination; span; independence; basis; dimension; norms; dot product; orthogonality; projection; least squares; matrices as transformations; matrix multiplication; transpose; normal equation; rank; wᵀx reveal}; edges are needed-to-understand arrows incl. branches: {vectors→norms→dot product→projection→least squares}; {add & scale→linear combination→span→independence→basis→dimension}; {independence→rank}; {matrices→multiplication→transpose→normal equation→least squares}; {dot product→wᵀx reveal→linear model}; {rank→(AᵀA)⁻¹ note}. Rendered as SVG in U0 and revisited, fully readable, in U10.

## Visual/representation rationale

Token set per the standard's visual design system (ink/paper/line neutrals, one accent, semantic good/bad/warn); badge system CLASS CORE/FOUNDATION/DEEP DIVE/ML LINK/EXTENSION + provenance tags (source/constructed/supplemental); callouts info/warn/good/ml; widget cards with EXPLORE tag and goal strip; check blocks with CHECK/MASTERY tags; predict blocks dashed; ladder rungs; print-note pattern. Vectors as arrows; span as a collapsing lattice; norms as city-block vs straight line; projection as shadow + dashed leftover + right-angle marker; squared error as shaded squares; matrices as warped grids; rank as a greying dependent column. Math as styled selectable HTML (true radical vinculum); no image formulas; no autoplay; motion only on learner action, disabled under reduced-motion.

## Assessment and misconception checks

Per LP-2026-0004: 9 unit checks each with ≥1 CR item and governing-rule feedback; distractors encode M1–M15; each unit's misconception alert is a visible callout. Mastery = 11 interleaved items with fresh numbers (Σᵢ₌₁⁴ i²; [4,−2]·[1,3]; ‖[2,−3,6]‖₂; proj [5,2] onto [3,0]; parallel-span reasoning; AB≠BA pipeline reasoning; duplicate-feature transfer; planted signed-L1 error-identification; orthogonal MCQ; rank MCQ; explain Aᵀ item), three-level confidence tags, confident-miss routing to the localStorage review list with a next-day return invitation.

## Accessibility and inclusion plan

Standard §1.1 baseline exactly as LP-2026-0004 declares: landmarks, skip link, heading order, focus-visible, native keyboard-operable controls; canvas role="img" + aria-label + adjacent readout via aria-describedby (readouts not aria-live — slider-chatter repair); color never sole encoder (labels/dashes/text); reduced-motion honored; measured AA contrast ≥ 4.5:1 for body text; print stylesheet with per-widget default-state notes; readable at 320 px; storage-unavailable fallback with visible reset.

## Performance/responsiveness intent

Single HTML file, zero external requests, system font stack, inline CSS/JS; canvases redraw only on input; target richness band ≈ reference implementation (CAN-2026-0003, 178,020 bytes) — depth, not bloat, governed by standard §7.

## Acceptance criteria and evaluation dimensions

- Renders from file:// with no console errors and no network; all 13 widgets, 3 gates, 4 ladders, 9 unit checks, matching, and the 11-item mastery check functional (handler-level simulation).
- Every number machine-recomputed (worked examples, ladder rungs, widget defaults, mastery keys); all widget results live-computed.
- XS-conformance: this contract verified element-for-element at P5 (every widget variable, gate behavior, ladder rung, glossary field, concept-map edge); LP reveal arcs pay off where named.
- Evaluated against the ten framework dimensions as a Stage 1 pilot; non-independent review caps disposition at private-pilot-complete, public-release eligibility ineligible (ADR-0003). The comparison judgment (vs CAN-2026-0003 reference and CAN-2026-0004 @0.3.0 output) uses the 2026-08-13 QA-checklist depth items plus the standard rubric.
