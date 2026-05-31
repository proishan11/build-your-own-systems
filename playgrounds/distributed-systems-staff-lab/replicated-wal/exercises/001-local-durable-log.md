# Exercise 001: Local Durable Log

Shared concept chapter: [Write-Ahead Logs](../../../../curriculum/concepts/storage/write-ahead-logs.md)

## Concept Primer

A write-ahead log is an append-only history of changes. Instead of mutating complex state directly and hoping every structure reaches disk consistently, the system first records the intended change in a simple sequential format.

For this first exercise, the log is not replicated yet. That is deliberate. Consensus becomes much easier when the local storage layer has a clear durability contract.

## Why This Matters

Replicated systems depend on logs. Raft replicates a log. Databases recover from a log. Queues replay from a log. If the local log can lose, reorder, or misread entries, every distributed guarantee built on top becomes suspect.

## Mental Model

Imagine a notebook where each line is numbered:

```text
1: append "alpha"
2: append "beta"
3: append "gamma"
```

On restart, the system rereads the notebook and rebuilds the table of contents. If the final line was only half-written during a crash, recovery should ignore or reject that incomplete tail rather than inventing data.

## Core Invariant

If `Append` returns index `N` successfully, then later reads should either return the exact payload for `N` or report a storage-level corruption/error. It must not silently return different bytes.

## Tiny Example

Append `alpha`, then append `beta`. The log returns indexes `1` and `2`. After closing and reopening the log, reading index `1` should still return `alpha`, and reading index `2` should still return `beta`.

## Common Misconceptions

- An append-only file is not automatically durable; OS page cache and `fsync` policy matter.
- The in-memory index is a convenience, not the source of truth.
- A successful write call does not always mean data is on stable storage.
- Recovery should be intentionally boring: scan, validate, rebuild indexes.

## Self-Check

Before coding, answer:

1. What is the durable source of truth?
2. What state can be rebuilt during `Open`?
3. What should happen if an index is missing?
4. What will change later when checksums and segment files are added?

## Goal

Build the single-node durable log that will later become the storage layer for a replicated Raft log.

## Concepts

- Append-only files.
- Monotonic log indexes.
- Length-prefixed records.
- Checksums.
- Crash recovery.
- Partial-write detection.

## Files To Edit

- `internal/wal/log.go`

## Contract

Your implementation must:

- Open or create a log directory.
- Append binary payloads and return monotonically increasing indexes starting at 1.
- Read payloads back by index.
- Persist entries across `Close` and `Open`.
- Detect missing indexes.
- Be structured so record checksums and segment rotation can be added next.

## Design Hints

Start deliberately simple:

- One data file is acceptable for this exercise.
- An in-memory index rebuilt on startup is acceptable.
- Use a binary record format with length and payload.
- Keep the public API stable so future exercises can add checksums, segments, and truncation.

Do not jump to Raft yet. Raft will be much easier once the local durability boundary is boring.

## Validation

Run from `playgrounds/distributed-systems-staff-lab/replicated-wal`:

```bash
go test ./...
```

## Further Reading

- Raft paper, "In Search of an Understandable Consensus Algorithm": https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
- Raft resources and visualizations: https://raft.github.io/
- ARIES recovery paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf

## Staff-Level Review Questions

1. What exactly is durable after `Append` returns?
2. What state must be rebuilt during `Open`?
3. What happens if the process crashes halfway through a record?
4. What API changes would become painful once Raft depends on this package?
