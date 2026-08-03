# Benchmark Strategy

## Purpose

Benchmarks distinguish measurable improvement from anecdotal preference. They assess prompts, models, agents, plans, and quality-loop changes against stable, rights-cleared cases.

## Benchmark suite composition

Maintain a balanced, versioned corpus across:

- source types: notebook, paper, PDF, slides, Markdown, documentation, and technical blog;
- subject complexity: foundational, intermediate, advanced, and cross-disciplinary;
- learning tasks: explanation, visualization, interaction, quiz, revision, and concept mapping;
- risk: ambiguous sources, mathematical detail, accessibility constraints, rights limitations, and adversarial/contradictory content;
- audiences: novice, transition learner, and advanced practitioner.

Each case contains an authorized source package, intended learner/outcome, immutable case version, expected evidence anchors, known traps, required evaluation dimensions, and allowed disclosure level. Benchmarks may include reference artifacts but must never leak them into a tested prompt.

## Protocol

1. Freeze the benchmark version and success hypothesis before testing.
2. Pin prompt bundle, model identity/configuration, workflow version, and evaluation rubric.
3. Run the candidate and baseline under comparable budgets.
4. Blind or mask evaluators to the treatment where practical.
5. Report per-case scores, aggregate distribution, cost/latency, failures, variance, and qualitative findings.
6. Promote only if critical gates do not regress and improvement meets the declared practical threshold.

## Governance

Benchmark changes are high-impact: preserve old versions, publish a change rationale, re-establish calibration, and avoid optimizing against a public test set. Separate development, validation, and holdout sets. Human reviewers approve additions involving high-stakes domains or sensitive materials.
