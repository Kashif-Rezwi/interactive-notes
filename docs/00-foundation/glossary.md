# Glossary

| Term | Meaning |
| --- | --- |
| Artifact | A learner-facing result or an internal planning/review object with a stable identity. |
| Adjudication | Accountable resolution of a material reviewer disagreement that preserves original evidence and residual uncertainty. |
| Benchmark | A frozen, versioned set of authorized cases used to compare prompts, models, roles, or workflows. |
| Bounded context | A named area of responsibility with clear ownership and exclusions, such as source stewardship or evaluation. |
| Calibration | Comparing evaluators or rubric interpretations against shared cases to make score meaning more consistent. |
| Candidate | A generated artifact that has not passed the release gate. |
| Concept model | Structured representation of claims, prerequisites, relationships, examples, and misconceptions extracted from source material. |
| Evaluation | Evidence-backed scoring of a candidate against a versioned rubric. |
| Escalation | A documented transfer of a risk, uncertainty, or decision to the role with the required authority or expertise. |
| Experience specification | The artifact-level contract for learner task, interaction, representation, accessibility, and acceptance criteria; it consumes a learning plan. |
| Exploration | Bounded, isolated work that may inform future production but cannot silently alter approved assets or release policy. |
| Generation run | One traceable attempt to transform a defined input under a named plan, prompt set, and model configuration. |
| Generation iteration | A fresh candidate produced from a prompt within a single generation run (ADR-0006 iteration accounting). |
| Handoff packet | Minimum information required for one role to transfer accountable work to another. |
| Hard gate | A non-negotiable release condition that a weighted score cannot override. |
| In-generation correction | A defect found and corrected before evaluation, counted per corrected defect (ADR-0006 iteration accounting). |
| Intake | The initial classification of a request's scope, source rights, risk, owner, and intended use. |
| Lesson | A coherent learner journey defined by outcomes, sequence, interaction, assessment, and accessibility intent. |
| Memory | Curated, reusable knowledge with provenance and a lifecycle; not raw history. |
| Playbook | A controlled operational procedure with trigger, owner, inputs, outputs, evidence, exit criteria, and escalation path. |
| Production | Governed work that consumes approved inputs, records full lineage, and must pass required release controls. |
| Private pilot | A bounded, non-public Stage 1 evaluation run. It may close as `private-pilot-complete` but is not a public learner release, benchmark result, or permission to distribute a candidate. |
| Public learner release | A decision to make a governed learner-facing artifact available to learners. It is distinct from authorization to publicly distribute a source package. |
| Prompt card | A versioned prompt asset with purpose, inputs, constraints, examples, tests, and change history. |
| Quality loop | The simplified lifecycle Plan → generate → evaluate → reflect → improve → validate → learn; its authoritative state machine also includes release and stop/fail/blocked outcomes. |
| Record | Immutable or append-only evidence about a decision, run, evaluation, experiment, or memory item. |
| Release Steward | The role that audits evidence and recommends a release disposition; it cannot waive specialist or human-owner controls. |
| Release eligibility | The recorded determination that a candidate is eligible or ineligible for public learner release. A non-independent review makes it ineligible. |
| Review independence | Whether a Reviewer was independent of the Creator for the same candidate. `Non-independent` is permitted only for a private pilot. Canonical rule and controlled record fields: ADR-0003. |
| Revision cycle | A post-evaluation material change to a candidate — the quality loop's `revising` state (ADR-0006 iteration accounting). |
| Role card | The operational contract for an active role: purpose, authority, inputs, outputs, controls, failure modes, and retirement criteria. |
| Source package | The rights-aware, versioned set of material and metadata supplied for transformation. |
| Traceability graph | Links connecting source, plans, prompts, model, candidate, evaluation, decisions, and release. |

## Lifecycle vocabularies

Document status describes guidance authority: Draft, Experimental, Approved, Deprecated, Superseded, or Archived. ADR lifecycle describes an architectural decision: Draft, Proposed, Accepted, Rejected, Deprecated, or Superseded. Prompt lifecycle describes readiness for use: draft, experimental, approved, deprecated, or retired. Memory confidence describes strength of evidence: Tentative, Supported, Established, Disputed, or Retired. These vocabularies are intentionally distinct because authority, decision state, operational readiness, and evidence confidence are different concepts.
