# Long-Term Memory Architecture

## Purpose

The system should improve because it remembers validated lessons about pedagogy, prompts, quality, interaction design, models, workflows, and architecture. Memory must remain inspectable, scoped, and reversible.

## Memory layers

| Layer | Contents | Authority | Retention |
| --- | --- | --- | --- |
| Working context | Active request, selected sources, current plan, temporary hypotheses | Run-local | Ends with run unless promoted |
| Episodic record | Complete run events, outputs, scores, reflections, errors | Evidence, not policy | Retain under logging policy |
| Semantic memory | Curated reusable lessons, patterns, known failure modes, decision rationale | Guidance with confidence | Reviewed and versioned |
| Procedural memory | Approved playbooks, templates, prompt cards, rubrics, agent contracts | Operational standard | Maintained until superseded |
| Benchmark memory | Frozen cases, baselines, calibration outcomes | Measurement standard | Immutable version history |

## Memory item types

Successful prompt patterns; failed prompt patterns; pedagogical tactics; visualization/animation patterns; accessibility lessons; UX findings; model strengths/limits; common source-ingestion failures; architecture decisions; cost/latency trade-offs; and risk controls.

## Retrieval rules

Retrieve memory by task, artifact family, learner context, domain, risk class, source type, quality dimension, and confidence. Retrieval returns the lesson **with** scope, evidence, age, conflicts, and status. It is advisory; current source evidence and explicit policy take precedence.

## Safety and privacy

Never store secrets, private learner data, copyrighted source text beyond the approved basis, hidden chain-of-thought, or unverified personal judgments in durable memory. Redact before curation. Access classification travels with a memory item and is enforced before future automation is introduced.

## Relationship to logs

Logs answer “what happened in this run?” Memory answers “what should influence similar work later?” A reflection is a candidate memory source, not memory by default.
