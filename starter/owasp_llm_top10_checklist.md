# OWASP Top 10 for LLM Applications (Reference Checklist)

**A real, honest note on versioning**: the list below is OWASP's v1.1
(2023) list — the version most widely cited in industry as of this
writing, and still real and still useful. OWASP has since moved active
development to a newer "GenAI Security Project" list; if you want to
check the current version, search "OWASP GenAI Security Project Top
10" — the underlying risk categories below are still substantively
correct even if the current list has evolved.

1. **LLM01: Prompt Injection** — user input manipulates the model into
   ignoring its original instructions.
2. **LLM02: Insecure Output Handling** — the model's output is trusted
   and acted on (e.g., executed, inserted into a database query)
   without validation.
3. **LLM03: Training Data Poisoning** — the model (or a fine-tune) was
   trained on data an attacker could manipulate.
4. **LLM04: Model Denial of Service** — resource-exhaustion attacks
   against the model (e.g., extremely long/repetitive inputs).
5. **LLM05: Supply Chain Vulnerabilities** — risk from third-party
   models, plugins, or training data.
6. **LLM06: Sensitive Information Disclosure** — the model reveals
   private/confidential data it was exposed to (via training or
   context).
7. **LLM07: Insecure Plugin Design** — a plugin/tool the model can call
   has inadequate input validation or access control.
8. **LLM08: Excessive Agency** — the model/agent is given more
   autonomy, permissions, or functionality than the task actually
   requires.
9. **LLM09: Overreliance** — a human accepts the model's output without
   the scrutiny it needs.
10. **LLM10: Model Theft** — unauthorized access to or exfiltration of
    a proprietary model.

## How to use this for your evaluation

Don't just copy this list — for each item, ask whether it applies to
`given_data/agentic_workflow_description.md`'s *actual* workflow
structure. Some items won't apply (this project doesn't use plugins in
the LLM07 sense, for example) — name the ones that genuinely do, and
say specifically *how* they'd manifest in *this* workflow, not in
general.
