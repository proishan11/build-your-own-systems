# Concept Library

This directory contains self-contained teaching chapters. Exercises should link here before asking the learner to implement code.

A concept chapter is not a project description. It should teach the idea well enough that a learner can open an exercise with the right vocabulary, mental model, invariant, and failure model already in place.

The first pass of the library covers 128 bookified chapters across the curriculum. The iteration tracker lives in [Concept Bookification Plan](../roadmap/concept-bookification-plan.md).

## Chapter Standard

| Section | Purpose |
| --- | --- |
| What You Should Know First | Names the prerequisite ideas without assuming mastery. |
| The Problem | Explains why the concept exists and what pain it removes. |
| Vocabulary | Defines the terms the learner will see in code, tests, papers, and docs. |
| Mental Model | Gives the learner a simple way to reason about the mechanism. |
| How It Works Step By Step | Builds the mechanism progressively instead of summarizing it in one paragraph. |
| Core Invariant | States the rule that must remain true for the system to be correct. |
| Worked Example | Walks through a small concrete scenario. |
| State Or Flow Walkthrough | Shows the transitions, data movement, or lifecycle the learner should simulate. |
| Implementation Shape | Shows how the idea tends to appear in code without giving full solutions. |
| Failure Modes | Names the traps that make real systems fail. |
| Exercise Mapping | Connects the concept to scaffolded projects and review expectations. |
| Exercise Bridge | Turns the concept into a short implementation plan. |
| Readiness Checklist | Gives a concrete ready-to-code gate. |
| Self-Check | Gives questions a learner should answer before coding. |
| Further Reading | Points to deeper references once the mental model is in place. |

## Current Chapters

