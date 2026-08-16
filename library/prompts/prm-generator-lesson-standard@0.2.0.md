# PRM-generator-lesson-standard@0.2.0

**Status:** Superseded by [@0.3.0](prm-generator-lesson-standard@0.3.0.md) (2026-08-13, standard colophon added to the output contract); never used for a governed generation  
**Owner:** Repository maintainer  
**Layer:** Task  
**Compatible roles:** Generator / Creator profile (Stage 1 five-profile model)  
**Last evaluated:** 2026-08-10 (RUN-20260810-0001; the prompt's substance produced CAN-2026-0003, which passed EVAL-2026-0002 incl. Revision 1)  
**Replaces / replaced by:** supersedes [@0.1.0](prm-generator-lesson-standard@0.1.0.md) (2026-08-13: visible banner/footer removed from the output contract); the unversioned generation instructions preserved as snapshots in RUN-20260804-0002 and RUN-20260810-0001

## Purpose and scope

Generate a governed, single-file interactive HTML lesson from an authorized source notes document, implementing the [lesson standard](../../docs/01-product/lesson-standard.md) end-to-end. Scope: learner-facing artifact generation only; the plan (LP) and specification (XS) are inputs, not outputs.

## Required inputs and source of truth

- `{SOURCE}` — the notes document (truth about *what was taught*, not about order or completeness).
- `{CONCEPT_MODEL}`, `{LEARNING_PLAN}`, `{SPEC}` — the pinned CM/LP/XS records; claims must trace to CM.
- `{PROVENANCE}` — candidate ID, run ID, source ID, model/configuration, date, prompt digest for the HTML header comment.
- `{PATTERN_CATALOG}` — the current lesson-patterns catalog.

## Output contract

One self-contained `.html` file: governed header comment carrying the provenance identity (no visible governance banner or footer on the learner-facing page); orientation unit with concept map; units following the canonical anatomy; synthesis + interleaved mastery assessment; review list; glossary; zero external requests; offline-capable; passes the standing verification suite (syntax, structure, zero-dependency, recomputation, behavioral simulation).

## Hard constraints and prohibited behavior

- Explain-before-use (standard §2); layered content labels + provenance tags on every block (§1.1).
- Coverage: every inventory item present or dispositioned (§3).
- Assessment: constructed response in every unit check; interleaved mastery with reasoning/transfer/error-identification items; never reuse worked numbers; feedback states governing rules (§5).
- Interaction only via the admission test (§4); goal-directed; live-computed values only — never hard-code what can be computed.
- Formulas: per-symbol keys, plain-language meaning, interpretation (the per-symbol formula key pattern in the pattern catalog).
- Zero external dependencies; accessibility and technical baselines (standard §1.1).
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
> 8. Provenance: header comment exactly as specified in {PROVENANCE}; no visible governance banner or footer on the page; no release, benchmark, or efficacy claims anywhere.
> 9. Self-verify before returning: every formula, every default value, every answer key; list what you verified.

## Examples and anti-examples

- **Example (good):** "The class placed this proof before the dot product existed; we moved it here, where it is legal" — labeled re-sequencing with reason.
- **Example (good):** a check item whose distractors are the documented misconceptions, with per-miss governing-rule feedback.
- **Anti-example (recognition-only):** a 10-item MCQ mastery quiz repeating worked numbers (v2/v3 defect class).
- **Anti-example (hard-coded contradiction):** interview text claiming AB and BA results that the live widget contradicts (v3 defect).
- **Anti-example (decorative):** a canvas that animates on load with no learner action and no manipulable variable.

## Evaluation set and success criteria

Success = the candidate passes the five audits of the lesson-generation workflow P5 with no unresolved Major/Critical defects, and scores ≥ 3 on every rubric dimension under non-independent review. Evaluation set until more modules exist: the AIML-4 Module 2 source (frozen).

## Known failure modes

1. Assessment drifts to recognition-only when content volume grows (MEM-2026-0002).
2. Added bridges outgrow the main path (scope creep) — enforce the additional-knowledge policy.
3. Hard-coded widget results drift from live UI — compute live only.
4. Provenance tags applied to examples but not to new claims (v3 determinant defect).
5. Readouts that dump numbers without interpretation.

## Change rationale and compatibility impact

Substance derived from the v4 generation instruction (snapshot digest `f1a43cbf21cf`) generalized to any source document, plus the hard-won defect classes from RUN-20260804-0001/0002 and RUN-20260810-0001. Any semantic change requires a version bump and a comparison run on the frozen evaluation set.

**0.2.0 (2026-08-13):** the visible status banner and provenance footer were removed from the output contract by owner decision; the governed HTML header comment is now the sole in-artifact provenance carrier, with lineage living in the run ledger. The lesson standard's Governed provenance rule and workflow P4 were amended to match, and the change was applied retroactively to the v2–v4 artifacts (new SHA-256 identities recorded in the run ledgers and evaluations). No pedagogy change; the frozen evaluation set remains valid.

Editorial (carried from 0.1.0, 2026-08-13): pattern references cite pattern names instead of catalog IDs, so a pattern-catalog renumbering cannot silently break the card.

