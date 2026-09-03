# RUN-20260904-0001: Linear algebra foundations v10 — full-verification reproduction run

**Status:** Pilot complete
**Parent run:** [RUN-20260903-0001](../runs/run-20260903-0001-linear-algebra-foundations-v9.md) (the @0.6.0 comparison run whose degraded-mode Audit 6 closure this run completes)
**Owner:** Repository maintainer (solo Stage 1 operator, creator + evaluator)
**Objective:** Reproduce the validated v9 reference design (CAN-2026-0008, post-norm-clarification fix at commit `201a778`) as fresh candidate CAN-2026-0009 (`linear-algebra-foundations-v10.html`) from the same, byte-unchanged source (SRC-2026-0001) under the unchanged prompt card @0.6.0, and execute the complete P5 suite **including live rendered-output verification (ADR-0010 Audit 6)** — the capability unavailable to RUN-20260903-0001 — closing its degraded-mode gap and repairing any inherited defects the live pass surfaces.
**Budget:** time / cost — single generation with bounded self-correction (max 2 revision cycles; none consumed); reviewer effort — non-independent solo pass
**Iteration counts:** generation = 1 ; in-generation corrections = 4 defect classes (title identity; §10.6 per-element slider encapsulation; §10.1 body-font floor; 320px overflow/clipping set) ; revision cycles = 0 (per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md))
**Classification:** production
**Operating scope:** Stage 1 private pilot
**Review-independence summary:** non-independent
**Public-release eligibility:** ineligible ([ADR-0003](../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md))

## Input manifest

- Source: [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md), SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` (re-verified at intake, 2026-09-04; unchanged since first capture)
- Concept model: [CM-2026-0007](../concepts/cm-2026-0007-linear-algebra-foundations.md) (iteration 5; stable claim set, re-grounded)
- Learning plan: [LP-2026-0008](../plans/lp-2026-0008-linear-algebra-foundations.md) (iteration 5; full depth pass carried)
- Experience specification: [XS-2026-0008](../specifications/xs-2026-0008-linear-algebra-foundations-v10.md) (iteration 5; conformance contract re-pinned to CAN-2026-0009)
- Prompt bundle: `prm-generator-lesson-standard@0.6.0` (SHA-256 `532febec136b15b4988963ad6c5ffb1477163f45013a81fd47474ab6b24c0506`, digest `532febec136b`, unchanged from the v9 comparison run — full snapshot in Appendix A) + `prm-orchestrator-autonomous@0.1.0`
- Reference for the depth bar and engineering contract: [BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) (CAN-2026-0003, v4) and the current reference candidate CAN-2026-0008 (v9) per the module README
- Rubric: evaluation framework (provisional Stage 1 weights) + 2026-08-15 QA-checklist depth items + lesson-standard §10.6–10.8 contracts
- Workflow: lesson-generation workflow P0–P6; benchmark BMK-2026-0001
- Tooling: `scripts/verify-candidate.py` (strict), purpose-built audit scripts (Appendix B), agent-browser 0.27.0 (Chrome for Testing 151.0.7922.76) for Audit 6

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-09-04 | CAN-2026-0009 (`linear-algebra-foundations-v10.html`) | Claude (Anthropic) via Cline terminal harness; exact model identifier not exposed | `prm-generator-lesson-standard@0.6.0` `532febec136b` | — | in-generation corrections: 4 inherited defect classes (below) |

**Reproduction method (declared):** because the source (SRC-2026-0001) is byte-identical, the active depth bar is unchanged, and prompt card @0.6.0 is unchanged, this run reproduced the validated v9 reference candidate (including its post-evaluation norm-clarification fix, commit `201a778`) in full and re-pinned its governed identity to this run: provenance header (CAN-2026-0009 / RUN-20260904-0001 / inputs CM-2026-0007 / LP-2026-0008 / XS-2026-0008), `<title>` version, and the per-version localStorage key (`laf9` → `laf10`). This is the same "reproduce reference richness from an unchanged source" semantics as RUN-20260815-0001; no claim, widget, ladder, gate, or assessment was dropped (the no-silent-drops rule holds — depth reproduced 1:1 with the reference, then improved where the live audit found inherited defects).

**In-generation corrections (4 defect classes, all inherited from v9 and repaired before evaluation):**

1. **Title identity defect (Minor, provenance):** the v9 artifact's `<title>` still read "(v8)" — a leftover from the v8→v9 reproduction that v9's audits missed. Repaired to "(v10)".
2. **§10.6 per-element slider encapsulation (Major, contract):** 15 of 22 range inputs (widgets W1, W2, W4, W5, W8, W12) still used the legacy `.ctrl` label layout that standard §10.6 and the @0.6.0 card prohibit ("never emit bare range inputs as loose siblings in raw flex containers"); only W3/W6 (7 sliders) were atomically encapsulated. EVAL-2026-0009's "all sliders encapsulated" evidence claim was therefore inaccurate. All 22 sliders now sit in `.ctrl-grid` > `.slider-control` > `.slider-head` (`.slider-label` + tabular `.slider-val`) > `.slider-track`, with IDs and aria-labels preserved.
3. **§10.1 body-font floor (Major, accessibility):** a `@media (max-width:640px){body{font-size:15.5px}}` override dropped the body font below the 16px hard floor at small widths (inherited from the pre-@0.6.0 lineage; invisible to v9's degraded Audit 6). The override is removed; computed body font is 16.5px at all screen breakpoints (measured live at 320/640/1024px).
4. **320px overflow / clipping set (Major, responsive):** at 320px the page scrolled horizontally to 514px — drivers: W10's six-input control label (486px) and W9's matrix labels (327px) could not wrap; the ML-connections table (`table.mlt`, 348px min-content) exceeded the viewport; and the concept-map SVG caption `<text>` spanned ~1153 viewBox units against a 760-unit viewBox (clipped). Repairs: `.ctrl label{flex-wrap:wrap}` globally; small-screen number-input width 3.6rem; `table.mlt` becomes a contained `display:block;overflow-x:auto` scroll region with tightened padding/font; the SVG caption split into two in-bounds lines (max x 705 < 760, verified live). Post-repair: `document.scrollWidth = 320 = viewport`, zero elements wider than the viewport, no clipped caption text.

## Evaluation and defects

### Standing verification audits (P5 Audits 1–6)

- **Audit 1 (Coverage):** full content inventory per CM-2026-0007 (27 concepts, 40 anchored claims, M1–M15); all 63 source cells dispositioned via the XS-2026-0008 content map (cells 1–2 agenda → U0 orientation; 3–10 → U1; 11–17 → U2; 20–24 → U3; 57–59 + 25–28 → U4 with repair R1 labeled; 31–32 → U5; 29–34 + 18–19 → U6 with repair R3; 46–56 → U7 with repair R2; 35–45 → U8; 60–61 → U9; 63 → U10; opaque PNG figures at cells 38/41–42 transcribed as keyed formulas, never redistributed). PASS.
- **Audit 2 (Mathematical & canvas extrema):** independent recomputation script (Appendix B.1) — **79/79 checks passed**: 10 unit-check numeric keys, 11 ladder values across 8 rungs, 4 mastery numeric keys, 24 MCQ correct-answer letters re-derived, the 4-pair match solution, 22 prose/widget-number strings, and live-math recomputations (least-squares 0.9/1.0/0.70; outlier preset 1.8/−0.5/5.8; W7 dot/cos/θ = 5/0.707/45°; W4 vectors = 2.5·[cosθ, sinθ]). Zero hard-coded widget outcomes (all readouts live-computed; verified live in Audit 6). PASS.
- **Audit 3 (Dependency order):** empty-taught-set read-through of the reproduced artifact: every term/notation/concept is taught, bridged (FOUNDATION labels: cos θ primer, matrix-inverse bridge), or labeled EXTENSION before load-bearing use; repairs R1–R3 labeled in-artifact; every forward promise names and reaches its payoff (wᵀx arc set up U2 → paid off U6; linear-model arc → closed U8; (AᵀA)⁻¹ loop → closed U9). PASS.

- **Audit 4 (Pedagogical & depth-calibration contract):** canonical unit anatomy (Learn → Predict → Explore → Practice → Check → Connect) across U1–U9; 3 prediction gates commitment-gated with option-specific feedback; 4 faded ladders (Σ, norms, dot product, projection — one per computational skill) with never-auto-opening hints; 9 unit checks each containing auto-graded constructed-response items; 11-item interleaved mastery with 3-level confidence and confident-miss routing; 15 misconceptions surfaced as diagnostic distractors with callout density ≤ 1 per unit (12 unit sections checked); 40-term glossary with all 6 fields × 40 entries; branched dependency concept map introduced in U0 and revisited at close. Declared modality note: the explain-in-own-words floor (LP outcome 12, 3 items) is delivered via diagnostic MCQs with model-answer reveals — the @0.6.0 resolution of the textarea prohibition; the self-grade engine branch ships as unused capability. Zero `<textarea>` fields. PASS.
- **Audit 5 (Technical & behavioral simulation):** `verify-candidate.py --strict` PASSED (0 failures, 9 notes) — including the two checks added at this run's P6 (per-element §10.6 slider encapsulation 22/22; §10.1 body-font floor, print exempt). Structural conformance script (Appendix B.2) — **42/42 checks passed**: canvas engineering contract (9 canvases; 9 resize listeners; 10 `makeView` occurrences; DPR `setTransform`; aspect-ratio CSS height; `clientWidth` at draw time; normalized X/Y transforms; signed angular arcs; zero pixel-offset anti-patterns; 9 `.legend-inline`; `canvas.viz` baseline), component contracts (§10.6 per-element, §10.7 stacks, §10.8 callouts ≤ 1/unit), 16 formula blocks + 27 symkeys, glossary shape, jargon discipline (zero deferrals; all `data-term` targets resolve), 25 design tokens, nav/header contracts, reduced-motion, print stylesheet, skip link, colophon-only closing, zero external references. Handler-level behavioral simulation (Appendix B.3) — **31/31 traces passed**: gate refusal/reveal/commitment-not-correctness, option-specific gate feedback, numeric grading boundaries (1e-7 rejected, 1e-10 accepted), MCQ routing to/from the review list, confident-miss vs plain-miss routing, ladder multi-input grading with rule feedback, matching accept/reject with row-naming, hint hidden-by-default + toggle, self-grade handler path, corrupted-persisted-state recovery (invalid JSON → clean defaults), reset (clears `laf10`, reloads), glossary popover open/Escape-close. PASS.
- **Audit 6 (Rendered-output verification, ADR-0010):** **live browser mode** (agent-browser 0.27.0, Chrome for Testing 151.0.7922.76, `file://` load) — the first fully non-degraded Audit 6 in this lineage since RUN-20260815-0002 (v8). Evidence: **zero console messages and zero page errors** on initial load and after the full interaction sequence; screenshots captured at 1024px, 640px, and 320px (pre- and post-repair); at 320px the computed body font is **16.5px**, `document.scrollWidth = 320` (no horizontal overflow), zero elements wider than the viewport, and the concept-map caption sits inside the viewBox (max x 705 < 760); live interaction traces all pass — gate g1 commit reveals W4 with option-specific feedback, ladder l1r2 (8, 20) grades ✓, mastery m2 with 'sure' confidence grades ✓ and the score builds ("1 / 11 correct"), W6 slider input live-updates the readout ([−6, −6] → ‖x‖₂ = 8.485, ‖x‖₁ = 12, ratio 1.414) with tabular value display, W4 angles driven to 350°/350° fire the collapse guard ("collapsed: the lattice is just a line — the span is 1-D!"), W8 'collapse' preset flattens the square with the rank-1 message; reduced-motion emulation confirmed (`prefers-reduced-motion: reduce` active, `scroll-behavior: auto`); print PDF renders (23 pages, print-notes visible). PASS.

