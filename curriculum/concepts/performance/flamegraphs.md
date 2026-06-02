# Flamegraphs

## What You Should Know First

You should be comfortable with latency, throughput, CPU, memory, queues, locks, measurement noise, and basic benchmarking.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How stack-sample visualizations show where time or CPU accumulates.

In real systems, performance work fails when teams optimize without a workload, baseline, or explanation for the bottleneck. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How stack-sample visualizations show where time or CPU accumulates. |
| Workload | The request mix, data size, concurrency, and environment being measured. |
| Bottleneck | The limiting resource or dependency on the critical path. |
| Regression | A measurable performance loss relative to a defined baseline. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of flamegraphs as a measured feedback loop from workload to symptom to profile to change to regression guard.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Define the workload | Write down request shape, concurrency, data size, and success criteria. |
| Measure baseline | Capture latency distribution, throughput, resource usage, and variance. |
| Profile the path | Find where time, allocation, waits, or contention accumulate. |
| Form one hypothesis | Explain why one change should move one metric. |
| Compare fairly | Run before/after measurements with the same workload and environment. |
| Guard the result | Add thresholds or dashboards that catch future regressions. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For flamegraphs, the invariant is:

> The system must preserve the explicit state contract for how stack-sample visualizations show where time or CPU accumulates, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on flamegraphs. Start with one operation, one state variable, and one failure path.

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
| Workload is defined | Request mix, data size, concurrency, environment, and success metric are fixed. | A benchmark without a workload definition is just a story. |
| Baseline is measured | Latency distribution, throughput, CPU, memory, allocation, waits, or errors are captured. | Percentiles and variance matter as much as averages. |
| Profile explains cost | Stacks, locks, queues, allocations, or resource saturation identify the bottleneck. | Optimize only after evidence points to the critical path. |
| One change is made | The implementation alters one variable and reruns the same workload. | Multiple changes make the result impossible to explain. |
| Regression guard remains | Thresholds, dashboards, or CI checks catch future performance loss. | A win that cannot be protected will eventually disappear. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Benchmark harness | Runs a repeatable workload. |
| Metric collector | Records percentiles, rates, resource usage, and errors. |
| Profiler hook | Captures stack, allocation, lock, or queue evidence. |
| Regression gate | Compares results against an explicit baseline. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Average-only reasoning | Mean latency hides p95 and p99 harm. |
| Benchmarking the wrong workload | The lab result does not match the real critical path. |
| Changing many variables | No one can explain which change helped. |
| No guardrail | The same bug returns in a later refactor. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| performance-engineering and SRE ladders | Use this chapter before opening project-specific placeholders that rely on flamegraphs. |
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

You are ready to implement an exercise using flamegraphs when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by flamegraphs that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [Systems Performance](https://www.brendangregg.com/systems-performance-2nd-edition-book.html) - Useful once the chapter mental model is clear.
- [USE Method](https://www.brendangregg.com/usemethod.html) - Useful once the chapter mental model is clear.
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - Useful once the chapter mental model is clear.
