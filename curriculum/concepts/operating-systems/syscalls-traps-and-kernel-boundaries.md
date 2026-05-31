# Syscalls, Traps, and Kernel Boundaries

## Concept

A system call is the controlled doorway from user code into the operating system kernel. A trap is the CPU mechanism that transfers control from less-privileged code to privileged kernel code.

## Why It Exists

User programs need services like files, memory, networking, and process creation, but they must not directly control hardware or corrupt other programs. The kernel boundary lets the OS provide power with isolation.

## Mental Model

```text
user program -> syscall instruction -> trap handler -> kernel service -> return
```

The program asks. The kernel checks permissions, performs the operation, and returns a result or error.

## Core Invariant

Untrusted user code must only affect kernel-managed state through validated kernel entry points.

## Tiny Example

When a process calls `read(fd, buf, n)`, the kernel must validate the file descriptor, validate the user memory range, copy bytes safely, update file offsets consistently, and return the number of bytes read.

## Common Misconceptions

- A syscall is not a normal function call; it crosses a privilege boundary.
- Kernel code cannot trust user pointers.
- Copying data across the boundary is part of the design, not accidental overhead.
- A crash in the kernel is much more serious than a crash in one user process.

## Self-Check

1. What changes when execution crosses into the kernel?
2. Why must user pointers be validated?
3. What state does a file descriptor represent?
4. What should happen if a syscall is interrupted?

## Further Reading

- xv6 book and source: https://pdos.csail.mit.edu/6.828/2019/xv6.html
- Berkeley CS162: https://cs162.org/

