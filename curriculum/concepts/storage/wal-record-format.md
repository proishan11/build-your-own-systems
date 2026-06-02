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

## How It Works Step By Step

A record format makes recovery boring by removing guesswork.

| Step | What The Writer Does | What The Reader Later Does |
| --- | --- | --- |
| Choose version | Writes a known format version or magic. | Rejects unsupported formats explicitly. |
| Encode type | Names the operation kind. | Dispatches to the right decoder. |
| Encode length | Records exact payload size. | Reads exactly that many bytes. |
| Encode payload | Stores operation-specific fields. | Parses fields without scanning beyond the record. |
| Encode checksum | Covers the bytes that must not change. | Detects torn writes or corruption. |
| Append sequentially | Places the record after previous records. | Scans forward until EOF, torn tail, or corruption. |

A good format lets the reader answer: complete, incomplete, corrupt, or valid. It should not need vibes.

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

## State Or Flow Walkthrough

A small `PUT` record might be laid out like this:

```text
magic(4) version(1) type(1) length(4) checksum(4) payload(length)
```

The scanner reads fixed header bytes first. If there are not enough header bytes, it has reached an incomplete tail. If the header is present, it reads `length` payload bytes. If those bytes are missing, the record is torn. If the checksum does not match, the record is corrupt.

Those cases should not collapse into one generic parse failure; recovery policy depends on the difference.

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

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| `database/001-wal-record-format` | Encoding, decoding, checksums, type tags, and malformed-record rejection. |
| Storage engine project ladders | Versioned record evolution and scanner behavior. |
| Recovery exercises | Torn-tail handling, corruption detection, and replay boundaries. |

## Exercise Bridge

WAL format exercises usually ask you to encode, decode, scan, and reject malformed records. Treat tests that corrupt bytes as design feedback: they are asking whether your format makes recovery unambiguous.

## Readiness Checklist

You are ready to implement WAL record formats when you can:

- draw the exact bytes in one record
- explain how the reader finds the next record
- identify which bytes the checksum covers
- distinguish EOF, torn tail, and corruption
- describe how the format can evolve safely

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
