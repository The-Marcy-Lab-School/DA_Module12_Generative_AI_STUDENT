# Catch the AI's Mistake — Exercise 1 (Code Snippet)

An AI assistant was asked: *"Write a function that returns the top 3
highest-value rows per category in a DataFrame."* Here's what it wrote:

```python
def top_3_per_category(df, category_col, value_col):
    """Return the top 3 rows by value_col, within each category_col group."""
    return df.groupby(category_col).head(3)
```

The AI's own explanation: *"This groups the DataFrame by category, then
takes the first 3 rows from each group — giving you the top 3 highest-
value rows per category."*

**Your job**: run this function on a real DataFrame (use your own
domain data) and check whether it actually does what the AI claims.
It's syntactically valid Python — it runs without error — but does it
produce the *right* answer?

**Hint, since this is your first pass at this exercise**: `.head(3)`
and "top 3 by value" are not automatically the same operation. Think
about what determines which 3 rows `.head(3)` returns from each group,
and whether that has anything to do with `value_col` at all.

Document in `agentic_workflow.py` section 7: the specific bug, why it's
wrong (not just "it's wrong" — trace through what it actually returns
vs. what was asked for), and your corrected version.
