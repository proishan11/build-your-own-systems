# Getting Started

This repository is a curriculum-as-code playground. You learn by reading a self-contained concept chapter, implementing missing code, running validators, and asking an AI coach for hints or review.

The curriculum is intentionally scaffolded. Most tests fail at first because the implementation is yours to write.

## What You Need

Required:

- Python 3.10 or newer.
- A terminal.
- A code editor.

Useful as you enter specific tracks:

- Go, for Go concurrency, database, distributed-system, and storage exercises.
- Rust, for Rust interpreter/runtime extensions when you add or expand those tracks.
- Git, for repo workflows and the Git object-model exercises.

Most project ladder exercises use Python-only stubs so you can start immediately.

## The Learning Plan

Read [Self-Contained Learning Plan](../curriculum/learning-plan.md) when you want the full path. It explains the phase order, the concept chapters to read, representative exercises, and the evidence you should produce before moving on.

## First Five Minutes

From the repo root:

```bash
tools/learn.py tracks
tools/learn.py list
tools/learn.py next
```

If you install the coaching skill from npm:

```bash
npx build-your-own-systems-skill install codex
```

You still need the curriculum repository locally to work through the exercises.

Open the next exercise:

```bash
tools/learn.py show go-concurrency/001-cancellable-fanout-fanin --open exercise
```

Run its validator:

```bash
tools/learn.py validate go-concurrency/001-cancellable-fanout-fanin
```

The validator should fail. That is correct. A good initial failure points at a placeholder, `NotImplementedError`, or a behavior mismatch in code you are expected to implement.

## Recommended First Path

If you want the most coherent path through the curriculum, start here:

1. Go Concurrency Gauntlet: cancellation, bounded queues, worker pools.
2. Database Systems Staff Lab: WAL records, slotted pages, buffer pools, B+ tree insertions.
3. Distributed Systems Staff Lab: durable logs and replicated-log reasoning.
4. Networking From Scratch: reliable receiver and IP routing.
5. Project ladders: choose a domain such as RAG, Kubernetes controllers, PostgreSQL operations, security, or performance.

Use:

```bash
tools/learn.py list --track go-concurrency
tools/learn.py next --track go-concurrency
```

## Understanding The Course Size

The curriculum currently has 365 runnable, project-specific scaffolded implementation exercises.

They are organized as 15 foundation exercises plus 350 project ladder exercises across 70 five-exercise project ladders.

Each project ladder has the same shape:

1. Core mechanism and first invariant.
2. State model and invariants.
3. Operation planner and deterministic diffs.
4. Failure, retry, and recovery boundary.
5. Integration simulation and operational report.

That common shape is deliberate. It lets you practice the same Staff-level reasoning loop across many domains.

## The Daily Loop

For each exercise:

1. Read the exercise markdown.
2. Read the linked concept chapter.
3. Answer the self-check questions in your own words.
4. Inspect the placeholder code and tests.
5. Implement the smallest behavior that satisfies the contract.
6. Run the validator.
7. Ask for a review, not just a solution.
8. Mark it complete when you can explain the invariant and the failure mode.

Commands:

```bash
tools/learn.py show <exercise-id> --open exercise
tools/learn.py show <exercise-id> --open concept
tools/learn.py validate <exercise-id>
tools/learn.py complete <exercise-id>
```

## Expected Failures

`tools/learn.py validate-all` is a scaffold health check, not a course completion check.

On a fresh checkout, it should reach every exercise and report failures because the learner stubs are intentionally unimplemented. That means:

- files exist
- imports resolve
- validators run
- failures point at learner work

Broken scaffold failures are different: missing files, syntax errors, import path errors, or commands that cannot start.

## Using An AI Coach

Install the portable skill or use the generic adapter, then ask:

```text
Use $interactive-learning-coach to teach me the concept for the next task before I code.
Use $interactive-learning-coach to give me Hint 1, but do not reveal the full solution.
Use $interactive-learning-coach to validate my implementation and review it like a Staff engineer.
```

See [Using the AI Coach](using-the-ai-coach.md) and [Portable Skill Installation](portable-skill-install.md).
