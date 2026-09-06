# CM-2026-0009: Matrix decompositions and applications (v2 rebuild concept model)

**Status:** Reviewed  
**Supersedes / iteration position:** Iteration 2, supersedes [CM-2026-0008](cm-2026-0008-matrix-decompositions-applications.md) (deeper re-read of the same source for the v2 from-scratch rebuild; CM-2026-0008 remains the v1 record)  
**Owner:** Repository maintainer  
**Source package:** [SRC-2026-0002](../sources/src-2026-0002-matrix-decompositions-applications.md)  
**Domain review status:** Reviewed by the same operator; non-independent  
**Confidence:** high

## Scope and learning boundary

The lesson reorganizes the 40-cell source into an orientation unit plus five dependency-ordered units: invariant directions, diagonalization, SVD, PCA, and low-rank approximation. It adds only the FOUNDATION bridges needed to read the formulas with the declared learner's prerequisites: matrix–vector products as transformations, the 2×2 determinant (area view), identity matrix, transpose, mean-centering, variance, linear independence, and rank. It does not teach numerical eigensolvers, the algebraic/geometric multiplicity proof, or a proof of the SVD's existence. Unlike v1, this iteration *does* add a fully worked constructed numeric SVD (the gap recorded in EVAL-2026-0011) and a constructed PCA dataset with live-computed principal directions.

## Concepts and definitions

| Concept | Definition | Source anchor |
|---|---|---|
| Eigenvector | A nonzero vector whose direction is unchanged by A: Av = λv | Cells 3–8 |
| Eigenvalue | The scale λ applied to an eigenvector | Cells 3–8 |
| Spectrum | The set {λ₁…λₙ} of a matrix's eigenvalues | Cells 9–10 |
| Characteristic equation | det(A − λI) = 0; its roots are the eigenvalues | Cell 10 |
| Diagonalization | A = PDP⁻¹ with P the eigenvector matrix, D the eigenvalue diagonal | Cells 11–12 |
| Matrix power shortcut | Aⁿ = PDⁿP⁻¹; Dⁿ raises diagonal entries individually | Cells 13–14 |
| Diagonalizability | Requires n linearly independent eigenvectors | Cell 15 |
| SVD | A = UΣVᵀ, valid for every real matrix including rectangular | Cells 17–19 |
| Left/right singular vectors | Columns of U (output directions) / V (input directions) | Cell 19 |
| Singular value | Nonnegative scale σᵢ describing a direction's strength | Cell 21 |
| σ–eigenvalue link | σᵢ = √λᵢ(AᵀA) | Cell 22 |
| Covariance matrix | C = (1/n)XᵀX on centered data X | Cell 26 |
| Principal component | Eigenvector of C / right singular vector of centered X, ordered by descending variance | Cells 27–29 |
| PCA | Projection onto ordered maximum-variance directions; SVD on centered data | Cells 25–29, 32 |
| Low-rank approximation | A_k = U_kΣ_kV_kᵀ keeping only top-k singular components | Cells 33–34 |
| Latent factor / latent space | Hidden lower-dimensional cause of high-dimensional observations | Cells 36–40 |

## Atomic claims and evidence anchors

