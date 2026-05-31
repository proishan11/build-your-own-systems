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

## Exercise Bridge

RAG exercises should force you to implement chunking, retrieval, citation, and evaluation separately. Agent exercises should force you to model state, tool schemas, retries, approval, and traces. Before coding, name which components are read-only and which can mutate the world.

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
