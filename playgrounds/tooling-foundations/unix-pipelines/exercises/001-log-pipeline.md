# Exercise 001: Unix Pipeline Workbench

Shared concept chapter: [Unix Pipelines](../../../../curriculum/concepts/developer-tools/unix-pipelines.md)

## Goal

Write a shell pipeline that summarizes error counts by endpoint from `data/access.log`.

## Contract

Edit `solutions/error_counts.sh` so it:

- reads `data/access.log`
- filters only rows whose status code is `500` or higher
- groups by endpoint path
- prints counts in descending numeric order
- emits exactly:

```text
3 /api/orders
2 /api/search
1 /api/users
```

## Validation

Run:

```bash
python3 -m unittest discover -s tests
```

## Staff-Level Review Questions

1. What goes to stdout versus stderr?
2. How does the script behave if the input file is missing?
3. Does the pipeline depend on incidental input ordering?

