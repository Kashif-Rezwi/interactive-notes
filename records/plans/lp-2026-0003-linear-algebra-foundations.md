# LP-2026-0003: Linear algebra foundations (regeneration test)

**Status:** Reviewed<br>
**Supersedes / iteration position:** Iteration 1 — original (fresh from CM-2026-0002; does not read LP-2026-0001/0002)<br>
**Owner:** Repository maintainer<br>
**Concept model:** [CM-2026-0002](../concepts/cm-2026-0002-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 student; comfortable with basic algebra and plotting 2-D points; no prior linear algebra assumed<br>
**Source and claim links:** SRC-2026-0001; all claims anchor per CM-2026-0002

## Measurable learning outcomes

1. Distinguish scalar/vector/matrix and read a data matrix as samples × features. (U1)
2. Expand and evaluate Σ notation. (U1)
3. Decide whether two 2-D vectors span the plane, a line, and justify via linear independence. (U2)
4. Compute a dot product and a norm by hand; state what its sign/size means. (U3)
5. Reproduce the linearity derivation of the dot product (interview skill). (U3)
6. Multiply 2×2 matrices; demonstrate AB ≠ BA with computed numbers; apply a matrix as a transformation. (U4)
7. Compute proj_b(a) and verify the residual is orthogonal to b. (U5)
8. Fit a least-squares line through the normal equation on 4 points and interpret SSE. (U5)
9. Determine the rank of a small matrix and connect low rank to feature redundancy. (U6)
10. Map each concept to its ML mechanism (synthesis). (U7)

## Sequence and rationale

U0 Orientation + concept map → U1 Building blocks (cells 3–17) → U2 Spaces: vector space, linear combination, span (20–24), **linear independence (57–59, moved, repair R1)**, basis (25–26), dimension (27–28) → U3 Dot product & norms (29–34), **interview proof skill (18–19, moved, repair R3)** → U4 Matrices & transformations (46–56, **moved before least squares, repair R2**) → U5 Projections & least squares (35–45) → U6 Rank (60–61) → U7 ML synthesis (62–63) → U8 Mastery + review. Explain-before-use governs every move; each repair is labeled in-artifact.

## Teaching strategy and cognitive-load choices

Canonical anatomy per unit (Learn → Predict → Explore → Practice → Check → Connect). One new idea per block. Prediction gates only on the two most counterintuitive reveals: span collapse (U2) and negative dot product (U3). Faded ladders for the four computational skills: Σ expansion, dot product, norm, projection. Additional-knowledge triage: MUST add = unit vector, 2×2 inverse bridge, cosθ primer (FOUNDATION, labeled); COULD add = eigenvector pointer (EXTENSION, one line); DO NOT add = determinants, full inversion, PCA internals.

## Assessment and evidence of learning

Per-unit checks each include ≥1 constructed-response numeric item with governing-rule feedback. Mastery (U8): 6 interleaved items — numeric dot product [3,−1]·[2,5], numeric norm ‖[1,2,2]‖₂, reasoning (span of parallel vectors), transfer (least squares with an outlier — which quantity changes most), error-identification (a worked AB=BA "proof" with a planted error), explain-in-own-words (why the normal equation needs the transpose). No lesson worked numbers reused. Confidence tags on mastery items; confident misses route to the review list.

## Accessibility and inclusion intent

Standard §1.1 baseline: semantic landmarks, native keyboard-operable controls, canvas text equivalents carrying the same numbers, color never sole encoder, reduced-motion honored, measured AA contrast, print fallback per interactive, no-JS readable (gated content hidden by JS, never by markup).

## Acceptance criteria and review boundary

LP approved when every outcome maps to ≥1 assessment item and the sequence passes an empty-taught-set read-through. Boundary: approves teaching order and assessment intent only; artifact-level interaction choices belong to XS.
