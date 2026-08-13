# LP-2026-0001: Learning plan for linear algebra foundations (AIML-4 Module 2)

**Status:** Reviewed<br>
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)<br>
**Concept model:** [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 learner beginning Module 2; comfortable with basic algebra and 2D coordinates; no prior linear algebra assumed<br>
**Source and claim links:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md); all claims anchored in CM-2026-0001 §Atomic claims

## Measurable learning outcomes

By the end, the learner can:

1. Classify a given ML quantity as scalar, vector, or matrix and state its shape interpretation (samples × features). (Claims 1–3)
2. Expand a summation expression and read wᵀx + b as a linear model of a feature vector. (Claims 5–6)
3. Compute a dot product by hand and interpret its sign as similar, orthogonal, or opposite direction. (Claim 14)
4. Compute L1 and L2 norms of a small vector and name one ML use of each. (Claim 15)
5. Determine whether two vectors are orthogonal and whether a small set is linearly independent. (Claims 16, 25)
6. Compute the projection of one 2D vector onto another and decompose a vector into x̂ + e. (Claims 17–18)
7. State the least-squares problem and the normal equation, and connect them to linear regression. (Claims 19, 27)
8. Interpret a 2×2 matrix-vector product as a geometric transformation and explain why matrix order matters. (Claims 20–21)
9. Match each core concept to its ML application from the source's connection table. (Claim 27)

## Sequence and rationale

Follow the source's seven-part order (cells 3–63), which already respects the dependency chains in CM-2026-0001:

1. **Notation first** (Parts 1): learners cannot read later formulas without scalar/vector/matrix, summation, and transpose/norm notation.
2. **Geometry second** (Part 2): span, basis, and dimension give the mental model that makes rank and independence meaningful later.
3. **Operations third** (Part 3): dot product and norms are the computational primitives for projection and least squares.
4. **Projections and least squares fourth** (Part 4): the module's stated climax ("Extremely Important", cell 44); placed after its prerequisites.
5. **Matrices fifth** (Part 5): transformations generalize the vector intuition and prepare the normal equation's notation.
6. **Rank and independence sixth** (Part 6): consolidates basis/dimension from Part 2 with matrix language from Part 5.
7. **ML connections last** (Part 7): a synthesis map plus interview-style proof practice (cell 19), rewarding retention rather than introducing new material.

## Teaching strategy and cognitive-load choices

- **Dual coding:** every formula pairs with a manipulable visual (vectors on a plane, projection diagram, transformation grid) so symbolic and geometric channels reinforce each other.
- **Worked example → guided practice → check:** each section presents the source definition, a worked numeric example (labeled constructed where not from the source), an interactive manipulation, and a two-to-three-question self-check with immediate feedback.
- **Chunking by part:** seven collapsible sections with a persistent progress indicator; no section mixes two dependency chains.
- **Germane load focus:** interactives isolate one variable at a time (e.g., projection explorer changes only the target vector before offering free play).
- **Interview skill:** the linearity-of-dot-product proof (cell 19) is presented as an optional step-through reveal to keep it available without forcing proof reading on first pass.

## Assessment and evidence of learning

- Embedded self-checks per section mapped to outcomes 1–9; each gives correctness feedback plus the governing source-grounded rule.
- Interactive widgets produce immediate causal feedback (numeric readouts and canvas updates), serving as formative assessment.
- No summative score is transmitted or stored; this private-pilot candidate has no analytics, and no learning-efficacy claim is made or implied.

## Accessibility and inclusion intent

- Semantic landmarks, skip link, and keyboard-operable controls for every interactive (sliders and buttons, no drag-only interactions).
- Every canvas has a text equivalent: live numeric readouts and an aria-described summary, so no information is canvas-only.
- Color is never the sole encoder; direction/sign states also use labels and shapes.
- Respects `prefers-reduced-motion`; no autoplaying animation.
- Plain-language restatements accompany each formal definition; reading level targets an early undergraduate technical audience.

## Acceptance criteria and review boundary

- Each outcome traces to at least one CM-2026-0001 atomic claim, and each claim used by the experience specification traces to SRC-2026-0001 cells.
- All nine outcomes are exercised by at least one self-check or interactive in the candidate.
- Reviewed in a non-independent solo-operator pass (see [EVAL-2026-0001](../evaluations/eval-2026-0001-linear-algebra-foundations-v2.md)); sufficient for a Stage 1 private pilot, insufficient for public release.
