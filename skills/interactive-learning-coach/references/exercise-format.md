# Exercise Format

Use this structure for new exercises.

## Required Sections

- **Concept Primer:** teach the idea before asking for code.
- **Why This Matters:** connect the concept to real systems.
- **Mental Model:** give the learner a concrete operational model.
- **Core Invariant:** state the property the implementation must preserve.
- **Tiny Example:** show a minimal walkthrough without solving the exercise.
- **Common Misconceptions:** point out likely traps.
- **Self-Check:** ask questions the learner should answer before coding.
- **Goal:** one concrete implementation outcome.
- **Concepts:** the computer-science ideas being practiced.
- **Files To Edit:** keep the scope clear.
- **Contract:** observable behavior the implementation must satisfy.
- **Design Hints:** conceptual guidance, not a complete solution.
- **Validation:** exact commands to run.
- **Further Reading:** primary papers, official docs, or high-quality articles.
- **Staff-Level Review Questions:** questions that force deeper reasoning.

## Placeholder Code Rules

- Stubs must compile.
- Tests should fail because behavior is missing, not because setup is broken.
- Comments should explain the intended design pressure.
- Public APIs should be stable enough for future exercises.
- Avoid implementing the solution in comments.

## Test Rules

Tests should:

- encode the contract
- use deterministic checks where possible
- avoid sleep-heavy concurrency tests unless there is no better option
- include one meaningful edge case
- leave room for multiple valid implementations

## Exercise Sizing

Prefer exercises that can be completed in 30-120 minutes. Split larger topics into milestones.

Good split:

- WAL record encoding
- WAL scanner
- partial-write recovery
- checksums
- segment rotation

Bad split:

- build a database

## Reference Rules

- Prefer official docs and original papers.
- Add approachable references before dense papers when the topic is new.
- Include why the reference is useful, not just the link.
- Keep references optional; the exercise should be learnable from the local concept primer.

