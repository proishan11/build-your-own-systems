# Unix Pipelines

## What You Should Know First

You should know that command-line programs read bytes from standard input, write normal output to standard output, write diagnostics to standard error, and finish with an exit status.

## The Problem

Large tools are hard to predict and hard to reuse. Unix pipelines solve this by encouraging small programs that do one transformation and compose through byte streams.

The shell connects these programs without each tool needing to know who produced its input or who will consume its output.

## Vocabulary

| Term | Meaning |
| --- | --- |
| stdin | File descriptor 0, usually the input stream. |
| stdout | File descriptor 1, normal output. |
| stderr | File descriptor 2, diagnostics and errors. |
| Pipe | Kernel buffer connecting one process's output to another process's input. |
| Exit status | Integer result that lets scripts decide success or failure. |
| Filter | Program that reads input, transforms it, and writes output. |
| Redirection | Shell syntax that connects file descriptors to files or other streams. |

## Mental Model

A pipeline is a stream graph:

```text
cat access.log | grep ERROR | sort | uniq -c
```

Each process runs independently. The kernel moves bytes from one process to the next through pipe buffers. If a later process stops reading, earlier processes may block or receive `SIGPIPE`.

## Core Invariant

A command-line tool should keep data output, diagnostic output, and process status separate.

This is what makes composition reliable. If diagnostics are mixed into stdout, the next command may parse error text as data.

## Worked Example

Imagine a command `count-errors` that reads log lines and prints the number of lines containing `ERROR`.

| Input/Condition | Correct Tool Behavior |
| --- | --- |
| Valid log lines | Print the count to stdout. |
| No matching lines | Print `0` to stdout and exit successfully. |
| Missing file argument | Print usage to stderr and exit nonzero. |
| Broken pipe | Stop cleanly instead of dumping a stack trace. |

The output should be easy for another program to read.

## Implementation Shape

Small Unix-style tools usually have:

| Piece | Responsibility |
| --- | --- |
| Argument parser | Decides options, files, and modes. |
| Input loop | Reads stdin or files incrementally. |
| Transformation | Implements the actual operation. |
| Output writer | Writes data to stdout. |
| Error path | Writes diagnostics to stderr and chooses exit status. |

Streaming matters. A tool that reads all input into memory may work for a toy file and fail badly on production logs.

## Failure Modes

| Failure | Why It Hurts Composition |
| --- | --- |
| Diagnostics on stdout | Downstream tools parse error text as data. |
| Always exit 0 | Scripts cannot detect failure. |
| Read all input eagerly | Large inputs exhaust memory. |
| Ignore broken pipe | Tools produce noisy errors in normal pipelines. |
| Locale-dependent output | Scripts behave differently across machines. |

## Exercise Bridge

Unix tooling exercises ask you to implement small filters, pipeline runners, shell redirection, and error counting. Before coding, decide what belongs on stdout, what belongs on stderr, and what exit status proves.

## Self-Check

1. Why does stderr exist separately from stdout?
2. What happens when downstream closes early?
3. How should a filter behave with empty input?
4. What makes an output script-friendly?
5. Which part of your tool should know about file descriptors?

## Further Reading

- The Art of Unix Programming: http://www.catb.org/~esr/writings/taoup/html/
- POSIX shell command language: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/coreutils.html
