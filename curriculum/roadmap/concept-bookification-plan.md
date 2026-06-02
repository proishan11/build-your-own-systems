# Concept Bookification Plan

This tracker keeps the concept-library expansion honest. The curriculum should not rely on project blurbs as teaching material; every important concept should become a self-contained chapter that a learner can read before implementing code.

## Bookified Chapter Bar

| Requirement | What It Means |
| --- | --- |
| Beginner entry | The chapter names prerequisites and introduces vocabulary before using it heavily. |
| Progressive explanation | The idea is built step by step, not only summarized. |
| Core invariant | The learner can state what must remain true for correctness. |
| Worked mechanics | The chapter shows state transitions, timelines, or data movement. |
| Failure reasoning | Common mistakes include why the wrong reasoning is tempting and how to correct it. |
| Exercise mapping | The chapter tells the learner which exercises use which parts of the concept. |
| Readiness check | The chapter ends with concrete questions that decide whether the learner is ready to code. |

## Iteration 1: Existing High-Impact Chapters

Status: complete.

These are the 15 concepts already linked by the first-wave exercises and project ladders. They were expanded first because they affect the largest amount of learner traffic.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Developer Tools | Unix Pipelines | [unix-pipelines.md](../concepts/developer-tools/unix-pipelines.md) |
| Bookified | Developer Tools | Git Object Model | [git-object-model.md](../concepts/developer-tools/git-object-model.md) |
| Bookified | Go Concurrency | Pipelines and Cancellation | [pipelines-and-cancellation.md](../concepts/go-concurrency/pipelines-and-cancellation.md) |
| Bookified | Operating Systems | Syscalls, Traps, and Kernel Boundaries | [syscalls-traps-and-kernel-boundaries.md](../concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md) |
| Bookified | Networking | Reliable Transport | [reliable-transport.md](../concepts/networking/reliable-transport.md) |
| Bookified | Storage | Write-Ahead Logs | [write-ahead-logs.md](../concepts/storage/write-ahead-logs.md) |
| Bookified | Storage | WAL Record Formats | [wal-record-format.md](../concepts/storage/wal-record-format.md) |
| Bookified | Distributed Systems | Raft and Replicated Logs | [raft-and-replicated-logs.md](../concepts/distributed-systems/raft-and-replicated-logs.md) |
| Bookified | Containers/Kubernetes | Reconciliation and Controllers | [reconciliation-and-controllers.md](../concepts/containers-kubernetes/reconciliation-and-controllers.md) |
| Bookified | PostgreSQL | Administration Mental Model | [postgres-admin-mental-model.md](../concepts/postgres/postgres-admin-mental-model.md) |
| Bookified | Security | Threat Modeling | [threat-modeling.md](../concepts/security/threat-modeling.md) |
| Bookified | Performance | Profiling and Tail Latency | [profiling-and-tail-latency.md](../concepts/performance/profiling-and-tail-latency.md) |
| Bookified | ML Systems | Autograd and Training Loops | [autograd-and-training-loops.md](../concepts/ml-systems/autograd-and-training-loops.md) |
| Bookified | AI Agents | RAG, Agents, and Tool Use | [rag-agents-and-tool-use.md](../concepts/ai-agents/rag-agents-and-tool-use.md) |
| Bookified | LLM Engineering | Evals, Traces, and Guardrails | [llm-evals-traces-and-guardrails.md](../concepts/llm-engineering/llm-evals-traces-and-guardrails.md) |

