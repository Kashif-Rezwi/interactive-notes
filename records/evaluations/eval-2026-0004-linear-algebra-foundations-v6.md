# EVAL-2026-0004: Linear algebra foundations v6 (CAN-2026-0005) — the @0.4.0 comparison evaluation

**Candidate ID/version:** CAN-2026-0005, [`linear-algebra-foundations-v6.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v6.html), SHA-256 `6202f3e9cfbc69075b10019d1fa7265ccf2a0949a2245e244e383e98db5b7dc6`, 170,701 bytes<br>
**Rubric version:** evaluation framework, provisional Stage 1 weights + 2026-08-13 QA-checklist depth items<br>
**Evaluator role/identity:** Repository maintainer (solo Stage 1 operator, Reviewer profile)<br>
**Evaluation mode:** human (script-assisted: recomputation, structural scans, handler-level behavioral simulation, measured contrast)<br>
**Operating scope:** Stage 1 private pilot<br>
**Review independence:** non-independent (author = reviewer)<br>
**Reviewer relationship or limitation:** reviewer authored the artifact; no screen-reader pass performed (artifact evidence only, per framework scoring rule)<br>
**Public-release eligibility:** ineligible (ADR-0003)<br>
**Confidence:** medium-high<br>
**Recommendation:** private-pilot-complete<br>
**Iterations reviewed:** builds = 1 (SHA-256 `6202f3e9…5b7dc6`) ; revision cycles = 0 (ADR-0006)

## Scope and evidence inspected

The single-file artifact; run ledger RUN-20260813-0002; inputs CM-2026-0003 / LP-2026-0004 / XS-2026-0004; the five-audit evidence (commands and outputs in the run ledger's verification section); the three-way depth comparison below (judged against CAN-2026-0003 reference and CAN-2026-0004 @0.3.0 output — the comparison the @0.4.0 card registered as its success criterion). This run doubles as the first governed use of prm-generator-lesson-standard@0.4.0.

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality (hard) | 4.0 | Full canonical anatomy per unit; 3 prediction gates with verified fidelity (hidden manipulable, choice-differentiated feedback — simulated); 4 faded ladders, one per computational skill; 3 explain items (floor ≥2); interleaved 11-item mastery with reasoning/transfer/error-ID and 3-level confidence; 15 named misconceptions surfaced as callouts/gate alerts and encoded as distractors | none open | — | medium-high |
| Factual/mathematical accuracy (hard) | 4.0 | 58/58 independent scripted recomputations PASS; source typos/mangled formulas corrected and flagged; widgets live-computed (handler-level sim), never hard-coded | none open | — | high |
| Source grounding (hard) | 3.5 | 63/63 cells dispositioned (Appendix A); claims anchored per CM-2026-0003; opaque figures (cells 38, 41–42) transcribed, not redistributed — transcription not verifiable against image content | Minor (inherited limitation) | independent figure check | medium |
| Interactivity and agency | 4.0 | 13 goal-directed manipulable widgets (zero static-demo mislabeling — the CAN-2026-0004 class absent); self-verifying readouts (e·y=0, x̂+e=x, live SSE); outlier preset teaches the squared-error mechanism | none open | — | medium-high |
| Accessibility and inclusion (hard) | 3.5 | 20 measured contrast pairs, worst 4.86:1 (AA); semantic landmarks; skip link; native controls; canvas text equivalents via aria-describedby; reduced-motion honored; print notes on all 13 widgets; no-JS readable (gates hidden by JS only) | no screen-reader pass (Minor, declared) | specialist review | medium |
| Visual clarity | 3.5 | Standard token set; badge system; one accent hue; consistent hierarchy; signature visual per central concept (span lattice, city-block norms, warped grid, error squares, rank greying) | none open | — | medium |
| User experience | 3.5 | Orientation unit with branched concept map (18 nodes) + text version, revisited at close; sticky nav dots driven by cleared checks; rule-explaining feedback; localStorage review list with return invitation + reset | none open | — | medium |
| Completeness | 4.0 | All §1.1 required elements present incl. colophon; XS-2026-0004 conformance verified element-for-element (13/13 widgets with declared manipulables, 3/3 gates, 4/4 ladders, glossary 40×6, concept-map edges); every LP reveal arc pays off where named (wᵀx U2→U6; (AᵀA)⁻¹ U8→U9) | none open | — | medium-high |
| Readability | 3.5 | Beginner-fit language; per-symbol formula keys; per-unit ledes; flagged source fixes readable | none open | — | medium |
| Technical feasibility/performance intent | 3.5 | Single file, 170,701 bytes, zero requests, file://-functional; canvases redraw on input; bounded inputs/autoscaling verified at extremes; localStorage degrades gracefully | none open | — | high |

## Weighted result and gate check

Weighted score: (4.0×18 + 4.0×18 + 3.5×10 + 4.0×10 + 3.5×14 + 3.5×8 + 3.5×8 + 4.0×6 + 3.5×4 + 3.5×4) / 100 = 376 / 100 = **3.76**.

Hard gates ≥ 3.5: educational quality 4.0 ✓ · factual/mathematical accuracy 4.0 ✓ · source grounding 3.5 ✓ · accessibility 3.5 ✓. All other dimensions ≥ 3 ✓. Weighted 3.76 ≥ 3.5 ✓. No 0–1 scores; no unassessed dimension; no unresolved Critical defect. **Diagnostically passes; recommendation: `private-pilot-complete`** (public-release eligibility: ineligible — non-independent review, ADR-0003).

## Comparison — the @0.4.0 hypothesis test (prompt evolution loop)

Judged on the 2026-08-13 QA-checklist depth items plus the rubric, per the @0.4.0 card's success criterion ("matches the reference implementation technique-for-technique on the depth bar"). v4/v5 counts from MEM-2026-0004's scripted comparison; v6 counts scripted on the final build.

| Depth item | CAN-2026-0003 (v4, reference) | CAN-2026-0004 (v5, @0.3.0) | CAN-2026-0005 (v6, @0.4.0) |
| --- | --- | --- | --- |
| Size | 178,020 B | 78,026 B (~44%) | **170,701 B (reference band)** |
| Widgets | 12 + matching | 9 | **13 + matching — all manipulable (0 demos badged Explore)** |
| Prediction gates | 3 (hiding, differentiated) | 2 (hollow: visible, answer-independent) | **3 (hiding, differentiated — simulated 41/41)** |
| Faded ladders | 4 | 1 (merged) | **4 (one per skill: Σ, norms, dot, projection)** |
| Check items | ~36 incl. 3 explain | 12, 0 explain; 2 recognition-only checks | **27 unit items incl. per-unit CR, 3 explain; 0 recognition-only checks** |
| Mastery | 10 items, 3-level confidence | 6 items, 2-level | **11 items (9 units + 2), 3-level confidence, confident-miss routing** |
| Glossary | 32 entries × 6 fields | 18 × 3 fields | **40 × 6 fields (240/240)** |
| Concept map | branched dependency graph | linear unit strip | **branched graph, 18 nodes, dashed promise edges, revisited at close** |
| wᵀx reveal arc | set up + paid off | promised, never paid (dangling) | **set up U2, paid off U6 (verified in-order)** |
| Canvas extrema | autoscaling | typed inputs render off-canvas | **bounded/autoscaled; 3 defects caught + fixed in-generation** |

**Verdict: hypothesis supported.** With depth made a spec-level conformance target (CM/LP/XS template floors) and demanded in the prompt (items 10–13), a single governed generation reproduced reference-implementation richness — closing the compliant-minimum collapse (MEM-2026-0004) observed under @0.3.0. The card's fallback lever (XS-level full enumeration) is not needed.

## Five-audit evidence

Audits 1–5 executed per the QA checklist; commands and outputs in RUN-20260813-0002 (verification evidence). Audit 1 matrix in Appendix A below. Audit 2: 58/58 recomputation PASS; canvas extrema driven to bounds (3 in-generation fixes). Audit 3: read-in-order pass clean after labeled repairs R1–R3; all forward promises paid. Audit 4: per-unit constructed-response items named (U1 numeric+explain; U2–U9 numeric; U6 explain; mastery explain); widget manipulability, gate fidelity, glossary shape, concept-map structure, XS conformance, reveal-arc payoff — all verified with named evidence. Audit 5: syntax, zero-dependency, unique-id, wiring, 41/41 behavioral simulation, measured contrast (20 pairs, worst 4.86:1), colophon, print/no-JS — all PASS.

## Defects found and resolved

10 in-generation corrections (enumerated in the run ledger, ADR-0006); none escaped to evaluation. No Major/Critical defects open.

## Disagreement or uncertainty

Scores rest on one source package and non-independent review; the v4↔v6 richness judgment is the owner's, corroborated by scripted counts but not by a learner pilot. Screen-reader behavior is asserted from markup evidence, not measured.

## Non-negotiable blockers

None. (No false claims, broken core tasks, access barriers, or provenance issues found.)

## Reviewer sign-off

Non-independent solo-operator review, 2026-08-13; release-ineligible by construction (ADR-0003). Scores record verified artifact evidence only.

## Appendix A — Coverage matrix (all 63 cells of SRC-2026-0001)

| Cells | Content | Lesson location | Disposition |
| --- | --- | --- | --- |
| 1–2 | Title, agenda | Page head / U0 | Included; "Scaler" typo corrected + flagged (U2 callout) |
| 3–5 | Scalar | U1 Learn | Included (constructed example added, labeled) |
| 6–7 | Vector + person example | U1 Learn | Included; order-matters beat expanded (M1) |
| 8–10 | Matrix, samples×features | U1 Learn + W1 matrix-shape explorer | Expanded (widget) |
| 11–13 | Functions, linear model | U2 Learn + W3 | Included; weighted-sum framing opens the wᵀx arc; "w T x" typography corrected + flagged |
| 14–15 | Summation | U2 Learn + W2 Σ-expander + ladder L1 | Expanded |
| 16–17 | Notation kit | U2 notation block | Included; "Rn" → ℝⁿ flagged |
| 18–19 | Proof intuition (linearity) | U6 collapsed interview proof | Moved after the dot product (repair R3), labeled; included |
| 20–21 | Vector space | U3 Learn | Included |
| 22 | Linear combination | U3 Learn + W4 | Included; M4 callout added |
| 23–24 | Span | U3 Learn + gate G1 + W4 lattice | Expanded; M5 callout + gate |
| 25–26 | Basis | U4 Learn (after independence) | Re-sequenced (repair R1), labeled; included |
| 27–28 | Dimension | U4 Learn | Included |
| 29–30 | Dot product, both forms | U6 Learn + W7 + gate G2 | Expanded; mangled Σ layout transcribed + flagged; cos θ primer bridged (FOUNDATION) |
| 31–32 | L2/L1 norms | U5 Learn + W6 + ladder L2 | Included; L2 formula typography corrected + flagged |
| 33–34 | Orthogonality | U6 Learn + W7 | Included; M10 callout added |
| 35–37 | Projection definition | U8 Learn + W11 + gate G3 | Expanded |
| 38 | Projection formula (opaque PNG) | U8 formula block | Transcribed from opaque format; figure not redistributed |
| 39 | Projection applications | U8 formula key + Connect | Included |
| 40–43 | Orthogonal decomposition | U8 Learn | Cells 41–42 transcribed from opaque PNG; not redistributed; M12 callout added |
| 44–45 | Least squares + normal equation | U8 Learn + W12 lab | Expanded; duplicated/mangled layout transcribed once; x̂ hat flagged; inverse bridged (FOUNDATION, ad−bc condition, determinant not named) |
| 46–48 | Matrix multiplication, AB≠BA | U7 Learn + W9 comparator | Moved before least squares (repair R2), labeled; expanded |
| 49–50 | Matrix-vector product | U7 Learn + W8 playground | Expanded; columns-as-destinations deep dive added |
| 51–52 | Identity matrix | U7 Learn | Included |
| 53–54 | Transpose | U7 Learn + W10 builder | Expanded (interactive pairing) |
| 55–56 | Symmetric matrix | U7 Learn | Included; eigen-properties pointer labeled EXTENSION |
| 57–59 | Linear independence | U4 Learn (before basis) + W5 zero-hunt | Moved (repair R1), labeled; mangled formula transcribed + flagged |
| 60–61 | Rank | U9 Learn + W13 inspector | Expanded; (AᵀA)⁻¹ loop closure from U8 |
| 62–63 | ML connections table | U10 synthesis table + matching | Expanded with per-row mechanisms; eigenvector row labeled EXTENSION |
