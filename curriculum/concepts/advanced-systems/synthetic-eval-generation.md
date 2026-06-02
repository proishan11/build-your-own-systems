# Synthetic Eval Generation

## What You Should Know First

You should be comfortable with the earlier systems tracks, including storage, networking, distributed systems, security, performance, and AI workflows.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How systems create test cases that expand coverage without replacing human judgment.

In real systems, advanced systems combine multiple failure models, trust models, and runtime constraints in one design. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How systems create test cases that expand coverage without replacing human judgment. |
| Composition | Combining mechanisms whose guarantees must still hold together. |
| Boundary | The place where assumptions change between components, organizations, or machines. |
| Tradeoff | A design choice that buys one property by spending another. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of synthetic eval generation as a composition problem where every layer contributes both capability and new failure modes.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| State the combined goal | Name which earlier concepts are being composed and why. |
| List assumptions | Write down trust, failure, performance, and compatibility assumptions. |
| Design the protocol or runtime | Define interfaces, metadata, state transitions, and ownership. |
| Constrain unsafe cases | Add validation, isolation, versioning, or recovery rules. |
| Measure the tradeoff | Track cost, latency, safety, compatibility, and operability. |
| Review evolution | Ask how the design survives scale, new users, and changed dependencies. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For synthetic eval generation, the invariant is:

> The system must preserve the explicit state contract for how systems create test cases that expand coverage without replacing human judgment, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on synthetic eval generation. Start with one operation, one state variable, and one failure path.

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
| Layers meet | A build action, mesh proxy, eBPF program, confidential workload, WASM component, or AI artifact crosses a boundary. | Write down what each layer assumes before composing them. |
| Contract is checked | Capabilities, provenance, versions, trust, resource limits, or merge semantics are validated. | Advanced systems fail when one layer assumes another guarantee silently. |
| Mechanism runs | The system executes remotely, routes traffic, observes the kernel, isolates data, merges state, or coordinates agents. | Powerful mechanisms need explicit blast-radius limits. |
| Evidence is produced | Attestations, traces, measurements, cache keys, policies, or eval cases explain the action. | The more advanced the system, the more valuable evidence becomes. |
| Evolution is reviewed | Compatibility, migration, rollback, and abuse cases are considered. | A deep prototype is not complete until it can change safely. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Boundary contract | Describes what each layer promises and requires. |
| State machine | Captures transitions and invalid states. |
| Compatibility layer | Handles versions, migrations, or partial adoption. |
| Evidence path | Records why a decision was made and whether it worked. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Guarantee mismatch | One layer assumes a property another layer does not provide. |
| Opaque failure | Debugging requires crossing too many hidden boundaries. |
| Security afterthought | New power is added before trust boundaries are redesigned. |
| No migration story | The system works only as a greenfield prototype. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| advanced follow-on projects across distributed systems, platform, and AI systems | Use this chapter before opening project-specific placeholders that rely on synthetic eval generation. |
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

You are ready to implement an exercise using synthetic eval generation when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by synthetic eval generation that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [Designing Data-Intensive Applications](https://dataintensive.net/) - Useful once the chapter mental model is clear.
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - Useful once the chapter mental model is clear.
- [Papers We Love](https://github.com/papers-we-love/papers-we-love) - Useful once the chapter mental model is clear.
