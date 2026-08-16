# MEM-2026-0004: Compliant-minimum collapse — a rule-complete pipeline still produces a thin lesson; depth must be specified, generated, and audited explicitly

**Status:** Supported
**Curator:** Repository maintainer (solo Stage 1 operator)
**Created / review date:** 2026-08-13
**Scope:** Interactive lesson generation and evaluation in Learning OS (Stage 1 pipeline)
**Tags:** generation-depth, prompt-design, quality-gate, evaluation-sensitivity, workflow
**Evidence records:** [RUN-20260813-0001](../runs/run-20260813-0001-linear-algebra-foundations-v5.md), [EVAL-2026-0003](../evaluations/eval-2026-0003-linear-algebra-foundations-v5.md), [EVAL-2026-0002](../evaluations/eval-2026-0002-linear-algebra-foundations-v4.md), [RUN-20260810-0001](../runs/run-20260810-0001-linear-algebra-foundations-v4.md)
**Supersedes / conflicts-with:** none (Iteration 1 — original)

## Lesson

The 2026-08-13 regeneration test built CAN-2026-0004 (v5) from source + governed workflow only, as a live pipeline test. The candidate passed all five P5 audits and weighted 3.59 — identical to the reference implementation CAN-2026-0003 (v4, corrected 3.59) — while shipping ~44% of its size and silently dropping the techniques that made v4 the reference: the wᵀx reveal arc (promised in Unit 1, never paid off), the magnitude-confound / cosine-similarity callout, per-skill faded ladders (1 shipped of the 4 its own plan named), the manipulable least-squares lab (shipped as a zero-input demo badged Explore), gate fidelity (widgets visible without commitment, answer-independent feedback), unit-level explain-in-words items, two recognition-only unit checks, a 3-field glossary missing used terms, a sequence-strip concept map, and bounded canvas inputs (typed values render off-canvas — the v2 defect class, reintroduced). The workflow verified the floor and could not see the missing depth; the rubric confirmed the blindness by scoring both candidates identically.

## Why this is believed

- Direct artifact comparison v4 ↔ v5 (inspection plus scripted counts): widgets 12 + matching vs 9; gates 3 (hiding manipulables, choice-differentiated) vs 2 (hollow); ladders 4 vs 1; check items ~36 (incl. 3 explain) vs 12 (0 explain); mastery 10 items / 3-level confidence vs 6 / 2-level; glossary 32 six-field entries vs 18 three-field; concept map branched dependency graph vs linear unit strip.
- The depth gap originated upstream: CM-2026-0002 (~1/3 the depth of CM-2026-0001) and a lighter LP/XS bounded what generation could produce; the artifact then under-shipped even its own XS (norm comparator, four ladders) with no conformance check to catch it.
- Two outright standard breaches (recognition-only U6/U7 checks; under-shaped glossary) passed Audit 4 — an unexecuted check is indistinguishable from a passed one.

## Recommended action

1. Generation: prompt card @0.4.0 carries the explicit depth bar (items 10–12), the conformance sweep (item 13), and the spec-conformance hard constraint.
2. Specification: CM/LP/XS templates declare depth per unit (claim/misconception floors; ledes, signature visuals, reveal arcs, per-skill ladders; per-widget manipulable variables), making depth a conformance target instead of an assumption.
3. Verification: the QA checklist audits depth item-by-item (per-unit constructed response, widget manipulability, gate fidelity, glossary six-field shape and coverage, dependency-graph concept map, XS conformance, reveal-arc payoff, canvas extrema).
4. Scoring: the evaluation framework's Stage 1 dimension anchors distinguish compliant-minimum from reference-depth candidates.

## Counterexamples and limitations

- Depth is not bloat: the standard's additional-knowledge policy (§7) and cognitive-load rules still govern; the depth bar constrains *how* planned concepts are taught, not how many.
- The @0.4.0 hypothesis is untested: its first governed run is the comparison; if depth still does not materialize, the lever moves to XS-level enumerativeness (fully enumerated per-unit element lists).
- Evidence comes from one source package and non-independent review; the artifact "feel" judgment is the owner's, not a learner pilot's.

## Retrieval guidance

Consult at P1–P3 authoring (is depth specified to the template floors?), at P4 generation (prompt card ≥ 0.4.0; conformance sweep executed), and at P5/P6 (were the depth checks executed with named, per-unit evidence?). Pair with MEM-2026-0002 (recognition-only assessment) and MEM-2026-0003 (structural checks cannot see dynamic defects).

## Privacy and retention

No personal data; retain as a standing generation/audit guard until superseded by comparison-run evidence.
