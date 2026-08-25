# Getting Started

## 1. Use this template — not Fork

Click **"Use this template"** on GitHub (not "Fork") for a clean,
independent copy for your own portfolio.

## 2. Environment is already set up

`.gitignore` and `LICENSE` are already here. Two real things to still
do:

- **Open `LICENSE`** and replace `[YOUR NAME]` with your own name, then
  commit.
- Confirm `.env` (if you create one for your API key) is covered by
  `.gitignore` — it already is, but double-check before your first
  commit that you never accidentally stage it.

## 3. Install the new libraries

```
pip install scikit-learn pandas google-genai
```

`scikit-learn` here is for real TF-IDF retrieval (not modeling, like
Module 12) — a real, lightweight way to do retrieval without needing a
paid embedding API.

## 4. Set up a free-tier LLM API

Read `starter/llm_api_setup.md` — Gemini's free tier is recommended
(no credit card required).

## 5. Pick your own real data problem

Before opening the starter file: what real question, about your own
domain, needs both a lookup (retrieval) and a computation (a data
task)? Write this down — section 1 of the starter file asks for it
first.

## 6. Open `starter/agentic_workflow.py` in VS Code

Each `# %%` marks a separate cell — run cells one at a time.

⚠️ **Common mistake**: building "an agentic workflow" that's really
just one prompt with no real chaining. Your retrieval step's output
needs to genuinely feed into your data task or your LLM call
programmatically — not just exist as a separate, disconnected cell.

⚠️ **Common mistake**: a human-in-the-loop checkpoint that's decorative
— a print statement saying "please review" with nothing that would
actually change based on what a human found. Build the checkpoint
*first* (per this project's own exemplar guidance), before writing the
rest of the workflow, so it's a real constraint, not an afterthought.

## 7. Commit incrementally

Commit as you finish each numbered section — a real commit history is
worth more than one final dump, and this project's own adaptability log
(section 8) needs a real "what I tried first, what I changed" story,
which is much easier to reconstruct honestly from real commits than
from memory at the end.

Next: `CHECKLIST_TIMELINE.md` for pacing and the full submission
checklist.
