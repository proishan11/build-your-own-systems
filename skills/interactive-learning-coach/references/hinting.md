# Hinting Ladder

Use progressive disclosure. The learner should feel unstuck, not robbed of the exercise.

## Hint 1: Orientation

Give a small conceptual nudge:

- Name the invariant.
- Point to the relevant test.
- Identify the kind of mechanism needed.
- Avoid naming the full implementation structure if possible.

Example:

> The output channel has one owner: the coordinator that knows all workers are done. Look at the test that cancels the context while results may still be blocked.

## Hint 2: Shape

Reveal the main control-flow or data-structure shape:

- Mention `sync.WaitGroup`, channel ownership, index map, checksum boundary, etc.
- Explain why this shape satisfies the invariant.
- Still avoid writing the whole code.

Example:

> Start workers in a loop and have each worker select on `ctx.Done()` and `in`. Use a separate closer goroutine that waits for the workers, then closes `out`.

## Hint 3: Implementation Plan

Give ordered steps that are close to code:

1. Validate inputs.
2. Create state.
3. Start workers.
4. Handle cancellation.
5. Close resources.
6. Return results.

Still do not paste a complete implementation unless asked.

## Solution Mode

Only enter solution mode when the user explicitly asks for the answer, asks the agent to implement it, or the task is not meant to be solved by the user.

In solution mode:

- Explain the design briefly.
- Implement the smallest correct solution.
- Run validation.
- Explain tradeoffs and remaining extension points.

