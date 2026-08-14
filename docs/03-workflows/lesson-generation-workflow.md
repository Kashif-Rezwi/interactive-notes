# Lesson Generation Workflow (Creative Interactive Notes)

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04 (or after two governed lessons generated under this workflow, whichever comes first)<br>
**Adopted by:** [ADR-0004](../adr/0004-lesson-standard-adoption.md)<br>
**Applies to:** governed generation of interactive HTML lessons from source notes. Executes inside the [quality loop](quality-loop.md) state machine and the [workflow architecture](workflow-architecture.md) stage model; this document specializes them for lessons. The binding content rules live in the [lesson standard](../01-product/lesson-standard.md) and [depth-calibration-contract.md](../01-product/depth-calibration-contract.md).

## Phase overview

```text
P0 Intake ──► P1 Source understanding ──► P2 Learning design ──► P3 Experience design
     │              (SRC record)              (CM record)           (LP record)         (XS record)
     ▼
P4 Generation ──► P5 Six audits & adversarial gate ──► P6 Evaluation & closure
     (RUN ledger)    (gate & rendered evidence)           (EVAL record + compounding updates)
```

No phase may be skipped. A later phase that discovers an earlier phase's defect routes back per the quality loop's retry policy (fix the plan, not the symptom).

## P0 — Intake and authorization

- **Input:** a notes document + a stated learner request.
- **Do:** confirm source authorization; create or reuse the SRC record (identity, hash, anchors); define the target learner precisely (what they can and cannot be assumed to know); declare budget and scope.
- **Exit:** approved SRC; learner definition; scope statement.
- **Ordering rule:** assign the class ordinal at intake and append the module README row in class sequence. Never infer class order from alphabetical file enumeration (see the content-package convention).

## P1 — Source understanding

- **Do:** build the content inventory — every topic, subtopic, definition, formula, example, terminology item, relationship, instructor assumption, underexplained concept, and missing-but-necessary concept. Then author the concept model (CM): atomic claims anchored to source locations, prerequisite graph, examples/non-examples, misconceptions, ambiguities (opaque figures, typos, imprecisions — each with a disposition).
- **Rules:** the source is the truth about *what was taught*, not about *order or completeness*; nothing is dropped silently (standard §3). Verify against the [depth-calibration contract](../01-product/depth-calibration-contract.md) conformance checklist before approval.
- **Exit:** CM reviewed; inventory complete with dispositions; conformance checklist verified.

## P2 — Learning design

- **Do:** author the learning plan (LP): measurable outcomes; dependency graph derived from the CM (not the source's page order); teaching sequence with reorder rationale; per-concept decisions from the standard (bridges, ladders, gates, misconceptions); assessment plan (mix per standard §5); the additional-knowledge triage (must/should/could/do-not-add, standard §7); **the depth pass — per-unit ledes, signature visuals, reveal arcs (setup → payoff unit), misconception-alert callouts, one ladder per computational skill, and explain-item placement ([depth-calibration-contract.md](../01-product/depth-calibration-contract.md); LP template fields; MEM-2026-0004). The active benchmark ([BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md)) is the calibration exemplar for depth; deliberate exclusion requires a recorded experiment rationale ([ADR-0011](../adr/0011-benchmark-definition-and-artifact-change-protocol.md)).**
- **Rules:** explain-before-use governs every sequencing choice (standard §2); research only where it changes a decision (standard §12).
- **Exit:** LP approved by the operator; outcomes measurable; conformance checklist verified.

## P3 — Experience design

- **Do:** author the experience specification (XS): map every unit to the canonical anatomy; choose interaction patterns per concept via the admission test (standard §4) from the [pattern catalog](../../library/patterns/lesson-patterns.md); specify feedback, states, accessibility alternatives, print fallbacks; write acceptance criteria; **declare every widget's manipulable variables (or static-demo reason), input bounds/autoscaling, the glossary term set, and the concept-map dependency edges — the XS is a conformance contract P5 verifies element-for-element, not a sketch ([depth-calibration-contract.md](../01-product/depth-calibration-contract.md)).**
- **Rules:** no decorative interaction; no recognition-only assessment; live-computed values only.
- **Exit:** XS approved; every LP outcome exercised by at least one specified check or interaction; conformance checklist verified.

## P4 — Generation

- **Do:** generate the candidate with the versioned prompt card ([PRM-generator-lesson-standard](../../library/prompts/prm-generator-lesson-standard@0.5.0.md)); record the run ledger (RUN) with pinned input identities, prompt digest, **full in-repo prompt snapshot ([prompt-architecture.md](../05-prompts/prompt-architecture.md); WF-001/WF-015)**, and verification evidence; **record iteration counts exactly per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md)** (generation iterations, in-generation corrections, revision cycles). **The artifact must conform to the XS element-for-element at the specified depth; a specified element that cannot be built well is escalated to the plan owner, never silently dropped (prompt items 12–14).**
- **Rules:** governed provenance comment header (identity in the HTML source; the only closing element on the page is the standard colophon per the lesson standard); zero external dependencies; all widget math computed live; **canvas engineering per [canvas-engineering-standard.md](../01-product/canvas-engineering-standard.md) (ADR-0013): responsive `makeView` pattern, per-widget viewport from XS, mandatory resize listeners, no hardcoded pixel offsets, `.legend-inline` on multi-entity canvases; design system per lesson standard §10.1–10.4: pinned tokens, frosted-glass nav, left-aligned header with chips, descriptive widget labels.**
- **Exit:** candidate renders cleanly from `file://`; standing verification suite passes.

