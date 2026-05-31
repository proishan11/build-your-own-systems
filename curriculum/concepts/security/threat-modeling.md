# Threat Modeling

## What You Should Know First

You should know that security is not only cryptography or login screens. Security is about what the system protects, who can act, what they can see, and what happens when assumptions fail.

## The Problem

Teams often discover security issues late, after architecture and code have already made unsafe behavior natural. Threat modeling moves security thinking earlier. It asks: what are we building, what can go wrong, and what are we going to do about it?

The goal is not to imagine every possible attack. The goal is to identify credible risks and design boundaries that reduce damage.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Asset | Something worth protecting: data, capability, identity, availability, or money. |
| Actor | User, service, operator, attacker, or automated process. |
| Trust boundary | Place where data or control crosses between different trust levels. |
| Threat | A possible unwanted event. |
| Mitigation | Design or control that reduces likelihood or impact. |
| Abuse case | Scenario describing how the system can be misused. |
| Least privilege | Give each actor only the access needed for its job. |

## Mental Model

Draw the system as data flows:

```text
user -> API -> service -> database
                |
                +-> external tool
```

Then mark trust boundaries. Every boundary is a place where validation, authentication, authorization, logging, rate limiting, or isolation may be needed.

## Core Invariant

No actor should gain more authority, data access, or ability to cause damage than the design explicitly grants.

This includes internal services and AI tools. "It is inside the system" is not the same as "it is trusted for everything."

## Worked Example

An agent can read documents and create support tickets.

| Question | Design Consequence |
| --- | --- |
| Can retrieved text instruct the agent? | Treat documents as untrusted evidence, not commands. |
| Can the agent mutate billing data? | Require explicit tool permission or human approval. |
| Are tool calls logged? | Keep an audit trail for actions. |
| What if the model is tricked? | Enforce policy outside the model. |

The prompt can help, but the system boundary should not depend only on prompt obedience.

## Implementation Shape

A threat model can be lightweight but concrete:

| Step | Output |
| --- | --- |
| Scope the system | Diagram, assets, actors, and trust boundaries. |
| Enumerate threats | Abuse cases or STRIDE-style categories. |
| Rank risk | Impact, likelihood, and detection difficulty. |
| Choose mitigations | Controls with owners and tests. |
| Validate | Security tests, logs, alerts, and review questions. |

Good threat models become engineering work. If nothing changes after the model, it was probably theater.

## Failure Modes

| Failure | Result |
| --- | --- |
| Treating internal traffic as trusted | One compromised service reaches everything. |
| Auth without authorization | Logged-in users can access wrong resources. |
| Secrets in logs | Debugging output becomes data exposure. |
| No audit trail | Incidents cannot be reconstructed. |
| Prompt-only safety | Model behavior becomes the security boundary. |
| Ignoring availability | Attackers can harm users without stealing data. |

## Exercise Bridge

Security exercises should force you to identify assets, model trust boundaries, exploit vulnerable behavior, and implement mitigations. Agent security labs should treat tools, retrieval, prompts, and sandboxes as separate boundaries.

## Self-Check

1. What assets does this system protect?
2. Where does untrusted data enter?
3. Which actor can mutate state?
4. What would you log for investigation?
5. Which mitigation is enforced by code rather than policy text?

## Further Reading

- OWASP Threat Modeling: https://owasp.org/www-community/Threat_Modeling
- STRIDE model overview: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- OWASP Top 10: https://owasp.org/www-project-top-ten/
