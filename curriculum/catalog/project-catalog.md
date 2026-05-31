# Project Catalog

This catalog lists Staff-level learning projects across operating systems, systems programming, networking, security, performance, distributed systems, databases, AI/ML systems, Kubernetes, containers, Unix tooling, Vim, Git, and PostgreSQL administration.

Each project should follow the loop:

```text
Concept chapter -> small exercises -> implementation milestone -> validator -> design review -> failure-mode extension
```

## How To Read This Catalog

- **Foundation:** learn the primitives.
- **Intermediate:** connect primitives into real components.
- **Advanced:** add correctness, recovery, scale, and operations.
- **Capstone:** build a system that forces tradeoffs.

## Systems Programming

### Mini Shell With Job Control

Build a shell that supports parsing, pipelines, redirection, environment variables, signals, foreground/background jobs, and exit statuses.

Teaches:

- processes and file descriptors
- pipes and redirection
- signals
- terminals and process groups
- error propagation

Staff pressure:

- handle `Ctrl-C` correctly
- do not leak child processes
- keep stdout/stderr semantics clean
- test pipeline failures

### Memory Allocator Lab

Build a malloc/free allocator with free lists, splitting, coalescing, alignment, and heap debugging.

Teaches:

- memory layout
- fragmentation
- alignment
- metadata corruption
- debugging low-level systems

Staff pressure:

- detect double free
- expose allocator stats
- benchmark fragmentation patterns
- build a heap consistency checker

### Event Loop and Async Runtime

Build a small event loop over `epoll`/`kqueue` or a portable abstraction.

Teaches:

- nonblocking I/O
- readiness versus completion
- timers
- task scheduling
- backpressure

Staff pressure:

- avoid busy loops
- support cancellation
- instrument event-loop lag
- test slow clients

## Operating Systems and Kernels

### xv6-Style Kernel Lab

Build or extend a small teaching kernel with system calls, traps, virtual memory, scheduling, and a file system.

Teaches:

- privilege boundaries
- traps and syscalls
- page tables
- process lifecycle
- kernel locking
- file system layout

Staff pressure:

- validate user pointers
- avoid kernel panics from user input
- reason about lock ordering
- test fork/exec/wait edge cases

### User-Level Thread Library

Build cooperative then preemptive user-level threads with context switching, stacks, mutexes, condition variables, and a scheduler.

Teaches:

- stacks and registers
- context switching
- scheduling
- synchronization
- preemption hazards

Staff pressure:

- detect deadlocks
- test scheduler fairness
- document signal-safety boundaries
- expose thread state for debugging

### Virtual Memory Simulator

Build a simulator for page tables, TLBs, page faults, replacement policies, copy-on-write, and memory-mapped files.

Teaches:

- address translation
- paging
- TLB behavior
- replacement algorithms
- copy-on-write

Staff pressure:

- explain every page fault
- benchmark replacement policies
- simulate memory pressure
- test permission violations

### Tiny Journaling File System

Build a block-based file system with inodes, directories, free-space management, buffer cache, and a journal.

Teaches:

- block devices
- inode layout
- directories
- crash consistency
- journaling

Staff pressure:

- crash-test metadata updates
- run fsck-style validation
- handle partial writes
- document on-disk compatibility

## Networking

### HTTP Server From Scratch

Build an HTTP/1.1 server with request parsing, keep-alive, routing, static files, chunked encoding, and graceful shutdown.

Teaches:

- protocol parsing
- connection lifecycle
- timeouts
- streaming
- request smuggling risks

Staff pressure:

- fuzz the parser
- handle slowloris-style clients
- separate protocol errors from application errors
- expose connection metrics

### DNS Resolver

Build a recursive-ish resolver with packet encoding/decoding, cache TTLs, retries, and UDP/TCP fallback.

Teaches:

- binary protocols
- caching
- retries and timeouts
- recursive resolution
- negative caching

Staff pressure:

- test malformed packets
- avoid cache poisoning basics
- expose cache hit rate and latency

### Layer 4 Load Balancer

Build a TCP load balancer with health checks, connection draining, least-connections, and consistent hashing.

Teaches:

- proxying
- health checks
- load distribution
- graceful deploys
- observability

Staff pressure:

- handle backend flapping
- preserve half-close behavior
- test under many concurrent connections

## Deep Networking

### Reliable Transport From Scratch

