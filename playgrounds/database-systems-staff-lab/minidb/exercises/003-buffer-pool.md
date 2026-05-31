# Exercise 003: Buffer Pool

Shared concept chapter: [Concept Backlog: Buffer Pool](../../../../curriculum/roadmap/concept-backlog.md)

## Concept Primer

A buffer pool caches disk pages in memory. Pages are pinned while in use, dirty when modified, and candidates for eviction only when unpinned.

## Goal

Implement a tiny buffer pool with pin/unpin, dirty tracking, eviction, and flush.

## Contract

Edit `internal/buffer/buffer_pool.go` so it:

- fetches pages by ID through a loader callback
- tracks pin counts
- rejects eviction of pinned pages
- marks pages dirty
- flushes dirty pages through a flush callback
- evicts an unpinned page when capacity is full

## Validation

Run:

```bash
go test ./internal/buffer
```

## Staff-Level Review Questions

1. What prevents eviction of a page in active use?
2. When is it safe to flush a dirty page relative to WAL?
3. What workload defeats naive eviction?

