# Durable Agent Execution

## What You Should Know First

You should be comfortable with documents, embeddings, prompts, model calls, tool calls, JSON schemas, and evaluation datasets.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How long-running agents checkpoint decisions, tool results, and resumable state.

In real systems, AI applications are unreliable when retrieval, model behavior, tools, and evaluation are not designed as a system. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How long-running agents checkpoint decisions, tool results, and resumable state. |
| Context | The information supplied to the model for a particular request. |
| Tool | A callable capability exposed to an agent or model workflow. |
| Grounding | Tying an answer to retrievable evidence rather than model memory alone. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of durable agent execution as a probabilistic application pipeline with explicit evidence, actions, policies, and measurement.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Define the task | State what the user needs and what evidence or tools may be used. |
| Prepare context | Chunk, embed, retrieve, rerank, summarize, or validate inputs. |
| Constrain action | Use schemas, allowlists, policies, and sandboxing around model or tool calls. |
| Generate with evidence | Ask the model to answer using the available context and cite support when required. |
| Evaluate behavior | Measure correctness, grounding, safety, cost, latency, and failure slices. |
| Persist traces | Store enough request, retrieval, tool, and model metadata for review. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For durable agent execution, the invariant is:

> The system must preserve the explicit state contract for how long-running agents checkpoint decisions, tool results, and resumable state, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on durable agent execution. Start with one operation, one state variable, and one failure path.

| Moment | Learner Question | Expected Reasoning |
| --- | --- | --- |
| Before the operation | What state is valid right now? | Name the data structure, boundary, or external promise before touching code. |
| During the operation | What can observe a partial change? | Decide whether the change is hidden, visible, retryable, or must be rolled back. |
| After success | What proves the operation completed? | Return a value, write durable state, publish status, emit telemetry, or update a version. |
| After failure | What state is still allowed? | Preserve the invariant and leave enough evidence to retry, recover, or reject. |

This tiny exercise is worth doing before the full project. It turns vague understanding into an implementation contract.

## State Or Flow Walkthrough

| Phase | State/Flow | What To Watch |
| --- | --- | --- |
| User task arrives | A question, goal, document set, tool request, or agent instruction enters the workflow. | Clarify whether the system needs evidence, action, or both. |
| Context is assembled | Chunks, embeddings, search results, reranked passages, memory, or tool state are selected. | More context is not automatically better context. |
| Model or agent acts | The workflow generates text, chooses a tool, emits structured output, or asks for approval. | Tool arguments and outputs must stay inside policy. |
| Grounding is checked | Citations, retrieval scores, schemas, eval scores, or guardrails validate the result. | A fluent answer still needs evidence. |
| Trace is stored | Prompt, context, model, tool calls, costs, latency, and scores become debuggable evidence. | Without traces, failures become folklore. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Ingestion path | Turns source data into searchable or actionable state. |
| Retriever or planner | Chooses evidence or tools. |
| Policy layer | Constrains unsafe prompts, tools, and outputs. |
| Eval harness | Scores examples and tracks regressions. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Pretty demos without evals | A few good answers hide weak retrieval or unsafe behavior. |
| Context as a dumping ground | Too much irrelevant text reduces answer quality. |
| Untrusted tool arguments | Prompt injection turns model text into unsafe action. |
| No traceability | Failures cannot be debugged after the response is gone. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| ai-rag-agents and LLM application ladders | Use this chapter before opening project-specific placeholders that rely on durable agent execution. |
| Foundation drills | Turn the invariant into one focused test before adding convenience behavior. |
| Staff review | Explain the failure model, the evidence you would inspect in production, and the tradeoff you accepted. |

When you open an exercise, copy the core invariant into your notes. Then find the placeholder function or class that is responsible for preserving it.

## Exercise Bridge

Before coding, write three sentences:

1. The state I own is ...
2. The operation is correct when ...
3. The failure case I must preserve is ...

Those sentences become your implementation plan and your first review checklist.

## Readiness Checklist

You are ready to implement an exercise using durable agent execution when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by durable agent execution that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [Retrieval-Augmented Generation paper](https://arxiv.org/abs/2005.11401) - Useful once the chapter mental model is clear.
- [ReAct paper](https://arxiv.org/abs/2210.03629) - Useful once the chapter mental model is clear.
- [RAGAS](https://docs.ragas.io/) - Useful once the chapter mental model is clear.
