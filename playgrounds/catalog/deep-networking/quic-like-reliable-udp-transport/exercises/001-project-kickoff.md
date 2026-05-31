# Exercise 001: QUIC-Like Reliable UDP Transport First Implementation Lab

Shared concept chapter: [reliable-transport.md](../../../../../curriculum/concepts/networking/reliable-transport.md)

## Concept Primer

This first lab turns **QUIC-Like Reliable UDP Transport** from a broad project idea into a concrete implementation problem. You are building one narrow mechanism, but you should treat it like production code: name the invariant, make the state explicit, and let the tests describe externally visible behavior.

The implementation target is: Reassemble ordered stream data from out-of-order frames.

## Why This Matters

Large systems become learnable when you can isolate a small correctness boundary. A Staff-level engineer does not begin by wiring together a giant demo. They find the smallest behavior that protects the future design, implement it cleanly, and use tests to keep later changes honest.

## Mental Model

Packets are small promises. Each header field constrains what the component may do next: accept, drop, forward, translate, acknowledge, or retransmit.

For this lab, trace one input through the component: what state is read, what decision is made, what state changes, and what result becomes visible to the caller.

## Core Invariant

After each public operation, the component must preserve this contract: buffer frames by offset; emit only contiguous bytes; ignore duplicate bytes. If a later feature makes this invariant harder to maintain, the design should expose that tension instead of hiding it in incidental code.

## Tiny Example

Start with the smallest state the tests can exercise. Apply one valid operation and inspect the returned value or stored state. Then apply one boundary operation: a mismatch, duplicate, missing value, limit crossing, malformed input, or unsupported action. The second case is where the invariant usually becomes clear.

## Common Misconceptions

- Forwarding logic can ignore stale or ambiguous state.
- Sequence numbers are just counters.
- Dropping a packet is always an error instead of sometimes the safest action.

## Self-Check

Before coding, answer:

1. What state does this component own, and what state is merely input?
2. What is the one condition that must be checked before mutation?
3. What should happen for the boundary case in the tests?
4. What information would you log or expose if this failed in production?

## Goal

Reassemble ordered stream data from out-of-order frames.

## Concepts

- packet state
- sequence numbers
- routing tables
- failure handling

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- buffer frames by offset
- emit only contiguous bytes
- ignore duplicate bytes
- track next expected offset

## Design Hints

- Write the decision table before coding branches.
- Preserve enough metadata to explain each action.
- Prefer deterministic tie-breaking so tests and incidents are explainable.
- Keep the implementation small enough that each test maps to a named behavior, not a side effect.

## Layered Hints

### Hint 1

Write down the state shape first. Most of these labs become straightforward once the data structure reflects the invariant.

### Hint 2

Implement the validation branch before the mutation branch. Rejecting or no-op behavior is often where correctness gets lost.

### Hint 3

After the first passing implementation, reread the tests and remove any accidental coupling to test literals. The code should satisfy the contract, not memorize the examples.

## Validation

Run from `playgrounds/catalog/deep-networking/quic-like-reliable-udp-transport`:

```bash
python3 -m unittest discover -s tests -p test_lab.py -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Reliable transport concept chapter: ../../../../../curriculum/concepts/networking/reliable-transport.md
- Stanford CS144: https://www.scs.stanford.edu/10au-cs144/

## Staff-Level Review Questions

1. What invariant does this first component protect?
2. What edge case would become a production incident later?
3. What should the next exercise add after this passes?
4. What metric, trace, or audit event would make failures visible?
