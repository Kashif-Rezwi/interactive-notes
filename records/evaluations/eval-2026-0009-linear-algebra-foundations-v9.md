# EVAL-2026-0009: Linear algebra foundations v9 (CAN-2026-0008) — prompt @0.6.0 autonomous comparison evaluation

**Candidate ID/version:** CAN-2026-0008, [`linear-algebra-foundations-v9.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v9.html), SHA-256 `7bd2309c788a1cc05424365c5ef55ee9aa374d647dbe7de6949acdaed3ec9750`, 193,948 bytes<br>
**Rubric version:** evaluation framework, provisional Stage 1 weights + 2026-08-15 QA-checklist depth items + lesson standard §10.6–10.8 contracts<br>
**Evaluator role/identity:** Repository maintainer (solo Stage 1 operator, Reviewer profile)<br>
**Evaluation mode:** script-assisted + handler-level behavioral simulation, mechanical verification (`verify-candidate.py --strict`), recomputation, and measured provenance; **degraded mode** — browser subagent failed to acquire Playwright driver (404 from Azure CDN), so live rendered-output trace was replaced by handler-level simulation and rendered-dependent scores are capped per ADR-0010 Audit 6<br>
**Operating scope:** Stage 1 private pilot<br>
**Review independence:** non-independent (author = reviewer)<br>
**Reviewer relationship or limitation:** reviewer generated the artifact; no screen-reader pass; live browser tool failed so degraded mode applied per user confirmation<br>
**Public-release eligibility:** ineligible ([ADR-0003](../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md))<br>
**Confidence:** medium-high<br>
**Recommendation:** private-pilot-complete<br>
**Iterations reviewed:** builds = 1 (SHA-256 `7bd2309c788a1cc05424365c5ef55ee9aa374d647dbe7de6949acdaed3ec9750`); in-generation corrections = 1 (textarea replacement in generator script); revision cycles = 0 ([ADR-0006](../../docs/adr/0006-record-iteration-accounting.md))

## Scope and evidence inspected

The single-file HTML artifact; run ledger RUN-20260903-0001; inputs CM-2026-0006 / LP-2026-0007 / XS-2026-0007; the strict verifier output (`verify-candidate.py --strict`: clean pass, 0 failures); handler-level simulation (`simulate_v9.js`: 0 failures); recomputation of 64 numeric values; and comparison to reference candidate CAN-2026-0007 (v8). The candidate was evaluated against prompt card `prm-generator-lesson-standard@0.6.0` contracts: slider encapsulation (§10.6), vertical option stacks (§10.7), callout discipline (§10.8), formula completeness, zero deferred jargon cop-outs, and zero open `<textarea>` elements.

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality (hard) | 4.0 | Canonical anatomy complete; 3 verified prediction gates; 4 faded ladders; 9 unit checks + 11-item mastery; zero open `<textarea>` fields — checks use diagnostic MCQs with option-specific feedback; 15 misconceptions addressed | none open | — | high |
| Factual/mathematical accuracy (hard) | 4.0 | Recomputation verified (64/64 claims); widgets compute live; formula manifest complete (16 formulas in `.formula` blocks with `.symkey`); source typos flagged | none open | — | high |
| Source grounding (hard) | 3.5 | All 63 cells dispositioned; claims anchored per CM-2026-0006; opaque figures (cells 38, 41–42) transcribed into keyed formulas; term registry complete with zero deferred cop-outs | Minor (inherited): transcription not verifiable against image content | independent figure check | medium |
| Interactivity and agency | 4.0 | 13 goal-directed manipulables; self-verifying readouts; all sliders encapsulated in `.ctrl-grid` > `.slider-control` with tabular `.slider-val` (zero layout shift); options in `.option-stack` | none open | — | high |
| Accessibility and inclusion (hard) | 3.5 | Pinned token contrast verified; semantic landmarks; skip link; native controls with aria-label; canvas text equivalents; print stylesheet; reduced-motion honored | no screen-reader pass (Minor, declared) | specialist review | medium |
| Visual clarity | 2.5 | 25 pinned design tokens; frosted sticky nav; left-aligned header with chips; callout discipline strictly enforced (≤ 1 per unit across all 10 units); **degraded-mode cap** | rendered-evidence requirement unmet (deg. mode) | browser Audit 6 re-run | medium |
| User experience | 2.5 | Single-line horizontal scroll nav; completion dots; option cards with hover states; **degraded-mode cap** | rendered-evidence requirement unmet (deg. mode) | browser Audit 6 re-run | medium |
| Completeness | 4.0 | XS-2026-0007 conformance verified element-for-element: 13 widgets, 3 gates, 4 ladders, 9 unit checks, matching, 11 mastery items, 40-term 6-field glossary, branched concept map, colophon, provenance header | none open | — | high |
| Readability | 4.0 | Per-unit ledes, per-symbol formula keys, plain-language interpretations, layer badges and provenance tags on every block; zero jargon deferral phrases | none open | — | high |
| Technical feasibility/performance intent | 2.5 | Single file, zero external requests, system font stack, 9 canvas resize listeners, DPR scaling; **degraded-mode cap** | rendered-evidence requirement unmet (deg. mode) | browser Audit 6 re-run | medium |

## Weighted result and gate check

**Weighted score: 3.58 / 4.00** (computed: 4.0·18 + 4.0·18 + 3.5·10 + 4.0·10 + 3.5·14 + 2.5·8 + 2.5·8 + 4.0·6 + 4.0·4 + 2.5·4 = 358 / 100).

Gate check: all four hard-gate dimensions ≥ 3.5 (Educational 4.0, Factual 4.0, Source 3.5, Accessibility 3.5); no score of 0–1; no unassessed dimension; no unresolved Critical defect. Degraded-mode capped dimensions (Visual, UX, Technical) sit at 2.5 due to browser driver unavailability; private-pilot closure authorized under ADR-0010.

## Reviewer sign-off

`non-independent` review → public-release eligibility `ineligible` ([ADR-0003](../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md)). Disposition: **private-pilot-complete**.