## Iteration 2: Local Systems, Concurrency, and Storage

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Developer Tools | Unix File Descriptors and Redirection | [unix-file-descriptors-and-redirection.md](../concepts/developer-tools/unix-file-descriptors-and-redirection.md) |
| Bookified | Developer Tools | Exit Status and Shell Error Handling | [exit-status-and-shell-error-handling.md](../concepts/developer-tools/exit-status-and-shell-error-handling.md) |
| Bookified | Developer Tools | Vim Motions and Text Objects | [vim-motions-and-text-objects.md](../concepts/developer-tools/vim-motions-and-text-objects.md) |
| Bookified | Developer Tools | Process Inspection with ps, lsof, strace, and dtruss | [process-inspection-with-ps-lsof-strace-and-dtruss.md](../concepts/developer-tools/process-inspection-with-ps-lsof-strace-and-dtruss.md) |
| Bookified | Go Concurrency | Channel Ownership | [channel-ownership.md](../concepts/go-concurrency/channel-ownership.md) |
| Bookified | Go Concurrency | Context Cancellation Trees | [context-cancellation-trees.md](../concepts/go-concurrency/context-cancellation-trees.md) |
| Bookified | Go Concurrency | Backpressure | [backpressure.md](../concepts/go-concurrency/backpressure.md) |
| Bookified | Go Concurrency | Worker Pools | [worker-pools.md](../concepts/go-concurrency/worker-pools.md) |
| Bookified | Go Concurrency | Race Detector and Memory Model | [race-detector-and-memory-model.md](../concepts/go-concurrency/race-detector-and-memory-model.md) |
| Bookified | Go Concurrency | Deterministic Concurrency Tests | [deterministic-concurrency-tests.md](../concepts/go-concurrency/deterministic-concurrency-tests.md) |
| Bookified | Operating Systems | User Pointer Validation | [user-pointer-validation.md](../concepts/operating-systems/user-pointer-validation.md) |
| Bookified | Operating Systems | Page Tables and Address Translation | [page-tables-and-address-translation.md](../concepts/operating-systems/page-tables-and-address-translation.md) |
| Bookified | Operating Systems | Context Switching | [context-switching.md](../concepts/operating-systems/context-switching.md) |
| Bookified | Operating Systems | Scheduling and Preemption | [scheduling-and-preemption.md](../concepts/operating-systems/scheduling-and-preemption.md) |
| Bookified | Operating Systems | File System Journaling | [file-system-journaling.md](../concepts/operating-systems/file-system-journaling.md) |

## Iteration 3: Networking, Databases, and Distributed Systems

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Operating Systems | Kernel Lock Ordering | [kernel-lock-ordering.md](../concepts/operating-systems/kernel-lock-ordering.md) |
| Bookified | Networking | Sliding Windows | [sliding-windows.md](../concepts/networking/sliding-windows.md) |
| Bookified | Networking | Retransmission Timers | [retransmission-timers.md](../concepts/networking/retransmission-timers.md) |
| Bookified | Networking | Flow Control versus Congestion Control | [flow-control-versus-congestion-control.md](../concepts/networking/flow-control-versus-congestion-control.md) |
| Bookified | Networking | IP Forwarding and Longest-Prefix Match | [ip-forwarding-and-longest-prefix-match.md](../concepts/networking/ip-forwarding-and-longest-prefix-match.md) |
| Bookified | Networking | NAT and Connection Tracking | [nat-and-connection-tracking.md](../concepts/networking/nat-and-connection-tracking.md) |
| Bookified | Networking | Routing Convergence | [routing-convergence.md](../concepts/networking/routing-convergence.md) |
| Bookified | Storage | Durable Writes and fsync | [durable-writes-and-fsync.md](../concepts/storage/durable-writes-and-fsync.md) |
| Bookified | Storage | Slotted Pages | [slotted-pages.md](../concepts/storage/slotted-pages.md) |
| Bookified | Storage | Buffer Pools | [buffer-pools.md](../concepts/storage/buffer-pools.md) |
| Bookified | Storage | B+ Tree Invariants | [b-plus-tree-invariants.md](../concepts/storage/b-plus-tree-invariants.md) |
| Bookified | Storage | LSM Compaction | [lsm-compaction.md](../concepts/storage/lsm-compaction.md) |
| Bookified | Storage | Checksums and Corruption | [checksums-and-corruption.md](../concepts/storage/checksums-and-corruption.md) |
| Bookified | Distributed Systems | Failure Models | [failure-models.md](../concepts/distributed-systems/failure-models.md) |
| Bookified | Distributed Systems | Quorum Intersection | [quorum-intersection.md](../concepts/distributed-systems/quorum-intersection.md) |

