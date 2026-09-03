# Recommended Timeline & Submission Checklist

A recommended schedule for this 9-day project. **Part A (build) runs
Days 1–6; Part B (audit what you built) runs Days 7–9** — the natural
order, since Part B's whole premise is auditing something that already
exists.

## Day 1 — Setup + pick your real problem + read the given audit artifacts

- [ ] `pip install pandas scikit-learn fairlearn google-genai`; open
  `LICENSE`, replace `[YOUR NAME]`, commit.
- [ ] Set up a free-tier LLM API key (`starter/llm_api_setup.md`).
- [ ] Define your own real data problem for Part A (section 1) — needs
  both a lookup and a computation to answer.
  - ⚠️ Solving a templated version of this module's own example instead
    of a genuinely self-defined problem is a real, common mistake — pick
    something specific to your own domain.
- [ ] Read `given_data/README.md` and `owasp_llm_top10_checklist.md` —
  you'll need these for Part B, and reading them now means Part A's
  human-in-the-loop checkpoint design (Day 5) can already keep them in
  mind.

**Exit criterion**: your Part A problem statement needs both retrieval
and a data computation — if it only needs one, pick a different
question — and you can explain what the given classifier predicts.

## Day 2 — Prompt engineering

- [ ] Write a naive prompt, then a revised one (role/context/task/format,
  section 2), with a real, specific explanation of the improvement.

**Exit criterion**: your explanation names something specific the naive
version would have gotten wrong.

## Day 3 — Retrieval (RAG)

- [ ] Chunk `data/SOURCE.md` (the real per-domain data-documentation
  doc — dataset sources, schemas, and real data quirks), justify your
  chunking strategy against its actual structure.
- [ ] Build a real TF-IDF retriever (TF-IDF = Term Frequency-Inverse
  Document Frequency — scores each word in a chunk by how often it
  appears there vs. across all chunks, so common words score low and
  distinctive ones score high); test against 5 real queries (section 3).

**Exit criterion**: a real relevance discussion — how many of your 5
queries retrieved correctly, and why any misses happened. (This is a
compressed, 1-day version of what took 2 days as a standalone module —
budget your time; if retrieval quality is genuinely struggling, a
simpler chunking strategy that you can fully justify beats a more
ambitious one you can't.)

## Day 4 — Data task + chain it

- [ ] A real computation against your own domain's actual CSV data
  (section 4), informed by what retrieval found.
- [ ] Chain retrieval → data task → LLM synthesis, called
  **programmatically** (section 5).
  - ⚠️ Calling a single prompt with no real chaining an "agentic
    workflow" is the #1 mistake on record — make sure each step's
    output genuinely feeds the next.

**Exit criterion**: a real number, computed from real code (not a
placeholder), and it's genuinely what your LLM synthesis step consumes.

## Day 5 — Human-in-the-loop checkpoint + catch two AI errors

- [ ] Design and implement a real, specific human-in-the-loop
  checkpoint (section 6) — build this as a real design constraint, not
  bolted on after the fact.
  - ⚠️ A decorative checkpoint that wouldn't actually catch a realistic
    error is the #2 mistake on record.
- [ ] `starter/ai_error_catch_1.md` (code) and
  `starter/ai_error_catch_2.md` (written summary) — the specific error
  and fix for each (section 7).

**Exit criterion**: you can name exactly what your checkpoint would
catch, concretely — not "AI could be wrong" — and your fix for exercise
2 addresses more than one real issue in the given text.

## Day 6 — Adaptability log + autonomy documentation

- [ ] One specific initial approach that didn't work, and the specific
  change made (section 8).
- [ ] What the workflow does autonomously vs. what needs sign-off
  (section 9), matching your section 6 checkpoint exactly.
  - ⚠️ Not documenting which parts are autonomous vs. sign-off-required
    is the #4 mistake on record.

**Exit criterion**: your adaptability log names a real failure, not "I
iterated a few times." Part A is done — commit and move to Part B.

## Day 7 — Bias/fairness audit + human/AI decision recommendation

- [ ] A real Fairlearn `MetricFrame` against
  `given_data/model_predictions.csv`, grouped by `rated_flood_zone`
  (`bias_audit.py` sections 1-2).
  - ⚠️ Reporting "no bias found" without ever running a real disparity
    computation is a real, common mistake.
- [ ] Diagnose a plausible root cause and propose a specific fix
  (sections 3-4).
- [ ] Complete `human_ai_decision_recommendation.md` — apply the
  stakes/reversibility framework to the given scenario, informed by
  your real fairness-audit finding.

**Exit criterion**: a real, computed disparity number (even if small),
a specific — not generic — proposed fix, and a specific real threshold
or a specific "never" call in your decision recommendation — not "with
appropriate oversight." (This compresses what took 3 days as a
standalone module into 1 — the audit itself is a single, focused
computation once the given data is already in hand.)

