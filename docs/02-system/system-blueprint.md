# System Blueprint

## Architectural thesis

Learning OS is a **governed transformation pipeline with a learning loop**, not a single content generator. It separates source understanding, pedagogical planning, artifact design, generation, quality assurance, release judgment, and organizational learning so each can be inspected and improved independently.

## Future bounded contexts

| Context | Owns | Must not own |
| --- | --- | --- |
| Source stewardship | Rights, source identity, extraction evidence, citations | Pedagogical claims or generated output approval |
| Knowledge modeling | Concepts, claims, prerequisites, relationships, misconceptions | Presentation and model-provider choices |
| Learning design | Outcomes, sequence, assessment, teaching strategy | Rendering implementation |
| Experience design | Interaction, visualization, accessibility intent, UX specification | Source-rights approval or factual adjudication |
| Generation | Candidate artifacts from approved plans and prompts | Final quality decisions |
| Evaluation and review | Rubrics, evidence, adjudication, release recommendation | Silent modification of candidates |
| Learning operations | Runs, experiments, prompts, memory, benchmarks, reports | Unreviewed policy changes |

## Conceptual lifecycle

```text
Authorized source package
  → extraction evidence
  → concept model
  → learning plan + experience specification
  → candidate artifact
  → evaluation evidence + review
  → release decision
  → reflection and curated memory
  ↘ traceability graph connects every stage ↗
```

The complete operational sequence is in [workflow architecture](../03-workflows/workflow-architecture.md). A stage may not consume an unapproved upstream artifact unless the record explicitly labels it exploratory.

## Stable identities

Every durable object receives a human-readable, immutable identifier: source package, concept model, plan, specification, prompt card, generation run, candidate, evaluation, decision, experiment, benchmark, and memory item. Identifiers permit lineage without relying on a file path or model provider.

## Design boundaries

- **Specification vs implementation:** plans describe intended behavior; future code realizes it and must trace back to the specification.
- **Candidate vs released artifact:** generation cannot self-certify release.
- **Measurement vs judgment:** automated metrics inform, but do not replace, rubric evidence and accountable review.
- **Raw history vs memory:** logs are complete but noisy; memory is compact, curated, and confidence-scoped.
- **Public vs restricted knowledge:** rights, privacy, and learner sensitivity determine storage and access before transformation.

## Technology neutrality

The future system may use a database, graph store, model gateway, queue, object storage, renderer, or frontend framework. These are implementation choices, not requirements of the operating model. Select them only after an ADR compares operational needs, cost, portability, privacy, and reversibility.