## Iteration 4: Distributed Systems, Security, and Performance

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Distributed Systems | Leader Leases and Fencing | [leader-leases-and-fencing.md](../concepts/distributed-systems/leader-leases-and-fencing.md) |
| Bookified | Distributed Systems | Idempotency and Retries | [idempotency-and-retries.md](../concepts/distributed-systems/idempotency-and-retries.md) |
| Bookified | Distributed Systems | Vector Clocks | [vector-clocks.md](../concepts/distributed-systems/vector-clocks.md) |
| Bookified | Distributed Systems | Consistent Hashing | [consistent-hashing.md](../concepts/distributed-systems/consistent-hashing.md) |
| Bookified | Distributed Systems | Gossip Membership | [gossip-membership.md](../concepts/distributed-systems/gossip-membership.md) |
| Bookified | Security | Trust Boundaries | [trust-boundaries.md](../concepts/security/trust-boundaries.md) |
| Bookified | Security | Authentication versus Authorization | [authentication-versus-authorization.md](../concepts/security/authentication-versus-authorization.md) |
| Bookified | Security | Session Security | [session-security.md](../concepts/security/session-security.md) |
| Bookified | Security | Secrets and Key Rotation | [secrets-and-key-rotation.md](../concepts/security/secrets-and-key-rotation.md) |
| Bookified | Security | Supply-Chain Provenance | [supply-chain-provenance.md](../concepts/security/supply-chain-provenance.md) |
| Bookified | Security | Sandboxing | [sandboxing.md](../concepts/security/sandboxing.md) |
| Bookified | Performance | Flamegraphs | [flamegraphs.md](../concepts/performance/flamegraphs.md) |
| Bookified | Performance | Queueing and Overload | [queueing-and-overload.md](../concepts/performance/queueing-and-overload.md) |
| Bookified | Performance | Lock Contention | [lock-contention.md](../concepts/performance/lock-contention.md) |
| Bookified | Performance | Benchmark Design | [benchmark-design.md](../concepts/performance/benchmark-design.md) |

## Iteration 5: AI, ML, Kubernetes, and Operations

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Performance | Regression Thresholds | [regression-thresholds.md](../concepts/performance/regression-thresholds.md) |
| Bookified | AI Systems | Chunking Strategies | [chunking-strategies.md](../concepts/ai-agents/chunking-strategies.md) |
| Bookified | AI Systems | Embedding and Vector Indexes | [embedding-and-vector-indexes.md](../concepts/ai-agents/embedding-and-vector-indexes.md) |
| Bookified | AI Systems | Hybrid Retrieval | [hybrid-retrieval.md](../concepts/ai-agents/hybrid-retrieval.md) |
| Bookified | AI Systems | Reranking | [reranking.md](../concepts/ai-agents/reranking.md) |
| Bookified | AI Systems | Grounded Generation and Citations | [grounded-generation-and-citations.md](../concepts/ai-agents/grounded-generation-and-citations.md) |
| Bookified | AI Systems | RAG Evals | [rag-evals.md](../concepts/ai-agents/rag-evals.md) |
| Bookified | AI Systems | Agent Tool Schemas | [agent-tool-schemas.md](../concepts/ai-agents/agent-tool-schemas.md) |
| Bookified | AI Systems | Durable Agent Execution | [durable-agent-execution.md](../concepts/ai-agents/durable-agent-execution.md) |
| Bookified | AI Systems | Prompt Injection and Tool Security | [prompt-injection-and-tool-security.md](../concepts/ai-agents/prompt-injection-and-tool-security.md) |
| Bookified | ML Systems | Tensor Storage | [tensor-storage.md](../concepts/ml-systems/tensor-storage.md) |
| Bookified | ML Systems | Checkpointing | [checkpointing.md](../concepts/ml-systems/checkpointing.md) |
| Bookified | ML Systems | Inference Serving | [inference-serving.md](../concepts/ml-systems/inference-serving.md) |
| Bookified | ML Systems | Dynamic Batching | [dynamic-batching.md](../concepts/ml-systems/dynamic-batching.md) |
| Bookified | ML Systems | Distributed Training | [distributed-training.md](../concepts/ml-systems/distributed-training.md) |