Build a TCP-like protocol over an unreliable packet interface with sequence numbers, ACKs, retransmission, flow control, and congestion-control basics.

Teaches:

- packet loss and reordering
- reliable delivery
- sliding windows
- retransmission timers
- flow versus congestion control

Staff pressure:

- test duplicate/lost/reordered packets
- avoid delivering bytes twice
- model timeouts as uncertainty
- benchmark throughput under loss

### IP Router Lab

Build a router that handles Ethernet frames, ARP, IPv4 forwarding, longest-prefix match, TTL, ICMP errors, and routing-table updates.

Teaches:

- packet forwarding
- ARP
- routing tables
- checksums
- ICMP

Staff pressure:

- test malformed packets
- explain every dropped packet
- avoid routing loops
- expose forwarding counters

### NAT Gateway

Build a NAT that tracks connections, rewrites addresses/ports, expires mappings, and handles TCP/UDP differences.

Teaches:

- connection tracking
- address translation
- ephemeral ports
- timeout policies
- stateful middleboxes

Staff pressure:

- handle port exhaustion
- test mapping expiry
- expose conntrack metrics
- reason about protocols that dislike NAT

### Dynamic Routing Simulator

Build distance-vector and link-state routing simulations with topology changes, route convergence, and failure injection.

Teaches:

- routing protocols
- convergence
- count-to-infinity
- link-state flooding
- failure detection

Staff pressure:

- visualize convergence
- detect routing loops
- compare protocols under churn

### QUIC-Like Reliable UDP Transport

Build a simplified QUIC-inspired transport with streams, connection IDs, retransmission, and handshake state.

Teaches:

- multiplexed streams
- connection migration intuition
- head-of-line blocking
- packet number spaces
- encrypted transport boundaries

Staff pressure:

- isolate stream failures
- test packet reordering
- measure tail latency versus TCP-like design

## Go Concurrency

### Go Concurrency Gauntlet

Build worker pools, cancellable pipelines, bounded queues, singleflight caches, pub/sub brokers, actors, crawlers, and a MapReduce runtime.

Teaches:

- goroutine ownership
- channel closing
- cancellation
- backpressure
- race freedom
- leak detection

Staff pressure:

- run `go test -race`
- add stress tests
- avoid sleep-based tests
- expose goroutine and queue metrics

## Distributed Systems

### Replicated WAL With Raft

Build a local durable log, then replicate it with Raft leader election, log replication, snapshots, and membership changes.

Teaches:

- consensus
- terms and epochs
- quorum commit
- crash recovery
- deterministic simulation

Staff pressure:

- separate safety and liveness
- simulate partitions and restarts
- test stale leaders
- instrument commit lag and election churn

### Dynamo-Style KV Store

Build a highly available key-value store with consistent hashing, sloppy quorums, hinted handoff, vector clocks, and read repair.

Teaches:

- availability/consistency tradeoffs
- conflict resolution
- anti-entropy
- quorum tuning
- operational SLAs

Staff pressure:

- make conflicts visible to clients
- test network partitions
- compare with Raft semantics
- expose divergence metrics

### MapReduce Runtime

Build a local then distributed MapReduce engine with task scheduling, shuffle, retries, speculative execution, and worker failure handling.

Teaches:

- data parallelism
- partitioning
- fault-tolerant execution
- deterministic task outputs
- scheduling

Staff pressure:

- retry idempotently
- handle partial task outputs
- add progress tracking
- benchmark skewed workloads

### Stream Processor

Build a mini Kafka/Flink-like system with partitions, offsets, consumer groups, checkpoints, and windowed aggregation.

Teaches:

- ordered logs
- replay
- consumer offsets
- checkpointing
- event time versus processing time

Staff pressure:

- define delivery semantics
- test rebalances
- handle poison messages
- expose lag and checkpoint age

## Database Systems

### MiniDB Storage Engine

Build WAL, slotted pages, buffer pool, B+ tree, recovery, query execution, and MVCC.

Teaches:

- durability
- storage layout
- indexing
- buffer management
- transactions
- query plans

Staff pressure:

- crash-test recovery
- benchmark point/range queries
- implement `EXPLAIN`
- inspect pages and WAL records

### LSM Tree KV Store

Build memtables, SSTables, Bloom filters, compaction, tombstones, snapshots, and iterators.

Teaches:

- write amplification
- read amplification
- compaction debt
- immutable files
- snapshot consistency

Staff pressure:

