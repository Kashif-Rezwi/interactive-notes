# LP-2026-0008: Learning plan for linear algebra foundations v10 (full-verification reproduction run)

**Status:** Reviewed<br>
**Supersedes / iteration position:** Iteration 5 — supersedes [LP-2026-0007](../plans/lp-2026-0007-linear-algebra-foundations.md) (same unchanged source, same validated teaching order and depth bar; this iteration serves RUN-20260904-0001, the full-verification reproduction run whose objective is to reproduce the validated v9 reference design under the unchanged prompt card @0.6.0 and complete the live rendered-output verification (ADR-0010 Audit 6) that RUN-20260903-0001 could not perform in degraded mode)<br>
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)<br>
**Concept model:** [CM-2026-0007](../concepts/cm-2026-0007-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 student; comfortable with basic algebra and plotting 2-D points; no prior linear algebra assumed (does not reliably know vector, scalar, transpose, cosine, or inverse)<br>
**Source and claim links:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md); all claims anchor per CM-2026-0007; added bridges labeled FOUNDATION, enrichments DEEP DIVE/EXTENSION

## Measurable learning outcomes

By the end, the learner can:

1. Classify an ML quantity as scalar, vector, or matrix, and read a data matrix as rows=samples, columns=features. (Claims 1–9; U1)
2. Expand and evaluate Σ notation, and read f: ℝⁿ → ℝ as "vector in, number out." (Claims 10, 13–14; U2)
3. Read the linear model as a weighted sum w₁x₁+w₂x₂+b and, after U6, as the dot product wᵀx+b — and explain why the two forms are the same. (Claims 11–12, 24; U2 setup, U6 payoff)
4. Compute a 2-D linear combination; decide whether two vectors span the plane; justify with linear independence. (Claims 17–20, 38; U3–U4)
5. Define basis and dimension; diagnose redundancy in a small vector set. (Claims 22–23; U4)
6. Compute L1 and L2 norms by hand and state one ML use of each. (Claims 26–27; U5)
7. Compute a dot product by hand; interpret its sign; explain the magnitude confound and why cosine similarity exists. (Claims 24–25, 28; U6)
8. Reproduce the linearity derivation (x+y)·z = x·z + y·z (interview skill). (Claim 16; U6)
9. Compute a matrix-vector product row-wise; demonstrate AB ≠ BA with computed numbers; interpret a 2×2 matrix as a movement of space. (Claims 33–36; U7)
10. Compute proj_y(x); verify e·y = 0 and x = x̂ + e; fit a least-squares line with the normal equation and interpret SSE; state when (AᵀA)⁻¹ fails. (Claims 29–32; U8, loop closed in U9)
11. Determine the rank of a small matrix and connect low rank to feature redundancy and multicollinearity. (Claims 38–39; U9)
12. **Explain & diagnose** (structured diagnostic assessment): why vector order matters (U1); the magnitude confound (U6); why the normal equation multiplies by Aᵀ (mastery). Standard §5 explain floor: ≥2 lesson-level explain items, here 3, delivered via diagnostic MCQs with detailed model-answer reveals (zero open `<textarea>` fields).

## Sequence and rationale

Teaching order is re-derived from CM-2026-0006 claim dependency chains, repairing the source's 3 dependency defects:

1. **U1 Quantities** (scalar → vector → matrix, cells 3–10): adds the person-example order-matters beat.
2. **U2 Compact math** (Σ → transpose-as-notation → f: ℝⁿ→ℝ → linear model as *weighted sum*, cells 11–17): wᵀx reveal arc (P-15) opens here and pays off in U6.
3. **U3 Combining vectors** (vector space → linear combination → span, cells 20–24): gate G1 (span collapse) on the unit's counterintuitive reveal.
4. **U4 Independence → basis → dimension** (cells 57–59 moved forward — **repair R1** — then cells 25–28): test for "no redundancy" precedes basis.
5. **U5 Measuring** (L2 → L1, cells 31–32): length before comparison, so geometric dot product is legal in U6.
6. **U6 Comparing** (dot product algebraic → cos θ primer (FOUNDATION) → geometric form → orthogonality → **wᵀx payoff** → linearity proof, cells 29–34; proof moved from cells 18–19 — **repair R3**): gate G2 (negative dot product).
7. **U7 Matrices move space** (Ax → grid warp → C=AB, AB≠BA → I, ᵀ, A=Aᵀ, cells 46–56 moved before least squares — **repair R2**): toolkit exists before U8 needs it.
8. **U8 Projection → decomposition → least squares** (cells 35–45): gate G3 (projection leftover); inverse (·)⁻¹ gets minimal FOUNDATION bridge.
9. **U9 Independence → rank → multicollinearity** (cells 60–61): closes U8 loop — (AᵀA)⁻¹ exists iff columns are independent.
10. **U10 Synthesis + mastery**: concept map revisited; cell-63 ML-connections table with per-row mechanisms at learner level; 11-item interleaved mastery check; review list.

