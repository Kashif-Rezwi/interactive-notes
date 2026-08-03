# Evidence Records

`records/` holds append-only evidence created by governed work. Source-provenance records exist at the documentation-foundation stage; no governed generation, evaluation, experiment, benchmark, or memory records exist yet. Do not place drafts, source originals, secrets, or unreviewed generated output here.

## Record rules

- Create a record from its template and give it a stable typed identifier.
- Preserve the original after correction; create a linked superseding record.
- Include classification, provenance, and access restrictions where applicable.
- Link records from their run ledger, decision, or authoritative document.
- Records establish evidence, not policy. Promote a recurring lesson only through the memory curation process.

| Directory | Record purpose | Standard template |
| --- | --- | --- |
| `runs/` | End-to-end generation and revision ledgers | `templates/run/` |
| `sources/` | Source identity, rights, and approved-use manifests | `templates/source/` |
| `evaluations/` | Scorecards, defects, adjudications | `templates/evaluation/` |
| `experiments/` | Bounded comparisons and outcomes | `templates/experiment/` |
| `memory/` | Curated lessons and supersession history | `templates/memory/` |
| `benchmarks/` | Frozen benchmark cases, charters, results | Benchmark protocol in `docs/06-evaluation/` |
| `decisions/` | Optional decision register/export | ADRs under `docs/adr/` remain canonical |
