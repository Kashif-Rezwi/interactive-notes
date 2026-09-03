# XS-2026-0008: Interactive notes candidate `linear-algebra-foundations-v10.html` (CAN-2026-0009)

**Status:** Approved<br>
**Approval scope:** Stage 1 governed generation<br>
**Supersedes / iteration position:** Iteration 5 — supersedes [XS-2026-0007](../specifications/xs-2026-0007-linear-algebra-foundations-v9.md) (this iteration re-pins the unchanged conformance contract — per-widget viewports, formula manifest, term definition registry, component layout contracts §10.6–§10.8, and strict assessment modality — to candidate v10 / CAN-2026-0009 for RUN-20260904-0001, the full-verification reproduction run)<br>
**Source concept model:** [CM-2026-0007](../concepts/cm-2026-0007-linear-algebra-foundations.md)<br>
**Learning plan:** [LP-2026-0008](../plans/lp-2026-0008-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 student; basic algebra + 2-D plotting; no prior linear algebra<br>
**Artifact family:** Single-file interactive HTML notes; zero external runtime dependencies; file://-functional<br>
**Learning outcomes:** All twelve outcomes of LP-2026-0008; every computational skill has its own faded ladder; every unit check contains auto-evaluated diagnostic items.

## Learner problem and teaching strategy

The learner meets linear algebra as abstract notation. The candidate invests in deep intuition, responsive manipulables, prediction gates, faded ladders, and disciplined layout. This build reproduces the validated v9 reference design (CAN-2026-0008) under the unchanged prompt card `prm-generator-lesson-standard@0.6.0` — atomic slider encapsulation (§10.6), vertical option stacks (§10.7), callout discipline (§10.8), comprehensive formula keys, direct term definition without cop-outs, and zero open textareas — with the run's headline objective being completion of live rendered-output verification (ADR-0010 Audit 6) and repair of the inherited v9 title-identity defect (the v9 artifact's `<title>` still read "(v8)").

## Content and evidence map

Ten teaching units re-sequence the source's seven parts per LP-2026-0007 (repairs R1–R3 labeled in-artifact):
- U0: Orientation with interactive SVG concept map
- U1: Quantities (cells 3–10, M1/M2)
- U2: Compact math (cells 11–17, M3, opens wᵀx arc)
- U3: Combining vectors (cells 20–24, M4/M5, gate G1)
- U4: Independence → basis → dimension (cells 57–59 R1 + 25–28, M6/M7)
- U5: Measuring (cells 31–32, M8)
- U6: Comparing (cells 29–34 + 18–19 R3, M9/M10, gate G2, wᵀx payoff)
- U7: Matrices move space (cells 46–56 R2, M11)
- U8: Projections & least squares (cells 35–45, M12/M13, gate G3, closes linear-model arc)
- U9: Rank & multicollinearity (cells 60–61, M14/M15, closes (AᵀA)⁻¹ loop)
- U10: Synthesis + matching + 11-item mastery check + review list
- Glossary: 40 terms, 6 fields each

## Interaction and feedback specification (conformance contract)

**Canvas engineering contract (ADR-0013, binding on every canvas):** Canonical responsive `makeView(canvasId, xMin, xMax, yMin, yMax)` pattern: `clientWidth` re-measured at every draw, DPR-scaled backing store, CSS height computed from mathematical aspect ratio, normalized transforms `X(x)`/`Y(y)`, `window.addEventListener("resize", draw)` per canvas widget (9 canvases → 9 listeners), no hardcoded pixel offsets, signed angular difference with wrapping for angle arcs, and `.legend-inline` on multi-entity canvases.

### Per-Widget Viewport & Parameters

