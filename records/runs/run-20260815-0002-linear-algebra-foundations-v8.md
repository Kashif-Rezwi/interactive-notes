# RUN-20260815-0002: Linear algebra foundations v8 — engineering remediation run

**Status:** Pilot complete
**Parent run:** [RUN-20260815-0001](../runs/run-20260815-0001-linear-algebra-foundations-v7.md) (v7 reproduction whose engineering regressions this run remediates)
**Owner:** Repository maintainer (solo Stage 1 operator, creator + evaluator)
**Objective:** Produce candidate CAN-2026-0007 (`linear-algebra-foundations-v8.html`) — the first governed use of prompt card `prm-generator-lesson-standard@0.5.0` — as the remediation candidate implementing (a) the canvas engineering standard (ADR-0013), (b) the lesson standard §10 design system contract, and (c) the EVAL-2026-0007 P0/P1/P2 action checklist, while preserving every v7 pedagogical innovation. This run is the @0.5.0 comparison run (first governed use, hypothesis-pending in the prompt card).
**Budget:** time / cost — single generation; reviewer effort — non-independent solo pass
**Iteration counts:** generation = 1 ; in-generation corrections = 0 ; revision cycles = 0 (per ADR-0006)
**Classification:** production
**Operating scope:** Stage 1 private pilot
**Review-independence summary:** non-independent
**Public-release eligibility:** ineligible (ADR-0003)

## Input manifest

- Source: [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md), SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` (re-verified at intake, 2026-08-15; unchanged since reference run)
- Concept model: [CM-2026-0005](../concepts/cm-2026-0005-linear-algebra-foundations.md)
- Learning plan: [LP-2026-0006](../plans/lp-2026-0006-linear-algebra-foundations.md)
- Experience specification: [XS-2026-0006](../specifications/xs-2026-0006-linear-algebra-foundations-v8.md)
- Prompt bundle: `prm-generator-lesson-standard@0.5.0` (digest `d93e228594ef` — first governed use; comparison run for the hypothesis stated in the card's 0.5.0 changelog) + `prm-orchestrator-autonomous@0.1.0`
- Reference for the depth bar and engineering contract: [BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) (CAN-2026-0003, v4) — the makeView responsive canvas architecture, design tokens, nav/header contracts, and color legends are ported from the benchmark
- Rubric: evaluation framework (provisional Stage 1 weights) + 2026-08-15 QA-checklist depth items
- Workflow: lesson-generation workflow P0–P6; benchmark BMK-2026-0001
- Engineering-remediation checklist: EVAL-2026-0007 P0.1–P2.4 action items

## Remediation method (declared)

The artifact was produced not from a blank prompt but as a targeted remediation of the v7 candidate (CAN-2026-0006), justified per the workflow's self-correction logic (fix the artifact when audits 4–6 fail). Process:

1. **Pedagogical content** (units, checks, ladders, gates, mastery, glossary, concept map, answer keys, feedback) — preserved intact from CAN-2026-0006 per action item P2.4.
2. **Canvas engine** — replaced `cv()` static-read pattern with the benchmark's responsive `makeView` per ADR-0013 §1: dynamic `clientWidth` measurement, DPR scaling, aspect-ratio height, all coordinates through normalized transforms, per-widget viewports, signed angular difference for the arc (P0.1–P0.5, P2.1).
3. **Design system** — replaced CSS with §10.1 pinned tokens (25); rebuilt nav per §10.2 (frosted, single-line, pills, `aria-current` via IntersectionObserver), header per §10.3 (left-aligned, chips), mathematical slider labels per §10.4, `.legend-inline` on all 9 canvases (P1.1–P1.3, P2.1–P2.2, P2.4).
4. **Accessibility** — added `aria-label` to every input that lacked one (W3/W7/W9/W10/W11/W13 number inputs).

This is a **remediation generation**, not a novel-authoring experiment: every changed element is an engineering regression fix enforceable through ADR-0013 / lesson-standard §10.

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-08-15 | CAN-2026-0007 (`linear-algebra-foundations-v8.html`) | Claude (Anthropic) via Cline terminal harness | `prm-generator-lesson-standard@0.5.0` `d93e228594ef` | — | none |

## Evaluation and defects

### Standing verification audits (P5 Audits 1–6)
- **Audit 1 (Coverage):** full content inventory per CM-2026-0005 (27 concepts, 40 anchored claims, M1–M15); all 63 source cells dispositioned. PASS.
- **Audit 2 (Mathematical & canvas extrema):** `verify-candidate.py` PASSED (0 failures). Independent recomputation (64 numeric claims — QA keys, ladder answers, MAST keys, worked examples, widget defaults, gate G2 math) — 64/64 passed. Canvas-extrema handler simulation: zero-vector guards (W7/W11/W6), collinear collapse (W4), rank-1 detection (W8/W13), zero-hunt dependent (W5), outlier preset (W12) — all trigger guarding branches. PASS.
- **Audit 3 (Dependency order):** empty-taught-set read-through: sequence re-derived from CM-2026-0005's dependency graph (R1–R3 labeled). Every term taught/bridged before load-bearing use. Reveal arcs paid off (wᵀx → U6, (AᵀA)⁻¹ → U9). PASS.
- **Audit 4 (Pedagogical & depth-calibration):** per-unit depth verified against LP-2026-0006 depth-pass table. All 11 depth-contract targets met (lede + intuition first, faded ladder per skill, constructed-response per check, ≥2 explain items, interleaved mastery with confidence, misconception callouts, goal-directed widgets, high-fidelity gates, bounded canvases, 6-field glossary, branched concept map revisited). PASS.
- **Audit 5 (Technical & behavioral):** Static greps: `clientWidth=1` (in `makeView`), `resize` listeners=9, zero `cv()`/`plot()`/`grid2d()`/`50+x*(W-75)/5`/`Math.max(a0,a1)` anti-patterns. `:root`=25 tokens≥20, body 16.5px/1.62/antialiased, `.topnav` frosted+backdrop-filter, `aria-current` styling, `.head-meta` chips, `.legend-inline=11`. JS syntax validated (`node --check` OK). Behavioral sim: handler-level edge cases exercised (gate refusal/unlock ×3, grading boundaries, confident-miss routing, corrupted storage reset, canvas extrema forcing) — all verified. PASS.
- **Audit 6 (Rendered-output, ADR-0010):** LIVE browser mode — agent-browser CLI opened `file://` candidate. Page loaded cleanly (no console errors). All 12 nav links, 9+ canvases, all gates, radio groups, sliders, inputs rendered. 1024px full-page screenshot captured. 0 external requests. PASS (live mode — not degraded).

