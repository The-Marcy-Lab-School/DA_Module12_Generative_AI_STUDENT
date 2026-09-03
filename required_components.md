# Required Components

Two parts. Part A lives in `starter/agentic_workflow.py` (9 numbered
sections); Part B is 4 separate files. Read
`starter/prompt_engineering_worksheet.md`, `starter/llm_api_setup.md`,
and both `starter/ai_error_catch_*.md` files before starting Part A;
read `starter/given_data/README.md`,
`starter/given_data/agentic_workflow_description.md`, and
`starter/owasp_llm_top10_checklist.md` before starting Part B.

## Part A — Agentic Workflow (`starter/agentic_workflow.py`)

### 1. Your own real data problem

A genuine, self-defined question — not a restatement of the module's
own example (`common_project_mistakes` #3). Needs both a real lookup
(retrieval) and a real computation (data task) to answer.

### 2. Prompt engineering

A naive prompt and a revised one (role/context/task/format), with a
real, specific explanation of why the revision is better.

### 3. Retrieval (RAG)

A real chunking strategy over `data/SOURCE.md` (the real per-domain data
documentation you've used since earlier modules — dataset sources,
schemas, and real data quirks, one section per domain), justified
against its actual structure. Tested against at least 5 real queries,
with a real discussion of how many retrieved correctly and why any
misses happened.

### 4. Data task

A real computation against your own domain's actual CSV data.

### 5. Chained workflow

Retrieval → data task → LLM synthesis, called **programmatically** —
not manually copying output between separate chat sessions
(`common_project_mistakes` #1's opposite: this must genuinely chain).

### 6. Human-in-the-loop checkpoint

A real, specific, implemented checkpoint — not a decorative "approve?"
prompt (`common_project_mistakes` #2). State exactly what it would
catch.

### 7. Two caught AI errors

`starter/ai_error_catch_1.md` (code) and `starter/ai_error_catch_2.md`
(written summary) — the specific error and specific fix for each.

### 8. Adaptability log

One specific initial approach that didn't work, and the specific change
made in response.

### 9. Autonomy documentation

What the workflow does autonomously vs. what requires human sign-off
(`common_project_mistakes` #4) — matching your section 6 checkpoint.

## Part B — Responsible AI Evaluation (4 files, each covering real, distinct graded ground)

### `starter/bias_audit.py` (code artifact)

A real Fairlearn group-fairness audit against
`given_data/model_predictions.csv` (sections 1-4): the metric, the
disparity, a diagnosed root cause, a specific proposed fix.

### `starter/human_ai_decision_recommendation.md`

The stakes/reversibility framework applied to the given scenario, plus
how your fairness-audit finding changes your recommendation.

### `starter/facilitation_outcome.md`

Filled in **after** your in-class facilitated group discussion — a
specific record of the decision your group reached and how you guided
it there.

### `starter/policy_memo.md` (written memo)

Integrates everything above into one business-framed recommendation: a
named governance framework, your fairness-audit summary, your security
evaluation of the given agentic workflow
(`given_data/agentic_workflow_description.md`, against
`owasp_llm_top10_checklist.md`), a named stakeholder who could be
harmed, your human/AI decision recommendation, PII-tier handling
guidance, and a final concrete recommendation.

---

**Common mistakes this project watches for** (see `instructor/rubric.md`
for the full grading detail):

- Calling a single prompt with no chaining an "agentic workflow."
- A human-in-the-loop checkpoint that's decorative and wouldn't catch a
  realistic error.
- Solving a templated version of the module's own example instead of a
  genuinely self-defined problem.
- Not documenting which parts of the workflow the agent can do
  autonomously versus what needs sign-off.
- Reporting "no bias found" without ever running a real disparity
  computation.
- Applying the OWASP LLM checklist generically instead of to the actual
  evaluated workflow.
- A policy memo with no named framework or concrete recommendation.
- Writing the ethical-implications section in vague terms instead of
  naming a specific stakeholder who could be harmed.
