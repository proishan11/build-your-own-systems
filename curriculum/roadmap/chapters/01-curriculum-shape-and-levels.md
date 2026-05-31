# Roadmap Chapter 1: Curriculum Shape and Levels

This chapter explains the learning loop and the level-by-level progression from tool fluency to AI systems and capstones.

## Curriculum Shape

Each module follows the same loop:

```text
Self-contained concept chapter
-> guided reading
-> small exercise
-> implementation milestone
-> tests/validators
-> failure-mode extension
-> Staff-level review
-> reflection
```

Every project should produce a working artifact and a design note.


## Levels

### Level 0: Tool Fluency

Goal: become fast and precise in the environment where all other work happens.

Concepts:

- Unix streams, redirection, exit status, signals
- Vim motions, text objects, quickfix, macros
- Git object model, branches, merge bases, reflog
- Shell scripting and process inspection

Projects:

- Coreutils From Scratch
- Shell Text Processing Workbench
- Vim Kata Track
- Mini Git
- Git Merge and Rebase Lab

Why first:

Staff engineers spend a shocking amount of time moving through code, logs, shells, diffs, and production evidence. Tool fluency compounds.

### Level 1: Local Systems

Goal: understand what a single machine does before distributing it.

Concepts:

- processes, file descriptors, pipes
- memory layout and allocation
- blocking versus nonblocking I/O
- event loops
- protocol parsing
- binary formats

Projects:

- Mini Shell With Job Control
- Memory Allocator Lab
- Event Loop and Async Runtime
- HTTP Server From Scratch
- DNS Resolver

Why here:

Distributed systems are mostly local systems plus uncertainty. If the learner does not understand process lifecycle, I/O, and parsing, distributed failure modes become fog.

### Level 2: Operating Systems and Deep Networking

Goal: understand the kernel and network layers that make higher-level infrastructure possible.

Concepts:

- syscalls and traps
- kernel/user boundaries
- virtual memory
- scheduling
- reliable transport
- packet forwarding
- NAT
- routing convergence

Projects:

- xv6-Style Kernel Lab
- User-Level Thread Library
- Virtual Memory Simulator
- Tiny Journaling File System
- Reliable Transport From Scratch
- IP Router Lab
- NAT Gateway
- Dynamic Routing Simulator

Why here:

Containers, databases, schedulers, and proxies all depend on these primitives. This level removes the mystery from "the OS did it" and "the network dropped it."

### Level 3: Concurrency

Goal: write services that do multiple things at once without leaks, races, or shutdown bugs.

Concepts:

- goroutine ownership
- channel closing
- mutexes and condition variables
- context cancellation
- backpressure
- worker pools
- race detection and stress testing

Projects:

- Go Concurrency Gauntlet
- Concurrent Web Crawler
- TCP Chat Server
- Mini MapReduce Runtime
- Deterministic Stress Harness

Why here:

Concurrency is the bridge between local systems and distributed systems. It teaches lifecycle, coordination, and backpressure in a setting where tests are still relatively cheap.

### Level 4: Storage and Databases

Goal: understand durability, indexing, query execution, and transactions from the inside.

Concepts:

- WAL and recovery
- record formats
- slotted pages
- buffer pools
- B+ trees
- LSM trees
- query planning
- MVCC
- vacuum/compaction

Projects:

- MiniDB Storage Engine
- LSM Tree KV Store
- Query Optimizer Lab
- MVCC Transaction Engine
- WAL/Page/Query Inspector

Why here:

Storage teaches invariants with teeth. Mistakes survive restarts. This is where "tests pass" starts being inadequate unless crash recovery is tested too.

### Level 5: Distributed Systems

Goal: reason about systems where timeouts are ambiguous and machines can disagree.

Concepts:

- failure models
- logical time
- quorum intersection
- consensus
- replication
- sharding
- anti-entropy
- idempotency
- exactly-once myths

Projects:

- Replicated WAL With Raft
- Sharded Replicated KV Store
- Dynamo-Style KV Store
- Gossip Membership and Failure Detector
- Durable Distributed Queue
- Stream Processor
- MapReduce Runtime

Why here:

The learner now has enough local storage and concurrency background to see what consensus is actually protecting.

### Level 6: Security and Performance

Goal: make reliability, safety, and speed evidence-driven rather than vibe-driven.

Concepts:

- threat modeling
- authentication and authorization
- secrets and key rotation
- supply-chain security
- profiling
- tail latency
- lock contention
- benchmark design

Projects:

- Vulnerable Web App Lab
- Auth and Session System
- Secrets Manager
- Supply-Chain Scanner
- Agent Security Lab
- Profiler From Scratch
- Tail Latency Lab
- Benchmark Harness

Why here:

Staff engineers are often trusted with risky changes. They need to know how systems fail under attack, overload, and bad assumptions.

### Level 7: Cloud Native and Operations

Goal: operate systems under realistic platform constraints.

Concepts:

- containers, namespaces, cgroups
- OCI images and registries
- Kubernetes reconciliation
- CRDs and operators
- admission control
- scheduling
- service discovery
- observability
- SLOs
- incident response
- cloud-native security

Projects:

- Mini Container Runtime
- OCI Image Builder
- Container Registry
- Kubernetes Controller From Scratch
- PostgreSQL Backup Operator
- Admission Controller
- Scheduler Simulator
- Observability Stack
- Rate-Limited API Gateway

Why here:

Modern infrastructure work is mostly reconciliation, policy, isolation, telemetry, and operations. The project work should force the learner to debug behavior from evidence.

### Level 8: ML Systems

Goal: understand model training and serving as systems problems.

Concepts:

- tensors
- autograd
- training loops
- checkpointing
- inference serving
- dynamic batching
- distributed training
- feature stores

Projects:

- Autograd Engine
- Mini Deep Learning Framework
- Inference Server
- Distributed Training Simulator
- Feature Store
- Model Registry

Why here:

ML systems are not only algorithms. They are data, checkpoints, serving paths, queues, latency, reproducibility, and operations.

### Level 9: AI Systems, RAG, and Agents

Goal: build AI systems that are measurable, grounded, secure, and operable.

Concepts:

- embeddings and retrieval
- chunking
- reranking
- grounded generation
- evals
- tool use
- agent loops
- durable execution
- human approval
- MCP-style tool protocols
- prompt injection and data exfiltration risks
- tracing and observability for stochastic systems

Projects:

- RAG From Scratch
- Hybrid Search Engine
- GraphRAG Knowledge System
- LLM Evals Harness
- Prompt and Model Registry
- LLM Trace Store
- Agent Runtime
- MCP Server and Client Lab
- Agent Sandbox and Policy Engine
- Multi-Agent Workflow With Human Approval

Why here:

AI systems are now real production systems. The hard parts are not just prompts; they are retrieval quality, tool permissions, traces, evals, sandboxes, and long-running workflow recovery.
