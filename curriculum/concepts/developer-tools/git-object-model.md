# Git Object Model

## What You Should Know First

You should know basic Git commands such as `git add`, `git commit`, `git branch`, and `git log`. This chapter explains the storage model underneath those commands.

## The Problem

Git needs to store snapshots, history, branches, merges, and content identity in a way that is local, efficient, and verifiable. The user interface talks about commits and branches, but the core is a content-addressed object database.

Understanding that database makes Git feel less magical. It also makes merge conflicts, rebases, tags, and detached HEAD states easier to reason about.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Blob | File contents, without the filename. |
| Tree | Directory listing that maps names to blobs or other trees. |
| Commit | Snapshot pointer plus parents, author metadata, and message. |
| Object ID | Hash-derived name for an object's content. |
| Ref | Human-readable pointer such as `refs/heads/main`. |
| HEAD | Pointer to the current branch or commit. |
| Index | Staging area that records the next tree to commit. |

## Mental Model

Git stores snapshots as a graph:

```text
commit -> tree -> blobs
   |
 parent commit
```

A branch is not the history itself. It is a movable pointer to a commit. The history is recovered by walking parent links.

## Core Invariant

An object ID must name exactly the content used to compute it.

This gives Git its integrity property. If object bytes change, the object ID changes. References can move, but objects are immutable once named.

## Worked Example

Suppose a repository has one file:

```text
README.md = "hello"
```

Git stores the file contents as a blob. A tree maps `README.md` to that blob. A commit points to the tree and to its parent commit, if any. The branch `main` points to the latest commit.

When you edit `README.md` and commit again, Git creates a new blob for the new contents, a new tree for the new snapshot, and a new commit pointing to the previous commit.

## Implementation Shape

A mini-Git implementation usually grows through these pieces:

| Piece | Responsibility |
| --- | --- |
| Object encoder | Prefixes object type and length, then hashes bytes. |
| Object store | Writes and reads objects by ID. |
| Tree builder | Records names, modes, and child object IDs. |
| Commit writer | Stores tree, parents, author, and message. |
| Ref manager | Reads and updates branch pointers safely. |
| Graph walker | Traverses parents for log, merge-base, and reachability. |

Keep object storage separate from working-tree status. The object database is immutable; refs and the index are the mutable parts.

## Failure Modes

| Failure | Consequence |
| --- | --- |
| Hashing only file contents for commits | Metadata and parents no longer affect identity. |
| Confusing branch with commit | Rebase, checkout, and detached HEAD become mysterious. |
| Treating file names as blob data | Renames become impossible to model correctly. |
| Updating refs unsafely | Crashes can lose branch tips. |
| Ignoring modes | Executable bits and tree entries become inaccurate. |

## Exercise Bridge

Git exercises use this concept for object exploration, mini-Git storage, merge-base, rebasing, and conflict reasoning. Before implementing, draw the object graph for the case you are testing.

## Self-Check

1. Why does a blob not store its filename?
2. What moves when a branch advances?
3. What does a commit point to?
4. Why is the object store content-addressed?
5. How can two branches share most of their history?

## Further Reading

- Pro Git, Git Internals: https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain
- Git object documentation: https://git-scm.com/docs/gitrepository-layout
- Git from the Bottom Up: https://jwiegley.github.io/git-from-the-bottom-up/
