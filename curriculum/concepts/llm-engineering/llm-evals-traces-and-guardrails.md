# Evals, Traces, and Guardrails

## What You Should Know First

You should know that LLM outputs are probabilistic and that a model can produce plausible text that is incomplete, unsupported, unsafe, or incorrectly structured.

## The Problem

Traditional tests work well when the expected output is exact. LLM applications often need a different kind of evidence. A good answer may have several valid phrasings, while a bad answer may look polished.

Evals, traces, and guardrails create an engineering loop around model behavior. Evals measure quality. Traces explain what happened. Guardrails constrain shape, policy, or risk.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Eval case | Input, expected behavior, and grading rule. |
| Golden dataset | Curated set of examples used repeatedly for comparison. |
| Trace | Structured record of prompt, model call, tool calls, retrieval, outputs, and timings. |
| Rubric | Criteria used to judge output quality. |
| Guardrail | Constraint or check applied before, during, or after model generation. |
| Regression | A change that worsens behavior compared with a baseline. |
| Groundedness | Degree to which claims are supported by supplied evidence. |

## Mental Model

Treat an LLM feature like a distributed system with uncertain components:

```text
input -> prompt -> retrieval/tools -> model -> parser/checks -> user-visible result
```

If the final result is wrong, you need enough trace data to know whether the issue came from retrieval, prompt design, tool output, model behavior, parsing, or policy.

## How It Works Step By Step

An LLM engineering loop should make model behavior inspectable and comparable.

| Step | Artifact | Purpose |
| --- | --- | --- |
| Define task | Task contract and risk level. | Clarifies what good output means. |
| Build eval set | Inputs, expected behavior, slices, and metadata. | Makes comparison repeatable. |
| Run system | Model, prompt, retrieval, tools, parser. | Produces outputs under controlled configuration. |
| Capture trace | Prompt, context, tool calls, timings, costs, outputs. | Makes failures debuggable. |
| Grade | Exact checks, rubric, model judge, or human review. | Converts behavior into evidence. |
| Compare baseline | New run versus previous run. | Detects regressions and tradeoffs. |
| Gate release | Thresholds for quality, safety, cost, or latency. | Prevents accidental degradation. |

The goal is not perfect measurement. The goal is disciplined measurement that gets better as failures teach you what to add.

## Core Invariant

Quality claims should be backed by reproducible examples, structured traces, and explicit grading criteria.

"It seemed better in a few manual tests" is not enough once the system matters to users.

## Worked Example

A structured-output assistant must return JSON for support ticket classification.

| Check | Question |
| --- | --- |
| Schema validation | Is the output parseable and does it match required fields? |
| Classification eval | Does the label match the expected category? |
| Safety guardrail | Did the answer avoid disallowed actions? |
| Trace inspection | Which prompt, model, retrieved docs, and tool calls produced the result? |
| Regression comparison | Did the new prompt improve one class while harming another? |

One failing example is not only a bug. It is also a new candidate for the eval set.

## State Or Flow Walkthrough

A support classifier returns JSON with `category`, `priority`, and `rationale`.

| Failure | Which Layer Catches It |
| --- | --- |
| Invalid JSON | Schema validator. |
| Wrong category | Eval grader against expected label. |
| Unsupported rationale | Groundedness or citation check. |
| Unsafe recommendation | Guardrail or policy check. |
| Slow or expensive response | Trace and metrics comparison. |

One example can fail several layers. Keeping those layers separate tells you whether to fix the prompt, retrieval, tool behavior, parser, or policy.

## Implementation Shape

A practical eval harness often includes:

| Component | Responsibility |
| --- | --- |
| Dataset loader | Reads eval cases and expected criteria. |
| Runner | Executes model, retrieval, and tool flows consistently. |
| Grader | Applies exact, semantic, rubric, or human review scoring. |
| Trace store | Records inputs, intermediate steps, outputs, timings, and costs. |
| Reporter | Compares runs and highlights regressions. |
| Gate | Fails builds or blocks rollout when quality drops too far. |

The right grader depends on the task. Exact matching is useful for JSON shape, but weak for summarization quality.

## Failure Modes

| Failure | Result |
| --- | --- |
| Tiny eval set | Optimizations overfit a handful of examples. |
| No trace store | Failures cannot be debugged after the fact. |
| Vague rubric | Scores vary wildly between reviewers. |
| Only aggregate scores | Averages hide catastrophic failures in important slices. |
| Guardrails without logging | Rejections cannot improve the product or policy. |
| No baseline | Teams cannot tell whether a change helped. |

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| Structured output validator | Schema checks, parser behavior, and repair boundaries. |
| LLM trace store | Durable trace records and debugging fields. |
| LLM evals harness | Datasets, runners, graders, and regression reports. |
| Model router | Cost, latency, quality, and fallback tradeoffs. |
| Human approval workflow | Guardrails around risky model-suggested actions. |

## Exercise Bridge

LLM engineering exercises should ask you to build structured output validation, trace storage, eval runners, model routing, cost dashboards, and approval workflows. Before coding, decide which failures are correctness bugs, which are policy violations, and which are quality regressions.

## Readiness Checklist

You are ready for LLM engineering exercises when you can:

- define what one eval case proves
- identify high-risk slices separately from aggregate score
- reproduce a bad output from trace data
- explain which guardrails run before tool execution
- name the threshold that would block a rollout

## Self-Check

1. What does a passing eval actually prove?
2. Which examples represent high-risk user impact?
3. Can you reproduce a bad answer from trace data?
4. Which guardrails run before tool execution?
5. What metric would stop a rollout?

## Further Reading

- HELM evaluation framework: https://crfm.stanford.edu/helm/latest/
- RAGAS documentation: https://docs.ragas.io/
- OpenTelemetry concepts: https://opentelemetry.io/docs/concepts/
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
