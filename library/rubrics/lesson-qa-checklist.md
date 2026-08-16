# Lesson QA Checklist (six audits & adversarial gate)

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Scope:** interactive HTML lessons generated under the [lesson standard](../../docs/01-product/lesson-standard.md) and [depth-calibration contract](../../docs/01-product/depth-calibration-contract.md). **This is a verification checklist, not a scoring rubric:** numeric gates and release decisions belong solely to the [evaluation framework](../../docs/06-evaluation/evaluation-framework.md).<br>
**Execution-evidence rule (WF-008):** every checked item must cite: (a) command or method used, (b) output or observation, (c) covered element list, and (d) executor identity and pass method (scripted / manual inspection / handler simulation / browser execution) in the evaluation record. An unchecked or evidence-free box is a gap, not a pass.<br>
**Origin:** codifies the audits that produced and repaired CAN-2026-0003 (RUN-20260810-0001, EVAL-2026-0002 incl. Revision 1).

## Audit 1 — Coverage

- [ ] Content inventory exists and is complete (topics, subtopics, definitions, formulas, examples, terminology, relationships, instructor assumptions, underexplained items, missing-but-necessary items).
- [ ] Every inventory item maps to a lesson location with a disposition (included / expanded / transcribed / added-foundation / added-extension / excluded-with-reason).
- [ ] The coverage matrix is attached to the evaluation record.
- [ ] Nothing important was removed because it "looked minor".

## Audit 2 — Mathematical

- [ ] Every formula matches the source or carries a flagged correction.
- [ ] Every displayed number, widget default, worked example, ladder answer, and assessment key independently recomputed (scripted; keep the script output as evidence).
- [ ] Widget results are computed live in the page (no hard-coded outcomes).
- [ ] Edge cases behave (zero vector, parallel vectors, outlier within view, division guards).
- [ ] Canvas extrema: every canvas widget bounds its inputs (sliders, min/max) or autoscales; drive every manipulable to its extremes and confirm nothing renders off-canvas (the v2 outlier / CAN-2026-0004 typed-input defect class).
- [ ] Notation consistent (sub/superscripts, transpose, norms, radical markup with true vinculum).
- [ ] New terms introduced by the lesson (e.g. determinant, inverse) are defined, bridged, or avoided — the v2/v3 determinant defect class.

## Audit 3 — Dependency order (read-in-order pass)

- [ ] A reader starts with an empty "taught-so-far" set and reads the artifact in order.
- [ ] Every term/notation/concept is taught, bridged, or labeled EXTENSION before it is load-bearing.
- [ ] Forward references are promises, not requirements ("Unit 8 closes this loop").
- [ ] The source's own ordering defects are repaired and the repairs are labeled.
- [ ] Findings are rated: any use-before-explain = Major or higher.

## Audit 4 — Pedagogical & depth-calibration contract

