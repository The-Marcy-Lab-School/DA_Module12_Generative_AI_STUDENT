# Project Overview: Generative & Responsible AI — Prompt Engineering, Agentic Tooling & AI Governance

## The objective

**Part A — Build.** Design and build a small agentic workflow: a
well-engineered prompt, a real retrieval step over a real knowledge
base, and a real data computation — chained together programmatically,
with a human checking the output before it's used for anything real.
Along the way, catch two real AI mistakes and document one place your
own first approach didn't work.

**Part B — Audit.** Now that something's built, ask the question that
comes right after: should it be trusted, and under what conditions?
Audit a real, already-built model for bias, evaluate a real AI
workflow's security exposure against an industry-standard checklist,
work through a real human-owned-vs-AI-assisted decision with your
group, and write a policy memo that turns all of it into one concrete
recommendation.

## Why this matters

Every earlier project in this program used AI as a coding assistant.
This one is different in two ways. First: you're building *with* AI as
a real, working part of your pipeline — not asking it questions in a
chat window, but calling it from code, feeding it retrieved context,
and deciding exactly where a human needs to step in before its output
is trusted. Second: once something is built, it asks whether it should
be trusted. A model that predicts well but was never checked for
disparate impact, or an AI workflow that was never evaluated for real
security exposure, is exactly how responsible-AI failures actually
happen in practice — not from malice, but from skipping the check.
Knowing what an AI agent can safely do alone, and knowing how to check
whether it should be trusted at all, are the two professional skills
this project tests together.

## What you'll build on

- `ai-assisted-coding`, from Module 4 — reviewing AI-suggested code,
  now brought to full independence (no partner this time).
- Your own domain data, from every project since Module 3.
- Claude.ai, already used since Module 4 — now paired with a real,
  programmatic API instead of only the chat interface.
- **A given, already-trained classifier's real predictions**
  (`starter/given_data/model_predictions.csv`) — the same one every
  student audits, in the same shape a real classifier's output takes.
  You're auditing its actual predictions, not building a new model.
- **A given, real agentic workflow description**
  (`starter/given_data/agentic_workflow_description.md`) — the same
  one every student evaluates for security exposure, structured the
  same way the workflow you build in Part A is.
- Module 10's own real PII sensitivity-tier system — reused directly
  for the policy memo's data-handling guidance.

## What this unlocks

`agentic-ai` and `data-governance` are both explicit prerequisites for
the capstone (Module 13). This project is your first real practice
building something that chains AI calls together, and your last
rehearsal of governance reasoning before both are assumed knowledge
going into your final program.

## Skills you'll practice

**Part A:**
- **Generative AI / LLMs** — how the model actually generates a
  response, and what that means for trusting it.
- **Prompt Engineering** — role/context/task/format, and proving a
  revision actually improves output.
- **Context Engineering** — real retrieval-design tradeoffs.
- **Agentic AI** — a real, chained, multi-step workflow.
- **AI Tool Orchestration** — calling tools/functions programmatically.
- **Working with AI Agents** — documenting autonomy boundaries.
- **RAG** — retrieval-augmented generation, for real, over a real
  knowledge base.
- **AI Output Validation** — catching real AI mistakes, twice,
  independently.
- **AI-Assisted Coding** — reviewing AI-suggested code unassisted.
- **Adaptability** — a real, documented pivot.
- **Creativity** — a genuinely self-defined problem.

**Part B:**
- **AI Governance** — comparing real framework expectations across
  regulated and non-regulated domains.
- **Responsible AI: Bias & Fairness** — a real, computed group-disparity
  audit.
- **AI Security Governance** — a real checklist-based exposure
  evaluation.
- **Data Ethics** — naming a specific stakeholder who could be harmed.
- **Decision Intelligence** — a real stakes/reversibility-justified
  recommendation.
- **Human-Durable Skills & Leadership** — facilitating a peer group to
  an actual decision.
- **AI Literacy** — explaining a governance recommendation to a
  non-technical stakeholder.
- **Data Governance & PII Classification** — reusing Module 10's real
  tier system for a new, AI-specific question.
- **Problem Solving** — a specific, technically plausible fix for a
  detected disparity.

## Timeline

9 days, plus a required share-out session scheduled after. See
`CHECKLIST_TIMELINE.md` for the day-by-day pacing and the full
submission checklist.

## Deliverables at a glance

Part A: one file, `starter/agentic_workflow.py`, run cell-by-cell in
VS Code's Jupyter extension, covering all 9 required components. Part
B: `starter/bias_audit.py` (the code), and three written components
(`human_ai_decision_recommendation.md`, `facilitation_outcome.md`,
`policy_memo.md`). See `required_components.md` for the full breakdown
and `CHECKLIST_TIMELINE.md` for pacing.
