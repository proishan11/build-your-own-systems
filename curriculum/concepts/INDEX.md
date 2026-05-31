# Concept Library

This directory contains self-contained teaching chapters. Exercises should link here before asking the learner to implement code.

A concept chapter is not a project description. It should teach the idea well enough that a learner can open an exercise with the right vocabulary, mental model, and invariant already in place.

## Chapter Standard

| Section | Purpose |
| --- | --- |
| What You Should Know First | Names the prerequisite ideas without assuming mastery. |
| The Problem | Explains why the concept exists and what pain it removes. |
| Vocabulary | Defines the terms the learner will see in code, tests, papers, and docs. |
| Mental Model | Gives the learner a simple way to reason about the mechanism. |
| Core Invariant | States the rule that must remain true for the system to be correct. |
| Worked Example | Walks through a small concrete scenario. |
| Implementation Shape | Shows how the idea tends to appear in code without giving full solutions. |
| Failure Modes | Names the traps that make real systems fail. |
| Exercise Bridge | Connects the concept to the scaffolded projects in this repo. |
| Self-Check | Gives questions a learner should answer before coding. |
| Further Reading | Points to deeper references once the mental model is in place. |

## Current Chapters

| Area | Concept | Chapter |
| --- | --- | --- |
| Go Concurrency | Pipelines and Cancellation | [pipelines-and-cancellation.md](go-concurrency/pipelines-and-cancellation.md) |
| Operating Systems | Syscalls, Traps, and Kernel Boundaries | [syscalls-traps-and-kernel-boundaries.md](operating-systems/syscalls-traps-and-kernel-boundaries.md) |
| Networking | Reliable Transport | [reliable-transport.md](networking/reliable-transport.md) |
| Storage | Write-Ahead Logs | [write-ahead-logs.md](storage/write-ahead-logs.md) |
| Storage | WAL Record Formats | [wal-record-format.md](storage/wal-record-format.md) |
| Distributed Systems | Raft and Replicated Logs | [raft-and-replicated-logs.md](distributed-systems/raft-and-replicated-logs.md) |
| AI Agents | RAG, Agents, and Tool Use | [rag-agents-and-tool-use.md](ai-agents/rag-agents-and-tool-use.md) |
| LLM Engineering | Evals, Traces, and Guardrails | [llm-evals-traces-and-guardrails.md](llm-engineering/llm-evals-traces-and-guardrails.md) |
| ML Systems | Autograd and Training Loops | [autograd-and-training-loops.md](ml-systems/autograd-and-training-loops.md) |
| Performance | Profiling and Tail Latency | [profiling-and-tail-latency.md](performance/profiling-and-tail-latency.md) |
| Security | Threat Modeling | [threat-modeling.md](security/threat-modeling.md) |
| Containers/Kubernetes | Reconciliation and Controllers | [reconciliation-and-controllers.md](containers-kubernetes/reconciliation-and-controllers.md) |
| Developer Tools | Unix Pipelines | [unix-pipelines.md](developer-tools/unix-pipelines.md) |
| Developer Tools | Git Object Model | [git-object-model.md](developer-tools/git-object-model.md) |
| PostgreSQL | Administration Mental Model | [postgres-admin-mental-model.md](postgres/postgres-admin-mental-model.md) |

## How To Use These Chapters

Read the concept chapter before the exercise. Then open the exercise and identify which part of the chapter appears in the placeholder code, which invariant the tests are protecting, and which failure mode the exercise is trying to make visible.

When adding a new exercise, either link to an existing chapter or create a new one. Avoid burying the only explanation inside a single exercise file; reusable concepts should live here.
