# Build Your Own Systems

Build Your Own Systems is a curriculum-as-code playground for learning deep computer science and systems engineering by building real projects.

It is designed for learners who want more than interview snippets. Each exercise asks you to learn the concept, implement a missing component, validate behavior, and review the result through correctness, failure, performance, operations, and evolution.

## What You Build

The curriculum covers:

- Go concurrency
- distributed systems
- database systems
- operating systems and kernels
- networking and deep networking
- interpreters and language runtimes
- build systems
- Unix command-line tools
- Vim and Git internals
- PostgreSQL administration
- containers and Kubernetes
- system design and SRE
- security engineering
- performance engineering
- ML systems
- LLM application engineering
- RAG and agent systems

The course currently has 365 runnable, project-specific scaffolded implementation exercises.

They are organized as 15 foundation exercises plus 350 project ladder exercises across 70 five-exercise ladders.

Every exercise follows the same learning contract: a book-like concept section, project-specific placeholder API, behavior tests with domain fixtures, hints, references, and Staff-level review questions. Tests are expected to fail until you implement each solution.

## Quick Start

Requirements:

- Python 3.10 or newer.
- A terminal.
- Go for Go-based tracks.

From the repo root:

```bash
tools/learn.py tracks
tools/learn.py list
tools/learn.py next
```

Open an exercise:

```bash
tools/learn.py show go-concurrency/001-cancellable-fanout-fanin --open exercise
tools/learn.py show go-concurrency/001-cancellable-fanout-fanin --open concept
```

Run its validator:

```bash
tools/learn.py validate go-concurrency/001-cancellable-fanout-fanin
```

The first run should usually fail. That is the point: the repository gives you compiling/importable stubs, tests, and explanations; you implement the behavior.

## Learning Loop

Use this loop for every exercise:

1. Read the exercise markdown.
2. Read the linked concept chapter.
3. Answer the self-check questions.
4. Inspect the placeholder code and tests.
5. Implement the smallest correct behavior.
6. Run the validator.
7. Ask the AI coach for review or hints.
8. Mark the exercise complete when you can explain the invariant and failure mode.

```bash
tools/learn.py complete <exercise-id>
```

Passing tests is necessary, but not sufficient. The goal is to build systems you can reason about under pressure.

## Recommended First Path

If you want the most coherent starting route:

1. Go Concurrency Gauntlet: cancellation, bounded queues, worker pools.
2. Database Systems Staff Lab: WAL records, slotted pages, buffer pools, B+ tree insertions.
3. Distributed Systems Staff Lab: durable logs and replicated-log reasoning.
4. Networking From Scratch: reliable receiver and IP routing.
5. Project ladders: choose RAG, agents, Kubernetes, PostgreSQL, security, performance, or another domain.

Commands:

```bash
tools/learn.py list --track go-concurrency
tools/learn.py next --track go-concurrency
```

## Project Tracks

| Track | Project | Focus |
| --- | --- | --- |
| Go Concurrency | [Go Concurrency Gauntlet](curriculum/projects/go-concurrency-gauntlet/project.md) | Goroutines, channels, cancellation, backpressure, race freedom, leak-free services |
| Distributed Systems | [Distributed Systems Staff Lab](curriculum/projects/distributed-systems-staff-lab/project.md) | Raft, replicated logs, sharding, leases, membership, failure injection |
| Database Systems | [Database Systems Staff Lab](curriculum/projects/database-systems-staff-lab/project.md) | WAL, storage engines, indexes, MVCC, query execution, transactions |

The broader catalog starts at [Project Catalog](curriculum/catalog/project-catalog.md) and continues as book-style chapters under [curriculum/catalog/chapters](curriculum/catalog/chapters/).

Self-contained concept chapters live in [Concept Library](curriculum/concepts/INDEX.md).

The full roadmap lives in:

- [Full Curriculum Plan](curriculum/roadmap/full-curriculum-plan.md), with detailed roadmap chapters under [curriculum/roadmap/chapters](curriculum/roadmap/chapters/)
- [Scaffolding Sequence](curriculum/roadmap/scaffolding-sequence.md)
- [Concept Backlog](curriculum/roadmap/concept-backlog.md)
- [Implementation Status](curriculum/roadmap/implementation-status.md)

## Documentation

Start here:

- [Getting Started](docs/getting-started.md)
- [Learning Workflow](docs/learning-workflow.md)
- [Using the AI Coach](docs/using-the-ai-coach.md)
- [Repository Tour](docs/repo-tour.md)
- [Portable Skill Installation](docs/portable-skill-install.md)
- [npm Package](docs/npm-package.md)
- [Maintainer Guide](docs/maintainer-guide.md)

## AI Coaching Skill

The portable coaching skill lives at:

```text
skills/interactive-learning-coach/
```

It works as a reusable instruction set for Codex, Claude Code, Cursor, Windsurf, and generic coding agents.

Use it with prompts like:

```text
Use $interactive-learning-coach to teach me the concept before the next task.
Use $interactive-learning-coach to give me Hint 1, but do not reveal the full solution.
Use $interactive-learning-coach to explain the approach without code.
Use $interactive-learning-coach to validate and review my implementation.
```

Install instructions are in [Portable Skill Installation](docs/portable-skill-install.md). A full step-by-step usage walkthrough is in [Using the AI Coach](docs/using-the-ai-coach.md).

## Repository Layout

```text
curriculum/   course manifest, concepts, project catalog, roadmap, rubrics
playgrounds/  learner implementation workspaces and tests
skills/       portable AI coaching skill
adapters/     Cursor and generic-agent adapters
docs/         learner and maintainer documentation
tools/        course CLI and scaffold audit tools
dist/         portable release zip
```

See [Repository Tour](docs/repo-tour.md) for details.

## npm Skill Installer

The GitHub repository is the source of truth for the full curriculum. npm is only for installing the portable coaching skill:

```bash
npx build-your-own-systems-skill install codex
```

The package installs `interactive-learning-coach` for Codex, Claude Code, Cursor, Windsurf, or generic agents. It does not distribute the full curriculum codebase.

See [npm Skill Package](docs/npm-package.md) for usage and publishing notes.

## Contributing

Contributions are welcome when they preserve the learning loop: concept first, implementation by the learner, validation, and Staff-level review.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding exercises, tests, docs, or skill changes.

## License

MIT. See [LICENSE](LICENSE).

## Validation Philosophy

On a fresh checkout:

```bash
tools/learn.py validate-all
```

should reach every exercise and report failures. That means the scaffold is healthy and the learner work is still missing.

A good initial failure points at:

- `NotImplementedError`
- `ErrNotImplemented`
- `TODO`
- a focused behavior mismatch

A bad scaffold failure is a missing file, broken import, syntax error, or command that cannot start.

## Staff-Level Learning Contract

Every substantial exercise should make you answer five questions:

1. Correctness: what invariants must never be violated?
2. Failure: what happens on crash, timeout, partition, retry, or partial write?
3. Performance: what is the critical path and where are the bottlenecks?
4. Operations: how would you debug this in production?
5. Evolution: what tradeoffs make this design easier or harder to extend?

That is the curriculum. The code is the laboratory.
