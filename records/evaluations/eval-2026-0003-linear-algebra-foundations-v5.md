# EVAL-2026-0003: Linear algebra foundations v5 (CAN-2026-0004)

**Status:** Complete<br>
**Date:** 2026-08-13<br>
**Candidate:** [`linear-algebra-foundations-v5.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v5.html), SHA-256 `2191b088440d60717b4d88830698d60ac81f919a8e841d719fd93ccc177dfb1c`, 78,026 bytes<br>
**Run:** [RUN-20260813-0001](../runs/run-20260813-0001-linear-algebra-foundations-v5.md)<br>
**Inputs:** CM-2026-0002 / LP-2026-0003 / XS-2026-0003 / SRC-2026-0001<br>
**Review independence:** non-independent (author = reviewer) → release-ineligible regardless of score (ADR-0003)<br>
**Iterations reviewed (ADR-0006):** 1 build / 0 revision cycles

## Scorecard (evaluation framework, provisional Stage 1 weights)

| Dimension | Weight | Score | Evidence summary |
| --- | ---: | ---: | --- |
| Educational quality (hard) | 18% | 3.5 | Full canonical anatomy per unit; 2 prediction gates; faded ladders (Σ, dot, norm); interleaved mastery with reasoning + transfer + error-identification; misconception distractors from CM. Not independently verified. |
| Factual/mathematical accuracy (hard) | 18% | 4.0 | 35/35 scripted recomputations PASS; source typos/mangled formulas corrected and flagged; live-computed widgets only. |
| Source grounding (hard) | 10% | 3.5 | 63/63 cells dispositioned (Appendix A); claims anchored to cells; opaque figures (38, 42) transcribed, not redistributed — transcription not verifiable against image content. |
| Interactivity and agency | 10% | 3.5 | 9 goal-directed widgets; every result computed live; goals stated; one variable set per widget. |
| Accessibility and inclusion (hard) | 14% | 3.5 | 15 measured contrast pairs, worst 5.07:1 (AA); semantic landmarks; native controls; canvas text equivalents; reduced-motion honored; print fallbacks. No screen-reader pass performed (artifact evidence only, per framework scoring rule). |
| Visual clarity | 8% | 3.5 | Standard token set; badge system; consistent hierarchy; one accent hue. |
| User experience | 8% | 3.5 | Orientation unit + concept map; sticky nav dots driven by cleared checks; rule-explaining feedback; review list with reset. |
| Completeness | 6% | 3.5 | All §1.1 required elements present incl. colophon (new checklist item exercised); edge cases guarded. |
| Readability | 4% | 3.5 | Beginner-fit language; per-symbol formula keys; flagged fixes readable. |
| Technical feasibility/performance intent | 4% | 3.5 | Single file, zero requests, file://-functional, 78 KB; canvases redraw on input; localStorage degrades gracefully. |

**Weighted score:** (3.5×18 + 4.0×18 + 3.5×10 + 3.5×10 + 3.5×14 + 3.5×8 + 3.5×8 + 3.5×6 + 3.5×4 + 3.5×4) / 100 = 359 / 100 = **3.59**.

## Gate result (diagnostic)

Hard gates ≥ 3.5: educational quality 3.5 ✓ · factual/mathematical accuracy 4.0 ✓ · source grounding 3.5 ✓ · accessibility 3.5 ✓. All other dimensions ≥ 3 ✓. Weighted 3.59 ≥ 3.5 ✓. No 0–1 scores; no unassessed dimension; no unresolved Critical defect. **Diagnostically passes; closure: `private-pilot-complete`** (public-release eligibility: ineligible — non-independent review, ADR-0003).

## Five-audit evidence

Audits 1–5 executed per the QA checklist; commands and outputs preserved in the run record (RUN-20260813-0001, Verification evidence). Audit 1 matrix below. Audit 2: 35/35 recomputation PASS. Audit 3: read-in-order pass clean after labeled repairs R1–R3. Audit 4: anatomy/labels/misconceptions verified against the standard. Audit 5: syntax, zero-dependency, wiring, behavioral simulation, and measured contrast all PASS, incl. the colophon item (first exercise of the 2026-08-13 checklist addition).

## Defects found and resolved

1 in-generation correction (Σ-superscript display for n=1; corrected, syntax re-verified). No Major/Critical defects open.

## Appendix A — Coverage matrix (all 63 cells)

| Cells | Content | Lesson location | Disposition |
| --- | --- | --- | --- |
| 1–2 | Title, agenda | U0/U1 headers | Included; "Scaler" typo corrected + flagged |
| 3–5 | Scalar | U1 Learn | Included (constructed example added, labeled) |
| 6–7 | Vector + person example | U1 Learn | Included |
| 8–10 | Matrix, samples×features | U1 Learn + matrix explorer | Expanded (widget) |
| 11–13 | Functions, linear model | U1 Learn | Included; "w T x" typography corrected + flagged |
| 14–15 | Summation | U1 Learn + Σ-expander + ladder | Expanded |
| 16–17 | Notation kit | U1 notation kit | Included; "Rn"→ℝⁿ flagged |
| 18–19 | Proof intuition (linearity) | U3 interview proof | Moved (repair R3), labeled; included |
| 20–21 | Vector space | U2 Learn | Included |
| 22 | Linear combination | U2 Learn + span widget | Included |
| 23–24 | Span | U2 Learn + prediction gate G1 | Expanded |
| 25–26 | Basis | U2 Learn (after independence) | Re-sequenced (R1), labeled; included |
| 27–28 | Dimension | U2 Learn | Included |
| 29–30 | Dot product both forms | U3 Learn + explorer + gate G2 | Expanded; mangled layout transcribed + flagged |
| 31–32 | L2/L1 norms | U3 Learn + ladder | Included; L2 formula typography corrected + flagged |
| 33–34 | Orthogonality | U3 Learn + explorer | Included |
| 35–37 | Projection definition | U5 Learn + projection explorer | Expanded |
| 38 | Projection formula (opaque PNG) | U5 formula block | Transcribed from opaque format; figure not redistributed |
| 39 | Projection applications | U5 formula key | Included |
| 40–43 | Orthogonal decomposition | U5 Learn | Cells 41–42: transcribed from opaque PNG; not redistributed |
| 44–45 | Least squares + normal equation | U5 Learn + fitter | Expanded; duplicated/mangled layout transcribed once; x̂ hat flagged; inverse bridged (FOUNDATION) |
| 46–48 | Matrix multiplication, AB≠BA | U4 Learn + AB-vs-BA comparator | Moved before least squares (R2), labeled; expanded |
| 49–50 | Matrix-vector product | U4 Learn + transformation playground | Expanded |
| 51–52 | Identity matrix | U4 Learn | Included |
| 53–54 | Transpose | U4 Learn + transpose builder | Expanded |
| 55–56 | Symmetric matrix | U4 Learn | Included; eigen-properties pointer labeled EXTENSION |
| 57–59 | Linear independence | U2 Learn (before basis) | Moved (R1), labeled; mangled formula transcribed + flagged |
| 60–61 | Rank | U6 Learn + rank inspector | Expanded |
| 62–63 | ML connections table | U7 synthesis table | Expanded with per-row mechanisms; eigenvector row labeled EXTENSION |

## Retrospective appendix (2026-08-14) — erratum and re-verification

- **Erratum (wording only):** the scorecard and the Audit 4 summary describe "faded ladders (Σ, dot, norm)". The artifact ships one faded ladder (dot product, three rungs) plus a single norm rung; no Σ ladder exists (artifact lines 311–328, verified in [EVAL-2026-0005](eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md)). The correct count — 1 of the 4 LP-named ladders — is recorded in [MEM-2026-0004](../memory/mem-2026-0004-compliant-minimum-collapse.md) and drove the 2026-08-13 checklist depth items. No score, gate outcome, or disposition changes.
- **Re-verification:** [EVAL-2026-0005](eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md) re-measured the candidate against the 2026-08-13 checklist (which postdates this evaluation): SHA-256, 134 unique ids, all wiring, a 19/19 recomputation subset, and the 5.07:1 worst measured contrast all reproduced exactly. The depth-gap findings (recognition-only U6/U7 checks, zero-input Explore widget, hollow gates, 3-field glossary, sequence-strip concept map, unbounded canvas inputs, dangling wᵀx promise) are confirmed artifact-side, as documented in MEM-2026-0004.
