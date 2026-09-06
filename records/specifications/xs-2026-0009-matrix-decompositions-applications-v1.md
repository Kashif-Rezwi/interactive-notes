# XS-2026-0009: Interactive notes candidate matrix decompositions v1

**Status:** Approved  
**Approval scope:** Stage 1 governed generation  
**Supersedes / iteration position:** Iteration 1 — original  
**Source concept model:** [CM-2026-0008](../concepts/cm-2026-0008-matrix-decompositions-applications.md)  
**Learning plan:** [LP-2026-0009](../plans/lp-2026-0009-matrix-decompositions-applications.md)  
**Target learner:** AIML-4 student with basic algebra and matrix multiplication  
**Artifact family:** Single-file offline HTML

## Learner problem and teaching strategy

Turn a dense agenda into an explain-before-use path. Each unit contains Learn, Predict or Explore, Practice, Check, and Connect sections. The page uses one accent and high-contrast semantic states.

## Content and evidence map

U1 cells 3–12 eigenpairs/spectrum; U2 cells 13–17 diagonalization; U3 cells 18–25 SVD; U4 cells 26–29 PCA; U5 cells 30–40 low rank and applications. Agenda cells 1–2 orient the page. No source cell is silently dropped.

## Interaction and feedback specification

- `eigen-scale`: sliders lambda and vector length; goal verify Av=lambda v; bounded [-3,3]; text readout gives both sides.
- `power-calc`: integer power n and diagonal entries; goal compute D^n; bounded n 1–8; live result.
- `pca-variance`: slider for retained components k and singular-value pair; goal compare retained energy; bounded k 1–2; labeled SVG bar chart and numeric equivalent.
- Prediction gate: radio choice before revealing whether an arbitrary vector is an eigenvector.
- Ladders: eigenpair check, diagonal power, retained-energy ratio. Hints are hidden until activated.

All range inputs use `.ctrl-grid > .slider-control > .slider-head/.slider-track`; choices use `.option-stack > .option-item`. There are no canvases in this candidate; SVG has text equivalents.

Concept map nodes: eigenpair → diagonalization; eigenpair → SVD intuition; SVD → PCA; SVD → low-rank approximation; PCA → variance explanation; low-rank → compression/denoising/latent factors.

## Formula manifest

| Formula ID | Name | Equation | Symbol key | Unit |
|---|---|---|---|---|
| EQ-001 | Eigenpair | `Av = lambda v` | A matrix; v vector; lambda scale | U1 |
| EQ-002 | Characteristic equation | `det(A - lambda I) = 0` | det determinant; I identity | U1 |
| EQ-003 | Diagonalization | `A = P D P^-1` | P eigenvectors; D eigenvalues | U2 |
| EQ-004 | SVD | `A = U Sigma V^T` | U output directions; Sigma scales; V input directions | U3 |
| EQ-005 | Singular/eigen link | `sigma_i = sqrt(lambda_i(A^T A))` | sigma singular value; lambda eigenvalue | U3 |
| EQ-006 | Covariance | `C = (1/n) X^T X` | X centered data; n samples | U4 |
| EQ-007 | Rank-k approximation | `A_k = U_k Sigma_k V_k^T` | k retained components | U5 |

## Term definition registry

| Term | First appearance | Definition | Glossary |
|---|---|---|---|
| eigenvector | U1 | Direction preserved by a transformation | complete |
| eigenvalue | U1 | Scale applied to an eigenvector | complete |
| spectrum | U1 | Set of eigenvalues | complete |
| diagonalization | U2 | Rewriting with eigenvector coordinates | complete |
| singular value | U3 | Nonnegative directional scale in SVD | complete |
| SVD | U3 | Three-stage decomposition valid for all matrices | complete |
| covariance | U4 | Pairwise variation after centering | complete |
| PCA | U4 | Ordered variance-maximizing projection | complete |
| rank | U5 | Number of independent directions retained | complete |
| latent factor | U5 | Hidden lower-dimensional cause | complete |

## Acceptance criteria

Strict mechanical verification passes; formulas have symbol keys; glossary targets resolve; no external requests or textareas; browser traces confirm all sliders and checks update.
