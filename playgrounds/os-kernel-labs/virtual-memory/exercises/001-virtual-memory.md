# Exercise 001: Virtual Memory Simulator

Shared concept chapter: [Syscalls, Traps, and Kernel Boundaries](../../../../curriculum/concepts/operating-systems/syscalls-traps-and-kernel-boundaries.md)

## Goal

Implement virtual-to-physical address translation with page permissions.

## Contract

Edit `vm.py` so it:

- maps virtual pages to physical frames
- translates virtual addresses to physical addresses
- rejects unmapped pages
- enforces read/write permissions
- reports page faults explicitly

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. What state lives in a page table entry?
2. Why are permissions checked during translation?
3. What information should a page fault expose?