- tune compaction
- expose write stalls
- test iterator correctness across levels
- compare against B+ tree tradeoffs

### Query Optimizer Lab

Build a simple SQL planner with table scans, index scans, joins, aggregates, cardinality estimates, and cost-based choices.

Teaches:

- logical and physical plans
- statistics
- join algorithms
- cost models
- plan regressions

Staff pressure:

- show `EXPLAIN`
- create bad-statistics scenarios
- test plan stability
- benchmark join choices

## ML Systems and Deep Learning Infrastructure

### Autograd Engine

Build a tiny tensor library with reverse-mode automatic differentiation, gradient accumulation, and optimizers.

Teaches:

- computation graphs
- chain rule
- tensor operations
- gradient accumulation
- optimizer state

Staff pressure:

- test gradients numerically
- track memory used by saved tensors
- separate training and inference behavior
- benchmark batch-size tradeoffs

### Mini Deep Learning Framework

Build modules, parameters, datasets, dataloaders, training loops, checkpointing, and evaluation metrics.

Teaches:

- model composition
- training loops
- checkpoint formats
- reproducibility
- metrics

Staff pressure:

- resume from checkpoint exactly
- record experiment metadata
- handle bad batches
- compare deterministic and nondeterministic runs

### Inference Server

Build a model-serving API with dynamic batching, request queues, warmup, timeouts, streaming responses, and metrics.

Teaches:

- serving latency
- batching
- queueing
- model lifecycle
- resource management

Staff pressure:

- measure p50/p95/p99 latency
- prevent unbounded queues
- expose batch-size and queue-depth metrics
- handle model reload safely

### Distributed Training Simulator

Build a simulator for data parallel training with gradient aggregation, stragglers, checkpointing, and worker failures.

Teaches:

- data parallelism
- all-reduce intuition
- synchronization cost
- stragglers
- fault recovery

Staff pressure:

- model slow workers
- recover from interrupted checkpoints
- compare synchronous and asynchronous updates

### Feature Store

Build offline and online feature pipelines with point-in-time correctness, backfills, materialization, and serving APIs.

Teaches:

- training/serving skew
- point-in-time joins
- data freshness
- backfills
- feature lineage

Staff pressure:

- test leakage
- expose freshness metrics
- audit feature definitions
- validate backfill safety

### Model Registry

Build a registry for model artifacts, metadata, metrics, lineage, approvals, deployment state, and rollback.

Teaches:

- artifact versioning
- experiment lineage
- model promotion
- reproducibility
- deployment governance

Staff pressure:

- require evaluation before promotion
- track training data lineage
- support rollback
- audit every deployment decision

## LLM Application Engineering

### Prompt and Model Registry

Build a registry for prompts, model configs, schemas, evaluation results, rollout state, and audit history.

Teaches:

- prompt versioning
- model routing
- schema compatibility
- rollout control
- auditability

Staff pressure:

- require evals before promotion
- support rollback
- track cost and latency by version
- prevent unsafe prompt/config combinations

### Structured Output Validator

Build a typed output layer with schemas, repair attempts, validation errors, and fallback policies.

Teaches:

- schema design
- constrained generation
- validation
- retries
- failure semantics

Staff pressure:

- distinguish invalid output from unsafe output
- measure repair success
- avoid infinite retry loops
- preserve raw model output for audit

### LLM Trace Store

Build a trace system for prompts, retrieved context, model calls, tool calls, approvals, outputs, token usage, and latency.

Teaches:

- observability for stochastic systems
- trace trees
- cost attribution
- replay/debuggability
- privacy redaction

Staff pressure:

- redact secrets
- make traces queryable
- connect eval failures to traces
- preserve enough data for incident review

### Sandboxed Coding Agent

Build an agent that can inspect code, plan edits, run tests, and propose patches inside a constrained sandbox.

Teaches:

- agent loops
- tool permissions
- filesystem sandboxing
- test-driven repair
- human approval

Staff pressure:

- block destructive commands by default
- audit every tool call
- recover from interrupted runs
- test prompt-injection attempts from repo files

### Human Approval Workflow

Build a workflow layer where model-suggested actions are reviewed, approved, rejected, or modified by a human.

Teaches:

- approval gates
- action classification
- workflow state
- audit logs
- rollback plans

Staff pressure:

- classify read versus write actions
- expire stale approvals
- show precise diffs before mutation
- preserve decision history

### Model Router

Build a router that chooses models by task, cost, latency, context length, quality tier, and fallback behavior.

