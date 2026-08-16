# ADR-0007: Correct evaluation gate arithmetic and standardize record status vocabularies

**Status:** Accepted  
**Date:** 2026-08-13  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Evaluation-framework weight table and gate formula; status vocabularies of record templates (RUN/XS/CM/LP/MEM/SRC)  
**Supersedes / superseded by:** the `/100` formula clause in the Decision section of [ADR-0003](0003-stage-1-pilot-evidence-and-gate-semantics.md) only — all other ADR-0003 semantics (0.5-point score precision, gate thresholds, pilot dispositions, controlled pilot fields) are unchanged

## Context and problem

A full-repository audit on 2026-08-13 surfaced two correctness defects and one hygiene defect:

1. **Gate arithmetic bug.** The evaluation framework's dimension weights are 18 + 18 + 10 + 10 + 14 + 8 + 8 + 6 + 4 + 2 = **98**, while the table's Total row claims **100%** and the gate formula divides by 100. Consequences: a perfect candidate can score at most 3.92; every recorded aggregate is deflated ~2% (EVAL-2026-0001 recorded 3.37; EVAL-2026-0002 recorded 3.51); and the ≥ 3.5 gate is silently a 3.57 bar on a normalized scale. This document is the sole authoritative numeric release-gate definition, so the error sits in the most load-bearing number in the repository.
2. **Status vocabulary sprawl.** The glossary deliberately keeps lifecycle vocabularies distinct, but practice drifted: run ledgers used off-template free-text statuses ("Generation complete; evaluation pass pending"); the two experience specifications use two different scope-laden phrasings ("Approved for Stage 1 private-pilot generation" / "Approved for Stage 1 governed generation"); the memory template labels its confidence field `Status:`, conflating the two axes the glossary separates; and the concept-model/learning-plan templates offer an unused, undefined `Approved` value while every real record uses `Reviewed`.
3. **Template/record divergence risk.** Records are append-only and are not retroactively rewritten, so the repair surface is the template set plus dated retrospective appendices — the convention established by ADR-0006.

## Decision

1. **Weight correction.** The `Technical feasibility/performance intent` dimension weight changes from 2% to 4%. The weights now sum to exactly 100, matching the Total row. At 2% the dimension was below meaningful discrimination, and no other weight changes. Standing rule: the dimension weights must always sum to exactly 100; a weight edit that breaks the sum is a defect in the gate definition. The sum is verified arithmetically at every weight edit and at the calibration review; a proposed repository-checker tool (separate tooling decision) will assert it mechanically.
2. **Formula normalization.** The weighted score is `sum(dimension score × dimension weight) / sum(dimension weights)` — with the required sum of 100 this equals division by 100 today, and the formula is structurally immune to a future sum drift. Comparison to gates remains unrounded; display remains two decimal places. Gate thresholds (hard gates ≥ 3.5; others ≥ 3; weighted ≥ 3.5) are unchanged.
3. **Retrospective recomputation.** Dated appendices on EVAL-2026-0001 and EVAL-2026-0002 record the corrected aggregates — **3.45** (was 3.37) and **3.59** (was 3.51) respectively. No gate outcome, disposition, confidence, or public-release eligibility changes: EVAL-2026-0001 still fails the weighted gate diagnostically, EVAL-2026-0002 still passes it diagnostically, both still fail the accessibility hard gate, and both remain `ineligible` for public release under non-independent review.
4. **Record status vocabularies (templates; mandatory for records created on or after 2026-08-13):**
   - **Run ledger:** `Status` must be one of the controlled values matching the quality-loop state machine (Planned | Generating | Evaluating | Reflecting | Revising | Validated | Released | Pilot complete | Stopped | Failed | Blocked). Free-text nuance belongs in the body or a dated appendix, not the status field.
   - **Experience specification:** `Draft | Approved | Superseded`. The approval scope (e.g. "Stage 1 governed generation") is declared in the record body, not in the status value.
   - **Concept model / learning plan:** `Draft | Reviewed | Superseded`, where `Reviewed` means reviewed within the declared scope and usable as a governed input. The unused, undefined `Approved` value is removed.
   - **Memory item:** the header field is renamed `Status:` → `Confidence:`; values (Tentative | Supported | Established | Disputed | Retired) are unchanged and match the glossary's memory-confidence vocabulary.
   - **Source package:** template wording aligned to the in-force record phrasing `Approved for the recorded use`.
