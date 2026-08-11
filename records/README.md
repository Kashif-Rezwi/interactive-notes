# Evidence Records

`records/` holds append-only evidence created by governed work. Source-provenance records exist at the documentation-foundation stage, and Stage 1 private pilots (RUN-20260804-0001, RUN-20260804-0002, RUN-20260810-0001) have populated concept, plan, specification, run, evaluation, and memory records. No experiment or benchmark records exist yet. Do not place drafts, source originals, secrets, or unreviewed generated output here.

## Record rules

- Create a record from its template and give it a stable typed identifier.
- Preserve the original after correction; create a linked superseding record.
- Include classification, provenance, and access restrictions where applicable.
- Link records from their run ledger, decision, or authoritative document.
- Records establish evidence, not policy. Promote a recurring lesson only through the memory curation process.
- **Iteration accounting (ADR-0006, effective 2026-08-11):** run ledgers declare `Iteration counts` (generation / in-generation corrections / revision cycles); evaluations declare `Iterations reviewed` (builds / revision cycles); supersedable records state their iteration/supersession position. Existing records predate these fields and are not retroactively rewritten; where real counts are reconstructable, a dated retrospective appendix documents them.

| Directory | Record purpose | Standard template |
| --- | --- | --- |
| `runs/` | End-to-end generation and revision ledgers | `templates/run/` |
| `sources/` | Source identity, rights, and approved-use manifests | `templates/source/` |
| `concepts/` | Source-grounded concept models with anchored claims | `templates/concept/` |
| `plans/` | Learning plans with measurable outcomes | `templates/learning/` |
| `specifications/` | Experience specifications for learner artifacts | `templates/lesson/` |
| `evaluations/` | Scorecards, defects, adjudications | `templates/evaluation/` |
| `experiments/` | Bounded comparisons and outcomes | `templates/experiment/` |
| `memory/` | Curated lessons and supersession history | `templates/memory/` |
| `benchmarks/` | Frozen benchmark cases, charters, results | Benchmark protocol in `docs/06-evaluation/` |
| `decisions/` | Optional decision register/export | ADRs under `docs/adr/` remain canonical |
