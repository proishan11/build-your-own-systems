# Scaffolding Sequence

This file turns the full curriculum plan into concrete repo work.

## Wave 1: Finish The First Learning Loop

Goal: prove the concept-primer -> placeholder -> validation -> review loop.

Create or complete:

1. Go Cancellable Fan-Out/Fan-In
2. MiniDB WAL Record Format
3. Replicated WAL Local Durable Log

Done means:

- concept chapter exists
- exercise doc links to concept
- placeholder compiles
- tests fail for intended missing behavior
- skill can provide Hint 1/2/3
- validation command is documented

## Wave 2: Tooling Foundations

Goal: add projects that make the learner faster in every later track.

Scaffold:

1. Unix Pipeline Workbench
2. Git Object Explorer
3. Vim Kata Track
4. Mini Shell: command execution

Done means:

- transcript/golden tests exist
- exercises use small datasets
- expected shell/editor/git concepts are explicit

## Wave 3: Concurrency Depth

Goal: deepen Go concurrency before distributed systems.

Scaffold:

1. Bounded Queue
2. Worker Pool
3. Token Bucket Rate Limiter
4. Singleflight Cache
5. Pub/Sub Broker

Done means:

- `go test -race ./...` is part of validation
- at least one cancellation test per exercise
- at least one leak/stress test per component

## Wave 4: Operating Systems and Deep Networking

Goal: add the machine and network substrate before advanced storage/distribution.

Scaffold:

1. Syscall Boundary Lab
2. Virtual Memory Simulator
3. User-Level Thread Library
4. Reliable Transport
5. IP Router
6. NAT Gateway

Done means:

- invalid user inputs are tested
- packet loss/reordering tests are deterministic
- every dropped packet has an explainable reason
- scheduler/page-fault state is inspectable

## Wave 5: Storage Core

Goal: make local durability solid.

Scaffold:

1. Durable Log with partial-write recovery
2. Slotted Page
3. Buffer Pool
4. B+ Tree Search/Insert
5. Recovery Scanner

Done means:

- binary format docs exist
- corruption tests exist
- restart tests exist
- inspector CLI exists for WAL/page data

## Wave 6: Distributed Core

Goal: introduce uncertainty and consensus.

Scaffold:

1. Deterministic Failure Simulator
2. Raft Persistent State
3. Raft Election
4. Raft Log Replication
5. Replicated State Machine

Done means:

- tests are reproducible by seed
- safety invariants are documented
- role/term/commit metrics are exposed

## Wave 7: Security and Performance

Goal: make correctness and speed evidence-driven.

Scaffold:

1. Threat Modeling Lab
2. Vulnerable Web App Exploit/Fix
3. Secrets Manager
4. Supply-Chain Scanner
5. Benchmark Harness
6. Profiler From Scratch
7. Tail Latency Lab

Done means:

- exploit tests exist before fixes
- privileged actions are audited
- performance claims include workload and baseline
- p95/p99 latency is measured

## Wave 8: Cloud Native and Operations

Goal: teach reconciliation, containers, and runbooks.

Scaffold:

1. Mini Container Namespace Runner
2. OCI Image Layout Builder
3. Kubernetes Reconciler Skeleton
4. Admission Controller
5. Postgres Backup/PITR Lab
6. Observability Stack

Done means:

- local dev environment is documented
- failure drills exist
- status/metrics/logging are part of validation

## Wave 9: ML Systems

Goal: teach model training and serving as systems problems.

Scaffold:

1. Autograd Engine
2. Training Loop
3. Checkpointing
4. Inference Server
5. Distributed Training Simulator
6. Feature Store

Done means:

- gradients are numerically checked
- checkpoints resume exactly
- inference exposes latency and queue metrics
- training/serving skew tests exist

## Wave 10: AI Systems and LLM Engineering

Goal: teach modern RAG and agents as production systems.

Scaffold:

1. Document Chunker
2. Embedding and Vector Search Abstraction
3. Hybrid Retrieval
4. Reranker
5. Citation-Grounded Answerer
6. Retrieval Eval Harness
7. Prompt and Model Registry
8. Structured Output Validator
9. LLM Trace Store
10. Tool Registry
11. Agent Trace Log
12. MCP Server/Client
13. Guardrails and Sandbox

Done means:

- retrieval quality is measured separately
- tool calls are logged
- mutating tools require approval
- prompt injection tests exist
- cost/latency is tracked

## Wave 11: Integrated Capstone

Goal: combine tracks into one Staff-level project.

Build:

```text
AI-assisted incident response platform
```

Required subsystems:

- Git-backed runbooks
- RAG over runbooks/incidents
- Postgres state and PITR
- local Kubernetes deployment
- agent tools for read-only diagnostics
- approval-gated mutating tools
- OpenTelemetry traces
- incident simulator

Done means:

- a simulated incident can be detected, investigated, explained, and remediated with human approval
- every action is traceable
- recovery procedures are tested
