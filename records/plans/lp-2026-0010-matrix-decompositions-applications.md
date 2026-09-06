# LP-2026-0010: Learning plan for matrix decompositions and applications v2

**Status:** Reviewed  
**Supersedes / iteration position:** Iteration 2, supersedes [LP-2026-0009](lp-2026-0009-matrix-decompositions-applications.md) (v2 from-scratch rebuild; v1 plan remains the v1 record)  
**Owner:** Repository maintainer  
**Concept model:** [CM-2026-0009](../concepts/cm-2026-0009-matrix-decompositions-applications.md)  
**Target learner and prerequisites:** AIML-4 learner who completed Class 1 (linear algebra foundations: vectors, dot products, matrix multiplication, projection) and is comfortable with algebra; no prior decomposition theory  
**Source and claim links:** [SRC-2026-0002](../sources/src-2026-0002-matrix-decompositions-applications.md); claims CM-2026-0009 #1–38

## Measurable learning outcomes

The learner can: (1) identify and verify an eigenpair numerically; (2) explain why A = PDP⁻¹ makes matrix powers cheap and compute a diagonal power; (3) state when diagonalization is possible and why it can fail; (4) read A = UΣVᵀ as three geometric stages and compute σᵢ from λᵢ(AᵀA); (5) carry a centered dataset through the PCA workflow and connect V of the SVD to principal directions; (6) choose a rank-k truncation, compute its retained energy and error, and state the information tradeoff; (7) connect each mechanism to one honest ML use (spectral methods, covariance analysis, PCA pipelines, recommenders, LoRA-style compression, latent spaces).

## Sequence and rationale

U0 Orientation (how to learn with the page, labels, loop, concept map) → U1 Invariant directions (Av = λv, spectrum, characteristic equation) → U2 Diagonalization (PDP⁻¹, powers, diagonalizability) → U3 SVD (formula, three stages, σ–eigenvalue link, full numeric SVD) → U4 PCA (centering, covariance, PCA = SVD on centered data, workflow) → U5 Low-rank approximation (A_k, energy/error, applications, latent spaces) → Synthesis + mastery → review list → glossary. Rationale: the eigen-direction idea opens in U1 and pays off twice (diagonal powers in U2; PCA directions in U4); SVD opens the decomposition language in U3 and pays off in U5's truncation. Application names (cells 22–24, 31, 36, 38) appear only after the mechanism they use, per the CM repair list.

## Teaching strategy and cognitive-load choices

One visual metaphor throughout: *a transformation has directions and strengths*. Depth pass per unit:

| Unit | Lede | Signature visual (P-14) | Reveal arcs (P-15) | Misconception callouts (≤1/unit) | Computational skills → ladders |
|---|---|---|---|---|---|
| U0 | Learn how the page teaches before the math starts. | Branched concept map (SVG) | — | — | — |
| U1 | Some vectors survive a transformation without turning. | `eigen-direction` canvas: rotate v, watch Av; only two angles keep direction | Eigen-direction setup → payoff in U4 (PCA directions are the data's eigen-directions) | "Every vector is an eigenvector" | L1 eigenpair verification |
| U2 | Rewriting a matrix in its own coordinates makes powers trivial. | `power-calc` live Dⁿ readout | "Cheap powers" setup → payoff in U5 (truncation is the same basis-change idea) | "Diagonalization is repeated multiplication" | L2 diagonal powers |
| U3 | Every matrix, even rectangular, factors into rotate–scale–rotate. | `svd-stage` canvas: unit circle → Vᵀ → Σ → U, step slider | σ = √λ(AᵀA) setup → payoff immediately in U4 (PCA runs on this link) | "SVD only works for square matrices" | L3 singular values from AᵀA |
| U4 | The data's own eigen-directions are the directions that matter. | `pca-plane` canvas: centered scatter, live PC1/PC2, k-projection | U1's eigen-direction arc and U3's σ-link both pay off here | "PCA works the same on uncentered data" | L4 retained-variance fractions |
| U5 | Keep the strongest components, drop the rest, keep most of the meaning. | `rank-energy` canvas: σ bars, live A_k matrix, energy meter | U2's basis-change + U3's SVD pay off here; latent-space close | "Rank-k keeps arbitrary entries" | L5 rank-k error (σ_{k+1}) |

Prediction gates (P-01, 3 total): G1 in U1 (is [1,1] an eigenvector of diag(2,3)?), G2 in U4 (which direction keeps most variance before the scatter reveals it), G3 in U5 (how much energy does rank-1 keep). Gates hide the manipulable until commitment; per-option feedback.

Explain-in-own-words items (≥2, with model-answer reveals and self-evaluation, no textareas): U2 "why does PDP⁻¹ make powers cheap", U4 "why must data be centered for PCA = SVD". Explain-item placement is inside the unit Check blocks.

Mastery check: 7 items (≈ 5 content units + 2), interleaved across units, with 3-level confidence tags (sure / think so / guessing) and confident misses routed to the persistent review list; includes reasoning items (M1, M5), transfer items (M4 sensor data, M7 recommender), and one error-identification item (M6). No worked numbers reused.

Additional-knowledge triage: must-add bridges — determinant (2×2 area view), identity matrix, matrix inverse, linear independence, transpose, mean-centering, variance, rank, projection. Should — descending/nonnegative Σ convention, σᵢ²/n variance relation. Could (collapsed EXTENSION) — geometric vs algebraic multiplicity naming. Do-not-add — numerical eigensolver algorithms, SVD existence proof, complex eigenvalues.

Calibration: [BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) is the active depth exemplar; v2 deliberately closes the three v1 gaps EVAL-2026-0011 exposes (no numeric SVD, no persistent progress state, 5-item mastery without confidence calibration).

## Assessment and evidence of learning

Every unit check has ≥1 constructed-response numeric item (auto-graded with tolerance) plus at least one diagnostic MCQ with per-option misconception feedback; feedback on every miss states the governing rule. Ladders L1–L5 each have 3 rungs with tiered, never-auto-opening hints. Mastery M1–M7 with confidence routing. Persistence: cleared checks fill nav completion dots; misses and confident mastery misses enter a localStorage review list with a spacing invitation and visible reset (graceful fallback when storage is unavailable).

## Accessibility and inclusion intent

Native controls only; keyboard-operable sliders/options; every canvas pairs a text readout with the same numbers and a `.legend-inline` legend; color never the sole encoder; `prefers-reduced-motion` honored; measured WCAG AA contrast; print fallback exposes explanations and hides controls; 16px font floor at all breakpoints.

## Acceptance criteria and review boundary

Strict mechanical verification (`verify-candidate.py`, 0 failures); independent Python recomputation of every displayed number; Node cross-check of the page's live JS math core; dependency-order read-through; six audits + adversarial gate per ADR-0009; rendered browser verification at 320/640/1024px per ADR-0010; repository checker exit 0. Status remains private-pilot-complete, non-independent, ineligible for public release.

## Conformance checklist (depth-calibration contract)

- [x] Active benchmark BMK-2026-0001 cited as calibration exemplar
- [x] Depth-pass table complete for every unit (lede, signature visual, reveal arcs with payoff units, misconception callouts, ladders per skill)
- [x] One full 3-rung faded ladder planned for each of the 5 computational skills (L1–L5)
- [x] ≥ 2 explain-in-own-words items with model-answer reveals allocated (U2, U4)
- [x] Every forward promise / reveal arc names its explicit payoff unit
