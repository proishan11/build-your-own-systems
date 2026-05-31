# Exercise 001: Reliable Transport Receiver

Shared concept chapter: [Reliable Transport](../../../../curriculum/concepts/networking/reliable-transport.md)

## Goal

Implement the receiver side of a tiny reliable byte stream.

## Contract

Edit `transport.py` so it:

- accepts segments with byte sequence numbers
- buffers out-of-order data
- delivers bytes to the application only in order
- ignores duplicate segments
- returns the next expected byte as the ACK number

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. Why can't out-of-order bytes be delivered immediately?
2. What makes duplicate delivery dangerous?
3. What does the ACK number mean?

