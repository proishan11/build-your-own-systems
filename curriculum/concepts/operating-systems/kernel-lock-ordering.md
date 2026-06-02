# Kernel Lock Ordering

## What You Should Know First

You should be comfortable with processes, memory addresses, files, interrupts, and the difference between user code and kernel code.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How kernel code avoids deadlocks while protecting shared state.

In real systems, kernel code must multiplex unsafe hardware while preserving isolation and predictable semantics. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How kernel code avoids deadlocks while protecting shared state. |
| Privilege | The ability to execute operations ordinary user programs cannot. |
| Kernel state | Data structures that describe processes, memory, files, locks, and devices. |
| Isolation | The rule that one process should not corrupt another process or the kernel. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of kernel lock ordering as a privileged state machine that admits requests through narrow, checked boundaries.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Enter the boundary | Move from user mode, interrupt context, or scheduler context into trusted code. |
| Validate inputs | Check pointers, permissions, sizes, lock order, and current process state. |
| Update kernel state | Modify only the data structures protected by the right ownership rule. |
| Interact with hardware | Translate the request into page table, device, timer, or filesystem operations. |
| Return evidence | Copy results back safely or expose a clear error code. |
| Stress the edge | Test invalid pointers, preemption, concurrent calls, and partial failure. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For kernel lock ordering, the invariant is:

> The system must preserve the explicit state contract for how kernel code avoids deadlocks while protecting shared state, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on kernel lock ordering. Start with one operation, one state variable, and one failure path.

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
| Entry occurs | A syscall, interrupt, scheduler event, or fault transfers control to privileged code. | Save enough context to validate and eventually return. |
| Inputs are checked | Pointers, permissions, process state, lock order, or memory mappings are validated. | Never let untrusted user state become trusted kernel state by accident. |
| Kernel state changes | The kernel updates process, memory, file, scheduler, or journal structures. | The right lock or isolation rule must protect the mutation. |
| Hardware or storage is touched | Page tables, timers, disks, or devices observe the change. | Partial effects must still leave a recoverable state. |
| Control returns | Registers, error codes, mappings, or wakeups expose the result. | A failed operation should not corrupt later execution. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Trap or entry path | Captures a request and saves enough context to return. |
| Validator | Rejects invalid state before mutation. |
| Kernel object | Represents process, memory, lock, file, or scheduler state. |
| Recovery path | Leaves the kernel consistent when the operation cannot finish. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Trusting user input | Malformed pointers or sizes corrupt privileged memory. |
| Wrong lock order | Two kernel paths deadlock under real concurrency. |
| Lost context | A process resumes with registers, mappings, or files inconsistent. |
| Toy-only tests | The design works only without preemption or faults. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| os-kernel-labs and systems-programming ladders | Use this chapter before opening project-specific placeholders that rely on kernel lock ordering. |
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

You are ready to implement an exercise using kernel lock ordering when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by kernel lock ordering that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) - Useful once the chapter mental model is clear.
- [xv6 book](https://pdos.csail.mit.edu/6.828/2023/xv6/book-riscv-rev3.pdf) - Useful once the chapter mental model is clear.
- [Linux man-pages](https://man7.org/linux/man-pages/) - Useful once the chapter mental model is clear.
