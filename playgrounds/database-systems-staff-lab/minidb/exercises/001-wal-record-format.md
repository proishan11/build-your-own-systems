# Exercise 001: WAL Record Format and Scanner

Shared concept chapter: [WAL Record Formats](../../../../curriculum/concepts/storage/wal-record-format.md)

## Concept Primer

A database WAL record is a compact, replayable description of something the database may need during recovery. A record format gives recovery code enough structure to decide where each record starts, where it ends, what kind of record it is, and whether the bytes look valid.

The scanner is the recovery reader. It walks forward through the log and returns complete records. If the process crashed while writing the final record, the scanner should stop cleanly at that torn tail.

## Why This Matters

Recovery code runs when the system is least trustworthy: after a crash, maybe with partially written bytes. The record format is the contract between normal operation and recovery. A sloppy format makes later recovery logic fragile.

## Mental Model

Each record is a shipping container:

```text
header: magic, version, type, LSN, payload length
body:   payload bytes
footer: checksum
```

The magic and version say "this is our format." The length says how many bytes to read. The checksum says whether the bytes still match what was written.

## Core Invariant

The scanner must return only complete, valid records in order. It must not return corrupted records or treat a torn final record as a real operation.

## Tiny Example

If the log contains records with LSNs `1`, `2`, and `3`, the scanner should return them in that order. If the file ends halfway through record `4`, the scanner should return `1`, `2`, `3`, then stop without error.

If a byte inside record `2` is flipped, the scanner should report corruption rather than quietly returning bad data.

## Common Misconceptions

- EOF in the middle of the final record can be normal after a crash.
- EOF or corruption in the middle of an earlier complete-looking record is not normal.
- Checksums do not fix data; they only help detect that data is wrong.
- LSNs are not just counters. Later recovery logic uses them to reason about ordering.

## Self-Check

Before coding, answer:

1. Which bytes are covered by the checksum?
2. How does the scanner know the payload length?
3. Why should partial final records be ignored?
4. What metadata will redo recovery need later?

## Goal

Implement the binary write-ahead log record format that MiniDB will use for redo recovery.

## Concepts

- Log sequence numbers.
- Record headers.
- Checksums.
- Binary encoding.
- Forward-compatible formats.
- Recovery scanning.

## Files To Edit

- `internal/wal/record.go`

## Contract

Your implementation must:

- Encode records with magic, version, type, LSN, payload length, payload, and checksum.
- Decode records in order.
- Stop cleanly at an incomplete final record.
- Report checksum corruption.
- Preserve payload bytes exactly.
- Make the format easy to extend later.

## Design Hints

Keep the format simple and explicit. A reasonable first record layout:

```text
magic[4] version[1] type[1] lsn[8] payload_len[4] payload[n] checksum[4]
```

Use little-endian encoding. Compute the checksum over the header fields and payload, excluding the checksum field itself.

## Validation

Run from `playgrounds/database-systems-staff-lab/minidb`:

```bash
go test ./...
```

## Further Reading

- ARIES recovery paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf
- Bigtable paper: https://research.google/pubs/pub27898
- LSM-tree paper: https://dsf.berkeley.edu/cs286/papers/lsm-acta1996.pdf

## Staff-Level Review Questions

1. What makes this format recoverable after a crash?
2. What happens when a future version adds fields?
3. Which corruptions are detected and which are not?
4. How would this format support group commit later?
