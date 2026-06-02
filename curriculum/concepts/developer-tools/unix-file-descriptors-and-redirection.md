# Unix File Descriptors and Redirection

## What You Should Know First

You should be comfortable with basic terminal use, processes, files, standard input, standard output, and exit status.

You do not need production experience with this topic yet. The goal of this chapter is to give you the vocabulary, state model, and correctness rule you need before you implement the exercise.

## The Problem

How shells and runtimes connect processes to files, pipes, terminals, and inherited resources.

In real systems, developer tools become unreliable when state, streams, and error reporting are implicit. A beginner usually sees the visible API first: a command, function, request, packet, query, or model call. The Staff-level move is to ask what state changes behind that API, what boundary is being crossed, and what must still be true when the happy path is interrupted.

This concept exists because intuition is not enough. You need a small model you can simulate in your head, then encode in tests.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Concept focus | How shells and runtimes connect processes to files, pipes, terminals, and inherited resources. |
| Descriptor | A small integer handle for an open file, pipe, terminal, or socket. |
| Contract | The part of tool behavior that scripts and humans can rely on. |
| Composition | Using one tool as a stable building block for another workflow. |
| Invariant | The correctness rule that must stay true across normal and failure paths. |

## Mental Model

Think of unix file descriptors and redirection as a small contract between a human command, a process, and the operating system.

That model is useful because it separates three questions:

| Question | Why It Matters |
| --- | --- |
| What state exists? | You cannot protect, recover, or test state you did not name. |
| Who may change it? | Most correctness bugs come from unclear ownership or stale authority. |
| What evidence proves it worked? | Production systems need observable proof, not just a returned value. |

## How It Works Step By Step

| Step | What You Do |
| --- | --- |
| Identify the boundary | Decide what comes from argv, stdin, files, environment, or editor state. |
| Make state visible | Name the descriptors, buffers, cursor positions, or repository objects the tool will touch. |
| Perform one operation | Apply the smallest transformation before adding convenience behavior. |
| Report separately | Keep machine-readable output, diagnostics, and status distinct. |
| Compose with neighbors | Check how this tool behaves when another command or editor action wraps it. |
| Test the contract | Use fixtures that prove success, failure, empty input, and malformed input. |

The step order is not ceremony. It is a way to keep the concept teachable: first make the boundary and state visible, then implement the operation, then test the places where reality disagrees with the clean diagram.

## Core Invariant

For unix file descriptors and redirection, the invariant is:

> The system must preserve the explicit state contract for how shells and runtimes connect processes to files, pipes, terminals, and inherited resources, even when inputs are malformed, operations are retried, work is concurrent, or failure happens halfway through.

A practical way to say the same thing: if you cannot explain who owns the state, when it may change, and how a broken attempt leaves it, the implementation is not ready.

## Worked Example

Imagine you are implementing a lab that depends on unix file descriptors and redirection. Start with one operation, one state variable, and one failure path.

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
| Command or edit request | Arguments, stdin, cursor position, file state, or process target enters the tool. | Keep user intent separate from hidden process or editor state. |
| State is resolved | Descriptors, buffers, refs, motions, files, or process ids become explicit objects. | Ambiguous state should be reported before mutation. |
| Operation runs | The tool reads, transforms, writes, moves, inspects, or reports one clear thing. | Preserve stdout, stderr, status, and repeatability. |
| Composition happens | Another command, script, editor action, or debugger uses the result. | The output contract must survive being reused by another tool. |
| Evidence remains | Exit status, deterministic output, or inspection output explains what happened. | The learner should be able to reproduce and script the behavior. |

## Implementation Shape

| Piece | Responsibility |
| --- | --- |
| Parser | Turns user-facing syntax into explicit operations. |
| State object | Represents descriptors, positions, refs, or inspected process facts. |
| Executor | Performs the operation without hiding errors. |
| Reporter | Writes data, diagnostics, and status through separate paths. |

Keep the first implementation small. Make the state explicit, write one failing test that names the invariant, implement the minimal behavior, then add edge cases around failure and concurrency.

## Failure Modes

| Failure Mode | Why It Happens |
| --- | --- |
| Hidden state | The command works interactively but scripts cannot predict it. |
| Mixed output | Diagnostics leak into data streams or structured output. |
| Implicit success | The tool hides a partial failure behind exit code 0. |
| Untested composition | The tool passes unit tests but breaks when piped, redirected, or repeated. |

The common pattern is pretending the environment is more polite than it is. Real callers retry, networks reorder, disks lie, users send malformed input, and model workflows drift. Your implementation should make those cases boring.

## Exercise Mapping

| Exercise Area | How This Chapter Helps |
| --- | --- |
| tooling-foundations and systems-programming ladders | Use this chapter before opening project-specific placeholders that rely on unix file descriptors and redirection. |
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

You are ready to implement an exercise using unix file descriptors and redirection when you can:

- explain the boundary this concept protects
- name the state that changes during the operation
- state the invariant without reading this chapter
- describe one realistic failure mode and the expected recovery behavior
- point to the test or validator that proves the invariant

## Self-Check

1. Which state is made explicit by unix file descriptors and redirection that would otherwise be hidden?
2. What is the smallest invariant you can test before implementing the full project behavior?
3. Which failure mode would be tempting to ignore in a toy implementation?
4. What evidence would you collect to debug this in a real system?
5. What tradeoff does this concept make between simplicity, correctness, performance, and operability?

## Further Reading

- [The Linux Programming Interface](https://man7.org/tlpi/) - Useful once the chapter mental model is clear.
- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) - Useful once the chapter mental model is clear.
- [Vim user manual](https://vimhelp.org/usr_toc.txt.html) - Useful once the chapter mental model is clear.
