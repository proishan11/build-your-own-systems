# Project Map

Use this as the curriculum expansion map.

## Go Concurrency Gauntlet

Purpose: teach production-grade concurrent Go.

Exercise ladder:

1. Cancellable fan-out/fan-in.
2. Bounded queue.
3. Worker pool.
4. Token bucket rate limiter.
5. Singleflight cache.
6. Pub/sub broker with slow-consumer policy.
7. Actor mailbox.
8. Concurrent LRU cache.
9. Concurrent web crawler.
10. TCP chat server.
11. Streaming proxy.
12. Mini MapReduce runtime.
13. Work-stealing scheduler.
14. Deterministic stress harness.

## Distributed Systems Staff Lab

Purpose: teach replicated systems and failure reasoning.

Exercise ladder:

1. Local durable WAL.
2. Network transport and deterministic simulator.
3. Raft leader election.
4. Raft log replication.
5. Client append semantics and idempotency.
6. Snapshots and compaction.
7. Membership changes.
8. Operational hardening.

Expansion projects:

- sharded replicated KV store
- gossip membership and failure detector
- durable distributed queue
- distributed lock and lease service

## Database Systems Staff Lab

Purpose: teach storage engines, query execution, and transactions.

Exercise ladder:

1. WAL record format and scanner.
2. Page manager.
3. Buffer pool.
4. B+ tree.
5. Recovery.
6. Query execution.
7. MVCC transactions.
8. Observability and tuning.

Expansion projects:

- LSM tree KV store
- mini relational query engine
- MVCC transaction engine
- WAL/page/query inspection tools

## Crafting Interpreters

Purpose: learn language implementation from tree-walk interpreters to bytecode VMs.

Suggested path:

1. Part 1 in Python: scanner, parser, AST, interpreter, functions, closures, classes.
2. Part 2 in Rust: bytecode chunks, VM, stack, compiler, closures, GC.

## Networking From Scratch

Purpose: learn protocols, framing, and service behavior.

Suggested projects:

- HTTP/1.1 server
- TCP proxy
- DNS resolver
- Redis-compatible server subset
- WebSocket chat
- TLS concepts lab

## RAG and Agent Systems

Purpose: build AI systems from retrieval primitives to agent runtime behavior.

Suggested projects:

- chunking and document ingestion
- embedding abstraction
- vector search
- reranking
- citation-grounded answer synthesis
- RAG eval harness
- tool-calling agent runtime
- memory and planning experiments

## Build Systems From Scratch

Purpose: learn dependency graphs, caching, invalidation, and hermetic execution.

Suggested projects:

- task graph executor
- content-addressed cache
- file watcher and invalidation
- sandboxed command runner
- remote cache protocol
- mini Bazel-like build language

## External Catalog

If present, use `curriculum/catalog/project-catalog.md` as the catalog index and `curriculum/catalog/chapters/` as the broader source for project recommendations across operating systems, systems programming, deep networking, security engineering, performance engineering, distributed systems, databases, ML systems, LLM engineering, AI/RAG/agents, Kubernetes, containers, Unix command line, Vim, Git, PostgreSQL administration, and SRE.

If present, use `curriculum/concepts/INDEX.md` to find reusable concept chapters before teaching or scaffolding an exercise.

If present, use `curriculum/roadmap/full-curriculum-plan.md` as the roadmap index, `curriculum/roadmap/chapters/` for detailed sequencing, and `curriculum/roadmap/scaffolding-sequence.md` for implementation order.

If present, use `curriculum/curriculum.json` as the source of truth for exercise IDs, validation commands, workspace paths, and learner progression.
