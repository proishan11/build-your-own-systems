# Exercise 003: LSM Tree KV Store Planning and Ordering

Shared concept chapter: [write-ahead-logs.md](../../../../../curriculum/concepts/storage/write-ahead-logs.md)

## Concept Primer

This exercise is a project-specific implementation milestone for **LSM Tree KV Store**. The work is centered on `plan_lsm_tree_kv_store_compact_runs`, not on a generic scaffold. You will implement behavior for **memtable write** moving through **sstable level** while preserving the project invariant.

The implementation target is: Implement `plan_lsm_tree_kv_store_compact_runs` so LSM Tree KV Store can produce a deterministic compact run plan from desired and observed sstable level state.

## Why This Matters

Real systems fail at their boundaries: malformed input, stale state, partial retries, and misleading metrics. This lab isolates one boundary of LSM Tree KV Store and gives you tests that force the behavior to be explicit. The point is to practice the same discipline you would need before adding scale, concurrency, durability, or distribution.

## Mental Model

Think of this component as a gate around **sstable level**. A **memtable write** arrives, the component decides whether `compact run` is safe, and the result must be deterministic enough to replay, debug, or review later.

The local state should be boring and inspectable. If you cannot explain how `tombstone resurrection` is represented, the implementation is probably hiding a production failure mode.

## Core Invariant

The same desired and observed sstable level states must always produce the same minimal ordered compact run plan.

## Tiny Example

If `sstable-level-primary` is stale, `sstable-level-old` is extra, and `sstable-level-canary` is missing, the plan updates, deletes, then creates in stable order.

## Common Misconceptions

- Treating this as shape validation instead of behavior validation.
- Letting project-specific failures collapse into one generic error path.
- Returning nondeterministic ordering from a planner or scenario runner.
- Exposing mutable internal state to callers and tests.

## Self-Check

Before coding, answer:

1. What state does `plan_lsm_tree_kv_store_compact_runs` own?
2. Which input should be rejected before mutation?
3. How does the test prove the invariant rather than only checking output shape?
4. What would you log or measure if `tombstone resurrection` happened in production?

## Goal

Implement `plan_lsm_tree_kv_store_compact_runs` so LSM Tree KV Store can produce a deterministic compact run plan from desired and observed sstable level state.

## Concepts

- durability
- page layout
- index invariants
- recovery

## Files To Edit

- `lab_003.py`

## Contract

Your implementation must:

- emit update operations for changed resources
- emit delete operations for extra observed resources
- emit create operations for missing desired resources
- sort operations deterministically

## Design Hints

- Compute changed, extra, and missing sets separately.
- Sort names inside each operation group.
- Do not include no-op actions; downstream retries should be minimal.

## Layered Hints

### Hint 1

Start with the expected dictionaries in `test_lab_003.py`. They describe the public contract more precisely than prose.

### Hint 2

Implement the rejection or boundary case before the happy path. That usually reveals the invariant.

### Hint 3

After the tests pass, check that repeated calls with the same input produce the same output and do not mutate caller-owned objects.

## Validation

Run from `playgrounds/catalog/database-systems/lsm-tree-kv-store`:

```bash
python3 -m unittest discover -s tests -p test_lab_003.py
```

## Further Reading

- Shared concept chapter linked at the top of this exercise.
- ARIES paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf

## Staff-Level Review Questions

1. What makes this implementation specific to LSM Tree KV Store, rather than a generic CRUD helper?
2. Which failure mode does `tombstone resurrection` represent in a real deployment?
3. How would retries, replays, or stale state affect this boundary?
4. What additional test would catch an operational incident before users see it?
