# LP-2026-0006: Learning plan for linear algebra foundations v8 (engineering-remediation run)

**Status:** Reviewed<br>
**Supersedes / iteration position:** Iteration 3 — supersedes [LP-2026-0005](../plans/lp-2026-0005-linear-algebra-foundations.md) (same unchanged source, same validated teaching order and assessment intent, re-pinned; the delta of this iteration is not pedagogical — it adds the ADR-0013 canvas-engineering and lesson-standard §10 design-system obligations that [EVAL-2026-0007](../evaluations/eval-2026-0007-linear-algebra-foundations-v4-v7-qa-design-audit.md) showed the previous artifact generation violated, plus its remediation mandate: preserve v7's pedagogical innovations — confidence calibration, per-option gate feedback, transpose explorer, SVG dependency map)<br>
**Owner:** Repository maintainer (solo Stage 1 operator, Creator profile)<br>
**Concept model:** [CM-2026-0005](../concepts/cm-2026-0005-linear-algebra-foundations.md)<br>
**Target learner and prerequisites:** AIML-4 student; comfortable with basic algebra and plotting 2-D points; no prior linear algebra assumed (does not reliably know vector, scalar, transpose, cosine, or inverse)<br>
**Source and claim links:** [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md); all claims anchor per CM-2026-0005; added bridges labeled FOUNDATION, enrichments DEEP DIVE/EXTENSION

## Measurable learning outcomes

By the end, the learner can (carried 1:1 from LP-2026-0005):

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
12. **Explain** (constructed response, not selection): why vector order matters (U1); the magnitude confound (U6); why the normal equation multiplies by Aᵀ (mastery). Standard §5 explain floor: ≥2 lesson-level explain items, here 3.

## Sequence and rationale

The source's seven-part order commits three dependency defects (CM-2026-0005 use-before-define list); teaching order is re-derived from the claim dependency chains and every deviation is labeled in-artifact. Carried 1:1 from LP-2026-0005:

1. **U1 Quantities** (scalar → vector → matrix, cells 3–10): the class's own order, kept; adds the person-example order-matters beat.
2. **U2 Compact math** (Σ → transpose-as-notation → f: ℝⁿ→ℝ → linear model as *weighted sum*, cells 11–17): transpose is taught here as pure notation so wᵀx is legal later; the linear model is introduced *without* dot-product notation — the wᵀx reveal arc (P-15) opens here and pays off in U6.
3. **U3 Combining vectors** (vector space → linear combination → span, cells 20–24): gate G1 (span collapse) on the unit's counterintuitive reveal.
4. **U4 Independence → basis → dimension** (cells 57–59 moved forward — **repair R1** — then cells 25–28): the source defines basis via independence 33 cells before teaching independence; here the test for "no redundancy" precedes the concept that needs it.
5. **U5 Measuring** (L2 → L1, cells 31–32): length before comparison, so the dot product's geometric form is legal in U6.
6. **U6 Comparing** (dot product algebraic → cos θ primer (FOUNDATION) → geometric form → orthogonality → **wᵀx payoff** → linearity proof, cells 29–34; proof moved from cells 18–19 — **repair R3**): gate G2 (negative dot product); the proof sits collapsed as an interview skill.
7. **U7 Matrices move space** (Ax → grid warp → C=AB, AB≠BA → I, ᵀ, A=Aᵀ, cells 46–56 moved before least squares — **repair R2**): the normal equation's full toolkit now exists before U8 needs it.
8. **U8 Projection → decomposition → least squares** (cells 35–45): gate G3 (projection leftover); inverse (·)⁻¹ gets a minimal FOUNDATION bridge (2×2, "when it fails" forward-linked to U9); the squared-error squares are the unit's memorable image.
9. **U9 Independence → rank → multicollinearity** (cells 60–61): closes the U8 loop — (AᵀA)⁻¹ exists iff columns are independent (full column rank).
10. **U10 Synthesis + mastery**: concept map revisited; the cell-63 ML-connections table with per-row mechanisms at learner level; interleaved mastery check; review list.

Determinants and inversion procedures are deliberately not taught (do-not-add tier); 2-D independence uses the zero-hunt combination test. Eigenvectors get one EXTENSION sentence so the cell-63 row is not dangling.

## Teaching strategy and cognitive-load choices

**Dependency rule:** nothing unexplained is load-bearing; bridges (cos θ primer, inverse bridge, unit-vector gloss) are FOUNDATION blocks at point of need.

**Engineering remediation rule (new in this iteration):** the artifact must implement the [canvas engineering standard](../../docs/01-product/canvas-engineering-standard.md) (responsive makeView viewport, DPR scaling, aspect-ratio height, one resize listener per canvas widget, normalized transforms, per-widget declared viewports, .legend-inline on multi-entity canvases, signed-arc angle computation) and the lesson standard §10 design system (pinned tokens, frosted single-line nav with aria-current active state via IntersectionObserver, left-aligned header with metadata chips, descriptive mathematical control labels). These obligations are artifact-level and are specified fully in XS-2026-0006; they change no pedagogy.

**Depth pass (mandatory fields, MEM-2026-0004) — carried 1:1 from LP-2026-0005:**

| Unit | Lede (one line) | Signature visual (P-14) | Reveal arc (P-15) | Misconception callouts | Ladder |
| --- | --- | --- | --- | --- | --- |
| U1 | Every dataset you will ever touch is just three shapes of numbers. | Matrix-shape explorer (m×n grid) | — | M1 order-matters, M2 rows/cols swap | — |
| U2 | Mathematicians hate writing long sums — so they invented compression. | Σ-expander (terms appearing) | **Opens:** weighted sum → "this has a shorter name, coming in U6" | M3 multiply-instead-of-add | **L1 Σ-expansion** |
| U3 | Two vectors and a dial for each can paint an entire plane — or just a line. | Span lattice that collapses when parallel | — | M4 positive-only scalars, M5 any-pair-spans | — |
| U4 | A good team has no redundant member; a basis is exactly that. | Zero-hunt independence tester | — | M6 different-≠-independent, M7 basis-≠-unit/perpendicular | — |
| U5 | How long is a vector? Two honest answers, two different walks. | L1 city-block path vs L2 straight line | — | M8 signed-entry L1 | **L2 norms** |
| U6 | One number that tells you whether two vectors agree, disagree, or couldn't care less. | Dot/angle lab with live θ arc | **Pays off:** the U2 weighted sum was wᵀx all along | M9 magnitude confound (+cosine callout), M10 zero-vector misreading | **L3 dot product** |
| U7 | A matrix is a verb: it grabs the plane and moves it. | Warped grid + unit square | — | M11 AB=BA commutativity | — |
| U8 | When no line fits, geometry picks the least-wrong one. | Squared-error squares + projection shadow | **Closes:** U2's linear model becomes the fitted line | M12 leftover-direction, M13 exact-fit expectation | **L4 projection** |
| U9 | Redundancy has a number — and it decides whether the normal equation can even run. | Rank inspector (dependent column greys out) | **Closes:** (AᵀA)⁻¹ loop from U8 | M14 rank=dimension, M15 harmless-duplicate | — |
| U10 | Everything you learned, pointed at machine learning. | Concept map revisited (now fully readable) | All arcs reviewed | — | — |

**Explain-in-own-words placement (standard §5 floor ≥2):** U1 check (why order matters), U6 check (the magnitude confound), mastery item 10 (why Aᵀ in the normal equation).

**Patterns:** prediction-gated reveals (P-01) ×3 with hidden manipulables and choice-differentiated feedback; faded ladders (P-02) ×4 — one per computational skill (Σ, norms, dot product, projection); goal-directed explorers (P-03); numeric text equivalents everywhere (P-04); concept map early + revisited (P-10); per-unit retrieval checks (P-11); interleaved mastery ≈ units+2 with three-level confidence (P-12); localStorage review list with return invitation (P-13); signature visuals (P-14); reveal arcs (P-15).

**Cognitive load:** one new idea per block; early units decompress notation inline, later units assume it; optional depth (proof, cosine-similarity deep dive) collapsed by default; badges + provenance tags on every block.

## Assessment and evidence of learning

Carried 1:1 from LP-2026-0005:

- 9 unit checks (U1–U9): each mixes recall/understanding/application and includes ≥1 constructed-response item (numeric entry with tolerance, or explain with honest model-answer reveal); every miss states the governing rule; distractors encode M1–M15.
- 3 prediction gates (G1 span collapse, G2 negative dot product, G3 projection leftover); the manipulable stays hidden until commitment; feedback differentiates by the chosen option and references the commitment.
- 4 faded ladders (worked → completion → independent; tiered never-auto-opening hints).
- Mastery (U10): 11 interleaved items = 9 content units + 2 (P-12); includes reasoning (span/basis of parallel pair; AB≠BA in pipelines), transfer (duplicate-feature dataset → what breaks in (AᵀA)⁻¹), error-identification (planted signed-L1 slip), 2 numeric, 1 explain; three-level confidence tags; confident misses route to the review list. **No worked numbers reused** (worked: [3,4] norms, [1,2]·[3,4], proj [2,2]→[4,0], fit on (1,2)(2,3)(3,3)(4,5); mastery uses fresh values).
- No scores leave the device; no efficacy claim is made or implied.

## Accessibility and inclusion intent

Standard §1.1 baseline: semantic landmarks, skip link, logical heading order, keyboard-operable native controls, no drag-only/hover-only interaction; every canvas role="img" + adjacent text equivalent carrying the same numbers; color never sole encoder; prefers-reduced-motion honored; measured WCAG AA contrast; print fallback per interactive; no-JS readable (gated content hidden by JS, never markup); 16 px minimum body text; storage-unavailable degrades gracefully with a visible reset.

## Acceptance criteria and review boundary

LP approved when: every outcome maps to ≥1 assessment item; the sequence passes an empty-taught-set read-through; the depth-pass table is complete for all 10 units; repairs R1–R3 are named with cell anchors. Boundary: approves teaching order, outcomes, assessment intent, and the engineering-remediation obligation only — artifact-level interaction choices belong to XS-2026-0006. Non-independent solo-operator review; sufficient for a Stage 1 private pilot, insufficient for public release.

## Conformance checklist (depth-calibration contract)

- [x] Active benchmark ([BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md)) cited as calibration exemplar — the engineering remediation ports its canvas architecture and design system onto the deeper v6/v7 pedagogy
- [x] Depth-pass table complete for every unit (one-line lede, signature visual, reveal arcs with payoff units, misconception callouts)
- [x] One full 3-rung faded ladder planned for each distinct computational skill in the CM (L1 Σ, L2 norms, L3 dot product, L4 projection)
- [x] ≥ 2 explain-in-own-words items with model answer reveals explicitly allocated (3: U1, U6, mastery item 10)
- [x] Every forward promise / reveal arc names its explicit payoff unit (wᵀx → U6; fitted-line arc → U8; (AᵀA)⁻¹ loop → U9)
