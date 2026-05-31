# Exercise 002: Slotted Page

Shared concept chapter: [Concept Backlog: Slotted Pages](../../../../curriculum/roadmap/concept-backlog.md)

## Concept Primer

A slotted page stores variable-length records inside a fixed-size page. Slot metadata grows from one side; record bytes grow from the other. The slot gives records a stable handle even if bytes move during compaction.

## Goal

Implement insertion, lookup, deletion, and free-space tracking for a fixed-size slotted page.

## Contract

Edit `internal/page/slotted_page.go` so it:

- creates a page with fixed capacity
- inserts variable-length records
- returns stable slot IDs
- reads records by slot
- marks slots deleted
- reports not found for deleted slots
- reports no space when a record does not fit

## Validation

Run:

```bash
go test ./internal/page
```

## Staff-Level Review Questions

1. What makes slot IDs stable?
2. What happens to fragmentation after deletes?
3. What metadata must be compatible on disk later?

