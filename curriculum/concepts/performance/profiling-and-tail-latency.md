# Profiling and Tail Latency

## Concept

Profiling identifies where time, CPU, memory, I/O, or contention is spent. Tail latency studies the slow requests, not just the average request.

## Why It Exists

Users experience individual requests. A system with good average latency can still feel broken if p95 or p99 latency is bad. Staff-level performance work starts from evidence.

## Mental Model

```text
measure -> localize bottleneck -> change one thing -> remeasure
```

For latency:

```text
p50: typical
p95: uncomfortable
p99: incident-shaped
```

## Core Invariant

Every optimization should name the measured bottleneck it targets and prove the effect with comparable measurements.

## Tiny Example

A service has average latency of 80 ms but p99 of 4 seconds. Profiling shows a global lock around cache refresh. The fix is not "use a faster language"; it is reducing contention or moving refresh off the request path.

## Common Misconceptions

- Benchmarks without workload assumptions are stories.
- Average latency hides pain.
- Optimizing before measuring often moves complexity, not bottlenecks.
- CPU profiles do not explain all I/O or lock contention problems.

## Self-Check

1. What metric proves the system is slow?
2. Is the bottleneck CPU, memory, I/O, lock contention, or queueing?
3. Which percentile matters for users?
4. What changed between benchmark runs?

## Further Reading

- Brendan Gregg's systems performance resources: https://www.brendangregg.com/systems-performance-2nd-edition-book.html
- USE method: https://www.brendangregg.com/usemethod.html
- OpenTelemetry docs: https://opentelemetry.io/docs/