## Day 8 — Facilitated discussion + security evaluation

- [ ] In-class group discussion (see your instructor for timing).
- [ ] Fill in `facilitation_outcome.md` immediately after — a real,
  specific record while it's fresh.
- [ ] Evaluate `given_data/agentic_workflow_description.md` against
  `owasp_llm_top10_checklist.md` — at least 2 real, specific exposure
  risks tied to the workflow's actual structure.
  - ⚠️ Applying the checklist generically instead of to the actual
    workflow is a real, common mistake.

**Exit criterion**: your own specific contribution to reaching the
group's decision is named, not just the group's final answer — and each
named security risk traces to a specific step in the given workflow,
not a generic AI-risk statement.

## Day 9 — Policy memo + final polish + submit

- [ ] Complete `policy_memo.md` in full, integrating your real audit,
  security evaluation, decision recommendation, and facilitation
  outcome into one recommendation. All required, not just the audit
  findings themselves:
  - [ ] A specific, named governance framework (not "best practices").
  - [ ] A specific, named stakeholder who could be harmed — not vague
    "customers could be harmed" language.
  - [ ] PII-tier handling guidance — which of Module 10's own
    sensitivity tiers are safe vs. unsafe to expose to this AI system.
  - ⚠️ A memo with no named framework or concrete recommendation is a
    real, common mistake.
- [ ] Re-read all Part A sections and all 4 Part B files against
  `required_components.md`; no placeholder `# TODO` text left.
- [ ] **Delete `PROJECT_OVERVIEW.md`** — it explains the assignment, not
  your project; a real portfolio repo shouldn't have "here's what you
  were asked to build" sitting in it.
- [ ] **Replace `README.md`'s content with your own real project README**
  — write it for someone who's never seen this assignment:
  - **Business Problem** — the real, self-defined question you answered
    in Part A, and what the audited model/workflow in Part B is for.
  - **Workflow Design** — your retrieval → data task → synthesis chain,
    and your human-in-the-loop checkpoint.
  - **AI Integration/Validation** — the two real AI errors you caught,
    and your adaptability log.
  - **Audit Findings** — the real disparity, root cause, and security
    risks you found.
  - **Recommendations** — your policy memo's real final call.
- [ ] Final commit, repo check.

## Day 10 — Share-out

Your instructor schedules this once every submission is in — usually a
few days after Day 9, not necessarily the next calendar day. Real
session, not optional: a ~90-minute pairs/trios session covering both
parts of this project — a partner adversarially stress-tests your Part
A human-in-the-loop checkpoint, then checks whether your Part B policy
memo's recommendation actually follows from your audit and security
findings, you trade one real story (an adaptability pivot or a
root-cause diagnosis) with another pair, and close with a group
reflection. Bring your checkpoint code, adaptability log, and finished
`policy_memo.md`/`bias_audit.py` — see your instructor for the exact
date.

---

## Above & Beyond (delta only — see `ABOVE_AND_BEYOND.md` for full detail)

- [ ] Extend your knowledge base with a second real document.
- [ ] Add a 3rd (or more) chained step.
- [ ] A real MCP case-study reflection comparing this project's direct
  tool-calling to what MCP would change.
- [ ] Compute a second Fairlearn metric and discuss what it captures
  differently.
- [ ] Evaluate against a second governance framework and compare.
- [ ] Propose and (if feasible) demonstrate a real fairness mitigation.
