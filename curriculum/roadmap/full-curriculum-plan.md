# Full Curriculum Plan

This plan turns the project catalog into a coherent learning path. The goal is not to finish every project. The goal is to build enough serious systems that the learner develops Staff-level instincts: invariants, failure modes, debugging, operations, and tradeoffs.

## Curriculum Shape

Each module follows the same loop:

```text
Concept mini-chapter
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

## Additional Concepts To Add

### Systems Concepts

- syscalls and libc boundary
- traps and privilege rings
- virtual memory and paging
- file systems and journaling
- process groups and terminals
- signals and async-signal safety
- sockets and TCP lifecycle
- TLS basics
- binary encoding and compatibility
- time, clocks, and timers
- rate limiting and overload control
- scheduling and preemption
- kernel/user copy boundaries

### Concurrency Concepts

- memory models
- lock ordering
- deadlock/livelock/starvation
- wait-free versus lock-free intuition
- actor model
- structured concurrency
- cancellation trees
- backpressure propagation
- deterministic testing

### Database Concepts

- isolation levels
- serializability and anomalies
- predicate locks
- two-phase commit
- distributed transactions
- replication slots
- checkpoints
- vacuum and bloat
- statistics and cardinality estimation
- indexes beyond B+ trees: hash, GIN, GiST, BRIN

### Distributed Systems Concepts

- CAP and PACELC, taught carefully
- consensus versus coordination
- leases and fencing
- vector clocks
- CRDTs
- consistent hashing
- gossip and failure detectors
- split brain
- sagas
- outbox/inbox patterns
- event sourcing
- backfill and migration safety

### Cloud Native Concepts

- Kubernetes API machinery
- reconciliation and finalizers
- owner references and garbage collection
- RBAC and service accounts
- network policies
- CSI/CNI/CRI mental models
- service mesh basics
- OpenTelemetry traces/metrics/logs
- supply-chain security
- SBOMs and image signing
- platform engineering
- FinOps fundamentals

### AI Systems Concepts

- autograd and training loops
- distributed training
- inference serving
- context engineering
- structured outputs
- tool schemas
- guardrails
- agent tracing
- durable agent checkpoints
- sandboxed tool execution
- retrieval evals
- groundedness evals
- synthetic eval generation
- graph retrieval
- memory systems
- model routing
- cost/latency tradeoffs
- AI security and prompt injection
- LLM eval design
- trace stores
- prompt/model registries

### Security Concepts

- threat modeling
- authentication versus authorization
- session security
- encryption and key management
- supply-chain security
- SBOMs and provenance
- sandboxing
- audit logs
- OWASP web and LLM risks

### Performance Concepts

- profiling
- flamegraphs
- tail latency
- queueing theory intuition
- lock contention
- benchmark design
- load shedding
- p50/p95/p99 reporting

### Developer Effectiveness Concepts

- build graphs
- hermeticity
- content-addressed caching
- remote execution
- monorepo scaling
- test selection
- CI/CD design
- release engineering
- feature flags
- migrations
- incident review

## Project Tracks To Add

### Track A: Unix and Tool Mastery

1. Unix Pipelines Lab
2. Coreutils From Scratch
3. Mini Shell With Job Control
4. Vim Kata Track
5. Git Object Explorer
6. Mini Git

Capstone:

- Debug a simulated production incident using only shell, Git, logs, and local tools.

### Track B: Systems Programming

1. Binary Encoding Lab
2. Memory Allocator
3. Event Loop
4. HTTP Server
5. DNS Resolver
6. TCP Proxy/Load Balancer

Capstone:

- Build a small reverse proxy with observability, graceful shutdown, config reload, and overload protection.

### Track C: Operating Systems and Kernels

1. Syscalls and Trap Handling
2. User Pointer Validation
3. Virtual Memory Simulator
4. User-Level Thread Library
5. Scheduler Lab
6. Tiny Journaling File System
7. Process Supervisor

Capstone:

- Extend a teaching kernel or kernel simulator with syscalls, virtual memory, scheduler instrumentation, and crash-consistent filesystem operations.

### Track D: Deep Networking

1. Packet Encoding Lab
2. Reliable Transport
3. IP Router
4. NAT Gateway
5. Dynamic Routing Simulator
6. QUIC-Like Reliable UDP Transport
7. Service Discovery and Health Checking

Capstone:

- Build a small network stack simulator that can route, retransmit, recover from packet loss, and explain every dropped packet.

### Track E: Database Internals

1. WAL Record Format
2. Durable Log
3. Slotted Pages
4. Buffer Pool
5. B+ Tree
6. Recovery
7. Query Execution
8. MVCC
9. LSM Tree Alternative

Capstone:

- MiniDB with `EXPLAIN`, crash recovery tests, page inspector, and benchmarks.

### Track F: Distributed Systems

1. Failure Model Simulator
2. Local WAL
3. Raft Election
4. Raft Log Replication
5. Replicated State Machine
6. Snapshots
7. Membership Changes
8. Sharded KV
9. Queue or Stream Processor

Capstone:

- A sharded replicated KV store with deterministic simulation and Jepsen-style history checking.

### Track G: Security Engineering

1. Threat Modeling Lab
2. Vulnerable Web App Exploit/Fix
3. Auth and Session System
4. Secrets Manager
5. Supply-Chain Scanner
6. Agent Security Lab
7. Sandbox Policy Engine

Capstone:

- Build a security review and policy platform that scans dependencies, threat-models services, audits secrets, and red-teams an agent tool workflow.

### Track H: Performance Engineering

1. Benchmark Harness
2. Profiler From Scratch
3. Flamegraph Lab
4. Tail Latency Lab
5. Lock Contention Lab
6. Load Shedding and Overload Control
7. eBPF-Style Observability Lab

Capstone:

- Diagnose and fix a deliberately slow service using profiles, traces, metrics, histograms, and controlled load tests.

### Track I: Cloud Native Platform Engineering

1. Mini Container Runtime
2. OCI Image Builder
3. Container Registry
4. Kubernetes Controller
5. Admission Controller
6. Scheduler Simulator
7. Postgres Backup Operator
8. Platform API

Capstone:

- A small internal developer platform that deploys services, enforces policy, provisions Postgres backups, and exposes traces/metrics.

### Track J: PostgreSQL Administration

1. Local Cluster Setup
2. Roles/Auth/TLS
3. Backup and Restore
4. PITR
5. Replication
6. Failover Drill
7. Query Tuning
8. Vacuum/Bloat Lab
9. Migration Safety

Capstone:

- Operate a simulated production Postgres service through data loss, slow queries, failover, and restore verification.

### Track K: ML Systems

1. Tensor Library
2. Autograd Engine
3. Training Loop
4. Checkpointing
5. Inference Server
6. Distributed Training Simulator
7. Feature Store
8. Model Registry

Capstone:

- Build a small ML platform that trains, checkpoints, serves, monitors, and rolls back a model with reproducible experiments.

### Track L: AI Systems and RAG

1. Embeddings and Vector Search
2. Hybrid Retrieval
3. Reranking
4. Citation-Grounded Synthesis
5. RAG Evals
6. GraphRAG
7. Agent Runtime
8. Tool Protocol/MCP
9. Guardrails and Sandbox
10. Multi-Agent Workflow

Capstone:

- A support/research agent that uses RAG, tools, durable checkpoints, human approvals, tracing, eval gates, and sandboxed execution.

### Track M: LLM Application Engineering

1. Prompt and Model Registry
2. Structured Output Validator
3. LLM Trace Store
4. Evals Regression Harness
5. Model Router
6. Sandboxed Coding Agent
7. Human Approval Workflow
8. Cost and Latency Dashboard

Capstone:

- Build an LLM application platform with prompt versioning, eval gates, trace search, model routing, tool approvals, and rollback.

### Track N: Build Systems and Developer Platforms

1. Task Graph
2. Incremental Rebuilds
3. Content-Addressed Cache
4. File Watching
5. Remote Cache
6. Test Selection
7. Build Language
8. CI Orchestrator

Capstone:

- A mini Bazel-like build system with remote cache, test selection, and explainable rebuild decisions.

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

## First 30 Scaffolds To Create

These should be generated before expanding further.

1. Go: Cancellable Fan-Out/Fan-In
2. Go: Bounded Queue
3. Go: Worker Pool
4. Unix: Pipeline Exercises
5. Git: Object Model Explorer
6. Shell: Parse and Execute Simple Commands
7. OS: Syscall Boundary Lab
8. OS: Virtual Memory Simulator
9. Networking: Reliable Transport
10. Networking: IP Router
11. Storage: WAL Record Format
12. Storage: Durable Log
13. Storage: Slotted Page
14. Database: Buffer Pool
15. Database: B+ Tree Insert
16. Distributed: Failure Simulator
17. Distributed: Raft Election
18. Distributed: Raft AppendEntries
19. Security: Threat Modeling Lab
20. Security: Vulnerable Web App Exploit/Fix
21. Performance: Benchmark Harness
22. Performance: Tail Latency Lab
23. Containers: Namespace Runner
24. Kubernetes: Reconcile Loop Skeleton
25. Postgres: Backup and Restore Lab
26. ML Systems: Autograd Engine
27. ML Systems: Inference Server
28. RAG: Chunk and Embed Documents
29. Agents: Tool Registry and Trace Log
30. Evals: Retrieval Quality Harness

## What To Build Into Every Exercise

Every scaffold should include:

- concept chapter link
- local primer
- self-check questions
- placeholder implementation
- tests
- validation command
- failure-mode extension
- Staff review questions
- deeper references

## Validation Strategy By Track

### Tooling

- golden tests
- shell transcript tests
- real-tool comparison tests

### Concurrency

- unit tests
- race detector
- leak tests
- stress loop
- benchmarks

### Operating Systems

- syscall boundary tests
- invalid pointer tests
- scheduler/fairness tests
- filesystem crash tests
- kernel invariant checkers

### Networking

- packet golden tests
- loss/reordering simulations
- malformed packet tests
- throughput and latency benchmarks
- route convergence tests

### Storage

- golden binary-format tests
- property tests
- crash-point tests
- corruption tests
- recovery tests

### Distributed Systems

- state-machine unit tests
- deterministic simulation
- partition/restart tests
- history checking
- latency and availability benchmarks

### Security

- exploit reproduction tests
- regression tests for fixes
- authorization matrix tests
- secret-leak scans
- audit-log completeness checks

### Performance

- benchmark baselines
- profiler output checks
- p95/p99 latency tests under load
- contention tests
- regression thresholds

### Kubernetes/Containers

- fake API server tests
- kind/minikube integration tests
- RBAC tests
- reconciliation idempotency tests
- failure injection

### PostgreSQL

- restore verification
- query plan comparison
- load tests
- replication lag simulation
- runbook drills

### AI Systems

- retrieval precision/recall
- groundedness checks
- tool-call audit tests
- prompt-injection tests
- trace completeness checks
- cost/latency benchmarks

### ML Systems

- numerical gradient checks
- checkpoint resume tests
- training/inference parity checks
- batch-size throughput and latency benchmarks
- data leakage tests

### LLM Engineering

- schema validation tests
- eval regression gates
- trace redaction checks
- tool approval tests
- prompt/model rollout tests

## Artifact Standards

Every serious project should produce:

- `README.md` or exercise notes
- design note
- implementation
- tests
- benchmark or simulation
- observability output
- failure-mode report
- next-step reflection

## Publishing Plan

To make this useful outside this repo:

1. Keep the portable skill in `skills/interactive-learning-coach`.
2. Keep concepts in `curriculum/concepts`.
3. Keep project roadmaps in `curriculum/roadmap`.
4. Keep exercises in `playgrounds/<track>/exercises`.
5. Ship adapters for Cursor, Windsurf, Claude, Codex, and generic `AGENTS.md`.
6. Version the curriculum by milestone, not by random file churn.
7. Add a `starter-pack` zip with the skill, concepts, catalog, and first exercise from each major track.

## Source Anchors For Fast-Moving Areas

- OpenAI Agents SDK evolution, sandboxes, files, tool use, memory: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- OpenAI Agents SDK docs: https://openai.github.io/openai-agents-python/
- MCP specification: https://modelcontextprotocol.io/specification/latest
- MCP official docs repository: https://github.com/modelcontextprotocol/modelcontextprotocol
- LangGraph docs: https://docs.langchain.com/oss/python/langgraph
- Microsoft GraphRAG docs: https://microsoft.github.io/graphrag/
- Kubernetes docs: https://kubernetes.io/docs/
- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/
- Kubernetes operator pattern: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- CNCF cloud native survey: https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
- CNCF landscape guide: https://landscapeapp.cncf.io/cncf/guide
- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/coreutils.html
- Git book: https://git-scm.com/book/en/v2
- Vim docs: https://www.vim.org/docs.php
- PostgreSQL admin docs: https://www.postgresql.org/docs/current/admin.html
- xv6 teaching OS: https://pdos.csail.mit.edu/6.828/2019/xv6.html
- Berkeley CS162: https://cs162.org/
- Stanford CS144: https://www.scs.stanford.edu/10au-cs144/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications
- MITRE ATT&CK: https://attack.mitre.org/matrices/enterprise/
- OpenSSF Scorecard: https://openssf.org/scorecard/
- OpenTelemetry docs: https://opentelemetry.io/docs/
