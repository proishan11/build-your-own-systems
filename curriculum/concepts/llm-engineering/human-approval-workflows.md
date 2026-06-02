# Human Approval Workflows

## What You Should Know First

You should be comfortable with prompts, model APIs, structured outputs, traces, datasets, latency, cost, and human review workflows.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How high-risk model actions route through people with useful context.

In real systems, LLM products need software engineering around nondeterministic model calls, not only better prompts. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How high-risk model actions route through people with useful context. |
| Prompt version | A named prompt artifact that can be reviewed, tested, and rolled back. |
| Trace | The recorded path of inputs, retrieval, tools, model calls, outputs, and scores. |
| Gate | A policy that prevents unsafe or regressed behavior from shipping. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of human approval workflows as a product workflow with versioned prompts, typed outputs, traces, evals, routing, approvals, and cost controls.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Version the contract | Name the prompt, model, schema, tools, and expected output shape. |
| Run the workflow | Execute model calls with typed inputs, timeouts, retries, and trace capture. |
| Validate output | Check JSON shape, safety rules, citations, and business constraints. |
| Score examples | Run evals over datasets and compare to baseline. |
| Route intentionally | Choose model or human review paths based on risk, cost, and latency. |
| Monitor production | Track quality, cost, latency, drift, and approval outcomes. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For human approval workflows, the invariant is:

> The system must preserve the explicit state contract for how high-risk model actions route through people with useful context, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on human approval workflows. Start with one operation, one state variable, and one failure path.

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
| Workflow starts | A prompt version, model choice, schema, dataset, or user request enters the runtime. | The model call is part of a versioned software contract. |
| Runtime captures trace | Inputs, retrieval, tools, model params, output, latency, and cost are recorded. | Trace first, then debug; otherwise failures vanish. |
| Output is validated | Schemas, policies, citations, safety checks, or business rules evaluate the response. | Prose is not a stable API until it satisfies the contract. |
| Eval or routing decision runs | The system scores examples, gates release, routes models, or escalates to humans. | Quality, risk, latency, and cost all participate in the decision. |
| Production signal updates | Dashboards, baselines, approvals, and regression reports reflect behavior. | LLM engineering needs operational feedback, not just prompt edits. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Registry | Stores prompts, models, schemas, datasets, and versions. |
| Runtime | Executes model workflows and records traces. |
| Evaluator | Scores outputs and creates regression reports. |
| Policy engine | Routes, blocks, escalates, or approves work. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Prompt drift | A behavior changes with no reviewable artifact. |
| Untyped output | Downstream code parses prose as if it were a stable API. |
| Eval overfitting | The system improves examples but not the real task. |
| Cost invisibility | Quality gains hide latency and spend regressions. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| llm-engineering and ai-rag-agents ladders | Use this chapter before opening project-specific placeholders that rely on human approval workflows. |
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

You are ready to implement an exercise using human approval workflows when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by human approval workflows that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [OpenAI Evals](https://github.com/openai/evals) - Useful once the chapter mental model is clear.
- [LangSmith tracing concepts](https://docs.smith.langchain.com/) - Useful once the chapter mental model is clear.
- [HumanLoop eval guides](https://humanloop.com/docs/evaluation/overview) - Useful once the chapter mental model is clear.
