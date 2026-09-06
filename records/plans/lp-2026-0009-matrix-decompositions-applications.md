# LP-2026-0009: Learning plan for matrix decompositions and applications

**Status:** Reviewed  
**Supersedes / iteration position:** Iteration 1 — original  
**Owner:** Repository maintainer  
**Concept model:** [CM-2026-0008](../concepts/cm-2026-0008-matrix-decompositions-applications.md)  
**Target learner and prerequisites:** AIML-4 learner comfortable with algebra, vectors, and matrix multiplication; no prior decomposition theory  
**Source and claim links:** [SRC-2026-0002](../sources/src-2026-0002-matrix-decompositions-applications.md)

## Measurable learning outcomes

The learner can: identify an eigenpair; explain why diagonalization makes powers cheap; describe the three stages of SVD; connect centered-data SVD to PCA; choose a rank-k truncation and explain its information tradeoff; and connect each mechanism to one honest ML use.

## Sequence and rationale

1. Invariant directions: teach the equation Av=lambda v and a live 2x2 example.
2. Diagonalization: show why diagonal powers are simple before discussing P D P^-1.
3. SVD: introduce input directions, scales, and output directions, then rectangular-matrix reach.
4. PCA: center data, define covariance/variance, and pay off the SVD connection.
5. Low rank: truncate singular components and connect the mechanism to compression, denoising, and latent factors.

## Teaching strategy and cognitive-load choices

The lesson uses one visual metaphor consistently: a transformation has directions and strengths. Signature visuals are an eigenvector scale readout, a diagonal-power calculator, an SVD three-stage strip, a PCA variance slider, and a rank-k energy meter. Reveal arc: the eigen-direction idea opens in Unit 1 and pays off in PCA; SVD opens the decomposition language and pays off in low-rank compression. One callout per unit names the highest-risk misconception. Faded ladders cover eigenpair checking, diagonal powers, and singular-value energy. Explain-in-own-words items live in Units 2 and 4, with a transfer item in mastery.

Calibration uses [BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) as the active depth exemplar while reducing scope to the supplied source.

## Assessment and evidence of learning

Each unit has a diagnostic choice or bounded numeric check with rule-based feedback. The mastery check interleaves five fresh items: eigenpair reasoning, diagonal power computation, SVD interpretation, PCA transfer, and low-rank error identification. No open textareas are used.

## Accessibility and inclusion intent

Native controls are keyboard-operable; SVG visualizations have text equivalents; color is paired with labels; reduced motion disables transitions; print CSS exposes the explanatory text and hides controls.

## Acceptance criteria and review boundary

Pass strict candidate verification, mathematical recomputation, dependency-order read-through, structural inspection, browser load and interaction checks at 320/640/1024px, and repository checker. Status remains private-pilot-complete and non-independent.

## Conformance checklist

- [x] Benchmark cited
- [x] Depth pass complete for every unit
- [x] Three faded computational ladders planned
- [x] Two explain-in-own-words items allocated
- [x] Reveal arcs name their payoff units
