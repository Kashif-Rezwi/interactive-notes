# Agent Catalog

This is the 18-role reference architecture. Stage 1 activates only five composites; see the [Stage 1 operating profile](stage-1-operating-profile.md) and its role cards before assigning work.

All agents use the universal handoff packet and may only act within their boundary. “Human reviewer” is a required control role, not a fallback for agent uncertainty.

| Agent | Purpose | Inputs → Outputs | Responsibilities | Boundary | Success criteria |
| --- | --- | --- | --- | --- | --- |
| Orchestrator | Coordinate a traceable workflow | Request, policies → plan, assignments, state | Triage, sequence, budgets, escalation | Does not invent facts or self-release | Each stage has an owner, state, and complete lineage |
| Source Steward | Protect source integrity and provenance | Source package → identity and manifest | Source identity, provenance, citation anchors | Does not interpret pedagogy | All use is traceable |
| Parser | Extract structured evidence | Authorized source → extraction evidence | Segment, normalize, locate claims and figures | Does not decide truth beyond source fidelity | Material content is recoverable with anchors |
| Concept Extractor | Build the concept model | Extraction evidence → concept model | Concepts, dependencies, examples, ambiguities | Does not create presentation | Claims and relations are source-supported |
| Domain/Math Reviewer | Validate domain truth | Concept/candidate → factual review | Check definitions, derivations, units, edge cases | Does not optimize UX | No unsupported material claims remain |
| Teacher | Translate knowledge into teaching | Concept model → explanation strategy | Analogies, sequence, misconceptions, formative checks | Does not approve source authorization | Outcomes are teachable and aligned |
| Curriculum Planner | Design a coherent progression | Concept model, learner profile → learning plan | Objectives, prerequisites, sequence, assessment alignment | Does not render artifacts | Each outcome has instruction and evidence of learning |
| Visualization Planner | Specify explanatory representations | Learning plan → visualization plan | Encodings, controls, annotations, failure modes | Does not implement visuals | Every visual answers a learning question |
| Experience/Interaction Planner | Specify learner action and feedback | Learning plan → experience specification | Interaction states, feedback, pacing, recovery | Does not claim factual correctness alone | Interactions produce meaningful learning evidence |
| Accessibility Reviewer | Ensure inclusive, usable experience | Specification/candidate → accessibility report | Alternatives, keyboard/readability/cognitive checks | Does not waive factual gates | Equivalent learning path is specified and verified |
| Generator | Produce bounded candidate artifacts | Approved specs, prompts → candidate/run | Follow constraints, preserve provenance, disclose limits | Cannot self-certify release | Candidate meets specification readiness criteria |
| Reviewer | Find cross-cutting defects | Candidate, rubric → review report | Completeness, consistency, requirement coverage | Cannot silently repair work | Defects are evidenced and actionable |
| Evaluator | Measure against rubric/benchmark | Candidate, rubric → scorecard | Score with evidence, confidence, and uncertainty | Cannot alter rubric to pass a candidate | Scores are calibrated, reproducible, explainable |
| Logger | Preserve operational evidence | Workflow events → run ledger | Timestamps, versions, costs, errors, decisions | Does not curate guidance | Ledger reconstructs what happened |
| Memory Manager | Convert evidence into reusable learning | Reflections, experiments → memory disposition | Deduplicate, scope, confidence, expiry, retrieval tags | Does not promote raw opinions | Approved memory is useful and traceable |
| Documentation Manager | Maintain repository coherence | Changes, ADRs → updated docs/indexes | Information architecture, links, terminology, lifecycle | Does not make unapproved policy | A new agent can find authoritative guidance |
| Release Steward | Make controlled release recommendation | Evidence bundle → release decision | Gate audit, acknowledgments, rollback/revision plan | Cannot overrule specialists silently | Decision is accountable and auditable |
| Human Accountable Owner | Hold final responsibility | Escalations → binding decisions | Risk acceptance, policy, public release, conflict resolution | Must not delegate accountability | Decisions are timely, explicit, and recorded |

## Agent definition standard

Before activating or adding a role, create a role card containing: purpose; trigger; inputs; outputs; authority; prohibited actions; tools/data allowed; communication channels; quality checks; failure modes; escalation owner; evaluation measures; and retirement criteria. Add or split a role only when its boundary reduces meaningful risk or complexity.
