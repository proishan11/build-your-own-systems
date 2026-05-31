# Roadmap Chapter 4: Scaffolding, Validation, and Publishing

This chapter describes how to turn the curriculum into maintained artifacts: scaffolds, validators, packaging, and references.

## First 30 Scaffolds To Create

These should be generated before expanding further.

1. Go: Cancellable Fan-Out/Fan-In
2. Go: Bounded Queue
3. Go: Worker Pool
4. Unix: Pipeline Exercises
5. Git: Object Model Explorer
6. Shell: Parse and Execute Simple Commands
7. OS: Syscall Boundary Lab
8. OS: Virtual Memory Simulator
9. Networking: Reliable Transport
10. Networking: IP Router
11. Storage: WAL Record Format
12. Storage: Durable Log
13. Storage: Slotted Page
14. Database: Buffer Pool
15. Database: B+ Tree Insert
16. Distributed: Failure Simulator
17. Distributed: Raft Election
18. Distributed: Raft AppendEntries
19. Security: Threat Modeling Lab
20. Security: Vulnerable Web App Exploit/Fix
21. Performance: Benchmark Harness
22. Performance: Tail Latency Lab
23. Containers: Namespace Runner
24. Kubernetes: Reconcile Loop Skeleton
25. Postgres: Backup and Restore Lab
26. ML Systems: Autograd Engine
27. ML Systems: Inference Server
28. RAG: Chunk and Embed Documents
29. Agents: Tool Registry and Trace Log
30. Evals: Retrieval Quality Harness


## What To Build Into Every Exercise

Every scaffold should include:

- concept chapter link
- local primer
- self-check questions
- placeholder implementation
- tests
- validation command
- failure-mode extension
- Staff review questions
- deeper references


## Validation Strategy By Track

### Tooling

- golden tests
- shell transcript tests
- real-tool comparison tests

### Concurrency

- unit tests
- race detector
- leak tests
- stress loop
- benchmarks

### Operating Systems

- syscall boundary tests
- invalid pointer tests
- scheduler/fairness tests
- filesystem crash tests
- kernel invariant checkers

### Networking

- packet golden tests
- loss/reordering simulations
- malformed packet tests
- throughput and latency benchmarks
- route convergence tests

### Storage

- golden binary-format tests
- property tests
- crash-point tests
- corruption tests
- recovery tests

### Distributed Systems

- state-machine unit tests
- deterministic simulation
- partition/restart tests
- history checking
- latency and availability benchmarks

### Security

- exploit reproduction tests
- regression tests for fixes
- authorization matrix tests
- secret-leak scans
- audit-log completeness checks

### Performance

- benchmark baselines
- profiler output checks
- p95/p99 latency tests under load
- contention tests
- regression thresholds

### Kubernetes/Containers

- fake API server tests
- kind/minikube integration tests
- RBAC tests
- reconciliation idempotency tests
- failure injection

### PostgreSQL

- restore verification
- query plan comparison
- load tests
- replication lag simulation
- runbook drills

### AI Systems

- retrieval precision/recall
- groundedness checks
- tool-call audit tests
- prompt-injection tests
- trace completeness checks
- cost/latency benchmarks

### ML Systems

- numerical gradient checks
- checkpoint resume tests
- training/inference parity checks
- batch-size throughput and latency benchmarks
- data leakage tests

### LLM Engineering

- schema validation tests
- eval regression gates
- trace redaction checks
- tool approval tests
- prompt/model rollout tests


## Artifact Standards

Every serious project should produce:

- `README.md` or exercise notes
- design note
- implementation
- tests
- benchmark or simulation
- observability output
- failure-mode report
- next-step reflection


## Publishing Plan

To make this useful outside this repo:

1. Keep the portable skill in `skills/interactive-learning-coach`.
2. Keep concepts in `curriculum/concepts`.
3. Keep project roadmaps in `curriculum/roadmap`.
4. Keep exercises in `playgrounds/<track>/exercises`.
5. Ship adapters for Cursor, Windsurf, Claude, Codex, and generic `AGENTS.md`.
6. Version the curriculum by milestone, not by random file churn.
7. Add a `starter-pack` zip with the skill, concepts, catalog, and first exercise from each major track.


## Source Anchors For Fast-Moving Areas

- OpenAI Agents SDK evolution, sandboxes, files, tool use, memory: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- OpenAI Agents SDK docs: https://openai.github.io/openai-agents-python/
- MCP specification: https://modelcontextprotocol.io/specification/latest
- MCP official docs repository: https://github.com/modelcontextprotocol/modelcontextprotocol
- LangGraph docs: https://docs.langchain.com/oss/python/langgraph
- Microsoft GraphRAG docs: https://microsoft.github.io/graphrag/
- Kubernetes docs: https://kubernetes.io/docs/
- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/
- Kubernetes operator pattern: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- CNCF cloud native survey: https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
- CNCF landscape guide: https://landscapeapp.cncf.io/cncf/guide
- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/coreutils.html
- Git book: https://git-scm.com/book/en/v2
- Vim docs: https://www.vim.org/docs.php
- PostgreSQL admin docs: https://www.postgresql.org/docs/current/admin.html
- xv6 teaching OS: https://pdos.csail.mit.edu/6.828/2019/xv6.html
- Berkeley CS162: https://cs162.org/
- Stanford CS144: https://www.scs.stanford.edu/10au-cs144/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications
- MITRE ATT&CK: https://attack.mitre.org/matrices/enterprise/
- OpenSSF Scorecard: https://openssf.org/scorecard/
- OpenTelemetry docs: https://opentelemetry.io/docs/
