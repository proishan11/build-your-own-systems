# Write-Ahead Logs

## Concept

A write-ahead log is an append-only record of changes that reaches durable storage before the database or service relies on those changes elsewhere.

## Why It Exists

Complex data structures are hard to update atomically. A B+ tree insert might touch several pages. A replicated log might update indexes and metadata. If the process crashes halfway through, the system needs a simple source of truth to recover from.

The WAL makes recovery possible by turning scattered mutations into an ordered history.

## Mental Model

Think of a WAL as a numbered notebook:

```text
1: put users/1 Alice
2: put users/2 Bob
3: delete users/1
```

On restart, the system rereads the notebook and rebuilds or repairs state.

## Core Invariant

The system must not expose or depend on a change unless the log record needed to recover that change has reached the required durability boundary.

## Tiny Example

If `Append("alpha")` returns index `1`, then after restart, reading index `1` should return exactly `"alpha"` or report a clear storage error. Returning different bytes is silent corruption.

## Common Misconceptions

- A successful `write` syscall does not always mean data is on stable storage.
- The in-memory index is not the source of truth.
- WAL is not only for databases; it is also the backbone of queues, consensus logs, and event stores.
- Recovery must be idempotent because it may replay work that partially happened before the crash.

## Self-Check

1. What exactly is durable after append returns?
2. What can be rebuilt by scanning the log?
3. What happens if the last record is partial?
4. What does `fsync` change?
5. What later features require stable log indexes?

## Further Reading

- ARIES recovery paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf
- Raft paper: https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
- Bigtable paper: https://research.google/pubs/pub27898

