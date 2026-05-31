# Exercise 001: Git Object Explorer

Shared concept chapter: [Git Object Model](../../../../curriculum/concepts/developer-tools/git-object-model.md)

## Goal

Implement enough of Git's loose-object decoding to inspect a blob object.

## Contract

Edit `git_objects.py` so it:

- computes the same object ID Git uses for a blob
- encodes a blob as `b"blob <len>\\0" + data`
- decodes a loose object compressed with zlib
- returns object type and payload

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. Why does the object ID include the header?
2. Why does changing one byte change the object ID?
3. What does a tree object add beyond a blob?

