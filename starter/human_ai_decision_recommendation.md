# Human-Owned vs. AI-Assisted: A Stakes/Reversibility Framework

## The framework (given — you apply this, not derive it)

For any real decision, ask two real questions:

- **Stakes**: if the AI gets this wrong, how bad is the real
  consequence — for the person affected, and for the organization?
- **Reversibility**: can a wrong outcome be caught and undone before
  real harm happens, or is it effectively final once acted on?

**High stakes + low reversibility** → the decision should stay
human-owned, with AI as an assistant at most (drafting, flagging,
never deciding). **Lower stakes + high reversibility** → AI-assisted
(or even AI-autonomous, with monitoring) is defensible.

## The scenario (given)

A `finance_insurance` claims team is considering: **should the model
audited in this project (`given_data/model_predictions.csv`) be allowed
to autonomously approve small claims (under a proposed real dollar
threshold), with no human review, when it predicts a nonzero payment
with high confidence (`predicted_probability` above a proposed
threshold)?**

## Your task

TODO — apply the framework to this real scenario:

1. **Stakes**: what's the real consequence of a wrong autonomous
   approval? A wrong autonomous denial (if the threshold logic also
   covered denials)? Be specific about who's harmed and how.
2. **Reversibility**: if the model wrongly approves a claim that
   shouldn't have been paid, can that be caught and reversed? If it
   wrongly withholds an autonomous approval (falling back to human
   review), what's actually lost — is that even a real harm?
3. **Recommendation**: given 1 and 2, should any part of this decision
   be AI-autonomous? If so, specify the exact real boundary (a real
   dollar threshold, a real confidence threshold, or "no autonomous
   approval at all, ever, for this decision") — not a vague "with
   appropriate oversight."
4. **Connect to your fairness audit**: does the disparity you found in
   your Fairlearn audit change your recommendation? (It should — a
   model with a known, real fairness gap autonomously deciding
   anything makes the stakes/reversibility calculus worse, not the
   same.)

This recommendation feeds your group's facilitated discussion — see
`facilitation_outcome.md`.
