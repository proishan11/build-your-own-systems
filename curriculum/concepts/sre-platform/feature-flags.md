# Feature Flags

## What You Should Know First

You should be comfortable with HTTP services, metrics, logs, traces, deploys, incidents, and the difference between user symptoms and internal causes.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How behavior changes are separated from deploys and controlled dynamically.

In real systems, platform systems need explicit reliability contracts, rollout controls, and operational evidence. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How behavior changes are separated from deploys and controlled dynamically. |
| SLO | A target for user-visible reliability over a window. |
| Telemetry | Metrics, logs, traces, profiles, and events used to understand behavior. |
| Control plane | The system that configures, routes, deploys, or governs production behavior. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of feature flags as a production feedback loop: define reliability, instrument behavior, control change, and learn from incidents.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Define user outcome | Name the availability, latency, correctness, or safety signal that matters. |
| Instrument the path | Emit metrics, logs, traces, and events at ownership boundaries. |
| Set the guardrail | Use SLOs, limits, flags, breakers, or rollout policies. |
| Operate change | Deploy progressively and observe both success and failure signals. |
| Respond to incidents | Use runbooks, ownership, timelines, and rollback paths. |
| Feed lessons back | Turn incidents and regressions into tests, alerts, and design changes. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For feature flags, the invariant is:

> The system must preserve the explicit state contract for how behavior changes are separated from deploys and controlled dynamically, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on feature flags. Start with one operation, one state variable, and one failure path.

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
| User-facing signal is defined | Availability, latency, correctness, saturation, or rollout health is named. | Reliability begins with the user-visible outcome. |
| Telemetry is emitted | Metrics, logs, traces, events, or profiles cross service boundaries with context. | Signals should explain ownership and causality. |
| Control is applied | SLOs, flags, limits, breakers, rollout stages, or runbooks shape behavior. | Controls protect users only when they can act quickly enough. |
| Incident or rollout changes state | The system mitigates, rolls back, escalates, or expands traffic. | Operations are part of the design, not an afterthought. |
| Learning feeds back | Postmortems, thresholds, dashboards, and tests change after new evidence. | A platform matures when production teaches the repo. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Signal model | Defines metrics and traces around user-visible behavior. |
| Policy mechanism | Rate limit, circuit break, flag, or rollout decision. |
| Runbook | Connects symptoms to commands and escalation. |
| Review loop | Turns production evidence into backlog changes. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Internal-only metrics | The system looks healthy while users are failing. |
| Static limits | Controls protect one workload and punish another. |
| No rollback path | A bad rollout can be detected but not stopped quickly. |
| Incident amnesia | The same failure repeats because no artifact changed. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| sre-system-design and platform ladders | Use this chapter before opening project-specific placeholders that rely on feature flags. |
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

You are ready to implement an exercise using feature flags when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by feature flags that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - Useful once the chapter mental model is clear.
- [OpenTelemetry documentation](https://opentelemetry.io/docs/) - Useful once the chapter mental model is clear.
- [Release It!](https://pragprog.com/titles/mnee2/release-it-second-edition/) - Useful once the chapter mental model is clear.
