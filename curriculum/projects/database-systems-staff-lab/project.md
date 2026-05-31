# Database Systems Staff Lab

## Purpose

This track teaches database systems by building the core pieces of a small database: durability, storage layout, indexing, buffering, transactions, query execution, and observability.

The goal is not to clone a production database. The goal is to develop the mental model needed to reason about database internals, performance cliffs, correctness guarantees, and operational tradeoffs.

## Learning Format

Every exercise starts with a concept primer before code: the storage or query concept, why it exists, the core invariant, a tiny walkthrough, common misconceptions, self-check questions, and optional papers or articles for depth. Implementation should feel like applying the lesson, not guessing what the tests want.

## Recommended Project Set

### 1. Durable Storage Engine

Build a single-node storage engine with a write-ahead log, page manager, buffer pool, and B+ tree.

Concepts:

- On-disk page formats.
- WAL protocol.
- Checkpoints.
- Crash recovery.
- Buffer replacement.
- B+ tree splits and merges.
- Free space management.

Why this matters:

This teaches the machinery behind durable indexed writes.

### 2. LSM Tree KV Store

Build an LSM-based key-value store.

Concepts:

- Memtables.
- SSTables.
- Bloom filters.
- Sparse indexes.
- Compaction.
- Tombstones.
- Read amplification and write amplification.

Why this matters:

This teaches the tradeoffs behind write-optimized stores such as RocksDB-style systems.

### 3. Mini Relational Query Engine

Build a small SQL-ish engine over your storage layer.

Concepts:

- Logical plans.
- Physical plans.
- Scans, filters, projections, joins, aggregates.
- Cost estimation.
- Iterator/vectorized execution.
- Simple optimizer rules.

Why this matters:

This teaches how declarative queries become executable plans.

### 4. MVCC Transaction Engine

Add multi-version concurrency control.

Concepts:

- Transaction IDs.
- Snapshot isolation.
- Serializable anomalies.
- Write-write conflicts.
- Garbage collection.
- Index visibility.
- Commit protocol.

Why this matters:

This is where storage, concurrency, and semantics collide.

### 5. Observability and Tuning Lab

Build tooling to inspect the database.

Concepts:

- Page inspection.
- WAL decoding.
- Query plan explanation.
- Lock/transaction debugging.
- Compaction statistics.
- Buffer pool hit rate.
- Latency histograms.

Why this matters:

A Staff engineer needs to debug systems from evidence, not vibes.

## Main Capstone: MiniDB

MiniDB is a single-node educational database that evolves from a durable KV store into a small transactional query engine.

### Phase 1: Write-Ahead Log

Build the durability foundation:

- Binary record format.
- Checksums.
- Log sequence numbers.
- Group commit option.
- Recovery scanner.
- Corruption and partial-write handling.

Staff-level questions:

- What promise does `Commit` make?
- What writes must be ordered before acknowledging success?
- How do you test crash points without actually crashing randomly?

### Phase 2: Page Manager

Build fixed-size pages:

- Page IDs.
- Slotted page layout.
- Free space accounting.
- Page allocation and reuse.
- Page checksums.
- Versioned page headers.

Staff-level questions:

- Why are slotted pages useful for variable-length records?
- What on-disk fields are part of compatibility?
- How do you safely evolve the format?

### Phase 3: Buffer Pool

Cache pages in memory:

- Pin and unpin.
- Dirty page tracking.
- LRU or clock replacement.
- Flush policy.
- Read/write latches.
- Metrics for hit rate and dirty pages.

Staff-level questions:

- What prevents evicting a page in active use?
- When can dirty pages be flushed safely relative to WAL?
- What workload defeats LRU?

### Phase 4: B+ Tree Index

Implement ordered indexing:

- Leaf pages.
- Internal pages.
- Search.
- Insert.
- Split.
- Range scan.
- Delete and optional merge/rebalance.

Staff-level questions:

- What invariants must every tree mutation preserve?
- How do you test split cascades?
- How does page size affect fanout and depth?

### Phase 5: Recovery

Implement restart safety:

- Redo.
- Undo or no-steal/no-force simplification.
- Checkpoints.
- Dirty page table.
- Transaction table.
- Idempotent replay.

Staff-level questions:

- What exact state is reconstructed from the WAL?
- Which recovery actions must be idempotent?
- What is the simplest recovery model that still teaches the real tradeoffs?

### Phase 6: Query Execution

Build a small query layer:

- Table scan.
- Index scan.
- Filter.
- Projection.
- Nested-loop join.
- Hash join.
- Aggregation.
- Explain output.

Staff-level questions:

- Where does the iterator model allocate too much?
- How do indexes change the physical plan?
- What statistics would improve plan choice?

### Phase 7: Transactions and MVCC

Add isolation:

- Transaction begin/commit/abort.
- Tuple versions.
- Snapshot reads.
- Write-write conflict detection.
- Vacuum old versions.
- Visibility rules.

Staff-level questions:

- What anomalies does snapshot isolation allow?
- What state determines tuple visibility?
- What happens to long-running readers?

### Phase 8: Performance and Operations

Make behavior inspectable:

- WAL decoder CLI.
- Page dump CLI.
- Query `EXPLAIN`.
- Compaction or vacuum stats.
- Benchmarks for point lookup, range scan, write throughput, recovery time.
- Fault injection for I/O errors.

Staff-level questions:

- What benchmark claim is each benchmark testing?
- Which metric would you alert on?
- How do you debug a slow query from first principles?

## Alternative Capstone: LSMDB

If you want a write-optimized path before B+ trees, build LSMDB:

1. WAL and memtable.
2. Sorted string table format.
3. Sparse index and block index.
4. Bloom filters.
5. Level-0 flush.
6. Leveled compaction.
7. Tombstones and range deletes.
8. Snapshots and iterators.
9. Write stalls and backpressure.
10. Compaction metrics and tuning.

Staff-level tradeoffs:

- Read amplification versus write amplification.
- Space amplification from stale versions.
- Compaction debt.
- Tail latency during background work.
- Iterator correctness across levels.

## Validation Strategy

Use layers:

1. Golden tests for binary formats.
2. Property tests for insert/read/delete sequences.
3. Crash-point tests for WAL and recovery.
4. Concurrency tests for transactions.
5. Differential tests against a simple in-memory model.
6. Benchmarks with documented workload assumptions.

## First Exercise To Scaffold

Start with **WAL Record Format and Recovery Scanner**.

Starter package:

```text
playgrounds/database-systems-staff-lab/minidb/
  internal/wal/
    record.go
    scanner.go
    writer.go
    wal_test.go
  cmd/waldump/
```

Core requirements:

- Encode records with length, type, LSN, payload, and checksum.
- Append records atomically from the caller perspective.
- Scan records in order.
- Stop cleanly at a partial final record.
- Report checksum corruption.
- Preserve enough metadata for redo recovery later.
