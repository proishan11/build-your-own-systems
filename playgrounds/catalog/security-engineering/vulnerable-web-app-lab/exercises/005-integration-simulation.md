# Exercise 005: Vulnerable Web App Lab Integration Scenario

Shared concept chapter: [threat-modeling.md](../../../../../curriculum/concepts/security/threat-modeling.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **Vulnerable Web App Lab**. The work is centered on `run_vulnerable_web_app_lab_scenario`, not on a generic scaffold. You will implement behavior for **http input** moving through **security policy** while preserving the project invariant.

The implementation target is: Implement `run_vulnerable_web_app_lab_scenario` so Vulnerable Web App Lab has a deterministic integration simulation with state, `requests_blocked`, failures, recoveries, and invariant reporting.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of Vulnerable Web App Lab and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **security policy**. A **http input** arrives, the component decides whether `sanitize request` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `xss payload` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The scenario runner must expose security policy state and requests_blocked metrics while reporting malformed events as violations instead of hiding them.

## Tiny Example

Applying `security policy=ready`, recording `requests_blocked=3`, failing, and recovering should preserve state and produce one failure plus one recovery.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `run_vulnerable_web_app_lab_scenario` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `xss payload` happened in production?

## Goal

Implement `run_vulnerable_web_app_lab_scenario` so Vulnerable Web App Lab has a deterministic integration simulation with state, `requests_blocked`, failures, recoveries, and invariant reporting.

## Concepts

- least privilege
- auditability
- trust boundaries
- abuse cases

## Files To Edit

- `lab_005.py`

## Contract

Your implementation must:

- process apply, metric, fail, and recover events in order
- track `requests_blocked`, failures, and recoveries
- return invariant_ok and violations
- handle empty scenarios deterministically

## Design Hints

- Initialize the full report shape before processing events.
- Treat missing resources as violations, not exceptions.
- Keep metric defaults explicit so dashboards do not infer missing data.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_005.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/security-engineering/vulnerable-web-app-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab_005.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- OWASP Top 10: https://owasp.org/www-project-top-ten/

## Staff-Level Review Questions

1. What makes this implementation specific to Vulnerable Web App Lab, rather than a generic CRUD helper?
2. Which failure mode does `xss payload` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
