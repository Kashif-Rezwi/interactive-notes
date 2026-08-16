# CM-2026-0001: Mathematical foundations and linear algebra for AIML-4 Module 2

**Status:** Reviewed<br>
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)<br>
**Source package:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md)<br>
**Domain review status:** Reviewed by the same operator in a separate Reviewer pass; non-independent (see [EVAL-2026-0001](../evaluations/eval-2026-0001-linear-algebra-foundations-v2.md))<br>
**Confidence:** high

## Scope and learning boundary

Covers the seven parts of the source notebook: mathematical notation (scalars, vectors, matrices, functions, summation), vector spaces and geometry (linear combination, span, basis, dimension), core operations (dot product, L1/L2 norms, orthogonality), projections and least squares, matrices and transformations (multiplication, matrix-vector product, identity, transpose, symmetry), rank and linear independence, and ML connections.

Out of scope (not in the source): eigen decomposition procedures, SVD, calculus of gradients, numerical methods, and any claim beyond the notebook's ML-connection table. The notebook's embedded figures (cells 38 and 42) are transcribed as formulas, not reproduced as images.

## Concepts and definitions

| Concept | Definition (as grounded) | Source anchor |
| --- | --- | --- |
| Scalar | A single numerical value; in ML used as optimization parameters or evaluation metrics (learning rate, weight, bias, loss) | Cell 5, "Scalar" |
| Vector | An ordered collection of numbers arranged in a single dimension, x ∈ Rⁿ; represents feature vectors, embeddings, distributions, hidden states | Cell 7, "Vector" |
| Matrix | A 2-dimensional arrangement of numbers, A ∈ R^(m×n); rows are samples, columns are features | Cells 9–10, "Matrix" |
| Function (ML) | A map f: Rⁿ → R from an n-dimensional input vector to a single real value | Cell 12, "Functions in Machine Learning" |
| Linear model | f(x) = wᵀx + b with weights w, feature vector x, bias b; basis of linear/logistic regression, perceptrons, neural network layers | Cell 13, "Example: Linear Model" |
| Summation notation | Σᵢ₌₁ⁿ xᵢ; compact form used in loss functions, gradients, optimization, statistics | Cell 15, "Summation Notation" |
| Vector space | A structure where vector addition and scalar multiplication are valid and results remain in the space; R² is the 2D example | Cell 21, "Vector Space Definition" |
| Linear combination | a₁x₁ + a₂x₂ + … + aₖxₖ; central to feature engineering, embeddings, PCA; every linear-model prediction is one | Cell 22, "Linear Combination" |
| Span | The set of all possible linear combinations of a set of vectors; two non-parallel 2D vectors span the plane | Cell 24, "Span" |
| Basis | The minimum set of vectors required to span a space; vectors must be linearly independent with no redundancy; {(1,0),(0,1)} is the standard basis of R² | Cell 26, "Basis" |
| Dimension | The number of basis vectors required to represent a space (line 1, plane 2, space 3); ML systems operate in hundreds to millions of dimensions | Cell 28, "Dimension" |
| Dot product | x·y = Σ xᵢyᵢ = ‖x‖‖y‖cos θ; large positive means similar direction, zero means orthogonal, negative means opposite | Cell 30, "Dot Product" |
| L2 norm | ‖x‖₂ = √(Σ xᵢ²); straight-line distance; used in gradient descent, regularization, distance metrics | Cell 32, "L2 Norm" |
| L1 norm | ‖x‖₁ = Σ \|xᵢ\|; used in sparse models, Lasso regression, feature selection | Cell 32, "Norms" |
| Orthogonality | Two vectors are orthogonal iff x·y = 0; orthogonal vectors are independent in direction | Cell 34, "Orthogonality" |
| Projection | proj_y(x) = (x·y / y·y) y; measures how much one vector lies along another; applied in dimensionality reduction, signal processing, PCA, optimization | Cells 37–39, "Projection Formula" (formula transcribed from the embedded figure in cell 38) |
| Orthogonal decomposition | Any vector decomposes as x = x̂ + e; geometric intuition behind regression error minimization | Cells 41–43, "Orthogonal Decomposition" (formula transcribed from the embedded figure in cell 42) |
| Least squares | For Ax = b with no exact solution, find the best approximate solution by minimizing squared error; normal equation x = (AᵀA)⁻¹Aᵀb | Cell 45, "Least Squares (Extremely Important)" |
| Matrix multiplication | C = AB combines transformations; not commutative (AB ≠ BA); order matters in ML pipelines | Cell 48, "Matrix Operations" |
| Matrix-vector product | Ax is a linear transformation (rotation, scaling, projection); neural network layers perform repeated matrix-vector multiplications | Cell 50, "Matrix-Vector Product" |
| Identity matrix | Ix = x; behaves like multiplication by 1; used in inversion, optimization, residual connections | Cell 52, "Identity Matrix" |
| Transpose | Swaps rows and columns: (Aᵀ)ᵢⱼ = Aⱼᵢ; used in covariance computation, backpropagation, proofs | Cell 54, "Transpose" |
| Symmetric matrix | A = Aᵀ; covariance matrices are symmetric; symmetric matrices have real eigenvalues and orthogonal eigenvectors; essential in PCA, spectral methods, optimization | Cell 56, "Symmetric Matrix" |
| Linear independence | a₁x₁ + … + aₙxₙ = 0 implies all aᵢ = 0; no vector can be represented using the others; no redundancy | Cell 59, "Linear Independence" |
| Rank | The number of linearly independent columns (or rows); full rank means no redundancy, low rank means redundant features; relates to multicollinearity and PCA rank reduction | Cell 61, "Rank" |

