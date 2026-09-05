# Threat model

## Assets

What is worth protecting: data, credentials, the model, the infrastructure it can reach, the trust of its users.

## Trust boundaries

A diagram with the boundaries drawn: internet / gateway / application / model / tools / cluster. Where does untrusted input enter? For RAG: documents. For agents: tool outputs.

## Attackers

Who might attack and what they want: an external user, a malicious document author, a compromised dependency, an insider, a confused agent.

## Threats

One row per threat. Use a checklist (STRIDE, or the OWASP Top 10 for LLM Applications) to make sure you have not skipped a category.

| Threat | Entry point | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|
| Prompt injection via retrieved document | RAG context | Agent takes attacker-directed action | | Tool allow-list, approval gate, instruction/data separation | |
| | | | | | |

## Residual risk

What remains after mitigations, and who accepted it.
