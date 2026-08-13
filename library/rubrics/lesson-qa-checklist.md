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
- [ ] Every unit check has ≥1 constructed-response item; feedback states governing rules.
- [ ] Mastery check: interleaved; reasoning + transfer + error-identification items; no reused worked numbers.
- [ ] Misconceptions: each major concept's beginner error is named and tested by a real distractor.
- [ ] Layers/provenance: every block labeled; additions carry reasons.
- [ ] ML connections are mechanisms at learner level; no forced references.
- [ ] Cognitive load: one new idea per block; no walls of text; optional depth collapsed.

## Audit 5 — Technical & behavioral

- [ ] `node --check` (or equivalent) passes on extracted scripts.
- [ ] Zero external `src`/`href`/`@import`; works from `file://`.
- [ ] No duplicate IDs; tag balance; all internal anchors resolve; all `data-*` wiring targets exist; all glossary references resolve.
- [ ] **Behavioral simulation** (handler-level, not load-only): gates commit/refuse/unlock; quiz grading writes rule-explaining feedback; completion dots fill only when fully correct; weak topics record and clear; mastery scores compute; confident-miss routing fires for radio AND numeric items; reveals/hints/presets/matching/reset all work.
- [ ] Contrast measured (not asserted) for every text/background pair — WCAG AA ≥ 4.5:1 for body-size text.
- [ ] Keyboard: every control reachable and operable; focus visible; popover focus-managed with Escape.
- [ ] Canvas: text equivalent adjacent via `aria-describedby`; no information by color alone; no live-region chatter on continuous input.
- [ ] `prefers-reduced-motion` honored; no autoplay; print fallbacks show each interactive's default-state result.
- [ ] No-JS: all content readable; nothing essential hidden by static markup.
- [ ] Storage unavailable → page still works; reset control clears state.
- [ ] Responsive: readable at 320 px; canvases rescale without distortion; no horizontal overflow.

## Failure routing

- Audit 1–3 failures → fix the plan/spec (P2/P3), not the artifact.
- Audit 4–5 failures → targeted revision with named parent run, defect, root cause, expected movement, regression checks (quality loop).
- Any Critical defect (false claim, broken core task, access barrier, provenance issue) → block; do not close as pilot-complete.
