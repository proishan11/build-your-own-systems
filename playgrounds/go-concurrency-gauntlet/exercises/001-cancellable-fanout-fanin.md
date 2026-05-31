# Exercise 001: Cancellable Fan-Out/Fan-In

Shared concept chapter: [Pipelines and Cancellation](../../../curriculum/concepts/go-concurrency/pipelines-and-cancellation.md)

## Concept Primer

A pipeline is a sequence of stages where each stage receives values, transforms them, and sends results onward. Fan-out means multiple workers share the same input stream. Fan-in means their outputs are merged into one result stream.

The hard part is not starting goroutines. The hard part is stopping them. A production pipeline must handle the case where the caller cancels the operation or stops reading results. If workers keep trying to send after nobody is listening, they can block forever.

## Why This Matters

This pattern shows up anywhere a service parallelizes work: file processing, request fan-out, crawlers, ETL jobs, queue consumers, and backend aggregation. If cancellation and ownership are wrong, the service leaks goroutines under exactly the conditions where it is already under stress.

## Mental Model

Think of each worker as a small machine:

1. Wait for either cancellation or an input item.
2. If canceled, stop.
3. If input closes, stop.
4. Process one item.
5. Try to deliver the result, but abandon delivery if cancellation happens.

One separate coordinator waits for all machines to stop, then closes the output channel. Workers send; the coordinator closes. That ownership split is the safety rail.

## Core Invariant

The output channel is closed exactly once, and only after every worker has stopped sending.

## Tiny Example

Input values are `1, 2, 3`, the function squares each value, and there are two workers. Worker A might process `1` and `3`; worker B might process `2`. The output order is not guaranteed, but the output set should be `{1, 4, 9}` if no cancellation occurs.

If the context is canceled after `1` is processed, it is acceptable to emit fewer than three results. Cancellation means the caller no longer requires all work to finish.

## Common Misconceptions

- A buffered channel is not a cancellation strategy; it only delays blocking.
- Every sender should not close the output channel. That causes send-after-close panics.
- `context.Context` does not forcibly kill goroutines. Your code must observe it.
- A worker can block forever if it sends to `out` without also selecting on `ctx.Done()`.

## Self-Check

Before coding, answer:

1. Who owns closing the output channel?
2. What happens if downstream stops reading?
3. Can a worker be stuck sending a result after cancellation?
4. Does cancellation require all already-read items to produce results?

## Goal

Implement a generic concurrent `Map` function that starts a fixed number of workers, applies a function to every input item, emits results, and exits cleanly when input closes or context is canceled.

## Concepts

- Goroutine ownership.
- Fan-out/fan-in.
- Context cancellation.
- Channel closing rules.
- Backpressure.
- Error propagation.

## Files To Edit

- `pipeline/pipeline.go`

## Contract

Your implementation must:

- Reject `workers <= 0`.
- Start exactly `workers` worker goroutines.
- Read from `in` until it closes or `ctx` is canceled.
- Call `fn(ctx, item)` for every consumed input item.
- Emit one `Result[R]` per consumed item unless cancellation prevents delivery.
- Preserve errors returned by `fn`.
- Close the output channel exactly once after all workers exit.
- Avoid goroutine leaks if the caller cancels the context and stops reading.

## Design Hints

Think in terms of ownership:

- Workers own calls to `fn`.
- A coordinator owns closing the output channel.
- The caller owns canceling the context.
- Nobody should send on a channel after it is closed.

A common shape is:

1. Validate `workers`.
2. Create the output channel.
3. Start `workers` goroutines.
4. Each worker loops on `select { case <-ctx.Done(): ...; case item, ok := <-in: ... }`.
5. When a worker has a result, send it with another `select` so cancellation can interrupt a blocked send.
6. Use a `sync.WaitGroup`.
7. Start one closer goroutine that waits for workers and closes output.

## Validation

Run from `playgrounds/go-concurrency-gauntlet`:

```bash
go test ./...
go test -race ./...
```

The tests intentionally describe behavior rather than the implementation. You should be able to change the internal structure without changing the tests.

## Further Reading

- Go blog, "Go Concurrency Patterns: Pipelines and cancellation": https://go.dev/blog/pipelines
- Go blog, "Go Concurrency Patterns: Context": https://go.dev/blog/context
- Go memory model: https://go.dev/ref/mem

## Staff-Level Review Questions

1. What owns the lifecycle of each goroutine?
2. What happens if downstream stops reading?
3. What happens if `fn` blocks forever?
4. What production metric would reveal goroutine leaks?
5. Would you buffer the output channel? Why or why not?
