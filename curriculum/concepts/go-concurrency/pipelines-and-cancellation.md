# Pipelines and Cancellation

## What You Should Know First

You should know that a goroutine is an independently scheduled function, a channel carries values between goroutines, and `context.Context` is a cooperative cancellation signal. You do not need to be an expert in Go scheduling before reading this chapter.

## The Problem

Concurrent programs often need to process many independent items: crawl URLs, resize images, query services, parse logs, or fan out requests. A pipeline lets you express this as stages instead of hand-wiring every worker.

The hard part is not starting work. The hard part is stopping work. If downstream quits early, upstream goroutines can block forever while sending. If cancellation is ignored, a request can finish while its workers keep running in the background.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Stage | A function or goroutine group that receives values, transforms them, and sends values onward. |
| Fan-out | Multiple workers read from the same input stream. |
| Fan-in | Multiple workers send into a shared output stream. |
| Backpressure | Slow downstream consumers naturally slow upstream producers. |
| Cancellation | A signal that work is no longer needed and should stop promptly. |
| Ownership | The rule that says which goroutine is allowed to close a channel or release a resource. |

## Mental Model

Picture a small factory line:

```text
input channel -> workers -> output channel
```

Each worker repeatedly makes three choices:

1. receive an input item
2. notice cancellation and stop
3. notice the input channel is closed and stop

When producing output, the worker must choose again:

1. send the result
2. notice cancellation and stop

One coordinator waits until all workers are done, then closes the output channel exactly once.

## How It Works Step By Step

A cancellable pipeline is a lifecycle protocol, not just a few goroutines.

| Step | Mechanism | Rule |
| --- | --- | --- |
| Validate inputs | Check worker count, nil function, or options. | Reject invalid configurations before starting goroutines. |
| Start workers | Launch a fixed number of goroutines. | Each worker must have a clear stop condition. |
| Receive work | Select on input and cancellation. | A canceled caller no longer needs more work. |
| Produce output | Select on output send and cancellation. | Do not block forever if downstream stopped reading. |
| Track lifecycle | Use a wait group or equivalent. | The closer must know when all sends are impossible. |
| Close output | One coordinator closes after all workers exit. | Multiple closers or early close can panic. |

The worker pool and bounded queue exercises are variations on the same lesson: ownership and wakeup rules matter more than the syntax of channels.

## Core Invariant

The output channel is closed exactly once, and only after all goroutines that might send to it have stopped sending.

This invariant prevents two common panics: sending on a closed channel and closing a channel more than once.

## Worked Example

Suppose `Map(ctx, in, square, workers=2)` receives `1, 2, 3`.

| Event | What Can Happen |
| --- | --- |
| Two workers start | Both wait on input or cancellation. |
| Inputs arrive | Worker A might process `1`; worker B might process `2`. |
| Results are sent | Output could be `1, 4, 9` or `4, 1, 9`; order is not guaranteed unless the API promises order. |
| Input closes | Workers drain available work, then exit. |
| All workers exit | The coordinator closes the output channel. |

If the caller cancels after one result, fewer outputs are acceptable. Cancellation means the caller has withdrawn interest in the remaining work.

## State Or Flow Walkthrough

A healthy fan-out/fan-in run looks like this:

```text
t0 caller creates ctx and input channel
t1 coordinator starts workers
t2 workers receive input values
t3 workers compute and send results
t4 input channel closes
t5 workers drain or exit
t6 coordinator observes all workers done
t7 coordinator closes output
```

A cancellation path is different:

```text
t0 caller cancels ctx
t1 blocked receivers wake through ctx.Done
t2 blocked senders choose cancellation instead of output send
t3 workers return without sending more results
t4 coordinator closes output after workers exit
```

If a worker sends without selecting on cancellation, `t2` can get stuck forever.

## Implementation Shape

Most cancellable fan-out/fan-in implementations have the same skeleton:

| Piece | Responsibility |
| --- | --- |
| Validate inputs | Reject nil functions, zero worker counts, or invalid options. |
| Worker goroutines | Receive input, call the function, and attempt to send output. |
| `sync.WaitGroup` | Tracks worker lifetime. |
| Closer goroutine | Waits for all workers and closes the output channel. |
| `select` blocks | Let receives and sends stop when the context is canceled. |

The worker usually needs two `select` statements: one around receiving input and one around sending output. A send can block if downstream stops reading.

## Failure Modes

| Failure | Why It Happens | Design Response |
| --- | --- | --- |
| Goroutine leak | A worker blocks on send after downstream quits. | Select on `ctx.Done()` while sending. |
| Double close panic | Multiple workers close the shared output. | Let only the coordinator close output. |
| Lost cancellation | Workers call slow code that never checks context. | Pass context into blocking operations when possible. |
| Sleep-based tests | Tests guess timing instead of observing state. | Use channels, deadlines, and race/leak checks. |
| Accidental ordering promise | Tests assume output order from concurrent workers. | Document whether order is guaranteed. |

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| `go-concurrency/001-cancellable-fanout-fanin` | Worker lifecycle, output ownership, and cancellation-aware sends. |
| `go-concurrency/002-bounded-queue` | Backpressure, blocked producers, blocked consumers, close semantics, and wakeups. |
| `go-concurrency/003-worker-pool` | Fixed worker budget, bounded job queue, futures, shutdown, and panic handling. |
| Go concurrency project ladder | Reuses the same lifecycle reasoning across crawlers, actors, brokers, and MapReduce. |

## Exercise Bridge

This concept appears in the Go Concurrency Gauntlet and in project ladders that use worker pools, crawlers, MapReduce workers, stream processors, or bounded queues. Before implementing, identify who owns every channel and what happens when the caller stops reading.

## Readiness Checklist

You are ready to implement concurrency exercises when you can:

- identify which goroutine owns closing each channel
- explain what wakes a blocked producer or consumer
- show what happens if downstream stops reading
- distinguish race freedom from leak freedom
- design a test that does not rely on arbitrary sleeps

## Self-Check

1. Who owns closing the output channel?
2. Can a worker block while sending output?
3. What happens if the context is canceled while a worker is computing?
4. Does the API promise output order?
5. What metric would reveal a goroutine leak in production?

## Further Reading

- Go blog, "Go Concurrency Patterns: Pipelines and cancellation": https://go.dev/blog/pipelines
- Go blog, "Go Concurrency Patterns: Context": https://go.dev/blog/context
- Go memory model: https://go.dev/ref/mem
