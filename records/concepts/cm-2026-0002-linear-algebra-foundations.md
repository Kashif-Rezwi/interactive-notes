# CM-2026-0002: Linear algebra foundations (regeneration test)

**Status:** Reviewed<br>
**Supersedes / iteration position:** Iteration 1 — original (authored fresh from source for the pipeline regeneration test; does not read or reuse CM-2026-0001)<br>
**Owner:** Repository maintainer<br>
**Source package:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md) (SHA-256 `23c6f4eb…f94445`; 63 markdown cells, 1-based anchors)<br>
**Domain review status:** Non-independent (author = reviewer)<br>
**Confidence:** high

## Scope and learning boundary

All 63 cells of the AIML-4 Module 2 Class 1 notebook: mathematical notation, vector spaces, core operations, projections/least squares, matrices/transformations, rank/independence, ML connections. Out of scope: eigenvalues/eigenvectors (named only in the cell-63 table — disposition below), matrix inversion mechanics, determinants, PCA internals.

## Concepts and definitions

Scalar (4–5); vector, column form, feature-vector reading (6–7); matrix, rows=samples/columns=features (8–10); function f: Rⁿ→R (11–12); linear model f(x)=wᵀx+b (13); summation Σ (14–15); notation xᵀ, ‖x‖, Rⁿ (16–17); linearity proof of dot product (18–19); vector space (20–21); linear combination (22); span (23–24); basis (25–26); dimension (27–28); dot product algebraic + geometric x·y=‖x‖‖y‖cosθ (29–30); L2 norm, L1 norm (31–32); orthogonality x·y=0 (33–34); projection (35–39); orthogonal decomposition (40–43); least squares + normal equation (44–45); matrix multiplication C=AB, AB≠BA (46–48); matrix-vector product as transformation (49–50); identity Ix=x (51–52); transpose (53–54); symmetric matrix A=Aᵀ (55–56); linear independence (57–59); rank (60–61); ML connection map (62–63).

## Atomic claims and evidence anchors

Every concept above anchors to the cited cells. Key load-bearing claims: "a vector is an ordered collection of numbers" (7); "rows are samples, columns features" (10); "every neural network layer is a linear transformation followed by a non-linear activation" (13); "span = all linear combinations" (24); "basis = minimum independent spanning set" (26); "dot product measures similarity; zero ⇒ orthogonal" (30, 34); "projection = how much one vector lies along another" (37); "least squares = best approximate solution minimizing squared error" (45); "matrix multiplication is not commutative" (48); "symmetric ⇒ real eigenvalues, orthogonal eigenvectors" (56); "independence ⇒ no redundancy" (59); "rank counts independent columns" (61).

## Prerequisites and relationships

Source assumes: basic algebra, 2-D plotting, angle θ, function notation. Dependency chain (repaired order): notation → vector space → linear combination → span → **linear independence → basis → dimension** → dot product → norms → orthogonality → **matrix multiplication → transpose** → projection → decomposition → least squares → rank → ML synthesis. Source-order defects requiring repair: basis (26) requires linear independence taught only at 57–59; the normal equation (45) uses transpose/inverse taught at 53–54 and not at all, respectively; the proof skill (18–19) uses the dot product taught at 29–30.

## Examples, non-examples, and misconceptions

Source examples: person vector [170,65,25] (7); 3×2 data matrix (10); linear model (13); Σ₁⁴ expansion (15); R² standard basis (26); linearity derivation (19). Misconceptions to name and test: AB=BA (against 48); two vectors always span a plane (against 24 — parallel collapse); x·y=0 means a zero vector (against 34); rank counts columns (against 61); least squares solves Ax=b exactly (against 45); "bigger norm = more important feature" (constructed).

## Ambiguities, gaps, and assumptions

- Cell 2: "Scaler" typo → corrected, flagged. Cell 17: "Rn" typography → ℝⁿ, flagged.
- Cell 32: L2 formula mangled as √(∑x^i_2) → transcribed ‖x‖₂=√(Σxᵢ²), flagged.
- Cells 30, 45, 59: duplicated/mangled formula layouts → transcribed cleanly, flagged.
- Cells 38, 42: opaque base64 PNGs (projection formula; decomposition) → transcribed as proj_b(a)=((a·b)/(b·b))·b and a=a∥+a⊥ with a⊥·b=0; figures not redistributed (provenance-preserving).
- Cell 45: normal equation uses matrix inverse, never taught → FOUNDATION bridge (2×2 only, "the matrix that undoes"); x̂ hat notation flagged as clarification. Full inversion → EXTENSION.
- cosθ (30) assumed → brief FOUNDATION primer. Unit vector → FOUNDATION bridge inside projection.
- Cell 63 names eigenvectors without teaching → EXTENSION label, one line, no teaching.