| # | Widget (unit) | Manipulable variables | Stated goal | Degenerate guard | Bounds / scaling | Viewport (`xMin, xMax, yMin, yMax`) |
| --- | --- | --- | --- | --- | --- | --- |
| W1 | Matrix-shape explorer (U1, canvas) | rows m, cols n (sliders) | "Build a matrix for 4 samples × 2 features" | min 1 each | m 1–6, n 1–4 | grid-units: (−2.6, 9.4, −1.3, 9.7) |
| W2 | Σ-expander (U2, text) | n (slider); term rule (i / 2i / i²) | "Make the sum exceed 50" | n ≥ 1 | n 1–8 | no canvas |
| W3 | Weighted-sum lab (U2, text) | w₁, w₂, x₁, x₂, b (sliders) | "Reach f(x) = 10" | none needed | ±10 each | no canvas |
| W4 | Span lattice (U3, canvas, **gated G1**) | v₁, v₂ direction (angle sliders) | "Collapse the lattice to a line, then restore the plane" | parallel snap within ~5° reported as collapse | fixed lengths 2.5/2; angles 0–350° step 10 | (−9.5, 9.5, −9.5, 9.5) |
| W5 | Zero-hunt tester (U4, canvas) | scalars a, b (sliders); pair preset toggle | "Hit (0,0) without setting both sliders to 0" | both-zero state named trivial | a,b ∈ [−2,2] step 0.5 | square autoscale (−R, R, −R, R), R = 2.1·max_c(\|v1_c\|+\|v2_c\|) |
| W6 | Norm comparator (U5, canvas) | endpoint (x, y) sliders | "Find a point where L1 is nearly double L2" | zero vector noted | x,y ∈ [−6,6] step 0.5 | (−6.8, 6.8, −6.8, 6.8) |
| W7 | Dot/angle lab (U6, canvas, **gated G2**) | v, w components (number inputs); double-v button | "Make them orthogonal; then make the dot product negative" | zero-length input guarded with teaching note | components ∈ [−5,5] step 0.5 | (−5.8, 5.8, −5.8, 5.8) |
| W8 | Transformation playground (U7, canvas) | four 2×2 entries (sliders); 6 presets | "Turn the square into a flat line" | singular preset labeled | entries ∈ [−2,2] step 0.5 | square autoscale (−R, R, −R, R), R ≤ 8.4 |
| W9 | AB-vs-BA comparator (U7, text) | entries of A and B (number inputs) | "Find a pair where AB and BA share no entry" | none needed | entries ∈ {0,1,2,3} | no canvas |
| W10 | Transpose builder (U7, canvas) | entries of a 2×3 A (number inputs); click cell to pair | "Predict which cell pairs swap" | — | entries ∈ [−9,9] | layout-units: (0, 64, 0, 26) |
| W11 | Projection explorer (U8, canvas, **gated G3**) | x and y components (number inputs) | "Make the leftover vanish; then make it as long as possible" | y ≈ 0 blocked with teaching note | components ∈ [−5,5] step 0.5 | (−7.5, 7.5, −7.5, 7.5) |
| W12 | Least-squares lab (U8, canvas) | y₁…y₄ of four points (sliders); outlier preset | "Drive SSE under 0.5; then place an outlier and watch the line chase it" | distinct x coordinates | y ∈ [0,8] step 0.5 | (−0.7, 5.7, −1.0, 9.6) |
| W13 | Rank inspector (U9, text) | six entries of a 3×2 matrix (number inputs) | "Force rank 1 without zeroing a column" | zero column called out | entries ∈ [−4,4] step 1 | no canvas |

### Formula Manifest (Mandatory per §1.1 & @0.6.0)

Every equation below MUST appear in a `.formula` block with a `.symkey` symbol list:
1. Linear model: `f(x) = w₁x₁ + w₂x₂ + ... + wₙxₙ + b` (U2)
2. Summation expansion: `Σᵢ₌₁ⁿ xᵢ = x₁ + x₂ + ... + xₙ` (U2)
3. Linear combination: `v = a₁v₁ + a₂v₂ + ... + aₖvₖ` (U3)
4. Linear independence test: `a₁v₁ + a₂v₂ + ... + aₖvₖ = 0 ⟹ all aᵢ = 0` (U4)
5. Euclidean L2 norm: `‖x‖₂ = √(Σᵢ₌₁ⁿ xᵢ²)` (U5)
6. Manhattan L1 norm: `‖x‖₁ = Σᵢ₌₁ⁿ |xᵢ|` (U5)
7. Algebraic dot product: `x · y = Σᵢ₌₁ⁿ xᵢyᵢ` (U6)
8. Geometric dot product: `x · y = ‖x‖ ‖y‖ cos θ` (U6)
9. Cosine similarity: `cos θ = (x · y) / (‖x‖ ‖y‖)` (U6)
10. Linear model as dot product: `f(x) = wᵀx + b` (U6)
11. Matrix-vector product: `Ax = [row₁ · x, row₂ · x, ..., rowₘ · x]ᵀ` (U7)
12. Transpose definition: `(Aᵀ)ᵢⱼ = Aⱼᵢ` (U7)
13. Scalar projection: `c = (x · y) / (y · y)` (U8)
14. Vector projection: `x̂ = proj_y(x) = c · y = ((x · y) / (y · y)) y` (U8)
15. Orthogonal decomposition: `x = x̂ + e, where e = x - x̂ and e · y = 0` (U8)
16. Normal equation: `x̂ = (AᵀA)⁻¹Aᵀb` (U8)

### Term Definition Registry (Zero Deferral Cop-outs per §1.4 & @0.6.0)

