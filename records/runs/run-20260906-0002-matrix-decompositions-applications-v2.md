# RUN-20260906-0002: Matrix decompositions and applications v2 (from-scratch rebuild)

**Status:** Pilot complete  
**Owner:** Repository maintainer (solo Stage 1 operator)  
**Objective:** Rebuild the Class 2 interactive notes from scratch at benchmark-band depth, revisiting all 40 source cells, closing the EVAL-2026-0011 gaps (numeric SVD, persistent progress state, confidence-calibrated mastery, deeper applications).  
**Budget:** One generation; maximum two revision cycles  
**Classification:** production  
**Operating scope:** Stage 1 private pilot  
**Review-independence summary:** non-independent  
**Public-release eligibility:** ineligible

## Input manifest

- Source: [SRC-2026-0002](../sources/src-2026-0002-matrix-decompositions-applications.md), SHA-256 `9616d9bd736974bb2d1a3ca2cc7f696834b13d22bbb66958d1c99dfdc1465ef5` (re-verified at intake)
- Concept model: [CM-2026-0009](../concepts/cm-2026-0009-matrix-decompositions-applications.md)
- Learning plan: [LP-2026-0010](../plans/lp-2026-0010-matrix-decompositions-applications.md)
- Experience specification: [XS-2026-0010](../specifications/xs-2026-0010-matrix-decompositions-applications-v2.md)
- Candidate: `CAN-2026-0011`, `matrix-decompositions-applications-v2.html`
- Prompt card: `prm-generator-lesson-standard@0.6.0`, digest `532febec136b` (the card file is the persisted prompt content)
- Benchmark: BMK-2026-0001 (calibration exemplar, per ADR-0011)

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-09-06 | CAN-2026-0011 | Cline (Claude Sonnet 4.6), autonomous orchestrator | prm-generator-lesson-standard@0.6.0 `532febec136b` + prm-orchestrator-autonomous@0.1.0 | single session | 2 in-generation corrections (see below) |

## Evaluation and defects

### Standing verification audits (P5 Audits 1–6)

