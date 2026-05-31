# Git Object Model

## Concept

Git stores content as immutable objects addressed by hashes. Commits point to trees, trees point to blobs and other trees, and branches point to commits.

## Why It Exists

The object model lets Git represent history as a graph of snapshots while sharing unchanged content efficiently.

## Mental Model

```text
branch -> commit -> tree -> blob
             |
             +-> parent commit
```

A branch is not the history itself. It is a movable pointer into the commit graph.

## Core Invariant

Object identity is derived from content. If content changes, the object ID changes.

## Tiny Example

Create a file, commit it, then edit the file. The old blob still exists. The new commit points to a new tree that points to a new blob for the changed file.

## Common Misconceptions

- A branch is a pointer, not a folder.
- A commit is a snapshot plus metadata, not a diff.
- Rebasing rewrites commit identities.
- The index is a real staging data structure, not just a UI concept.

## Self-Check

1. What does a commit point to?
2. What changes when a file changes?
3. Why does rebase change hashes?
4. What is stored in the index?

## Further Reading

- Pro Git book: https://git-scm.com/book/en/v2
- Git reference docs: https://git-scm.com/docs

