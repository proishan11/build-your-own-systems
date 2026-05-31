# RAG, Agents, and Tool Use

## Concept

RAG gives a model external knowledge at answer time. Agents give a model a loop for choosing actions, using tools, observing results, and continuing toward a goal.

## Why It Exists

Language models are useful but bounded by context, training data, and lack of direct access to private systems. RAG connects models to relevant documents. Tool use connects models to actions. Agent runtimes add state, policy, recovery, tracing, and human checkpoints.

## Mental Model

RAG is an evidence pipeline:

```text
question -> retrieve -> rerank -> synthesize answer with citations
```

An agent is a control loop:

```text
goal -> plan -> tool call -> observation -> update state -> next action
```

Production systems often combine both: an agent calls retrieval tools, search tools, code tools, and workflow tools.

## Core Invariant

The system must keep evidence, actions, and authority boundaries explicit. The model should not silently confuse generated text, retrieved facts, and tool results.

## Tiny Example

A support assistant receives "Why did invoice 123 fail?" A RAG-only system retrieves invoice docs and answers. An agentic system might query billing, inspect logs, create a ticket, and ask a human before issuing a refund.

## Current Directions

As of May 2026, practical AI systems are moving toward:

- graph-structured retrieval for relationship-heavy corpora
- tool protocols such as MCP
- durable agent execution with checkpoints and traces
- human-in-the-loop approval for risky actions
- evaluation harnesses for retrieval quality, groundedness, and tool safety
- stronger sandboxing and policy around tool execution

## Common Misconceptions

- RAG does not automatically make answers correct; retrieval quality and synthesis matter.
- Agents are not magic autonomy; they are state machines with probabilistic decision points.
- Tool access is a security boundary.
- More retrieved context can make answers worse if it adds distractors.
- Traces are not optional once tools can mutate real systems.

## Self-Check

1. What evidence supports the answer?
2. Which actions are read-only and which mutate state?
3. Where can a human approve or stop the workflow?
4. How do you evaluate retrieval separately from generation?
5. What happens if a tool call succeeds but the model never observes the result?

## Further Reading

- RAG paper: https://arxiv.org/abs/2005.11401
- ReAct paper: https://arxiv.org/abs/2210.03629
- Toolformer paper: https://arxiv.org/abs/2302.04761
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/latest
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- LangGraph docs: https://docs.langchain.com/oss/python/langgraph
- Microsoft GraphRAG: https://microsoft.github.io/graphrag/

