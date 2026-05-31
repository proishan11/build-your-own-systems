# Project Catalog

This catalog is the table of contents for the project side of **Build Your Own Systems**. It is intentionally split into book-style chapters so each domain has room for a short narrative, a project table, and a clear learning arc.

The curriculum currently describes 70 project ladders. Each ladder maps to five scaffolded implementation exercises in `playgrounds/catalog/`, with concept notes, placeholder code, validators, hints, references, and Staff-level review prompts.

## How To Read This Catalog

Read the catalog like a technical book, not a menu of random project ideas. A chapter groups related systems concepts, then each table row explains what the learner builds, which ideas the project teaches, and where Staff-level pressure should appear.

| Level | What It Means | How To Work |
| --- | --- | --- |
| Foundation | Learn the primitives and local invariants. | Prefer smaller exercises and write down the core invariant before coding. |
| Intermediate | Compose primitives into real components. | Track state transitions, ownership boundaries, and failure cases. |
| Advanced | Add correctness, recovery, scale, and operations. | Introduce crash tests, retries, metrics, and design review. |
| Capstone | Build a system that forces tradeoffs. | Compare alternatives and explain what the implementation deliberately does not handle. |

## Catalog Chapters

| Chapter | Domains | Project Ladders | Why It Exists |
| --- | --- | ---: | --- |
| [Chapter 1: Systems Foundations](chapters/01-systems-foundations.md) | Systems Programming, Operating Systems and Kernels, Unix Command Line, Vim, Git | 13 | Build this first when the learner needs stronger local reasoning and sharper tool fluency. |
| [Chapter 2: Networking and Distributed Systems](chapters/02-networking-and-distributed-systems.md) | Networking, Deep Networking, Go Concurrency, Distributed Systems | 13 | Build this after local systems so concurrency, unreliable networks, and replicated state have somewhere to attach. |
| [Chapter 3: Data Systems](chapters/03-data-systems.md) | Database Systems, PostgreSQL Administration | 6 | Build this when the learner is ready for crash recovery, persistence, and operational database work. |
| [Chapter 4: AI and ML Systems](chapters/04-ai-and-ml-systems.md) | ML Systems and Deep Learning Infrastructure, LLM Application Engineering, AI, RAG, and Agents | 18 | Build this when the learner wants modern AI systems without treating model calls as magic. |
| [Chapter 5: Cloud and Platform Engineering](chapters/05-cloud-and-platform-engineering.md) | Kubernetes, Containers | 7 | Build this when the learner is ready to think in reconciliation loops, isolation boundaries, and platform APIs. |
| [Chapter 6: Production, Security, and Performance](chapters/06-production-security-and-performance.md) | System Design and SRE, Security Engineering, Performance Engineering | 13 | Build this when the learner needs Staff-level judgment under operational, adversarial, and performance pressure. |

## Learning Contract

Every project ladder should feel like a chapter exercise from a serious systems book: teach the concept, make the learner implement the mechanism, validate behavior, then review the design under failure.

| Stage | Learner Experience | Repository Artifact |
| --- | --- | --- |
| Concept | A short explanation introduces the mental model, invariant, and common misconception. | Exercise markdown and concept references. |
| Implementation | The learner fills placeholder code with comments that point at the intended design. | `lab*.py`, Go/Rust/Python modules, or equivalent track files. |
| Validation | Tests fail for the missing behavior, not for unrelated setup. | Focused validators and `tools/learn.py validate`. |
| Review | The learner explains correctness, failure handling, observability, and test coverage. | Staff-level review questions and optional design notes. |

## Recommended Staff-Level Path

| Phase | Focus | Representative Projects |
| ---: | --- | --- |
| 1 | Tooling and local reasoning | Unix pipelines, Vim, Git, Mini Shell With Job Control |
| 2 | Operating systems and memory | Syscalls, virtual memory, user-level threads, Tiny Journaling File System |
| 3 | Networking fundamentals | Reliable transport, IP router, DNS resolver, Layer 4 load balancer |
| 4 | Concurrency under load | Go Concurrency Gauntlet, worker pools, stress harnesses |
| 5 | Storage internals | MiniDB WAL, slotted pages, buffer pool, B+ tree, LSM Tree KV Store |
| 6 | Distributed correctness | Replicated WAL With Raft, Dynamo-Style KV Store, Stream Processor |
| 7 | Security and performance | Threat modeling labs, Profiler From Scratch, Tail Latency Lab |
| 8 | AI systems | RAG From Scratch, LLM evals, trace store, Agent Runtime, MCP tools |
| 9 | Platform and operations | Mini container runtime, Kubernetes controller/operator, PostgreSQL PITR |
| 10 | Capstone judgment | Integrated incident-response and design-review capstone |

This path builds from local correctness to distributed correctness to operational judgment. The exact order can change, but skipping the invariant-building stages makes the advanced projects feel much more slippery than they need to be.
