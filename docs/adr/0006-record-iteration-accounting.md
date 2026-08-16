# ADR-0006: Mandate iteration accounting in governed records

**Status:** Accepted  
**Date:** 2026-08-11  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Record structure for all governed records (runs, evaluations, and supersession chains)  
**Supersedes / superseded by:** none

## Context and problem

Nobody can currently answer "how many iterations did this candidate really go through?" EVAL-2026-0002 documents two candidate hashes (implicitly two builds) but states "Iterations: 2" nowhere. RUN-20260810-0001's `Budget` line mentions iterations informally and mixes three different kinds of change (fresh candidates, pre-evaluation assembly fixes, post-evaluation revision cycles) into one word. As the repository becomes a calibration corpus for the evaluation framework (three-pilot commitment), records must speak iteration counts explicitly and unambiguously.

## Decision

1. **Run ledgers** must declare `Iteration counts` with three distinct, defined counters:
   - *generation iterations* — fresh candidates produced from prompts;
   - *in-generation corrections* — defects found and corrected before evaluation (counted per corrected defect, not per fix pass);
   - *revision cycles* — material candidate changes after evaluation (the quality loop's `revising` state).
2. **Evaluation records** must declare `Iterations reviewed`: how many distinct builds and how many revision cycles the evaluation examined, with each build's hash (revision sections already numbered, e.g. "Revision 1").
3. **Other records** (SRC/CM/LP/XS/MEM) that can be superseded state their position in the supersession chain (e.g. "Iteration 2, supersedes LP-2026-0001"), because records are append-only and are corrected by linked supersession rather than in-place revision.
4. Existing records are **not retroactively rewritten**. Where real counts can be reconstructed, a dated retrospective appendix may document them (append-only-legal). The field is mandatory for records created on or after 2026-08-11.
5. This changes record/template fields and workflow phase notes; it does not change any gate, score, or traceability identity of artifacts.

## Decision drivers

- Repository rule: templates/record structure changes that affect traceability semantics require an ADR.
- Principle 7 (explicit contracts) and principle 9 (measurable, contestable quality): iteration counts make revision history answerable and auditable.
- The quality loop already distinguishes these states; the records simply failed to capture them numerically.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Rely on existing prose (Budget line, revision sections) | Zero work | Ambiguous; the three counters merge; not machine-checkable | Rejected |
| B. Mandatory structured counters in run/eval + supersession chain for others (chosen) | Unambiguous; three-part disambiguation matches the quality loop; calibrates future automation | Requires template edits and discipline on new records only | Selected |
| C. Retrofit every existing record | Complete coverage | Violates append-only for the old record bodies | Rejected; retrospective appendices used instead |

## Consequences

- Positive: iteration counts become first-class facts; comparisons across candidates and models become possible; the Stage 2 evaluation harness can read counts automatically.
- Negative/operational: creators must record counts at each phase (workflow P4/P6 note added).
- Educational/assessment: no learner-facing change.
- Reversibility: fully reversible by superseding this ADR; no historical record bodies were changed.

## Evidence and validation

Demonstrated retrospectively on RUN-20260810-0001 and EVAL-2026-0002 (dated appendices, 2026-08-11): generation = 1, in-generation corrections = 4, revision cycles = 1; EVAL reviewed 2 builds / 1 revision cycle. Validated formally by the next governed run.

## Rollback or migration plan

Supersede this ADR; template fields marked optional; records keep whatever counts exist.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-11 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: this ADR, the run/evaluation template fields, the workflow phase notes, and the two retrospective appendices. Decision: accept. Limitation: non-independent self-review — no second reviewer exists at Stage 1 — recorded per the policy's independence rule. Formal validation: the next governed run must exercise the new fields; this ADR is re-examined at the calibration review or the date below, whichever comes first.

## Review trigger/date

Review at the calibration review (three completed pilots) or 2026-11-04, whichever comes first.
