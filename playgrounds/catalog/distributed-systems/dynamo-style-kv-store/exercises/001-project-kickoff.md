# Exercise 001: Dynamo-Style KV Store First Implementation Lab

Shared concept chapter: [raft-and-replicated-logs.md](../../../../../curriculum/concepts/distributed-systems/raft-and-replicated-logs.md)

## Concept Primer

This first lab turns **Dynamo-Style KV Store** from a broad project idea into a concrete implementation problem. You are building one narrow mechanism, but you should treat it like production code: name the invariant, make the state explicit, and let the tests describe externally visible behavior.

The implementation target is: Implement vector-clock comparison for conflict detection.

## Why This Matters

Large systems become learnable when you can isolate a small correctness boundary. A Staff-level engineer does not begin by wiring together a giant demo. They find the smallest behavior that protects the future design, implement it cleanly, and use tests to keep later changes honest.

## Mental Model

A distributed component is a promise made across unreliable machines. Local state may change only when the protocol evidence says the change remains safe after retry, delay, or partial failure.

For this lab, trace one input through the component: what state is read, what decision is made, what state changes, and what result becomes visible to the caller.

## Core Invariant

After each public operation, the component must preserve this contract: increment node counters; merge clocks by max counter; classify happens-before. If a later feature makes this invariant harder to maintain, the design should expose that tension instead of hiding it in incidental code.

## Tiny Example

Start with the smallest state the tests can exercise. Apply one valid operation and inspect the returned value or stored state. Then apply one boundary operation: a mismatch, duplicate, missing value, limit crossing, malformed input, or unsupported action. The second case is where the invariant usually becomes clear.

## Common Misconceptions

- A retry is the same as a fresh request.
- Leader code is enough to prove replica safety.
- Passing single-node tests says much about partitions.

## Self-Check

Before coding, answer:

1. What state does this component own, and what state is merely input?
2. What is the one condition that must be checked before mutation?
3. What should happen for the boundary case in the tests?
4. What information would you log or expose if this failed in production?

## Goal

Implement vector-clock comparison for conflict detection.

## Concepts

- replicated state
- quorums
- idempotency
- fault boundaries

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- increment node counters
- merge clocks by max counter
- classify happens-before
- detect concurrent versions

## Design Hints

- Write the safety condition before the mutation.
- Preserve operation identity so retries are explainable.
- Test disagreement, stale state, or duplicate delivery early.
- Keep the implementation small enough that each test maps to a named behavior, not a side effect.

## Layered Hints

### Hint 1

Write down the state shape first. Most of these labs become straightforward once the data structure reflects the invariant.

### Hint 2

Implement the validation branch before the mutation branch. Rejecting or no-op behavior is often where correctness gets lost.

### Hint 3

After the first passing implementation, reread the tests and remove any accidental coupling to test literals. The code should satisfy the contract, not memorize the examples.

## Validation

Run from `playgrounds/catalog/distributed-systems/dynamo-style-kv-store`:

```bash
python3 -m unittest discover -s tests -p test_lab.py -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Raft and replicated logs: ../../../../../curriculum/concepts/distributed-systems/raft-and-replicated-logs.md
- Raft paper: https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro

## Staff-Level Review Questions

1. What invariant does this first component protect?
2. What edge case would become a production incident later?
3. What should the next exercise add after this passes?
4. What metric, trace, or audit event would make failures visible?
