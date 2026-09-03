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

## 3. Install the libraries

```
pip install pandas scikit-learn fairlearn google-genai
```

`scikit-learn` is for Part A's real TF-IDF (Term Frequency-Inverse
Document Frequency) retrieval — a real, lightweight way to do retrieval
without needing a paid embedding API. `fairlearn` is new for Part B — a
real, standard, open-source group-fairness metrics library.

## 4. Set up a free-tier LLM API (for Part A)

Read `starter/llm_api_setup.md` — Gemini's free tier is recommended
(no credit card required).

## 5. Pick your own real data problem (for Part A)

Before opening the starter file: what real question, about your own
domain, needs both a lookup (retrieval) and a computation (a data
task)? Write this down — section 1 of `agentic_workflow.py` asks for it
first.

## 6. Open `starter/agentic_workflow.py` in VS Code (Part A)

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

## 7. Read the given artifacts before opening `bias_audit.py` (Part B)

Once Part A is built (Days 1–6), read `given_data/README.md` (what the
model is), `given_data/agentic_workflow_description.md` (what workflow
you're security-evaluating), and `owasp_llm_top10_checklist.md` (the
reference checklist). Part B audits and evaluates real, already-built
things — understand them before starting.

⚠️ **Common mistake**: reporting "no bias found" without ever running a
real disparity computation. Even a small, real disparity is worth
reporting honestly — don't round a real number down to "basically
fair."

⚠️ **Common mistake**: applying the OWASP checklist as a generic list
rather than to the actual given workflow's real structure. Every risk
you name should trace to a specific step in
`given_data/agentic_workflow_description.md`.

## 8. Do the in-class facilitated discussion before filling in `facilitation_outcome.md`

`facilitation_outcome.md` needs a real, specific record of an actual
discussion — don't fill it in before the session happens.

## 9. Commit incrementally

Commit as you finish each numbered section or component — a real
commit history is worth more than one final dump, and Part A's own
adaptability log (section 8) needs a real "what I tried first, what I
changed" story, which is much easier to reconstruct honestly from real
commits than from memory at the end.

Next: `CHECKLIST_TIMELINE.md` for pacing and the full submission
checklist.
