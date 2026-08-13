# Lesson QA Checklist (five audits)

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Scope:** interactive HTML lessons generated under the [lesson standard](../../docs/01-product/lesson-standard.md). **This is a verification checklist, not a scoring rubric:** numeric gates and release decisions belong solely to the [evaluation framework](../../docs/06-evaluation/evaluation-framework.md).<br>
**Evidence standard:** every checked box cites its evidence (command output, recomputation, or read-through note) in the evaluation record.<br>
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

## Audit 4 — Pedagogical (against the lesson standard)

- [ ] Beginner test: the declared learner can follow every unit without outside knowledge.
- [ ] Unit anatomy present: Learn (intuition first) → Predict → Explore → Practice → Check → Connect.
- [ ] Every interaction passed the five-question admission test; goals are stated; one variable at a time.
- [ ] Every unit check has ≥1 constructed-response item; feedback states governing rules. **Verified unit by unit — name each unit's constructed-response item in the evidence; a recognition-only unit check is a Major (CAN-2026-0004 shipped two).**
- [ ] Mastery check: interleaved; reasoning + transfer + error-identification items; no reused worked numbers; size ≈ one item per content unit + 2 (pattern P-12); three-level confidence tags (sure / think so / guessing); ≥2 explain-in-own-words items per lesson with model answers (standard §5).
- [ ] Misconceptions: each major concept's beginner error is named and tested by a real distractor **and surfaced in its own visible alert callout where the LP names one**.
- [ ] Layers/provenance: every block labeled; additions carry reasons.
- [ ] ML connections are mechanisms at learner level; no forced references.
- [ ] Cognitive load: one new idea per block; no walls of text; optional depth collapsed.
- [ ] **Depth bar (MEM-2026-0004):** every Learn block opens with a concrete intuition and a tiny worked numeric example before any widget; every unit carries a one-line lede; each computational skill named in the LP has its own full faded ladder (worked → completion → independent).
- [ ] **Widget manipulability:** every Explore-badged widget has ≥1 learner-manipulable variable; a widget with none is a recorded static-demo decision, never badged Explore (standard §4; CAN-2026-0004's fixed-point least-squares widget is the contrast case).
- [ ] **Gate fidelity:** prediction gates hide the manipulable until commitment; feedback differentiates by the chosen option and references the commitment (MEM-2026-0001; CAN-2026-0004's text-only, answer-independent gates are the contrast case).
- [ ] **Spec conformance:** every widget, ladder, gate, check, and assessment element specified in the XS exists in the artifact at the specified depth; every LP-planned reveal arc pays off at the unit it names — no dangling forward promises (CAN-2026-0004 promised a wᵀx payoff that never arrived).
- [ ] **Glossary shape:** every term the lesson uses has an entry with all six fields (simple / precise / intuition / example / related / where-it-appears); every dotted in-text term resolves (CAN-2026-0004 shipped 3-field entries and left used terms — unit vector, residual, inverse — unlisted).
- [ ] **Concept map:** a dependency graph with branching needed-to-understand arrows — not a sequence strip of unit names — revisited at the close (CAN-2026-0004's 8-box linear chain is the contrast case).

## Audit 5 — Technical & behavioral

- [ ] `node --check` (or equivalent) passes on extracted scripts.
- [ ] Zero external `src`/`href`/`@import`; works from `file://`.
- [ ] No duplicate IDs; tag balance; all internal anchors resolve; all `data-*` wiring targets exist; all glossary references resolve.
- [ ] **Behavioral simulation** (handler-level, not load-only): gates commit/refuse/unlock; quiz grading writes rule-explaining feedback; completion dots fill only when fully correct; weak topics record and clear; mastery scores compute; confident-miss routing fires for radio AND numeric items; reveals/hints/presets/matching/reset all work.
- [ ] Contrast measured (not asserted) for every text/background pair — WCAG AA ≥ 4.5:1 for body-size text.
- [ ] Keyboard: every control reachable and operable; focus visible; popover focus-managed with Escape.
- [ ] Canvas: text equivalent adjacent via `aria-describedby`; no information by color alone; no live-region chatter on continuous input.
- [ ] `prefers-reduced-motion` honored; no autoplay; print fallbacks show each interactive's default-state result.
- [ ] Colophon per the lesson standard: exactly the brand line and AI-honesty line (muted, reduced-motion-safe, prints as text); candidate identity present in the HTML header comment; no governance banner, provenance footer, or status/release/benchmark/efficacy claims anywhere on the page.
- [ ] No-JS: all content readable; nothing essential hidden by static markup.
- [ ] Storage unavailable → page still works; reset control clears state.
- [ ] Responsive: readable at 320 px; canvases rescale without distortion; no horizontal overflow.

## Failure routing

- Audit 1–3 failures → fix the plan/spec (P2/P3), not the artifact.
- Audit 4–5 failures → targeted revision with named parent run, defect, root cause, expected movement, regression checks (quality loop).
- Any Critical defect (false claim, broken core task, access barrier, provenance issue) → block; do not close as pilot-complete.
