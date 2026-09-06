# XS-2026-0010: Interactive notes candidate matrix decompositions v2

**Status:** Approved  
**Approval scope:** Stage 1 governed generation  
**Supersedes / iteration position:** Iteration 2, supersedes [XS-2026-0009](xs-2026-0009-matrix-decompositions-applications-v1.md) (v2 from-scratch rebuild at benchmark-band depth)  
**Source concept model:** [CM-2026-0009](../concepts/cm-2026-0009-matrix-decompositions-applications.md)  
**Learning plan:** [LP-2026-0010](../plans/lp-2026-0010-matrix-decompositions-applications.md)  
**Target learner:** AIML-4 student, post-Class-1 (vectors, dot products, matrix multiplication), no decomposition theory  
**Artifact family:** Single-file offline HTML  
**Learning outcomes:** per LP-2026-0010 §Measurable learning outcomes (7 outcomes, each exercised by ≥1 assessment item)

## Learner problem and teaching strategy

The source is a dense, application-heavy agenda with no worked numbers. The artifact turns it into an explain-before-use path: orientation unit, five units in canonical anatomy (Learn → Predict → Explore → Practice → Check → Connect), synthesis with interleaved mastery, persistent review list, glossary. One visual metaphor throughout: a transformation has directions and strengths. All readouts are computed live in the page; nothing hard-codes what can be computed.

## Content and evidence map

U0 cells 1–2 (agenda → orientation); U1 cells 3–10 (eigenvectors/eigenvalues, geometric reading, spectrum, characteristic equation) + FOUNDATION bridges (determinant, identity); U2 cells 11–16 (diagonalization, powers, diagonalizability, ML insight) + bridges (inverse, linear independence) + constructed A=[[3,1],[0,2]] example; U3 cells 17–24 (SVD formula, three stages, singular values, σ–eigenvalue link, applications) + constructed full numeric SVD of A=[[2,1],[1,2]] (closes EVAL-2026-0011 gap); U4 cells 25–32 (PCA goal, covariance, PCA=SVD connection, workflow, applications) + constructed 10-point dataset; U5 cells 33–40 (low-rank approximation, applications, deep ML insight, latent spaces) + constructed 4×3 ratings matrix. No source cell is silently dropped; the full 40-cell dispositions ship in the evaluation coverage matrix.

## Learning sequence

U0 → U1 → U2 → U3 → U4 → U5 → Synthesis + mastery (M1–M7) → review list → glossary → colophon. Reveal arcs per LP depth-pass table; every forward reference is a promise with a named payoff unit.

## Interaction and feedback specification

**W1 `eigen-direction` (U1, canvas).** Manipulable: θ (direction of unit vector v), slider 0–360°, step 5°. Fixed model: A = diag(2,3) (source cell 6). Draw v and Av as labeled arrows; live readout prints v, Av, and the alignment measure (cross product of v and Av; zero ⇒ direction preserved). Degenerate guard: none needed (v is a unit vector by construction); A is fixed so nothing renders off-canvas. Viewport: xMin=−4, xMax=4, yMin=−4, yMax=4. Legend: v, Av. Text equivalent: full numeric readout of both vectors and alignment. Goal strip: "Find the angles where Av keeps v's direction."

**W2 `power-calc` (U2, numeric widget, no canvas — reason: the skill is arithmetic on diagonal entries, no spatial structure).** Manipulables: d₁, d₂ (diagonal entries, sliders −3…3, step 1) and n (power, slider 1…8). Live readout: Dⁿ matrix and the count of multiplications avoided (n−1). Degenerate guard: d=0 allowed and discussed (0ⁿ=0); negative d sign alternation shown live.

