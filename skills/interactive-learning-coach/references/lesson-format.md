# Lesson Format

Use this before implementation unless the user explicitly skips the learning stage.

## Default Lesson Shape

Keep the first pass compact:

1. **Concept:** name the idea in one sentence.
2. **Why it exists:** describe the problem it solves.
3. **Mental model:** give an analogy or operational model that maps to code.
4. **Core invariant:** state what must always be true.
5. **Tiny example:** walk through a minimal example without full implementation.
6. **Misconceptions:** list 2-4 traps beginners commonly hit.
7. **Self-check:** ask 2-4 questions before coding.
8. **Implementation bridge:** describe how the concept maps to this exercise.
9. **Deep dives:** list optional references, starting with approachable material.

## Tone

Teach like a good technical book:

- precise but not dense
- concrete before abstract
- one concept per section
- no performative jargon
- connect theory to the exact implementation task

## Depth Levels

Use the user's request to choose depth:

- **Quick primer:** 5-10 paragraphs, one tiny example.
- **Book section:** deeper explanation, diagrams in text, tradeoffs, historical context.
- **Paper guide:** explain what to read, which sections matter, and what questions to answer.
- **Implementation bridge:** short concept recap plus design approach.

## Self-Check Examples

Go concurrency:

- Who owns closing each channel?
- What happens if the receiver stops reading?
- Which goroutine can block forever?

Durable logs:

- What has to reach disk before success is acknowledged?
- What state can be rebuilt after restart?
- How do you recognize a torn final record?

Raft:

- What prevents two leaders in one term?
- Why is a majority quorum enough for safety?
- What must be persisted before responding?

Databases:

- What invariant does WAL enforce?
- Which operation is redoable?
- What is the difference between logical and physical records?

