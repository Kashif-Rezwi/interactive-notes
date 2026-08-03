# Repository Map

## Directory taxonomy

```text
Learning OS/
├── README.md                         # Repository entry point and contract
├── AGENTS.md                         # Universal operating instructions for AI agents
├── CONTRIBUTING.md                   # Contribution and review expectations
├── content/                          # Course and module packages, navigated through README indexes
│   ├── README.md                     # Catalog and package navigation rules
│   └── <course-slug>/                # One course or subject area
│       ├── README.md                 # Course-level module index
│       └── <module-slug>/            # Leaf learning-material package
│           ├── README.md             # Links to every source and generated artifact
│           ├── sources/              # Preserved notebooks, documents, and other inputs
│           └── generated/            # Generated learning artifacts; no nested artifact directories
├── docs/                             # Authoritative, versioned architecture and governance
│   ├── 00-foundation/                # Vision, invariants, principles, controlled vocabulary
│   ├── 01-product/                   # Future product intent and learner-experience criteria
│   ├── 02-system/                    # Conceptual architecture, boundaries, and contracts
│   ├── 03-workflows/                 # Lifecycle, quality loop, states, retries, handoffs
│   ├── 04-agents/                    # Roles, boundaries, protocol, and success criteria
│   ├── 05-prompts/                   # Prompt taxonomy, lifecycle, versioning, review
│   ├── 06-evaluation/                # Rubrics, calibration, benchmark and release gates
│   ├── 07-memory/                    # Long-term learning, curation, retrieval, retention
│   ├── 08-observability/             # Logging, lineage, privacy, incident learning
│   ├── 09-operations/                # Repeatable playbooks and operating cadence
│   ├── 10-governance/                # Documentation, naming, versioning, review, releases
│   ├── 11-roadmap/                   # Stages, risks, open questions, implementation gates
│   └── adr/                          # Immutable architecture decision records and index
├── templates/                        # Reusable human-readable record templates; no runtime templates
│   ├── adr/                          # Decision record starter
│   ├── documentation/                # Architecture and policy document starter
│   ├── source/                       # Source-package manifest starter
│   ├── concept/                      # Concept-model starter
│   ├── learning/                     # Learning-plan starter
│   ├── agent/                        # Role-card starter
│   ├── prompt/                       # Versioned prompt-card starter
│   ├── run/                          # Generation-run record starter
│   ├── evaluation/                   # Evaluation report starter
│   ├── memory/                       # Curated lesson starter
│   ├── experiment/                   # Experiment plan and result starter
│   ├── playbook/                     # Operational playbook starter
│   ├── lesson/                       # Learner-artifact specification starter
│   └── examples/                      # Simulated template walkthroughs; never evidence
├── records/                          # Append-only evidence; populated only by governed work
│   ├── runs/                         # Immutable run manifests and reflection links
│   ├── sources/                      # Source-package manifests and rights decisions
│   ├── evaluations/                  # Scorecards, reviewer evidence, adjudications
│   ├── experiments/                  # Hypotheses, comparisons, findings, invalidations
│   ├── memory/                       # Approved, superseded, and retired learning records
│   ├── benchmarks/                   # Frozen benchmark definitions and results
│   └── decisions/                    # Optional decision register/export; ADRs remain canonical
└── library/                          # Curated, reusable reference knowledge
    ├── prompts/                      # Approved prompt-card registry; experimental cards stay in records
    ├── rubrics/                      # Approved reusable rubrics and calibration guidance
    ├── patterns/                     # Pedagogy, interaction, visualization, accessibility patterns
    └── references/                   # Rights-aware source references and research summaries
```

## Ownership and rules

| Area | Source of truth | Change rule |
| --- | --- | --- |
| `docs/00–11` | Version-controlled architecture | Review against documentation standard |
| `docs/adr` | Architecture decisions | Never rewrite accepted history; supersede |
| `templates` | Record structure | Change with an ADR if traceability semantics change |
| `records` | Evidence | Append only; correct by linked supersession |
| `library` | Curated reusable knowledge | Cite origin, scope, rights, and confidence |
| `content` | Learning material and package-level navigation | Preserve source files; index all material through the closest README; follow the content-package convention |

Numbered documentation directories express reading order, not status or implementation dependency. Do not create a new top-level category without showing why an existing category cannot own the material.