**W3 `svd-stage` (U3, canvas).** Manipulable: stage s, slider 0–3 (0: input circle with v₁,v₂; 1: after Vᵀ rotation; 2: after Σ axis scaling; 3: after U rotation = A's image). Fixed model: A = [[2,1],[1,2]]; the page computes σ, v₁, v₂, u₁, u₂ live from AᵀA via the closed-form 2×2 symmetric eigen solution. Viewport: xMin=−4, xMax=4, yMin=−4, yMax=4. Legend: unit circle, v₁/v₂ directions, image ellipse. Text equivalent: stage description plus live σ and direction numbers.

**W4 `pca-plane` (U4, canvas).** Manipulable: k (components kept, slider 1–2). Fixed model: the constructed 10-point dataset (CM: constructed example); the page centers it live, builds C = (1/n)XᵀX, solves the 2×2 symmetric eigen problem live, draws PC1/PC2 arrows, and for k=1 draws the projected points. Readout: λ₁, λ₂, variance fraction kept, PC1 angle. Viewport: xMin=−3.5, xMax=3.5, yMin=−3, yMax=3. Legend: centered points, PC1, PC2, projected points. Degenerate guard: λ₂>0 by dataset construction; centering removes translation. Goal strip: "See how much variance one direction keeps."

**W5 `rank-energy` (U5, canvas + numeric readout).** Manipulable: k (rank kept, slider 1–3). Fixed model: the constructed 4×3 ratings matrix M (CM: constructed example); the page computes σ and V live from MᵀM via a Jacobi symmetric eigensolver, then Uₖ = MVₖ/σₖ and A_k = UₖΣₖVₖᵀ live. Displays: σ bar chart, retained energy fraction, live A_k matrix entries vs M, and error σ_{k+1}. Viewport (bar chart): xMin=0, xMax=4, yMin=0, yMax=13 (σ₁ ≈ 12.08 bound). Legend: kept bars, dropped bars. Degenerate guard: k bounded 1–3; σ sorted descending. Goal strip: "Choose k to balance size against lost energy."

**Prediction gates (3, P-01):** G1 (U1) "Is [1,1] an eigenvector of diag(2,3)?" — options: yes-everything-scales / no-components-scale-differently / only-if-λ-equal — hides W1 until commit; per-option feedback re-derives the rule (Av must equal λv entry-by-entry). G2 (U4) "One direction keeps most of the variance — which?" — options: widest-spread direction / horizontal axis / vertical axis / no-direction-special — hides W4 until commit. G3 (U5) "Rank-1 keeps how much of this matrix's energy?" — options: about a third / about 85% / over 99% — hides W5 until commit. Unlock is by commitment, never by correctness; feedback differentiates by chosen option.

**Ladders (5, one per computational skill, each 3 rungs, tiered hints, never auto-open):** L1 eigenpair verification (worked: diag(2,3), v=[1,0] → λ=2; completion: diag(2,3), v=[3,0]; independent: diag(2,3), v=[1,1] → not an eigenvector). L2 diagonal powers (worked: diag(2,3)³ → (8,27); completion: diag(3,2)⁴ → (81,16); independent: diag(5,1)² → (25,1)). L3 σ from λ(AᵀA) (worked: λ=9 → σ=3; completion: λ=25 → σ=5; independent: λ=49 → σ=7). L4 retained variance/energy fractions (worked: λ=(9,1) keep 1 → 90%; completion: λ=(8,2) → 80%; independent: σ=(4,3) rank-1 energy → 64%). L5 rank-k error (worked: σ=(5,2) rank-1 error → 2; completion: σ=(7,3,1) rank-1 error → 3; independent: σ=(6,2,0.5) rank-2 error → 0.5).

**Unit checks (constructed response + diagnostic MCQ each):** U1 numeric: eigenvalue of diag(−2,5) for [0,1] → 5 (tolerance 0). U2 numeric: diag(3,2)⁴ (1,1)-entry → 81 (tolerance 0) + explain-in-own-words (model answer reveal + self-evaluation). U3 numeric: λ(AᵀA)=49 → σ=7 (tolerance 0.01). U4 numeric: covariance eigenvalues (6,2), keep 1 component → 75% (tolerance 1) + explain-in-own-words (model answer reveal + self-evaluation). U5 numeric: σ=(4,3) rank-1 energy → 64% (tolerance 1). Each unit also carries one diagnostic MCQ whose distractors are the CM misconceptions, with per-option feedback naming the governing rule. Zero textareas; zero unvalidated free text.

**Mastery (M1–M7, interleaved, confidence-tagged):** M1 reasoning MCQ (diag(4,1), is [1,1] an eigenvector and why); M2 numeric (diag(5,2)³ (1,1)-entry → 125); M3 interpretation MCQ (σ₁=4 > σ₂=2 meaning); M4 transfer numeric (sensor covariance eigenvalues (20,5), keep 1 → 80%, tolerance 1); M5 reasoning MCQ (why center before PCA); M6 error-identification MCQ ("drop σ₁, keep the rest, lose almost nothing" — find the flaw); M7 transfer numeric (recommender σ=(9,3,1), rank-1 energy → 89%, tolerance 1.5). Each item carries sure/think-so/guessing confidence; confident misses route to the review list.

**Persistence (P-13):** cleared checks fill nav completion dots (localStorage `mda2-dots`); misses and confident mastery misses append to review list (localStorage `mda2-review`) with a spacing invitation and visible reset; graceful in-memory fallback with a visible note when storage is unavailable; corrupted storage resets to defaults.

**Concept map (branched, SVG, U0 + revisited in synthesis):** nodes: matrix transformation, eigenvector/eigenvalue, spectrum, diagonalization, matrix powers, transpose, singular value, SVD, PCA, covariance, rank, low-rank approximation, applications, latent space. Edges: transformation→eigenvector; eigenvector→spectrum; eigenvector→diagonalization; diagonalization→powers; diagonalization→covariance-analysis (ML LINK); transpose+singular value→SVD; SVD→PCA (via centered covariance); covariance→PCA; PCA→applications; SVD→low-rank; rank→low-rank; low-rank→compression/denoising; low-rank→latent space; latent space→generative AI.

All range inputs use `.ctrl-grid > .slider-control > .slider-head/.slider-track` with tabular `.slider-val`; options use `.option-stack > .option-item`; every canvas follows the ADR-0013 `makeView` pattern with resize listeners and `.legend-inline`.

## Formula manifest

| Formula ID | Name / Purpose | Equation | Symbol Key Breakdown | Target Unit |
|---|---|---|---|---|
| EQ-001 | Eigenpair | Av = λv | A: square matrix; v: nonzero eigenvector; λ: eigenvalue scale | U1 |
| EQ-002 | Characteristic equation | det(A − λI) = 0 | det: determinant (2×2 area scale); I: identity matrix; λ: unknown eigenvalue | U1 |
| EQ-003 | Diagonalization | A = PDP⁻¹ | P: eigenvector columns; D: diagonal of eigenvalues; P⁻¹: inverse of P | U2 |
| EQ-004 | Power shortcut | Aⁿ = PDⁿP⁻¹ | n: power; Dⁿ: entry-wise powers of diagonal | U2 |
| EQ-005 | SVD | A = UΣVᵀ | U: output (left) directions; Σ: nonnegative descending scales; Vᵀ: transpose of input (right) directions | U3 |
| EQ-006 | σ–eigenvalue link | σᵢ = √λᵢ(AᵀA) | σᵢ: i-th singular value; λᵢ: i-th eigenvalue of AᵀA; √: square root | U3 |
| EQ-007 | Covariance | C = (1/n)XᵀX | X: mean-centered data (rows = samples); n: sample count; C: covariance matrix | U4 |
| EQ-008 | Variance per component | varᵢ = σᵢ²/n | σᵢ: singular value of centered X; n: samples; varᵢ: variance along component i | U4 |
| EQ-009 | Rank-k approximation | A_k = U_kΣ_kV_kᵀ | subscript k: keep only the top-k columns/values | U5 |
| EQ-010 | Retained energy | Σᵢ≤k σᵢ² / Σⱼ σⱼ² | σᵢ²: squared singular values ("energy"); k: kept count | U5 |
| EQ-011 | Truncation error | ‖A − A_k‖₂ = σ_{k+1} | ‖·‖₂: largest singular value of the remainder; σ_{k+1}: first discarded singular value | U5 |

## Term definition registry

| Term | First appearance | Introductory intuition / definition | Glossary status |
|---|---|---|---|
| eigenvector | U1 | Direction a transformation does not turn | complete |
| eigenvalue | U1 | How far that direction stretches | complete |
| spectrum | U1 | The matrix's full set of eigenvalues | complete |
| characteristic equation | U1 | det(A−λI)=0, the equation whose roots are eigenvalues | complete |
| determinant | U1 (FOUNDATION) | For 2×2, ad−bc: how much the transformation scales area | complete |
| identity matrix | U1 (FOUNDATION) | The do-nothing matrix (ones on the diagonal) | complete |
| diagonal matrix | U1 | Nonzero entries only on the diagonal | complete |
| diagonalization | U2 | Rewriting A in its own eigen-coordinates | complete |
| matrix inverse | U2 (FOUNDATION) | The matrix that undoes another | complete |
| linearly independent | U2 (FOUNDATION) | Vectors none of which can be built from the others | complete |
| matrix power | U2 | Repeated multiplication by the same matrix | complete |
| transpose | U3 (FOUNDATION) | Flip rows and columns across the diagonal | complete |
| singular value | U3 | Nonnegative strength of one input→output direction pair | complete |
| left/right singular vectors | U3 | Output (U) / input (V) direction columns | complete |
| SVD | U3 | Rotate–scale–rotate factorization valid for every matrix | complete |
| eigen decomposition | U3 | The square-matrix-only eigen factorization | complete |
| covariance matrix | U4 | Pairwise spread of centered data | complete |
| mean-centering | U4 | Subtract each feature's mean from every sample | complete |
| variance | U4 (FOUNDATION) | Average squared deviation from the mean | complete |
| principal component | U4 | Highest-variance direction of centered data | complete |
| PCA | U4 | Projection onto ordered principal directions | complete |
| projection | U4 (FOUNDATION) | Dropping a point onto a direction | complete |
| rank | U5 | Number of independent directions a matrix really uses | complete |
| low-rank approximation | U5 | Rebuilding A from its top-k components | complete |
| matrix factorization | U5 | Writing a matrix as a product of factor matrices | complete |
| denoising | U5 | Removing weak components that carry little structure | complete |
| latent factor | U5 | Hidden lower-dimensional cause behind observations | complete |
| latent space | U5 | The coordinate system of latent factors | complete |
| recommender system | U5 | Predicting preferences from a user–item matrix | complete |
| LoRA (low-rank adaptation) | U5 (ML LINK) | Fine-tuning by learning small low-rank updates | complete |
| transformer | U5 (ML LINK) | The attention-based architecture behind modern LLMs | complete |
| latent semantic analysis | U3/U5 (ML LINK) | Topic discovery via SVD of word–document matrices | complete |


## Visual/representation rationale

Vectors as labeled arrows from the origin (taught before first use); transformations drawn by mapping the unit circle; multi-entity canvases carry `.legend-inline` swatches; σ magnitudes as bars (kept vs dropped); matrices as bordered grids of numbers. One accent hue plus semantic good/bad/warn; pinned token set per standard §10.1.

## Assessment and misconception checks

As declared in the interaction section: 5 unit checks (each 1 constructed-response numeric + 1 diagnostic MCQ with misconception distractors + U2/U4 explain-in-own-words with model answers), 5 ladders × 3 rungs, 3 prediction gates, mastery M1–M7 with confidence routing. Strict modality: MCQ / bounded auto-graded numeric only; zero `<textarea>`, zero unvalidated free text; options in `.option-stack`.

## Accessibility and inclusion plan

Semantic landmarks (header/nav/main/section/footer), logical heading order, `aria-live` readouts, keyboard-operable native controls, canvas text equivalents with identical numbers, legends plus labels (color never sole encoder), `prefers-reduced-motion` disables transitions, print stylesheet exposes content and hides controls, focus-visible rings, 16px floor at every breakpoint, no drag-only or hover-only interaction.

## Performance/responsiveness intent

Single file; zero external requests; all canvases responsive via `makeView` (clientWidth at draw time, DPR scaling, aspect-ratio height, resize listeners ≥ canvas count); nav single-line horizontal scroll; storage guarded with try/catch and reset.

## Acceptance criteria and evaluation dimensions

`verify-candidate.py` strict pass (0 failures); every Formula-Manifest equation present in a `.formula` block with `.symkey`; every Term-Registry term defined at first mention and linked to a 6-field glossary entry; every widget matches its declaration element-for-element; six audits + adversarial gate pass; rendered verification at 320/640/1024px with 0 console errors; repository checker exit 0; disposition private-pilot-complete, non-independent, release-ineligible.

## Conformance checklist (depth-calibration contract)

- [x] Every widget declares learner-manipulable variable(s) or explicit "static demo" justification (W2 is numeric by stated reason)
- [x] Every canvas widget declares input bounding (sliders, min/max) — θ, s, k, k bounded; fixed models bounded by construction
- [x] Every canvas widget declares its mathematical viewport (W1 ±4/±4; W3 ±4/±4; W4 x±3.5/y±3; W5 0–4 × 0–13)
- [x] Controls declare atomic `.slider-control` encapsulation and `.option-stack` layout
- [x] Complete Formula manifest (EQ-001–EQ-011) mapped to unit `.formula` blocks
- [x] Complete Term definition registry (32 terms); zero deferred jargon
- [x] Assessment modality strictly MCQ / bounded auto-graded numeric; no `<textarea>`
- [x] Exhaustive glossary term set listed from the CM (every term used gets 6 fields)
- [x] Concept map declares explicit dependency nodes and directed edges (multi-branch)
- [x] Every LP-planned ladder (L1–L5), prediction gate (G1–G3), and reveal arc has a specified element
- [x] Canvas text equivalents specified for every visual component
