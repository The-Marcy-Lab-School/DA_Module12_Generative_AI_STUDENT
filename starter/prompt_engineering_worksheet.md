# Prompt Engineering: Role, Context, Task, Format

A structured way to go from a naive prompt to a genuinely better one.
Use this structure in `agentic_workflow.py` section 2 — this file is
the reference, not something you submit separately.

## The four parts

- **Role**: who should the AI act as? ("a data analyst reviewing
  insurance claims," not just "an assistant")
- **Context**: what does it actually need to know to answer well? (the
  real, specific facts about your data/question — not generic
  background)
- **Task**: the precise action, stated unambiguously (not "tell me
  about X" — "identify the three claims with the largest payment
  discrepancy and explain why each is unusual")
- **Format**: exactly how the output should be structured (a table? a
  numbered list? a specific length?)

## A worked example (not your domain — don't copy this, use it as a pattern)

**Naive prompt**: "Summarize this sales data."

**Revised prompt**:
> **Role**: You are a retail analyst preparing a weekly briefing for a
> regional manager who has 2 minutes to read it.
> **Context**: Here is last week's sales data by store location [data
> would go here]. The manager cares most about stores that
> underperformed relative to their own historical average, not just
> raw totals.
> **Task**: Identify the 3 stores with the largest negative deviation
> from their own 8-week rolling average, and name one plausible
> explanation for each.
> **Format**: A 3-bullet list, one store per bullet, each under 25
> words.

**Why this is better**: the naive version would produce a generic
paragraph the manager has to re-read to extract anything actionable.
The revised version, by specifying role + a real constraint (2
minutes), a real comparison basis (rolling average, not raw totals, per
context), a real task (deviation + explanation, not just "summarize"),
and a real format (3 short bullets), gets an answer the manager can
actually use without further editing.

## Do this for your own real task

Your `agentic_workflow.py` section 2 should follow this same structure
— naive prompt first, then a revised version using all four parts,
specific to your own real data problem (section 1), with your own real
explanation of why the revision is better.
