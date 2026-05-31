# Exercise 002: Stream Processor State Model and Invariants

Shared concept chapter: [raft-and-replicated-logs.md](../../../../../curriculum/concepts/distributed-systems/raft-and-replicated-logs.md)

## Concept Primer

This exercise deepens **Stream Processor** by adding the next implementation boundary after the starter lab. The focus is not broad feature count; it is building one mechanism that later project milestones can trust.

The implementation target is: Implement the explicit state model that future project features mutate through validated events.

## Why This Matters

A serious systems project becomes understandable when each layer has a contract. This exercise asks you to encode that contract in code and tests before adding more moving parts. That habit is what lets Staff engineers change complex systems without guessing.

## Mental Model

A distributed component is a promise made across unreliable machines. Local state may change only when the protocol evidence says the change remains safe after retry, delay, or partial failure.

For this milestone, draw the component as three boxes: input, owned state, and observable output. Correct code validates the input, mutates only owned state, and returns an output that explains what happened.

## Core Invariant

The component must preserve this contract after every operation: apply events only when their version is newer than the current key version, ignore duplicate event IDs without duplicating audit entries, reject stale events with a clear exception. A later milestone may add scale or distribution, but it must not weaken this invariant.

## Tiny Example

Take one normal operation and one boundary operation from `tests/test_lab_002.py`. Before coding, write the expected state transition by hand. If the expected transition is hard to state in one sentence, simplify the internal representation first.

## Common Misconceptions

- Passing the first happy-path assertion means the component is finished.
- Internal state can be exposed directly because this is only a learning scaffold.
- A retry, replay, duplicate, or malformed input can be handled later without shaping the API now.
- Do not treat a retry as a new operation; identity and idempotency are part of correctness.

## Self-Check

Before coding, answer:

1. What state does this exercise introduce that exercise 001 did not need?
2. Which branch protects the invariant before mutation?
3. What behavior must remain deterministic for review and debugging?
4. What would you measure or log when this component misbehaves?

## Goal

Implement the explicit state model that future project features mutate through validated events.

## Concepts

- replicated state
- quorums
- idempotency
- fault boundaries

## Files To Edit

- `lab_002.py`

## Contract

Your implementation must:

- apply events only when their version is newer than the current key version
- ignore duplicate event IDs without duplicating audit entries
- reject stale events with a clear exception
- return immutable snapshots for reads and audits

## Design Hints

- Keep the representation boring and explicit; clever encodings hide invariants.
- Implement validation and idempotency before optimizing the successful path.
- Prefer deterministic ordering for every returned list, report, or plan.
- Make boundary behavior visible in the return value or exception type.

## Layered Hints

### Hint 1

Start with the data structure that makes the invariant obvious. Most of the code should become simple conditionals over that structure.

### Hint 2

Run the test file directly and implement one assertion at a time. Do not start by trying to satisfy every scenario at once.

### Hint 3

After the tests pass, look for accidental mutation leaks: returned dictionaries and lists should not let callers corrupt internal state.

## Validation

Run from `playgrounds/catalog/distributed-systems/stream-processor`:

```bash
python3 -m unittest discover -s tests -p test_lab_002.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- Raft and replicated logs: ../../../../../curriculum/concepts/distributed-systems/raft-and-replicated-logs.md
- Raft paper: https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro

## Staff-Level Review Questions

1. What invariant did this milestone add or strengthen?
2. Which malformed, duplicate, stale, or partial input should be tested next?
3. How would this implementation behave under replay or retry?
4. What would make this component easier to debug in production?
