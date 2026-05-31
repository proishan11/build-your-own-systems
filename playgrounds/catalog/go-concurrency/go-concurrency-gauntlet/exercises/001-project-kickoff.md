# Exercise 001: Go Concurrency Gauntlet First Implementation Lab

Shared concept chapter: [pipelines-and-cancellation.md](../../../../../curriculum/concepts/go-concurrency/pipelines-and-cancellation.md)

## Concept Primer

This first lab turns **Go Concurrency Gauntlet** from a broad project idea into a concrete implementation problem. You are building one narrow mechanism, but you should treat it like production code: name the invariant, make the state explicit, and let the tests describe externally visible behavior.

The implementation target is: Implement the first invariant-preserving core for Go Concurrency Gauntlet.

## Why This Matters

Large systems become learnable when you can isolate a small correctness boundary. A Staff-level engineer does not begin by wiring together a giant demo. They find the smallest behavior that protects the future design, implement it cleanly, and use tests to keep later changes honest.

## Mental Model

A concurrent system is a set of lifetimes. Every producer, worker, and consumer needs a reason to start, a bounded way to make progress, and a reliable way to stop.

For this lab, trace one input through the component: what state is read, what decision is made, what state changes, and what result becomes visible to the caller.

## Core Invariant

After each public operation, the component must preserve this contract: model named resources; reject duplicate resource IDs; update resource state through explicit transitions. If a later feature makes this invariant harder to maintain, the design should expose that tension instead of hiding it in incidental code.

## Tiny Example

Start with the smallest state the tests can exercise. Apply one valid operation and inspect the returned value or stored state. Then apply one boundary operation: a mismatch, duplicate, missing value, limit crossing, malformed input, or unsupported action. The second case is where the invariant usually becomes clear.

## Common Misconceptions

- Passing tests once proves there are no leaks.
- A buffered queue removes the need for cancellation.
- Closing channels from multiple places is harmless.

## Self-Check

Before coding, answer:

1. What state does this component own, and what state is merely input?
2. What is the one condition that must be checked before mutation?
3. What should happen for the boundary case in the tests?
4. What information would you log or expose if this failed in production?

## Goal

Implement the first invariant-preserving core for Go Concurrency Gauntlet.

## Concepts

- goroutine lifecycle
- channels
- cancellation
- backpressure

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- model named resources
- reject duplicate resource IDs
- update resource state through explicit transitions
- record an audit event per transition

## Design Hints

- Identify who owns shutdown.
- Make blocked sends and receives cancellation-aware.
- Use tests to prove no result is lost when work is concurrent.
- Keep the implementation small enough that each test maps to a named behavior, not a side effect.

## Layered Hints

### Hint 1

Write down the state shape first. Most of these labs become straightforward once the data structure reflects the invariant.

### Hint 2

Implement the validation branch before the mutation branch. Rejecting or no-op behavior is often where correctness gets lost.

### Hint 3

After the first passing implementation, reread the tests and remove any accidental coupling to test literals. The code should satisfy the contract, not memorize the examples.

## Validation

Run from `playgrounds/catalog/go-concurrency/go-concurrency-gauntlet`:

```bash
python3 -m unittest discover -s tests -p test_lab.py -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Pipelines and cancellation: ../../../../../curriculum/concepts/go-concurrency/pipelines-and-cancellation.md
- Go blog pipelines: https://go.dev/blog/pipelines

## Staff-Level Review Questions

1. What invariant does this first component protect?
2. What edge case would become a production incident later?
3. What should the next exercise add after this passes?
4. What metric, trace, or audit event would make failures visible?
