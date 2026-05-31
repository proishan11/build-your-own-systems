# Staff-Level Review

Lead with findings. Prioritize bugs and missing guarantees over style.

## Review Order

1. Correctness and invariants.
2. Failure modes.
3. Concurrency and resource lifecycle.
4. Durability, recovery, or distributed-systems semantics.
5. Observability and debuggability.
6. Test coverage.
7. Simplicity and API clarity.

## Finding Format

Use this shape:

```text
Severity: file:line
What is wrong.
Why it matters.
Concrete fix or direction.
```

Severity levels:

- **Critical:** data loss, safety violation, deadlock, unsound consensus behavior.
- **High:** race, leak, broken cancellation, incorrect recovery, missing idempotency.
- **Medium:** important edge case, weak test, unclear API guarantee.
- **Low:** readability or maintainability issue.

## Review Questions

Ask these when the implementation is plausible but the design needs sharper reasoning:

1. What invariant does this code rely on?
2. Who owns closing this channel/file/socket?
3. What happens if the caller cancels midway?
4. What happens if this operation succeeds but the response is lost?
5. What happens after a crash between these two writes?
6. What metric would reveal this failing in production?

## Validation

When possible, run the exercise command. For Go concurrency, prefer:

```bash
go test ./...
go test -race ./...
```

For storage and distributed systems, prefer targeted tests first, then broader suites and stress/simulation tests.