## Atomic claims and evidence anchors

Citation anchors follow SRC-2026-0001: source SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445`, one-based cell ordinal, visible heading.

1. A scalar is a single numerical value (cell 5, "Scalar").
2. A vector is an ordered collection of numbers in a single dimension, x = [x₁,…,xₙ]ᵀ ∈ Rⁿ (cell 7, "Vector").
3. A matrix is a 2-dimensional arrangement of numbers; in ML, rows are samples and columns are features (cells 9–10, "Matrix").
4. A function maps inputs to outputs, f: Rⁿ → R (cell 12, "Functions in Machine Learning").
5. The linear model is f(x) = wᵀx + b; every neural network layer is a sequence of linear transformations followed by non-linear activations (cell 13, "Example: Linear Model").
6. Summation notation Σᵢ₌₁ⁿ xᵢ adds elements from index 1 to n (cell 15, "Summation Notation").
7. Key notation: xᵀ transpose, ‖x‖ norm, Rⁿ n-dimensional space (cell 17, "Important Notation").
8. The dot product is linear: (x+y)·z = x·z + y·z, provable by expanding with summation notation and distributing (cell 19, "Proof Intuition (Interview Skill)").
9. A vector space is closed under vector addition and scalar multiplication (cell 21, "Vector Space Definition").
10. A linear combination scales vectors and adds them: a₁x₁ + … + aₖxₖ (cell 22, "Linear Combination").
11. The span of vectors is the set of all their linear combinations; two non-parallel vectors in 2D span the entire plane (cell 24, "Span").
12. A basis is a minimum linearly independent spanning set; {(1,0),(0,1)} is the standard basis of R² (cell 26, "Basis").
13. Dimension is the number of basis vectors required to represent a space (cell 28, "Dimension").
14. x·y = Σ xᵢyᵢ and x·y = ‖x‖‖y‖cos θ; sign of the dot product indicates similar, orthogonal, or opposite direction (cell 30, "Dot Product").
15. ‖x‖₂ = √(Σ xᵢ²) measures straight-line distance; ‖x‖₁ = Σ \|xᵢ\| (cell 32, "Norms").
16. Two vectors are orthogonal iff x·y = 0 (cell 34, "Orthogonality").
17. proj_y(x) = (x·y / y·y) y (cell 37 heading "Projection Formula" plus formula transcribed from the embedded figure in cell 38).
18. Any vector decomposes as x = x̂ + e, the geometric intuition behind regression error minimization (cells 41–43, "Orthogonal Decomposition"; formula transcribed from the embedded figure in cell 42).
19. Least squares minimizes squared error for Ax = b when no exact solution exists; the normal equation is x = (AᵀA)⁻¹Aᵀb (cell 45, "Least Squares (Extremely Important)").
20. Matrix multiplication combines transformations and is not commutative (cell 48, "Matrix Operations").
21. Ax is a linear transformation: rotation, scaling, or projection (cell 50, "Matrix-Vector Product").
22. The identity matrix satisfies Ix = x (cell 52, "Identity Matrix").
23. Transpose swaps rows and columns, (Aᵀ)ᵢⱼ = Aⱼᵢ (cell 54, "Transpose").
24. A symmetric matrix satisfies A = Aᵀ and has real eigenvalues and orthogonal eigenvectors (cell 56, "Symmetric Matrix").
25. Vectors are linearly independent iff a₁x₁ + … + aₙxₙ = 0 forces every aᵢ = 0 (cell 59, "Linear Independence").
26. Rank is the number of linearly independent columns (or rows) of a matrix (cell 61, "Rank").
27. ML connections: dot product → similarity/attention; norms → regularization; projection → PCA; least squares → linear regression; rank → feature redundancy; orthogonality → independent components; matrix multiplication → neural networks; eigenvectors → PCA/spectral clustering (cell 63, "PART 7" table).

## Prerequisites and relationships

- Assumed learner prerequisites (not taught by the source): basic arithmetic, algebraic manipulation, and plotting points in 2D.
- Dependency chain: scalar/vector/matrix → summation notation → dot product → norms → orthogonality → projection → orthogonal decomposition → least squares.
- Parallel chain: linear combination → span → basis → dimension → linear independence → rank.
- Matrix operations (multiplication, transpose, identity, symmetry) depend on matrix definition and feed the normal equation and ML connections.

## Examples, non-examples, and misconceptions

**Source examples:** the vector [170, 65, 25]ᵀ as height/weight/age of a person (cell 7); a 3×2 matrix as 3 samples and 2 features (cell 10); Σᵢ₌₁⁴ xᵢ = x₁+x₂+x₃+x₄ (cell 15); R² as a vector space (cell 21); standard basis {(1,0),(0,1)} (cell 26).

**Non-examples (derived for teaching, marked as such in artifacts):** two parallel 2D vectors do not span the plane (contrast with cell 24); a set containing a redundant vector is not a basis (contrast with cell 26); swapping matrix order generally gives a different product (cell 48).

**Common misconceptions to check:**
- Confusing the dot product's sign cases; zero means orthogonal, not "small" (cell 30).
- Treating matrix multiplication as commutative (cell 48).
- Believing Ax = b always has an exact solution; least squares exists for the approximate case (cell 45).
- Confusing dimension of a space with the number of components listed in a redundant description (cells 26–28, 59–61).

## Ambiguities, gaps, and assumptions

- The notebook contains no worked numeric example for the normal equation; any worked example in a derived artifact is constructed, not source-quoted, and must be labeled as such.
- Cells 38 and 42 embed PNG figures; the formulas above are transcriptions of those figures read at extraction time. The figures are not redistributed in derived artifacts.
- The source states L2 norm as ‖x‖₂ = √(Σ xᵢ²) with a typographic subscript/superscript ambiguity in the raw text; the standard reading is adopted.
- The source mentions eigenvectors only in the ML-connections table (cell 63); eigen concepts are named but not taught.
- "Scaler" in the agenda (cell 2) is a source typo for "Scalar".

## Review and acceptance criteria

- Every concept and claim above carries a cell-ordinal anchor to SRC-2026-0001.
- No claim exceeds the source; constructed examples are labeled as constructed.
- Accepted for Stage 1 private-pilot use by the linked run [RUN-20260804-0001](../runs/run-20260804-0001-linear-algebra-foundations-v2.md); not domain-reviewed independently, which limits any downstream public-release eligibility.
