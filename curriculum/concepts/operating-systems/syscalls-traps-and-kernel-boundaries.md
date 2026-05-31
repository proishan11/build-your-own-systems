# Syscalls, Traps, and Kernel Boundaries

## What You Should Know First

You should know that ordinary programs run in user mode and the operating system kernel runs with more privilege. User programs cannot directly access every device, page table, or hardware instruction.

## The Problem

Programs need privileged services: read a file, write to a socket, allocate memory, create a process, or get the time. Letting every program touch hardware directly would make isolation impossible.

A system call is the controlled doorway from user code into the kernel. A trap is the hardware-supported transition that lets the CPU switch from unprivileged execution to privileged kernel handling.

## Vocabulary

| Term | Meaning |
| --- | --- |
| User mode | CPU mode for ordinary application code. |
| Kernel mode | CPU mode with access to privileged instructions and kernel memory. |
| Syscall | A requested kernel service such as `read`, `write`, or `fork`. |
| Trap | A controlled transfer into kernel code caused by syscall, exception, or interrupt. |
| Process | An execution context with its own address space and resources. |
| User pointer | An address supplied by user code that the kernel must validate before using. |

## Mental Model

Think of the kernel as a guarded service desk:

```text
user program -> syscall number + arguments -> kernel handler -> result
```

The kernel should never trust the caller. The caller may pass invalid pointers, huge lengths, stale file descriptors, or arguments designed to trigger edge cases.

## Core Invariant

Untrusted user input must not let user code corrupt kernel memory, access another process's private state, or crash the kernel.

This is a security invariant and a reliability invariant. A bad user program should fail as a user program, not take down the machine.

## Worked Example

Consider `read(fd, user_buffer, n)`.

| Step | Kernel Responsibility |
| --- | --- |
| Enter kernel | Save enough user state to return later. |
| Decode arguments | Identify syscall number and arguments. |
| Validate fd | Check that the descriptor exists and is readable. |
| Validate user buffer | Ensure the range points to writable user memory. |
| Copy data | Move bytes from kernel/file state into user memory safely. |
| Return result | Restore user execution with byte count or error code. |

If the user buffer points into kernel memory, the syscall must reject it. If it crosses an unmapped page, the kernel must handle that safely.

## Implementation Shape

A teaching kernel usually separates:

| Layer | Responsibility |
| --- | --- |
| Trap entry | Save registers and switch to kernel handling. |
| Syscall dispatcher | Map syscall number to handler. |
| Argument fetcher | Read integers and pointers from user context. |
| Validation helpers | Check user memory and resource handles. |
| Copy helpers | Move data across the user/kernel boundary. |
| Return path | Put result in the expected register and resume user code. |

Clear helper boundaries matter because validation bugs are often repeated across syscall handlers.

## Failure Modes

| Failure | Consequence |
| --- | --- |
| Trusting user pointers | Kernel memory corruption or panic. |
| Partial copy bugs | Incorrect success after only part of a buffer was valid. |
| Leaking kernel memory | Uninitialized bytes become visible to user code. |
| Wrong error semantics | Applications cannot recover correctly. |
| Holding locks across user copy | Page faults or slow paths can deadlock kernel code. |

## Exercise Bridge

OS exercises use this concept for syscall dispatch, virtual memory validation, traps, fork/exec/wait behavior, and file-system calls. Before implementing a syscall, list which arguments are untrusted and which resources need ownership checks.

## Self-Check

1. Why can a user program not call disk hardware directly?
2. What makes a user pointer dangerous?
3. What state must be saved on trap entry?
4. How should the kernel report invalid arguments?
5. Why is copying data across the boundary more subtle than assigning a pointer?

## Further Reading

- xv6 book: https://pdos.csail.mit.edu/6.828/2023/xv6/book-riscv-rev3.pdf
- Linux syscall table and calling conventions: https://man7.org/linux/man-pages/man2/syscall.2.html
- Operating Systems: Three Easy Pieces: https://pages.cs.wisc.edu/~remzi/OSTEP/
