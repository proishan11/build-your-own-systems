# Reading List

Use this list when adding deeper references to exercises. Prefer primary sources and official docs. Add approachable articles only when they help the learner build intuition before reading papers.

## Go Concurrency

- Go blog, "Go Concurrency Patterns: Pipelines and cancellation": https://go.dev/blog/pipelines
  - Best first read for fan-out/fan-in, cancellation, and blocked senders.
- Go blog, "Go Concurrency Patterns: Context": https://go.dev/blog/context
  - Explains context cancellation, deadlines, and request-scoped lifecycle.
- Go memory model: https://go.dev/ref/mem
  - Use when discussing data races, synchronization, and visibility.

## Operating Systems and Networking

- xv6 teaching OS: https://pdos.csail.mit.edu/6.828/2019/xv6.html
  - Compact teaching kernel for syscalls, traps, virtual memory, scheduling, and filesystems.
- Berkeley CS162: https://cs162.org/
  - Strong operating-systems course reference for processes, memory, concurrency, and distributed systems foundations.
- Stanford CS144: https://www.scs.stanford.edu/10au-cs144/
  - Useful anchor for reliable transport and networking labs.
- RFC 9293, Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc9293
  - Current TCP specification reference.

## Security and Performance

- OWASP Top 10: https://owasp.org/www-project-top-ten/
  - Standard reference for common web application risks.
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications
  - Practical reference for LLM application security risks.
- MITRE ATT&CK Enterprise Matrix: https://attack.mitre.org/matrices/enterprise/
  - Useful taxonomy for adversary behavior.
- OpenSSF Scorecard: https://openssf.org/scorecard/
  - Good anchor for supply-chain security checks.
- OpenTelemetry docs: https://opentelemetry.io/docs/
  - Current reference for traces, metrics, and logs.
- Brendan Gregg USE method: https://www.brendangregg.com/usemethod.html
  - Practical performance debugging framework.

## ML Systems

- Stanford CS329S: https://bulletin.stanford.edu/courses/2230771
  - Course anchor for machine learning systems design.
- Machine Learning in Production at CMU: https://mlip-cmu.github.io/
  - Practical reference for ML production workflows, evaluation, deployment, and operations.

## Distributed Systems

- Raft paper, "In Search of an Understandable Consensus Algorithm": https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
  - Primary paper for leader election, log replication, terms, and safety.
- Raft website: https://raft.github.io/
  - Useful hub for the extended paper, talks, and visualizations.
- Dynamo paper: https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store
  - Strong contrast to Raft: availability-first design, sloppy quorums, vector clocks, conflict resolution.
- Spanner paper: https://research.google/pubs/pub39966
  - Deep read for externally consistent distributed transactions and clock uncertainty.
- MapReduce paper: https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/
  - Useful for distributed execution, retries, partitioning, and fault handling.

## Database Systems

- ARIES paper, "ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging": https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf
  - Canonical recovery paper. Read after a basic WAL implementation exists.
- LSM-tree paper, "The Log-Structured Merge-Tree": https://dsf.berkeley.edu/cs286/papers/lsm-acta1996.pdf
  - Primary source for write-optimized indexing and merge policies.
- Bigtable paper: https://research.google/pubs/pub27898
  - Practical storage-system design using tablets, SSTables, logs, and compaction.

## Interpreters and Languages

- Crafting Interpreters: https://craftinginterpreters.com/
  - Best practical book-style path from scanning/parsing to bytecode VMs.

## RAG and Agents

- OpenAI Agents SDK evolution, sandboxes, files, tool use, and memory: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
  - Current reference for the shift toward more capable agent harnesses, sandboxed execution, and long-running work.
- RAG paper, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks": https://arxiv.org/abs/2005.11401
  - Primary paper for combining parametric generation with retrieved context.
- ReAct paper: https://arxiv.org/abs/2210.03629
  - Good foundation for tool-using agents that interleave reasoning and action.
- Toolformer paper: https://arxiv.org/abs/2302.04761
  - Useful for thinking about when and how language models call external tools.
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/latest
  - Current protocol reference for connecting agents to tools and data sources.
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
  - Practical agent-building framework with tools, handoffs, guardrails, and tracing concepts.
- LangGraph docs: https://docs.langchain.com/oss/python/langgraph
  - Useful for durable execution, graph-shaped agent workflows, streaming, and human-in-the-loop patterns.
- Microsoft GraphRAG docs: https://microsoft.github.io/graphrag/
  - Practical reference for graph-structured retrieval pipelines.

## Build Systems

- "Build Systems a la Carte": https://simon.peytonjones.org/assets/pdfs/build-systems-original.pdf
  - Excellent conceptual framework for dependency graphs, rebuilding, caching, and build semantics.

## Kubernetes and Containers

- CNCF Annual Cloud Native Survey: https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
  - Useful current context for Kubernetes, cloud native maturity, and AI infrastructure.
- CNCF landscape guide: https://landscapeapp.cncf.io/cncf/guide
  - Map of cloud-native categories: orchestration, observability, security, service mesh, storage, and platform tooling.
- Kubernetes docs: https://kubernetes.io/docs/
  - Official reference for Kubernetes architecture, APIs, workloads, and operations.
- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/
  - Core concept for reconciliation loops.
- Kubernetes operator pattern: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
  - Best starting point for custom controllers and CRDs.
- Open Container Initiative: https://opencontainers.org/
  - Standards home for container image, runtime, and distribution specs.
- OCI runtime spec: https://github.com/opencontainers/runtime-spec
  - Primary reference for container runtime behavior.

## Unix, Git, Vim, and PostgreSQL

- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/coreutils.html
  - Official reference for many foundational Unix commands.
- Pro Git book: https://git-scm.com/book/en/v2
  - Best book-style explanation of Git's object model and workflows.
- Git reference docs: https://git-scm.com/docs
  - Authoritative command reference.
- Vim docs: https://www.vim.org/docs.php
  - Gateway to Vim's built-in user manual and reference docs.
- PostgreSQL server administration: https://www.postgresql.org/docs/current/admin.html
  - Official entry point for Postgres operations.
- PostgreSQL backup and restore: https://www.postgresql.org/docs/current/backup.html
  - Essential reference for backup, restore, and recovery labs.
