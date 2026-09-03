# %% [markdown]
# # Bias/Fairness Audit
#
# Run this file cell-by-cell in VS Code's Jupyter extension. Audits the
# real, provided model predictions in `given_data/model_predictions.csv`
# — see `given_data/README.md` for what this model is and why
# `rated_flood_zone` is the real segment to check.

# %%
import pandas as pd
from fairlearn.metrics import MetricFrame, false_negative_rate, false_positive_rate, selection_rate
from sklearn.metrics import accuracy_score

# %% [markdown]
# ## 1. Load the given predictions

# %%
df = pd.read_csv("given_data/model_predictions.csv")
print(df.shape)
print(df['rated_flood_zone'].value_counts())

# %% [markdown]
# ## 2. Run a real Fairlearn group-fairness audit
#
# Pick the two real flood zones with the most rows (the smaller
# categories have too few rows for a stable metric) and compute a real
# `MetricFrame` across them.

# %%
# TODO: filter to the 2 zones with the most rows
# TODO: build a real fairlearn.metrics.MetricFrame with at least
# false_negative_rate, selection_rate, and accuracy_score, grouped by
# rated_flood_zone
# TODO: print mf.by_group and at least one real .difference() value

# %% [markdown]
# ## 3. Diagnose a plausible root cause
#
# TODO (markdown, right here): given what you know about this model
# (its real features: `occupancy_type`, `cause_of_damage` — NOT
# `rated_flood_zone` itself), what's a plausible, specific explanation
# for why a disparity by flood zone would show up anyway? (Hint: think
# about whether the model's actual features could be indirectly
# correlated with flood zone, even without using it directly.)

# %% [markdown]
# ## 4. Propose a specific fix
#
# TODO (markdown, right here): not "collect more data" — a real,
# specific, technically plausible fix (e.g., a specific reweighting
# approach, a specific fairness constraint, a specific threshold
# adjustment per group, or a specific alternative feature set).