| Area | Concept | Chapter |
| --- | --- | --- |
| Advanced Systems | AI Supply-Chain Security | [ai-supply-chain-security.md](advanced-systems/ai-supply-chain-security.md) |
| Advanced Systems | Confidential Containers | [confidential-containers.md](advanced-systems/confidential-containers.md) |
| Advanced Systems | CRDTs | [crdts.md](advanced-systems/crdts.md) |
| Advanced Systems | eBPF Observability | [ebpf-observability.md](advanced-systems/ebpf-observability.md) |
| Advanced Systems | Multi-Agent Coordination | [multi-agent-coordination.md](advanced-systems/multi-agent-coordination.md) |
| Advanced Systems | Predicate Locking | [predicate-locking.md](advanced-systems/predicate-locking.md) |
| Advanced Systems | Remote Build Execution | [remote-build-execution.md](advanced-systems/remote-build-execution.md) |
| Advanced Systems | Serializable Snapshot Isolation | [serializable-snapshot-isolation.md](advanced-systems/serializable-snapshot-isolation.md) |
| Advanced Systems | Service Mesh Internals | [service-mesh-internals.md](advanced-systems/service-mesh-internals.md) |
| Advanced Systems | Synthetic Eval Generation | [synthetic-eval-generation.md](advanced-systems/synthetic-eval-generation.md) |
| Advanced Systems | WASM Components | [wasm-components.md](advanced-systems/wasm-components.md) |
| AI Agents | RAG, Agents, and Tool Use | [rag-agents-and-tool-use.md](ai-agents/rag-agents-and-tool-use.md) |
| AI Systems | Agent Tool Schemas | [agent-tool-schemas.md](ai-agents/agent-tool-schemas.md) |
| AI Systems | Chunking Strategies | [chunking-strategies.md](ai-agents/chunking-strategies.md) |
| AI Systems | Durable Agent Execution | [durable-agent-execution.md](ai-agents/durable-agent-execution.md) |
| AI Systems | Embedding and Vector Indexes | [embedding-and-vector-indexes.md](ai-agents/embedding-and-vector-indexes.md) |
| AI Systems | Grounded Generation and Citations | [grounded-generation-and-citations.md](ai-agents/grounded-generation-and-citations.md) |
| AI Systems | Hybrid Retrieval | [hybrid-retrieval.md](ai-agents/hybrid-retrieval.md) |
| AI Systems | Prompt Injection and Tool Security | [prompt-injection-and-tool-security.md](ai-agents/prompt-injection-and-tool-security.md) |
| AI Systems | RAG Evals | [rag-evals.md](ai-agents/rag-evals.md) |
| AI Systems | Reranking | [reranking.md](ai-agents/reranking.md) |
| Containers/Kubernetes | Reconciliation and Controllers | [reconciliation-and-controllers.md](containers-kubernetes/reconciliation-and-controllers.md) |
| Databases | Cardinality Estimation | [cardinality-estimation.md](databases/cardinality-estimation.md) |
| Databases | Isolation Anomalies | [isolation-anomalies.md](databases/isolation-anomalies.md) |
| Databases | Join Algorithms | [join-algorithms.md](databases/join-algorithms.md) |
| Databases | MVCC Visibility | [mvcc-visibility.md](databases/mvcc-visibility.md) |
| Databases | Query Planning | [query-planning.md](databases/query-planning.md) |
| Databases | Two-Phase Commit | [two-phase-commit.md](databases/two-phase-commit.md) |
| Databases | Vacuum and Bloat | [vacuum-and-bloat.md](databases/vacuum-and-bloat.md) |
| Developer Tools | Exit Status and Shell Error Handling | [exit-status-and-shell-error-handling.md](developer-tools/exit-status-and-shell-error-handling.md) |
| Developer Tools | Git Object Model | [git-object-model.md](developer-tools/git-object-model.md) |
| Developer Tools | Process Inspection with ps, lsof, strace, and dtruss | [process-inspection-with-ps-lsof-strace-and-dtruss.md](developer-tools/process-inspection-with-ps-lsof-strace-and-dtruss.md) |
| Developer Tools | Unix File Descriptors and Redirection | [unix-file-descriptors-and-redirection.md](developer-tools/unix-file-descriptors-and-redirection.md) |
| Developer Tools | Unix Pipelines | [unix-pipelines.md](developer-tools/unix-pipelines.md) |
| Developer Tools | Vim Motions and Text Objects | [vim-motions-and-text-objects.md](developer-tools/vim-motions-and-text-objects.md) |
| Distributed Systems | Consistent Hashing | [consistent-hashing.md](distributed-systems/consistent-hashing.md) |
| Distributed Systems | Failure Models | [failure-models.md](distributed-systems/failure-models.md) |
| Distributed Systems | Gossip Membership | [gossip-membership.md](distributed-systems/gossip-membership.md) |
| Distributed Systems | Idempotency and Retries | [idempotency-and-retries.md](distributed-systems/idempotency-and-retries.md) |
| Distributed Systems | Leader Leases and Fencing | [leader-leases-and-fencing.md](distributed-systems/leader-leases-and-fencing.md) |
| Distributed Systems | Quorum Intersection | [quorum-intersection.md](distributed-systems/quorum-intersection.md) |
| Distributed Systems | Raft and Replicated Logs | [raft-and-replicated-logs.md](distributed-systems/raft-and-replicated-logs.md) |
| Distributed Systems | Vector Clocks | [vector-clocks.md](distributed-systems/vector-clocks.md) |
| Go Concurrency | Backpressure | [backpressure.md](go-concurrency/backpressure.md) |
| Go Concurrency | Channel Ownership | [channel-ownership.md](go-concurrency/channel-ownership.md) |
| Go Concurrency | Context Cancellation Trees | [context-cancellation-trees.md](go-concurrency/context-cancellation-trees.md) |
| Go Concurrency | Deterministic Concurrency Tests | [deterministic-concurrency-tests.md](go-concurrency/deterministic-concurrency-tests.md) |
| Go Concurrency | Pipelines and Cancellation | [pipelines-and-cancellation.md](go-concurrency/pipelines-and-cancellation.md) |
| Go Concurrency | Race Detector and Memory Model | [race-detector-and-memory-model.md](go-concurrency/race-detector-and-memory-model.md) |
| Go Concurrency | Worker Pools | [worker-pools.md](go-concurrency/worker-pools.md) |
| Kubernetes and Containers | Admission Webhooks | [admission-webhooks.md](containers-kubernetes/admission-webhooks.md) |
| Kubernetes and Containers | Cgroups | [cgroups.md](containers-kubernetes/cgroups.md) |
| Kubernetes and Containers | Finalizers | [finalizers.md](containers-kubernetes/finalizers.md) |
| Kubernetes and Containers | Informers and Watches | [informers-and-watches.md](containers-kubernetes/informers-and-watches.md) |
| Kubernetes and Containers | Kubernetes Api Machinery | [kubernetes-api-machinery.md](containers-kubernetes/kubernetes-api-machinery.md) |
| Kubernetes and Containers | Namespaces | [namespaces.md](containers-kubernetes/namespaces.md) |
| Kubernetes and Containers | OCI Image Layout | [oci-image-layout.md](containers-kubernetes/oci-image-layout.md) |
| Kubernetes and Containers | Owner References | [owner-references.md](containers-kubernetes/owner-references.md) |
| Kubernetes and Containers | RBAC | [rbac.md](containers-kubernetes/rbac.md) |
| Kubernetes and Containers | Scheduling Constraints | [scheduling-constraints.md](containers-kubernetes/scheduling-constraints.md) |
| LLM Engineering | Cost and Latency Dashboards | [cost-and-latency-dashboards.md](llm-engineering/cost-and-latency-dashboards.md) |
| LLM Engineering | Eval Regression Gates | [eval-regression-gates.md](llm-engineering/eval-regression-gates.md) |
| LLM Engineering | Evals, Traces, and Guardrails | [llm-evals-traces-and-guardrails.md](llm-engineering/llm-evals-traces-and-guardrails.md) |
| LLM Engineering | Human Approval Workflows | [human-approval-workflows.md](llm-engineering/human-approval-workflows.md) |
| LLM Engineering | Model Routing | [model-routing.md](llm-engineering/model-routing.md) |
| LLM Engineering | Prompt and Model Registries | [prompt-and-model-registries.md](llm-engineering/prompt-and-model-registries.md) |
| LLM Engineering | Structured Outputs | [structured-outputs.md](llm-engineering/structured-outputs.md) |
| LLM Engineering | Trace Stores | [trace-stores.md](llm-engineering/trace-stores.md) |
| ML Systems | Autograd and Training Loops | [autograd-and-training-loops.md](ml-systems/autograd-and-training-loops.md) |
| ML Systems | Checkpointing | [checkpointing.md](ml-systems/checkpointing.md) |
| ML Systems | Distributed Training | [distributed-training.md](ml-systems/distributed-training.md) |
| ML Systems | Dynamic Batching | [dynamic-batching.md](ml-systems/dynamic-batching.md) |
| ML Systems | Feature Stores | [feature-stores.md](ml-systems/feature-stores.md) |
| ML Systems | Inference Serving | [inference-serving.md](ml-systems/inference-serving.md) |
| ML Systems | Tensor Storage | [tensor-storage.md](ml-systems/tensor-storage.md) |
| Networking | Flow Control versus Congestion Control | [flow-control-versus-congestion-control.md](networking/flow-control-versus-congestion-control.md) |
| Networking | IP Forwarding and Longest-Prefix Match | [ip-forwarding-and-longest-prefix-match.md](networking/ip-forwarding-and-longest-prefix-match.md) |
| Networking | NAT and Connection Tracking | [nat-and-connection-tracking.md](networking/nat-and-connection-tracking.md) |
| Networking | Reliable Transport | [reliable-transport.md](networking/reliable-transport.md) |
| Networking | Retransmission Timers | [retransmission-timers.md](networking/retransmission-timers.md) |
| Networking | Routing Convergence | [routing-convergence.md](networking/routing-convergence.md) |
| Networking | Sliding Windows | [sliding-windows.md](networking/sliding-windows.md) |
| Operating Systems | Context Switching | [context-switching.md](operating-systems/context-switching.md) |
| Operating Systems | File System Journaling | [file-system-journaling.md](operating-systems/file-system-journaling.md) |
| Operating Systems | Kernel Lock Ordering | [kernel-lock-ordering.md](operating-systems/kernel-lock-ordering.md) |
| Operating Systems | Page Tables and Address Translation | [page-tables-and-address-translation.md](operating-systems/page-tables-and-address-translation.md) |
| Operating Systems | Scheduling and Preemption | [scheduling-and-preemption.md](operating-systems/scheduling-and-preemption.md) |
| Operating Systems | Syscalls, Traps, and Kernel Boundaries | [syscalls-traps-and-kernel-boundaries.md](operating-systems/syscalls-traps-and-kernel-boundaries.md) |
| Operating Systems | User Pointer Validation | [user-pointer-validation.md](operating-systems/user-pointer-validation.md) |
| Performance | Benchmark Design | [benchmark-design.md](performance/benchmark-design.md) |
| Performance | Flamegraphs | [flamegraphs.md](performance/flamegraphs.md) |
| Performance | Lock Contention | [lock-contention.md](performance/lock-contention.md) |
| Performance | Profiling and Tail Latency | [profiling-and-tail-latency.md](performance/profiling-and-tail-latency.md) |
| Performance | Queueing and Overload | [queueing-and-overload.md](performance/queueing-and-overload.md) |
| Performance | Regression Thresholds | [regression-thresholds.md](performance/regression-thresholds.md) |
| PostgreSQL | Administration Mental Model | [postgres-admin-mental-model.md](postgres/postgres-admin-mental-model.md) |
| PostgreSQL Administration | Autovacuum | [autovacuum.md](postgres/autovacuum.md) |
| PostgreSQL Administration | Checkpoints | [checkpoints.md](postgres/checkpoints.md) |
| PostgreSQL Administration | Connection Pooling | [connection-pooling.md](postgres/connection-pooling.md) |
| PostgreSQL Administration | Index Design | [index-design.md](postgres/index-design.md) |
| PostgreSQL Administration | Locking and Wait Events | [locking-and-wait-events.md](postgres/locking-and-wait-events.md) |
| PostgreSQL Administration | PITR | [pitr.md](postgres/pitr.md) |
| PostgreSQL Administration | Replication Slots | [replication-slots.md](postgres/replication-slots.md) |
| PostgreSQL Administration | WAL Archiving | [wal-archiving.md](postgres/wal-archiving.md) |
| Security | Authentication versus Authorization | [authentication-versus-authorization.md](security/authentication-versus-authorization.md) |
| Security | Sandboxing | [sandboxing.md](security/sandboxing.md) |
| Security | Secrets and Key Rotation | [secrets-and-key-rotation.md](security/secrets-and-key-rotation.md) |
| Security | Session Security | [session-security.md](security/session-security.md) |
| Security | Supply-Chain Provenance | [supply-chain-provenance.md](security/supply-chain-provenance.md) |
| Security | Threat Modeling | [threat-modeling.md](security/threat-modeling.md) |
| Security | Trust Boundaries | [trust-boundaries.md](security/trust-boundaries.md) |
| SRE and Platform | Circuit Breakers | [circuit-breakers.md](sre-platform/circuit-breakers.md) |
| SRE and Platform | Feature Flags | [feature-flags.md](sre-platform/feature-flags.md) |
| SRE and Platform | Incident Response | [incident-response.md](sre-platform/incident-response.md) |
| SRE and Platform | OpenTelemetry | [opentelemetry.md](sre-platform/opentelemetry.md) |
| SRE and Platform | Progressive Delivery | [progressive-delivery.md](sre-platform/progressive-delivery.md) |
| SRE and Platform | Rate Limiting | [rate-limiting.md](sre-platform/rate-limiting.md) |
| SRE and Platform | RED and USE Metrics | [red-and-use-metrics.md](sre-platform/red-and-use-metrics.md) |
| SRE and Platform | Runbook Design | [runbook-design.md](sre-platform/runbook-design.md) |
| SRE and Platform | SLOs and Error Budgets | [slos-and-error-budgets.md](sre-platform/slos-and-error-budgets.md) |
| Storage | B+ Tree Invariants | [b-plus-tree-invariants.md](storage/b-plus-tree-invariants.md) |
| Storage | Buffer Pools | [buffer-pools.md](storage/buffer-pools.md) |
| Storage | Checksums and Corruption | [checksums-and-corruption.md](storage/checksums-and-corruption.md) |
| Storage | Durable Writes and fsync | [durable-writes-and-fsync.md](storage/durable-writes-and-fsync.md) |
| Storage | LSM Compaction | [lsm-compaction.md](storage/lsm-compaction.md) |
| Storage | Slotted Pages | [slotted-pages.md](storage/slotted-pages.md) |
| Storage | WAL Record Formats | [wal-record-format.md](storage/wal-record-format.md) |
| Storage | Write-Ahead Logs | [write-ahead-logs.md](storage/write-ahead-logs.md) |

## How To Use These Chapters

Read the concept chapter before the exercise. Then open the exercise and identify which part of the chapter appears in the placeholder code, which invariant the tests are protecting, and which failure mode the exercise is trying to make visible.

When adding a new exercise, either link to an existing chapter or create a new one. Avoid burying the only explanation inside a single exercise file; reusable concepts should live here.
