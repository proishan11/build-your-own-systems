# Two-Phase Commit

## What You Should Know First

You should be comfortable with tables, indexes, transactions, pages, query plans, and the difference between logical results and physical execution.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How distributed participants coordinate an atomic commit decision.

In real systems, database engines must produce correct answers while choosing physical strategies under uncertainty and concurrency. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How distributed participants coordinate an atomic commit decision. |
| Plan | A physical strategy for computing a query result. |
| Visibility | The rule that decides which version of a row a transaction may observe. |
| Cost | A model estimate of work, memory, I/O, and cardinality. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of two-phase commit as a layered engine that transforms declarative intent into storage, execution, and transactional behavior.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Parse intent | Convert a query or transaction request into explicit logical operations. |
| Estimate state | Use statistics, visibility rules, and indexes to describe likely work. |
| Choose operators | Pick scans, joins, sorts, locks, or commit protocols. |
| Execute with isolation | Read and write versions according to the transaction contract. |
| Expose evidence | Return rows, errors, plans, locks, or metrics that explain behavior. |
| Test anomalies | Exercise skew, stale stats, concurrent transactions, and partial failures. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For two-phase commit, the invariant is:

> The system must preserve the explicit state contract for how distributed participants coordinate an atomic commit decision, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on two-phase commit. Start with one operation, one state variable, and one failure path.

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
| Query or transaction arrives | SQL, a transaction operation, or a commit request enters the engine. | Logical intent is not yet a physical plan. |
| Metadata is consulted | Catalogs, statistics, indexes, row versions, locks, or participant states are read. | Wrong metadata can still produce legal but terrible behavior. |
| Execution strategy is chosen | The planner or transaction manager selects scans, joins, locks, visibility, or commit rules. | The strategy must preserve result correctness under concurrency. |
| Operators run | Rows are read, joined, filtered, versioned, locked, committed, or aborted. | Memory, I/O, and isolation constraints shape real behavior. |
| Evidence is exposed | Plans, wait events, transaction status, or result rows explain the decision. | Good database debugging starts by asking what the engine thought would happen. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Catalog | Stores table, index, type, and statistics metadata. |
| Planner | Chooses an execution strategy. |
| Executor | Runs operators while respecting memory and transaction state. |
| Transaction manager | Controls visibility, locks, commits, and aborts. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Wrong estimate | A legal plan becomes catastrophically slow. |
| Invisible version leak | A transaction reads data it should not see. |
| Operator assumption mismatch | A join or sort exceeds memory or changes result semantics. |
| Distributed commit ambiguity | Participants disagree about whether a transaction committed. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| database-systems and query-optimizer ladders | Use this chapter before opening project-specific placeholders that rely on two-phase commit. |
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

You are ready to implement an exercise using two-phase commit when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by two-phase commit that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [CMU 15-445](https://15445.courses.cs.cmu.edu/) - Useful once the chapter mental model is clear.
- [PostgreSQL planner docs](https://www.postgresql.org/docs/current/planner-optimizer.html) - Useful once the chapter mental model is clear.
- [Readings in Database Systems](http://www.redbook.io/) - Useful once the chapter mental model is clear.
