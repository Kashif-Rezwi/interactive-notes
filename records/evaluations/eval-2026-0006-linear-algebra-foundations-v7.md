# EVAL-2026-0006: Linear algebra foundations v7 (CAN-2026-0006) — reproduction evaluation

**Candidate ID/version:** CAN-2026-0006, [`linear-algebra-foundations-v7.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v7.html), SHA-256 `1f1427432860471a0b709b52f936f7e27c918c812cabaca06f111e780b2dc1e0`, 170,701 bytes
**Rubric version:** evaluation framework, provisional Stage 1 weights + 2026-08-13 QA-checklist depth items
**Evaluator role/identity:** Repository maintainer (solo Stage 1 operator, Reviewer profile)
**Evaluation mode:** human (script-assisted: structural + handler-level behavioral simulation, recomputation, measured provenance); **degraded mode** — no browser subagent available, so no live rendered-output trace or screenshot contrast re-measurement (ADR-0010 Audit 6)
**Operating scope:** Stage 1 private pilot
**Review independence:** non-independent (author = reviewer)
**Reviewer relationship or limitation:** reviewer authored (reproduced) the artifact; no screen-reader pass; no live browser rendering performed
**Public-release eligibility:** ineligible (ADR-0003)
**Confidence:** medium
**Recommendation:** private-pilot-complete
**Iterations reviewed:** builds = 1 (SHA-256 `1f142743…2dc1e0`); revision cycles = 0 (ADR-0006)

## Scope and evidence inspected

The single-file artifact; run ledger RUN-20260815-0001; inputs CM-2026-0004 / LP-2026-0005 / XS-2026-0005; the standing verifier output (0 failures); the reproduction relationship to the reference candidate CAN-2026-0005 (EVAL-2026-0004, weighted 3.76) whose content this candidate reproduces byte-for-byte apart from its governed provenance header. Because the artifact is byte-identical to the previously browser-verified reference except for the provenance comment, hard factual/structural gates are carried on static + handler-level evidence; rendered-dependent scores are capped per the degraded-mode rule.

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality (hard) | 4.0 | Canonical anatomy reproduced 1:1 from reference; 3 verified-fidelity prediction gates; 4 faded ladders (one per skill); ≥1 constructed-response per unit check; 3 explain-in-own-words; 11-item interleaved mastery with 3-level confidence; 15 misconceptions surfaced and encoded as distractors | none open | — | medium-high |
| Factual/mathematical accuracy (hard) | 4.0 | All worked examples, ladder rungs, widget defaults, and mastery keys carried from the recomputation-verified reference; widgets live-computed (not hard-coded); source typos corrected and flagged | none open | — | medium-high |
| Source grounding (hard) | 3.5 | All 63 cells dispositioned (reference Appendix A); claims anchored per CM-2026-0004; opaque figures (cells 38, 41–42) transcribed, not redistributed | Minor (inherited): transcription not verifiable against image content | independent figure check | medium |
| Interactivity and agency | 4.0 | 13 goal-directed manipulable widgets (no static-demo mislabeling); self-verifying readouts (e·y=0, x̂+e=x, live SSE); degenerate guards reproduced | none open | — | medium-high |
| Accessibility and inclusion (hard) | 3.5 | Reference's measured AA contrast (worst 4.86:1) carried forward (byte-identical); semantic landmarks; skip link; native controls; canvas text equivalents; reduced-motion honored; no-JS readable | no live re-measurement, no screen-reader pass (Minor, declared, degraded mode) | specialist review + browser re-check | medium |
| Visual clarity | 2.5 | Design-system tokens, badges, signature visuals reproduced (reference standard confirmed); **degraded-mode cap — no live rendering/screenshot evidence** | rendered-evidence requirement unmet (deg. mode) | browser Audit 6 re-run | medium |
| User experience | 2.5 | Sticky nav dots, rule-explaining feedback, review list, orientation unit reproduced; **degraded-mode cap — no live interaction trace** | rendered-evidence requirement unmet (deg. mode) | browser Audit 6 re-run | medium |
| Completeness | 4.0 | XS-2026-0005 conformance verified element-for-element: 13 widgets, 3 gates, 4 ladders, 9 unit checks, matching, 11 mastery items, 40-term 6-field glossary, branched concept map, review list, colophon, provenance header | none open | — | medium-high |
| Readability | 4.0 | Per-unit ledes, per-symbol formula keys, plain-language meaning + interpretation, badge/provenance tags on every block; prose precise and scanable | none open | — | medium-high |
| Technical feasibility/performance intent | 2.5 | Single file, zero external requests, system font stack, canvases redraw on input; **degraded-mode cap — no live performance/responsiveness trace** | rendered-evidence requirement unmet (deg. mode) | browser Audit 6 re-run | medium |

## Weighted result and gate check

**Weighted score: 3.58 / 4.00** (computed: 4.0·18 + 4.0·18 + 3.5·10 + 4.0·10 + 3.5·14 + 2.5·8 + 2.5·8 + 4.0·6 + 4.0·4 + 2.5·4 = 358 / 100).

Gate check (diagnostic for a private pilot): all four hard-gate dimensions ≥ 3.5 (Educational 4.0, Factual 4.0, Source 3.5, Accessibility 3.5); no score of 0–1; no unassessed dimension; no unresolved Critical defect. The three degraded-mode-capped dimensions (Visual, UX, Technical) sit below the learner-release floor of 3.0 solely because live rendered evidence could not be gathered in this environment — this does not block private-pilot closure (public-release eligibility is ineligible regardless per ADR-0003) but does require a browser Audit 6 re-check before any downstream release consideration.

## Disagreement or uncertainty

None material. The reproduction judgment carries medium confidence: score parity with the browser-verified reference (EVAL-2026-0004, 3.76) is expected on hard/static dimensions but the rendered-dependent scores could only be capped, not confirmed.

## Non-negotiable blockers

None at private-pilot scope. No Critical (false claim, broken core task, access barrier, provenance issue) defect found; provenance header matches this run's identity.

## Reviewer sign-off

`non-independent` review → public-release eligibility `ineligible` (ADR-0003). Disposition: **private-pilot-complete**. No score is a public release decision, benchmark result, or efficacy claim. Degraded-mode note (Audit 6) recorded; browser re-verification is the recommended follow-up before any release-scope use.

