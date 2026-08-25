# Recommended Timeline & Submission Checklist

A recommended schedule for this 9-day project.

## Day 1 — Setup + pick your real problem

- [ ] `pip install scikit-learn pandas google-genai`; open `LICENSE`,
  replace `[YOUR NAME]`, commit.
- [ ] Set up a free-tier LLM API key (`starter/llm_api_setup.md`).
- [ ] Define your own real data problem (section 1) — needs both a
  lookup and a computation to answer.
  - ⚠️ Solving a templated version of this module's own example instead
    of a genuinely self-defined problem is a real, common mistake — pick
    something specific to your own domain.

**Exit criterion**: your problem statement needs both retrieval and a
data computation — if it only needs one, pick a different question.

## Day 2 — Prompt engineering

- [ ] Write a naive prompt, then a revised one (role/context/task/format,
  section 2), with a real, specific explanation of the improvement.

**Exit criterion**: your explanation names something specific the naive
version would have gotten wrong.

## Days 3-4 — Retrieval (RAG)

- [ ] Chunk `SOURCE.md`, justify your chunking strategy against its
  actual structure.
- [ ] Build a real TF-IDF retriever; test against 5 real queries
  (section 3).

**Exit criterion**: a real relevance discussion — how many of your 5
queries retrieved correctly, and why any misses happened.

## Day 5 — Data task

- [ ] A real computation against your own domain's actual CSV data
  (section 4), informed by what retrieval found.

**Exit criterion**: a real number, computed from real code, not a
placeholder.

## Day 6 — Chain it + human-in-the-loop checkpoint

- [ ] Chain retrieval → data task → LLM synthesis, called
  **programmatically** (section 5).
  - ⚠️ Calling a single prompt with no real chaining an "agentic
    workflow" is the #1 mistake on record — make sure each step's
    output genuinely feeds the next.
- [ ] Design and implement a real, specific human-in-the-loop
  checkpoint (section 6) — build this as a real design constraint, not
  bolted on after the fact.
  - ⚠️ A decorative checkpoint that wouldn't actually catch a realistic
    error is the #2 mistake on record.

**Exit criterion**: you can name exactly what your checkpoint would
catch, concretely — not "AI could be wrong."

## Day 7 — Catch two AI errors

- [ ] `starter/ai_error_catch_1.md` (code) and
  `starter/ai_error_catch_2.md` (written summary) — the specific error
  and fix for each (section 7).

**Exit criterion**: your fix for exercise 2 addresses more than one
real issue in the given text.

## Day 8 — Adaptability log + autonomy documentation

- [ ] One specific initial approach that didn't work, and the specific
  change made (section 8).
- [ ] What the workflow does autonomously vs. what needs sign-off
  (section 9), matching your section 6 checkpoint exactly.
  - ⚠️ Not documenting which parts are autonomous vs. sign-off-required
    is the #4 mistake on record.

**Exit criterion**: your adaptability log names a real failure, not "I
iterated a few times."

## Day 9 — Final polish + submit

- [ ] Re-read all 9 sections against `required_components.md`; no
  placeholder `# TODO` text left.
- [ ] Final commit, repo check.

**Heads up**: after this project is due, there's a peer share-out
session on your actual workflow — details in class.

---

## Above & Beyond (delta only — see `ABOVE_AND_BEYOND.md` for full detail)

- [ ] Extend your knowledge base with a second real document.
- [ ] Add a 3rd (or more) chained step.
- [ ] A real MCP case-study reflection comparing this project's direct
  tool-calling to what MCP would change.