## P5 — The six audits and adversarial gate (mandatory)

Run all six audits and record execution evidence in the evaluation record. Executable checklist: [lesson-qa-checklist](../../library/rubrics/lesson-qa-checklist.md).

| # | Audit | Core question | Method |
| --- | --- | --- | --- |
| 1 | **Coverage** | Did anything from the source silently disappear? | Coverage matrix: every inventory item → lesson location + disposition |
| 2 | **Mathematical** | Is every formula, number, and answer key correct? | Independent scripted recomputation of every value; live-computation check; canvas-extrema bounds check |
| 3 | **Dependency order** | Is anything used before being explained? | Read-in-order pass with a "taught-so-far" set (standard §2) |
| 4 | **Pedagogical** | Does the artifact implement the standard & depth floor? | Beginner test, cognitive-load test, interaction admission test, practice/transfer/ML-relevance tests (standard §§4–6); **depth-calibration contract scans: per-unit constructed response, widget manipulability, gate fidelity, glossary 6-field shape, concept-map branching, and XS-conformance sweep** |
| 5 | **Technical & behavioral** | Does the code and logic work under simulation? | Syntax/structure/duplicate-ID scans; zero-dependency scan; **handler-level behavioral simulation** (gates, grading, feedback, state); measured contrast; keyboard/no-JS/reduced-motion/print review; **canvas engineering checks ([ADR-0013](../adr/0013-canvas-engineering-standard-adoption.md)): responsive viewport, resize listeners, normalized transforms, per-widget viewport, color legends, angular arcs; design system conformance (standard §10.1–10.4): token count, nav contract, header contract, label quality** |
| 6 | **Rendered-output verification** | Does it render and behave correctly in a real browser? | **Browser pass ([ADR-0010](../adr/0010-rendered-output-verification.md)):** zero console errors on load/interaction; responsive screenshots at $\ge 320\text{px}$, $640\text{px}$, $1024\text{px}$ (confirming body font $\ge 16\text{px}$); live interaction traces for every widget/gate/ladder/mastery/reset; canvas extrema visuals; print stylesheet render |

### Mandatory Adversarial Re-Examination Gate ([ADR-0009](../adr/0009-forced-adversarial-re-examination-gate.md))

After all six audits pass, before the run transitions to `reflecting`:
- Conduct an adversarial re-examination using methods independent of initial P5 checks:
  1. *Read-in-order dependency re-pass* from a fresh perspective.
  2. *Handler-level behavioral simulation* targeting edge cases (gate refusal/unlock branches, grading boundary cases, confident-miss routing on radio AND numeric items, reset from corrupted states).
  3. *Canvas-extrema forcing* (driving manipulables to boundary extremes and degenerate values).
  4. *Honesty & provenance scan* (checking for unsupported claims, dangling forward promises, uncredited additions).
- Record methods executed, covered elements, and findings in the evaluation record.
- Clean pass with documented evidence allows transition to `reflecting`. Any defect routes to `revising` per the quality loop.

### Failure Routing
- Audits 1–3 failing ⇒ route to P2/P3 (the plan is wrong, not the artifact).
- Audits 4–6 / Adversarial gate failing ⇒ targeted revision per the quality loop.

## P6 — Evaluation, closure, and knowledge-system update

- **Do:** score with the [evaluation framework](../06-evaluation/evaluation-framework.md); record EVAL (independence status sets release eligibility per policy) declaring **`Iterations reviewed` per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md)** (builds examined, each with its hash; revision cycles); include execution evidence, rendered evidence, and re-verification pass results; close the RUN ledger with reflection and memory disposition.
- **Then update the compounding assets** (this is what makes the next lesson better):
  - *Memory:* promote reusable, evidenced lessons to `records/memory/`.
  - *Pattern catalog:* add/strengthen patterns observed working; demote anti-patterns observed failing.
  - *Misconception knowledge:* new beginner errors discovered → add to the catalog and the next CM template usage.
  - *QA checklist:* any defect class that escaped → add the check that would have caught it.
  - *Prompt card:* update only with a comparison hypothesis (prompt evolution loop).
  - *Standard:* amend only via review when evidence contradicts a rule.
  - *Calibration:* each completed pilot counts toward the framework's three-pilot calibration commitment.
  - *Forward-looking risk review (WF-013):* ask "what could the next lesson lose that has never failed yet?" and record proactive risk observations in the evaluation reflection.
- **Exit:** EVAL recorded; memory disposition explicit; persistence checklist verified; curation done or explicitly deferred with reason.

## Persistence checklist (WF-015)

Before closing a run, verify that no session-only knowledge is required for future reproduction:
- [ ] Full rendered prompt snapshot is recorded in-repo (not digest-only)
- [ ] All audit outputs and execution methods are in the EVAL record
- [ ] Complete coverage matrix is attached to the EVAL record
- [ ] Adversarial re-examination evidence is recorded
- [ ] Rendered verification screenshots and console captures are attached
- [ ] Re-verification pass results are documented
- [ ] Deferred evaluations are explicitly closed or scheduled with date and rationale
- [ ] Memory disposition is explicit for every observation
- [ ] Lineage can be fully reconstructed in-repo without external session material

## Two-speed note

Exploration prototypes may skip P5–P6 gates but may never be promoted to governed status by copy/paste — they re-enter at P1 with their evidence (workflow architecture, "two-speed work").
