# Given Data: A Provided Model's Predictions

`model_predictions.csv` (600 rows) is real output from a real
classifier — the same real model type built in Module 11, predicting
whether a `finance_insurance` flood-insurance claim results in a
nonzero building-damage payment, using only intake-time features
(`occupancy_type`, `cause_of_damage` — deliberately not
`building_damage_amount`, per Module 11's own "don't use a
near-definitional feature" finding).

## Columns

- `claim_id` — real claim identifier.
- `occupancy_type`, `cause_of_damage` — the real features the model was
  trained on.
- `rated_flood_zone` — a real geographic flood-risk classification
  (`AE` = high-risk, `X` = lower-risk, plus several smaller real
  categories) — **not** a feature the model was trained on. This is
  your sensitive/segment feature for the fairness audit.
- `actual_nonzero_payment` — the real, true outcome (1 = the claim
  actually got paid, 0 = it didn't).
- `predicted_nonzero_payment` — the model's real prediction (1 or 0).
- `predicted_probability` — the model's real predicted probability.

## Why this is the right artifact for a fairness audit

You're not building a new model this project — you're auditing one
that already exists, which is the realistic shape of this work in
practice (most fairness audits happen against models someone else
already built and deployed). `rated_flood_zone` is a real, meaningful
segment to check: it's not something the model was trained on, but it's
a real, protected-adjacent geographic classification where a
disparity would be a genuine, concrete concern for an insurer's real
claims-handling fairness.