## Depth pass table (mandatory fields, MEM-2026-0004)

| Unit | Lede (one line) | Signature visual (P-14) | Reveal arc (P-15) | Misconception callouts | Ladder |
| --- | --- | --- | --- | --- | --- |
| U1 | Every dataset you will ever touch is just three shapes of numbers. | Matrix-shape explorer (m×n grid) | — | M1 order-matters (callout), M2 rows/cols swap (inline) | — |
| U2 | Mathematicians hate writing long sums — so they invented compression. | Σ-expander (terms appearing) | **Opens:** weighted sum → "this has a shorter name, coming in U6" | M3 multiply-instead-of-add (callout) | **L1 Σ-expansion** |
| U3 | Two vectors and a dial for each can paint an entire plane — or just a line. | Span lattice that collapses when parallel | — | M5 any-pair-spans (callout), M4 positive-only scalars (inline) | — |
| U4 | A good team has no redundant member; a basis is exactly that. | Zero-hunt independence tester | — | M6 different-≠-independent (callout), M7 basis-≠-unit/perpendicular (inline) | — |
| U5 | How long is a vector? Two honest answers, two different walks. | L1 city-block path vs L2 straight line | — | M8 signed-entry L1 (callout) | **L2 norms** |
| U6 | One number that tells you whether two vectors agree, disagree, or couldn't care less. | Dot/angle lab with live θ arc | **Pays off:** the U2 weighted sum was wᵀx all along | M9 magnitude confound (callout), M10 zero-vector misreading (inline) | **L3 dot product** |
| U7 | A matrix is a verb: it grabs the plane and moves it. | Warped grid + unit square | — | M11 AB=BA commutativity (callout) | — |
| U8 | When no line fits, geometry picks the least-wrong one. | Squared-error squares + projection shadow | **Closes:** U2's linear model becomes the fitted line | M12 leftover-direction (callout), M13 exact-fit expectation (inline) | **L4 projection** |
| U9 | Redundancy has a number — and it decides whether the normal equation can even run. | Rank inspector (dependent column greys out) | **Closes:** (AᵀA)⁻¹ loop from U8 | M14 rank=dimension (callout), M15 harmless-duplicate (inline) | — |
| U10 | Everything you learned, pointed at machine learning. | Concept map revisited (now fully readable) | All arcs reviewed | Zero callouts (synthesis unit) | — |

## Assessment and evidence of learning

- 9 unit checks (U1–U9): each mixes recall/understanding/application with auto-graded diagnostic MCQs and numeric entry with tolerance. Strictly zero `<textarea>` fields in checks (standard §1.4).
- 3 prediction gates (G1, G2, G3): manipulable hidden until commitment; option-specific feedback quotes learner's choice.
- 4 faded ladders (L1 Σ, L2 norms, L3 dot product, L4 projection): worked → completion → independent with tiered hints.
- Mastery (U10): 11 interleaved items with fresh numbers, 3-level confidence rating, confident-miss routing to local review list.

## Conformance checklist (depth-calibration contract)

- [x] Active benchmark ([BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md)) cited as calibration exemplar
- [x] Depth-pass table complete for every unit (one-line lede, signature visual, reveal arcs with payoff units, disciplined callouts ≤1 per unit)
- [x] One full 3-rung faded ladder planned for each distinct computational skill in the CM (L1 Σ, L2 norms, L3 dot product, L4 projection)
- [x] ≥ 2 explain-in-own-words items with model answer reveals explicitly allocated (3: U1, U6, mastery item 10)
- [x] Every forward promise / reveal arc names its explicit payoff unit (wᵀx → U6; fitted-line arc → U8; (AᵀA)⁻¹ loop → U9)
