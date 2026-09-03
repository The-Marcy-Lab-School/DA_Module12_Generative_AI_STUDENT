# Given AI Workflow: A Real Agentic Pipeline to Security-Evaluate

This is the real workflow structure built in Part A of this project —
you're evaluating its security exposure, not rebuilding or re-running
it. It's deliberately the same fixed, given description every student
evaluates (not literally pulled from your own submission), so the
security-exposure findings this exercise grades are comparable across
students.

## The workflow, step by step

1. **Retrieval step**: a real TF-IDF retriever searches a small
   knowledge base (`SOURCE.md`, real per-domain data documentation —
   schemas, licenses, real caveats) for context relevant to a user's
   natural-language query, returning the highest-scoring chunk.
2. **Data task step**: a real pandas computation runs against a
   domain's actual CSV data (e.g., computing a real fraction/statistic),
   informed by what the query and retrieval step found.
3. **LLM synthesis step**: the retrieved context and the data task's
   real result are inserted into a prompt template, which is sent to a
   real LLM API (Gemini, Anthropic, or OpenAI, depending on the
   student's own setup) to produce a written response.
4. **Human-in-the-loop checkpoint**: before the LLM's response is used
   for anything real, an automated check verifies a required
   disclosure is present (e.g., a data-provenance caveat), and a human
   is expected to read the response before acting on it.

## What you need to evaluate

Using the OWASP LLM Top 10 checklist (`owasp_llm_top10_checklist.md`),
identify **at least 2 concrete exposure risks specific to this actual
workflow's structure** — not a generic list of "AI could be risky"
concerns. Think concretely: what happens if the retrieved context (step
1) contains something unexpected? What happens if the data task (step
2) returns a value the prompt template wasn't expecting? What happens
if the LLM (step 3) is asked, by a user, to "ignore your previous
instructions" before the human checkpoint (step 4) ever sees the
output?
