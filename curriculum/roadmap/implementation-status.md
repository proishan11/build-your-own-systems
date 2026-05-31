# Implementation Status

This file separates the full curriculum map from the runnable course surface.

## Current State

- Full topic roadmap: complete enough for planning.
- Portable skill: installed and valid.
- Machine-readable manifest: `curriculum/curriculum.json`.
- Course CLI: `tools/learn.py`.
- Runnable project-specific implementation exercise count: 365.
- Foundation exercises: 15.
- Project ladder exercises: 350 across 70 five-exercise ladders.

## Runnable Scaffolds

### Foundation Exercises

| Exercise ID | Status |
| --- | --- |
| `go-concurrency/001-cancellable-fanout-fanin` | scaffolded |
| `go-concurrency/002-bounded-queue` | scaffolded |
| `go-concurrency/003-worker-pool` | scaffolded |
| `tooling/001-unix-pipelines` | scaffolded |
| `tooling/002-git-object-explorer` | scaffolded |
| `tooling/003-minishell-exec` | scaffolded |
| `os/001-syscall-boundary` | scaffolded |
| `os/002-virtual-memory` | scaffolded |
| `networking/001-reliable-transport` | scaffolded |
| `networking/002-ip-router` | scaffolded |
| `database/001-wal-record-format` | scaffolded |
| `distributed/001-local-durable-log` | scaffolded |
| `database/002-slotted-page` | scaffolded |
| `database/003-buffer-pool` | scaffolded |
| `database/004-btree-insert` | scaffolded |

### Project Implementation Ladders

Every project in [Project Catalog](../catalog/project-catalog.md) and its chapter files now has a five-exercise implementation ladder under:

```text
playgrounds/catalog/<track>/<project>/exercises/
```

Each project ladder includes:

1. `001-project-kickoff.md`: core mechanism and first invariant.
2. `002-state-model.md`: explicit state model, deduplication, version checks, and audit history.
3. `003-operation-planner.md`: deterministic desired-vs-observed diff planning.
4. `004-failure-recovery.md`: retry budget, permanent failure, and sticky success behavior.
5. `005-integration-simulation.md`: scenario runner, operational metrics, and invariant reporting.

Each implementation exercise includes:

- a concept primer, mental model, invariant, tiny example, misconceptions, and self-check prompts
- project-specific placeholder code in `lab*.py`
- behavior tests with domain fixtures in `tests/test_lab*.py`
- design hints and layered hints
- further reading
- a manifest entry
- a validation command

These are no longer generic project contracts or one-off starter labs. Each project ladder now has a staged implementation path with project-specific API names, domain fixtures, edge cases, failure modes, and review prompts.

## Expected Validation Behavior

The scaffolds are supposed to fail initially. A clean scaffold failure means:

- tests run
- imports/packages resolve
- failure points at `not implemented`, `TODO`, or a behavior mismatch caused by placeholder code

That is different from a broken scaffold, where tests fail because of missing files, bad paths, syntax errors, or missing dependencies.

## Next Course-Building Milestones

1. Add concept chapters for bounded queues, worker pools, slotted pages, buffer pools, and B+ tree invariants.
2. Add more domain-specific advanced capstones for the most important tracks.
3. Add `tools/learn.py hint` and `tools/learn.py concept` helpers.
4. Add an optional web dashboard once the CLI flow is stable.
