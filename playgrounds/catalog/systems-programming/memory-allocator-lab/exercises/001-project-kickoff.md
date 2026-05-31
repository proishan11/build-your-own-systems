# Exercise 001: Memory Allocator Lab First Implementation Lab

Shared concept chapter: [unix-pipelines.md](../../../../../curriculum/concepts/developer-tools/unix-pipelines.md)

## Concept Primer

This first lab turns **Memory Allocator Lab** from a broad project idea into a concrete implementation problem. You are building one narrow mechanism, but you should treat it like production code: name the invariant, make the state explicit, and let the tests describe externally visible behavior.

The implementation target is: Implement a first-fit allocator over a fixed-size simulated heap.

## Why This Matters

Large systems become learnable when you can isolate a small correctness boundary. A Staff-level engineer does not begin by wiring together a giant demo. They find the smallest behavior that protects the future design, implement it cleanly, and use tests to keep later changes honest.

## Mental Model

Treat the program as a small runtime that owns finite resources. Inputs request state transitions; your implementation decides what changes, what is returned, and what must be cleaned up.

For this lab, trace one input through the component: what state is read, what decision is made, what state changes, and what result becomes visible to the caller.

## Core Invariant

After each public operation, the component must preserve this contract: return stable integer addresses; split free blocks on allocation; coalesce adjacent free blocks on free. If a later feature makes this invariant harder to maintain, the design should expose that tension instead of hiding it in incidental code.

## Tiny Example

Start with the smallest state the tests can exercise. Apply one valid operation and inspect the returned value or stored state. Then apply one boundary operation: a mismatch, duplicate, missing value, limit crossing, malformed input, or unsupported action. The second case is where the invariant usually becomes clear.

## Common Misconceptions

- It is enough for the happy path to work once.
- Parsing and execution can be blurred together without cost.
- Resource cleanup can be added after the behavior is correct.

## Self-Check

Before coding, answer:

1. What state does this component own, and what state is merely input?
2. What is the one condition that must be checked before mutation?
3. What should happen for the boundary case in the tests?
4. What information would you log or expose if this failed in production?

## Goal

Implement a first-fit allocator over a fixed-size simulated heap.

## Concepts

- resource ownership
- explicit state machines
- error boundaries
- deterministic cleanup

## Files To Edit

- `lab.py`

## Contract

Your implementation must:

- return stable integer addresses
- split free blocks on allocation
- coalesce adjacent free blocks on free
- reject double-free and out-of-memory cases

## Design Hints

- Start by representing the smallest state you need explicitly.
- Separate validation from mutation so bad inputs do not half-apply.
- Make cleanup and error paths visible in the return value or state.
- Keep the implementation small enough that each test maps to a named behavior, not a side effect.

## Layered Hints

### Hint 1

Write down the state shape first. Most of these labs become straightforward once the data structure reflects the invariant.

### Hint 2

Implement the validation branch before the mutation branch. Rejecting or no-op behavior is often where correctness gets lost.

### Hint 3

After the first passing implementation, reread the tests and remove any accidental coupling to test literals. The code should satisfy the contract, not memorize the examples.

## Validation

Run from `playgrounds/catalog/systems-programming/memory-allocator-lab`:

```bash
python3 -m unittest discover -s tests -p test_lab.py -p test_lab.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Unix pipelines concept chapter: ../../../../../curriculum/concepts/developer-tools/unix-pipelines.md
- xv6 teaching OS: https://pdos.csail.mit.edu/6.828/2019/xv6.html

## Staff-Level Review Questions

1. What invariant does this first component protect?
2. What edge case would become a production incident later?
3. What should the next exercise add after this passes?
4. What metric, trace, or audit event would make failures visible?
