# Exercise 003: Worker Pool

Shared concept chapter: [Pipelines and Cancellation](../../../curriculum/concepts/go-concurrency/pipelines-and-cancellation.md)

## Concept Primer

A worker pool limits concurrency by running submitted jobs on a fixed number of workers. It turns unbounded goroutine creation into a controlled queue plus a fixed execution budget.

## Why This Matters

Without a pool, a burst of requests can create enough work to exhaust memory, file descriptors, or downstream capacity. A pool is one way to make overload explicit.

## Mental Model

```text
submitter -> bounded job queue -> workers -> futures
```

Submitters enqueue work. Workers pull jobs. Futures let callers observe result or failure.

## Core Invariant

Every accepted job completes exactly once with either a value, an error, or a panic converted into an error.

## Self-Check

1. What is the difference between rejecting a job and accepting a job that later fails?
2. Who closes the job queue?
3. What happens to blocked submitters during shutdown?
4. How should panics inside jobs be reported?

## Goal

Implement a bounded worker pool with futures and graceful shutdown.

## Files To Edit

- `workerpool/workerpool.go`

## Contract

Your implementation must:

- reject invalid worker or queue sizes
- accept jobs until shutdown begins
- run at most `workers` jobs concurrently
- return a future for each accepted job
- convert panics into errors
- let callers wait for results with context cancellation
- stop accepting jobs after shutdown

## Validation

Run:

```bash
go test ./workerpool
go test -race ./workerpool
```

## Staff-Level Review Questions

1. What owns worker goroutine lifecycle?
2. Can submit block forever?
3. Can result waiters leak?
4. What metrics would show pool saturation?