Teaches:

- model selection
- fallback policies
- latency/cost tradeoffs
- quality gates
- routing observability

Staff pressure:

- avoid silent quality regressions
- track per-route cost and latency
- test fallback loops
- expose routing explanations

### Cost and Latency Dashboard

Build dashboards and budgets for model calls, tool calls, retrieval, latency percentiles, cache hit rates, and eval pass rates.

Teaches:

- LLM operations
- cost attribution
- latency analysis
- caching
- quality/cost tradeoffs

Staff pressure:

- alert on spend spikes
- connect cost to user/product flows
- separate retrieval latency from model latency
- show regressions by version

## AI, RAG, and Agents

### RAG From Scratch

Build ingestion, chunking, embeddings abstraction, vector search, hybrid search, reranking, answer synthesis, citations, and evals.

Teaches:

- retrieval quality
- chunking tradeoffs
- embedding indexes
- grounding
- eval design

Staff pressure:

- measure retrieval separately from generation
- detect unsupported claims
- track citation precision
- test distractor documents

### GraphRAG Knowledge System

Build entity extraction, relationship extraction, graph construction, community summaries, graph-aware retrieval, and comparison with vector-only RAG.

Teaches:

- graph retrieval
- entity resolution
- global versus local questions
- summarization pipelines
- retrieval evaluation

Staff pressure:

- handle conflicting entities
- measure graph extraction quality
- compare latency/cost with naive RAG
- expose provenance

### Agent Runtime

Build an agent loop with tool registry, typed tool calls, state checkpoints, traces, retries, human approvals, and policy checks.

Teaches:

- tool use
- planning loops
- durable execution
- structured outputs
- human-in-the-loop controls

Staff pressure:

- persist every action
- recover from process crash mid-run
- distinguish read-only and mutating tools
- add red-team tests for prompt injection

### MCP Server and Client Lab

Build a Model Context Protocol server exposing safe tools, then write a client that discovers and invokes them.

Teaches:

- tool protocols
- schemas
- sandboxing
- capability discovery
- trust boundaries

Staff pressure:

- enforce least privilege
- audit tool calls
- sandbox filesystem/network access
- threat-model untrusted tool output

### LLM Evals Harness

Build a harness for golden-answer evals, pairwise judging, retrieval evals, groundedness checks, regression tracking, and cost/latency dashboards.

Teaches:

- eval design
- stochastic systems testing
- model regression
- trace analysis
- quality gates

Staff pressure:

- avoid judging leakage
- separate retrieval and generation failures
- track confidence intervals
- require evals before prompt changes

## Kubernetes

### Kubernetes Controller From Scratch

Build a controller that watches a custom resource and reconciles child resources.

Teaches:

- Kubernetes API model
- watches and informers
- desired versus observed state
- idempotent reconciliation
- status conditions

Staff pressure:

- handle retries safely
- set owner references
- update status clearly
- use minimal RBAC

### Operator for PostgreSQL Backups

Build an operator that schedules backups, records status, verifies restores, and alerts on missed recovery objectives.

Teaches:

- CRDs
- controllers
- backup orchestration
- secrets
- operational runbooks

Staff pressure:

- test restore, not just backup
- handle stuck jobs
- model RPO/RTO
- add disaster-recovery drills

### Admission Controller

Build a validating/mutating admission webhook for image policies, resource limits, labels, and security context.

Teaches:

- admission flow
- policy enforcement
- TLS/webhooks
- failure policy
- cluster security

Staff pressure:

- avoid blocking the cluster during outages
- report actionable errors
- test policy bypass attempts

### Scheduler Simulator

Build a scheduler that assigns pods to nodes using resource requests, affinity, taints, topology spread, and preemption.

Teaches:

- bin packing
- constraints
- fairness
- preemption
- scheduling explainability

Staff pressure:

- show why scheduling failed
- simulate large clusters
- test fragmented capacity

## Containers

### Mini Container Runtime

Build a runtime using Linux namespaces, cgroups, mounts, capabilities, seccomp, and an OCI-style bundle.

Teaches:

- process isolation
- filesystem isolation
- resource limits
- container lifecycle
- security boundaries

Staff pressure:

- drop capabilities
- isolate mounts
- enforce memory/CPU limits
- explain what is not isolated

### OCI Image Builder

Build a simple image builder that creates layers, config, manifests, and content-addressed blobs.

Teaches:

