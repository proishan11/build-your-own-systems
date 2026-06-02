# Owner References

## What You Should Know First

You should be comfortable with Linux processes, filesystems, images, APIs, YAML-style desired state, and service ownership.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How Kubernetes records object ownership for garbage collection.

In real systems, container platforms work by turning desired state into isolated processes and continuously reconciled infrastructure. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How Kubernetes records object ownership for garbage collection. |
| Desired state | The state a user or controller wants the system to converge toward. |
| Control loop | A repeated observe-diff-act cycle. |
| Isolation primitive | A kernel mechanism that limits what a process can see or use. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of owner references as declarative control loops over API objects plus lower-level Linux isolation primitives.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Represent desired state | Encode intent in an object, image, namespace, policy, or scheduling request. |
| Observe actual state | Read API objects, node resources, process state, or runtime metadata. |
| Compute the delta | Decide which create, update, delete, bind, or reject action is needed. |
| Act idempotently | Make actions safe to retry after timeouts and crashes. |
| Record status | Publish conditions, events, metrics, and ownership edges. |
| Handle lifecycle edges | Test deletion, finalization, RBAC denial, scheduling failure, and restart. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For owner references, the invariant is:

> The system must preserve the explicit state contract for how Kubernetes records object ownership for garbage collection, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on owner references. Start with one operation, one state variable, and one failure path.

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
| Desired state is declared | An object, image, namespace, policy, or scheduling request describes intent. | Declarative state is the source of truth. |
| Actual state is observed | The API server, cache, node, runtime, or controller reports current state. | Watch streams and caches can lag; design for reconciliation. |
| Delta is computed | The controller, runtime, or scheduler decides create, update, delete, bind, reject, or cleanup. | The action should be safe to repeat. |
| Status or ownership changes | Conditions, events, finalizers, owner refs, or resource accounting are updated. | Lifecycle metadata is how the platform cleans up and explains itself. |
| Policy edge is handled | RBAC denial, admission failure, resource pressure, or deletion races are handled. | Platform correctness lives in the awkward lifecycle edges. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| API object | Defines the desired state contract. |
| Watcher or runtime reader | Observes current state. |
| Reconciler | Turns differences into idempotent actions. |
| Status writer | Records evidence and next-step conditions. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Imperative drift | Manual changes fight the controller or runtime. |
| Unsafe retry | A timed-out create action duplicates work. |
| Missing ownership | Garbage collection or cleanup cannot know what belongs together. |
| Privilege confusion | A container or controller receives broader access than intended. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| containers-kubernetes ladders | Use this chapter before opening project-specific placeholders that rely on owner references. |
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

You are ready to implement an exercise using owner references when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by owner references that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [Kubernetes API concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/) - Useful once the chapter mental model is clear.
- [Kubernetes controllers](https://kubernetes.io/docs/concepts/architecture/controller/) - Useful once the chapter mental model is clear.
- [OCI image spec](https://github.com/opencontainers/image-spec) - Useful once the chapter mental model is clear.
