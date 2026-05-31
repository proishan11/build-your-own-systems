# PostgreSQL Administration Mental Model

## What You Should Know First

You should know that PostgreSQL is both a database server and an operating system resident process with files, memory, background workers, logs, replication connections, and recovery rules.

## The Problem

Application engineers often treat a database as a black box until something hurts: slow queries, disk growth, replication lag, failed backups, or a bad deploy. PostgreSQL administration makes the database observable, recoverable, and tunable.

The goal is not memorizing settings. The goal is knowing which subsystem is responsible for the symptom.

## Vocabulary

| Term | Meaning |
| --- | --- |
| WAL | Write-ahead log used for crash recovery and replication. |
| Checkpoint | Process of flushing dirty data so recovery has less WAL to replay. |
| Vacuum | Cleanup process for dead tuples created by MVCC. |
| Autovacuum | Background workers that run vacuum and analyze automatically. |
| Replication slot | Mechanism that retains WAL needed by a replica or consumer. |
| PITR | Point-in-time recovery from base backup plus WAL. |
| Query plan | Execution strategy chosen by the optimizer. |
| Statistics | Data the planner uses to estimate row counts and costs. |

## Mental Model

Think of PostgreSQL as four connected systems:

| System | Question It Answers |
| --- | --- |
| Storage and WAL | Can the database recover after a crash? |
| MVCC and vacuum | Which row versions are visible, and when can old ones be removed? |
| Planner and executor | How will this query read and join data? |
| Replication and backup | Can the system survive node loss or operator mistakes? |

Most incidents become clearer when you identify which system is under stress.

## Core Invariant

A production database should have a tested path to recover committed data to an explicit recovery objective.

Backups that have never been restored are hopes, not evidence.

## Worked Example

A dashboard shows replication lag climbing.

| Question | Why It Matters |
| --- | --- |
| Is the primary generating WAL quickly? | Write bursts can overwhelm replicas. |
| Is the replica applying WAL slowly? | CPU, disk, locks, or conflicts may be the issue. |
| Are replication slots retaining WAL? | Disk can fill if consumers fall behind. |
| Are backups or archives healthy? | Recovery options depend on WAL availability. |

The right response depends on the subsystem, not on the generic label "database is slow."

## Implementation Shape

Administration labs should build habits around:

| Practice | Evidence |
| --- | --- |
| Backup and restore | A restore transcript and verified data. |
| PITR | Recovery to a named timestamp or transaction boundary. |
| Query tuning | `EXPLAIN`/`ANALYZE` before and after. |
| Vacuum analysis | Table bloat, dead tuples, and autovacuum behavior. |
| Replication drills | Lag, failover, promotion, and client reconnection. |
| Monitoring | Metrics for WAL, locks, connections, cache, and disk. |

The lesson is operational: every claim should be backed by a command, metric, or recovery artifact.

## Failure Modes

| Failure | Consequence |
| --- | --- |
| Backups without restore tests | Recovery fails during the incident. |
| Ignoring WAL growth | Disk fills and the primary can halt. |
| Missing statistics | Planner chooses bad query plans. |
| Long transactions | Vacuum cannot clean old row versions. |
| Unbounded connections | Memory and scheduling collapse. |
| Manual failover confusion | Split brain or data loss. |

## Exercise Bridge

PostgreSQL labs should teach backup/PITR, query performance, replication/failover, and operational dashboards. Before implementing, write the recovery objective or performance objective in concrete terms.

## Self-Check

1. Can you prove a backup is restorable?
2. What is the difference between crash recovery and PITR?
3. Why can a long transaction cause table bloat?
4. What does `EXPLAIN ANALYZE` add beyond `EXPLAIN`?
5. Which metric would warn you before replication lag becomes data risk?

## Further Reading

- PostgreSQL WAL documentation: https://www.postgresql.org/docs/current/wal.html
- PostgreSQL backup and restore: https://www.postgresql.org/docs/current/backup.html
- PostgreSQL query planning: https://www.postgresql.org/docs/current/using-explain.html
