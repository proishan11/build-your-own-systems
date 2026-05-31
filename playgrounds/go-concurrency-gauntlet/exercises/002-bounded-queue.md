# Exercise 002: Bounded Queue

Shared concept chapter: [Pipelines and Cancellation](../../../curriculum/concepts/go-concurrency/pipelines-and-cancellation.md)

## Concept Primer

A bounded queue is a coordination point between producers and consumers. It has finite capacity, so it forces backpressure instead of allowing memory to grow without limit.

## Why This Matters

Most production outages are not caused by a single slow operation. They are caused by queues growing quietly until latency, memory, and retries amplify each other. Bounded queues make overload visible.

## Mental Model

The queue is a room with a fixed number of slots. Producers wait when the room is full. Consumers wait when the room is empty. Closing the queue tells everyone no new items will arrive.

## Core Invariant

No push succeeds after close, and every pushed item is popped at most once.

## Self-Check

1. What happens when the queue is full?
2. What happens when the queue is empty?
3. What does close mean for blocked producers?
4. What does close mean for consumers after the queue is drained?

## Goal

Implement a context-aware bounded queue with `Push`, `Pop`, and `Close`.

## Files To Edit

- `queue/queue.go`

## Contract

Your implementation must:

- reject non-positive capacity
- block producers when full
- block consumers when empty
- unblock operations when context is canceled
- reject pushes after close
- let consumers drain already-pushed items after close
- return `ErrClosed` after the closed queue is drained

## Validation

Run:

```bash
go test ./queue
go test -race ./queue
```

## Staff-Level Review Questions

1. Which goroutine owns queue state?
2. Can a blocked producer stay blocked forever after close?
3. Does the implementation wake all waiters on close?
4. How would you expose queue depth in production?

