# Threat Modeling

## Concept

Threat modeling is the practice of identifying what can go wrong, who can cause it, what they can access, and how the system should prevent, detect, or recover from it.

## Why It Exists

Security failures often come from unclear trust boundaries. A system cannot protect what its designers never named.

## Mental Model

```text
assets -> actors -> trust boundaries -> threats -> controls -> tests
```

Start with what matters, then reason about who can influence it.

## Core Invariant

Every privileged action must have an explicit authorization boundary and an audit trail.

## Tiny Example

An AI agent has a tool called `delete_file(path)`. Threat modeling asks: who can prompt the agent, which paths are allowed, whether dry-run is available, who approves deletion, and how the action is logged.

## Common Misconceptions

- Authentication is not authorization.
- Internal tools still need security boundaries.
- Logging is not useful if it cannot answer who did what and why.
- Prompt injection is a security issue when model output can trigger tools.

## Self-Check

1. What asset is being protected?
2. Who can influence input?
3. What crosses a trust boundary?
4. What action needs approval?
5. What evidence remains after the action?

## Further Reading

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications
- MITRE ATT&CK Enterprise Matrix: https://attack.mitre.org/matrices/enterprise/
- OpenSSF Scorecard: https://openssf.org/scorecard/

