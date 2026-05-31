# Raft and Replicated Logs

## Concept

Raft is a consensus algorithm that lets a cluster agree on a single ordered log, even when some nodes crash, restart, or temporarily cannot communicate.

## Why It Exists

Distributed systems need agreement. If two machines accept different writes as "committed," clients can observe impossible histories. Raft turns the problem into leader election plus log replication with explicit terms and quorum rules.

## Mental Model

At any moment, one leader is responsible for appending entries. Followers replicate the leader's log. An entry becomes committed when it is safely stored on a quorum under Raft's rules.

```text
client -> leader -> followers
              |       |
              +-- quorum commit
```

## Core Invariant

If a log entry is committed at index `i`, every future leader must contain that same entry at index `i`.

## Tiny Example

In a five-node cluster, the leader appends entry `x`. Once three nodes have `x` at the same log index, the leader can usually advance commit state. If the leader crashes, any future leader elected by a majority must overlap with that majority.

## Common Misconceptions

- A timeout is suspicion, not proof of failure.
- Majority replication is about intersection, not popularity.
- Log matching prevents leaders from stitching together incompatible histories.
- Reads need semantics too; "I am leader" is not always enough for a linearizable read.

## Self-Check

1. What prevents two leaders in the same term?
2. What state must be persisted before voting?
3. Why do quorums protect committed entries?
4. What happens to uncommitted entries from an old leader?

## Further Reading

- Raft paper, "In Search of an Understandable Consensus Algorithm": https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
- Raft resources and visualizations: https://raft.github.io/
- Diego Ongaro dissertation: https://web.stanford.edu/~ouster/cgi-bin/papers/OngaroPhD.pdf

