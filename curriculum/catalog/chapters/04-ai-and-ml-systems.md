# Chapter 4: AI and ML Systems

This chapter frames AI as systems engineering. Training loops, model serving, RAG pipelines, traces, evals, tool calls, approvals, and agent sandboxes are all treated as software systems with contracts and failure modes.

**Chapter promise:** The learner should be able to separate model behavior from system behavior, design useful evaluation loops, and build AI applications that can be inspected, routed, constrained, and recovered.

## Chapter Map

| Domain | Projects | What This Domain Trains |
| --- | ---: | --- |
| ML Systems and Deep Learning Infrastructure | 6 | ML systems projects treat training and serving as infrastructure problems with state, scheduling, resource pressure, and reproducibility concerns. |
| LLM Application Engineering | 7 | LLM application engineering focuses on the software around models: prompts, schemas, traces, routing, approval, cost, and latency. |
| AI, RAG, and Agents | 5 | RAG and agent systems combine retrieval, state, tools, evaluation, and safety boundaries. These projects keep those responsibilities explicit. |

## ML Systems and Deep Learning Infrastructure

ML systems projects treat training and serving as infrastructure problems with state, scheduling, resource pressure, and reproducibility concerns.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Autograd Engine | Build a tiny tensor library with reverse-mode automatic differentiation, gradient accumulation, and optimizers. | computation graphs<br>chain rule<br>tensor operations<br>gradient accumulation<br>optimizer state | test gradients numerically<br>track memory used by saved tensors<br>separate training and inference behavior<br>benchmark batch-size tradeoffs |
| Mini Deep Learning Framework | Build modules, parameters, datasets, dataloaders, training loops, checkpointing, and evaluation metrics. | model composition<br>training loops<br>checkpoint formats<br>reproducibility<br>metrics | resume from checkpoint exactly<br>record experiment metadata<br>handle bad batches<br>compare deterministic and nondeterministic runs |
| Inference Server | Build a model-serving API with dynamic batching, request queues, warmup, timeouts, streaming responses, and metrics. | serving latency<br>batching<br>queueing<br>model lifecycle<br>resource management | measure p50/p95/p99 latency<br>prevent unbounded queues<br>expose batch-size and queue-depth metrics<br>handle model reload safely |
| Distributed Training Simulator | Build a simulator for data parallel training with gradient aggregation, stragglers, checkpointing, and worker failures. | data parallelism<br>all-reduce intuition<br>synchronization cost<br>stragglers<br>fault recovery | model slow workers<br>recover from interrupted checkpoints<br>compare synchronous and asynchronous updates |
| Feature Store | Build offline and online feature pipelines with point-in-time correctness, backfills, materialization, and serving APIs. | training/serving skew<br>point-in-time joins<br>data freshness<br>backfills<br>feature lineage | test leakage<br>expose freshness metrics<br>audit feature definitions<br>validate backfill safety |
| Model Registry | Build a registry for model artifacts, metadata, metrics, lineage, approvals, deployment state, and rollback. | artifact versioning<br>experiment lineage<br>model promotion<br>reproducibility<br>deployment governance | require evaluation before promotion<br>track training data lineage<br>support rollback<br>audit every deployment decision |

## LLM Application Engineering

