# Initial Risk Register

| Risk | Likelihood | Impact | Early signal | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
| Fluent but false educational content | Medium | Critical | Weak citations, evaluator disagreement, learner corrections | Source anchors, domain review, factual gate, uncertainty disclosures | Domain review owner |
| Superficial interactivity | High | High | Controls do not change a mental model or assessment result | Interaction specification and educational evaluation | Experience owner |
| Accessibility treated as late polish | High | Critical | Missing equivalent paths or inaccessible representations | Accessibility planning/review gate from design stage | Accessibility owner |
| Copyright/rights misuse | Medium | Critical | Unknown origin or transformation terms | Source authorization and restricted-content process | Source Steward |
| Prompt/model overfitting | High | High | Gains vanish outside a favorite example set | Frozen benchmarks, holdouts, model comparisons | Evaluation owner |
| Memory becomes stale or wrong | Medium | High | Repeated overrides or conflicting guidance | Confidence, expiry, review, retrieval audits | Memory Manager |
| Multi-agent coordination overhead | High | Medium | Duplicate work, handoff rejections, unclear authority | Narrow roles, handoff protocol, coordination metrics | Orchestrator |
| Irreversible early technology choice | Medium | High | Architecture inferred from a prototype | Technology-neutral contracts, ADR gate, reversibility analysis | Architecture owner |
| Sensitive learner data misuse | Medium | Critical | Unnecessary tracking or unclear consent | Data minimization, classification, approval before collection | Human owner |
| Evaluation theater | Medium | High | Scores lack evidence/calibration or never block release | Rubric evidence, calibration, independent review | Evaluation owner |
| Cost/latency escalation | High | Medium | Iteration loops with no score movement | Budgets, plateau stop rule, benchmark efficiency metrics | Operations owner |
| Scope collapse into a generic content generator | Medium | High | Missing learner outcomes or quality gates | Charter, product boundaries, release criteria | Product owner |

Review this register at least quarterly and after every material incident. Likelihood and impact are preliminary and must be recalibrated with evidence.
