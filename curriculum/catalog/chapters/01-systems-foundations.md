# Chapter 1: Systems Foundations

This chapter begins close to the machine and close to the developer. The learner builds shells, allocators, kernels, file systems, command-line tools, editor workflows, and Git internals so later systems work has a concrete base instead of folklore.

**Chapter promise:** By the end of this chapter, the learner should be able to explain how a process starts, how bytes move through files and pipes, how memory is organized, and how daily tools encode real systems ideas.

## Chapter Map

| Domain | Projects | What This Domain Trains |
| --- | ---: | --- |
| Systems Programming | 3 | Systems programming makes abstractions tangible. These projects ask the learner to manage processes, memory, descriptors, timers, and scheduling decisions directly. |
| Operating Systems and Kernels | 4 | Operating systems work teaches where user code stops and privileged code begins. The projects emphasize boundaries, invariants, and recovery from malformed input. |
| Unix Command Line | 2 | The command line is a composable systems interface. These projects turn everyday tools into implementation exercises around streams, exits, parsing, and text transformations. |
| Vim | 2 | Vim is included as a fluency track because editing speed, navigation, and refactoring mechanics change how comfortably a learner can inspect large systems. |
| Git | 2 | Git is a distributed content-addressed database disguised as a daily tool. These projects make commits, trees, merges, and rebases explicit. |

## Systems Programming

Systems programming makes abstractions tangible. These projects ask the learner to manage processes, memory, descriptors, timers, and scheduling decisions directly.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Mini Shell With Job Control | Build a shell that supports parsing, pipelines, redirection, environment variables, signals, foreground/background jobs, and exit statuses. | processes and file descriptors<br>pipes and redirection<br>signals<br>terminals and process groups<br>error propagation | handle `Ctrl-C` correctly<br>do not leak child processes<br>keep stdout/stderr semantics clean<br>test pipeline failures |
| Memory Allocator Lab | Build a malloc/free allocator with free lists, splitting, coalescing, alignment, and heap debugging. | memory layout<br>fragmentation<br>alignment<br>metadata corruption<br>debugging low-level systems | detect double free<br>expose allocator stats<br>benchmark fragmentation patterns<br>build a heap consistency checker |
| Event Loop and Async Runtime | Build a small event loop over `epoll`/`kqueue` or a portable abstraction. | nonblocking I/O<br>readiness versus completion<br>timers<br>task scheduling<br>backpressure | avoid busy loops<br>support cancellation<br>instrument event-loop lag<br>test slow clients |

## Operating Systems and Kernels

Operating systems work teaches where user code stops and privileged code begins. The projects emphasize boundaries, invariants, and recovery from malformed input.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| xv6-Style Kernel Lab | Build or extend a small teaching kernel with system calls, traps, virtual memory, scheduling, and a file system. | privilege boundaries<br>traps and syscalls<br>page tables<br>process lifecycle<br>kernel locking<br>file system layout | validate user pointers<br>avoid kernel panics from user input<br>reason about lock ordering<br>test fork/exec/wait edge cases |
| User-Level Thread Library | Build cooperative then preemptive user-level threads with context switching, stacks, mutexes, condition variables, and a scheduler. | stacks and registers<br>context switching<br>scheduling<br>synchronization<br>preemption hazards | detect deadlocks<br>test scheduler fairness<br>document signal-safety boundaries<br>expose thread state for debugging |
| Virtual Memory Simulator | Build a simulator for page tables, TLBs, page faults, replacement policies, copy-on-write, and memory-mapped files. | address translation<br>paging<br>TLB behavior<br>replacement algorithms<br>copy-on-write | explain every page fault<br>benchmark replacement policies<br>simulate memory pressure<br>test permission violations |
| Tiny Journaling File System | Build a block-based file system with inodes, directories, free-space management, buffer cache, and a journal. | block devices<br>inode layout<br>directories<br>crash consistency<br>journaling | crash-test metadata updates<br>run fsck-style validation<br>handle partial writes<br>document on-disk compatibility |

## Unix Command Line

The command line is a composable systems interface. These projects turn everyday tools into implementation exercises around streams, exits, parsing, and text transformations.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Coreutils From Scratch | Implement `cat`, `head`, `tail`, `wc`, `sort`, `uniq`, `grep`, `xargs`, and `find` subsets. | streams<br>file traversal<br>text processing<br>exit status<br>POSIX-ish behavior | handle binary input<br>preserve stdout/stderr contracts<br>test large files<br>compare behavior with real tools |
| Shell Text Processing Workbench | Create exercises where the learner solves log analysis, CSV cleanup, filesystem audits, and process inspection using pipelines. | composability<br>quoting<br>redirection<br>pipes<br>debugging shell scripts | write reproducible scripts<br>handle filenames with spaces<br>use `set -euo pipefail` responsibly |

## Vim

Vim is included as a fluency track because editing speed, navigation, and refactoring mechanics change how comfortably a learner can inspect large systems.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Vim Kata Track | Build a series of editing challenges covering motions, text objects, macros, registers, marks, windows, quickfix, substitutions, and help navigation. | modal editing<br>composable commands<br>repeatability<br>editor-as-language | optimize edit sequences<br>explain command composition<br>use quickfix for project-scale edits |
| Vim Plugin From Scratch | Build a small plugin: project notes, test runner, quickfix helper, or text-object extension. | Vimscript or Lua basics<br>buffers/windows<br>mappings<br>commands<br>help docs | write `:help` documentation<br>avoid clobbering user mappings<br>test with minimal config |

## Git

Git is a distributed content-addressed database disguised as a daily tool. These projects make commits, trees, merges, and rebases explicit.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Mini Git | Implement `init`, `hash-object`, `cat-file`, `write-tree`, `commit-tree`, branches, checkout, diff, merge basics, and status. | content-addressed storage<br>commit graphs<br>trees/blobs<br>index<br>branching | explain every object written<br>handle file mode and path edge cases<br>visualize the graph |
| Git Merge and Rebase Lab | Build exercises around conflict resolution, merge bases, rebasing, reflog recovery, bisect, and blame. | DAG reasoning<br>history rewriting<br>conflict mechanics<br>recovery | recover from bad rebase<br>explain why a conflict happened<br>write safe team workflows |

## How To Use This Chapter

| Move | What The Learner Should Do | Evidence To Produce |
| --- | --- | --- |
| Learn the concept | Read the relevant concept chapter before opening the code. | A short note naming the invariant and the failure mode. |
| Implement the milestone | Fill the placeholder implementation for the current exercise only. | A passing validator for that milestone. |
| Review like a Staff engineer | Inspect edge cases, recovery behavior, observability, and test strength. | A design note explaining what the tests prove and what they do not prove. |
