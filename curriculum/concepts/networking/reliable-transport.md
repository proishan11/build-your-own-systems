# Reliable Transport

## What You Should Know First

You should know that packets can be lost, duplicated, delayed, and delivered out of order. You should also know that an application usually wants a simpler abstraction: bytes arrive once, in order, or the connection fails clearly.

## The Problem

IP-style packet delivery is best effort. It does not promise that a packet will arrive, arrive once, or arrive before later packets. Reliable transport protocols build a stronger contract on top of that weak network.

The goal is not just "try again." A reliable transport must decide what was sent, what was acknowledged, what should be retransmitted, how much data can be in flight, and when the receiver is ready for more.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Sequence number | A number that identifies the position of bytes or packets in a stream. |
| ACK | Acknowledgement from receiver to sender. |
| Retransmission | Sending data again because delivery is uncertain. |
| Sliding window | The range of data allowed to be in flight. |
| Flow control | Receiver tells sender how much buffer space is available. |
| Congestion control | Sender estimates how much the network can handle. |
| Duplicate packet | A packet the receiver has already processed or buffered. |

## Mental Model

Reliable transport is a conversation between two ledgers:

```text
sender ledger: sent, acknowledged, waiting
receiver ledger: received, buffered, delivered
```

The sender advances when it receives acknowledgements. The receiver delivers data to the application only when the next expected sequence is available.

## Core Invariant

The receiver must deliver each byte to the application at most once and in stream order.

This invariant is why buffering and duplicate detection matter. A protocol can retransmit aggressively, but it must not deliver repeated data as if it were new.

## Worked Example

Suppose the sender transmits packets `1`, `2`, and `3`, but the network delivers `1`, `3`, and later `2`.

| Receiver Event | Correct Behavior |
| --- | --- |
| Packet `1` arrives | Deliver `1`; next expected is `2`. |
| Packet `3` arrives | Buffer `3`; do not deliver yet. |
| ACK sent | Receiver can acknowledge what it has or what it expects next, depending on protocol design. |
| Packet `2` arrives | Deliver `2`, then deliver buffered `3`. |
| Duplicate `2` arrives | Drop it or acknowledge again; do not deliver twice. |

## Implementation Shape

A teaching reliable transport usually has:

| Component | Responsibility |
| --- | --- |
| Packet format | Carries sequence numbers, ACKs, flags, and payload. |
| Send buffer | Tracks sent but unacknowledged data. |
| Receive buffer | Holds out-of-order data until gaps are filled. |
| Timer system | Retransmits when acknowledgement does not arrive. |
| Window logic | Limits in-flight data based on receiver and network signals. |
| Test harness | Injects loss, reordering, duplication, and delay. |

Keep protocol state explicit. If the only state is "last packet sent," reordering and retransmission will quickly become untestable.

## Failure Modes

| Failure | Effect |
| --- | --- |
| No duplicate detection | Application receives the same bytes twice. |
| No buffering | Out-of-order delivery loses valid data. |
| Retransmit too quickly | Network congestion gets worse. |
| Retransmit too slowly | Throughput collapses after loss. |
| Confusing flow and congestion control | Receiver capacity and network capacity become tangled. |
| No sequence wrap plan | Long-running streams eventually collide with old sequence space. |

## Exercise Bridge

Reliable transport exercises typically start with ordered delivery, then add ACKs, retransmission, windows, and loss simulation. Before coding, decide whether your sequence numbers count packets or bytes and what acknowledgement means.

## Self-Check

1. What does an ACK acknowledge in this protocol?
2. Can the receiver deliver packet `3` before packet `2`?
3. Where are out-of-order packets stored?
4. When does the sender retransmit?
5. What prevents duplicate delivery?

## Further Reading

- RFC 9293, Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc9293
- Computer Networks: A Systems Approach, transport chapter: https://book.systemsapproach.org/e2e/tcp.html
- QUIC transport RFC 9000: https://www.rfc-editor.org/rfc/rfc9000
