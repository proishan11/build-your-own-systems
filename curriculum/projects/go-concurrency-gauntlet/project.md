# Go Concurrency Gauntlet

## Purpose

This project trains Go concurrency through implementation pressure. You will build small but production-shaped components where correctness depends on cancellation, ownership, backpressure, ordering, race freedom, and cleanup.

The goal is not to memorize goroutine/channel patterns. The goal is to develop the engineering reflexes needed to design concurrent services that keep working under load, shutdown, slow consumers, retries, and failure.

## What You Will Build

By the end, you will have a small concurrent runtime toolkit:

- A cancellable pipeline library.
- A bounded worker pool.
- A token bucket rate limiter.
- A singleflight cache.
- A pub/sub broker with slow-consumer handling.
- An actor-style mailbox.
- A concurrent web crawler.
- A TCP chat server.
- A mini MapReduce runtime.
- A deterministic stress harness for concurrency tests.

## Learning Format

Every exercise starts with a concept primer before code: why the pattern exists, the mental model, the core invariant, a tiny example, common misconceptions, self-check questions, and optional deeper references. Only then should the learner move into placeholder implementation and validation.

## Staff-Level Learning Outcomes

You should be able to explain:

- When to use channels, mutexes, atomics, condition variables, and context cancellation.
- How to prevent goroutine leaks.
- How to design APIs that make ownership and shutdown semantics obvious.
- How backpressure differs from buffering.
- How to test concurrency without relying on sleep-heavy tests.
- How to use `go test -race`, stress loops, benchmarks, and leak detection.
- How to reason about fairness, starvation, throughput, latency, and memory growth.

## Validation Standard

Every exercise should eventually support:

```bash
go test ./...
go test -race ./...
go test -run TestStress -count=100 ./...
go test -bench=. ./...
```

Where relevant, add leak detection with a package such as `go.uber.org/goleak`.

## Exercise Ladder

### Phase 1: Foundations

1. **Cancellable Fan-Out/Fan-In**
   - Build a pipeline where multiple workers consume inputs and emit outputs.
   - Preserve cancellation when downstream stops early.
   - Prove no goroutine leaks after cancellation.

2. **Bounded Queue**
   - Implement a blocking queue with `Push`, `Pop`, `Close`, and context-aware operations.
   - Define behavior for push-after-close and pop-after-drain.
   - Compare channel-based and mutex/condition-variable designs.

3. **Worker Pool**
   - Build a worker pool with bounded queueing, graceful shutdown, and immediate shutdown.
   - Return futures or result handles.
   - Ensure panics in jobs do not kill the pool silently.

4. **Token Bucket Rate Limiter**
   - Implement a limiter with burst capacity.
   - Support blocking wait, context cancellation, and non-blocking allow.
   - Benchmark lock contention.

### Phase 2: Shared State and Coordination

5. **Singleflight Cache**
   - Ensure concurrent requests for the same key share one in-flight computation.
   - Handle errors, cancellation, and cache TTL.
   - Prevent canceled callers from canceling work needed by other callers unless policy says so.

6. **Pub/Sub Broker**
   - Implement topics, subscriptions, publishing, and unsubscribe.
   - Choose a slow-consumer policy: block publisher, drop newest, drop oldest, or disconnect.
   - Expose metrics for dropped messages and subscriber lag.

7. **Actor Mailbox**
   - Build actors with serialized message handling.
   - Support ask/reply with timeout.
   - Add supervision policy for handler panics.

8. **Concurrent LRU Cache**
   - Implement a fixed-capacity cache with safe concurrent access.
   - Compare one global lock against sharded locks.
   - Benchmark read-heavy and write-heavy workloads.

### Phase 3: Networked Concurrency

9. **Concurrent Web Crawler**
   - Crawl URLs with per-host limits, global limits, deduplication, and cancellation.
   - Avoid unbounded memory growth.
   - Produce structured crawl results and errors.

10. **TCP Chat Server**
    - Support multiple clients, rooms, broadcast, private messages, and graceful shutdown.
    - Handle slow clients without blocking the whole room.
    - Add simple protocol parsing and fuzz tests.

11. **Streaming Proxy**
    - Proxy TCP streams bidirectionally.
    - Correctly propagate half-closes, deadlines, cancellation, and byte counters.
    - Add tests with in-memory pipes.

### Phase 4: Runtime and Systems Patterns

12. **Mini MapReduce Runtime**
    - Execute map tasks, shuffle intermediate values, and run reduce tasks.
    - Retry failed tasks.
    - Track task states and expose progress.

13. **Work-Stealing Scheduler**
    - Implement local queues per worker and stealing from peers.
    - Compare throughput against a global queue.
    - Discuss fairness and cache locality.

14. **Deterministic Stress Harness**
    - Build a test harness that repeatedly runs operations with randomized scheduling.
    - Capture seed values for failed runs.
    - Make flakes reproducible.

## Capstone: Concurrent Service Kernel

Build a small service framework that combines:

- Worker pool.
- Rate limiter.
- Singleflight cache.
- Pub/sub event stream.
- Graceful shutdown.
- Metrics.
- Structured logs.
- Integration tests under load.

Example application: a concurrent URL metadata fetcher that deduplicates requests, rate-limits outbound calls, streams events to subscribers, and shuts down cleanly.

## Design Reviews

Before implementation, write a short design note:

- What owns each goroutine?
- What closes each channel?
- How does cancellation flow?
- Where does backpressure happen?
- What can block forever?

After implementation, answer:

- What race did the design avoid?
- What leak did the design avoid?
- What benchmark result surprised you?
- What would break under 10x concurrency?

## First Exercise To Scaffold

Start with **Cancellable Fan-Out/Fan-In**.

Starter package:

```text
playgrounds/go-concurrency-gauntlet/
  go.mod
  pipeline/
    pipeline.go
    pipeline_test.go
```

The placeholder implementation should expose:

```go
func Map[T any, R any](
    ctx context.Context,
    workers int,
    in <-chan T,
    fn func(context.Context, T) (R, error),
) (<-chan Result[R], error)
```

Core requirements:

- Reject `workers <= 0`.
- Stop workers when `ctx` is canceled.
- Stop workers when input closes.
- Do not block forever if downstream stops reading after cancellation.
- Preserve worker errors in the result stream.
- Close the output channel exactly once.
