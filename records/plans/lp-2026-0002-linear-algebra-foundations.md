# LP-2026-0002: Learning plan for linear algebra foundations, redesign (AIML-4 Module 2)

**Status:** Reviewed
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)
**Concept model:** [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) (reused unchanged — dependencies are unchanged; this plan changes *teaching order* and *pedagogy*, which belong to the plan layer)
**Supersedes:** [LP-2026-0001](lp-2026-0001-linear-algebra-foundations.md) for new generation work; LP-2026-0001 remains the plan of record for candidates CAN-2026-0001/0002
**Target learner and prerequisites:** AIML-4 learner relearning Module 2 after a poor first pass; comfortable with basic algebra and 2D coordinates; does **not** reliably know terms such as vector, scalar, linear combination, cosine, transpose, or matrix inverse
**Source and claim links:** [SRC-2026-0001](../sources/SRC-2026-0001-aiml-4-module-02.md); all claims anchored in CM-2026-0001 §Atomic claims; added bridges are labeled Foundation/Supplemental

## Measurable learning outcomes

By the end, the learner can:

1. Classify an ML quantity as scalar, vector, or matrix and state the rows=samples / columns=features reading. (Claims 1–3)
2. Expand a summation by hand and compute small sums; read f: Rⁿ → R as "vector in, number out". (Claims 5, 4)
3. Read the linear model as a weighted sum Σ wᵢxᵢ + b and, after Unit 5, as the dot product wᵀx + b. (Claims 6, 14)
4. Compute 2D linear combinations; state whether two vectors span the plane; define basis and dimension; diagnose redundancy. (Claims 9–13)
5. Compute L1 and L2 norms and state one ML use of each. (Claim 15)
6. Compute a dot product by hand; interpret its sign; explain the magnitude confound and why cosine similarity exists. (Claim 14; extension)
7. Compute a 2D projection; verify e·y = 0 and x̂ + e = x. (Claims 17–18)
8. State the least-squares problem, minimize-squared-error objective, and normal equation; state the invertibility condition (full column rank). (Claims 19, 25–26)
9. Interpret a 2×2 matrix-vector product geometrically; compute it row-wise; explain why AB ≠ BA. (Claims 20–21)
10. Test 2D independence with the area test; connect rank to multicollinearity and to (AᵀA)⁻¹ existing. (Claims 25–26)
11. **Explain** (constructed response, not selection): why a vector needs fixed order; what "span the plane" means; why the magnitude confound breaks raw dot-product similarity; why duplicate features break naive least squares; why a prediction is a linear combination.

Outcome 11 is the deliberate addition over LP-2026-0001: recognition-only assessment was the diagnosed gap across all three prior variants.

## Sequence and rationale

The source's seven-part order contains one true dependency violation (the linearity proof of the dot product appears in Part 1, before the dot product exists in Part 3) and several use-before-define cases (wᵀx + b, xᵀ, (AᵀA)⁻¹, eigenvectors). Teaching order is therefore re-derived from the dependency chains in CM-2026-0001, and every deviation from lecture order is labeled in the artifact:

1. **Quantities** (scalar → vector → matrix): the class's order, kept; adds the data/arrow dual view of vectors.
2. **Compact math** (Σ → transpose-as-tool → functions → linear model as *weighted sum*): transpose and the weighted-sum framing are taught here so that wᵀx is legal later. The linear model is deliberately introduced *without* dot-product notation.
3. **Combining vectors** (add/scale → linear combination → span → basis → dimension): the geometry chain.
4. **Measuring** (L2 then L1): length before comparison.
5. **Comparing** (dot product → cosine bridge → sign/orthogonality → the wᵀx reveal → optional linearity proof): the class's Part 1 proof moves here, where it is legal; the wᵀx reveal closes the loop opened in Unit 2.
6. **Projection → decomposition → least squares**: the source's stated climax; inverse is bridged minimally and the invertibility condition is forward-linked to Unit 8.
7. **Matrices as transformations** (Ax → grid warp → AB≠BA → I, ᵀ, A=Aᵀ, eigenvector one-line extension).
8. **Independence → rank → multicollinearity**, closing the Unit 6 loop ((AᵀA)⁻¹ ⟺ full column rank).
9. **Synthesis + interleaved mastery check.**

Determinants are deliberately *not* taught; 2D independence uses the scaled-copy/area test (named as the determinant only in passing). Eigenvectors get one extension sentence so the Part 7 table is not dangling.

## Teaching strategy and cognitive-load choices

- **Dependency rule:** never use an unexplained concept; prerequisites get a Foundation block at point of need (cos θ primer, transpose flip, inverse bridge).
- **Unit loop:** Learn → Predict → Explore → Practice → Check → Connect. Prediction gates (commit before the canvas unlocks) on the three highest-value reveals (span collapse, opposite-direction dot product, projection leftover).
- **Faded worked examples:** three-rung ladders (full → completion → independent with tiered never-auto-opening hints) for the four computational skills: Σ, norms, dot product, projection.
- **Dual coding:** every canvas pairs with a live symbolic readout; self-verifying readouts (e·y = 0, x̂ + e = x) carry the invariants.
- **Retrieval over recognition:** every unit check includes ≥1 constructed response (numeric entry or explain-in-words with model-answer reveal); mastery check interleaves units and includes a transfer item (embedding search) and an error-identification item (debug-the-math).
- **Confidence calibration:** sure/think/guess tags on mastery items; confident misses are flagged as highest-value events and routed to the review list.
- **Layered content:** every block labeled Class core / Foundation / Deep dive / ML link / Extension plus source/constructed/supplemental provenance tags, so added material is never confusable with class material.
- **Persistence for spacing:** progress and weak topics in localStorage (local only); the review card explicitly invites next-day re-testing.

## Assessment and evidence of learning

- 8 unit checks (21 radio items, 12 numeric blanks, 3 explain-in-words), each with rule-explaining feedback per item; 3 prediction gates; 4 faded ladders; 1 debug-the-math; 1 matching warm-up; 10-item interleaved mastery check (recall/compute/reasoning/transfer/explain) with confidence tags.
- Mastery items do not repeat worked examples (per the owner's brief §20).
- No scores are transmitted; all state is local; no efficacy claim is made or implied.

## Accessibility and inclusion intent

- Semantic landmarks, skip link, logical heading order, keyboard-operable native controls; no drag-only interaction.
- Every canvas has role="img", an aria-label, and an adjacent text readout carrying the same numbers; live regions are off by default to prevent slider chatter (v3 defect), readable on demand via aria-describedby.
- Color never the sole encoder (labels, dashes, text); prefers-reduced-motion honored; print stylesheet replaces canvases with default-state text notes.
- Plain-language restatement precedes formalism; every formula symbol is named in a symbol key.

## Acceptance criteria and review boundary

- Renders from file:// with zero network requests; JS passes node --check; all widget math machine-recomputed; structural checks (duplicate IDs, tag balance, reference integrity) clean.
- Every factual statement traces to CM-2026-0001 claims or is labeled Foundation/Supplemental/constructed.
- Reviewed in a non-independent solo-operator pass (see [EVAL-2026-0002](../evaluations/eval-2026-0002-linear-algebra-foundations-v4.md)); sufficient for a Stage 1 private pilot, insufficient for public release.
