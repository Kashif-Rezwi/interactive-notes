# EVAL-2026-0010: Linear algebra foundations v10 (CAN-2026-0009) — full-verification reproduction evaluation

**Candidate ID/version:** CAN-2026-0009, [`linear-algebra-foundations-v10.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v10.html), SHA-256 `dc9e64e1b8cfebb5507e2b28e1f870e67c8e31bfa47b49f6c6f479668fed4f96`, 197,467 bytes
**Rubric version:** evaluation framework, provisional Stage 1 weights + 2026-08-15 QA-checklist depth items + lesson standard §10.6–10.8 contracts
**Evaluator role/identity:** Repository maintainer (solo Stage 1 operator, Reviewer profile)
**Evaluation mode:** script-assisted + handler-level behavioral simulation, mechanical verification (`verify-candidate.py --strict`, post-P6-strengthened), independent recomputation (79 checks), structural conformance (42 checks), and **live browser rendered-output verification** (ADR-0010 Audit 6; agent-browser 0.27.0, Chrome for Testing 151.0.7922.76) — non-degraded
**Operating scope:** Stage 1 private pilot
**Review independence:** non-independent (author = reviewer)
**Reviewer relationship or limitation:** reviewer generated the artifact; no screen-reader pass; screenshots captured but evaluated via programmatic geometry (evaluator model cannot inspect images) — all rendered claims are backed by measured values
**Public-release eligibility:** ineligible ([ADR-0003](../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md))
**Confidence:** medium-high
**Recommendation:** private-pilot-complete
**Iterations reviewed:** builds = 1 (SHA-256 `dc9e64e1b8cfebb5507e2b28e1f870e67c8e31bfa47b49f6c6f479668fed4f96`); in-generation corrections = 4 defect classes (title identity; §10.6 per-element slider encapsulation; §10.1 body-font floor; 320px overflow/clipping set — all inherited from CAN-2026-0008 and repaired before evaluation); revision cycles = 0 ([ADR-0006](../../docs/adr/0006-record-iteration-accounting.md))

## Scope and evidence inspected

The single-file HTML artifact; run ledger [RUN-20260904-0001](../runs/run-20260904-0001-linear-algebra-foundations-v10.md) (includes the full audit-script appendices and verbatim outputs); inputs CM-2026-0007 / LP-2026-0008 / XS-2026-0008; strict verifier output (0 failures, 9 notes); recomputation (79/79); structural conformance (42/42); behavioral simulation (31/31); live-browser evidence (0 console messages/errors at load and after full interaction; screenshots at 1024/640/320px; measured 16.5px body font and zero horizontal overflow at 320px; live gate/ladder/mastery/slider/canvas-extrema traces; reduced-motion emulation; print PDF). Comparison reference: CAN-2026-0008 (v9), whose degraded-mode closure this run completes.

**Coverage matrix (compact, per Audit 1):** all 63 source cells dispositioned — cells 1–2 (agenda) → U0 orientation; 3–10 (scalar/vector/matrix) → U1; 11–17 (functions, Σ, notation kit) → U2; 18–19 (linearity proof, moved R3) + 29–34 (dot/norms/orthogonality) → U6/U5; 20–24 (vector space/combination/span) → U3; 25–28 + 57–59 (independence moved R1, basis, dimension) → U4; 35–45 (projection, decomposition, least squares) → U8; 46–56 (matrix ops moved R2) → U7; 60–61 (rank) → U9; 63 (ML table) → U10; cells 38/41–42 (opaque PNG figures) transcribed as keyed formulas, never redistributed. Nothing removed as "looked minor"; omissions none.

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality (hard) | 4.0 | Canonical anatomy across U1–U9; 3 commitment-gated prediction gates with option-specific feedback (verified live + simulated); 4 faded ladders (one per computational skill) with tiered never-auto-opening hints; 9 unit checks each with auto-graded constructed-response; 11-item interleaved mastery with 3-level confidence and confident-miss routing (verified); 15 misconceptions as diagnostic distractors; zero `<textarea>` | none open | — | high |
| Factual/mathematical accuracy (hard) | 4.0 | 79/79 independent recomputations (answer keys, ladder values, mastery keys, MCQ truths, worked examples, widget defaults); live widget math verified in-browser (W6 8.485/12/1.414; W4 vectors ≡ 2.5·[cosθ,sinθ]; least-squares 0.9/1.0/0.70; outlier 1.8/−0.5/5.8) | none open | — | high |
| Source grounding (hard) | 3.5 | All 63 cells dispositioned (coverage matrix above); claims anchored per CM-2026-0007; opaque figures transcribed, not redistributed | Minor (inherited): figure transcription not verifiable against image content | independent figure check | medium |
| Interactivity and agency | 4.0 | 13 goal-directed manipulables; live-verified causal feedback and degenerate guards (W4 collapse at equal angles, W8 singular collapse, W12 outlier chase); all 22 sliders atomically encapsulated (§10.6 per-element, repaired from 7/22 in v9) with tabular values — zero layout shift | none open | — | high |
| Accessibility and inclusion (hard) | 4.0 | Semantic landmarks, skip link, aria-labels on all controls, canvas `role="img"` + `aria-describedby` + numeric readouts, color-never-sole-encoder (9 legends), keyboard-operable native controls; **16px floor at all screen breakpoints (repaired; measured 16.5px at 320/640/1024)**; **zero horizontal overflow and no clipped text at 320px (repaired)**; reduced-motion honored (live-verified); print fallback renders | no live screen-reader pass (Minor, declared) | specialist review | medium-high |
| Visual clarity | 3.5 | Live-rendered evidence at 3 widths: 25 pinned tokens, frosted sticky nav, left-aligned header with chips, legends on all 9 canvases, concept-map caption within viewBox (repaired, max x 705 < 760) | Minor (inherited, XS-documented): concept-map SVG palette uses categorical colors outside the pinned token set | — | medium-high |
| User experience | 3.5 | Live traces: gate reveal + scroll-into-view, rule-explaining feedback on misses, mastery score build-up, review-list persistence and reset, tabular slider values (no reflow during drag), single-line nav with completion dots | none open | — | medium-high |
| Completeness | 4.0 | XS-2026-0008 conformance verified element-for-element: 13 widgets (9 canvases with declared viewports), 3 gates, 4 ladders, 9 unit checks, matching, 11 mastery items, 40-term × 6-field glossary, branched concept map revisited, review list, colophon, provenance header | none open | — | high |
| Readability | 4.0 | Per-unit ledes; 16 keyed formulas with per-symbol keys and interpretations; layer badges + provenance tags on every block; zero jargon deferral phrases; mathematical slider labels | none open | — | high |
| Technical feasibility/performance intent | 3.5 | Single 197KB file; zero external requests (verified live from `file://`); system font stack; 9 resize listeners; DPR-crisp canvas rendering; responsive at 320/640/1024 (live-measured); print PDF renders (23 pages) | Minor (observation): 197KB vs 178KB benchmark — within band | — | medium-high |

## Weighted result and gate check

**Weighted score: 3.85 / 4.00** (4.0·18 + 4.0·18 + 3.5·10 + 4.0·10 + 4.0·14 + 3.5·8 + 3.5·8 + 4.0·6 + 4.0·4 + 3.5·4 = 72+72+35+40+56+28+28+24+16+14 = 385 / 100).

Gate check (diagnostic for a private pilot): all four hard-gate dimensions ≥ 3.5 (Educational 4.0, Factual 4.0, Source grounding 3.5, Accessibility 4.0); no score of 0–1; no unassessed dimension; no unresolved Critical defect. Unlike RUN-20260903-0001, no dimension is degraded-mode capped: Visual clarity, User experience, and Technical feasibility are scored on live rendered evidence for the first time since EVAL-2026-0008, recovering the three 2.5-capped dimensions to their evidenced values.

## Disagreement or uncertainty

None material. Declared interpretation notes: (1) the explain-in-own-words floor (LP-2026-0008 outcome 12) is delivered via diagnostic MCQs with model-answer reveals — the @0.6.0 assessment-modality resolution of the textarea prohibition; the self-grade engine branch ships as unused capability (forward-looking note for the next prompt-card iteration); (2) the reviewer could not visually inspect screenshots (no image input); all rendered claims therefore rest on measured geometry (font sizes, scroll widths, element bounding boxes, viewBox extents) captured live, which is stronger evidence than unaided visual inspection; (3) EVAL-2026-0009's "all sliders encapsulated" evidence claim is corrected by this evaluation — v9 shipped 7/22 encapsulated; v10 ships 22/22.

## Non-negotiable blockers

None at private-pilot scope. No Critical defect (false claim, broken core task, access barrier, provenance issue) remains: the four inherited defect classes (title identity, §10.6 partial encapsulation, §10.1 font floor, 320px overflow/clipping) were Major/Minor, found by this run's audits, and repaired in-generation before evaluation. Provenance header matches this run's identity; canvas engineering contract (ADR-0013 §7) and design-system contract (§10.1–10.4) fully satisfied.

## Reviewer sign-off

`non-independent` review requires public-release eligibility `ineligible`. Disposition: **private-pilot-complete**. No score is a public release decision, benchmark result, or efficacy claim. The run's headline result — completing the live rendered verification that the v9 comparison run could not, and repairing the four inherited defect classes it surfaced — is recorded as evidence for ADR-0010, not as a new benchmark.


