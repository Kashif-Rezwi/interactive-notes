# EVAL-2026-0008: Linear algebra foundations v8 (CAN-2026-0007) — engineering remediation evaluation

**Candidate ID/version:** CAN-2026-0007, [`linear-algebra-foundations-v8.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v8.html), SHA-256 `cdfb2e3fedea86c82898bab479241362d92e931e43ce636b16a8345a98d64ab1`
**Rubric version:** evaluation framework, provisional Stage 1 weights + 2026-08-15 QA-checklist depth items (including ADR-0013 canvas engineering and lesson-standard §10 design-system checks)
**Evaluator role/identity:** Repository maintainer (solo Stage 1 operator, Reviewer profile)
**Evaluation mode:** human (script-assisted: structural, handler-level behavioral simulation, recomputation, provenance measurement, conformance greps); **live browser mode** — `agent-browser` CLI used for rendered-output verification (ADR-0010 Audit 6)
**Operating scope:** Stage 1 private pilot
**Review independence:** non-independent (author = reviewer)
**Reviewer relationship or limitation:** reviewer authored (remediated) the artifact; no screen-reader pass
**Public-release eligibility:** ineligible (ADR-0003)
**Confidence:** medium-high
**Recommendation:** private-pilot-complete
**Iterations reviewed:** builds = 1 (SHA-256 `cdfb2e3fedea86c82898bab479241362d92e931e43ce636b16a8345a98d64ab1`); revision cycles = 0 (ADR-0006)

## Scope and evidence inspected

The single-file artifact; run ledger RUN-20260815-0002; inputs CM-2026-0005 / LP-2026-0006 / XS-2026-0006; standing verifier output (0 failures); recomputation script (64/64 passed); conformance greps (9 resize listeners, 9 canvases, 10 makeView calls, 0 anti-patterns, 25 tokens, 11 legends); behavioral simulation (handler-level edge cases); browser-verification screenshot (live agent-browser, 1024px). This is the first governed use of prompt card @0.5.0 — the comparison run for its pending hypothesis.

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality (hard) | 4.0 | Canonical anatomy reproduced 1:1 from the validated reference (CAN-2026-0006); 3 verified-fidelity prediction gates; 4 faded ladders; ≥1 constructed-response per unit check; 3 explain-in-own-words; 11-item interleaved mastery with 3-level confidence; 15 misconceptions surfaced and encoded as distractors | none open | — | medium-high |
| Factual/mathematical accuracy (hard) | 4.0 | All 64 numeric claims independently recomputed — QA keys, MULTI answers, MAST keys, worked examples (Σ, norms, dot, projection, least-squares m/c/SSE, AB≠BA, gate G2), widget defaults, magnitude-confound examples | none open | — | medium-high |
| Source grounding (hard) | 3.5 | All 63 cells dispositioned; claims anchored per CM-2026-0005; opaque figures (cells 38/41–42) transcribed, not redistributed | Minor (inherited): transcription not verifiable against image content | independent figure check | medium |
| Interactivity and agency | 4.0 | 13 goal-directed manipulable widgets; self-verifying readouts (e·y=0, x̂+e=x, live SSE); degenerate guards on all canvases (zero-vector, collinear, zero-y, dependent presets) | none open | — | medium-high |
| Accessibility and inclusion (hard) | 4.0 | Semantic landmarks, skip link, heading order, keyboard-operable controls; every input has an accessible name (aria-label added to W3/W7/W9/W10/W11/W13 — repaired v7 gap); canvas role="img" + aria-label + readout; color never sole encoder; reduced-motion honored; print stylesheet; readable at 320px | no live screen-reader pass (Minor, declared) | specialist review | medium |
| Visual clarity | 3.5 | Pinned design tokens (25 vars); warm `--paper` palette; antialiased fonts; `.legend-inline` on all 9 canvases; frosted-glass nav with pills and active state; responsive makeView canvas engine renders crisp at all viewport sizes; concept-map SVG retained as documented deliberate variation | Minor (declared): SVG palette uses CAN-2026-0006 categorical colors, not the pinned token set (XS documents this as deliberate) | — | medium-high |
| User experience | 3.5 | Foated single-line nav with completion dots via IntersectionObserver; left-aligned header with metadata chips; rule-explaining feedback on every miss; localStorage review list; 3-level confidence tags with confident-miss routing | no live interaction trace (browser screenshot captured, exercised in handler sim) | — | medium |
| Completeness | 4.0 | XS-2026-0006 conformance verified element-for-element: 13 widgets with declared viewports, 3 gates, 4 ladders, 9 unit checks, matching, 11 mastery items, 40-term 6-field glossary, branched concept map (revisited), review list, colophon, provenance header; 9 makeView calls match XS-specified viewports; 9 resize listeners | none open | — | medium-high |
| Readability | 4.0 | Per-unit ledes, per-symbol formula keys, plain-language meaning + interpretation, badge/provenance tags on every block, mathematical slider labels per §10.4 | none open | — | medium-high |
| Technical feasibility/performance intent | 3.5 | Single file, 180KB, zero external requests, system font stack, canvas redraw on input + resize (9 resize listeners); responsive makeView architecture scales correctly (verified at 320px and 1024px via agent-browser resize) | Minor (observation): file size 180KB vs benchmark 178KB — within target band | — | medium-high |

## Weighted result and gate check

**Weighted score: 3.85 / 4.00** (4.0·18 + 4.0·18 + 3.5·10 + 4.0·10 + 4.0·14 + 3.5·8 + 3.5·8 + 4.0·6 + 4.0·4 + 3.5·4) = (72+72+35+40+56+28+28+24+16+14) = 385 / 100 = **3.85 / 4.00**.

Gate check (diagnostic for a private pilot): all four hard-gate dimensions ≥ 3.5 (Educational 4.0, Factual 4.0, Source 3.5, Accessibility 4.0); no score of 0–1; no unassessed dimension; no unresolved Critical defect. The two Minor observations (inherited figure transcription, documented SVG palette variation) do not block private-pilot closure. Public-release eligibility is ineligible regardless per ADR-0003.

## Disagreement or uncertainty

None material. Live browser verification (Audit 6) was non-degraded for the first time in this candidate lineage — scores on Visual/UX/Technical are based on actual evidence rather than the capped 2.5 of v7's degraded mode.

## Non-negotiable blockers

None at private-pilot scope. No Critical (false claim, broken core task, access barrier, provenance issue) defect found; provenance header matches this run's identity. Canvas engineering contract fully satisfied — all 8 ADR-0013 §7 items pass. Design-system contract fully satisfied — all §10.1–10.4 items verified.

## Reviewer sign-off

`non-independent` review → public-release eligibility `ineligible` (ADR-0003). Disposition: **private-pilot-complete**. No score is a public release decision, benchmark result, or efficacy claim. The @0.5.0 comparison-run hypothesis is **SUPPORTED**: the canvas engineering standard + design-system contract prevented the v7 regression class in this single governed generation.