5. **Existing record bodies are not rewritten** (append-only). Declared equivalences: MEM `Status: Supported` ≡ `Confidence: Supported`; XS scope-laden phrasings ≡ `Approved`; historical run free-text statuses are read through their bodies and appendices.

## Decision drivers

- Principle 9 (measurable and contestable quality): a gate whose arithmetic is wrong is neither.
- Principle 7 (explicit contracts): status fields are contracts; free text defeats querying and the Stage 2 harness.
- The repository-map change rule: template changes that affect traceability semantics require an ADR — this is that ADR.
- Append-only record discipline (ADR-0006 appendix convention) makes correction-without-rewrite possible.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Fix only the Total row (declare 98%) | Smallest edit | Freezes an arbitrary 98; the /100 formula still deflates and caps scores at 3.92; future weight edits can re-break it | Rejected |
| B. Rebalance to 100 + normalize formula by Σweights (chosen) | Table becomes truthful; formula immune to recurrence; one small, justified weight change | Historical aggregates shift (documented via appendices); backward comparison needs the appendix note | Selected |
| C. Rewrite historical EVAL bodies in place | Single set of numbers | Violates append-only evidence rules | Rejected |
| D. Leave status vocabularies free-form | Zero work | Off-template values already observed; Stage 2 automation would ingest ambiguity | Rejected |
| E. Controlled vocabularies via templates + this ADR (chosen) | Queryable, harness-ready, matches quality-loop states | Small template churn; historical records keep their values under declared equivalence | Selected |

## Consequences

- Positive: the sole gate authority is now arithmetically correct and self-defending; recorded aggregates become truthful via appendices; status fields become machine-checkable; templates and the glossary's vocabulary separation are consistent.
- Negative/operational: any future weight edit carries a sum-verification duty; pre-2026-08-13 aggregates are labeled as computed under the defective formula (the appendices carry both values).
- Backward comparison: EVAL-2026-0001 3.37 → 3.45; EVAL-2026-0002 3.51 → 3.59. No gate outcome, disposition, or eligibility changes for either record.
- Reversibility: fully reversible by superseding this ADR; appendices remain as history.

## Evidence and validation

- Audit recomputation (2026-08-13): weights summed to 98 against a stated Total of 100; max achievable score 3.92; EVAL-2026-0001 numerator 337 → 337/100 = 3.37 recorded vs 345/100 = 3.45 corrected; EVAL-2026-0002 numerator 351 → 351/100 = 3.51 recorded vs 359/100 = 3.59 corrected (Technical weight 4 in both corrections).
- Gate outcomes re-checked after correction: unchanged for both records (see the EVAL appendices).
- Vocabulary sprawl evidence: run-20260804-0002 and run-20260810-0001 status lines; xs-2026-0001 vs xs-2026-0002 status phrasings; memory template field label; glossary lifecycle-vocabulary section.
- Validation: this ADR is exercised by the next governed run (status fields) and at the calibration review (weight-sum check).

## Rollback or migration plan

Supersede this ADR with a new decision; restore the prior weights and formula in the framework; the retrospective appendices remain as history. No artifact bytes, hashes, identities, or release states are affected by this ADR, so no migration exists.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-13 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: the evaluation framework weight table and gate rules, the ADR-0003 formula clause, EVAL-2026-0001 and EVAL-2026-0002 scorecards and arithmetic, the six affected record templates, the glossary lifecycle vocabularies, and existing record status usage. Evidence considered: the 2026-08-13 audit recomputation and cross-file vocabulary scan. Decision: accept. Limitation: non-independent self-review — no second reviewer exists at Stage 1 — recorded per the policy's independence rule.

## Review trigger/date

Review at the calibration review (three completed pilots) or by 2026-11-04, whichever comes first; also review immediately if any future weight edit is proposed before the repository checker asserts the sum automatically.

