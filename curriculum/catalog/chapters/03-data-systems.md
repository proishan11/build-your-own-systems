# Chapter 3: Data Systems

This chapter treats data as something that must survive crashes, contention, growth, and operator mistakes. The projects cover storage-engine internals and the operational work of keeping PostgreSQL reliable.

**Chapter promise:** The learner should understand why durability is a protocol, not a checkbox: records need formats, pages need invariants, recovery needs replay rules, and production databases need backup, restore, replication, and performance evidence.

## Chapter Map

| Domain | Projects | What This Domain Trains |
| --- | ---: | --- |
| Database Systems | 3 | Database internals turn abstract correctness into bytes on disk. Each project makes durability, indexing, planning, or recovery visible. |
| PostgreSQL Administration | 3 | PostgreSQL administration is operational database engineering: backups, restores, failover, query plans, and evidence-based tuning. |

## Database Systems

Database internals turn abstract correctness into bytes on disk. Each project makes durability, indexing, planning, or recovery visible.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| MiniDB Storage Engine | Build WAL, slotted pages, buffer pool, B+ tree, recovery, query execution, and MVCC. | durability<br>storage layout<br>indexing<br>buffer management<br>transactions<br>query plans | crash-test recovery<br>benchmark point/range queries<br>implement `EXPLAIN`<br>inspect pages and WAL records |
| LSM Tree KV Store | Build memtables, SSTables, Bloom filters, compaction, tombstones, snapshots, and iterators. | write amplification<br>read amplification<br>compaction debt<br>immutable files<br>snapshot consistency | tune compaction<br>expose write stalls<br>test iterator correctness across levels<br>compare against B+ tree tradeoffs |
| Query Optimizer Lab | Build a simple SQL planner with table scans, index scans, joins, aggregates, cardinality estimates, and cost-based choices. | logical and physical plans<br>statistics<br>join algorithms<br>cost models<br>plan regressions | show `EXPLAIN`<br>create bad-statistics scenarios<br>test plan stability<br>benchmark join choices |

## PostgreSQL Administration

PostgreSQL administration is operational database engineering: backups, restores, failover, query plans, and evidence-based tuning.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Backup and PITR Lab | Build a PostgreSQL environment with base backups, WAL archiving, point-in-time recovery, and restore verification. | backups<br>WAL archiving<br>RPO/RTO<br>restore drills<br>disaster recovery | prove restore works<br>simulate data loss<br>document a runbook<br>alert on broken archiving |
| Query Performance Lab | Create datasets and bad queries, then diagnose with `EXPLAIN`, indexes, statistics, vacuum, and configuration. | query planning<br>indexes<br>statistics<br>bloat<br>wait events | measure before tuning<br>avoid cargo-cult indexes<br>explain plan changes<br>protect write performance |
| Replication and Failover Lab | Build primary/replica streaming replication, monitor lag, perform failover, and validate client behavior. | streaming replication<br>timelines<br>lag<br>failover<br>consistency tradeoffs | simulate primary loss<br>prevent split brain<br>document promotion workflow<br>test application retry behavior |

## How To Use This Chapter

| Move | What The Learner Should Do | Evidence To Produce |
| --- | --- | --- |
| Learn the concept | Read the relevant concept chapter before opening the code. | A short note naming the invariant and the failure mode. |
| Implement the milestone | Fill the placeholder implementation for the current exercise only. | A passing validator for that milestone. |
| Review like a Staff engineer | Inspect edge cases, recovery behavior, observability, and test strength. | A design note explaining what the tests prove and what they do not prove. |
