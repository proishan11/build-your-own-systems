# Roadmap Chapter 3: Recommended Master Sequence

This chapter gives the recommended order for a learner who wants the most coherent Staff-level progression.

## Recommended Master Sequence

This is the main path for a serious learner.

### Phase 1: Tooling and Local Reasoning

Duration: 4-6 weeks.

Build:

- Unix Pipelines Lab
- Vim Kata Track
- Git Object Explorer
- Cancellable Go Pipeline
- Mini Shell parser and process execution

Review standards:

- can explain stdin/stdout/stderr
- can recover Git mistakes
- can navigate and edit quickly
- can reason about process lifecycle

### Phase 2: Operating Systems and Deep Networking

Duration: 8-12 weeks.

Build:

- Syscall and Trap Lab
- Virtual Memory Simulator
- User-Level Thread Library
- Reliable Transport
- IP Router
- NAT Gateway

Review standards:

- can explain kernel/user boundaries
- validates untrusted pointers and packets
- can reason about page faults and routing failures
- packet loss/reordering tests are deterministic

### Phase 3: Concurrency and Networking Services

Duration: 6-8 weeks.

Build:

- Bounded Queue
- Worker Pool
- Singleflight Cache
- HTTP Server
- TCP Proxy
- Concurrent Web Crawler

Review standards:

- no goroutine leaks
- race detector passes
- graceful shutdown works
- slow clients do not break the system
- backpressure is deliberate

### Phase 4: Storage Internals

Duration: 8-10 weeks.

Build:

- WAL Record Format
- Durable Log
- Slotted Page
- Buffer Pool
- B+ Tree
- Recovery Scanner

Review standards:

- crash tests pass
- binary format is documented
- page/WAL inspectors exist
- benchmarks state what they measure

### Phase 5: Distributed Core

Duration: 10-14 weeks.

Build:

- Failure Simulator
- Raft Leader Election
- Raft Log Replication
- Replicated State Machine
- Snapshots
- Sharded KV

Review standards:

- safety and liveness are separated
- simulations are reproducible by seed
- stale leaders are fenced
- client retries are idempotent

### Phase 6: Security and Performance

Duration: 6-10 weeks.

Build:

- Threat Modeling Lab
- Vulnerable Web App Exploit/Fix
- Secrets Manager
- Supply-Chain Scanner
- Profiler From Scratch
- Tail Latency Lab
- Benchmark Harness

Review standards:

- trust boundaries are explicit
- privileged actions are audited
- tests include exploit/regression cases
- performance changes are measured with comparable workloads
- p95/p99 behavior is visible

### Phase 7: Operations and Cloud Native

Duration: 8-12 weeks.

Build:

- Mini Container Runtime
- OCI Image Builder
- Kubernetes Controller
- Admission Controller
- Postgres Backup/PITR Lab
- Observability Stack

Review standards:

- status surfaces are useful
- RBAC is minimal
- restore drills are tested
- traces, metrics, and logs answer production questions

### Phase 8: ML Systems

Duration: 8-12 weeks.

Build:

- Autograd Engine
- Training Loop
- Checkpointing
- Inference Server
- Distributed Training Simulator
- Feature Store

Review standards:

- gradients are numerically checked
- checkpoints resume correctly
- training and serving metadata are reproducible
- inference latency and queue depth are measured

### Phase 9: AI Systems and LLM Engineering

Duration: 10-14 weeks.

Build:

- RAG From Scratch
- GraphRAG
- Evals Harness
- Prompt and Model Registry
- LLM Trace Store
- Agent Runtime
- MCP Server/Client
- Agent Sandbox and Guardrails

Review standards:

- retrieval and generation are evaluated separately
- tool calls are audited
- mutating actions require approval
- traces are complete
- prompt injection tests exist
- cost/latency is measured

### Phase 10: Capstone Integration

Duration: 8-16 weeks.

Build one integrated system:

```text
AI-assisted incident response platform
```

It should include:

- service deployment on a local Kubernetes cluster
- Postgres-backed state
- RAG over runbooks and incident history
- an agent runtime with safe tools
- observability ingestion
- Git-backed config changes
- approval gates for mutating actions
- simulation of incidents

This capstone ties together systems, databases, distributed systems, security, performance, cloud native, Postgres administration, ML/AI systems, Git, and Unix tooling.