- **Audit 1 (Coverage): PASS.** All 40 source cells dispositioned: cells 1–2 → U0 orientation; 3–10 → U1 (+ FOUNDATION bridges for determinant/identity); 11–16 → U2 (+ constructed diagonalization of [[3,1],[0,2]]); 17–24 → U3 (+ constructed full numeric SVD of [[2,1],[1,2]], closing the EVAL-2026-0011 gap); 25–32 → U4 (+ constructed 10-point dataset); 33–40 → U5 (+ constructed 4×3 ratings matrix; cell 36's "4R≈UVᵀ" typo corrected with tag). No silent drops; full matrix ships in EVAL-2026-0012.
- **Audit 2 (Mathematical & canvas extrema): PASS.** Node harness executed the page's live math core (eig2sym, jacobi, svd2, covariance) against independent pure-Python recomputation: 21/21 checks exact (eig(2,3)=(3,2); A⁵=[[243,211],[0,32]] for [[3,1],[0,2]]; PDP⁻¹ verified; σ=(3,1), uᵢ=vᵢ=(1,±1)/√2, UΣVᵀ=A; PCA λ=(2.3911263, 0.3857737), frac 86.108%, PC1 33.071°, σ₁=4.8899; ratings σ=(12.075638, 4.848052, 1.294358), energy 85.275% / 99.020%, V orthonormal, A₃ reproduces M to 1e-9). All check/ladder/mastery keys re-derived. Canvas extrema driven live (θ 0–360, stage 0–3, k 1–2, k 1–3, d∈{0,−3}, n=8) — nothing renders off-canvas.
- **Audit 3 (Dependency order): PASS.** Fresh read-in-order pass: determinant and identity taught before the characteristic equation (U1); inverse and linear independence bridged before PDP⁻¹ (U2); transpose bridged before AᵀA (U3); eigen decomposition named and defined at its comparison point (U3); variance/centering/projection bridged before covariance (U4); rank bridged before A_k (U5); application names (LSA, LoRA, transformer, diffusion) each carry a one-line bridge at first mention; every forward reference names a payoff unit that delivers.
- **Audit 4 (Pedagogical & depth-calibration contract): PASS.** U0 loop table + label legend; unit anatomy Learn→Predict→Explore→Practice→Check→Connect in U1–U5; 3 prediction gates with commitment-gated unlock and per-option feedback; 5 faded ladders (one per computational skill) with never-auto-opening hints; ≥1 constructed response per unit check (5 numeric) + diagnostic MCQs with misconception distractors; 2 explain-in-own-words items with model answers and self-evaluation; 7-item interleaved mastery with 3-level confidence and confident-miss routing; ≤1 callout per unit; 34-entry 6-field glossary; branched concept map in U0 and revisited in synthesis; goal strips on all widgets; W2's non-canvas modality justified in the XS.
- **Audit 5 (Technical & behavioral simulation): PASS.** `verify-candidate.py` strict (auto-engaged via @0.6.0 header): 0 failures, 9 notes — provenance header, colophon, ~34 glossary terms, all 7 range inputs per-element `.slider-track`-encapsulated, tabular `.slider-val`, `.option-stack` everywhere, 12 `.formula` blocks with 12 `.symkey`s, callout density, 16.5px body font, 0 textareas, 0 external requests, 169 unique IDs, all data-terms resolve. Canvas engineering (ADR-0013): `makeView` with `clientWidth` at draw time, DPR `setTransform`, aspect-ratio height, 4 resize listeners ≥ 4 canvases, per-widget viewports matching the XS declarations, `.legend-inline` on all multi-entity canvases. Behavioral simulation: gate refusal, confidence refusal, wrong/right grading branches, hint toggles, reset — all traced (see Audit 6).
- **Audit 6 (Rendered-output verification, ADR-0010): PASS, live browser.** Opened via `file://` in Chromium (agent-browser CDP). Zero console errors and zero page errors at load and after every trace. Responsive sweep: 320px/640px/1024px screenshots captured; body font measured 16.5px at every width; 640/1024 no overflow. Interaction traces: G1 commit (b) unlocks W1 with differentiated feedback; θ slider → live readout (θ=90° gives v=(0,1), Av=(0,3), cross=0, "direction preserved"); Unit 1 numeric (5) and MCQ (c) correct → feedback ok + nav dot fills; M1 (b, sure) correct; M3 (wrong, sure) → confident miss routed to review list; M2 without confidence → refusal; G2/G3 refusal and unlock branches; W2 extremes (d=0, d=−3, n=8 → diag(0, 6561) — sign alternation and zero crush live); W4 k=2, W5 k=1 (85.3% live) and k=3; W3 stage 3; resize event re-render; reload persistence; reset clears storage and dots. **One defect found and fixed in-generation: 56px horizontal overflow at 320px from the applications table's min-content width (the v9/CAN-2026-0008 defect class) — repaired with `display:block; overflow-x:auto` on `table.apptable`; re-verified clean.**
### Adversarial re-examination (mandatory gate per ADR-0009)

- **Read-in-order dependency re-pass:** fresh sweep without Audit 3 notes — no use-before-explain found; all four reveal arcs pay off where promised (U1 eigen-direction → U4 PCA header + PCA=SVD section; U2 cheap-powers sandwich → U5 A_k symbol key; U3 σ-link → U4 EQ-008; U5 latent close).
- **Handler-level behavioral simulation:** gate refusal across all 3 gates; grading boundaries (tolerances ±0 / ±1 / ±1.5 verified in code and live); confident-miss routing on radio (M3) and refusal-before-confidence (M2); reset from populated storage; corrupted-storage fallback (`loadJSON` try/catch → defaults) verified by code inspection.
- **Canvas-extrema forcing:** every manipulable driven to bounds (θ 0/360, stage 0/3, k 1/2 and 1/3, d −3/0/3, n 1/8) — all shapes remain in-viewport by construction (fixed models + bounded sliders); zero console errors.
- **Honesty & provenance scan:** constructed examples tagged; the source's "likely noise" softened; "4R≈UVᵀ" typo corrected and flagged; no release/benchmark/efficacy claims anywhere on the page; the only closing element is the standard colophon; header comment carries full identity.
- **Findings:** clean pass with documented evidence; no defect routed to revising.

### Re-verification pass (WF-008)

- Sampled checks re-executed after both in-generation corrections: `node --check` (JS syntax), full Node math harness (21/21), `verify-candidate.py` strict (0 failures), 320px overflow re-check (clean), affected interaction traces re-run.
- Headline claims reproduced: yes — σ=(12.08, 4.85, 1.29), rank-1 energy 85.3%, PCA retained variance 86.1% all reproduce live in-browser and match Python to 1e-6.

## Reflection and root-cause hypothesis

The v1 gaps (EVAL-2026-0011) all closed: a hand-checkable numeric SVD; persistent progress (nav dots + review list + reset); 7-item confidence-calibrated mastery; mechanism-anchored applications. Both in-generation defects belonged to known failure classes (stray paren in a template string — caught by `node --check`; 320px table overflow — the class RUN-20260904-0001 added live-browser sweeps for, caught by the rendered pass). Harness lesson recorded: CLI synthetic clicks on label-wrapped radios can under-register — real DOM events exercised every branch; this is a test-harness note, not an artifact defect.

## Revision history and regression checks

- In-generation correction 1: stray `)` in the `drawW2` readout template (JS SyntaxError) — fixed; `node --check` clean; re-verified.
- In-generation correction 2: 320px overflow from `table.apptable` min-content — fixed with block+scroll; re-measured docWidth=320 at 320px; 640/1024 unaffected.
- No post-evaluation revision cycles.

## Decision and approvers

**Final candidate identity at closure:** CAN-2026-0011, `matrix-decompositions-applications-v2.html`, SHA-256 `6c7e50951ce318c97272e7788439a2e7cce6c2b774f99df640786ef8ce28ae01`, 136,143 bytes  
**Disposition:** private-pilot-complete  
**Decision scope:** private pilot  
**Approvers and limitations:** Repository maintainer (solo Stage 1 operator); non-independent review; public release ineligible; no screen-reader specialist pass; no second evaluator.

**Iteration counts:** generation = 1; in-generation corrections = 2; revision cycles = 0 (per ADR-0006)

## Memory disposition

No new memory promoted: both in-generation defect classes are already codified (JS-syntax checking; the 320px overflow class in RUN-20260904-0001 / QA checklist change history). Observation for the pattern catalog: "reveal-arc payoffs declared in the LP depth-pass table and repeated per-unit in the XS content map survive generation" — candidate for MEM promotion after a second lesson confirms it.

## Lineage audit

SRC-2026-0002 → CM-2026-0009 → LP-2026-0010 → XS-2026-0010 → CAN-2026-0011 → EVAL-2026-0012. The v1 lineage (CM-2026-0008 → LP-2026-0009 → XS-2026-0009 → CAN-2026-0010 → EVAL-2026-0011) remains intact and superseded.

## Prompt snapshot

User trigger: `hey lets use the repo setup to build interactive notes for this @attachment:Matrix_Decompositions_&_Applications.ipynb notes! we have already built v1 lets revisit the doc again thoroughly and built it from scratch!`

Workflow directive: execute governed P0–P6 lesson generation for a v2 from-scratch rebuild — full source re-read (CM-2026-0009), depth-pass learning plan (LP-2026-0010), conformance specification (XS-2026-0010), single-file offline candidate (CAN-2026-0011) closing the EVAL-2026-0011 gaps, strict verification, six audits, adversarial re-examination, evaluation, module README update, and repository checker. Generator prompt card: `prm-generator-lesson-standard@0.6.0`, SHA-256 `532febec136b15b4988963ad6c5ffb1477163f45013a81fd47474ab6b24c0506` (the card file at [`library/prompts/prm-generator-lesson-standard@0.6.0.md`](../../library/prompts/prm-generator-lesson-standard@0.6.0.md) is the persisted prompt content); orchestrator skill: `prm-orchestrator-autonomous@0.1.0`.