- image layers
- digests
- registries
- reproducibility
- caching

Staff pressure:

- make builds reproducible
- verify digests
- implement layer cache invalidation

### Container Registry

Build a small OCI-compatible registry subset with blob upload, manifest push/pull, auth, and garbage collection.

Teaches:

- content-addressed storage
- HTTP APIs
- auth
- garbage collection
- distribution semantics

Staff pressure:

- handle interrupted uploads
- prevent deleting referenced blobs
- expose storage metrics

## Unix Command Line

### Coreutils From Scratch

Implement `cat`, `head`, `tail`, `wc`, `sort`, `uniq`, `grep`, `xargs`, and `find` subsets.

Teaches:

- streams
- file traversal
- text processing
- exit status
- POSIX-ish behavior

Staff pressure:

- handle binary input
- preserve stdout/stderr contracts
- test large files
- compare behavior with real tools

### Shell Text Processing Workbench

Create exercises where the learner solves log analysis, CSV cleanup, filesystem audits, and process inspection using pipelines.

Teaches:

- composability
- quoting
- redirection
- pipes
- debugging shell scripts

Staff pressure:

- write reproducible scripts
- handle filenames with spaces
- use `set -euo pipefail` responsibly

## Vim

### Vim Kata Track

Build a series of editing challenges covering motions, text objects, macros, registers, marks, windows, quickfix, substitutions, and help navigation.

Teaches:

- modal editing
- composable commands
- repeatability
- editor-as-language

Staff pressure:

- optimize edit sequences
- explain command composition
- use quickfix for project-scale edits

### Vim Plugin From Scratch

Build a small plugin: project notes, test runner, quickfix helper, or text-object extension.

Teaches:

- Vimscript or Lua basics
- buffers/windows
- mappings
- commands
- help docs

Staff pressure:

- write `:help` documentation
- avoid clobbering user mappings
- test with minimal config

## Git

### Mini Git

Implement `init`, `hash-object`, `cat-file`, `write-tree`, `commit-tree`, branches, checkout, diff, merge basics, and status.

Teaches:

- content-addressed storage
- commit graphs
- trees/blobs
- index
- branching

Staff pressure:

- explain every object written
- handle file mode and path edge cases
- visualize the graph

### Git Merge and Rebase Lab

Build exercises around conflict resolution, merge bases, rebasing, reflog recovery, bisect, and blame.

Teaches:

- DAG reasoning
- history rewriting
- conflict mechanics
- recovery

Staff pressure:

- recover from bad rebase
- explain why a conflict happened
- write safe team workflows

## PostgreSQL Administration

### Backup and PITR Lab

Build a PostgreSQL environment with base backups, WAL archiving, point-in-time recovery, and restore verification.

Teaches:

- backups
- WAL archiving
- RPO/RTO
- restore drills
- disaster recovery

Staff pressure:

- prove restore works
- simulate data loss
- document a runbook
- alert on broken archiving

### Query Performance Lab

Create datasets and bad queries, then diagnose with `EXPLAIN`, indexes, statistics, vacuum, and configuration.

Teaches:

- query planning
- indexes
- statistics
- bloat
- wait events

Staff pressure:

- measure before tuning
- avoid cargo-cult indexes
- explain plan changes
- protect write performance

### Replication and Failover Lab

Build primary/replica streaming replication, monitor lag, perform failover, and validate client behavior.

Teaches:

- streaming replication
- timelines
- lag
- failover
- consistency tradeoffs

Staff pressure:

- simulate primary loss
- prevent split brain
- document promotion workflow
- test application retry behavior

## System Design and SRE

### Rate-Limited API Gateway

Build an API gateway with auth, rate limits, circuit breakers, request hedging, retries, and observability.

Teaches:

- overload control
- fairness
- tail latency
- failure containment
- idempotency

Staff pressure:

- avoid retry storms
- define per-tenant fairness
- test dependency outages

### Observability Stack

Build metrics, logs, traces, RED/USE dashboards, alerts, and incident notebooks around one of the systems above.

Teaches:

- telemetry
- alert design
- tracing
- SLOs
- incident response

Staff pressure:

- alert on symptoms, not noise
- make debugging paths obvious
- run game days

### Feature Flag and Rollout System

Build flags, targeting, gradual rollout, kill switches, audit logs, and experiment analysis.

Teaches:

- configuration distribution
- consistency
- blast-radius control
- auditability
- product experimentation

