# LLM Evals, Traces, and Guardrails

## Concept

Production LLM systems need evals to measure behavior, traces to explain behavior, and guardrails to constrain behavior around risky inputs, outputs, and tool calls.

## Why It Exists

LLM behavior is probabilistic and context-sensitive. A prompt change, model change, retrieval change, or tool schema change can alter behavior in surprising ways. Tests must measure the system, not just individual functions.

## Mental Model

```text
input -> context assembly -> model/tool loop -> output
             |                  |
          trace              guardrails
             |
           evals
```

Traces show what happened. Evals decide whether it was good enough. Guardrails define what must not happen.

## Core Invariant

Every consequential model output or tool action must be attributable to its input context, model/tool decisions, and policy checks.

## Tiny Example

A support agent proposes refunding an order. The trace should show the user request, retrieved policy, tool calls, model output, approval decision, and final action. An eval should catch unsupported refunds.

## Common Misconceptions

- JSON mode is not a correctness proof.
- Guardrails in prompts are weaker than typed validation and policy checks.
- Passing golden examples does not prove robustness.
- Tool calls are part of the security boundary.

## Self-Check

1. What is being evaluated: retrieval, reasoning, output, or tool use?
2. What trace data is needed to debug a bad answer?
3. Which actions need human approval?
4. How do you prevent prompt injection from reaching tools?

## Further Reading

- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- OpenAI Agents SDK evolution: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- LangGraph docs: https://docs.langchain.com/oss/python/langgraph
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications

