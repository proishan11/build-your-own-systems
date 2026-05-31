# Learning Workflow

This curriculum is not meant to be consumed like a list of coding puzzles. Each exercise is a small book chapter followed by a lab.

The intended skill is not only "make tests pass." The intended skill is: understand an invariant, implement it, validate it, and review it under failure.

## The Exercise Shape

Every substantial exercise should contain:

- Concept Primer: the idea in plain language.
- Why This Matters: where the idea appears in real systems.
- Mental Model: how to reason about the mechanism.
- Core Invariant: what must remain true.
- Tiny Example: a small walkthrough before coding.
- Common Misconceptions: traps to avoid.
- Self-Check: questions to answer before implementation.
- Contract: observable behavior your code must satisfy.
- Design Hints: direction without full code.
- Validation: exact command to run.
- Staff-Level Review Questions: how to pressure-test your solution.

Read those sections in order. They are there to slow you down in the useful way.

## The Four Passes

Use four passes per exercise.

### Pass 1: Learn

Read the exercise and concept chapter. Write down:

- the state owned by the component
- the invariant
- the boundary case
- the failure mode

If you cannot explain the invariant, do not start coding yet.

### Pass 2: Implement

Open the files listed in "Files To Edit." Implement only the required contract.

Keep the first implementation boring:

- explicit data structures
- deterministic ordering
- clear error cases
- small functions
- no speculative abstractions

### Pass 3: Validate

Run:

```bash
tools/learn.py validate <exercise-id>
```

Read the first meaningful failure. Fix one behavior at a time.

For Go exercises, some validators may run `go test ./...` or race checks. For project ladder exercises, validators usually run one Python test file for the current milestone.

### Pass 4: Review

After tests pass, review the solution against Staff-level questions:

- What invariant does this code protect?
- What input can violate the invariant?
- What happens on retry, replay, timeout, crash, or partial update?
- What state is exposed to callers?
- What would you log, trace, or measure in production?
- Which test proves the hardest claim?

Ask the AI coach to review the code before marking it complete.

## Hint Discipline

Use hints in layers:

1. Hint 1: mental model or state shape.
2. Hint 2: branch structure or edge case.
3. Hint 3: near-code approach.
4. Solution: only when you explicitly want to compare.

This keeps you in the driver's seat. The goal is to build your reasoning muscles, not outsource the interesting part.

## Choosing A Path

Use the foundation exercises when you want a curated systems base:

- `go-concurrency`
- `database-systems`
- `distributed-systems`
- `deep-networking`
- `tooling-foundations`
- `os-kernel-labs`

Use project ladders when you want breadth or a specific domain:

- LLM engineering
- RAG and agents
- Kubernetes and containers
- PostgreSQL administration
- security engineering
- performance engineering
- operating systems
- networking
- system design and SRE

List tracks:

```bash
tools/learn.py tracks
```

List a track:

```bash
tools/learn.py list --track ai-rag-agents
```

## Completion Standard

Mark an exercise complete when all are true:

- validator passes
- you can explain the invariant
- you can explain the hardest test
- you can name one failure mode not yet tested
- you can describe what the next milestone should add

Command:

```bash
tools/learn.py complete <exercise-id>
```
