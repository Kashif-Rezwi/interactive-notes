# Future Implementation Plan

Implementation begins only after Stage 1 evidence supports automation. The plan below is intentionally capability-oriented, not a code design.

## Sequence

1. **Formalize contracts.** Convert approved plain-language artifact contracts into versioned machine-readable schemas without changing their meaning. Validate against manual records.
2. **Build provenance first.** Create identity, lineage, record, access-classification, and retention capabilities before generation features.
3. **Automate a thin vertical slice.** Support one authorized source type and one artifact family from intake through independent evaluation and memory disposition.
4. **Build evaluation alongside generation.** No generator integration is complete without rubric capture, benchmark comparison, review workflow, and stop conditions.
5. **Add reviewer-facing tools before broad learner UI.** Experts need evidence, diffs, citations, defects, and release controls to govern output.
6. **Implement rendering/runtime behind specifications.** Technology choices must satisfy accessibility, interaction, performance, and provenance acceptance criteria documented in an ADR.
7. **Introduce learner data only by consented hypothesis.** Instrument strictly necessary events with transparent purpose, retention, and opt-out controls.
8. **Scale through modules.** Separate ingestion, knowledge modeling, planning, generation, evaluation, registry/memory, and artifact delivery so the workflow remains inspectable.

## First implementation ADRs

Before writing code, decide data classification/retention, source attribution, schema and identity strategy, model gateway/provider policy, benchmark storage, human review authority, initial source/artifact slice, and accessibility baseline.

## Acceptance criteria for the first vertical slice

- An authorized input is transformed only through version-pinned artifacts.
- A reviewer can reconstruct the complete lineage without reading model internals.
- A candidate cannot release without required factual, educational, and accessibility evidence.
- A targeted revision produces a parent/child run comparison and preserves the baseline.
- A validated lesson is either curated to memory with scope/confidence or explicitly rejected.
- The process works with manual fallback and does not depend on undocumented human knowledge.
