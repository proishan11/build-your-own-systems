# Checksums and Corruption

## What You Should Know First

You should be comfortable with bytes, files, blocks, crashes, checksums, and the difference between memory and durable media.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How systems detect damaged bytes before turning them into trusted state.

In real systems, storage systems must preserve structured data across crashes, partial writes, and future reads. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How systems detect damaged bytes before turning them into trusted state. |
| Page | A fixed-size unit commonly used to organize data on disk or in cache. |
| Durability | The promise that acknowledged data survives the relevant crash model. |
| Recovery | The procedure that rebuilds a valid state after failure. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of checksums and corruption as a set of on-disk promises guarded by explicit formats and recovery rules.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Define the format | Specify headers, lengths, checksums, offsets, and versioning before writing bytes. |
| Choose write order | Decide which record, page, index, or manifest reaches disk first. |
| Track in-memory state | Represent cache residency, dirty state, and pending changes explicitly. |
| Flush deliberately | Use the correct durable boundary for the guarantee you expose. |
| Recover by scanning | Treat the disk as suspect and rebuild from validated structures. |
| Inject corruption | Test torn writes, truncated files, stale pages, and checksum mismatches. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For checksums and corruption, the invariant is:

> The system must preserve the explicit state contract for how systems detect damaged bytes before turning them into trusted state, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on checksums and corruption. Start with one operation, one state variable, and one failure path.

| Moment | Learner Question | Expected Reasoning |
| --- | --- | --- |
| Before the operation | What state is valid right now? | Name the data structure, boundary, or external promise before touching code. |
| During the operation | What can observe a partial change? | Decide whether the change is hidden, visible, retryable, or must be rolled back. |
| After success | What proves the operation completed? | Return a value, write durable state, publish status, emit telemetry, or update a version. |
| After failure | What state is still allowed? | Preserve the invariant and leave enough evidence to retry, recover, or reject. |

This tiny exercise is worth doing before the full project. It turns vague understanding into an implementation contract.

## State Or Flow Walkthrough

| Phase | State/Flow | What To Watch |
| --- | --- | --- |
| Logical request arrives | A record, page, key, write, read, flush, or recovery operation enters the engine. | Separate the logical operation from its physical layout. |
| Format state is decoded | Headers, offsets, checksums, versions, page ids, or free-space metadata are read. | Untrusted bytes must be validated before becoming state. |
| In-memory state changes | Buffers, dirty flags, slots, trees, memtables, or manifests are updated. | Track ownership and mutation order explicitly. |
| Durability boundary is crossed | The implementation writes, fsyncs, checkpoints, compacts, or records recovery evidence. | Expose durability only after the required bytes are safe. |
| Recovery can replay | A scanner or validator can reconstruct a legal state after crash or corruption. | If recovery cannot explain a state, the write path is underspecified. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Encoder | Turns structured state into versioned bytes. |
| Page or record manager | Owns layout, allocation, and lookup. |
| Flush policy | Defines when memory becomes durable enough. |
| Recovery scanner | Reconstructs state from trusted on-disk evidence. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Assuming write atomicity | The disk may expose a prefix, stale sector, or reordered write. |
| No versioning | Future code cannot read old data safely. |
| Cache lies | Tests pass in memory but lose acknowledged data on crash. |
| Unchecked bytes | Corruption becomes valid-looking state. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| database-systems and distributed durable-log ladders | Use this chapter before opening project-specific placeholders that rely on checksums and corruption. |
| Foundation drills | Turn the invariant into one focused test before adding convenience behavior. |
| Staff review | Explain the failure model, the evidence you would inspect in production, and the tradeoff you accepted. |

When you open an exercise, copy the core invariant into your notes. Then find the placeholder function or class that is responsible for preserving it.

## Exercise Bridge

Before coding, write three sentences:

1. The state I own is ...
2. The operation is correct when ...
3. The failure case I must preserve is ...

Those sentences become your implementation plan and your first review checklist.

## Readiness Checklist

You are ready to implement an exercise using checksums and corruption when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by checksums and corruption that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [ARIES paper](https://dl.acm.org/doi/10.1145/128765.128770) - Useful once the chapter mental model is clear.
- [Database Internals](https://www.databass.dev/) - Useful once the chapter mental model is clear.
- [CMU 15-445](https://15445.courses.cs.cmu.edu/) - Useful once the chapter mental model is clear.
