# PostgreSQL Administration Mental Model

## Concept

PostgreSQL administration is the practice of keeping a database correct, available, performant, recoverable, and observable while real workloads change over time.

## Why It Exists

A database is not just a query engine. It is a durable service with storage, memory, background processes, replication, backups, authentication, query planning, and operational risk.

## Mental Model

Think in loops:

```text
workload -> storage/WAL/buffers/planner -> metrics/logs -> tuning/change -> observe again
```

Administration is evidence-driven. The first question is not "which knob should I tune?" It is "what evidence says where the bottleneck or risk is?"

## Core Invariant

Backups and recovery procedures must be tested before they are needed.

## Tiny Example

A query slows down. Possible causes include a bad plan, missing statistics, table bloat, lock contention, I/O saturation, or changed data distribution. The admin gathers evidence before tuning.

## Common Misconceptions

- A backup that has never been restored is a hope, not a backup.
- Indexes speed reads but slow some writes and consume maintenance.
- Vacuum is not optional housekeeping; it is part of MVCC health.
- Replication lag is an application-visible risk.

## Self-Check

1. Can you restore to a point in time?
2. What are the top wait events?
3. Which queries dominate load?
4. Are autovacuum and checkpoints healthy?
5. What is the replication lag and why?

## Further Reading

- PostgreSQL server administration: https://www.postgresql.org/docs/current/admin.html
- Backup and restore: https://www.postgresql.org/docs/current/backup.html
- WAL introduction: https://www.postgresql.org/docs/current/wal-intro.html

