# Exercise 001: Syscall Boundary Lab

Shared concept chapter: [Syscalls, Traps, and Kernel Boundaries](../../../../curriculum/concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md)

## Goal

Implement a tiny simulated kernel syscall boundary that validates user pointers before copying bytes.

## Contract

Edit `kernel.py` so it:

- models user memory as a fixed-size byte array
- validates pointer ranges before reading or writing
- rejects invalid file descriptors
- copies data from a kernel-owned file table into user memory
- returns the number of bytes read

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. Why can't the kernel trust a user pointer?
2. What should happen on partial reads?
3. What kernel state changes when a read succeeds?

