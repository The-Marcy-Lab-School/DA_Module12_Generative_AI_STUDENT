# MVP: Minimum Bar

See `instructor` materials distributed separately for full grading
detail. This is a short, scannable bar — one line per requirement.

## Part A — Agentic Workflow

- [ ] A genuinely self-defined data problem, not a restatement of the
  module's own example.
- [ ] A naive prompt and a revised (role/context/task/format) prompt,
  with a real, specific explanation of the improvement.
- [ ] A real retrieval step over `SOURCE.md`, chunking justified, tested
  against ≥5 real queries.
- [ ] A real data-task computation against your own domain's actual CSV
  data.
- [ ] A real chained workflow (retrieval → data task → LLM synthesis)
  called programmatically — no manual copy-paste between steps.
- [ ] A real, specific human-in-the-loop checkpoint — documented
  exactly what it would catch.
- [ ] Both planted AI errors caught, with a specific fix documented for
  each.
- [ ] A real adaptability log: a specific initial approach that failed,
  and the specific change made.
- [ ] Clear documentation of what the workflow does autonomously vs.
  what requires human sign-off.

## Part B — Responsible AI Evaluation

- [ ] A real, computed Fairlearn group-disparity metric against the
  given model's predictions.
- [ ] A plausible, specific diagnosed root cause and a specific
  (not generic) proposed fix.
- [ ] A completed `human_ai_decision_recommendation.md`, with a
  specific real threshold or "never" call, informed by your fairness
  finding.
- [ ] A real, specific `facilitation_outcome.md`, filled in after an
  actual group discussion.
- [ ] At least 2 real, specific OWASP-checklist exposure risks tied to
  the given workflow's actual structure.
- [ ] A policy memo naming a specific governance framework, a named
  stakeholder who could be harmed, correct PII-tier handling guidance,
  and a specific final recommendation.
