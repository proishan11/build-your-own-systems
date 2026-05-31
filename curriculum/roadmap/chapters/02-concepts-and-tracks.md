# Roadmap Chapter 2: Concepts and Project Tracks

This chapter is the expansion map: concepts to teach and tracks that can grow into more implementation ladders.

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
