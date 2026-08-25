# Project Overview: Generative AI, Prompt Engineering & Agentic AI Tooling

## The objective

Design and build a small agentic workflow: a well-engineered prompt, a
real retrieval step over a real knowledge base, and a real data
computation — chained together programmatically, with a human checking
the output before it's used for anything real. Along the way, catch two
real AI mistakes and document one place your own first approach didn't
work.

## Why this matters

Every earlier project in this program used AI as a coding assistant.
This one is different: you're building *with* AI as a real, working
part of your pipeline — not asking it questions in a chat window, but
calling it from code, feeding it retrieved context, and deciding
exactly where a human needs to step in before its output is trusted.
That distinction — knowing what an AI agent can safely do alone versus
what needs your sign-off — is the actual, professional skill this
project is testing.

## What you'll build on

- `ai-assisted-coding`, from Module 4 — reviewing AI-suggested code,
  now brought to full independence (no partner this time).
- Your own domain data, from every project since Module 3.
- Claude.ai, already used since Module 4 — now paired with a real,
  programmatic API instead of only the chat interface.

## What this unlocks

`agentic-ai` is an explicit prerequisite for the capstone (Module 15).
This project is your first real practice building something that
chains AI calls together — the capstone assumes you already know how.

## Skills you'll practice

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

## Deliverables at a glance

One file, `starter/agentic_workflow.py`, run cell-by-cell in VS Code's
Jupyter extension, covering all 9 required components. See
`required_components.md` for the full breakdown and
`CHECKLIST_TIMELINE.md` for pacing.
