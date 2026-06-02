# Self-Contained Learning Plan

This is the learner-facing path through **Build Your Own Systems**. It ties together the concept chapters, scaffolded exercises, project ladders, validation commands, and Staff-level review checkpoints.

The goal is not to sprint through every project. The goal is to build a durable mental model of systems work: name the invariant, implement the mechanism, validate behavior, inspect failure modes, and explain the tradeoff.

## How This Plan Is Self-Contained

The curriculum has three layers. Use them in this order.

| Layer | What It Gives You | Where It Lives |
| --- | --- | --- |
| Concept chapter | The vocabulary, mental model, invariant, worked example, implementation shape, and failure modes. | [Concept Library](concepts/INDEX.md) |
| Exercise | A focused implementation milestone with placeholder code, tests, hints, and review prompts. | `playgrounds/.../exercises/` |
| Project ladder | A five-step path from core operation to state model, planning, failure recovery, and integration simulation. | [Project Catalog](catalog/project-catalog.md) |

You should not need to leave the repo to understand what an exercise is asking. External references are for depth, comparison, and taste after the local explanation has given you the mental model.

## The Learning Loop

Every exercise should follow the same rhythm.

| Step | What You Do | Evidence You Produce |
| --- | --- | --- |
| Learn | Read the linked concept chapter before touching code. | A short note naming the invariant and the failure mode. |
| Inspect | Read the placeholder implementation and tests. | A list of behaviors the tests prove. |
| Implement | Fill only the current exercise's missing behavior. | A small diff focused on the contract. |
| Validate | Run the exercise validator. | Passing focused tests, or one understood failure. |
| Review | Explain correctness, failure handling, observability, and missing coverage. | Staff-level review answers. |

If you cannot explain the invariant in plain language, do not start coding yet. That little pause is where most of the learning happens.

## Phase Map

| Phase | Theme | Main Concepts | Representative Work |
| ---: | --- | --- | --- |
| 0 | Tool fluency | Unix streams, Git objects, editor movement, shell process model. | Unix pipelines, Mini Git, shell text processing, Vim kata. |
| 1 | Local systems | Syscalls, process boundaries, memory, file descriptors, protocol parsing. | Mini shell, syscall boundary, virtual memory, HTTP/DNS labs. |
| 2 | Concurrency | Goroutine ownership, cancellation, bounded queues, worker lifecycle. | Cancellable fan-out/fan-in, bounded queue, worker pool. |
| 3 | Storage and databases | WAL, record formats, recovery, pages, buffer pools, indexes. | WAL record format, local durable log, MiniDB storage engine. |
| 4 | Distributed systems | Replicated logs, quorums, consensus, retries, idempotency. | Replicated WAL with Raft, Dynamo-style KV store, stream processor. |
| 5 | Cloud and operations | Reconciliation, containers, controllers, backups, observability. | Kubernetes controller, container runtime, PostgreSQL backup/PITR. |
| 6 | Security and performance | Threat modeling, boundaries, profiling, tail latency, benchmark evidence. | Vulnerable app lab, agent security, profiler, tail latency lab. |
| 7 | AI and ML systems | Autograd, serving, RAG, tool use, evals, traces, guardrails. | Autograd engine, RAG from scratch, agent runtime, eval harness. |

The phases are ordered to reduce mystery. Distributed systems are easier after local systems. Databases are easier after logs and file formats. AI agents are easier after you already understand state, tools, traces, policy, and failure recovery.

## Phase 0: Tool Fluency

You begin with the tools that make every later project easier to inspect. This is not "just productivity." Unix, Vim, and Git are systems in miniature: streams, process exit codes, content-addressed storage, graph traversal, and composable interfaces.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Unix pipelines | Data output, diagnostic output, exit status, stream composition, and broken-pipe behavior. | [Unix Pipelines](concepts/developer-tools/unix-pipelines.md) |
| Git object model | Blobs, trees, commits, refs, HEAD, object identity, and history as a graph. | [Git Object Model](concepts/developer-tools/git-object-model.md) |

Start with `tooling/001-unix-pipelines`, then move to `tooling/002-git-object-explorer`. When you finish this phase, you should be able to explain what belongs on stdout versus stderr and draw a commit/tree/blob graph by hand.

## Phase 1: Local Systems

Local systems teach the boundary between your program, the operating system, and the network. You learn why user code cannot directly touch privileged state, why parsing protocols is more than splitting strings, and why errors must preserve enough information for callers to recover.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Kernel boundary | Syscall dispatch, traps, user-pointer validation, and error semantics. | [Syscalls, Traps, and Kernel Boundaries](concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md) |
| Reliable transport | Sequence numbers, ACKs, retransmission, receiver buffers, and duplicate suppression. | [Reliable Transport](concepts/networking/reliable-transport.md) |

Work through `os/001-syscall-boundary`, `os/002-virtual-memory`, `networking/001-reliable-transport`, and `networking/002-ip-router`. When you finish, you should be able to state which inputs are untrusted and what invariant prevents duplicate network delivery.

## Phase 2: Concurrency

Concurrency is where lifecycle discipline becomes visible. Starting goroutines is cheap; stopping them without leaks, races, or blocked sends is the hard part.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Pipelines and cancellation | Channel ownership, fan-out/fan-in, context cancellation, bounded work, and goroutine leaks. | [Pipelines and Cancellation](concepts/go-concurrency/pipelines-and-cancellation.md) |

Start with `go-concurrency/001-cancellable-fanout-fanin`, then `go-concurrency/002-bounded-queue`, then `go-concurrency/003-worker-pool`. Use `go test -race` whenever possible. When you finish, you should be able to answer who closes each channel, what wakes blocked producers, and what happens during shutdown.

