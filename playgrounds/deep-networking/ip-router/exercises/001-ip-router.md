# Exercise 001: IP Router Longest-Prefix Match

Shared concept chapter: [Reliable Transport](../../../../curriculum/concepts/networking/reliable-transport.md)

## Goal

Implement the forwarding decision for a tiny IPv4 router.

## Contract

Edit `router.py` so it:

- stores routes as CIDR prefixes
- chooses the longest matching prefix
- decrements TTL when forwarding
- rejects packets whose TTL would reach zero
- returns the selected next hop and output interface

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. Why is longest-prefix match needed?
2. What does TTL protect against?
3. What counters would a real router expose?

