# Above & Beyond: Stretch Scope

Each item below is optional, and each one previews something the
capstone (Module 13) will assume you already have a real feel for.

## Part A — Agentic Workflow

### 1. A second, real knowledge-base document

Extend your retrieval step beyond `SOURCE.md` with a second real
document (e.g. your own earlier project's `README.md`), and discuss how
retrieval quality/relevance changes with a more heterogeneous knowledge
base. **Why this matters next**: the capstone's own agentic work will
likely need to retrieve across multiple real sources, not one clean
file — this is that judgment call, made for real.

### 2. A longer chain

Add a 3rd (or more) real step to your chain — e.g., a second data task,
or a real validation step that checks the LLM's output against your
data before the human-in-the-loop checkpoint even sees it. **Why this
matters next**: `agentic-ai` is an explicit prerequisite for Module 13
— longer, more realistic chains are exactly what that project assumes
you can build.

### 3. A real MCP case-study reflection

Read a real, current explainer on the Model Context Protocol (MCP) and
write a real comparison: what would change about your workflow's
tool-calling if you'd built it via MCP instead of this project's direct
approach? **Why this matters next**: this module's own Part B
governance content assumes familiarity with how modern agent tooling is
actually standardized in practice, not just a single project's bespoke
approach.

## Part B — Responsible AI Evaluation

### 1. A second Fairlearn metric

Compute both `demographic_parity_difference` and
`equalized_odds_difference` (or another second real metric) and discuss
what each one captures differently — they can disagree, and knowing why
is a real, useful skill. **Why this matters next**: the capstone's own
`data-governance` work assumes you already know that "fair" isn't a
single number.

### 2. A second governance framework

Evaluate your chosen AI system against a **second** real framework (not
just your chosen domain's) and compare what each would require
differently for the exact same system. **Why this matters next**: real
organizations often operate across multiple regulatory regimes at once
— this is that comparison, made for real.

### 3. A real fairness mitigation, demonstrated

Rather than just proposing a fix, actually implement one — e.g.,
Fairlearn's own `ExponentiatedGradient` reduction technique — and show
whether it actually narrows the real disparity you found, and what it
costs in overall accuracy. **Why this matters next**: the capstone will
expect you to move from "I found a problem" to "I fixed it and can show
the tradeoff," not stop at diagnosis.
