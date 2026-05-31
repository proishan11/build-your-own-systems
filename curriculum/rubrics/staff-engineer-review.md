# Staff Engineer Review Rubric

Use this rubric when reviewing any exercise implementation.

## Correctness

- The implementation states or implies clear invariants.
- The code handles edge cases intentionally, not accidentally.
- Tests cover normal behavior, boundary cases, and at least one failure path.
- Error handling preserves useful context.
- Retries, cancellation, cleanup, and partial progress are safe.

## Concurrency

- Shared state has an explicit ownership model.
- Goroutines, tasks, sockets, files, and timers cannot leak indefinitely.
- Cancellation is propagated through blocking operations.
- Backpressure is deliberate.
- Race detector and stress tests are part of validation where applicable.

## Distributed Systems

- Timeouts and retries are treated as uncertainty, not proof.
- Message duplication, delay, reordering, and loss are considered.
- Leader, lease, epoch, term, or fencing semantics are explicit.
- Recovery logic is tested after crash or restart.
- Safety and liveness are discussed separately.

## Database Systems

- Durability boundaries are explicit.
- On-disk formats are versioned or at least documented.
- Recovery is idempotent.
- Reads and writes have clear consistency semantics.
- Performance discussions include I/O, memory, CPU, and contention.

## Code Quality

- APIs are small and honest about their guarantees.
- Tests describe behavior rather than implementation trivia.
- Observability is present at meaningful state transitions.
- Benchmarks measure a specific claim.
- Complexity earns its keep.

## Staff-Level Reflection Prompt

After each milestone, answer:

1. What is the key invariant?
2. What is the most dangerous failure mode?
3. What would you instrument first in production?
4. What design decision would be hardest to reverse later?
5. What would change if this had 100x more load or 10x more nodes?

