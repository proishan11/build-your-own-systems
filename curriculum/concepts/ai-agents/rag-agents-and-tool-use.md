# RAG, Agents, and Tool Use

## What You Should Know First

You should know that a language model predicts text from context. It does not automatically know your private documents, current database state, or what happened inside an external tool unless that information is supplied to it.

## The Problem

Useful AI applications often need two things beyond a raw model call:

1. relevant external knowledge at answer time
2. controlled access to actions such as search, database queries, code execution, tickets, or workflows

Retrieval-augmented generation, or RAG, supplies evidence. Tool use supplies actions. Agent runtimes coordinate repeated model decisions, tool calls, observations, state, policy, and recovery.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Document chunk | A searchable unit of text or data. |
| Embedding | Numeric representation used for similarity search. |
| Retriever | Component that selects candidate evidence for a query. |
| Reranker | Component that reorders retrieved evidence for relevance. |
| Tool call | Structured request from model or runtime to an external capability. |
| Observation | Result returned by a tool. |
| Agent state | Durable record of goal, messages, tool calls, observations, and decisions. |
| Policy boundary | Rule that decides what the agent may do without approval. |

## Mental Model

RAG is an evidence pipeline:

```text
question -> retrieve -> rerank -> synthesize answer with citations
```

An agent is a control loop:

```text
goal -> plan -> tool call -> observation -> update state -> next action
```

Production systems often combine both. An agent may call retrieval, inspect logs, query a database, ask for approval, and then take a limited action.

## How It Works Step By Step

RAG and agents should be built as explicit systems, not as one giant prompt.

| Step | RAG Or Agent Component | Responsibility |
| --- | --- | --- |
| Ingest | Loader and chunker | Turn source material into stable searchable units. |
| Index | Embeddings, lexical index, or graph | Make retrieval possible. |
| Retrieve | Retriever | Select candidate evidence for a query. |
| Rerank | Reranker or scorer | Put the strongest evidence first. |
| Plan | Model or runtime | Decide whether an answer or tool call is needed. |
| Act | Tool executor | Call allowed tools with structured arguments. |
| Observe | Runtime state | Record tool results exactly. |
| Synthesize | Model | Produce answer grounded in evidence and observations. |
| Evaluate | Eval harness | Measure retrieval, groundedness, tool safety, and task success. |

Every step should leave enough trace data that a failure can be debugged later.

## Core Invariant

The system must keep evidence, generated text, tool observations, and authority boundaries explicit.

If these boundaries blur, the model can treat guesses as facts, treat untrusted retrieved text as instructions, or take actions that should have required review.

## Worked Example

A support assistant receives: "Why did invoice 123 fail?"

| System Type | Behavior |
| --- | --- |
| RAG-only | Retrieve billing docs and answer with citations. |
| Tool-using | Query invoice status and payment logs, then answer from observations. |
| Agentic | Plan investigation, call tools, summarize evidence, create a ticket, and ask a human before issuing a refund. |

The last flow is more powerful, but every new action introduces state, security, and recovery concerns.

## State Or Flow Walkthrough

A production agent answering "Why did deployment 42 fail?" might run this timeline:

```text
1. record user goal
2. retrieve deployment docs and recent incident notes
3. call deployment API for rollout status
4. call logs API for failed pods
5. observe image pull error
6. draft explanation with citations and observations
7. ask for approval before rollback
8. if approved, call rollback tool and record result
```

The model decides parts of the flow, but the runtime owns the durable state, tool permissions, approval gates, and trace.

## Implementation Shape

A reliable RAG or agent system usually separates:

| Component | Responsibility |
| --- | --- |
| Ingestion | Parse, chunk, normalize, and index source material. |
| Retrieval | Find candidate chunks for a query. |
| Grounding | Bind answer claims to evidence. |
| Tool schema | Define tool names, arguments, and return shapes. |
| Runtime state | Persist messages, calls, observations, and checkpoints. |
| Policy engine | Decide what is allowed, denied, or requires approval. |
| Evaluator | Measure retrieval quality, groundedness, tool safety, and task success. |

Do not hide all of this inside one prompt. The prompt is only one part of the system.

## Failure Modes

| Failure | Example |
| --- | --- |
| Retrieval miss | The answer is fluent but based on irrelevant context. |
| Context stuffing | Too many chunks distract the model. |
| Prompt injection | Retrieved text tells the model to ignore policy. |
| Tool confusion | The model treats a failed call as a successful observation. |
| Lost checkpoint | A long-running agent cannot recover after process restart. |
| Silent mutation | A tool changes real state without trace or approval. |

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| RAG from scratch | Chunking, retrieval, reranking, citations, and grounded answer generation. |
| GraphRAG knowledge system | Relationship-aware retrieval and evidence graph traversal. |
| Agent runtime | State, tool schemas, observations, retries, and checkpoints. |
| MCP server/client lab | Tool protocol boundaries and structured capability exposure. |
| LLM evals harness | Retrieval quality, groundedness, and tool-safety measurement. |

## Exercise Bridge

RAG exercises should force you to implement chunking, retrieval, citation, and evaluation separately. Agent exercises should force you to model state, tool schemas, retries, approval, and traces. Before coding, name which components are read-only and which can mutate the world.

## Readiness Checklist

You are ready for RAG/agent exercises when you can:

- separate generated text from retrieved evidence
- identify which tools are read-only and which mutate state
- explain where prompt injection can cross a boundary
- define what a trace must record
- evaluate retrieval separately from final answer quality

## Self-Check

1. What evidence supports the answer?
2. Which actions are read-only and which mutate state?
3. Where can a human approve or stop the workflow?
4. How do you evaluate retrieval separately from generation?
5. What happens if a tool call succeeds but the runtime crashes before recording the observation?

## Further Reading

- RAG paper: https://arxiv.org/abs/2005.11401
- ReAct paper: https://arxiv.org/abs/2210.03629
- Toolformer paper: https://arxiv.org/abs/2302.04761
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/latest
- Microsoft GraphRAG: https://microsoft.github.io/graphrag/