Staff pressure:

- handle stale clients
- support emergency rollback
- prevent unsafe flag combinations

## Security Engineering

### Vulnerable Web App Lab

Build a deliberately vulnerable application, exploit it, then fix it with tests.

Teaches:

- injection
- broken access control
- session flaws
- insecure deserialization
- security regression testing

Staff pressure:

- write exploit proofs
- add tests that prevent reintroduction
- log security-relevant events
- document trust boundaries

### Auth and Session System

Build authentication, password storage, sessions, CSRF protection, MFA hooks, and authorization checks.

Teaches:

- identity
- password hashing
- sessions
- authorization
- CSRF/XSS boundaries

Staff pressure:

- rotate sessions on privilege change
- test confused-deputy cases
- audit admin actions
- model account recovery risk

### Secrets Manager

Build a local secrets manager with envelope encryption, access policies, audit logs, rotation, and lease-based credentials.

Teaches:

- encryption at rest
- key hierarchy
- access control
- rotation
- auditability

Staff pressure:

- prevent plaintext leaks in logs
- implement least privilege
- test rotation failure modes
- model compromise recovery

### Supply-Chain Scanner

Build a scanner that reads dependency manifests, checks known-vulnerability feeds, verifies checksums/signatures, and emits policy results.

Teaches:

- dependency metadata
- vulnerability matching
- provenance
- SBOMs
- policy-as-code

Staff pressure:

- distinguish vulnerable from reachable
- handle false positives
- generate actionable reports
- gate builds with explainable policy

### Agent Security Lab

Build attacks and defenses for prompt injection, tool abuse, data exfiltration, malicious documents, and unsafe tool outputs.

Teaches:

- LLM threat models
- tool trust boundaries
- retrieval poisoning
- sandboxing
- approval gates

Staff pressure:

- add red-team fixtures
- separate untrusted data from instructions
- require approval for mutating tools
- trace every security decision

## Performance Engineering

### Profiler From Scratch

Build a sampling profiler that captures stack traces, aggregates hot paths, and renders a simple flamegraph-like report.

Teaches:

- sampling
- stack unwinding intuition
- CPU attribution
- profiler overhead
- visualization

Staff pressure:

- measure profiler overhead
- compare sampled versus instrumented timing
- handle short-lived functions
- make results reproducible

### Tail Latency Lab

Build a service with controlled sources of latency: queues, locks, GC pressure, slow dependencies, and retry storms.

Teaches:

- p50/p95/p99
- queueing
- contention
- load shedding
- timeout budgets

Staff pressure:

- show histograms
- isolate root causes
- prevent coordinated retry storms
- validate improvements under load

### Lock Contention Lab

Build workloads around global locks, sharded locks, lock-free-ish structures, and read/write locks.

Teaches:

- contention
- critical sections
- fairness
- starvation
- profiling locks

Staff pressure:

- prove contention with evidence
- benchmark under varying cores
- explain throughput versus latency
- avoid premature cleverness

### Benchmark Harness

Build a harness for repeatable benchmarks, warmup, workload definitions, confidence intervals, and regression reports.

Teaches:

- experimental design
- workload modeling
- variance
- regression detection
- performance reporting

Staff pressure:

- record environment metadata
- detect noisy runs
- compare against baselines
- prevent benchmark gaming

### Observability With eBPF Concepts

Build a lab that traces syscalls, network connections, latency, and process behavior using available platform tooling or simulated eBPF probes.

Teaches:

- kernel-level observability
- low-overhead tracing
- syscall visibility
- production debugging

Staff pressure:

- minimize overhead
- avoid leaking sensitive data
- connect low-level signals to user-visible symptoms

## Recommended Staff-Level Path

1. Unix pipelines, Vim, Git, and mini shell.
2. Operating systems: syscalls, virtual memory, user-level threads.
3. Deep networking: reliable transport, router, DNS, proxy.
4. Go Concurrency Gauntlet.
5. MiniDB WAL and storage engine.
6. Replicated WAL with Raft.
7. Security engineering and threat modeling labs.
8. Performance engineering and observability labs.
9. RAG From Scratch and LLM evals/traces.
10. Agent Runtime with MCP tools and sandboxing.
11. Mini container runtime.
12. Kubernetes controller/operator.
13. PostgreSQL backup/PITR and query performance labs.
14. Integrated incident-response capstone.

This path builds from local correctness to distributed correctness to operational judgment.