All 40 terms below MUST be defined with plain-language geometric intuition on first mention and included in the 6-field glossary:
1. `scalar`: Single numerical magnitude scaling a vector or tracking a metric (learning rate, loss).
2. `vector`: Ordered array of numbers representing a direction and magnitude in feature space.
3. `matrix`: Rectangular 2D array of numbers storing data samples across features or linear transformations.
4. `feature`: Measurable property of an observation; maps to columns in a design matrix.
5. `sample`: Individual data observation or instance; maps to rows in a design matrix.
6. `function`: Rule mapping an input vector from ℝⁿ to an output value or vector.
7. `linear-model`: Model computing predictions as a weighted sum plus a constant bias.
8. `weights`: Parameters scaling each feature's contribution in a model.
9. `bias`: Constant offset shifting the model prediction independently of inputs.
10. `summation`: Mathematical notation for compact sequential addition over an index.
11. `index`: Integer tracking positions of elements in vectors, matrices, or sums.
12. `transpose`: Operation flipping a matrix or vector over its diagonal, swapping rows and columns.
13. `norm`: Function measuring the length or magnitude of a vector.
14. `rn-space`: Real n-dimensional coordinate space containing all vectors with n real entries.
15. `vector-space`: Set closed under vector addition and scalar multiplication.
16. `linear-combination`: Sum of vectors where each vector is scaled by a real scalar.
17. `span`: Complete subspace reachable by all linear combinations of a vector set.
18. `basis`: Minimal linearly independent set of vectors that spans an entire space without redundancy.
19. `dimension`: Minimum number of basis vectors required to span a space.
20. `linear-independence`: Property where no vector in a set can be written as a linear combination of the others.
21. `dependent-vectors`: Set where at least one vector is redundant and can be built from the rest.
22. `zero-vector`: Vector of all zeros acting as the additive identity in vector space.
23. `dot-product`: Scalar result multiplying matching components of two vectors, reflecting directional agreement.
24. `orthogonality`: State where two vectors meet at 90° and their dot product is exactly zero.
25. `l2-norm`: Straight-line Euclidean distance from the origin to a vector tip.
26. `l1-norm`: City-block Manhattan distance summing absolute coordinate lengths.
27. `cosine-similarity`: Measure of directional alignment independent of vector magnitudes.
28. `projection`: Shadow of one vector dropped perpendicularly onto another vector's line.
29. `residual`: Error vector leftover between the original vector and its projection.
30. `orthogonal-decomposition`: Splitting a vector into a parallel projection plus a perpendicular residual.
31. `least-squares`: Optimization fitting a line or hyperplane by minimizing total squared residuals.
32. `normal-equation`: Closed-form analytic solution solving linear least-squares without iterations.
33. `matrix-multiplication`: Composition of linear transformations combining two matrices.
34. `identity-matrix`: Square matrix leaving any vector unchanged when multiplied.
35. `symmetric-matrix`: Square matrix equal to its own transpose.
36. `rank`: Maximum number of linearly independent rows or columns in a matrix.
37. `full-rank`: Matrix whose rank equals the maximum possible for its dimensions.
38. `multicollinearity`: High linear dependency among predictor features causing matrix inversion instability.
39. `embedding`: Dense vector representation capturing semantic meaning in continuous space.
40. `pca`: Principal Component Analysis, an orthogonal projection method maximizing feature variance.

## Component Layout & Discipline Rules (§10.6–§10.8)

1. **Sliders (§10.6):** Wrapped in `.ctrl-grid` > `.slider-control` with `.slider-head` (`.slider-label` and `.slider-val` with `font-variant-numeric: tabular-nums` and `min-width: 4.5ch`) and `.slider-track` (`<input type="range" style="width:100%">`).
2. **Option Stacks (§10.7):** Radio and checkbox choices in `.predict` and `.check` MUST use `.option-stack` with `.option-item` card wrappers and `.option-text`.
3. **Callout Discipline (§10.8):** At most **1** `.callout` per unit. All other misconceptions are woven into narrative prose or diagnostic MCQ distractor feedback.
4. **Assessment Modalities (§1.4):** Strictly zero `<textarea>` elements. All checks use diagnostic MCQs with option-specific explanations, visual target challenges, or bounded numeric inputs with tolerance.

## Conformance checklist (depth-calibration contract)

- [x] Every widget declares learner-manipulable variable(s) or explicit justification
- [x] Every canvas widget declares input bounding or autoscaling parameters
- [x] Every canvas widget declares its mathematical viewport (`xMin, xMax, yMin, yMax`)
- [x] Exhaustive glossary term set listed from the CM (40 terms, 6 fields each)
- [x] Formula Manifest declared with 16 keyed equations
- [x] Term Definition Registry declared with 40 direct definitions
- [x] Component contracts (§10.6–§10.8) and zero `<textarea>` rule specified
- [x] Concept map declares explicit dependency nodes and directed edges
- [x] Every LP-planned ladder, prediction gate, and reveal arc has a specified element
