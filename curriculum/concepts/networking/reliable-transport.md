# Reliable Transport

## Concept

Reliable transport turns an unreliable packet network into an ordered byte stream or message stream using sequence numbers, acknowledgements, retransmission, flow control, and congestion control.

## Why It Exists

Networks drop, duplicate, delay, and reorder packets. Applications often want simpler semantics: "deliver this data in order, without duplicates, or tell me the connection failed."

## Mental Model

```text
sender: bytes -> segments with sequence numbers -> network
receiver: reorder buffer -> acknowledgements -> ordered bytes
```

The sender keeps unacknowledged data until it knows the receiver has it.

## Core Invariant

The receiver must deliver each byte to the application at most once and in order.

## Tiny Example

The sender transmits segments `0-99`, `100-199`, and `200-299`. The network delivers `200-299` first. The receiver stores it but cannot deliver it yet because bytes `0-199` are missing.

## Common Misconceptions

- ACKs can be lost too.
- Timeout means uncertainty, not proof of packet loss.
- Flow control protects the receiver; congestion control protects the network.
- Reliable transport does not make the remote application correct.

## Self-Check

1. What data must the sender keep for retransmission?
2. What happens when packets arrive out of order?
3. How is flow control different from congestion control?
4. Why are duplicate packets dangerous?

## Further Reading

- Stanford CS144: https://www.scs.stanford.edu/10au-cs144/
- RFC 9293, Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc9293

