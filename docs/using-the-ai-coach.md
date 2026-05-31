# Using The AI Coach

The repository includes a portable coaching skill:

```text
skills/interactive-learning-coach/
```

The skill tells an AI coding agent how to teach concepts, give layered hints, validate implementations, and review code like a Staff engineer. It is platform-neutral Markdown, with thin adapters for specific tools.

Install details are in [Portable Skill Installation](portable-skill-install.md).

## What The Coach Should Do

The coach should:

- read the local exercise, tests, and source files before advising
- teach the concept before implementation unless you ask to skip
- give hints without spoiling the final implementation
- explain approaches in natural language
- run validators and summarize failures
- review correctness, failure modes, concurrency, durability, observability, and tests
- suggest the next task when you finish

The coach should not dump complete solutions by default. Ask explicitly if you want one.

## High-Signal Prompts

Start a session:

```text
Use $interactive-learning-coach. I want to start the next exercise in go-concurrency. Teach the concept first, then give me the implementation contract.
```

Ask for a hint:

```text
Use $interactive-learning-coach. Give me Hint 1 for the current exercise. Do not show code yet.
```

Ask for an approach:

```text
Use $interactive-learning-coach. Explain the approach in natural language. Name the invariant and the likely pitfall, but do not write the implementation.
```

Validate:

```text
Use $interactive-learning-coach. Run the validator for this exercise and explain the smallest next fix.
```

Review:

```text
Use $interactive-learning-coach. Review my implementation like a Staff engineer. Focus on correctness, failure modes, and missing tests.
```

Find the next task:

```text
Use $interactive-learning-coach. Based on my completed exercises, give me the next task and explain why it is next.
```

Go deeper:

```text
Use $interactive-learning-coach. Teach this concept more deeply and give me references worth reading after I finish the lab.
```

## Example Workflow

This is the recommended step-by-step flow for using the skill with this repository.

### 1. Install The Skill

Codex:

```bash
npx build-your-own-systems-skill install codex
```

Claude Code:

```bash
npx build-your-own-systems-skill install claude
```

Cursor project:

```bash
npx build-your-own-systems-skill install cursor --cwd .
```

Generic project:

```bash
npx build-your-own-systems-skill install generic --cwd .
```

Use `--force` when updating an existing install.

### 2. Open The Curriculum Repo

Start from the repository root:

```bash
tools/learn.py tracks
tools/learn.py next --track go-concurrency
```

You can choose any track, but `go-concurrency` is the recommended first path.

### 3. Ask The Coach To Start The Exercise

```text
Use $interactive-learning-coach. Start the next exercise in go-concurrency.
First read the local exercise, tests, and source files. Then teach me the concept before I implement anything.
```

Expected coach behavior:

- identifies the next exercise
- reads the exercise markdown and tests
- explains the mental model
- names the core invariant
- gives a tiny example
- stops before writing the full solution

### 4. Ask For The Implementation Contract

```text
Use $interactive-learning-coach. Summarize the implementation contract for this exercise.
Tell me the files to edit, the validator command, and the edge case I should handle first.
```

Now inspect the files yourself:

```bash
tools/learn.py show <exercise-id> --open exercise
tools/learn.py show <exercise-id> --open concept
tools/learn.py validate <exercise-id>
```

The validator should fail before you implement the placeholder.

### 5. Ask For A Hint Without Spoiling The Solution

```text
Use $interactive-learning-coach. Give me Hint 1 only. Do not write code.
Focus on the state I should track and the invariant I must preserve.
```

If still stuck:

```text
Use $interactive-learning-coach. Give me Hint 2. Still avoid full code.
```

### 6. Implement The Solution Yourself

Edit the files listed in the exercise.

Keep the first pass simple:

- model the state explicitly
- implement validation before mutation
- keep output ordering deterministic
- handle the boundary case in the tests

Run:

```bash
tools/learn.py validate <exercise-id>
```

### 7. Ask The Coach To Debug A Failure

If validation fails:

```text
Use $interactive-learning-coach. Run the validator for this exercise.
Explain the first meaningful failure and the smallest next fix. Do not rewrite the whole solution.
```

Expected coach behavior:

- runs the local validator
- summarizes the important failure
- points at the relevant file and behavior
- suggests one focused fix

### 8. Ask For Staff-Level Review

After tests pass:

```text
Use $interactive-learning-coach. Review my implementation like a Staff engineer.
Lead with correctness issues. Check failure modes, idempotency, ordering, observability, and missing tests.
```

A good review should answer:

- what invariant the code protects
- where the implementation can still fail
- which test proves the hardest claim
- what behavior would matter in production

### 9. Mark The Exercise Complete

When you can explain the invariant and failure mode:

```bash
tools/learn.py complete <exercise-id>
tools/learn.py next
```

Then repeat the loop.

### 10. Continue A Project Ladder

For project ladders, each project has five exercises:

1. core mechanism and first invariant
2. state model and invariants
3. operation planner and deterministic diffs
4. failure, retry, and recovery boundary
5. integration simulation and operational report

Ask:

```text
Use $interactive-learning-coach. Continue the current project ladder.
Show me what changed conceptually from the previous exercise to this one.
```

## Working Without Native Skill Support

If your tool does not support skills:

1. Keep `skills/interactive-learning-coach/` in the repository.
2. Copy [adapters/generic/AGENTS.md](../adapters/generic/AGENTS.md) to `AGENTS.md` at the repo root.
3. Ask the agent to read `skills/interactive-learning-coach/SKILL.md`.

Example:

```text
Read skills/interactive-learning-coach/SKILL.md and use it as your operating instructions for this repo.
Then help me with the next database-systems exercise.
```

## Review Expectations

A good review should lead with findings, not encouragement.

Ask the coach to check:

- invariant violations
- mutation leaks
- idempotency problems
- retry and replay behavior
- ordering and determinism
- race conditions
- crash/recovery gaps
- tests that pass accidentally
- missing operational visibility

The review is part of the curriculum. Treat it like the moment where tests become engineering judgment.
