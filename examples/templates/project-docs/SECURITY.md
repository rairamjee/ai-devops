# Security

## Surface

What can reach this system and from where: users, other services, the internet, an AI agent's tools. What data it handles and how sensitive it is.

## Identity and access

Who and what can call it; how they authenticate; which Kubernetes ServiceAccount and RBAC it runs with, and why those permissions and no more.

## Secrets

Which secrets exist, where they live, how they reach the process (never in code, never in images, never in prompts or logs), how they rotate.

## Network

Ingress and egress rules. For AI projects: which model providers or hubs the system may reach, and what is blocked.

## Container and supply chain

Base image and how it is pinned; non-root user; read-only filesystem; capabilities dropped; how dependencies are pinned and scanned.

## AI-specific controls (AI projects)

- Prompt injection and indirect injection: where untrusted text enters the prompt and what limits its influence.
- Output handling: validation before anything acts on model output.
- Tools and agents: allow-lists, argument validation, least privilege, approval gates, audit log.
- Data: what may and may not be sent to a model provider.

## Known gaps

Be honest. A short list of gaps with a reason is more credible than silence.

See also [THREAT-MODEL.md](THREAT-MODEL.md) where present.