## Iteration 6: Databases, LLM Engineering, and Platform Depth

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | ML Systems | Feature Stores | [feature-stores.md](../concepts/ml-systems/feature-stores.md) |
| Bookified | Databases | Query Planning | [query-planning.md](../concepts/databases/query-planning.md) |
| Bookified | Databases | Cardinality Estimation | [cardinality-estimation.md](../concepts/databases/cardinality-estimation.md) |
| Bookified | Databases | Join Algorithms | [join-algorithms.md](../concepts/databases/join-algorithms.md) |
| Bookified | Databases | MVCC Visibility | [mvcc-visibility.md](../concepts/databases/mvcc-visibility.md) |
| Bookified | Databases | Vacuum and Bloat | [vacuum-and-bloat.md](../concepts/databases/vacuum-and-bloat.md) |
| Bookified | Databases | Isolation Anomalies | [isolation-anomalies.md](../concepts/databases/isolation-anomalies.md) |
| Bookified | Databases | Two-Phase Commit | [two-phase-commit.md](../concepts/databases/two-phase-commit.md) |
| Bookified | LLM Engineering | Prompt and Model Registries | [prompt-and-model-registries.md](../concepts/llm-engineering/prompt-and-model-registries.md) |
| Bookified | LLM Engineering | Structured Outputs | [structured-outputs.md](../concepts/llm-engineering/structured-outputs.md) |
| Bookified | LLM Engineering | Trace Stores | [trace-stores.md](../concepts/llm-engineering/trace-stores.md) |
| Bookified | LLM Engineering | Eval Regression Gates | [eval-regression-gates.md](../concepts/llm-engineering/eval-regression-gates.md) |
| Bookified | LLM Engineering | Model Routing | [model-routing.md](../concepts/llm-engineering/model-routing.md) |
| Bookified | LLM Engineering | Human Approval Workflows | [human-approval-workflows.md](../concepts/llm-engineering/human-approval-workflows.md) |
| Bookified | LLM Engineering | Cost and Latency Dashboards | [cost-and-latency-dashboards.md](../concepts/llm-engineering/cost-and-latency-dashboards.md) |

## Iteration 7: Kubernetes, PostgreSQL, SRE, and Later Depth

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Kubernetes and Containers | Namespaces | [namespaces.md](../concepts/containers-kubernetes/namespaces.md) |
| Bookified | Kubernetes and Containers | Cgroups | [cgroups.md](../concepts/containers-kubernetes/cgroups.md) |
| Bookified | Kubernetes and Containers | OCI Image Layout | [oci-image-layout.md](../concepts/containers-kubernetes/oci-image-layout.md) |
| Bookified | Kubernetes and Containers | Kubernetes Api Machinery | [kubernetes-api-machinery.md](../concepts/containers-kubernetes/kubernetes-api-machinery.md) |
| Bookified | Kubernetes and Containers | Informers and Watches | [informers-and-watches.md](../concepts/containers-kubernetes/informers-and-watches.md) |
| Bookified | Kubernetes and Containers | Finalizers | [finalizers.md](../concepts/containers-kubernetes/finalizers.md) |
| Bookified | Kubernetes and Containers | Owner References | [owner-references.md](../concepts/containers-kubernetes/owner-references.md) |
| Bookified | Kubernetes and Containers | RBAC | [rbac.md](../concepts/containers-kubernetes/rbac.md) |
| Bookified | Kubernetes and Containers | Admission Webhooks | [admission-webhooks.md](../concepts/containers-kubernetes/admission-webhooks.md) |
| Bookified | Kubernetes and Containers | Scheduling Constraints | [scheduling-constraints.md](../concepts/containers-kubernetes/scheduling-constraints.md) |
| Bookified | PostgreSQL Administration | WAL Archiving | [wal-archiving.md](../concepts/postgres/wal-archiving.md) |
| Bookified | PostgreSQL Administration | PITR | [pitr.md](../concepts/postgres/pitr.md) |
| Bookified | PostgreSQL Administration | Replication Slots | [replication-slots.md](../concepts/postgres/replication-slots.md) |
| Bookified | PostgreSQL Administration | Autovacuum | [autovacuum.md](../concepts/postgres/autovacuum.md) |
| Bookified | PostgreSQL Administration | Index Design | [index-design.md](../concepts/postgres/index-design.md) |

