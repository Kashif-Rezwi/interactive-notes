# RUN-YYYYMMDD-NNNN: Short outcome

**Status:** Planned | Generating | Evaluating | Reflecting | Revising | Validated | Released | Pilot complete | Stopped | Failed | Blocked (controlled values per [ADR-0007](../../docs/adr/0007-gate-arithmetic-and-record-status-hygiene.md), matching the quality-loop states; free-text nuance belongs in the body, not this field)<br>
**Parent run:**  
**Owner:**  
**Objective:**  
**Budget:** time / cost / reviewer effort  
**Iteration counts:** generation = ? ; in-generation corrections = ? ; revision cycles = ? (per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md); mandatory for records created on or after 2026-08-11 — generation = fresh candidates from prompts, in-generation corrections = defects corrected before evaluation, revision cycles = post-evaluation material changes)  
**Classification:** exploratory | production<br>
**Operating scope:** Stage 1 private pilot | public release candidate<br>
**Review-independence summary:** independent | non-independent | not applicable<br>
**Public-release eligibility:** eligible | ineligible | not assessed

## Input manifest

List source, concept model, plan, specification, prompt bundle, model/configuration, rubric, workflow, and benchmark versions.

(Prompt persistence rule: record the full un-redacted prompt snapshot in an appendix to this record or a linked in-repo file, alongside its SHA-256 digest. Digest-only references to out-of-band material are prohibited per prompt-architecture.md.)

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |

## Evaluation and defects

### Standing verification audits (P5 Audits 1–6)
- Audit 1 (Coverage):
- Audit 2 (Mathematical & canvas extrema):
- Audit 3 (Dependency order):
- Audit 4 (Pedagogical & depth-calibration contract):
- Audit 5 (Technical & behavioral simulation):
- Audit 6 (Rendered-output verification per ADR-0010: browser, console, responsive screenshots at ≥320px/640px/1024px, interaction traces, print, reduced-motion):

### Adversarial re-examination (mandatory gate per ADR-0009)
- Re-examination method(s): (read-in-order re-pass, behavioral simulation of edge cases, canvas extrema forcing, honesty/provenance scan)
- Elements covered:
- Findings & severity: (clean pass with documented evidence / defects routed to revising)

### Re-verification pass (WF-008)
- Sampled checks re-executed:
- Headline claims reproduced: (yes / discrepancy details)

## Reflection and root-cause hypothesis

## Revision history and regression checks

## Decision and approvers

**Final candidate identity at closure:** restate the current build's candidate ID, SHA-256, and byte size here (earlier builds remain in Generation events and revision sections)<br>
**Disposition:** released | private-pilot-complete | revise | hold | reject<br>
**Decision scope:** private pilot | public learner release<br>
**Approvers and limitations:**

## Memory disposition

Promoted memory IDs, rejected observations, and rationale.

## Lineage audit
