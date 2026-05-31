# Exercise 001: Mini Shell Parse and Execute

Shared concept chapter: [Unix Pipelines](../../../../curriculum/concepts/developer-tools/unix-pipelines.md)

## Goal

Implement a tiny shell function that parses one command line and executes it without pipelines or redirection.

## Contract

Edit `minishell.py` so it:

- splits a command line using shell-like quoting rules
- returns an argv list
- executes the command with captured stdout/stderr
- returns the process exit code
- rejects empty commands

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. Why is string-splitting on spaces incorrect?
2. What is the difference between argv and a shell command string?
3. What should go to stdout versus stderr?