## Phase 3: Storage and Databases

Storage systems make correctness durable. Bugs survive restarts. This phase teaches how append-only logs, record formats, and recovery rules turn scattered mutations into a history the system can rebuild from.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| WAL | Durable boundaries, replay, checkpoints, idempotence, and torn-tail handling. | [Write-Ahead Logs](concepts/storage/write-ahead-logs.md) |
| WAL record formats | Headers, payloads, length prefixes, type tags, checksums, and versioning. | [WAL Record Formats](concepts/storage/wal-record-format.md) |
| PostgreSQL operations | WAL, checkpoints, vacuum, replication slots, PITR, query plans, and restore evidence. | [PostgreSQL Administration Mental Model](concepts/postgres/postgres-admin-mental-model.md) |

Work through `database/001-wal-record-format`, `distributed/001-local-durable-log`, and the database systems staff-lab exercises. When you finish, you should be able to say what is durable after append returns and what recovery does with partial final records.

## Phase 4: Distributed Systems

Distributed systems add uncertainty. A timeout does not prove failure. A retry might happen after a partial success. A leader can be stale. A quorum protects safety because any two majorities overlap.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Raft and replicated logs | Terms, leader election, quorum commit, log matching, persistence, and safety versus liveness. | [Raft and Replicated Logs](concepts/distributed-systems/raft-and-replicated-logs.md) |

Start with the replicated WAL work before jumping into larger distributed stores. When you finish this phase, you should be able to distinguish accepted, replicated, committed, and applied state.

## Phase 5: Cloud and Operations

Cloud-native systems are mostly control loops, isolation boundaries, and evidence. A controller observes state, compares it with intent, takes an idempotent action, and records what happened.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Reconciliation | Desired state, observed state, idempotent actions, finalizers, status, and retry behavior. | [Reconciliation and Controllers](concepts/containers-kubernetes/reconciliation-and-controllers.md) |
| PostgreSQL operations | Backup, restore, replication, lag, plans, statistics, and operational proof. | [PostgreSQL Administration Mental Model](concepts/postgres/postgres-admin-mental-model.md) |

Use the Kubernetes and PostgreSQL project ladders here. When you finish, you should be able to design a controller action that is safe to retry and a restore drill that proves backup quality.

## Phase 6: Security and Performance

Security and performance are not finishing touches. They are engineering disciplines that ask for evidence. Security asks what actors can do across trust boundaries. Performance asks what workload, metric, profile, and baseline prove a claim.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Threat modeling | Assets, actors, trust boundaries, abuse cases, mitigations, and least privilege. | [Threat Modeling](concepts/security/threat-modeling.md) |
| Profiling and tail latency | Percentiles, queueing, profiles, coordinated omission, contention, and benchmark design. | [Profiling and Tail Latency](concepts/performance/profiling-and-tail-latency.md) |

Work through vulnerable app, auth/session, agent security, profiler, benchmark, and tail latency labs. When you finish, you should be able to draw a trust boundary diagram and explain why an average latency number is not enough.

## Phase 7: AI and ML Systems

AI systems are still systems. They have state, inputs, outputs, tool boundaries, traces, evaluation loops, cost, latency, and failure modes. This phase avoids treating model calls as magic.

| Concept | What You Should Understand | Chapter |
| --- | --- | --- |
| Autograd and training loops | Tensors, computational graphs, gradients, backpropagation, optimizers, and checkpointing. | [Autograd and Training Loops](concepts/ml-systems/autograd-and-training-loops.md) |
| RAG and agents | Retrieval, reranking, tool calls, observations, policy boundaries, durable state, and approval. | [RAG, Agents, and Tool Use](concepts/ai-agents/rag-agents-and-tool-use.md) |
| Evals and traces | Eval cases, golden datasets, rubrics, trace stores, guardrails, and regression gates. | [LLM Evals, Traces, and Guardrails](concepts/llm-engineering/llm-evals-traces-and-guardrails.md) |

Start with RAG from scratch before agent runtime. Build evals and traces early, not after the agent becomes hard to debug. When you finish, you should be able to separate model behavior from system behavior.

## What Counts As Completion

Do not measure progress only by checked boxes. Each phase should leave behind evidence.

| Evidence | Good Signal |
| --- | --- |
| Passing validator | The implementation satisfies the focused behavioral contract. |
| Invariant note | You can name the rule the code preserves. |
| Failure-mode note | You can explain what happens on cancellation, retry, crash, timeout, malformed input, or overload. |
| Review answer | You can identify residual risk and missing tests. |
| Operational signal | You can say what metric, log, trace, or benchmark would reveal production trouble. |

The Staff-level bar is not "I made the tests pass." It is "I know what the tests prove, what they do not prove, and what I would measure next."

## How To Ask The Coach

Use the portable skill as a learning partner, not a solution dispenser.

```text
Use $interactive-learning-coach. Start the next exercise from the self-contained learning plan.
Teach the concept first. Then ask me the self-check questions before showing the implementation contract.
```

For hints:

```text
Use $interactive-learning-coach. Give me Hint 1 for this exercise, but do not reveal the full solution.
```

For review:

```text
Use $interactive-learning-coach. Validate my solution and review it like a Staff engineer.
Focus on invariants, failure modes, cancellation, durability, observability, and tests.
```

## Maintaining The Plan

Whenever a project ladder adds a new concept, update the [Concept Library](concepts/INDEX.md) or add a new chapter before adding more exercises. The curriculum should stay self-contained: project pages describe what to build, while concept chapters teach how to think.