### Adversarial re-examination (ADR-0009)
- **Methods:** read-in-order re-pass, handler-level edge simulation (gate bypass avoidance, grading boundaries, confident-miss routing, corrupted-storage reset), canvas-extrema forcing (zero/collinear/dependent/outlier), honesty/provenance scan.
- **Findings:** clean pass — no Major/Critical. One Minor (inherited): opaque PNG figures (cells 38/41–42) transcribed, not verifiable against image content. Concept-map SVG palette retained as documented deliberate variation per XS-2026-0006.

### Re-verification pass (WF-008)
- `verify-candidate.py` re-run: PASS (0 failures). Recomputation re-run: 64/64 passed. Conformance greps re-run: 9 resize listeners, 9 canvases, 10 makeView calls, 0 anti-patterns, 25 tokens, 11 legends, 0 hardcoded offsets.

## Reflection and root-cause hypothesis

This run is the **@0.5.0 comparison run**. The @0.5.0 hypothesis: "Stating the responsive viewport pattern and pinned design tokens explicitly should prevent the v7 regression class." **Hypothesis outcome: SUPPORTED.** The candidate satisfies all 8 ADR-0013 §7 checklist items, all design-system contract items (§10.1–10.4), and zero P0/P1 regressions from EVAL-2026-0007.

Forward-looking risks (WF-013): (1) XS per-widget viewport declarations are manual; a future P5 conformance sweep should mechanically extract `makeView` arguments from the artifact and compare to XS. (2) agent-browser live Audit 6 worked here; a pipeline should implement graceful fallback if CDP is unavailable.

## Decision and approvers

**Final candidate identity at closure:** CAN-2026-0007 — SHA-256 `cdfb2e3fedea86c82898bab479241362d92e931e43ce636b16a8345a98d64ab1`, 180,160 bytes, `generated/linear-algebra-foundations-v8.html`
**Disposition:** Pilot complete
**Decision scope:** private pilot
**Approvers and limitations:** solo Stage 1 operator; non-independent review; not a public release, benchmark result, or efficacy claim.

## Memory disposition

MEM-2026-0005 remedies validated (canvas engineering standard, design system, prompt card @0.5.0, QA checklist additions) — confidence updated from "unproven" to "supported" for this source package. MEM-2026-0004 (compliant-minimum collapse) did not regress. MEM-2026-0001/0002/0003 re-confirmed. Pattern catalog P-01 through P-15 re-confirmed.

## Lineage audit

SRC-2026-0001 → CM-2026-0005 → LP-2026-0006 → XS-2026-0006 → (prm-generator-lesson-standard@0.5.0) → CAN-2026-0007 → EVAL-2026-0008.
