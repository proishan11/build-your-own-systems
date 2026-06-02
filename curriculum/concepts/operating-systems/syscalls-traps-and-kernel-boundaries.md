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

## How It Works Step By Step

A syscall is a controlled transition from less privilege to more privilege.

| Step | What Happens | Risk If Wrong |
| --- | --- | --- |
| User prepares arguments | Registers or stack contain syscall number and values. | Bad pointers and invalid handles are still just numbers. |
| Trap instruction executes | CPU switches into kernel-controlled entry code. | Broken save/restore corrupts user execution. |
| Kernel dispatches | Syscall number selects a handler. | Unknown numbers must fail safely. |
| Handler validates | File descriptors, lengths, flags, and user memory are checked. | Trusting user input can crash or corrupt the kernel. |
| Kernel performs work | Files, process tables, VM, or devices are accessed. | Locking and partial failure semantics matter. |
| Result returns | Success value or error code is placed for user code. | Ambiguous errors make applications unreliable. |

A syscall handler should be paranoid and boring. It should reject nonsense early, copy data carefully, and leave the kernel consistent even when the caller is hostile.

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

## State Or Flow Walkthrough

For `write(fd, user_buffer, n)`, the kernel does not receive a safe byte slice. It receives an address and a length from untrusted code.

```text
user memory:        [ bytes to write ]
user registers:     fd, pointer, length
trap entry:         save state, switch privilege
kernel validation:  fd exists, pointer range readable
copy/write path:    move bytes to file/socket/device
return path:        byte count or error
```

The pointer might be null, point to unmapped memory, cross a page boundary, or name memory the process cannot read. The kernel must handle all of those cases without panicking.

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

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| `os/001-syscall-boundary` | Syscall dispatch, argument validation, user-pointer safety, and error return rules. |
| `os/002-virtual-memory` | Address translation, permission checks, and page-level reasoning. |
| Kernel project ladders | Trap handling, process lifecycle, file-system calls, and kernel lock-ordering concerns. |

## Exercise Bridge

OS exercises use this concept for syscall dispatch, virtual memory validation, traps, fork/exec/wait behavior, and file-system calls. Before implementing a syscall, list which arguments are untrusted and which resources need ownership checks.

## Readiness Checklist

You are ready to implement syscall exercises when you can:

- explain why a user pointer is not a kernel pointer
- list which arguments need validation before use
- describe what state trap entry must preserve
- return errors without corrupting kernel state
- separate authorization failure from malformed input

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
