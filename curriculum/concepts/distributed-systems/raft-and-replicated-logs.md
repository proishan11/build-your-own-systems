# Raft and Replicated Logs

## What You Should Know First

You should understand that machines can crash, messages can be delayed, and a timeout is not proof that another node is dead. Reading [Write-Ahead Logs](../storage/write-ahead-logs.md) first helps because Raft builds a replicated log out of local durable logs.

## The Problem

A distributed service needs multiple machines to agree on the same history of commands. If two nodes commit different commands at the same log index, clients can observe impossible states.

Raft solves this by electing a leader and making the leader replicate an ordered log to a quorum. The algorithm is designed to be understandable: leader election, log replication, and safety rules are separated enough that you can reason about them directly.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Term | A logical epoch. Terms increase when elections happen. |
| Leader | The node currently allowed to accept client writes for a term. |
| Follower | A node that accepts replication from the leader. |
| Candidate | A node asking for votes during an election. |
| Quorum | A majority of nodes. Any two majorities overlap. |
| Commit index | Highest log index known to be safely committed. |
| Log matching | If two logs contain the same term and index, the preceding entries must match. |

## Mental Model

Raft is a replicated notebook with one elected writer:

```text
client -> leader -> followers
              |       |
              +-- quorum commit
```

The leader can propose entries. Followers copy them if the new entries are consistent with their previous log. Once a quorum has an entry under Raft's commit rules, the entry is committed and can be applied to the state machine.

## Core Invariant

If a log entry is committed at index `i`, every future leader must contain that same entry at index `i`.

This invariant is the heart of Raft safety. Liveness matters too, but a slow system is usually better than a system that commits contradictory histories.

## Worked Example

In a five-node cluster, leader `A` appends command `set x=1` at index `7`.

| Step | What Matters |
| --- | --- |
| `A` persists the entry | A leader must not forget entries it accepted. |
| `A` sends AppendEntries | Followers check previous index and term before accepting. |
| Three nodes store the entry | A majority now overlaps with any future majority. |
| `A` advances commit index | The command can be applied and acknowledged. |
| `A` crashes | Any future leader elected by a majority must be compatible with committed history. |

Uncommitted entries are different. They may be overwritten by a later leader if they did not reach the safety boundary.

## Implementation Shape

A teaching implementation often grows in layers:

| Layer | Responsibility |
| --- | --- |
| Persistent state | Current term, voted-for candidate, and log entries survive restart. |
| Election timer | Followers become candidates after silence. |
| RequestVote | Candidates ask for votes and prove their log is up to date. |
| AppendEntries | Leaders replicate entries and send heartbeats. |
| Commit/application loop | Committed entries are applied exactly once in log order. |
| Simulation harness | Tests partitions, restarts, stale leaders, and message delay. |

The local durable log is not an implementation detail. It is part of the consensus protocol.

## Failure Modes

| Failure | Why It Breaks Reasoning |
| --- | --- |
| Voting twice in one term | Can elect two leaders in the same term. |
| Forgetting persisted term | Restarted nodes can violate election safety. |
| Accepting mismatched AppendEntries | Logs can diverge silently. |
| Applying uncommitted entries | Clients can observe state that later disappears. |
| Treating timeout as fact | A node may be slow or partitioned, not dead. |

## Exercise Bridge

The replicated WAL project starts with a local durable log, then adds replication, terms, quorum commit, snapshots, and membership. Before writing code, name which state is volatile, which state is persistent, and which message proves quorum intersection.

## Self-Check

1. What prevents two leaders in the same term?
2. What state must be persisted before voting?
3. Why do quorums protect committed entries?
4. What happens to uncommitted entries from an old leader?
5. Why is log freshness checked during voting?

## Further Reading

- Raft paper, "In Search of an Understandable Consensus Algorithm": https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
- Raft resources and visualizations: https://raft.github.io/
- Diego Ongaro dissertation: https://web.stanford.edu/~ouster/cgi-bin/papers/OngaroPhD.pdf
