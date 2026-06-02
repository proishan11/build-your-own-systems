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

## How It Works Step By Step

A shell pipeline is simple at the surface, but it contains several operating-system ideas.

| Step | What Happens | Why It Matters |
| --- | --- | --- |
| Parse command line | The shell splits commands, arguments, pipes, and redirections. | Tools do not see the full pipeline; they see argv and file descriptors. |
| Create pipes | The shell asks the kernel for connected read/write file descriptors. | Pipes are kernel buffers, not temporary files. |
| Fork processes | Each command runs as a separate process. | Tools execute concurrently and may block independently. |
| Wire descriptors | The shell connects stdout of one process to stdin of the next. | Composition works because tools agree on streams. |
| Close unused ends | Parent and child close descriptors they do not need. | Leaked descriptors can keep readers waiting forever. |
| Wait and collect status | The shell observes process exits. | Scripts need a reliable success/failure signal. |

The key design lesson is that a pipeline is not one program with many function calls. It is several processes connected by a small contract: bytes, descriptors, and exit status.

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

## State Or Flow Walkthrough

Consider this pipeline:

```bash
awk '$4 >= 500 { print $3 }' data/access.log | sort | uniq -c | sort -nr
```

| Stage | Input | Output | Responsibility |
| --- | --- | --- | --- |
| `awk` | log lines | endpoint paths | Select rows whose status code is an error. |
| `sort` | endpoint paths | grouped endpoint paths | Put identical keys next to each other. |
| `uniq -c` | grouped paths | count plus path | Count adjacent duplicates. |
| `sort -nr` | count/path rows | descending counts | Make the most frequent error path first. |

If `awk` prints diagnostics to stdout, `sort` and `uniq` will treat those diagnostics as data. If any command exits nonzero and the script ignores it, the final output can look valid while hiding a broken middle stage.

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

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| `tooling/001-unix-pipelines` | Stream filtering, stdout/stderr separation, sorting, grouping, and script-friendly output. |
| `tooling/003-minishell-exec` | Process creation, pipe wiring, redirection, and exit-status propagation. |
| Shell text processing project ladders | Composable filters, malformed input handling, and deterministic command output. |

When solving these exercises, first identify the stream contract: what bytes enter, what bytes leave on stdout, what diagnostics go to stderr, and what exit status means.

## Exercise Bridge

Unix tooling exercises ask you to implement small filters, pipeline runners, shell redirection, and error counting. Before coding, decide what belongs on stdout, what belongs on stderr, and what exit status proves.

## Readiness Checklist

You are ready to implement a Unix pipeline exercise when you can:

- describe which process owns each stage of the pipeline
- explain why diagnostics belong on stderr
- predict what happens when downstream closes early
- name the command whose exit status should fail the script
- rewrite a pipeline as a sequence of stream transformations

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
