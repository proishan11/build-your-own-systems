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

## How It Works Step By Step

A commit is the visible unit in everyday Git, but it is assembled from smaller immutable objects.

| Step | Object Created Or Updated | What It Represents |
| --- | --- | --- |
| Store file bytes | Blob | File contents without filename. |
| Build directory snapshot | Tree | Names, modes, and child object IDs. |
| Record history | Commit | Tree pointer, parent commit IDs, author, and message. |
| Move branch | Ref update | Human-readable name now points at the new commit. |
| Update working state | Index and working tree | The next staged snapshot and editable files. |

The object database is mostly immutable. Refs are mutable pointers. Many Git surprises become easier when you separate those two facts.

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

## State Or Flow Walkthrough

Start with one commit:

```text
main -> C1 -> T1 -> B_readme
```

Edit `README.md` and commit again:

```text
main -> C2 -> T2 -> B_readme_v2
        |
        parent -> C1
```

The branch did not contain the files. The branch moved from `C1` to `C2`. The new commit points to a new tree, and the tree points to blobs. If another file did not change, the new tree can still point at the old blob.

This is why Git can make branching cheap: creating a branch is usually just creating another ref pointing at an existing commit.

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

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| `tooling/002-git-object-explorer` | Reading raw objects, decoding type/length headers, and walking blob/tree/commit links. |
| Mini Git project ladder | Object encoding, tree construction, commit writing, and ref updates. |
| Git merge and rebase lab | Parent links, merge bases, rewritten commits, and ref movement. |

When solving Git exercises, draw the graph before changing code. Most implementation errors are graph errors wearing command-line clothes.

## Exercise Bridge

Git exercises use this concept for object exploration, mini-Git storage, merge-base, rebasing, and conflict reasoning. Before implementing, draw the object graph for the case you are testing.

## Readiness Checklist

You are ready to implement a Git object exercise when you can:

- explain why blobs do not store filenames
- distinguish immutable objects from mutable refs
- draw a commit with its tree and parent links
- describe what moves when `main` advances
- explain how two branches can share most objects

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
