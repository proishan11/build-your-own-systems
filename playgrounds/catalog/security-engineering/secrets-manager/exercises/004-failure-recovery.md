# Exercise 004: Secrets Manager Failure and Recovery

Shared concept chapter: [threat-modeling.md](../../../../../curriculum/concepts/security/threat-modeling.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Secrets Manager**. The work is centered on `recover_secrets_manager_plaintext_exposure`, not on a generic scaffold. You will implement behavior for **secret version** moving through **secret store** while preserving the project invariant.

The implementation target is: Implement `recover_secrets_manager_plaintext_exposure` so Secrets Manager handles transient failures, permanent `plaintext exposure` cases, and exhausted retry budgets explicitly.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Secrets Manager and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **secret store**. A **secret version** arrives, the component decides whether `rotate secret` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `plaintext exposure` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

Recovery decisions for secret store must never turn a permanent plaintext exposure into an unsafe retry.

## Tiny Example

A timeout on attempt 1 retries at attempt 2. The domain-specific failure fails immediately. A timeout at the max attempt gives up.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `recover_secrets_manager_plaintext_exposure` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `plaintext exposure` happened in production?

## Goal

Implement `recover_secrets_manager_plaintext_exposure` so Secrets Manager handles transient failures, permanent `plaintext exposure` cases, and exhausted retry budgets explicitly.

## Concepts

- least privilege
- auditability
- trust boundaries
- abuse cases

## Files To Edit

- `lab_004.py`

## Contract

Your implementation must:

- retry transient timeout or unavailable errors while attempts remain
- fail permanent `plaintext exposure` reports immediately
- give up when retry budget is exhausted
- include resource and reason fields for operators

## Design Hints

- Classify permanent domain failures before retryable infrastructure failures.
- Compare `attempt` to `max_attempts` before returning retry.
- Return structured decisions; strings alone are too hard to operate.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_004.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/security-engineering/secrets-manager`:

```bash
python3 -m unittest discover -s tests -p test_lab_004.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- OWASP Top 10: https://owasp.org/www-project-top-ten/

## Staff-Level Review Questions

1. What makes this implementation specific to Secrets Manager, rather than a generic CRUD helper?
2. Which failure mode does `plaintext exposure` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
