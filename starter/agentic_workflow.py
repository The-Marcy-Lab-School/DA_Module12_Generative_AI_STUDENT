# %% [markdown]
# # Agentic Workflow Project
#
# Run this file cell-by-cell in VS Code's Jupyter extension. See
# `../required_components.md` for exactly what each section needs.
# This is a genuinely open-ended build — you're defining your own real
# data problem, not filling in a fixed template's blanks.

# %%
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# %% [markdown]
# ## 1. Define your own real data problem
#
# Not a restatement of any example you've seen — a genuine question
# about your own chosen domain (see the domain data you've used since
# Module 3) that an agentic workflow (prompt + retrieval + a data
# computation) could actually help answer.
#
# TODO (markdown, right here):
# - What real question are you answering, and for whom?
# - Why does answering it need BOTH retrieval (looking something up)
#   AND a data task (computing something)? If your answer only needs
#   one, pick a different question — the point is a real chain.

# %% [markdown]
# ## 2. Prompt engineering: naive vs. revised
#
# Write a first, naive prompt for your task. Then revise it using a
# real role/context/task/format structure, and show both side by side
# — see `../starter/prompt_engineering_worksheet.md`.

# %%
naive_prompt = ""  # TODO
revised_prompt = ""  # TODO

# %% [markdown]
# TODO (markdown): why is the revised version actually better? Be
# specific — not "it's more detailed," but what a vague prompt would
# have gotten wrong that the revised one fixes.

# %% [markdown]
# ## 3. Retrieval step (RAG)
#
# Your knowledge base is `../data/SOURCE.md` (in this repo) — the same
# file describing every domain's real schema/license/caveats that
# you've already used since Module 3. Chunk it, build a real retriever,
# and test it against at least 5 real questions.

# %%
# TODO: load SOURCE.md, chunk it (decide your own chunking strategy —
# by section? by paragraph? justify your choice against the file's
# actual structure)
chunks = []  # TODO

# %%
# TODO: build a real TF-IDF retriever (TfidfVectorizer + cosine_similarity)
# TODO: run at least 5 real test queries, print which chunk each one
# retrieves and its similarity score

# %% [markdown]
# TODO (markdown): how many of your 5 queries retrieved a genuinely
# relevant chunk? If any missed, why — what does that tell you about
# your chunking choice?

# %% [markdown]
# ## 4. Data task
#
# A real computation against your own domain's actual CSV data (see
# `../data/<domain>/` in this repo), informed by what your retrieval
# step found (e.g., the retrieved schema info tells you which column to
# query).

# %%
# TODO: a real pandas computation against your own domain data

# %% [markdown]
# ## 5. Chain it: retrieval → data task → LLM synthesis
#
# The whole point of "agentic" is that these steps run **programmatically
# in sequence**, not manually copy-pasted between separate chat
# sessions. See `../starter/llm_api_setup.md` for real, free API setup.

# %%
# TODO: call a real LLM API (Anthropic, OpenAI, or Gemini's free tier)
# with a prompt that includes your retrieved context AND your data
# task's real result, asking it to synthesize a written answer

# %% [markdown]
# ## 6. Human-in-the-loop checkpoint
#
# Design this BEFORE you assume the AI's output is usable — per this
# project's own exemplar guidance, decide what a human must check and
# why, as a real design constraint, not an afterthought.
#
# TODO (markdown, right here):
# - Exactly what would a human need to verify before using this output?
# - What's one realistic, specific error your checkpoint would actually
#   catch? (Not a generic "the AI could be wrong" — something specific
#   to YOUR workflow.)

# %%
# TODO: implement the actual checkpoint — a real pause/review step in
# your code, not just a comment saying "a human should check this"

# %% [markdown]
# ## 7. Catch two real AI errors
#
# See `../starter/ai_error_catch_1.md` (a code snippet, more guided)
# and `../starter/ai_error_catch_2.md` (a written summary, more
# independent). Both have a real planted error.
#
# TODO (markdown, right here): for each one, name the specific error
# and your specific fix.

# %% [markdown]
# ## 8. Adaptability log
#
# TODO (markdown, right here): describe one specific initial approach
# in this project that didn't work, and the specific change you made in
# response. Not "I iterated a few times" — the actual failure and the
# actual fix.

# %% [markdown]
# ## 9. Autonomy documentation
#
# TODO (markdown, right here): state plainly what this workflow does
# autonomously (no human involved) versus what requires sign-off before
# it's used — this should match your section 6 checkpoint exactly.
