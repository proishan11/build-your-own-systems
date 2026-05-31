# Pipelines and Cancellation

## Concept

A pipeline is a sequence of stages connected by channels or queues. Each stage receives values, performs work, and sends results onward. Fan-out lets multiple workers share the same input stream; fan-in merges their results.

## Why It Exists

Pipelines let you express concurrent work without manually assigning every job to every worker. They are useful for I/O-heavy processing, crawlers, batch jobs, stream processors, and request fan-out.

The main danger is lifecycle. Starting goroutines is easy. Stopping them reliably is the real engineering problem.

## Mental Model

Picture a factory line:

```text
input -> [worker worker worker] -> output
```

Every worker repeatedly chooses between:

- take one input item
- notice cancellation and stop
- notice the input is closed and stop

When producing output, the worker must again choose between:

- send the result
- notice cancellation and stop

One coordinator waits for every worker to stop, then closes the output channel.

## Core Invariant

The output channel is closed exactly once, and only after all possible sends are finished.

## Tiny Example

Inputs are `1, 2, 3`. The function squares values. With two workers, the output may arrive as `4, 1, 9` or `1, 9, 4`; order is not guaranteed unless the API promises ordering.

If the context is canceled after one result, fewer outputs are acceptable. Cancellation means the caller no longer needs all results.

## Common Misconceptions

- Buffered channels are not a substitute for cancellation.
- `context.Context` does not kill goroutines; goroutines must check it.
- Every sender should not close the output channel.
- A send can block forever if the receiver stops reading.
- Race-free code can still leak goroutines.

## Self-Check

1. Who owns closing the output channel?
2. What happens if downstream reads only one result and cancels?
3. Can a worker block while sending output?
4. Does this API preserve input order?
5. What metric would reveal a goroutine leak in production?

## Implementation Bridge

For a cancellable fan-out/fan-in `Map`, expect:

- input validation
- a `sync.WaitGroup`
- worker goroutines
- `select` on input and cancellation
- `select` on output send and cancellation
- one closer goroutine

## Further Reading

- Go blog, "Go Concurrency Patterns: Pipelines and cancellation": https://go.dev/blog/pipelines
- Go blog, "Go Concurrency Patterns: Context": https://go.dev/blog/context
- Go memory model: https://go.dev/ref/mem

