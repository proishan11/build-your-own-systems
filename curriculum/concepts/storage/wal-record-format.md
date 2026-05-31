# WAL Record Formats

## What You Should Know First

Read [Write-Ahead Logs](write-ahead-logs.md) first. This chapter focuses on the bytes inside each log record: how to frame them, validate them, and evolve them over time.

## The Problem

A WAL is only useful if recovery can parse it after a crash. Plain concatenated payloads are not enough. Recovery needs to know where each record starts and ends, whether the record is complete, what kind of operation it describes, and whether the bytes are corrupt.

The record format is the contract between the writer today and the recovery code tomorrow.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Header | Fixed-size metadata at the start of a record. |
| Payload | The operation-specific bytes carried by the record. |
| Length prefix | A field that tells the reader how many payload bytes follow. |
| Type tag | A field that identifies the kind of record. |
| Checksum | A digest used to detect torn or corrupted records. |
| Version | A field that lets the format evolve without guessing. |

## Mental Model

Think of each record as a small envelope:

```text
+---------+------+----------+----------+---------+
| version | type | length   | checksum | payload |
+---------+------+----------+----------+---------+
```

Recovery reads one envelope at a time. If the header is incomplete, the tail is ignored. If the payload is incomplete or checksum fails, recovery stops or reports corruption according to the storage contract.

## Core Invariant

A reader must never silently accept bytes as a different valid operation than the writer intended.

This is stronger than "the parser does not crash." A parser that turns corrupted bytes into a plausible delete operation is dangerous.

## Worked Example

Suppose the system encodes `PUT key=cat value=gray`.

| Field | Example |
| --- | --- |
| Version | `1` |
| Type | `PUT` |
| Length | number of bytes in the payload |
| Checksum | digest over header fields and payload |
| Payload | encoded key and value |

During recovery, the scanner reads the header, reads exactly `length` payload bytes, recomputes the checksum, then yields a typed record to the replay layer.

## Implementation Shape

A clean implementation separates parsing from replay:

| Layer | Responsibility |
| --- | --- |
| Byte encoder | Converts typed records into bytes. |
| Byte decoder | Converts bytes into typed records or explicit errors. |
| Scanner | Iterates through a file and handles EOF, torn tail, and corruption. |
| Replayer | Applies valid records to state. |

This separation keeps storage bugs easier to inspect. The decoder should not mutate database state, and the replayer should not guess byte framing.

## Failure Modes

| Failure | Symptom | Better Design |
| --- | --- | --- |
| No length prefix | Recovery cannot skip or stop precisely. | Add explicit length. |
| No checksum | Torn writes can become fake valid records. | Check each record. |
| Host-endian integers | Files differ across machines. | Pick a byte order. |
| No version | Format migration becomes guesswork. | Include version or magic bytes. |
| Parser accepts trailing junk | Corruption hides until later. | Validate exact lengths. |

## Exercise Bridge

WAL format exercises usually ask you to encode, decode, scan, and reject malformed records. Treat tests that corrupt bytes as design feedback: they are asking whether your format makes recovery unambiguous.

## Self-Check

1. How does the reader know where a record ends?
2. Which bytes are covered by the checksum?
3. What should happen on a partial final record?
4. Can the format evolve without breaking older data?
5. Are parser errors distinct from valid delete or empty records?

## Further Reading

- PostgreSQL WAL internals overview: https://www.postgresql.org/docs/current/wal-internals.html
- SQLite file format: https://www.sqlite.org/fileformat.html
- ARIES recovery paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf
