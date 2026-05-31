# Distributed Systems Staff Lab

## Purpose

This track teaches distributed systems by building components that must preserve correctness when machines disagree, crash, retry, pause, partition, and recover.

The goal is to develop the habits of a Staff engineer: separate safety from liveness, state invariants explicitly, design for observability, and test failure modes rather than only the happy path.

## Learning Format

Every exercise starts with a concept primer before code: why the system pattern exists, the failure model it addresses, the safety invariant, a tiny walkthrough, common misconceptions, self-check questions, and optional papers or articles for depth. Implementation comes after the learner can describe the invariant in plain language.

## Recommended Project Set

### 1. Replicated Write-Ahead Log With Raft

Build a durable replicated log that accepts client appends on a leader and commits entries after quorum replication.

Concepts:

- Persistent logs.
- Leader election.
- Terms and epochs.
- Quorum commit.
- Log matching.
- Crash recovery.
- Snapshots.
- Membership changes.

Why this matters:

This is the foundation under replicated databases, metadata stores, queues, and coordination systems.

### 2. Sharded Replicated KV Store

Build a key-value store on top of replicated groups.

Concepts:

- Sharding and placement.
- Per-shard Raft groups.
- Rebalancing.
- Linearizable reads.
- Fencing tokens.
- Idempotent client requests.
- Hot shard mitigation.

Why this matters:

This teaches the gap between implementing consensus and operating a useful distributed data system.

### 3. Gossip Membership and Failure Detector

Build a membership layer that tracks live nodes using gossip and suspicion.

Concepts:

- Heartbeats.
- Phi accrual failure detection.
- Epidemic dissemination.
- Anti-entropy.
- Split brain.
- Tombstones and incarnation numbers.

Why this matters:

Consensus systems often need membership, discovery, and failure suspicion, but suspicion is not proof. This project teaches that boundary.

### 4. Durable Distributed Queue

Build a queue with replicated metadata and durable message storage.

Concepts:

- At-least-once delivery.
- Visibility timeouts.
- Consumer groups.
- Deduplication.
- Dead-letter queues.
- Backpressure.
- Replay.

Why this matters:

Queues expose the tension between correctness, operational ergonomics, and product semantics.

### 5. Distributed Lock and Lease Service

Build locks, leases, and fencing tokens on top of a replicated log.

Concepts:

- Session expiry.
- Clock assumptions.
- Fencing.
- Linearizable state transitions.
- Client pause failures.
- Lease renewal.

Why this matters:

This project teaches why naive distributed locks are dangerous and what guarantees callers actually need.

## Main Capstone: Replicated WAL With Raft

### Phase 1: Local Durable Log

Build a single-node append-only log:

- Segment files.
- Length-prefixed records.
- Checksums.
- `fsync` policy.
- Recovery after partial writes.
- Log truncation.

Staff-level questions:

- What exactly is durable after `Append` returns?
- What happens if the process crashes between write and index update?
- How do you detect torn or partial records?

### Phase 2: Network Transport and Simulation

Build an RPC layer and a deterministic simulator:

- Request/response RPC.
- Timeouts.
- Message delay, loss, duplication, and reordering.
- Node pause and restart.
- Virtual clock for tests where possible.

Staff-level questions:

- Which failures are transport failures versus peer failures?
- How do tests avoid becoming flaky sleep-based tests?
- How will you reproduce a failed simulation seed?

### Phase 3: Leader Election

Implement Raft elections:

- Follower, candidate, leader states.
- Terms.
- Randomized election timeouts.
- Vote requests.
- Persistent current term and voted-for state.
- Step-down on higher term.

Staff-level questions:

- What invariant prevents two leaders in one term?
- What must be persisted before responding to a vote request?
- What liveness risks come from bad timeout settings?

### Phase 4: Log Replication

Replicate entries from leader to followers:

- `AppendEntries`.
- Previous log index and term checks.
- Conflict handling.
- Match index and next index.
- Commit index advancement.
- Application to a state machine.

Staff-level questions:

- What invariant is the log matching property protecting?
- Why can the leader only commit entries from its current term by counting replicas?
- How do retries remain idempotent?

### Phase 5: Client Semantics

Expose an append API:

- Leader redirect.
- Client request IDs.
- Idempotent append.
- Read-your-writes option.
- Commit acknowledgements.
- Timeout behavior.

Staff-level questions:

- Did the append fail, or is the outcome unknown?
- How should clients retry safely?
- What error should a follower return?

### Phase 6: Snapshots and Compaction

Add log compaction:

- State machine snapshots.
- Install snapshot RPC.
- Snapshot metadata.
- Truncation after snapshot.
- Recovery from snapshot plus suffix log.

Staff-level questions:

- What is the atomicity boundary between snapshot and log truncation?
- How do lagging followers catch up?
- How do snapshots affect test determinism?

### Phase 7: Membership Changes

Support changing the cluster:

- Add learner node.
- Joint consensus or equivalent safe transition.
- Remove node.
- Bootstrap new cluster.
- Persist cluster configuration.

Staff-level questions:

- What prevents committing different configs on different quorums?
- How do you avoid removing the leader unsafely?
- What operational workflow should humans follow?

### Phase 8: Production Hardening

Add operational features:

- Metrics: term, role, commit lag, append latency, fsync latency.
- Structured logs with node ID and term.
- Admin status endpoint.
- Chaos simulation suite.
- Benchmarks for append throughput and recovery time.

Staff-level questions:

- What dashboard would reveal an unstable leader?
- What alert indicates data safety risk versus availability risk?
- What are the first three runbook commands?

## Validation Strategy

Use layers:

1. Unit tests for log format and state transitions.
2. Property tests for append/recover/truncate behavior.
3. Deterministic simulation for election and replication.
4. Crash-recovery tests for persistence.
5. Jepsen-style history checks for client-visible behavior.
6. Benchmarks under realistic batching and fsync policies.

## Suggested Implementation Languages

- Go if you want networked concurrency and fast iteration.
- Rust if you want stricter ownership pressure and storage safety.
- Python only for early simulation prototypes, not the final capstone.

## First Exercise To Scaffold

Start with **Local Durable Log**.

Starter package:

```text
playgrounds/distributed-systems-staff-lab/replicated-wal/
  cmd/waltool/
  internal/wal/
    log.go
    log_test.go
    record.go
    segment.go
```

Core requirements:

- Append binary records.
- Return monotonically increasing log indexes.
- Read records by index.
- Recover committed records after restart.
- Ignore a final partial record after simulated crash.
- Detect checksum corruption.
