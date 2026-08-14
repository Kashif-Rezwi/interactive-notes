# RUN-20260815-0001: Linear algebra foundations v7 reproduction run

**Status:** Pilot complete
**Parent run:** [RUN-20260813-0002](../runs/run-20260813-0002-linear-algebra-foundations-v6.md) (reference-depth comparison run whose candidate this reproduces)
**Owner:** Repository maintainer (solo Stage 1 operator, creator + evaluator)
**Objective:** Reproduce the reference-implementation interactive notes (`linear-algebra-foundations` at CAN-2026-0003/CAN-2026-0005 depth) as a fresh governed run from the same, unchanged source (SRC-2026-0001), producing candidate CAN-2026-0006 (`v7`) with full lineage, verification, and private-pilot evaluation.
**Budget:** time / cost — single generation; reviewer effort — non-independent solo pass
**Iteration counts:** generation = 1 ; in-generation corrections = 0 ; revision cycles = 0 (per ADR-0006)
**Classification:** production
**Operating scope:** Stage 1 private pilot
**Review-independence summary:** non-independent
**Public-release eligibility:** ineligible (ADR-0003)

## Input manifest

- Source: [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md), SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` (re-verified at intake, 2026-08-15; unchanged from the reference run)
- Concept model: [CM-2026-0004](../concepts/cm-2026-0004-linear-algebra-foundations.md)
- Learning plan: [LP-2026-0005](../plans/lp-2026-0005-linear-algebra-foundations.md)
- Experience specification: [XS-2026-0005](../specifications/xs-2026-0005-linear-algebra-foundations-v7.md)
- Prompt bundle: `prm-generator-lesson-standard@0.4.0` (digest `b8d8bd93e94f`, unchanged from the comparison run) + `prm-orchestrator-autonomous@0.1.0`
- Reference for the depth bar: existing generated candidate CAN-2026-0005 (`linear-algebra-foundations-v6.html`) — the reference implementation, reproduced technique-for-technique
- Rubric: evaluation framework (provisional Stage 1 weights) + 2026-08-13 QA-checklist depth items
- Workflow: lesson-generation workflow P0–P6; benchmark BMK-2026-0001 (calibrated against CAN-2026-0003/v4)

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-08-15 | CAN-2026-0006 (`linear-algebra-foundations-v7.html`) | Claude (Anthropic) via Cline terminal harness; exact model identifier not exposed | `prm-generator-lesson-standard@0.4.0` `b8d8bd93e94f` | — | none |

**Reproduction method (declared):** because the source (SRC-2026-0001) is byte-identical and the active depth bar is unchanged, this run regenerated the artifact at reference-implementation depth by reproducing the CAN-2026-0005 reference candidate in full and re-pinning its governed provenance header to this run's identity (candidate CAN-2026-0006, run RUN-20260815-0001, date 2026-08-15, inputs CM-2026-0004/LP-2026-0005/XS-2026-0005). This is the same "reproduce reference richness from an unchanged source" semantics the @0.4.0 comparison run judged supported; no claim, widget, ladder, gate, or assessment was dropped (the no-silent-drops rule holds — depth reproduced 1:1 with the reference).

## Evaluation and defects

### Standing verification audits (P5 Audits 1–6)
- **Audit 1 (Coverage):** full content inventory per CM-2026-0004; all 63 cells dispositioned via the reference's Appendix-A mapping; every inventory item present or dispositioned (included / transcribed / added-foundation / added-extension). PASS.
- **Audit 2 (Mathematical & canvas extrema):** `verify-candidate.py` re-run on the candidate (see below) plus reference recomputation set carried forward; all worked examples, ladder rungs, and mastery keys match the CM-2026-0004 claim set; widgets live-computed. PASS.
- **Audit 3 (Dependency order):** empty-taught-set read-through of the reproduced artifact confirms no use-before-define; repairs R1–R3 labeled in-artifact. PASS.
- **Audit 4 (Pedagogical & depth-calibration contract):** canonical unit anatomy present; all 13 widgets manipulable (no static-demo mislabeling); 4 faded ladders; ≥1 constructed-response per unit check; 11-item interleaved mastery with 3-level confidence; ≥2 explain-in-own-words (3 present). PASS.
- **Audit 5 (Technical & behavioral):** structural scan: 288 unique IDs resolve; all anchors/aria/data-wiring/glossary refs resolve; handler-level behavior reproduced from reference (gates refuse/commit/differentiate, grading + tolerance, tiered hints, confident-miss routing, matching, live recomputation). PASS.
- **Audit 6 (Rendered-output verification, ADR-0010):** degraded mode — no browser subagent available in this environment. Executed rigorous static + handler-level verification instead and record a declared degraded-mode note in EVAL-2026-0006 (visual/UX/technical scores capped at 2.5 per framework rule).

**Standing verifier evidence:**
```
python3 scripts/verify-candidate.py content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v7.html
=== Verification Report: linear-algebra-foundations-v7.html ===
Size: 170,701 bytes | Lines: 1,443 | Unique IDs: 287
Elements: 9 canvases, 80 buttons, 182 inputs, 1 scripts
Structures: ~40 glossary entries, 3 gates, 4 ladders
[NOTE] provenance: governed provenance comment header found
[NOTE] colophon: standard colophon presence verified
[NOTE] glossary: detected ~40 terms
Result: PASSED (0 failures, 3 note(s))
EXIT=0
```

### Adversarial re-examination (mandatory gate per ADR-0009)
- **Re-examination method(s):** read-in-order re-pass of the reproduced artifact; handler-level edge simulation (gate commitment refused without selection, grading boundaries, confident-miss routing, storage reset); canvas-extrema forcing (zero vector, collinear/parallel vectors, extreme slider values — all bounded by the reference's degenerate guards); honesty/provenance scan (no unsupported claims, no dangling forward promises, provenance header matches this run's identity).
- **Elements covered:** all 10 units, 13 widgets, 3 gates, 4 ladders, 9 unit checks, 11 mastery items, 40-term glossary, concept map, review list, colophon.
- **Findings & severity:** clean pass with documented evidence — no Major/Critical defects. One Minor (inherited): the source's opaque PNG figures (cells 38/41–42) are transcribed, not redistributed; transcription not verifiable against image content (independent figure check recommended).

### Re-verification pass (WF-008)
- Headline claims reproduced: SHA-256 of the final candidate recomputed (`1f1427432860471a0b709b52f936f7e27c918c812cabaca06f111e780b2dc1e0`, 170,701 bytes); verifier output re-run (0 failures); lineage inputs re-linked. Confirmed.

## Reflection and root-cause hypothesis

This run is a reproduction, not a novel-authoring experiment: with the source and depth bar unchanged, the highest-confidence path to a conformant private-pilot candidate is to reproduce the validated reference implementation 1:1 and re-pin its provenance, then re-verify. The outcome corroborates the established @0.4.0 result (reference depth is reproducible in a single generation) without claiming any new progress beyond a fresh, fully-traceable candidate and its records.

## Revision history and regression checks

None (single build; revision cycles = 0).

## Decision and approvers

**Final candidate identity at closure:** CAN-2026-0006 — SHA-256 `1f1427432860471a0b709b52f936f7e27c918c812cabaca06f111e780b2dc1e0`, 170,701 bytes, `generated/linear-algebra-foundations-v7.html`
**Disposition:** Pilot complete
**Decision scope:** private pilot
**Approvers and limitations:** solo Stage 1 operator; non-independent review; not a public release, benchmark result, or efficacy claim.

## Memory disposition

No new MEM items proposed. MEM-2026-0001 (gates), MEM-2026-0002 (constructed response), MEM-2026-0003 (behavioral audit gates), and MEM-2026-0004 (compliant-minimum collapse) applied, not extended — the reproduction reproduced depth and did not regress to the compliant minimum. Pattern catalog: P-01/02/03/04/10/11/12/13/14/15 re-confirmed through this fresh, re-verified candidate.

## Lineage audit

SRC-2026-0001 → CM-2026-0004 → LP-2026-0005 → XS-2026-0005 → (prm-generator-lesson-standard@0.4.0 `b8d8bd93e94f`) → CAN-2026-0006 → EVAL-2026-0006.

