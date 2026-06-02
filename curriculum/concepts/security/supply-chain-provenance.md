# Supply-Chain Provenance

## What You Should Know First

You should be comfortable with HTTP basics, identities, permissions, secrets, logs, and the idea that inputs can be adversarial.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How builds and dependencies prove where artifacts came from.

In real systems, security failures happen when systems trust the wrong boundary or forget who can cause an action. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How builds and dependencies prove where artifacts came from. |
| Asset | Something valuable enough to protect. |
| Principal | The user, service, job, or tool requesting access. |
| Control | A preventive, detective, or recovery mechanism that reduces risk. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of supply-chain provenance as assets, actors, trust boundaries, controls, and evidence arranged around abuse cases.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Name the asset | Decide what must remain confidential, intact, available, or attributable. |
| Map the boundary | Identify which components, users, networks, and tools are trusted. |
| Describe abuse | Write the attacker goal before designing the defense. |
| Add controls | Choose validation, authorization, isolation, rotation, provenance, or monitoring. |
| Log useful evidence | Record enough facts to investigate without leaking secrets. |
| Test misuse | Write tests for bypasses, replay, confused deputy behavior, and unsafe defaults. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For supply-chain provenance, the invariant is:

> The system must preserve the explicit state contract for how builds and dependencies prove where artifacts came from, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on supply-chain provenance. Start with one operation, one state variable, and one failure path.

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
| Request crosses boundary | A user, service, dependency, tool, artifact, or untrusted input asks for action. | Identify the trust boundary before trusting fields. |
| Identity and authority are checked | Authentication, authorization, policy, session, secret, or provenance controls run. | Identity alone does not grant permission. |
| Sensitive action is attempted | The system reads data, writes state, executes code, issues credentials, or calls a tool. | Controls must run before the irreversible side effect. |
| Evidence is recorded | Audit logs, provenance, alerts, or trace metadata capture the decision. | Do not leak secrets while creating useful forensic evidence. |
| Abuse path is tested | Replay, bypass, confused deputy, injection, or unsafe defaults are exercised. | Security confidence comes from negative tests, not only happy-path tests. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Policy model | Represents who can do what under which conditions. |
| Boundary check | Runs before sensitive state changes. |
| Secret handling | Avoids exposing credentials in logs, files, prompts, or traces. |
| Audit path | Leaves durable evidence of security-relevant decisions. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Authentication as authorization | Knowing who someone is does not say what they may do. |
| Trusting caller-provided metadata | Attackers choose the fields that weak checks accept. |
| Leaking in observability | Logs and traces become another secret store. |
| No abuse tests | The happy path passes while the exploit path is untested. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| security-engineering and agent-security ladders | Use this chapter before opening project-specific placeholders that rely on supply-chain provenance. |
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

You are ready to implement an exercise using supply-chain provenance when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by supply-chain provenance that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - Useful once the chapter mental model is clear.
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) - Useful once the chapter mental model is clear.
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) - Useful once the chapter mental model is clear.
