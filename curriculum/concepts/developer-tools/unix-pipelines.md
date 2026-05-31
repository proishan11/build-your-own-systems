# Unix Pipelines

## Concept

Unix pipelines connect small programs using standard input and standard output. Each tool does one transformation; the shell composes them.

## Why It Exists

Pipelines let users build powerful workflows without writing a new program for every task. They are also a practical lesson in streams, processes, file descriptors, backpressure, and exit status.

## Mental Model

```bash
cat access.log | grep ERROR | sort | uniq -c
```

Each process reads bytes, writes bytes, and exits with a status. The shell wires the file descriptors.

## Core Invariant

Each stage should consume input, produce output, and report failure through exit status without corrupting the stream contract.

## Tiny Example

`grep ERROR` does not need to know whether input came from a file, another process, or a terminal. It just reads stdin.

## Common Misconceptions

- Text streams are interfaces.
- Exit status is data too.
- `stderr` should not be mixed with machine-readable `stdout`.
- Backpressure appears when a downstream process cannot read fast enough.

## Self-Check

1. Which file descriptors are connected?
2. What happens when downstream exits early?
3. What should go to stdout versus stderr?
4. How does the shell learn a command failed?

## Further Reading

- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/coreutils.html
- Bash manual: https://www.gnu.org/software/bash/manual/

