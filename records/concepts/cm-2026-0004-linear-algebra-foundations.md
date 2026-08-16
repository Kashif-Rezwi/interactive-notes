# CM-2026-0004: Mathematical foundations and linear algebra for AIML-4 Module 2 (v7 reproduction run)

**Status:** Reviewed<br>
**Supersedes / iteration position:** Iteration 2 — supersedes [CM-2026-0003](../concepts/cm-2026-0003-linear-algebra-foundations.md) (a fresh run of the same, unchanged source at reference-implementation depth; the claim set is stable because SRC-2026-0001's bytes and the active depth bar are unchanged, so CM-2026-0003 is re-grounded, not re-derived from scratch)<br>
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)<br>
**Source package:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md) — SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445`, 63 markdown cells (hash re-verified at intake, 2026-08-15)<br>
**Domain review status:** Reviewed by the same operator in a separate Reviewer pass; non-independent<br>
**Confidence:** high

## Scope and learning boundary

Identical to [CM-2026-0003](../concepts/cm-2026-0003-linear-algebra-foundations.md) (Iteration 1 of this lineage), which this record supersedes and reproduces at the depth floor the @0.4.0 comparison run validated:

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
| Dot product | x·y = Σ xᵢyᵢ = ‖x‖‖y‖cos θ; large positive → similar direction, zero → orthogonal, negative → opposite | Cells 30 |
| L2 norm | ‖x‖₂ = √(Σ xᵢ²); straight-line distance; used in gradient descent, regularization, distance metrics | Cell 32 |
| L1 norm | ‖x‖₁ = Σ |xᵢ|; used in sparse models, Lasso, feature selection | Cell 32 |
| Orthogonality | x·y = 0; vectors are independent in direction | Cell 34 |
| Projection | How much one vector lies along another; applications in dimensionality reduction, signal processing, PCA, optimization | Cells 37–39 |
| Orthogonal decomposition | Any vector splits into a component along a direction plus a perpendicular leftover; the geometric intuition behind regression error | Cells 40–42 |
| Least squares / normal equation | Given Ax = b with often no exact solution, x̂ = (AᵀA)⁻¹Aᵀb minimizes the squared error | Cell 45 |
| Matrix multiplication | C = AB combines transformations; not commutative (AB ≠ BA); order matters in ML pipelines | Cell 48 |
| Matrix–vector product | Ax is a linear transformation: rotation, scaling, projection; NN layers perform repeated matrix–vector products | Cells 49–50 |
| Identity matrix | Ix = x, behaves like multiplying by 1; used in matrix inversion, optimization, residual connections | Cell 52 |
| Transpose | (Aᵀ)ᵢⱼ = Aⱼᵢ swaps rows and columns; important in covariance, backpropagation, proofs | Cell 54 |
| Symmetric matrix | A = Aᵀ; covariance matrices are symmetric; symmetric matrices have real eigenvalues and orthogonal eigenvectors | Cell 56 |
| Linear independence | a₁x₁ + … + aₙxₙ = 0 ⇒ all aᵢ = 0; no vector is representable by the others, no redundancy | Cell 59 |
| Rank | The number of linearly independent columns (or rows); full rank → no redundancy, low rank → redundant features | Cell 61 |
| ML-connections map | Dot product → similarity/attention; norms → regularization; projection → PCA; least squares → linear regression; rank → feature redundancy; orthogonality → independent components; matrix multiplication → neural networks; eigenvectors → PCA/spectral clustering | Cell 63 |

## Atomic claims and evidence anchors

40 anchored atomic claims across the 27 concepts above, reproducing CM-2026-0003's depth floor — including the single-mention load-bearing claims (cells 9, 12, 19, 21, 35) that a thin claim list would otherwise starve (MEM-2026-0004). Every claim above carries a one-based cell-ordinal anchor to SRC-2026-0001 in the rightmost column; no claim exceeds the source; constructed examples/non-examples are labeled in-artifact.

## Prerequisites and relationships

Reproduces CM-2026-0003's dependency chain. Full ordering (empty-taught-set read-through passes): scalar → vector → matrix → function/linear model → summation → notation kit → dot-product linearity proof → vector space → linear combination → span → basis → dimension → dot product/orthogonality → norms → projection → orthogonal decomposition → normal equation (requires the added inverse + cos θ FOUNDATION bridges) → matrix operations → matrix–vector product → identity → transpose → symmetry → linear independence → rank → ML map. Source ordering defects repaired and labeled: independence/basis moved early (R1); matrices moved before projections so Aᵀ in the normal equation is defined before use (R2); cos θ primer added (R3). Every use-before-define the source commits is either taught first, bridged as FOUNDATION, or labeled EXTENSION.

## Examples, non-examples, and misconceptions

**Examples** (each with its cell anchor, reproducing CM-2026-0003): the height/weight/age vector [170,65,25]ᵀ (cell 7); the 3×2 dataset matrix (cell 10); Σᵢ₌₁⁴ xᵢ = x₁+x₂+x₃+x₄ (cell 15); the (x+y)·z expansion proof (cell 19); the standard basis {(1,0),(0,1)} of ℝ² (cell 26). **Non-examples** include: a parallel pair of 2D vectors that fail to span the plane; [1,2] and [2,4] as a dependent pair; AB ≠ BA on a computed pair; a 3×2 matrix that cannot have rank 3; a set containing the zero vector being dependent.

**Misconceptions (each named with its wrong answer, distractor-ready):**
- M1 Vector: "reordering a vector's entries leaves it unchanged" — learner picks "[65,170,25]ᵀ describes the same person."
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

Identical to CM-2026-0003: cell 2 "Scaler" typo corrected and flagged; cells 13/17/30/59 mangled fragments adopt the standard reading, each flagged; cells 38/41–42 opaque PNGs transcribed, never redistributed; cell 45's normal equation written x̂ with the exact-vs-approximate distinction flagged; no source numeric example exists for projection or the normal equation so all such examples are constructed and labeled; the inverse (·)⁻¹ and cos θ require minimal FOUNDATION bridges; eigenvalues/eigenvectors and "attention"/"spectral clustering" name-drops are EXTENSION pointers only.

## Review and acceptance criteria

- Every concept and claim carries a cell-ordinal anchor to SRC-2026-0001; no claim exceeds the source; constructed examples/non-examples are labeled.
- Depth floor exercised: 40 anchored claims across 27 concepts — reproducing CM-2026-0003 and the reference-implementation depth bar (BMK-2026-0001 / MEM-2026-0004).
- Accepted for Stage 1 governed generation under RUN-20260815-0001; non-independent review limits any downstream release eligibility (ADR-0003).