LLM application engineering focuses on the software around models: prompts, schemas, traces, routing, approval, cost, and latency.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Prompt and Model Registry | Build a registry for prompts, model configs, schemas, evaluation results, rollout state, and audit history. | prompt versioning<br>model routing<br>schema compatibility<br>rollout control<br>auditability | require evals before promotion<br>support rollback<br>track cost and latency by version<br>prevent unsafe prompt/config combinations |
| Structured Output Validator | Build a typed output layer with schemas, repair attempts, validation errors, and fallback policies. | schema design<br>constrained generation<br>validation<br>retries<br>failure semantics | distinguish invalid output from unsafe output<br>measure repair success<br>avoid infinite retry loops<br>preserve raw model output for audit |
| LLM Trace Store | Build a trace system for prompts, retrieved context, model calls, tool calls, approvals, outputs, token usage, and latency. | observability for stochastic systems<br>trace trees<br>cost attribution<br>replay/debuggability<br>privacy redaction | redact secrets<br>make traces queryable<br>connect eval failures to traces<br>preserve enough data for incident review |
| Sandboxed Coding Agent | Build an agent that can inspect code, plan edits, run tests, and propose patches inside a constrained sandbox. | agent loops<br>tool permissions<br>filesystem sandboxing<br>test-driven repair<br>human approval | block destructive commands by default<br>audit every tool call<br>recover from interrupted runs<br>test prompt-injection attempts from repo files |
| Human Approval Workflow | Build a workflow layer where model-suggested actions are reviewed, approved, rejected, or modified by a human. | approval gates<br>action classification<br>workflow state<br>audit logs<br>rollback plans | classify read versus write actions<br>expire stale approvals<br>show precise diffs before mutation<br>preserve decision history |
| Model Router | Build a router that chooses models by task, cost, latency, context length, quality tier, and fallback behavior. | model selection<br>fallback policies<br>latency/cost tradeoffs<br>quality gates<br>routing observability | avoid silent quality regressions<br>track per-route cost and latency<br>test fallback loops<br>expose routing explanations |
| Cost and Latency Dashboard | Build dashboards and budgets for model calls, tool calls, retrieval, latency percentiles, cache hit rates, and eval pass rates. | LLM operations<br>cost attribution<br>latency analysis<br>caching<br>quality/cost tradeoffs | alert on spend spikes<br>connect cost to user/product flows<br>separate retrieval latency from model latency<br>show regressions by version |

## AI, RAG, and Agents

RAG and agent systems combine retrieval, state, tools, evaluation, and safety boundaries. These projects keep those responsibilities explicit.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| RAG From Scratch | Build ingestion, chunking, embeddings abstraction, vector search, hybrid search, reranking, answer synthesis, citations, and evals. | retrieval quality<br>chunking tradeoffs<br>embedding indexes<br>grounding<br>eval design | measure retrieval separately from generation<br>detect unsupported claims<br>track citation precision<br>test distractor documents |
| GraphRAG Knowledge System | Build entity extraction, relationship extraction, graph construction, community summaries, graph-aware retrieval, and comparison with vector-only RAG. | graph retrieval<br>entity resolution<br>global versus local questions<br>summarization pipelines<br>retrieval evaluation | handle conflicting entities<br>measure graph extraction quality<br>compare latency/cost with naive RAG<br>expose provenance |
| Agent Runtime | Build an agent loop with tool registry, typed tool calls, state checkpoints, traces, retries, human approvals, and policy checks. | tool use<br>planning loops<br>durable execution<br>structured outputs<br>human-in-the-loop controls | persist every action<br>recover from process crash mid-run<br>distinguish read-only and mutating tools<br>add red-team tests for prompt injection |
| MCP Server and Client Lab | Build a Model Context Protocol server exposing safe tools, then write a client that discovers and invokes them. | tool protocols<br>schemas<br>sandboxing<br>capability discovery<br>trust boundaries | enforce least privilege<br>audit tool calls<br>sandbox filesystem/network access<br>threat-model untrusted tool output |
| LLM Evals Harness | Build a harness for golden-answer evals, pairwise judging, retrieval evals, groundedness checks, regression tracking, and cost/latency dashboards. | eval design<br>stochastic systems testing<br>model regression<br>trace analysis<br>quality gates | avoid judging leakage<br>separate retrieval and generation failures<br>track confidence intervals<br>require evals before prompt changes |

## How To Use This Chapter

| Move | What The Learner Should Do | Evidence To Produce |
| --- | --- | --- |
| Learn the concept | Read the relevant concept chapter before opening the code. | A short note naming the invariant and the failure mode. |
| Implement the milestone | Fill the placeholder implementation for the current exercise only. | A passing validator for that milestone. |
| Review like a Staff engineer | Inspect edge cases, recovery behavior, observability, and test strength. | A design note explaining what the tests prove and what they do not prove. |
