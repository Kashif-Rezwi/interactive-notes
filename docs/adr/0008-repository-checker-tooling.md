# ADR-0008: Adopt the repository checker as governance tooling

**Status:** Accepted  
**Date:** 2026-08-13  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Repository-maintenance tooling only — no application code, no runtime, no product commitment  
**Supersedes / superseded by:** none

## Context and problem

The repository's acceptance criteria require mechanically checkable invariants: links must resolve (ADR-0001), preserved bytes must keep their hashes (content-package convention, source manifests), rubric weights must sum to 100 (ADR-0007), record status fields use controlled vocabularies (ADR-0007), and ADRs must be indexed. Until now every one of these was verified by hand. The 2026-08-13 audit demonstrated the cost: the rubric weights had summed to 98 against a stated 100 since the framework was written, and no process caught it, because nothing executed the check. The same audit's manual verification scripts immediately surfaced four further defects (stale registry claim, filename-convention violation, missing coverage matrix, factual drift in `records/README.md`).

The charter forbids application implementation in this phase. A read-only hygiene checker is repository-maintenance tooling, not product code: it builds nothing, serves no learner, and commits the future system to no technology.

## Decision

1. Adopt `scripts/check-repo.py` — a single-file, Python 3 standard-library-only, read-only, offline, deterministic checker — as governed repository tooling. It asserts exactly seven written conventions:
   - **Links:** every relative link in every Markdown file resolves to an existing path.
   - **Hashes:** every file under `content/` has its current SHA-256 cited in at least one Markdown record (provenance coverage), and every source manifest in `records/sources/` declares the current hash of each content file it links.
   - **Weights:** the evaluation framework's dimension weights sum to exactly 100 and match the table's Total row (ADR-0007 weight-integrity rule).
   - **Status vocabularies:** record headers use the ADR-0007 controlled vocabularies per record type; pre-ADR-0007 deviations pass only through an explicit grandfather list that encodes ADR-0007 §5's declared equivalences.
   - **README metadata:** `docs/README.md` and numbered section READMEs declare Status, Owner, Review by, and Applies to (documentation standard).
   - **Filenames:** record filenames are lowercase kebab-case (README.md excepted); generated artifacts match `<note-slug>-v<N>.<ext>` (naming conventions); source originals are exempt (preserved filenames).
   - **ADR index:** every `docs/adr/NNNN-*.md` appears in the ADR index.
2. Usage rule: run `python3 scripts/check-repo.py` before committing a change that touches governed surfaces (docs, records, templates, library, content READMEs) and at every run closure; it must exit 0. There is no hosted CI at Stage 1; adoption as a CI gate is a separate future decision.
3. Boundaries: the checker enforces conventions that are already written down — it never introduces a rule, never modifies a file, never executes or scores an artifact, and is not the Stage 2 evaluation harness. A new asserted invariant requires a governing document first; the checker then encodes it. Adding to the grandfather list requires an ADR or an explicit equivalence declaration in one.
4. The checker changes under the normal change protocol: defect fixes freely; new checks follow rule 3.

## Decision drivers

- Principle 9 (measurable and contestable): an invariant that is never executed is a hope, not a control.
- Principle 12 (earn complexity): one zero-dependency script replaces recurring manual verification; no service, no build step, no lockfile.
- The audit evidence: four of the Phase A/B defects were mechanically detectable years earlier than any human review cadence would have caught them.
- Charter non-goals are respected: this is maintenance tooling for the documentation system, not the beginning of the application.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Keep manual verification | Zero tooling | Demonstrated failure (the 98-weight bug survived every review); does not scale to lesson 2 | Rejected |
| B. Hosted CI (GitHub Actions et al.) | Automatic on every push | External service commitment, configuration surface, and cost/identity decisions the roadmap defers; overkill for a solo operator | Rejected for Stage 1; revisit at Stage 2 |
| C. Local zero-dependency script (chosen) | Runs anywhere Python 3 exists; read-only; auditable in one file; no supply chain | Maintainer must remember to run it; conventions must be encoded as they evolve | Selected |
| D. Full machine-readable schema validation | Deep verification | Stage 2 scope per the roadmap and future-implementation plan; premature now | Rejected for now |

## Consequences

- Positive: the seven invariants become executable in seconds; audit-class regressions (broken links, orphaned artifacts, weight drift, vocabulary drift, unindexed ADRs) fail loudly at commit time instead of silently compounding.
- Negative/operational: the script must evolve with the conventions it encodes; the grandfather list is the machine-readable form of ADR-0007 §5 and grows only through declared equivalences.
- Boundaries preserved: no application code, no dependency, no runtime, no CI commitment; `scripts/` is added to the repository map with its own change rule.
- Reversibility: fully reversible — delete `scripts/`, supersede this ADR; no record, artifact, or hash is affected.

## Evidence and validation

- The manual equivalents of these checks drove the 2026-08-13 audit: the link checker (0 broken links, re-run after every phase), the hash re-verification (all five content files match their recorded SHA-256s), and the weight-sum recomputation (98 vs 100, the audit's critical finding).
- Post-adoption validation: the checker exits 0 over the repository state after the Phase A/B repairs, and each check was verified to fail when its invariant is deliberately broken (dry-run fault injection during authoring).
- The checker is exercised at every subsequent governed-run closure and conventions commit.

## Rollback or migration plan

Delete `scripts/` and supersede this ADR. Nothing else references the checker except usage guidance (AGENTS.md) and the repository-map entry, both of which name this ADR.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-13 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: the script's seven checks against their governing documents (naming conventions, documentation standard, ADR-0007, content-package convention, ADR strategy), the script's read-only behavior, and its output on the current repository. Evidence considered: the 2026-08-13 audit findings the checks would have caught, and the clean post-Phase A/B run. Decision: accept. Limitation: non-independent self-review — no second reviewer exists at Stage 1 — recorded per the policy's independence rule.

## Review trigger/date

Review when Stage 2 automation begins (the checker's semantics fold into the evaluation harness and a CI decision is made), when a new asserted invariant is proposed without a governing document, or by 2026-11-04, whichever comes first.

