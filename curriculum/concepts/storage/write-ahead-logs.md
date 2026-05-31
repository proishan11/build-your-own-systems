# Write-Ahead Logs

## What You Should Know First

You should know that memory disappears on process crash, files are durable only after the operating system and storage device have accepted the right writes, and complex data structures often require several updates for one logical change.

## The Problem

A storage engine cannot usually update everything atomically. A single insert might modify a table page, an index page, a free-space map, and metadata. If the process crashes halfway through, the system needs a durable record of what it intended to do.

A write-ahead log, or WAL, solves this by recording changes in an append-only history before the system exposes or depends on those changes elsewhere.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Log record | A serialized description of one operation or state change. |
| Log sequence number | A monotonically increasing position in the log. Often abbreviated LSN. |
| Durable boundary | The point at which the system can rely on a record surviving restart. |
| Replay | Reading log records after restart and applying them again. |
| Checkpoint | A point where enough state has been flushed that older log records may no longer be needed for recovery. |
| Idempotence | The property that replaying an operation more than once does not corrupt state. |

## Mental Model

Think of a WAL as a numbered notebook:

```text
1: put users/1 Alice
2: put users/2 Bob
3: delete users/1
```

The in-memory index is convenient, but the notebook is the source that survives a crash. On restart, the system scans the notebook and rebuilds or repairs state.

## Core Invariant

The system must not expose or depend on a change unless the log record needed to recover that change has crossed the required durability boundary.

That boundary might be `fsync`, a group commit batch, a replicated quorum, or another explicit persistence rule. The key is that the boundary must be named and tested.

## Worked Example

Imagine a key-value store with `Put("x", "alpha")`.

| Step | Correct Behavior |
| --- | --- |
| Serialize record | Create a record containing operation type, key, value, and checksum. |
| Append record | Write it to the log at the next LSN. |
| Force durability | Flush according to the API's durability promise. |
| Update index | Point key `x` at the new value or record location. |
| Return success | Only now tell the caller that the write succeeded. |

After restart, key `x` should either recover as `"alpha"` or the append should be reported as not durable. Returning different bytes is silent corruption.

## Implementation Shape

A minimal WAL usually has:

| Component | Responsibility |
| --- | --- |
| Encoder | Turns a record into bytes with length, type, payload, and checksum. |
| Appender | Writes records sequentially and returns a stable position. |
| Sync policy | Decides when to call `fsync` or equivalent. |
| Scanner | Reads records in order and stops cleanly at a torn tail. |
| Recovery loop | Replays committed records into indexes or pages. |

Append-only design is powerful because it turns random mutation into sequential I/O, but the implementation still needs careful framing and recovery rules.

## Failure Modes

| Failure | Why It Matters |
| --- | --- |
| Partial tail record | A crash may leave only half of the final record. Recovery must stop safely. |
| Missing checksum | Corruption can be mistaken for valid data. |
| Index-first update | A crash can expose state that the log cannot recover. |
| Non-idempotent replay | Recovery can duplicate effects after a partial crash. |
| Ambiguous durability | Callers cannot reason about what survives restart. |

## Exercise Bridge

This concept powers the WAL record format, MiniDB storage engine, replicated WAL, queues, event stores, stream processors, and Raft logs. When you open an exercise, first identify the durable boundary and the replay rule.

## Self-Check

1. What exactly is durable when append returns?
2. What can be rebuilt by scanning the log?
3. What should recovery do with a partial final record?
4. What does `fsync` change, and what does it not guarantee?
5. Which later features require stable log indexes?

## Further Reading

- ARIES recovery paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf
- Raft paper: https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
- Bigtable paper: https://research.google/pubs/pub27898