### Adversarial re-examination (mandatory gate per ADR-0009)

- **Re-examination method(s):** (1) read-in-order dependency re-pass from a fresh perspective, independent of Audit 3 notes; (2) handler-level behavioral simulation of edge cases (31 traces, Appendix B.3 — gate refusal/unlock branches, grading boundary inputs, confident-miss routing on radio and numeric items, reset from corrupted persisted state); (3) canvas-extrema forcing in the live browser (W4 angles to 350°/350° → collapse guard; W6 components to ±6 bounds; W8 'collapse' singular preset; W12 outlier preset recomputed m = 1.8, c = −0.5, SSE = 5.8); (4) honesty/provenance scan (provenance header matches this run's identity; colophon-only closing; no release/benchmark/efficacy claims; no dangling forward promises; no uncredited external claims; zero external requests verified live).
- **Elements covered:** all 12 unit sections, 13 widgets, 3 gates, 4 ladders, 9 unit checks, matching, 11 mastery items, 40-term glossary, concept map, review list, storage/reset, popover.
- **Findings & severity:** 4 inherited defect classes found (title identity — Minor; §10.6 partial encapsulation — Major; §10.1 font floor — Major; 320px overflow/clipping — Major), all repaired in-generation before evaluation; post-repair clean pass with documented evidence (all four verification suites re-run green). This gate is also where EVAL-2026-0009's inaccurate "all sliders encapsulated" evidence claim was identified — validating ADR-0009's independent-perspective requirement.

### Re-verification pass (WF-008)

- Sampled checks re-executed on the final build: `verify-candidate.py --strict` → PASSED (0 failures, 9 notes); recomputation → 79/79; conformance → 42/42; simulation → 31/31 (full outputs in Appendix B).
- Headline claims reproduced: SHA-256 of the final candidate recomputed — `dc9e64e1b8cfebb5507e2b28e1f870e67c8e31bfa47b49f6c6f479668fed4f96`, 197,467 bytes; source hash re-verified unchanged; lineage inputs re-linked. Confirmed.

## Reflection and root-cause hypothesis

This run is a full-verification reproduction: with source, depth bar, and prompt card unchanged, the highest-confidence path was to reproduce the validated v9 reference 1:1, re-pin identity, and complete the rendered verification that RUN-20260903-0001 could not perform. The outcome concretely validates ADR-0010's premise: **the live rendered pass surfaced four inherited defect classes within minutes** — a title-version mismatch, partial per-element §10.6 conformance, a sub-16px media-query font override, and a 320px overflow/clipping set — all of which survived v9's presence-based mechanical checks and degraded-mode closure. Root cause: the @0.6.0 comparison run audited the new component contracts primarily through the presence-based verifier (class names exist) rather than per-element structural verification, and its degraded Audit 6 capped exactly the checks (font floor at breakpoints, overflow spot-checks) that would have caught the rest — a compound blind spot. The P6 response closes the enforcement gap mechanically: `verify-candidate.py` now counts range inputs against `.slider-track` wrappers per element and scans every screen-media body font-size declaration against the 16px floor (print exempt); re-run on v9, the strengthened verifier fails on exactly the two classes v9 shipped, while the v4 benchmark remains clean in legacy compatibility mode.

## Revision history and regression checks

None post-evaluation (single build; revision cycles = 0). All four defect-class repairs occurred in-generation, before evaluation, and were re-verified by the full suite; regression checks: strict verifier, recomputation (79), conformance (42), and simulation (31) all re-run green on the final build; live browser re-checks at all three widths post-repair.

## Decision and approvers

**Final candidate identity at closure:** CAN-2026-0009 — SHA-256 `dc9e64e1b8cfebb5507e2b28e1f870e67c8e31bfa47b49f6c6f479668fed4f96`, 197,467 bytes, `generated/linear-algebra-foundations-v10.html`
**Disposition:** Pilot complete
**Decision scope:** Stage 1 private pilot
**Approvers and limitations:** solo Stage 1 operator; non-independent review; not a public release, benchmark result, or efficacy claim.

## Memory disposition

No new MEM records promoted (memory promotion requires the review policy's process). Disposition of observations: (a) the concrete value of live rendered-output verification extends the recorded evidence for ADR-0010 and MEM-2026-0003 (standing gates) — referenced, not re-authored; (b) the 320px overflow/clipping set is a new instance of the MEM-2026-0005 layout-responsiveness class, now caught at generation time by the amended verifier — referenced; (c) the presence-only vs per-element verification lesson is codified as tooling (two new `verify-candidate.py` checks) and a QA-checklist change-history entry rather than a new memory record. Pattern catalog: unchanged — P-01…P-15 re-confirmed through this fresh, fully verified candidate; no pattern observed failing.

## Lineage audit

SRC-2026-0001 → CM-2026-0007 → LP-2026-0008 → XS-2026-0008 → (prm-generator-lesson-standard@0.6.0 `532febec136b`) → CAN-2026-0009 → EVAL-2026-0010.






## Appendix A: Fully rendered prompt snapshot

Prompt card identity: `prm-generator-lesson-standard@0.6.0`, SHA-256 `532febec136b15b4988963ad6c5ffb1477163f45013a81fd47474ab6b24c0506` (digest `532febec136b`), at [`library/prompts/prm-generator-lesson-standard@0.6.0.md`](../../library/prompts/prm-generator-lesson-standard@0.6.0.md) — unchanged from RUN-20260903-0001; the card file itself is the persisted prompt content (prompt-architecture persistence rule). Orchestrator trigger rendered for this run:

```markdown
You are the Autonomous Lesson Orchestrator for Learning OS. You are given a source notes document content/aiml-4/module-02-math-statistics-for-ml/sources/Mathematical_Foundations_&_Linear_Algebra_Fundamentals.ipynb and user trigger prompt "lets go, create interactive notes for @[content/aiml-4/module-02-math-statistics-for-ml/sources/Mathematical_Foundations_&_Linear_Algebra_Fundamentals.ipynb]".

Execute the full P0-P6 governed workflow:
- P0: Hash source (re-verify SRC-2026-0001), allocate sequential IDs, initialize RUN-20260904-0001.
- P1: Author CM-2026-0007 (iteration; stable claim set, re-grounded) adhering to the depth-calibration contract.
- P2: Author LP-2026-0008 (iteration; resequenced explain-before-use teaching order and depth pass table).
- P3: Author XS-2026-0008 (iteration; per-widget viewports, formula manifest, term definition registry, component layout contracts) for candidate CAN-2026-0009.
- P4: Generate candidate CAN-2026-0009 (linear-algebra-foundations-v10.html) under prm-generator-lesson-standard@0.6.0 digest 532febec136b, reproducing the validated v9 reference design with identity re-pinned to this run.
- P5: Execute six QA audits and the adversarial gate; enforce strict mechanical verification; perform live rendered-output verification (ADR-0010 Audit 6) via agent-browser.
- P6: Author EVAL-2026-0010, update module README, verify repository hygiene (check-repo.py), and curate compounding assets (verifier strengthening for escaped defect classes).
```

## Appendix B: Audit execution methods and outputs (WF-008 / WF-015 persistence)

All three scripts below were executed against the final build of `linear-algebra-foundations-v10.html` (SHA-256 `dc9e64e1b8cfebb5507e2b28e1f870e67c8e31bfa47b49f6c6f479668fed4f96`); their outputs follow each script verbatim. The standing verifier output (`python3 scripts/verify-candidate.py --strict`, run after the P6 strengthening) is included first.

### B.0 Standing verifier (strict)

```
=== Verification Report: linear-algebra-foundations-v10.html [STRICT (v0.6.0 contract)] ===
Size: 197,467 bytes | Lines: 2,027 | Unique IDs: 376
Elements: 9 canvases, 80 buttons, 169 inputs, 0 textareas, 1 scripts
Structures: ~40 glossary entries, 3 gates, 4 ladders, 16 formulas
--------------------------------------------------
[NOTE] provenance: governed provenance comment header found
[NOTE] colophon: standard colophon presence verified
[NOTE] glossary: detected ~40 terms
[NOTE] slider-layout: atomic .slider-control and tabular numeric styling verified
[NOTE] slider-encapsulation: all 22 range inputs verified inside .slider-track wrappers (per-element)
[NOTE] font-floor: all 1 body font-size declaration(s) >= 16px
[NOTE] option-layout: vertical .option-stack and .option-item verified
[NOTE] formula: detected 16 .formula blocks with 27 symbol keys
[NOTE] callout-density: callout discipline verified (<= 1 per unit)

Result: PASSED (0 failures, 9 note(s))
```

Strengthening evidence (P6): the same verifier run strictly against the v9 reference (`linear-algebra-foundations-v9.html`) fails with exactly the two escaped classes — `[FAIL] slider-encapsulation: 15 of 22 range input(s) are NOT wrapped in .slider-track` and `[FAIL] font-floor: body font-size below the 16px floor in 1 declaration(s) (15.5, px)` — while the v4 benchmark in legacy compatibility mode remains PASSED (defects noted as `[LEGACY]`, no regression).

### B.1 Independent recomputation — `recompute.py` (Audit 2)

```python
#!/usr/bin/env python3
"""Independent recomputation audit — CAN-2026-0009 (linear-algebra-foundations-v10.html).

Audit 2 evidence for RUN-20260904-0001 (WF-008 execution-evidence rule).
Every numeric claim embedded in the artifact (QA/MULTI/MAST answer keys, MCQ correct
letters, match solution, worked examples, widget default readouts, gate feedback
numbers) is recomputed from first principles and compared with the artifact value.
Read-only; zero dependencies; exit 0 = all checks pass.
"""
import math
import re
import sys

HTML = "/Users/kashifrezwi/Developer/interactive-notes/content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v10.html"
html = open(HTML, encoding="utf-8").read()
fails = []
passed = 0


def eq(a, b, eps=1e-9):
    return abs(a - b) <= eps


def check_num(name, computed, art_id, note=""):
    """Compare an independently computed value with the artifact's embedded numeric key."""
    global passed
    m = re.search(art_id + r":\{t:'num',a:(-?[\d.]+)", html)
    if not m:
        fails.append(f"{name}: artifact key not found")
        print(f"[FAIL] {name}: artifact key not found")
        return
    embedded = float(m.group(1))
    if eq(computed, embedded):
        passed += 1
        print(f"[OK]   {name}: independent = {computed:g} | artifact = {embedded:g} {note}")
    else:
        fails.append(f"{name}: independent {computed:g} != artifact {embedded:g}")
        print(f"[FAIL] {name}: independent {computed:g} != artifact {embedded:g}")


def check_str(name, computed_desc, pattern):
    global passed
    if re.search(pattern, html):
        passed += 1
        print(f"[OK]   {name}: {computed_desc}")
    else:
        fails.append(f"{name}: artifact string not found")
        print(f"[FAIL] {name}: artifact string not found ({computed_desc})")


print("=== Independent recomputation — CAN-2026-0009 (v10) ===\n")

print("--- Unit-check numeric keys (QA) ---")
check_num("u1q2 features of a 4x3 table (cols)", 3, "u1q2")
check_num("u2q1 sum i=1..5", sum(range(1, 6)), "u2q1")
check_num("u3q1 2nd comp of 3*[2,1]+(-1)*[1,1]", 3 * 1 + (-1) * 1, "u3q1")
check_num("u4q2 dimension of the plane", 2, "u4q2")
check_num("u5q1 ||[-5,12]||_2", math.sqrt(25 + 144), "u5q1")
check_num("u5q2 ||[-5,12]||_1", 5 + 12, "u5q2")
check_num("u6q1 [2,3].[4,-1]", 2 * 4 + 3 * (-1), "u6q1")
check_num("u7q1 2nd comp of [[2,0],[1,3]]x, x=[1,2]", 1 * 1 + 3 * 2, "u7q1")
check_num("u8q1 c = ([6,3].[2,0])/([2,0].[2,0])", (6 * 2 + 3 * 0) / (2 * 2 + 0 * 0), "u8q1")
check_num("u9q1 rank of [[2,4],[1,2],[0,0]] (col2=2*col1)", 1, "u9q1")

print("\n--- Faded-ladder keys (MULTI) ---")
MULTI_EXPECT = {
    "l1r2": {"a": 2 * 4, "b": 2 + 4 + 6 + 8},
    "l1r3": {"a": (1 + 1) + (2 + 1) + (3 + 1)},
    "l2r2": {"a": math.sqrt(36 + 64), "b": 6 + 8},
    "l2r3": {"a": math.sqrt(1 + 4 + 4), "b": 1 + 2 + 2},
    "l3r2": {"a": 2 * 4, "b": 2 * 4 + (-1) * 3},
    "l3r3": {"a": 1 * 3 + 0 * 5 + (-2) * 1},
    "l4r2": {"a": 3 * 1 + 4 * 0, "b": (3 * 1 + 4 * 0) / (1 * 1 + 0 * 0)},
    "l4r3": {"a": (2 * 1 + 3 * 1) / (1 * 1 + 1 * 1)},
}
for mid, ans in MULTI_EXPECT.items():
    m = re.search(mid + r":\{.*?ans:\{a:(-?[\d.]+)(?:,b:(-?[\d.]+))?", html)
    if not m:
        fails.append(f"{mid}: artifact MULTI key not found")
        print(f"[FAIL] {mid}: artifact MULTI key not found")
        continue
    emb = {"a": float(m.group(1))}
    if m.group(2) is not None:
        emb["b"] = float(m.group(2))
    ok = all(eq(ans[k], emb[k]) for k in ans) and set(ans) == set(emb)
    if ok:
        passed += 1
        print(f"[OK]   {mid}: independent = {ans} | artifact = {emb}")
    else:
        fails.append(f"{mid}: independent {ans} != artifact {emb}")
        print(f"[FAIL] {mid}: independent {ans} != artifact {emb}")

print("\n--- Mastery numeric keys (MAST) ---")
check_num("m2 sum i^2, i=1..4", 1 + 4 + 9 + 16, "m2")
check_num("m3 [4,-2].[1,3]", 4 * 1 + (-2) * 3, "m3")
check_num("m4 ||[2,-3,6]||_2", math.sqrt(4 + 9 + 36), "m4")
c_m9 = (5 * 3 + 2 * 0) / (3 * 3 + 0 * 0)
check_num("m9 shadow x of [5,2] on [3,0] (= c*3, c=15/9)", c_m9 * 3, "m9")

print("\n--- MCQ correct-answer letters (keyed truth independently re-derived) ---")
MCQ_EXPECT = {
    "u1q1": "b", "u1q3": "b", "u2q2": "b", "u2q3": "b", "u3q2": "b", "u3q3": "c",
    "u4q1": "b", "u4q3": "c", "u5q3": "b", "u6q2": "c", "u6q3": "a", "u7q2": "b",
    "u7q3": "b", "u8q2": "a", "u8q3": "b", "u9q2": "b", "u9q3": "c",
    "m1": "b", "m5": "b", "m6": "b", "m7": "b", "m8": "c", "m10": "a", "m11": "b",
}
for qid, letter in MCQ_EXPECT.items():
    m = re.search(qid + r":\{t:'mcq',c:'([abc])'", html)
    if m and m.group(1) == letter:
        passed += 1
        print(f"[OK]   {qid}: keyed correct option '{letter}' matches re-derived truth")
    else:
        got = m.group(1) if m else "MISSING"
        fails.append(f"{qid}: keyed {got} != re-derived {letter}")
        print(f"[FAIL] {qid}: keyed {got} != re-derived {letter}")

print("\n--- Match solution ---")
m = re.search(r"var sol=\{mt1:'(\w+)',mt2:'(\w+)',mt3:'(\w+)',mt4:'(\w+)'\}", html)
sol_expected = ("sim", "reg", "fit", "red")
if m and tuple(m.groups()) == sol_expected:
    passed += 1
    print("[OK]   match sol: sim/reg/fit/red (dot->similarity, L1->regularization, LS->fit, rank->redundancy)")
else:
    fails.append("match sol mismatch")
    print(f"[FAIL] match sol: artifact {m.groups() if m else None} != {sol_expected}")

print("\n--- Worked examples and prose-embedded numbers ---")
check_str("Sigma worked example 5+3+8+1", "5+3+8+1 = 17", r"5\+3\+8\+1 = 17")
check_str("Weighted-sum default 2*3+(-1)*4+0.5", "= 2.5", r"2·3 \+ \(−1\)·4 \+ 0\.5 = 2\.5")
check_str("Dot worked [1,2].[3,4]", "3+8 = 11", r"3 \+ 8 = 11")
check_str("Orthogonality [1,2].[2,-1]", "2-2 = 0", r"\[1, 2\]·\[2, −1\] = 2 − 2 = 0")
check_str("Magnitude confound long pair", "10000", r"\[100, 0\]·\[100, 0\] = 10 000")
check_str("Magnitude confound perpendicular pair", "12-12 = 0", r"\[3, 4\]·\[4, −3\] = 0")
check_str("Norm worked [3,4] L2", "5", r"√25 = <b>5</b>")
check_str("Norm worked [3,4] L1", "7", r"3 \+ 4 = <b>7</b>")
check_str("Dependence worked 2*[1,2]+(-1)*[2,4]", "[0,0]", r"2·\[1,2\] \+ \(−1\)·\[2,4\] = \[0,0\]")
check_str("Ax worked row1", "1*3+2*1 = 5", r"1·3 \+ 2·1 = 5")
check_str("Ax worked row2", "0*3+1*1 = 1", r"0·3 \+ 1·1 = 1")
check_str("AB != BA worked AB", "[[2,1],[4,3]]", r"\[\[2, 1\], \[4, 3\]\]")
check_str("AB != BA worked BA", "[[3,4],[1,2]]", r"\[\[3, 4\], \[1, 2\]\]")
check_str("Transpose worked", "[[1,4],[2,5],[3,6]]", r"\[\[1, 4\], \[2, 5\], \[3, 6\]\]")
check_str("Projection worked [2,2] on [4,0]", "c=0.5 shadow [2,0] e [0,2]", r"c = 0\.5\. Shadow = 0\.5·\[4,0\] = <b>\[2, 0\]</b>; leftover e = \[0, 2\]")
check_str("Least-squares m", "18/20 = 0.9", r"18/20 = 0\.9")
check_str("Least-squares c", "(13-9)/4 = 1.0", r"\(13 − 9\)/4 = 1\.0")
check_str("Least-squares SSE", "0.01+0.04+0.49+0.16 = 0.70", r"SSE = 0\.70")
check_str("m9 rule shadow", "15/9 = 5/3 -> [5,0]", r"15/9 = 5/3; shadow = \(5/3\)·\[3,0\] = \[5,0\]")
check_str("Gate G2 product", "4*3*cos120 = -6", r"cos 120° ≈ −0\.5, so the product is −6")
check_str("u6q2 cos150 reading", "cos150 = -0.866 -> -0.87", r"cos 150° ≈ −0\.87")
check_str("cos(theta) default w7", "5/sqrt(50) = 0.707", r"cos θ ≈ 0\.707")

print("\n--- Widget default readouts (live-computed values, print-note statements) ---")
check_str("W1 3x2 = 6 numbers", "3*2 = 6", r"6 numbers")
check_str("W2 default sum", "1+2+3+4 = 10", r"1\+2\+3\+4 = 10")
check_str("W6 default ratio", "7/5 = 1.4", r"ratio 1\.40")
check_str("W7 default", "dot 5, theta 45", r"dot = 5, θ = 45°")
check_str("W9 default AB/BA", "AB [[2,1],[1,0]] BA [[0,1],[1,2]]", r"AB = \[\[2,1\],\[1,0\]\] but BA = \[\[0,1\],\[1,2\]\]")
check_str("W11 default", "c 0.5 shadow [2,0] leftover [0,2]", r"c = 0\.5, shadow \[2,0\], leftover \[0,2\], and e·y = 0")
check_str("W12 default line", "y = 0.9x + 1.0", r"y = 0\.9x \+ 1\.0, SSE = 0\.70")
check_str("W13 default rank", "cols [1,2,3],[2,1,0] rank 2", r"rank 2 \(full for 3×2\)")

print("\n--- Independent widget-math recomputation (values the JS must produce live) ---")
xs = [1, 2, 3, 4]
n = 4
ys = [2, 3, 3, 5]
sx, sy = sum(xs), sum(ys)
sxy, sxx = sum(x * y for x, y in zip(xs, ys)), sum(x * x for x in xs)
m_ls = (n * sxy - sx * sy) / (n * sxx - sx * sx)
c_ls = (sy - m_ls * sx) / n
sse_ls = sum((y - (m_ls * x + c_ls)) ** 2 for x, y in zip(xs, ys))
print(f"       W12 default least squares: m={m_ls:g} c={c_ls:g} SSE={sse_ls:g} (artifact states 0.9 / 1.0 / 0.70)")
if eq(m_ls, 0.9) and eq(c_ls, 1.0) and eq(sse_ls, 0.7):
    passed += 1
    print("[OK]   W12 default least-squares recomputation matches stated 0.9/1.0/0.70")
else:
    fails.append("W12 default least-squares mismatch")
    print("[FAIL] W12 default least-squares mismatch")
ys_out = [2, 3, 3, 8]
sy_o = sum(ys_out)
sxy_o = sum(x * y for x, y in zip(xs, ys_out))
m_o = (n * sxy_o - sx * sy_o) / (n * sxx - sx * sx)
c_o = (sy_o - m_o * sx) / n
sse_o = sum((y - (m_o * x + c_o)) ** 2 for x, y in zip(xs, ys_out))
print(f"       W12 outlier preset recomputation: m={m_o:g} c={c_o:g} SSE={sse_o:g} (live on click; no prose claim)")
v1 = [2.5 * math.cos(math.radians(20)), 2.5 * math.sin(math.radians(20))]
v2 = [2 * math.cos(math.radians(80)), 2 * math.sin(math.radians(80))]
print(f"       W4 default vectors: v1=[{v1[0]:.3f}, {v1[1]:.3f}] v2=[{v2[0]:.3f}, {v2[1]:.3f}] (live-computed)")
dot_w7 = 2 * 1 + 1 * 3
cos_w7 = dot_w7 / (math.sqrt(5) * math.sqrt(10))
th_w7 = math.degrees(math.acos(cos_w7))
print(f"       W7 default: dot={dot_w7:g} cos={cos_w7:.4f} theta={th_w7:.1f}deg (artifact states 5 / 0.707 / 45deg)")
if eq(dot_w7, 5) and abs(cos_w7 - 0.707) < 0.001 and eq(th_w7, 45):
    passed += 1
    print("[OK]   W7 default dot/angle recomputation matches stated values")
else:
    fails.append("W7 default recomputation mismatch")
    print("[FAIL] W7 default recomputation mismatch")

print(f"\n=== Result: {passed} passed, {len(fails)} failed ===")
if fails:
    for f in fails:
        print("  FAILED:", f)
    sys.exit(1)
sys.exit(0)

```

**Output (verbatim):**

```
=== Independent recomputation — CAN-2026-0009 (v10) ===

--- Unit-check numeric keys (QA) ---
[OK]   u1q2 features of a 4x3 table (cols): independent = 3 | artifact = 3 
[OK]   u2q1 sum i=1..5: independent = 15 | artifact = 15 
[OK]   u3q1 2nd comp of 3*[2,1]+(-1)*[1,1]: independent = 2 | artifact = 2 
[OK]   u4q2 dimension of the plane: independent = 2 | artifact = 2 
[OK]   u5q1 ||[-5,12]||_2: independent = 13 | artifact = 13 
[OK]   u5q2 ||[-5,12]||_1: independent = 17 | artifact = 17 
[OK]   u6q1 [2,3].[4,-1]: independent = 5 | artifact = 5 
[OK]   u7q1 2nd comp of [[2,0],[1,3]]x, x=[1,2]: independent = 7 | artifact = 7 
[OK]   u8q1 c = ([6,3].[2,0])/([2,0].[2,0]): independent = 3 | artifact = 3 
[OK]   u9q1 rank of [[2,4],[1,2],[0,0]] (col2=2*col1): independent = 1 | artifact = 1 

--- Faded-ladder keys (MULTI) ---
[OK]   l1r2: independent = {'a': 8, 'b': 20} | artifact = {'a': 8.0, 'b': 20.0}
[OK]   l1r3: independent = {'a': 9} | artifact = {'a': 9.0}
[OK]   l2r2: independent = {'a': 10.0, 'b': 14} | artifact = {'a': 10.0, 'b': 14.0}
[OK]   l2r3: independent = {'a': 3.0, 'b': 5} | artifact = {'a': 3.0, 'b': 5.0}
[OK]   l3r2: independent = {'a': 8, 'b': 5} | artifact = {'a': 8.0, 'b': 5.0}
[OK]   l3r3: independent = {'a': 1} | artifact = {'a': 1.0}
[OK]   l4r2: independent = {'a': 3, 'b': 3.0} | artifact = {'a': 3.0, 'b': 3.0}
[OK]   l4r3: independent = {'a': 2.5} | artifact = {'a': 2.5}

--- Mastery numeric keys (MAST) ---
[OK]   m2 sum i^2, i=1..4: independent = 30 | artifact = 30 
[OK]   m3 [4,-2].[1,3]: independent = -2 | artifact = -2 
[OK]   m4 ||[2,-3,6]||_2: independent = 7 | artifact = 7 
[OK]   m9 shadow x of [5,2] on [3,0] (= c*3, c=15/9): independent = 5 | artifact = 5 

--- MCQ correct-answer letters (keyed truth independently re-derived) ---
[OK]   u1q1: keyed correct option 'b' matches re-derived truth
[OK]   u1q3: keyed correct option 'b' matches re-derived truth
[OK]   u2q2: keyed correct option 'b' matches re-derived truth
[OK]   u2q3: keyed correct option 'b' matches re-derived truth
[OK]   u3q2: keyed correct option 'b' matches re-derived truth
[OK]   u3q3: keyed correct option 'c' matches re-derived truth
[OK]   u4q1: keyed correct option 'b' matches re-derived truth
[OK]   u4q3: keyed correct option 'c' matches re-derived truth
[OK]   u5q3: keyed correct option 'b' matches re-derived truth
[OK]   u6q2: keyed correct option 'c' matches re-derived truth
[OK]   u6q3: keyed correct option 'a' matches re-derived truth
[OK]   u7q2: keyed correct option 'b' matches re-derived truth
[OK]   u7q3: keyed correct option 'b' matches re-derived truth
[OK]   u8q2: keyed correct option 'a' matches re-derived truth
[OK]   u8q3: keyed correct option 'b' matches re-derived truth
[OK]   u9q2: keyed correct option 'b' matches re-derived truth
[OK]   u9q3: keyed correct option 'c' matches re-derived truth
[OK]   m1: keyed correct option 'b' matches re-derived truth
[OK]   m5: keyed correct option 'b' matches re-derived truth
[OK]   m6: keyed correct option 'b' matches re-derived truth
[OK]   m7: keyed correct option 'b' matches re-derived truth
[OK]   m8: keyed correct option 'c' matches re-derived truth
[OK]   m10: keyed correct option 'a' matches re-derived truth
[OK]   m11: keyed correct option 'b' matches re-derived truth

--- Match solution ---
[OK]   match sol: sim/reg/fit/red (dot->similarity, L1->regularization, LS->fit, rank->redundancy)

--- Worked examples and prose-embedded numbers ---
[OK]   Sigma worked example 5+3+8+1: 5+3+8+1 = 17
[OK]   Weighted-sum default 2*3+(-1)*4+0.5: = 2.5
[OK]   Dot worked [1,2].[3,4]: 3+8 = 11
[OK]   Orthogonality [1,2].[2,-1]: 2-2 = 0
[OK]   Magnitude confound long pair: 10000
[OK]   Magnitude confound perpendicular pair: 12-12 = 0
[OK]   Norm worked [3,4] L2: 5
[OK]   Norm worked [3,4] L1: 7
[OK]   Dependence worked 2*[1,2]+(-1)*[2,4]: [0,0]
[OK]   Ax worked row1: 1*3+2*1 = 5
[OK]   Ax worked row2: 0*3+1*1 = 1
[OK]   AB != BA worked AB: [[2,1],[4,3]]
[OK]   AB != BA worked BA: [[3,4],[1,2]]
[OK]   Transpose worked: [[1,4],[2,5],[3,6]]
[OK]   Projection worked [2,2] on [4,0]: c=0.5 shadow [2,0] e [0,2]
[OK]   Least-squares m: 18/20 = 0.9
[OK]   Least-squares c: (13-9)/4 = 1.0
[OK]   Least-squares SSE: 0.01+0.04+0.49+0.16 = 0.70
[OK]   m9 rule shadow: 15/9 = 5/3 -> [5,0]
[OK]   Gate G2 product: 4*3*cos120 = -6
[OK]   u6q2 cos150 reading: cos150 = -0.866 -> -0.87
[OK]   cos(theta) default w7: 5/sqrt(50) = 0.707

--- Widget default readouts (live-computed values, print-note statements) ---
[OK]   W1 3x2 = 6 numbers: 3*2 = 6
[OK]   W2 default sum: 1+2+3+4 = 10
[OK]   W6 default ratio: 7/5 = 1.4
[OK]   W7 default: dot 5, theta 45
[OK]   W9 default AB/BA: AB [[2,1],[1,0]] BA [[0,1],[1,2]]
[OK]   W11 default: c 0.5 shadow [2,0] leftover [0,2]
[OK]   W12 default line: y = 0.9x + 1.0
[OK]   W13 default rank: cols [1,2,3],[2,1,0] rank 2

--- Independent widget-math recomputation (values the JS must produce live) ---
       W12 default least squares: m=0.9 c=1 SSE=0.7 (artifact states 0.9 / 1.0 / 0.70)
[OK]   W12 default least-squares recomputation matches stated 0.9/1.0/0.70
       W12 outlier preset recomputation: m=1.8 c=-0.5 SSE=5.8 (live on click; no prose claim)
       W4 default vectors: v1=[2.349, 0.855] v2=[0.347, 1.970] (live-computed)
       W7 default: dot=5 cos=0.7071 theta=45.0deg (artifact states 5 / 0.707 / 45deg)
[OK]   W7 default dot/angle recomputation matches stated values

=== Result: 79 passed, 0 failed ===
```

### B.2 Structural conformance — `conformance.py` (Audit 5)

```python
#!/usr/bin/env python3
"""Structural conformance audit — CAN-2026-0009 (linear-algebra-foundations-v10.html).

Audit 5 mechanical evidence for RUN-20260904-0001: canvas engineering contract
(ADR-0013), component layout contracts (standard 10.6-10.8), design tokens,
assessment modality, glossary shape, jargon discipline, and identity re-pins.
Read-only; zero dependencies; exit 0 = all checks pass.
"""
import re
import sys

HTML = "/Users/kashifrezwi/Developer/interactive-notes/content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v10.html"
html = open(HTML, encoding="utf-8").read()
fails = []
oks = 0


def chk(name, cond, detail=""):
    global oks
    if cond:
        oks += 1
        print(f"[OK]   {name} {detail}")
    else:
        fails.append(name)
        print(f"[FAIL] {name} {detail}")


print("=== Structural conformance — CAN-2026-0009 (v10) ===\n")

# --- Identity re-pins (run-specific) ---
chk("provenance header pinned to CAN-2026-0009 / RUN-20260904-0001",
    "candidate: CAN-2026-0009" in html and "run: RUN-20260904-0001" in html
    and "inputs: CM-2026-0007 / LP-2026-0008 / XS-2026-0008" in html)
chk("title carries v10 (inherited v9 title defect repaired)",
    "<title>Mathematical Foundations &amp; Linear Algebra — Interactive Notes (v10)</title>" in html)
chk("storage key re-pinned to laf10 (getItem + setItem + removeItem)",
    html.count("'laf10'") == 3 and "laf9" not in html)

# --- Canvas engineering contract (ADR-0013) ---
canvases = len(re.findall(r"<canvas\b", html))
resize_listeners = len(re.findall(r"addEventListener\('resize'", html))
chk("resize listener count >= canvas count", resize_listeners >= canvases,
    f"({resize_listeners} listeners, {canvases} canvases)")
chk("exactly 9 canvas widgets", canvases == 9)
makeview_calls = len(re.findall(r"makeView\(", html))
chk("10 makeView occurrences (1 definition + 9 per-widget calls)", makeview_calls == 10, f"({makeview_calls})")
chk("makeView canonical signature present",
    "function makeView(canvasId, xMin, xMax, yMin, yMax){" in html)
chk("DPR scaling via setTransform(dpr,0,0,dpr,0,0)", "ctx.setTransform(dpr, 0, 0, dpr, 0, 0)" in html)
chk("clientWidth measured at draw time", "cv.clientWidth || 640" in html)
chk("CSS height from mathematical aspect ratio", 'cv.style.height = ch + "px"' in html)
chk("normalized X/Y transforms", "return (x - xMin) / (xMax - xMin);" in html
    and "return 1 - (y - yMin) / (yMax - yMin);" in html)
chk("no hardcoded pixel-offset helpers (px = 50 + ... anti-pattern)",
    not re.search(r"var px\s*=\s*function\(x\)\{return 50", html))
chk("signed angular difference with wrapping for arcs",
    "if(dAng>Math.PI)dAng-=2*Math.PI" in html and "if(dAng<-Math.PI)dAng+=2*Math.PI" in html)
chk("no Math.max/Math.min angle-arc anti-pattern",
    not re.search(r"ctx\.arc\([^)]*Math\.max\(a", html))
legends = len(re.findall(r'<div class="legend-inline">', html))
chk("legend-inline on every multi-entity canvas (9)", legends == 9, f"({legends})")
chk("canvas CSS baseline (canvas.viz 100% width)", "canvas.viz{width:100%" in html)

# --- Component layout contracts (standard 10.6-10.7) ---
range_inputs = len(re.findall(r'<input type="range"', html))
slider_tracks = len(re.findall(r'<div class="slider-track">', html))
slider_controls = len(re.findall(r'<div class="slider-control">', html))
chk("every range input encapsulated in .slider-track (per-element 10.6)",
    range_inputs == slider_tracks, f"({range_inputs} sliders, {slider_tracks} tracks)")
chk(".slider-control wrapper count == slider count", slider_controls == range_inputs,
    f"({slider_controls})")
ctrl_grids = len(re.findall(r'<div class="ctrl-grid">', html))
chk(".ctrl-grid containers present (>= 6 widget grids)", ctrl_grids >= 6, f"({ctrl_grids})")
chk("tabular-nums slider values", "font-variant-numeric:tabular-nums" in html)
chk("no bare legacy range-in-label pattern remains",
    not re.search(r"<label>[^<]*<input type=\"range\"", html))
option_stacks = len(re.findall(r'<div class="option-stack">', html))
option_items = len(re.findall(r'<label class="option-item"', html))
chk("option-stack vertical layout on all option sets", option_stacks >= 30 and option_items >= 60,
    f"({option_stacks} stacks, {option_items} items)")

# --- Callout discipline (10.8) ---
units = re.findall(r'<section class="unit"[^>]*id="([^"]+)"[^>]*>(.*?)</section>', html, re.S)
over = []
for uid, body in units:
    c = len(re.findall(r'class="callout', body))
    if c > 1:
        over.append((uid, c))
chk("callout density <= 1 per unit", not over, f"(units checked: {len(units)}, violators: {over})")

# --- Assessment modality (1.4) ---
chk("zero <textarea> elements", "textarea" not in html)
chk("no deferred-jargon cop-out phrases",
    not re.search(r"words belong to a later course|promise for a later course|a later course makes this precise", html, re.I))

# --- Formula manifest & glossary ---
formulas = len(re.findall(r'<div class="formula">', html))
symkeys = len(re.findall(r'class="symkey"', html))
chk("16 .formula blocks (XS-2026-0008 Formula Manifest)", formulas == 16, f"({formulas})")
chk("symbol keys annotate formulas", symkeys >= 16, f"({symkeys})")
gitems = len(re.findall(r'<div class="gitem"', html))
chk("40 glossary entries", gitems == 40, f"({gitems})")
fields = {f: len(re.findall(r'<p><span class="fl">' + f + r':</span>', html))
          for f in ("Simple", "Precise", "Intuition", "Example", "Related", "Where it appears")}
chk("6-field glossary shape on every entry",
    all(v == 40 for v in fields.values()), str(fields))
gterms = set(re.findall(r'data-term="([^"]+)"', html))
gids = set(re.findall(r'<div class="gitem" id="([^"]+)"', html))
chk("every in-text glossary term resolves to a glossary entry", gterms <= gids,
    f"(terms: {len(gterms)}, unresolved: {sorted(gterms - gids)})")

# --- Design tokens (10.1) ---
root = re.search(r":root\{(.*?)\}", html, re.S).group(1)
tokens = len(re.findall(r"--[a-z0-9-]+:", root))
chk("pinned design token set (>= 25 custom properties)", tokens >= 25, f"({tokens})")
chk("16px+ body font with 1.6+ line-height",
    re.search(r"font-size:1[6-9]" + r"(\.\d+)?px;line-height:1\.6", html) is not None)
chk("frosted-glass sticky nav", "backdrop-filter:blur(6px)" in html.replace(" ", ""))
chk("single-line horizontal scroll nav (no wrap)",
    re.search(r"\.topnav-inner\{[^}]*overflow-x:auto[^}]*\}", html) is not None)
chk("pill-style nav links", "border-radius:999px" in html)
chk("aria-current active state styling", 'a[aria-current="true"]' in html)
chk("left-aligned header with meta chips",
    re.search(r"header\.page-head\{[^}]*text-align:left", html) is not None and 'class="chip"' in html)
chk("reduced-motion honored", "prefers-reduced-motion:reduce" in html)
chk("print stylesheet present", "@media print" in html)
chk("skip link present", 'class="skip-link"' in html)
chk("colophon is the page's only closing element",
    html.rstrip().endswith("</html>")
    and '<footer class="colophon">' in html
    and "AI-generated, so mistakes can sneak in" in html
    and "Built with ♥ using Interactive Notes" in html)

# --- Zero-dependency ---
ext = re.findall(r'(?:src|href)="(?:https?:)?//[^"]+"', html)
chk("zero external references", not ext, str(ext[:3]))

print(f"\n=== Result: {oks} passed, {len(fails)} failed ===")
if fails:
    for f in fails:
        print("  FAILED:", f)
    sys.exit(1)
sys.exit(0)

```

**Output (verbatim):**

```
=== Structural conformance — CAN-2026-0009 (v10) ===

[OK]   provenance header pinned to CAN-2026-0009 / RUN-20260904-0001 
[OK]   title carries v10 (inherited v9 title defect repaired) 
[OK]   storage key re-pinned to laf10 (getItem + setItem + removeItem) 
[OK]   resize listener count >= canvas count (9 listeners, 9 canvases)
[OK]   exactly 9 canvas widgets 
[OK]   10 makeView occurrences (1 definition + 9 per-widget calls) (10)
[OK]   makeView canonical signature present 
[OK]   DPR scaling via setTransform(dpr,0,0,dpr,0,0) 
[OK]   clientWidth measured at draw time 
[OK]   CSS height from mathematical aspect ratio 
[OK]   normalized X/Y transforms 
[OK]   no hardcoded pixel-offset helpers (px = 50 + ... anti-pattern) 
[OK]   signed angular difference with wrapping for arcs 
[OK]   no Math.max/Math.min angle-arc anti-pattern 
[OK]   legend-inline on every multi-entity canvas (9) (9)
[OK]   canvas CSS baseline (canvas.viz 100% width) 
[OK]   every range input encapsulated in .slider-track (per-element 10.6) (22 sliders, 22 tracks)
[OK]   .slider-control wrapper count == slider count (22)
[OK]   .ctrl-grid containers present (>= 6 widget grids) (8)
[OK]   tabular-nums slider values 
[OK]   no bare legacy range-in-label pattern remains 
[OK]   option-stack vertical layout on all option sets (38 stacks, 92 items)
[OK]   callout density <= 1 per unit (units checked: 12, violators: [])
[OK]   zero <textarea> elements 
[OK]   no deferred-jargon cop-out phrases 
[OK]   16 .formula blocks (XS-2026-0008 Formula Manifest) (16)
[OK]   symbol keys annotate formulas (27)
[OK]   40 glossary entries (40)
[OK]   6-field glossary shape on every entry {'Simple': 40, 'Precise': 40, 'Intuition': 40, 'Example': 40, 'Related': 40, 'Where it appears': 40}
[OK]   every in-text glossary term resolves to a glossary entry (terms: 14, unresolved: [])
[OK]   pinned design token set (>= 25 custom properties) (25)
[OK]   16px+ body font with 1.6+ line-height 
[OK]   frosted-glass sticky nav 
[OK]   single-line horizontal scroll nav (no wrap) 
[OK]   pill-style nav links 
[OK]   aria-current active state styling 
[OK]   left-aligned header with meta chips 
[OK]   reduced-motion honored 
[OK]   print stylesheet present 
[OK]   skip link present 
[OK]   colophon is the page's only closing element 
[OK]   zero external references []

=== Result: 42 passed, 0 failed ===
```

### B.3 Handler-level behavioral simulation — `simulate_v10.js` (Audit 5 + adversarial gate)

```javascript
#!/usr/bin/env node
/* Handler-level behavioral simulation — CAN-2026-0009 (linear-algebra-foundations-v10.html).
 * Audit 5 + adversarial-gate evidence for RUN-20260904-0001 (ADR-0009 methods 1-3):
 * loads the artifact's own <script> engine against a minimal DOM shim and drives
 * gate commitment, grading boundaries, confident-miss routing, corrupted-state reset,
 * hint toggling, matching, and the glossary popover. Exit 0 = all traces pass.
 */
"use strict";
const fs = require("fs");

const HTML_PATH = "/Users/kashifrezwi/Developer/interactive-notes/content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v10.html";
const html = fs.readFileSync(HTML_PATH, "utf-8");
const scriptMatch = html.match(/<script>\s*([\s\S]*?)\s*<\/script>/);
if (!scriptMatch) { console.error("no script found"); process.exit(1); }
const artifactScript = scriptMatch[1];

let failures = 0, passes = 0;
function trace(name, cond, detail) {
  if (cond) { passes++; console.log("[OK]   " + name + (detail ? " — " + detail : "")); }
  else { failures++; console.log("[FAIL] " + name + (detail ? " — " + detail : "")); }
}

/* ---------- minimal DOM shim ---------- */
const elements = {};
const checkedInputs = {};   // name -> value, set by the test driver
const docListeners = {};    // type -> [handlers]
const ctxStub = new Proxy({}, { get: (t, k) => (k === "canvas" ? undefined : function () {}) });
function makeElement(id) {
  const listeners = {};
  const el = {
    id: id, value: "", textContent: "", innerHTML: "", hidden: false,
    className: "", style: {}, width: 0, height: 0, clientWidth: 640, clientHeight: 320,
    classList: {
      _set: new Set(),
      add(c) { this._set.add(c); },
      remove(c) { this._set.delete(c); },
      contains(c) { return this._set.has(c); },
    },
    addEventListener(t, fn) { (listeners[t] = listeners[t] || []).push(fn); },
    dispatch(t, ev) { (listeners[t] || []).forEach((f) => f(ev || {})); },
    getAttribute(a) { return a === "data-term" ? "g-vector" : null; },
    setAttribute(a, v) { if (a === "aria-current") el._ariaCurrent = v; },
    focus() {}, scrollIntoView() {},
    getBoundingClientRect() { return { top: 0, bottom: 10, left: 0, right: 10 }; },
    contains() { return false; },
    getContext() { return ctxStub; },
    onclick: null,
  };
  return el;
}
function el(id) { if (!elements[id]) elements[id] = makeElement(id); return elements[id]; }
const document = {
  getElementById(id) { if (!elements[id]) elements[id] = makeElement(id); return elements[id]; },
  querySelector(sel) {
    const m = sel.match(/^input\[name="([^"]+)"\]:checked$/);
    if (m && Object.prototype.hasOwnProperty.call(checkedInputs, m[1])) {
      return { value: checkedInputs[m[1]] };
    }
    return null;
  },
  querySelectorAll() { return []; },
  addEventListener(t, fn) { (docListeners[t] = docListeners[t] || []).push(fn); },
};
const storage = {};
const localStorage = {
  getItem(k) { return Object.prototype.hasOwnProperty.call(storage, k) ? storage[k] : null; },
  setItem(k, v) { storage[k] = String(v); },
  removeItem(k) { delete storage[k]; },
};
let reloaded = false;
const location = { reload() { reloaded = true; } };
const window = { devicePixelRatio: 2, innerWidth: 1024, scrollY: 0, addEventListener() {} };
globalThis.document = document;
globalThis.localStorage = localStorage;
globalThis.location = location;
globalThis.window = window;
globalThis.IntersectionObserver = class { observe() {} disconnect() {} };

/* ---------- pre-seed control defaults parsed from the artifact HTML ---------- */
let m;
const inputRe = /<input[^>]*id="([^"]+)"[^>]*value="([^"]*)"/g;
while ((m = inputRe.exec(html)) !== null) {
  if (!elements[m[1]]) elements[m[1]] = makeElement(m[1]);
  elements[m[1]].value = m[2];
}
const selectRe = /<select[^>]*id="([^"]+)"[^>]*>\s*<option value="([^"]+)"/g;
while ((m = selectRe.exec(html)) !== null) {
  if (!elements[m[1]]) elements[m[1]] = makeElement(m[1]);
  elements[m[1]].value = m[2]; // a select defaults to its first option
}
/* elements shipping with the hidden attribute (hint boxes, feedback lines) */
const hiddenRe = /<([a-z]+)[^>]*id="([^"]+)"[^>]*\shidden/g;
while ((m = hiddenRe.exec(html)) !== null) {
  if (!elements[m[2]]) elements[m[2]] = makeElement(m[2]);
  elements[m[2]].hidden = true;
}

/* ---------- load the artifact engine (against corrupted persisted state) ---------- */
localStorage.setItem("laf10", '{"weak":{"garbage topic":"missed"},"done":null,"graded":x'); // invalid JSON tail
try {
  eval(artifactScript);
} catch (e) {
  console.error("[FAIL] engine load threw: " + e.message);
  process.exit(1);
}
trace("artifact engine loads and initializes against the DOM shim without throwing", true);
trace("engine recovers from corrupted persisted state (invalid JSON falls back to clean defaults)",
  /Nothing yet/.test(elements["reviewList"].innerHTML));

/* ---------- 1. Prediction gates: commitment required ---------- */
trace("engine applies gated-hide to all 3 gated widgets at init",
  elements["w4"].classList.contains("gated-hide")
    && elements["w7"].classList.contains("gated-hide")
    && elements["w11"].classList.contains("gated-hide"));
window.__commit("g1");
trace("gate g1 refuses commit without a selection (widget stays hidden)",
  elements["w4"].classList.contains("gated-hide")
    && /Pick an option/.test(elements["fb-g1"].innerHTML));
checkedInputs["g1"] = "line";
window.__commit("g1");
trace("gate g1 reveals the manipulable only after a committed choice",
  !elements["w4"].classList.contains("gated-hide"));
trace("gate g1 feedback is option-specific (names the (a + 2b)v1 collapse for 'line')",
    /\(a \+ 2b\)/.test(elements["fb-g1"].innerHTML));
checkedInputs["g2"] = "pos"; window.__commit("g2");
trace("gate g2 wrong-choice feedback differentiates (names the trap for 'pos')",
  /trap/.test(elements["fb-g2"].innerHTML) && !elements["w7"].classList.contains("gated-hide"));
checkedInputs["g3"] = "perp"; window.__commit("g3");
trace("gate g3 reveals w11 after commit", !elements["w11"].classList.contains("gated-hide"));

/* ---------- 2. Numeric grading boundaries ---------- */
window.__grade("u2q1");
trace("numeric grade refuses empty input", /Type a number first/.test(elements["fb-u2q1"].innerHTML));
el("in-u2q1").value = "15"; window.__grade("u2q1");
trace("numeric grade accepts exact answer 15", /Correct/.test(elements["fb-u2q1"].innerHTML)
  && elements["fb-u2q1"].className.indexOf("ok") !== -1);
el("in-u2q1").value = "15.0000001"; window.__grade("u2q1");
trace("numeric grade rejects 1e-7 deviation (tolerance boundary)",
  elements["fb-u2q1"].className.indexOf("no") !== -1);
el("in-u2q1").value = "15.0000000001"; window.__grade("u2q1");
trace("numeric grade accepts sub-1e-9 float noise",
  elements["fb-u2q1"].className.indexOf("ok") !== -1);
el("in-m3").value = "-2"; checkedInputs["cf-m3"] = "sure"; window.__gradeM("m3");
trace("mastery numeric m3 grades -2 correct", /Correct/.test(elements["fb-m3"].innerHTML));

/* ---------- 3. MCQ grading + review routing ---------- */
window.__grade("u1q1");
trace("MCQ grade refuses empty selection", /Choose an option first/.test(elements["fb-u1q1"].innerHTML));
checkedInputs["u1q1"] = "a"; window.__grade("u1q1");
trace("MCQ wrong choice marks miss + routes topic to review list",
  elements["fb-u1q1"].className.indexOf("no") !== -1
    && /Scalars, vectors, matrices/.test(elements["reviewList"].innerHTML));
checkedInputs["u1q1"] = "b"; window.__grade("u1q1");
trace("MCQ correct choice clears the topic from the review list",
  elements["fb-u1q1"].className.indexOf("ok") !== -1
    && !/Scalars, vectors, matrices \(Unit 1\) — missed/.test(elements["reviewList"].innerHTML));

/* ---------- 4. Confident-miss routing (mastery) ---------- */
el("in-m2").value = "29"; checkedInputs["cf-m2"] = "sure"; window.__gradeM("m2");
trace("confident miss on m2 routes to review flagged 'confident miss'",
  /confident miss/.test(elements["reviewList"].innerHTML));
el("in-m2").value = "30"; window.__gradeM("m2");
trace("correct m2 clears the confident-miss flag",
  !/confident miss/.test(elements["reviewList"].innerHTML));
el("in-m4").value = "6"; checkedInputs["cf-m4"] = "guessing"; window.__gradeM("m4");
trace("non-confident miss routes as plain 'missed', not confident-miss",
  /missed/.test(elements["reviewList"].innerHTML) && !/confident miss/.test(elements["reviewList"].innerHTML));

/* ---------- 5. MULTI ladder grading ---------- */
el("in-l1r2a").value = "8"; el("in-l1r2b").value = "20"; window.__gradeMulti("l1r2");
trace("ladder l1r2 grades (8, 20) correct", /Correct/.test(elements["fb-l1r2"].innerHTML));
el("in-l1r2b").value = "19"; window.__gradeMulti("l1r2");
trace("ladder l1r2 partial-wrong rejected with rule feedback",
  /Not quite/.test(elements["fb-l1r2"].innerHTML) && /2\+4\+6\+8 = 20/.test(elements["fb-l1r2"].innerHTML));

/* ---------- 6. Matching ---------- */
el("mt1").value = "sim"; el("mt2").value = "reg";
el("mt3").value = "fit"; el("mt4").value = "red";
window.__gradeMatch();
trace("match check accepts the full correct mapping", /All four matched/.test(elements["fb-match"].innerHTML));
el("mt4").value = "fit"; window.__gradeMatch();
trace("match check rejects a wrong mapping and names the row to recheck",
  /Recheck/.test(elements["fb-match"].innerHTML) && /Rank/.test(elements["fb-match"].innerHTML));

/* ---------- 7. Hints never auto-open; toggle works ---------- */
trace("hint boxes ship hidden", elements["l1r2h1"].hidden === true);
window.__hint("l1r2h1");
trace("hint toggles open on demand", elements["l1r2h1"].hidden === false);

/* ---------- 8. Explain-floor modality + self-grade handler path (engine capability) ---------- */
/* LP-2026-0008 outcome 12: the explain floor is delivered via diagnostic MCQs with
 * model-answer reveals (the @0.6.0 modality resolution); the self-grade engine branch
 * ships as capability. This trace exercises that handler path for behavioral coverage. */
const selfOk = { getAttribute: (a) => (a === "data-self" ? "mok:m9" : null) };
(docListeners["click"] || []).forEach((fn) => fn({ target: selfOk }));
trace("self-grade handler path logs a mastery item understood (engine capability)",
  /understood|Logged/.test(elements["fb-m9"].innerHTML));

/* ---------- 9. Reset from persisted state ---------- */
el("in-u5q1").value = "12"; window.__grade("u5q1");
trace("grading persists misses to storage and renders them in the review list",
  /L2 norm/.test(elements["reviewList"].innerHTML) && storage["laf10"] !== undefined);
window.__hint("l1r2h1");
elements["resetAll"].dispatch("click");
trace("reset clears laf10 storage and reloads", reloaded === true && !("laf10" in storage));

/* ---------- 10. Glossary popover ---------- */
const glossBtn = makeElement("btn-gloss");
window.__gloss(glossBtn);
trace("glossary popover opens with the term's entry", elements["popover"].hidden === false
  && elements["popover"].innerHTML.length > 0);
(docListeners["keydown"] || []).forEach((fn) => fn({ key: "Escape" }));
trace("Escape closes the popover", elements["popover"].hidden === true);

/* ---------- 11. Gate unlock is by commitment, never correctness ---------- */
checkedInputs["g1"] = "plane"; window.__commit("g1");
trace("gate reveals even for the misconception choice (commitment-based, not correctness-based)",
  !elements["w4"].classList.contains("gated-hide")
    && /misconception to fix/.test(elements["fb-g1"].innerHTML));

console.log("\n=== Simulation result: " + passes + " passed, " + failures + " failed ===");
process.exit(failures ? 1 : 0);

```

**Output (verbatim):**

```
[OK]   artifact engine loads and initializes against the DOM shim without throwing
[OK]   engine recovers from corrupted persisted state (invalid JSON falls back to clean defaults)
[OK]   engine applies gated-hide to all 3 gated widgets at init
[OK]   gate g1 refuses commit without a selection (widget stays hidden)
[OK]   gate g1 reveals the manipulable only after a committed choice
[OK]   gate g1 feedback is option-specific (names the (a + 2b)v1 collapse for 'line')
[OK]   gate g2 wrong-choice feedback differentiates (names the trap for 'pos')
[OK]   gate g3 reveals w11 after commit
[OK]   numeric grade refuses empty input
[OK]   numeric grade accepts exact answer 15
[OK]   numeric grade rejects 1e-7 deviation (tolerance boundary)
[OK]   numeric grade accepts sub-1e-9 float noise
[OK]   mastery numeric m3 grades -2 correct
[OK]   MCQ grade refuses empty selection
[OK]   MCQ wrong choice marks miss + routes topic to review list
[OK]   MCQ correct choice clears the topic from the review list
[OK]   confident miss on m2 routes to review flagged 'confident miss'
[OK]   correct m2 clears the confident-miss flag
[OK]   non-confident miss routes as plain 'missed', not confident-miss
[OK]   ladder l1r2 grades (8, 20) correct
[OK]   ladder l1r2 partial-wrong rejected with rule feedback
[OK]   match check accepts the full correct mapping
[OK]   match check rejects a wrong mapping and names the row to recheck
[OK]   hint boxes ship hidden
[OK]   hint toggles open on demand
[OK]   self-grade handler path logs a mastery item understood (engine capability)
[OK]   grading persists misses to storage and renders them in the review list
[OK]   reset clears laf10 storage and reloads
[OK]   glossary popover opens with the term's entry
[OK]   Escape closes the popover
[OK]   gate reveals even for the misconception choice (commitment-based, not correctness-based)

=== Simulation result: 31 passed, 0 failed ===
```
