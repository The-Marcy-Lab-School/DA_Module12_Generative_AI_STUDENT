# AI-Use Policy Recommendation Memo

Written for a real stakeholder in your chosen regulated domain. Reuse
your real numbers from `bias_audit.py` — don't re-derive anything here.

## 1. Chosen domain and governance framework

TODO: which regulated domain (`finance_insurance`, `healthcare_operations`,
or `public_sector`), and which specific, named framework applies?
(`finance_insurance` → the Federal Reserve/OCC's SR 11-7 model-risk-
management guidance; `healthcare_operations` → HIPAA's Security Rule
access-control expectations; `public_sector` → NIST's AI Risk
Management Framework.) Compare it against at least one other
framework's expectations — what would a non-regulated domain be able
to skip that your chosen domain can't?

## 2. Bias/fairness audit summary

TODO: your real Fairlearn metric, the real disparity found (or not
found), your diagnosed root cause, and your proposed fix — from
`bias_audit.py`, summarized for a non-technical reader.

## 3. Security exposure summary

TODO: the ≥2 real, specific OWASP-checklist risks you identified for
the given agentic workflow (`given_data/agentic_workflow_description.md`),
and what you'd recommend to address each.

## 4. Ethical implications: who could be harmed, and how

TODO: name a **specific stakeholder** (not "customers" — a specific,
concrete role or person type) who could be harmed by this AI system's
proposed use, and specifically how. Vague language here
(`common_project_mistakes` #4) is the most common way this section goes
wrong.

## 5. Human-owned vs. AI-assisted recommendation

TODO: summarize your real recommendation from
`human_ai_decision_recommendation.md` and your group's real facilitated
outcome from `facilitation_outcome.md`.

## 6. PII/sensitivity-tier handling

TODO: using Module 10's real tier system (Public / Internal /
Confidential / Restricted), which tiers of data in your chosen domain
are safe to expose to the AI system being governed, and which aren't?
Be specific about *why*, tied to your chosen framework from section 1.

## 7. Final recommendation

TODO: a specific, concrete, named-framework-grounded recommendation —
not "the company should be careful with AI" (`common_project_mistakes`
#3).
