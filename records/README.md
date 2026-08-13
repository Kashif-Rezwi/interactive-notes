# Evidence Records

`records/` holds append-only evidence created by governed work. Source-provenance records exist at the documentation-foundation stage, and Stage 1 private pilots (RUN-20260804-0001, RUN-20260804-0002, RUN-20260810-0001) have populated concept, plan, specification, run, evaluation, and memory records (RUN-20260804-0002's evaluation is formally deferred — see its Appendix B — so that run has no evaluation record). No experiment or benchmark records exist yet. Do not place drafts, source originals, secrets, or unreviewed generated output here.

## Record rules

- Create a record from its template and give it a stable typed identifier.
- Preserve the original after correction; create a linked superseding record.
- Include classification, provenance, and access restrictions where applicable.
- Link records from their run ledger, decision, or authoritative document.
- Records establish evidence, not policy. Promote a recurring lesson only through the memory curation process.
- **Iteration accounting (ADR-0006, mandatory for records created on or after 2026-08-11):** run ledgers declare `Iteration counts` (generation / in-generation corrections / revision cycles); evaluations declare `Iterations reviewed` (builds / revision cycles); supersedable records state their iteration/supersession position. Existing records predate these fields and are not retroactively rewritten; where real counts are reconstructable, a dated retrospective appendix documents them.
- **Filename-correction propagation:** when an artifact or record file is renamed without content change (bytes and hash unchanged for learner-facing artifacts, per the naming conventions), references in existing records may be updated in place to the new path with a `(renamed from …; bytes unchanged)` note and a traceable commit. This is the only permitted in-place edit to a record's original body; all evidence content remains append-only.

| Directory | Record purpose | Standard template |
| --- | --- | --- |
| `runs/` | End-to-end generation and revision ledgers | `templates/run/` |
| `sources/` | Source identity and provenance records | — |
| `concepts/` | Source-grounded concept models with anchored claims | `templates/concept/` |
| `plans/` | Learning plans with measurable outcomes | `templates/learning/` |
| `specifications/` | Experience specifications for learner artifacts | `templates/lesson/` |
| `evaluations/` | Scorecards, defects, adjudications | `templates/evaluation/` |
| `experiments/` | Bounded comparisons and outcomes | `templates/experiment/` |
| `memory/` | Curated lessons and supersession history | `templates/memory/` |
| `benchmarks/` | Frozen benchmark cases, charters, results | Benchmark protocol in `docs/06-evaluation/` |

`decisions/` is intentionally not populated at Stage 1 — ADRs under `docs/adr/` remain the canonical decision narrative. Create the register only when a searchable export is first needed.

## Stage 1 progress scoreboard

Updated at each run closure (last update: 2026-08-13). Canonical commitments: the ADR-0002/ADR-0003 review triggers and the evaluation framework's calibration commitment.

| Commitment | Target | Current state | What closes the gap |
| --- | --- | --- | --- |
| Completed private pilots | 3 | **3 ✓** (RUN-20260804-0001, RUN-20260810-0001, RUN-20260813-0001) | Met |
| Source packages represented | ≥ 2, or 3 materially distinct candidates from one package recorded as limited evidence | 1 package (SRC-2026-0001); **3 distinct evaluated candidates exist (v2, v4, v5) — fallback satisfiable as limited evidence** | Calibration review may proceed on limited evidence; a second SRC record still strengthens it |
| Evaluated candidates | 3 | **3 ✓** (EVAL-2026-0001, EVAL-2026-0002, EVAL-2026-0003) | Met via the v5 regeneration run; CAN-2026-0002's deferred evaluation (RUN-20260804-0002 Appendix B) remains open — its cross-model comparison objective is unaffected |
| Independent review | Required for any public release | None yet (all reviews non-independent) | External reviewer; not a Stage 1 blocker |
