# Exercise 004: B+ Tree Insert

Shared concept chapter: [Concept Backlog: B+ Tree Invariants](../../../../curriculum/roadmap/concept-backlog.md)

## Concept Primer

A B+ tree keeps keys ordered and stores values in leaves. Internal nodes guide search. Splits preserve balance when nodes fill.

## Goal

Implement ordered insert and lookup for a small in-memory B+ tree.

## Contract

Edit `internal/btree/btree.go` so it:

- rejects invalid order
- inserts integer keys with string values
- overwrites existing keys
- retrieves values by key
- returns keys in sorted order for range scans
- preserves sorted order after enough inserts to require splits

## Validation

Run:

```bash
go test ./internal/btree
```

## Staff-Level Review Questions

1. What invariant makes search logarithmic?
2. What must be true after a split?
3. How will this change once nodes live on pages?

