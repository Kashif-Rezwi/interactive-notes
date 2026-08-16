# ADR-0011: Define unified benchmark representation and controlled artifact-change protocol

**Status:** Accepted  
**Date:** 2026-08-14  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Benchmark governance, context assembly (P1–P4), and artifact modification lifecycle  
**Supersedes / superseded by:** none

## Context and problem

The comprehensive audit ([comprehensive-workflow-and-benchmark-audit.md](../audit/comprehensive-workflow-and-benchmark-audit.md)) identified three interlocking gaps in how the pipeline represents and governs its benchmark:

1. **Benchmark excluded from generation context (WF-005):** V5 was run under an experimental condition where prior candidates were explicitly excluded from context, resulting in a compliant-minimum collapse. While rules were codified, the concrete structural exemplar (what 178 KB of depth looks like in practice) was absent from generation inputs.
2. **Post-evaluation artifact mutation (WF-009):** The benchmark artifact (CAN-2026-0003, `linear-algebra-foundations-v4.html`) underwent three owner-directed edit passes post-evaluation (clarifications/un-gating on 08-11, colophon retrofit on 08-13, and banner removal on 08-13) without re-running a full governed generation run or evaluation. While tracked via append-only appendices, no formalized change protocol governed these edits.
3. **Dual benchmark identity (WF-012):** The lesson standard named CAN-2026-0003 (v4) as the "reference implementation," while the module README named CAN-2026-0005 (v6) as the "reference lesson," creating ambiguity about which artifact defines the quality bar.

## Decision

1. **Unified benchmark authority:**
   - Establish `records/benchmarks/` as the single authoritative home for frozen benchmark definitions.
   - Designate [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) (CAN-2026-0003, `linear-algebra-foundations-v4.html`, hash `b35c622e…1590`) as the primary benchmark for the AIML-4 Module 2 family.
   - All references in `docs/01-product/lesson-standard.md`, `README.md`, and prompt cards point to `BMK-2026-0001`.
   - Distinguish terminology: a **benchmark** is an immutable frozen reference standard; a **reference candidate** is the latest compliant governed artifact (currently CAN-2026-0005, v6) used as an authoring starting point.
2. **Benchmark in context assembly (P1–P4):**
   - The active benchmark record (BMK) and its measured characteristics inventory are explicit inputs to P1–P4 context assembly.
   - **Context policy:** Lesson planning (P2) and experience specification (P3) must consult the active benchmark definition as a calibration exemplar for depth, widget complexity, and assessment rigor.
   - **Permitted exclusion:** A generation run may deliberately exclude the benchmark from context only when executing a documented experiment (e.g. testing whether rules alone suffice), and must record the rationale in the run manifest and linked experiment record.
3. **Controlled artifact-change protocol:**
   - Any modification to an evaluated, governed learner artifact outside an active generation run must follow a strict change protocol:
     a. Record a change event in the parent run ledger and evaluation record via a dated appendix.
     b. Document the explicit rationale (e.g. brand colophon standardization, typo correction).
     c. Record pre-change and post-change SHA-256 hashes and byte counts.
     d. Define and execute a targeted re-check scope (syntax, recomputation, regression check).
     e. If the change alters pedagogy, sequencing, or interaction models, route the change into a new governed revision cycle (`revising`) or new candidate version.

## Decision drivers

- Principle 7 (explicit contracts), Principle 8 (governed lineage), and Principle 9 (measurable quality).
- Audit findings WF-001, WF-005, WF-009, and WF-012.
- Preventing ambiguity between benchmark standards and latest experimental builds.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Maintain separate "reference implementation" and "reference lesson" terms | No documentation edits needed | Continued confusion about which artifact sets the quality bar | Rejected |
| B. Prohibit any post-evaluation artifact edits under any circumstance | Absolute immutability | Forces full re-runs for non-pedagogical styling/colophon updates | Rejected |
| C. Formal benchmark record + explicit context policy + controlled change protocol (chosen) | Unambiguous single source of truth; permits documented non-pedagogical adjustments while maintaining strict hash lineage | Requires discipline in recording change events | Selected |

## Consequences

- Positive: Clarifies benchmark identity across the entire repository; prevents uncalibrated generations by embedding the benchmark into context assembly; creates an auditable protocol for artifact maintenance.
- Operational: Updates `docs/01-product/lesson-standard.md`, `docs/03-workflows/lesson-generation-workflow.md`, `content/aiml-4/module-02-math-statistics-for-ml/README.md`, and `records/README.md`.
- Reversibility: Fully reversible by superseding this ADR.

## Evidence and validation

- Benchmark record `BMK-2026-0001` created under `records/benchmarks/`.
- Cross-links across documentation and module packages verified by `scripts/check-repo.py`.

## Rollback or migration plan

Supersede this ADR and return to prior informal reference terminology.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-14 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: this ADR, BMK-2026-0001, and cross-references. Decision: accept. Limitation: non-independent self-review recorded per policy.

## Review trigger/date

Review at the Stage 1 calibration review or 2026-11-04, whichever comes first.