1. Most vectors rotate and stretch under a matrix; eigenvectors only stretch (cells 3–4, 7–8).
2. Eigenvectors are nonzero by definition; the zero vector is excluded because it would satisfy the equation trivially (implicit in cell 5; bridge).
3. Av = λv holds for square matrices; v is the eigenvector and λ the eigenvalue (cell 5).
4. For diag(2,3), [1,0] and [0,1] are eigenvectors with eigenvalues 2 and 3 (cell 6).
5. Eigenvectors reveal dominant directions, stable patterns, and intrinsic geometry; foundational for PCA, spectral methods, dynamical systems, covariance analysis (cell 6).
6. Eigenvectors define invariant subspaces / stable transformation axes; eigenvalues are expansion/contraction rates along them (cells 7–8).
7. The set of eigenvalues is called the spectrum; spectral clustering, normalization, and graph theory originate from eigen-analysis (cell 10).
8. Eigenvalues are roots of det(A − λI) = 0 (cell 10; the duplicated equation in the cell is a transcription artifact).
9. A = PDP⁻¹ where P collects eigenvectors and D the eigenvalues (cell 12).
10. Diagonalization is useful because diagonal matrices are easy to compute with (cell 12).
11. A¹⁰⁰ = PD¹⁰⁰P⁻¹ avoids 100 sequential multiplications; D¹⁰⁰ raises diagonal entries individually (cells 12, 14).
12. Diagonalization also simplifies exponentials, differential equations, and dynamical systems (cell 12).
13. A matrix is diagonalizable iff it has n linearly independent eigenvectors (equivalently geometric = algebraic multiplicity for every eigenvalue) (cell 15).
14. Diagonalization helps understand transformations, simplify covariance structures, analyze stability, and interpret neural network dynamics (cell 16).
15. SVD works for all matrices, including rectangular/non-square, unlike eigen decomposition (cell 18).
16. A = UΣVᵀ with U left singular vectors, Σ singular values, Vᵀ right singular vectors (cell 19).
17. SVD decomposes a transformation into rotation/reflection → axis-wise scaling → rotation/reflection (cell 20).
18. Every linear transformation can be interpreted geometrically through these three stages (cell 20).
19. Singular values indicate importance of directions, energy captured, and information strength (cell 21).
20. Larger singular value → more important structure; smaller → the source claims "likely noise" (cell 21; softened in v2 to "can carry less dominant structure or noise").
21. SVD is powerful via noise reduction, compression, latent feature extraction, and numerical stability (cell 21).
22. σᵢ = √(λᵢ(AᵀA)) (cell 22; the source's unbalanced parenthesis is a typo, dispositioned).
23. SVD applications: PCA, embedding compression, latent semantic analysis, image compression/denoising, topic modeling, matrix factorization, low-rank adaptation / efficient fine-tuning (cells 22–24).
24. PCA seeks directions of maximum variance and minimum redundancy, projecting high-dimensional data into fewer dimensions (cell 25).
25. PCA starts from the covariance matrix (1/n)XᵀX (cell 26).
26. PCA computes eigenvectors of the covariance matrix and its largest eigenvalues; principal components are the highest-variance, most informative directions (cell 27).
27. PCA is fundamentally SVD on centered data: for mean-centered X = UΣVᵀ, columns of V are principal directions and singular values carry variance information (cells 27, 32).
28. Principal components are ordered by descending eigenvalue (cell 29).
29. PCA workflow: center → covariance → eigenvectors/SVD → keep top-k → project (cell 30).
30. PCA applications: face recognition, word-embedding reduction, risk factor analysis, gene expression compression (cell 31).
31. Low-rank approximation replaces the full A = UΣVᵀ by A_k = U_kΣ_kV_kᵀ using only top-k singular values (cell 34).
32. Real-world data has redundancy, hidden structure, correlated features, so large matrices can often be approximated with few components (cell 34).
33. Approximation error depends on the discarded singular values; lower discarded values → better approximation (cell 34).
34. Recommender systems factor a user–item matrix R ≈ UVᵀ learning latent user preferences and hidden item features (Netflix, Amazon, Spotify) (cell 36).
35. Image compression stores only top singular values with minimal quality loss (cell 36).
36. NLP/LLM systems compress transformer embeddings, word vectors, and attention matrices; used in efficient LLM serving and LoRA fine-tuning (cell 36).
37. Modern AI relies on low-rank structure, latent spaces, compressed representations — deep learning, transformers, recommenders, generative AI (cell 38).
38. High-dimensional observations often emerge from lower-dimensional latent variables — one of the deepest ideas in generative AI, representation learning, world models (cell 40).

## Prerequisites and relationships

Full dependency chain (source-order repairs in brackets):

matrix and vector → matrix–vector product as transformation [FOUNDATION bridge] → eigenvector/eigenvalue → spectrum → characteristic equation [requires determinant, identity matrix — FOUNDATION bridges] → diagonalization [requires linear independence, matrix inverse — bridges] → matrix powers → transpose [bridge] → AᵀA eigenvalues → singular values → SVD (U, Σ, V) → geometric three-stage reading → mean-centering and variance [bridges] → covariance matrix → PCA (eigenvectors of C; = SVD of centered X) → rank [bridge] and truncation → low-rank approximation A_k → applications (compression, denoising, recommenders, LoRA) → latent spaces.

Source use-before-define cases flagged for repair: "Unlike eigen decomposition" in cell 18 appears before SVD is defined (repaired: the comparison is taught after both concepts exist); the applications table (cell 24) names PCA/LSA before they are taught (repaired: each name is bridged at first mention and mechanisms precede application names); det(A−λI)=0 uses determinant and identity matrix before the source defines them (repaired with FOUNDATION bridges); "geometric multiplicity = algebraic multiplicity" (cell 15) is stated without definitions (repaired with a plain-language equivalence: "enough independent eigenvectors to fill P"); cell 36's "4R≈UVᵀ" is a typo for R ≈ UVᵀ (dispositioned, corrected in the lesson with provenance tag).

Visual conventions taught before first use: vectors drawn as arrows from the origin; a transformation drawn by mapping a unit circle/points; color legend swatches for every multi-entity canvas.

## Examples, non-examples, and misconceptions

**Examples (all anchored):** diag(2,3) eigenvectors [1,0],[0,1] (cell 6); A¹⁰⁰ = PD¹⁰⁰P⁻¹ (cells 12, 14); singular values as direction importance (cell 21); PCA workflow steps (cell 30); user–item factorization R ≈ UVᵀ (cell 36). Constructed examples added for v2 (labeled `constructed example`): A = [[3,1],[0,2]] diagonalization with P = [[1,1],[0,−1]] and A⁵ = [[243,211],[0,32]]; full numeric SVD of A = [[2,1],[1,2]] with σ = (3,1) and uᵢ = vᵢ = (1,±1)/√2; a 10-point centered dataset whose live-computed first principal direction retains ≈86% of variance; a 4×3 ratings matrix (two taste groups) whose rank-1 truncation retains ≈85% of the energy.

**Non-examples:** a vector that rotates under A is not an eigenvector; a non-diagonalizable matrix (deficient eigenvectors) cannot fill P; a rectangular matrix has no eigen decomposition but does have an SVD; keeping arbitrary entries of A is not rank-k truncation.

**Misconceptions (each with the wrong answer a holder would give):**
1. "Every vector is an eigenvector because matrices scale things" → chooses Yes for [1,1] with diag(2,3).
2. "The eigenvalue is an entry of the matrix" → reads λ off A's diagonal in general.
3. "det(A−λI)=0 means det(A)=0" → treats the equation as a statement about A alone.
4. "Diagonalization is repeated multiplication" → computes A·A·… instead of PDⁿP⁻¹.
5. "Every matrix is diagonalizable" → assumes P always exists.
6. "SVD only works for square matrices" → denies rectangular SVD.
7. "Singular values can be negative" → treats σᵢ like eigenvalues of A.
8. "σᵢ are eigenvalues of A" → equates the two spectra directly.
9. "Smaller singular values are always noise" → treats the source's "likely noise" as a law (softened per ambiguity below).
10. "PCA picks the direction with the largest mean" → confuses centering with mean-maximization.
11. "PCA works the same on uncentered data" → skips Step 1 of the workflow.
12. "Singular values are the variances" → misses the σᵢ²/n relation (variance along component i = σᵢ²/n under 1/n covariance).
13. "Rank-k means keeping k arbitrary matrix entries" → misunderstands truncation.
14. "Rank-k compression preserves every detail" → ignores discarded-σ error.
15. "Latent factors are directly observable features" → misses the hidden-cause meaning.

## Ambiguities, gaps, and assumptions

- The source gives no numeric SVD; v2 supplies the constructed A = [[2,1],[1,2]] example and marks it `constructed example` (closes the EVAL-2026-0011 gap).
- "Smaller singular value → likely noise" (cell 21) is softened to "can carry less dominant structure or noise"; no universal noise claim is made.
- The source's Σ is written informally without stating nonnegativity or descending order; the lesson states both explicitly (bridge, flagged).
- Cell 10 duplicates det(A−λI)=0 and cell 36's "4R≈UVᵀ" is a typo; both dispositioned as transcription artifacts, corrected with tags.
- The source's variance claim is qualitative ("singular values = variance information"); v2 states the precise relation variance along component i = σᵢ²/n for centered data with 1/n covariance (supplemental, labeled).
- The applications lists (cells 22–24, 31, 36, 38) are mechanism-anchored in the lesson: each application name is introduced only after the mechanism it uses, with one-line bridges (LSA, LoRA, transformers, diffusion models) per the zero-jargon rule.
- Assumption: the learner has taken AIML-4 Class 1 (linear algebra foundations: vectors, dot products, matrix multiplication); the artifact links back to the governed v10 lesson where relevant.

## Review and acceptance criteria

All 40 source cells dispositioned in the coverage matrix; every major term defined before use; every formula with a per-symbol key; live-computed demonstrations (eigen alignment, powers, SVD stages, PCA projection, rank-k energy) rather than hard-coded readouts; the constructed numeric SVD is present and verified; misconceptions appear as distractors with per-miss feedback and at most one callout per unit.

## Conformance checklist (depth-calibration contract)

- [x] ≥ 1 anchored atomic claim per concept (38 claims across 16 concepts)
- [x] Full dependency graph covering every prerequisite and flagging every source use-before-define case
- [x] ≥ 1 diagnosed misconception per major concept with clear wrong-answer definitions (15 misconceptions)
- [x] Every source example anchored to cell
- [x] ≥ 1 non-example per conceptual distinction the source draws