- [ ] Beginner test: the declared learner can follow every unit without outside knowledge.
- [ ] Unit anatomy present: Learn (intuition first) → Predict → Explore → Practice → Check → Connect.
- [ ] Every interaction passed the five-question admission test; goals are stated; one variable at a time.
- [ ] Every unit check has $\ge 1$ constructed-response item; feedback states governing rules. **Verified unit by unit — name each unit's constructed-response item in the evidence; a recognition-only unit check is a Major (CAN-2026-0004 shipped two).**
- [ ] Mastery check: interleaved; reasoning + transfer + error-identification items; no reused worked numbers; size $\approx$ one item per content unit + 2 (pattern P-12); three-level confidence tags (`sure` / `think so` / `guessing`); $\ge 2$ explain-in-own-words items per lesson with model answers (standard §5).
- [ ] Misconceptions: each major concept's beginner error is named and tested by a real distractor **and surfaced in its own visible alert callout where the LP names one**.
- [ ] Layers/provenance: every block labeled; additions carry reasons.
- [ ] ML connections are mechanisms at learner level; no forced references.
- [ ] Cognitive load: one new idea per block; no walls of text; optional depth collapsed.
- [ ] **Depth bar (MEM-2026-0004; depth-calibration-contract.md):** every Learn block opens with a concrete intuition and a tiny worked numeric example before any widget; every unit carries a one-line lede; each computational skill named in the LP has its own full faded ladder (worked → completion → independent).
- [ ] **Lede quality (WF-011):** every unit's lede is a single informative sentence naming concept and purpose (not a section title restated as prose).
- [ ] **One-idea-per-block (WF-011):** scan blocks to verify no single block introduces $\ge 2$ ungrounded ideas simultaneously.
- [ ] **Token/badge consistency (WF-011):** every block carries exactly one valid layer badge (`CLASS CORE`/`FOUNDATION`/`DEEP DIVE`/`ML LINK`/`EXTENSION`) and one provenance tag.
- [ ] **Widget manipulability:** every Explore-badged widget has $\ge 1$ learner-manipulable variable; a widget with none is a recorded static-demo decision, never badged Explore (standard §4; CAN-2026-0004's fixed-point least-squares widget is the contrast case).
- [ ] **Gate fidelity:** prediction gates hide the manipulable until commitment; feedback differentiates by the chosen option and references the commitment (MEM-2026-0001; CAN-2026-0004's text-only, answer-independent gates are the contrast case).
- [ ] **Spec conformance:** every widget, ladder, gate, check, and assessment element specified in the XS exists in the artifact at the specified depth; every LP-planned reveal arc pays off at the unit it names — no dangling forward promises (CAN-2026-0004 promised a $w^T x$ payoff that never arrived).
- [ ] **Glossary shape:** every term the lesson uses has an entry with all six fields (simple / precise / intuition / example / related / where-it-appears); every dotted in-text term resolves (CAN-2026-0004 shipped 3-field entries and left used terms — unit vector, residual, inverse — unlisted).
- [ ] **Concept map:** a dependency graph with branching needed-to-understand arrows — not a sequence strip of unit names — revisited at the close (CAN-2026-0004's 8-box linear chain is the contrast case).

## Audit 5 — Technical & behavioral simulation

- [ ] `node --check` (or equivalent) passes on extracted scripts.
- [ ] Zero external `src`/`href`/`@import`; works from `file://`.
- [ ] No duplicate IDs; tag balance; all internal anchors resolve; all `data-*` wiring targets exist; all glossary references resolve.
- [ ] **Behavioral simulation** (handler-level, not load-only): gates commit/refuse/unlock; quiz grading writes rule-explaining feedback; completion dots fill only when fully correct; weak topics record and clear; mastery scores compute; confident-miss routing fires for radio AND numeric items; reveals/hints/presets/matching/reset all work.
- [ ] Contrast measured (not asserted) for every text/background pair — WCAG AA $\ge 4.5:1$ for body-size text.
- [ ] Keyboard: every control reachable and operable; focus visible; popover focus-managed with Escape.
- [ ] Canvas: text equivalent adjacent via `aria-describedby`; no information by color alone; no live-region chatter on continuous input.
- [ ] **Canvas responsive viewport (ADR-0013 §1):** every canvas widget reads `cv.clientWidth` at draw time (not from HTML `width`/`height` attributes); applies DPR scaling (`ctx.setTransform(dpr,0,0,dpr,0,0)`); computes CSS height from the mathematical aspect ratio (`cv.style.height = ch + "px"`). Evidence: source inspection for `clientWidth`, `cv.style.height`, and `setTransform` per widget.
- [ ] **Canvas resize listeners (ADR-0013 §1):** `window.addEventListener("resize", draw)` count ≥ canvas widget count. Evidence: scripted grep count; list each widget's resize listener line number.
- [ ] **Canvas normalized transforms (ADR-0013 §1):** all coordinate mappings flow through `X(x) = (x-xMin)/(xMax-xMin)` and `Y(y) = 1-(y-yMin)/(yMax-yMin)`; no hardcoded pixel offset functions (e.g. `return 50 + x * (W-75) / 5`). Evidence: regex scan for hardcoded numeric pixel offsets in coordinate functions; flag any match.
- [ ] **Canvas per-widget viewport (ADR-0013 §2):** every `makeView` (or equivalent) call passes `xMin/xMax/yMin/yMax` matching the XS declaration. Evidence: cross-reference XS widget table against artifact `makeView` calls.
- [ ] **Canvas color legends (ADR-0013 §4):** every multi-entity canvas pairs with a `.legend-inline` element mapping colors to mathematical terms. Evidence: DOM scan pairing each canvas with its adjacent legend.
- [ ] **Canvas angular arcs (ADR-0013 §5):** signed angular difference with wrapping used for all angle arc rendering; `Math.max`/`Math.min` on angles not present. Evidence: source inspection of arc-drawing code.
- [ ] **Design token conformance (standard §10.1):** `:root` declares ≥ 20 custom properties including `--paper`, `--ink`, `--accent`, `--mono`, `--sans`, `--line`, `--good`, `--bad`, `--warn`, badge colors, and layout constants. Evidence: scripted token count and spot-check of key values.
- [ ] **Nav design contract (standard §10.2):** sticky nav uses `backdrop-filter: blur()`, semi-transparent background, `overflow-x: auto` on inner container (not `flex-wrap: wrap`), pill-style links (`border-radius: 999px`), and `[aria-current="true"]` active styles exist. Evidence: CSS inspection.
- [ ] **Header design contract (standard §10.3):** header is left-aligned with `.head-meta` row of `.chip` metadata chips. Evidence: DOM inspection.
- [ ] **Widget label quality (standard §10.4):** slider/input labels are descriptive and mathematical (e.g. `a₁ (scale v₁)`), not single letters. Evidence: per-widget label inspection.
- [ ] `prefers-reduced-motion` honored; no autoplay; print fallbacks show each interactive's default-state result.
- [ ] Colophon per the lesson standard: exactly the brand line and AI-honesty line (muted, reduced-motion-safe, prints as text); candidate identity present in the HTML header comment; no governance banner, provenance footer, or status/release/benchmark/efficacy claims anywhere on the page.
- [ ] No-JS: all content readable; nothing essential hidden by static markup.
- [ ] Storage unavailable → page still works; reset control clears state.

## Audit 6 — Rendered-output verification (browser-based, ADR-0010)

- [ ] Open candidate from `file://` in a real browser; record browser name and version.
- [ ] **Console check:** zero errors and zero unhandled warnings on initial page load and after full interaction sequence.
- [ ] **Responsive rendering & font check:** capture screenshots at $\ge 320\text{px}$, $640\text{px}$, and $1024\text{px}$. Confirm body font $\ge 16\text{px}$ at all breakpoints per standard §10. Confirm no horizontal overflow or clipped text.
- [ ] **Live interaction traces:** exercise each widget, gate, ladder, mastery item, and reset in live browser; record pass/fail trace for each.
- [ ] **Canvas extrema visual check:** drive each canvas to min/max in browser; visual screenshots confirm all elements stay within grid bounds.
- [ ] **Print preview:** Ctrl-P / ⌘-P preview verifies default-state visual notes render cleanly.
- [ ] **Reduced motion preview:** enable `prefers-reduced-motion: reduce` in browser; verify no unprompted transitions/animations fire.
- [ ] **Benchmark inclusion:** if [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) is the active benchmark, run the rendered pass on it to establish the baseline (first execution; frozen reference thereafter).

## Adversarial re-examination (mandatory gate, ADR-0009)

After all six audits pass, before the run transitions to `reflecting`:
- [ ] **Read-in-order dependency re-pass:** fresh-perspective verification of the taught-so-far set without relying on Audit 3 notes.
- [ ] **Edge-case behavioral simulation:** gate refusal/unlock across all branches, grading with boundary inputs, confident-miss routing on radio AND numeric items, reset from corrupted states.
- [ ] **Canvas-extrema forcing:** drive every manipulable to boundary extremes and degenerate values (zero vectors, collinear points, parallel vectors).
- [ ] **Honesty & provenance scan:** verify all formula keys, check for dangling forward references, confirm no uncredited external claims.
- [ ] Document methods executed, covered elements, and findings in the evaluation record.
- [ ] Any defect discovered routes the run to `revising` per the quality loop.

## Declaration of judgment-based qualities (WF-011)

The following qualities are intentionally recognized as judgment-based rather than mechanically checkable:
- Analogy and lede aptness (depth and resonance of real-world intuition)
- Signature visual aesthetic aptness (presence is checked by Audit 4; aesthetic elegance is judged)
- Information density vs cognitive load balance
- Prose readability and voice consistency

These qualities are evaluated via the [evaluation framework](../../docs/06-evaluation/evaluation-framework.md) dimension anchors, supported by the evaluator's cited reasoning.

## Failure routing

- Audit 1–3 failures → fix the plan/spec (P2/P3), not the artifact.
- Audit 4–6 / Adversarial gate failures → targeted revision with named parent run, defect, root cause, expected movement, regression checks (quality loop).
- Any Critical defect (false claim, broken core task, access barrier, provenance issue) → block; do not close as pilot-complete.

## Change history

| Date | Change |
| --- | --- |
| 2026-08-11 | Initial version, codifying V4's audits (commit `3453c6d`) |
| 2026-08-13 | Depth bar, manipulability, gate fidelity, spec conformance, glossary shape, concept-map, and reveal-arc items (commit `8db0c1a`) |
| 2026-08-14 | Added Audit 6 (rendered-output verification, [ADR-0010](../../docs/adr/0010-rendered-output-verification.md)); added mandatory adversarial re-examination gate ([ADR-0009](../../docs/adr/0009-forced-adversarial-re-examination-gate.md)); added execution-evidence rule (WF-008); added depth-calibration concrete checks and judgment qualities declaration (WF-007/WF-011). |
| 2026-08-15 | Added canvas engineering checks (responsive viewport, resize listeners, normalized transforms, per-widget viewport, color legends, angular arcs — ADR-0013) and design system checks (token conformance, nav design contract, header design contract, widget label quality — standard §10.1–10.4) to Audit 5, codified from EVAL-2026-0007 audit findings. |
