# Concept Backlog

This backlog lists concept mini-chapters to add under `curriculum/concepts/`.

## Highest Priority

### Tooling

- Unix file descriptors and redirection
- Exit status and shell error handling
- Git objects, refs, and reflog
- Vim motions and text objects
- Process inspection with `ps`, `lsof`, `strace`/`dtruss`

### Go Concurrency

- Channel ownership
- Context cancellation trees
- Backpressure
- Worker pools
- Race detector and memory model
- Deterministic concurrency tests

### Operating Systems

- Syscalls and traps
- User pointer validation
- Page tables and address translation
- Context switching
- Scheduling and preemption
- File system journaling
- Kernel lock ordering

### Deep Networking

- Reliable transport
- Sliding windows
- Retransmission timers
- Flow control versus congestion control
- IP forwarding and longest-prefix match
- NAT and connection tracking
- Routing convergence

### Storage

- Durable writes and `fsync`
- Slotted pages
- Buffer pool
- B+ tree invariants
- LSM compaction
- Checksums and corruption

### Distributed Systems

- Failure models
- Quorum intersection
- Leader leases and fencing
- Idempotency and retries
- Vector clocks
- Consistent hashing
- Gossip membership

### AI Systems

- Chunking strategies
- Embedding and vector indexes
- Hybrid retrieval
- Reranking
- Grounded generation and citations
- RAG evals
- Agent tool schemas
- Durable agent execution
- Prompt injection and tool security

### Security

- Threat modeling
- Trust boundaries
- Authentication versus authorization
- Session security
- Secrets and key rotation
- Supply-chain provenance
- Sandboxing

### Performance

- Profiling
- Flamegraphs
- Tail latency
- Queueing and overload
- Lock contention
- Benchmark design
- Regression thresholds

## Medium Priority

### Databases

- Query planning
- Cardinality estimation
- Join algorithms
- MVCC visibility
- Vacuum and bloat
- Isolation anomalies
- Two-phase commit

### ML Systems

- Tensor storage
- Autograd
- Training loops
- Checkpointing
- Inference serving
- Dynamic batching
- Distributed training
- Feature stores

### LLM Engineering

- Prompt/model registries
- Structured outputs
- Trace stores
- Eval regression gates
- Model routing
- Human approval workflows
- Cost and latency dashboards

### Kubernetes and Containers

- Namespaces
- Cgroups
- OCI image layout
- Kubernetes API machinery
- Informers and watches
- Finalizers
- Owner references
- RBAC
- Admission webhooks
- Scheduling constraints

### PostgreSQL Administration

- WAL archiving
- PITR
- Replication slots
- Autovacuum
- Index design
- Locking and wait events
- Checkpoints
- Connection pooling

### SRE and Platform

- RED and USE metrics
- SLOs and error budgets
- OpenTelemetry
- Incident response
- Runbook design
- Feature flags
- Progressive delivery
- Rate limiting
- Circuit breakers

## Later Depth

- CRDTs
- Predicate locking
- Serializable snapshot isolation
- Remote build execution
- Service mesh internals
- eBPF observability
- Confidential containers
- WASM components
- Model routing
- Multi-agent coordination
- Synthetic eval generation
- AI supply-chain security
