# Consistent Hashing

## What You Should Know First

You should be comfortable with RPCs, clocks, retries, logs, replicas, and the fact that networks can delay, drop, duplicate, and partition messages.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How systems distribute keys while minimizing movement as membership changes.

In real systems, distributed systems must make progress without assuming one machine has a complete or current view of reality. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How systems distribute keys while minimizing movement as membership changes. |
| Replica | A node that stores or computes part of the system state. |
| Quorum | A set of participants large enough to preserve an intersection guarantee. |
| Partition | A communication failure where some nodes cannot exchange messages. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of consistent hashing as several state machines coordinating through messages, quorums, leases, or replicated logs.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| State assumptions | Name the failure model, clock assumptions, and messages the protocol can rely on. |
| Choose coordination state | Represent terms, versions, vector clocks, membership, leases, or hash ranges explicitly. |
| Send guarded messages | Attach enough metadata for receivers to reject stale or unsafe work. |
| Commit by rule | Advance visible state only when the protocol invariant is satisfied. |
| Recover after ambiguity | Treat retries, duplicate messages, and old leaders as normal cases. |
| Simulate the network | Test partitions, delayed messages, crashes, restarts, and reordering. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For consistent hashing, the invariant is:

> The system must preserve the explicit state contract for how systems distribute keys while minimizing movement as membership changes, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on consistent hashing. Start with one operation, one state variable, and one failure path.

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
| Local event occurs | A client request, timer, message, crash, restart, or membership change reaches one node. | Local observation is not global truth. |
| Metadata is compared | Terms, epochs, vector clocks, leases, versions, or membership views are checked. | Stale authority must be rejected before side effects. |
| Coordination rule runs | The protocol applies quorum, retry, fencing, hashing, or gossip rules. | The rule must hold under delay, duplication, and partition. |
| State becomes visible | A write commits, owner changes, conflict is recorded, or membership converges. | Visibility should follow the protocol invariant, not local optimism. |
| Ambiguity is handled | Retries, old messages, crashed nodes, and split views are reconciled. | The implementation should make uncertainty explicit instead of hand-waving it away. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Node state | Persistent and volatile fields needed for protocol decisions. |
| Message handlers | Validate metadata before mutating local state. |
| Commit rule | The exact condition that makes an action visible. |
| Simulator | Controls delivery, crashes, restarts, and clocks. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Assuming clocks are truth | Local time can be skewed, paused, or delayed. |
| Retry without idempotency | A safe-looking retry performs the operation twice. |
| No fencing | An old leader or owner continues to mutate state. |
| Testing only synchrony | The design collapses under partitions and reorderings. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| distributed-systems ladders and database replication projects | Use this chapter before opening project-specific placeholders that rely on consistent hashing. |
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

You are ready to implement an exercise using consistent hashing when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by consistent hashing that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [Raft paper](https://raft.github.io/raft.pdf) - Useful once the chapter mental model is clear.
- [Designing Data-Intensive Applications](https://dataintensive.net/) - Useful once the chapter mental model is clear.
- [The Morning Paper distributed systems archive](https://blog.acolyer.org/category/distributed-systems/) - Useful once the chapter mental model is clear.