## Iteration 8: Operations and Advanced Systems

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | PostgreSQL Administration | Locking and Wait Events | [locking-and-wait-events.md](../concepts/postgres/locking-and-wait-events.md) |
| Bookified | PostgreSQL Administration | Checkpoints | [checkpoints.md](../concepts/postgres/checkpoints.md) |
| Bookified | PostgreSQL Administration | Connection Pooling | [connection-pooling.md](../concepts/postgres/connection-pooling.md) |
| Bookified | SRE and Platform | RED and USE Metrics | [red-and-use-metrics.md](../concepts/sre-platform/red-and-use-metrics.md) |
| Bookified | SRE and Platform | SLOs and Error Budgets | [slos-and-error-budgets.md](../concepts/sre-platform/slos-and-error-budgets.md) |
| Bookified | SRE and Platform | OpenTelemetry | [opentelemetry.md](../concepts/sre-platform/opentelemetry.md) |
| Bookified | SRE and Platform | Incident Response | [incident-response.md](../concepts/sre-platform/incident-response.md) |
| Bookified | SRE and Platform | Runbook Design | [runbook-design.md](../concepts/sre-platform/runbook-design.md) |
| Bookified | SRE and Platform | Feature Flags | [feature-flags.md](../concepts/sre-platform/feature-flags.md) |
| Bookified | SRE and Platform | Progressive Delivery | [progressive-delivery.md](../concepts/sre-platform/progressive-delivery.md) |
| Bookified | SRE and Platform | Rate Limiting | [rate-limiting.md](../concepts/sre-platform/rate-limiting.md) |
| Bookified | SRE and Platform | Circuit Breakers | [circuit-breakers.md](../concepts/sre-platform/circuit-breakers.md) |
| Bookified | Advanced Systems | CRDTs | [crdts.md](../concepts/advanced-systems/crdts.md) |
| Bookified | Advanced Systems | Predicate Locking | [predicate-locking.md](../concepts/advanced-systems/predicate-locking.md) |
| Bookified | Advanced Systems | Serializable Snapshot Isolation | [serializable-snapshot-isolation.md](../concepts/advanced-systems/serializable-snapshot-isolation.md) |

## Iteration 9: Advanced and Emerging Topics

Status: complete.

| Status | Area | Concept | Chapter |
| --- | --- | --- | --- |
| Bookified | Advanced Systems | Remote Build Execution | [remote-build-execution.md](../concepts/advanced-systems/remote-build-execution.md) |
| Bookified | Advanced Systems | Service Mesh Internals | [service-mesh-internals.md](../concepts/advanced-systems/service-mesh-internals.md) |
| Bookified | Advanced Systems | eBPF Observability | [ebpf-observability.md](../concepts/advanced-systems/ebpf-observability.md) |
| Bookified | Advanced Systems | Confidential Containers | [confidential-containers.md](../concepts/advanced-systems/confidential-containers.md) |
| Bookified | Advanced Systems | WASM Components | [wasm-components.md](../concepts/advanced-systems/wasm-components.md) |
| Bookified | Advanced Systems | Multi-Agent Coordination | [multi-agent-coordination.md](../concepts/advanced-systems/multi-agent-coordination.md) |
| Bookified | Advanced Systems | Synthetic Eval Generation | [synthetic-eval-generation.md](../concepts/advanced-systems/synthetic-eval-generation.md) |
| Bookified | Advanced Systems | AI Supply-Chain Security | [ai-supply-chain-security.md](../concepts/advanced-systems/ai-supply-chain-security.md) |

## Future TODO

The initial backlog is now bookified. When a new project introduces a reusable concept, add it here first, assign it to the next 15-concept iteration, and create the chapter before linking exercises to it.
