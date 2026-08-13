# PRM-generator-lesson-standard@0.4.0

**Status:** Draft (registered during Stage 1 per ADR-0004; promotion to Approved requires the prompt promotion process and owner approval)  
**Owner:** Repository maintainer  
**Layer:** Task  
**Compatible roles:** Generator / Creator profile (Stage 1 five-profile model)  
**Last evaluated:** not yet — its first governed use is the next regeneration run on the frozen evaluation set, which doubles as the comparison run for the 0.4.0 hypothesis (see Change rationale)  
**Replaces / replaced by:** supersedes [@0.3.0](prm-generator-lesson-standard@0.3.0.md) (2026-08-13: adds the explicit depth bar and spec-conformance duty after the v5 regeneration test exposed compliant-minimum collapse); earlier lineage in @0.3.0

## Purpose and scope

Generate a governed, single-file interactive HTML lesson from an authorized source notes document, implementing the [lesson standard](../../docs/01-product/lesson-standard.md) end-to-end. Scope: learner-facing artifact generation only; the plan (LP) and specification (XS) are inputs, not outputs.

## Required inputs and source of truth

- `{SOURCE}` — the notes document (truth about *what was taught*, not about order or completeness).
- `{CONCEPT_MODEL}`, `{LEARNING_PLAN}`, `{SPEC}` — the pinned CM/LP/XS records; claims must trace to CM.
- `{PROVENANCE}` — candidate ID, run ID, source ID, model/configuration, date, prompt digest for the HTML header comment.
- `{PATTERN_CATALOG}` — the current lesson-patterns catalog.

## Output contract

One self-contained `.html` file: governed header comment carrying the provenance identity; the standard colophon (brand + AI-honesty lines per the lesson standard) as the page's only closing element; orientation unit with concept map; units following the canonical anatomy; synthesis + interleaved mastery assessment; review list; glossary; zero external requests; offline-capable; passes the standing verification suite (syntax, structure, zero-dependency, recomputation, behavioral simulation). **The contract is the standard at full depth, not at minimum compliance: everything below and everything declared in {LEARNING_PLAN} / {SPEC} ships — or its absence is a stated, labeled decision, never a silent omission.**

## Hard constraints and prohibited behavior

- Explain-before-use (standard §2); layered content labels + provenance tags on every block (§1.1).
- Coverage: every inventory item present or dispositioned (§3).
- Assessment: constructed response in every unit check; interleaved mastery with reasoning/transfer/error-identification items; never reuse worked numbers; feedback states governing rules (§5).
- Interaction only via the admission test (§4); goal-directed; live-computed values only — never hard-code what can be computed.
- Formulas: per-symbol keys, plain-language meaning, interpretation (the per-symbol formula key pattern in the pattern catalog).
- Zero external dependencies; accessibility and technical baselines (standard §1.1).
- **Spec conformance:** every widget, ladder, gate, check, and assessment element declared in {LEARNING_PLAN} / {SPEC} exists in the artifact at the specified depth. If a specified element cannot be built well, stop and escalate to the plan owner — never ship the gap silently.
- Prohibited: decorative interaction, recognition-only assessment, unexplained jargon, unsupported claims, gamification, autoplay, efficacy claims, CDN references.

## Uncertainty and escalation behavior

If the source is ambiguous or wrong, do not silently fix or silently propagate: correct and flag in-artifact, and record the disposition in the CM. If a required concept cannot be taught at the declared learner level, mark it EXTENSION and escalate to the plan owner rather than half-explaining.

## Prompt content

> You are generating a governed interactive lesson. Inputs: {SOURCE}, {CONCEPT_MODEL}, {LEARNING_PLAN}, {SPEC}, {PROVENANCE}, {PATTERN_CATALOG}.
> 1. Obey the lesson standard (attached/linked) in full; where source order conflicts with the dependency rule, follow the learning plan's sequence.
> 2. Teach to the declared learner: nothing unexplained is ever load-bearing; bridge or defer.
> 3. For each unit emit: Learn (intuition→example→visual→definition→keyed formula→interpretation) → Predict → Explore (goal-directed) → Practice (faded ladder for computational skills) → Check (≥1 constructed response; rule-explaining feedback) → Connect (relationship strip + ML mechanism).
> 4. Labels: every block carries a layer badge and provenance tag.
> 5. Build interactions only from the pattern catalog; compute every displayed value live in the page's script.
> 6. Emit the mastery assessment per standard §5 and the glossary per the glossary-as-data pattern.
> 7. Engineering: single file; zero external requests; semantic HTML; keyboard-operable native controls; canvas text equivalents; reduced-motion; print fallbacks; local-only state with reset.
> 8. Provenance: header comment exactly as specified in {PROVENANCE}; close the page with the standard colophon (brand + AI-honesty lines, per the lesson standard); no governance banner or provenance footer; no release, benchmark, or efficacy claims anywhere.
> 9. Self-verify before returning: every formula, every default value, every answer key; list what you verified.
> 10. **Depth bar — explanations.** Every Learn block opens with a concrete, real-world intuition and contains a tiny worked example with actual numbers *before* any widget; every unit carries a one-line lede; every misconception named in the plan gets its own visible alert callout. No anatomy step may be collapsed away: a Learn with no example or a Connect with no mechanism is an unfinished unit.
> 11. **Depth bar — interactions.** Every Explore widget manipulates at least one learner-controlled variable; if the concept admits none, build a static demonstration and label it as one — never badge a demo as Explore. Prediction gates hide the manipulable until commitment and return feedback that differentiates by the chosen option and references the commitment. Canvases bound their inputs (sliders, min/max) or autoscale, so no learner action can draw off-canvas; multi-entity canvases carry a color legend. Each computational skill named in the plan gets its own full faded ladder (worked → completion → independent).
> 12. **Depth bar — assessment and reference.** Every unit check, without exception, includes ≥1 constructed-response item; the lesson includes ≥2 explain-in-own-words items with honest model-answer reveals; mastery size ≈ one item per content unit + 2, with three-level confidence tags (sure / think so / guessing). The glossary covers every term the lesson uses, each entry with simple + precise + intuition + example + related + where-it-appears. The concept map is a dependency graph with branching needed-to-understand arrows — never a strip of unit names — and is revisited at the close. Every forward promise made in the text pays off at the unit it names.
> 13. **Conformance sweep before returning.** Diff the artifact against {SPEC} and {LEARNING_PLAN} element by element; list anything specified that is missing or reduced, and fix it or escalate — never ship the gap silently. Then list what you verified.

