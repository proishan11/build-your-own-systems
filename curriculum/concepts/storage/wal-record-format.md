# WAL Record Formats

## Concept

A WAL record format defines how recovery code recognizes, validates, and decodes log entries.

## Why It Exists

After a crash, recovery reads raw bytes. It needs to know where records start and end, what kind of operation each record represents, and whether the bytes are complete and valid.

## Mental Model

Each record is a container:

```text
magic | version | type | lsn | payload_length | payload | checksum
```

The scanner uses the header to know what to read, the payload length to find the end, and the checksum to detect corruption.

## Core Invariant

The scanner returns only complete, valid records in order.

## Tiny Example

Records `1`, `2`, and `3` are complete. Record `4` is half-written because the process crashed. Recovery should return `1`, `2`, `3`, then stop cleanly.

If a byte in record `2` is flipped, recovery should report corruption.

## Common Misconceptions

- EOF at a torn tail can be normal after a crash.
- Checksums detect corruption; they do not repair it.
- LSNs are not decorative counters; later recovery uses them for ordering.
- Format versioning matters once data can outlive the binary that wrote it.

## Self-Check

1. Which bytes does the checksum cover?
2. How does the scanner detect a partial final record?
3. How would a future format version be introduced?
4. What metadata will redo need later?

## Further Reading

- ARIES recovery paper: https://cs.uwaterloo.ca/~david/cs448/aries-mohan.pdf
- PostgreSQL WAL overview: https://www.postgresql.org/docs/current/wal-intro.html
- Bigtable paper: https://research.google/pubs/pub27898

