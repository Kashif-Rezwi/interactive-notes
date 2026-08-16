# CM-2026-0003: Mathematical foundations and linear algebra for AIML-4 Module 2 (v6 comparison run)

**Status:** Reviewed<br>
**Supersedes / iteration position:** Iteration 1 — original (authored fresh from SRC-2026-0001 for the prompt-card @0.4.0 comparison run; CM-2026-0001 consulted only as the depth-floor calibration exemplar per the template note and MEM-2026-0004)<br>
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)<br>
**Source package:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md) — SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445`, 63 markdown cells (hash re-verified at intake, 2026-08-13)<br>
**Domain review status:** Reviewed by the same operator in a separate Reviewer pass; non-independent<br>
**Confidence:** high

## Scope and learning boundary

Covers all seven parts of the source notebook: notation (scalars, vectors, matrices, functions, summation, notation kit, proof intuition), vector spaces and geometry (vector space, linear combination, span, basis, dimension), core operations (dot product, L2/L1 norms, orthogonality), projections and least squares (projection, orthogonal decomposition, normal equation), matrices and transformations (multiplication, matrix-vector product, identity, transpose, symmetry), rank and linear independence, and the ML-connections table.

Out of scope (not in the source): determinant procedure and named use, matrix inversion procedure beyond a bridged 2×2 reading, eigen decomposition, SVD, gradient calculus, PCA internals, numerical methods. The embedded PNG figures (cells 38, 41–42) are transcribed as formulas, never redistributed as images.

## Concepts and definitions

| Concept | Definition (as grounded) | Source anchor |
| --- | --- | --- |
| Scalar | A single numerical value; in ML used as optimization parameters or evaluation metrics (learning rate, weight value, bias, loss) | Cell 5 |
| Vector | An ordered collection of numbers in a single dimension, x = [x₁,…,xₙ]ᵀ ∈ ℝⁿ; represents feature vectors, embeddings, user representations, distributions, hidden states | Cell 7 |
| Matrix | A 2-dimensional arrangement of numbers, A ∈ ℝ^(m×n); rows = samples/observations, columns = features | Cells 9–10 |
| Function (ML) | A map f: ℝⁿ → ℝ from an n-dimensional input vector to a single real value | Cell 12 |
| Linear model | f(x) = wᵀx + b with weights w, features x, bias b; foundation of linear/logistic regression, perceptrons, neural networks; every NN layer is linear transformations + non-linear activations | Cell 13 |
| Summation notation | Σᵢ₌₁ⁿ xᵢ adds elements from index 1 to n; used in loss functions, gradients, optimization, statistics | Cell 15 |
| Notation kit | xᵀ transpose; ‖x‖ norm; ℝⁿ n-dimensional space | Cell 17 |
| Dot-product linearity | (x+y)·z = x·z + y·z, proved by expanding with Σ and distributing; an interview skill used in gradient derivations and backpropagation | Cell 19 |
| Vector space | A structure closed under vector addition and scalar multiplication; ℝ² contains all 2D vectors | Cell 21 |
| Linear combination | a₁x₁ + a₂x₂ + … + aₖxₖ — scale vectors and add; central to feature engineering, NN representations, embeddings, PCA; every linear-model prediction is one | Cell 22 |
| Span | The set of all possible linear combinations of a set of vectors; two non-parallel 2D vectors span the entire plane | Cell 24 |
| Basis | The minimum set of vectors required to span a space; must be linearly independent, no redundancy; {(1,0),(0,1)} is the standard basis of ℝ² | Cell 26 |
| Dimension | The number of basis vectors required to represent a space (line 1, plane 2, space 3); ML systems operate in hundreds to millions of dimensions | Cell 28 |
| Dot product | x·y = Σ xᵢyᵢ = ‖x‖‖y‖cos θ; large positive = similar direction, zero = orthogonal, negative = opposite | Cell 30 |
| L2 norm | ‖x‖₂ = √(Σ xᵢ²); straight-line distance; used in gradient descent, regularization, distance metrics | Cell 32 |
| L1 norm | ‖x‖₁ = Σ \|xᵢ\|; used in sparse models, Lasso regression, feature selection | Cell 32 |
| Orthogonality | Two vectors are orthogonal iff x·y = 0; orthogonal vectors are independent in direction | Cell 34 |
| Projection | proj_y(x) = (x·y / y·y)·y; how much of x lies along y; applied in dimensionality reduction, signal processing, PCA, optimization | Cells 37–39 (formula transcribed from the cell-38 figure) |
| Orthogonal decomposition | Any vector decomposes as x = x̂ + e (projection plus perpendicular leftover); the geometric intuition behind regression error minimization | Cells 40–43 (formula transcribed from the cell-42 figure) |
| Least squares | For Ax = b with (often) no exact solution, find the best approximate solution by minimizing squared error; normal equation x̂ = (AᵀA)⁻¹Aᵀb | Cell 45 |
| Matrix multiplication | C = AB combines transformations; not commutative (AB ≠ BA in general); order matters in ML pipelines | Cell 48 |
| Matrix-vector product | Ax is a linear transformation (rotation, scaling, projection); NN layers perform repeated matrix-vector multiplications | Cell 50 |
| Identity matrix | Ix = x; behaves like multiplication by 1; used in inversion, optimization, residual connections | Cell 52 |
| Transpose | Swaps rows and columns: (Aᵀ)ᵢⱼ = Aⱼᵢ; used in covariance computation, backpropagation, proofs | Cell 54 |
| Symmetric matrix | A = Aᵀ; the covariance matrix is symmetric; symmetric matrices have real eigenvalues and orthogonal eigenvectors; essential in PCA, spectral methods, optimization | Cell 56 |
| Linear independence | a₁x₁ + … + aₙxₙ = 0 forces every aᵢ = 0; no vector can be represented using the others; no redundancy | Cell 59 |
| Rank | The number of linearly independent columns (or rows) of a matrix; full rank = no redundancy, low rank = redundant features; ties to multicollinearity; PCA reduces rank | Cell 61 |

## Atomic claims and evidence anchors

Anchors follow SRC-2026-0001: one-based cell ordinal over the 63 markdown cells.

1. A scalar is a single numerical value; ML examples are learning rate, weight value, bias term, loss value (cell 5).
2. Scalars serve as optimization parameters or evaluation metrics in ML systems (cell 5).
3. A vector is an ordered collection of numbers arranged in a single dimension (cell 7).
4. x = [x₁,…,xₙ]ᵀ ∈ ℝⁿ (cell 7).
5. Vectors represent feature vectors, word embeddings, user representations, probability distributions, hidden states (cell 7).
6. [170, 65, 25]ᵀ can read as height, weight, age of one person (cell 7).
7. A matrix is a 2-dimensional arrangement of numbers, A ∈ ℝ^(m×n), with m rows and n columns (cells 9–10).
8. In ML, matrix rows are samples/observations and columns are features; the 3×2 example holds 3 samples × 2 features (cell 10).
9. Datasets in ML pipelines are almost always represented as matrices (cell 10).
10. A function maps inputs to outputs; f: ℝⁿ → ℝ takes an n-vector to one real value (cell 12).
11. The linear model is f(x) = wᵀx + b with weights w, feature vector x, bias b (cell 13).
12. This equation founds linear regression, logistic regression, perceptrons, neural networks; every NN layer is linear transformations followed by non-linear activations (cell 13).
13. Σᵢ₌₁ⁿ xᵢ adds all elements from index 1 to n; used in loss functions, gradient calculations, optimization equations, statistical computations (cell 15).
14. Σᵢ₌₁⁴ xᵢ = x₁+x₂+x₃+x₄ (cell 15).
15. Notation: xᵀ is transpose, ‖x‖ is norm, ℝⁿ is n-dimensional space (cell 17).
16. The dot product is linear: (x+y)·z = x·z + y·z; the proof expands with Σ and distributes; such derivations matter in gradient derivations, backpropagation proofs, optimization theory, ML interviews (cell 19).
17. A vector space is a structure where vector addition and scalar multiplication are valid and keep results inside the space; ℝ² contains all 2D vectors (cell 21).
18. A linear combination scales vectors and adds them: a₁x₁ + a₂x₂ + … + aₖxₖ (cell 22).
19. Linear combination is central to feature engineering, NN representations, latent embeddings, PCA; every prediction in a linear model is a weighted linear combination of features (cell 22).
20. The span of vectors is the set of all their linear combinations; vectors that generate an entire space are said to span it; two non-parallel 2D vectors span the plane (cell 24).
21. In ML, feature representations span information space and embeddings span semantic spaces (cell 24).
22. A basis is the minimum set of vectors required to span a space; its vectors must be linearly independent with no redundant vectors; {(1,0),(0,1)} is the standard basis of ℝ² (cell 26).
23. Dimension is the number of basis vectors required to represent a space: line 1, plane 2, space 3; ML systems often operate in hundreds, thousands, or millions of dimensions (cell 28).
24. x·y = Σᵢ xᵢyᵢ (cell 30).
25. x·y = ‖x‖‖y‖cos θ where θ is the angle between the vectors; large positive = similar direction, zero = orthogonal, negative = opposite (cell 30).
26. ‖x‖₂ = √(Σ xᵢ²) measures straight-line distance; applied in gradient descent, regularization, distance metrics (cell 32).
27. ‖x‖₁ = Σ \|xᵢ\|; applied in sparse models, Lasso regression, feature selection (cell 32).
28. Two vectors are orthogonal iff x·y = 0; orthogonal vectors are independent in direction (cell 34).
29. proj_y(x) = (x·y / y·y)·y measures how much one vector lies along another; applied in dimensionality reduction, signal processing, PCA, optimization (cells 37–39; formula transcribed from the cell-38 PNG).
30. Any vector decomposes as x = x̂ + e; this is the geometric intuition behind regression error minimization (cells 40–43; formula transcribed from the cell-42 PNG).
31. For Ax = b an exact solution often does not exist; least squares finds the best approximate solution by minimizing squared error (cell 45).
32. The normal equation is x̂ = (AᵀA)⁻¹Aᵀb (cell 45; presented twice in the source with mangled line-broken layout; x̂ hat added for precision, flagged).
33. Matrix multiplication C = AB combines transformations; it is not commutative, AB ≠ BA; order matters significantly in ML pipelines (cell 48).
34. Ax is a linear transformation: rotation, scaling, projection; NN layers internally perform repeated matrix-vector multiplications (cell 50).
35. The identity matrix behaves like multiplication by 1: Ix = x; used in matrix inversion, optimization, residual connections (cell 52).
36. Transpose swaps rows and columns, (Aᵀ)ᵢⱼ = Aⱼᵢ; important in covariance computation, backpropagation, linear algebra proofs (cell 54).
37. A symmetric matrix satisfies A = Aᵀ; the covariance matrix is symmetric; symmetric matrices have real eigenvalues and orthogonal eigenvectors; essential in PCA, spectral methods, optimization (cell 56).
38. Vectors are linearly independent iff a₁x₁ + … + aₙxₙ = 0 implies every aᵢ = 0; no vector can be represented using the others; no redundancy exists (cell 59; mangled line-broken layout transcribed).
39. Rank is the number of linearly independent columns (or rows) in a matrix; full rank = no redundancy, low rank = redundant features; ML insight: multicollinearity problem; PCA reduces rank (cell 61).
40. ML connections: dot product → similarity/attention; norms → regularization; projection → PCA; least squares → linear regression; rank → feature redundancy; orthogonality → independent components; matrix multiplication → neural networks; eigenvectors → PCA/spectral clustering (cell 63).

## Prerequisites and relationships

Assumed learner prerequisites (declared at intake): basic arithmetic, algebraic manipulation, plotting points in 2D. Nothing else.

Dependency chains (derived from the claims, not the source's page order):
- scalar/vector/matrix (claims 1–9) → Σ notation (13–14) → functions + linear model as weighted sum (10–12, notation kit 15).
- vector addition/scaling (17) → linear combination (18–19) → span (20–21) → **linear independence (38)** → basis (22) → dimension (23) → rank (39).
- vectors → norms (26–27) → dot product algebraic form (24) → geometric form (25, needs a cos θ primer — not in the source, FOUNDATION bridge) → orthogonality (28) → projection (29) → orthogonal decomposition (30) → least squares (31–32).
- matrix definition (7–9) → matrix-vector product (34; row-wise products are dot products — needs claim 24) → matrix multiplication (33) → identity (35), transpose (36), symmetric (37) → normal equation (32; needs transpose + multiplication + a minimal inverse bridge — not in the source, FOUNDATION).

Use-before-define cases the source commits (each needs repair or bridging in the plan):
1. The linearity proof (cell 19) uses the dot product before the source defines it (cell 30) → repair R3: teach it after the dot product.
2. The basis definition (cell 26) requires linear independence, taught only at cell 59 → repair R1: independence before basis.
3. The normal equation (cell 45) uses transpose and matrix multiplication, taught at cells 54 and 48, and uses (·)⁻¹ with no inverse teaching anywhere → repair R2: matrices before least squares, plus a FOUNDATION inverse bridge.
4. wᵀx (cell 13) uses transpose and dot-product machinery before both → teach the linear model as an explicit weighted sum first; the compact wᵀx form becomes a planned reveal once the dot product exists (reveal arc, P-15).
5. Eigenvectors appear only in the cell-63 table with no teaching → EXTENSION one-liner with a promise, never load-bearing.

Visual conventions the lesson will rely on (each taught before first use): vectors drawn as arrows from the origin on a 2D grid; a matrix drawn as a labeled grid of numbers; a point cloud with a fitted line; a grid that warps under a transformation; a parallelogram/lattice built from two vectors.

## Examples, non-examples, and misconceptions

**Source examples (all anchored):** [170, 65, 25]ᵀ as height/weight/age (cell 7); 3×2 matrix as 3 samples × 2 features with entries 1..6 (cell 10); Σᵢ₌₁⁴ xᵢ expansion (cell 15); ℝ² as vector space (cell 21); {(1,0),(0,1)} standard basis (cell 26); line/plane/space dimensions (cell 28); linearity expansion of (x+y)·z (cell 19).

**Non-examples (constructed, labeled as such):** [65, 170, 25]ᵀ is a different vector than [170, 65, 25]ᵀ (order matters — contrast cell 7); two parallel vectors do not span the plane (contrast cell 24); {[1,0],[2,0]} is not a basis of ℝ² (redundant — contrast cell 26); a 3×2 matrix cannot have rank 3 (contrast cell 61); AB = BA fails on a computed pair (contrast cell 48); a set containing the zero vector is never independent (extends cell 59).

**Misconceptions (each named with its wrong answer, distractor-ready):**
- M1 Vector: "reordering a vector's entries leaves it unchanged" — the learner picks "[65,170,25]ᵀ describes the same person."
- M2 Matrix: "rows are features, columns are samples" — the swapped reading of cell 10.
- M3 Σ: "Σ xᵢ multiplies the terms" — learner computes a product.
- M4 Linear combination: "the scalars aᵢ must be positive" — learner rejects negative or zero scalars.
- M5 Span: "any two 2D vectors span the whole plane" — learner answers "the plane" for a parallel pair (the gate's committed wrong answer).
- M6 Independence: "vectors that look different are independent" — learner calls [1,2] and [2,4] independent.
- M7 Basis: "basis vectors must be unit length and perpendicular" — learner rejects a valid skewed basis.
- M8 Norms: "‖x‖₁ adds the signed entries" — learner computes ‖[−3,4]‖₁ = 1 instead of 7.
- M9 Dot product: "a bigger dot product always means more similar direction" — the magnitude confound (‖x‖‖y‖ grows the product without changing θ).
- M10 Orthogonality: "x·y = 0 means one of the vectors is the zero vector" — learner misses perpendicularity.
- M11 Matrix multiplication: "AB = BA always, numbers commute so matrices do too."
- M12 Projection: "the leftover e can point in any direction" — learner picks a non-perpendicular leftover (the gate's wrong answers).
- M13 Least squares: "the best-fit line passes through every data point" — learner expects an exact fit.
- M14 Rank: "a 3×2 matrix has rank 3" — learner reports the larger dimension instead of rank ≤ min(m,n).
- M15 Multicollinearity: "a duplicate feature is harmless" — learner sees no problem with column 2 = 2 × column 1 (breaks (AᵀA)⁻¹, the U8 loop-closure).

## Ambiguities, gaps, and assumptions

- Cell 2 agenda lists "Scaler" — typo for "Scalar"; correct and flag in-artifact.
- Cell 13 renders wᵀx as broken "w T x" line fragments; cell 17 renders ℝⁿ as "Rn"; cell 30's Σ form and cell 59's independence condition are line-broken fragments; cell 32 renders ‖x‖₂ = √(Σ xᵢ²) with sub/superscript ambiguity — the standard reading is adopted, each flagged.
- Cells 38 and 42 embed opaque PNG formulas (projection; orthogonal decomposition). Transcriptions above follow CM-2026-0001's readings (consistent with cells 37/40–43 prose). Figures are never redistributed; transcriptions are flagged in-artifact.
- Cell 45 presents the normal equation twice in mangled layout and writes x without the hat; the lesson writes x̂ (the approximate solution) and flags the distinction: x̂ is generally not an exact solution of Ax = b.
- The source contains no worked numeric example for the normal equation or projection — every numeric example in the artifact is constructed and labeled `constructed example`.
- The inverse (·)⁻¹ is used (cell 45) but never taught; the plan must add a minimal FOUNDATION bridge (2×2 inverse + "when it fails") without teaching an inversion procedure.
- cos θ is used (cell 30) but never taught; a one-block FOUNDATION primer is required.
- Eigenvalues/eigenvectors are named (cells 56, 63) but never taught; EXTENSION pointer only.
- Cell 63's "attention" and "spectral clustering" name-drop advanced ML; one-line glosses at learner level, labeled ML LINK/EXTENSION.

## Review and acceptance criteria

- Every concept and claim above carries a cell-ordinal anchor to SRC-2026-0001; no claim exceeds the source; constructed examples/non-examples are labeled.
- Depth floor exercised: 40 anchored claims across 27 concepts — including single-mention load-bearing claims (9, 12, 19, 21, 35) — versus the ~13-claim floor that preceded CAN-2026-0004 (MEM-2026-0004).
- Accepted for Stage 1 governed generation under RUN-20260813-0002; non-independent review limits any downstream release eligibility (ADR-0003).