## Examples and anti-examples

- **Example (good):** "The class placed this proof before the dot product existed; we moved it here, where it is legal" — labeled re-sequencing with reason.
- **Example (good):** a check item whose distractors are the documented misconceptions, with per-miss governing-rule feedback.
- **Anti-example (recognition-only):** a 10-item MCQ mastery quiz repeating worked numbers (v2/v3 defect class).
- **Anti-example (hard-coded contradiction):** interview text claiming AB and BA results that the live widget contradicts (v3 defect).
- **Anti-example (decorative):** a canvas that animates on load with no learner action and no manipulable variable.
- **Anti-example (demo badged as explorer, CAN-2026-0004):** a least-squares "explorer" with fixed points and no learner input — a demonstration must be presented and labeled as one.
- **Anti-example (hollow gate, CAN-2026-0004):** a prediction gate whose widget stays visible and whose reveal text is identical for every choice — the commitment has no consequence, so it teaches nothing.
- **Anti-example (dangling promise, CAN-2026-0004):** text promising "wᵀx returns in Unit 3" with no reveal delivered in Unit 3 — every forward reference must pay off where promised.

## Evaluation set and success criteria

Success = the candidate passes the five audits of the lesson-generation workflow P5 with no unresolved Major/Critical defects, scores ≥ 3 on every rubric dimension under non-independent review, **and matches the reference implementation (CAN-2026-0003) technique-for-technique on the depth bar (prompt items 10–12)** — the comparison that tests the 0.4.0 hypothesis. Evaluation set until more modules exist: the AIML-4 Module 2 source (frozen).

## Known failure modes

1. Assessment drifts to recognition-only when content volume grows (MEM-2026-0002).
2. Added bridges outgrow the main path (scope creep) — enforce the additional-knowledge policy.
3. Hard-coded widget results drift from live UI — compute live only.
4. Provenance tags applied to examples but not to new claims (v3 determinant defect).
5. Readouts that dump numbers without interpretation.
6. **Compliant-minimum collapse:** every rule satisfied at its floor while the depth that carries the learning — analogies, worked examples, signature visuals, misconception callouts, reveal arcs — is silently dropped (the CAN-2026-0004 class; MEM-2026-0004).
7. **Spec drift:** elements declared in the LP/XS (a widget, a ladder, an item mix) quietly missing from the artifact while audits pass anyway — conformance is an explicit generation duty (prompt item 13).

## Change rationale and compatibility impact

Substance derived from the v4 generation instruction (snapshot digest `f1a43cbf21cf`) generalized to any source document, plus the hard-won defect classes from RUN-20260804-0001/0002, RUN-20260810-0001, and RUN-20260813-0001. Any semantic change requires a version bump and a comparison run on the frozen evaluation set.

**0.4.0 (2026-08-13):** adds the explicit depth bar (prompt items 10–12), the conformance sweep (item 13), the spec-conformance hard constraint, and failure modes 6–7. **Hypothesis (prompt evolution loop):** the 2026-08-13 regeneration test (RUN-20260813-0001, EVAL-2026-0003) showed @0.3.0's rule-only instruction converges to the compliant minimum — the candidate passed every gate at ~44% of the reference implementation's size and lost its signature techniques. Stating the depth bar explicitly should reproduce reference-implementation richness in a single governed generation. **Comparison run:** the next regeneration of the frozen AIML-4 Module 2 source, judged against CAN-2026-0003 (reference) and CAN-2026-0004 (@0.3.0 output) on the 2026-08-13 QA-checklist depth items plus the standard rubric. Inputs and the rest of the contract are unchanged.

**0.3.0 (2026-08-13):** the standard colophon (brand line + AI-honesty line) was added as the required closing element of every governed lesson, replacing the removed governance banner/footer with a warm, honest learner-facing close; enforced by the lesson standard and a QA-checklist item. Applied to v2–v4 the same day. No pedagogy change; the frozen evaluation set remains valid.

**0.2.0 (2026-08-13):** the visible status banner and provenance footer were removed from the output contract by owner decision; the governed HTML header comment is now the sole in-artifact provenance carrier, with lineage living in the run ledger. The lesson standard's Governed provenance rule and workflow P4 were amended to match, and the change was applied retroactively to the v2–v4 artifacts (new SHA-256 identities recorded in the run ledgers and evaluations). No pedagogy change; the frozen evaluation set remains valid.

Editorial (carried from 0.1.0, 2026-08-13): pattern references cite pattern names instead of catalog IDs, so a pattern-catalog renumbering cannot silently break the card.

