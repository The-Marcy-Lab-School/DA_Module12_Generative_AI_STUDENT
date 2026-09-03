# Module 12: Generative & Responsible AI — Prompt Engineering, Agentic Tooling & AI Governance

A real agentic workflow — prompt engineering, retrieval, a data task,
and a human-in-the-loop checkpoint, chained together programmatically —
followed by a real audit of whether an AI system like it should be
trusted: a bias/fairness audit, a security evaluation, a human-vs-AI
decision, and a policy memo tying it all together.

**Due:** 9 days, plus a required share-out session scheduled after. See
`CHECKLIST_TIMELINE.md` for the day-by-day pacing and the full
submission checklist.

**Before you do anything else**: click **"Use this template"** on this
repo's GitHub page (not "Fork") to create your own copy — see
`GETTING_STARTED.md` step 1 for why this matters.

- **What/why**: see `PROJECT_OVERVIEW.md`.
- **Setup, step by step**: see `GETTING_STARTED.md`.
- **Pacing + full submission checklist**: see `CHECKLIST_TIMELINE.md`.
- **Exactly what to build**: see `required_components.md`.

## Knowledge base and given artifacts

Part A's retrieval step uses `data/SOURCE.md` (in this repo) — the same
file describing every domain's real schema, license, and caveats that
you've already used since Module 3. `data/<domain>/` also has the real
CSVs for your data task step.

Part B audits, rather than builds, new things:

- `starter/given_data/model_predictions.csv` — a real, provided
  classifier's real predictions (see `given_data/README.md`).
- `starter/given_data/agentic_workflow_description.md` — a real,
  already-built AI workflow's structure, for the security evaluation.
- `starter/owasp_llm_top10_checklist.md` — the real reference checklist.

## Setup

```
pip install pandas scikit-learn fairlearn google-genai
```

See `starter/llm_api_setup.md` for real, free LLM API access (no
credit card required).
