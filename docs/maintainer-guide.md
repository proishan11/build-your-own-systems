# Maintainer Guide

This guide is for people publishing, extending, or auditing the curriculum.

## Release Checklist

Before publishing a release:

```bash
python3 -m json.tool curriculum/curriculum.json >/tmp/curriculum-json-ok
python3 tools/scaffold_catalog.py
python3 -m py_compile tools/learn.py tools/scaffold_catalog.py
node --check bin/install-build-your-own-systems-skill.js
npm pack --dry-run
python3 /Users/proishan/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/interactive-learning-coach
tools/learn.py validate-all
```

Expected result:

- JSON validation passes.
- Project ladder audit passes.
- Skill validation passes.
- npm dry run succeeds.
- `validate-all` reaches every exercise and reports expected scaffold failures.

On a fresh scaffold, `validate-all` should not pass. It should fail because learner implementations are incomplete.

## Current Curriculum Surface

The course currently has:

- 365 runnable, project-specific scaffolded implementation exercises.
- 15 foundation exercises.
- 350 project ladder exercises across 70 five-exercise ladders.

Audit:

```bash
python3 tools/scaffold_catalog.py
```

Expected output includes:

```text
Project ladders from catalog: 70
Expected exercises per project: 5
Manifest exercises: 365
Project-specific implementation ladders are complete.
```

## Adding A New Exercise

Use the exercise template:

```text
curriculum/templates/exercise-template.md
```

Every exercise should include:

- concept primer
- why this matters
- mental model
- core invariant
- tiny example
- common misconceptions
- self-check
- goal
- files to edit
- contract
- design hints
- validation command
- further reading
- Staff-level review questions

Add:

1. Exercise markdown under the relevant `playgrounds/.../exercises/` directory.
2. Placeholder implementation that compiles or imports.
3. Tests that fail for the intended learner-work reason.
4. Manifest entry in `curriculum/curriculum.json`.
5. Concept chapter link, or a new concept chapter if needed.

## Placeholder Rules

Good placeholders:

- compile/import successfully
- expose a stable public API
- fail with `NotImplementedError`, `ErrNotImplemented`, or a focused behavior mismatch
- include comments explaining the design pressure
- avoid solving the exercise in comments

Bad placeholders:

- fail because files are missing
- fail because imports are broken
- require unrelated services to start
- hide the real learning objective behind setup complexity

## Validation Rules

Validators should be scoped to the current exercise.

For project ladder exercises under `playgrounds/catalog/`, prefer:

```bash
python3 -m unittest discover -s tests -p test_lab_003.py
```

This avoids running future milestone tests before the learner reaches them.

For Go exercises, use the local package's normal test command:

```bash
go test ./...
```

Add race validation when concurrency behavior matters:

```bash
go test -race ./...
```

## Building The Portable Package

The release artifact is:

```text
dist/build-your-own-systems-portable.zip
```

Rebuild it after curriculum, docs, skill, or adapter changes:

```bash
find . -type d -name __pycache__ -prune -exec rm -rf {} +
python3 - <<'PY'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path.cwd()
out = root / "dist" / "build-your-own-systems-portable.zip"
out.parent.mkdir(exist_ok=True)
include_roots = [
    root / "bin",
    root / "skills" / "interactive-learning-coach",
    root / "adapters",
    root / "docs",
    root / "curriculum",
    root / "playgrounds",
    root / "tools",
]
include_files = [
    root / "README.md",
    root / "LICENSE",
    root / "CONTRIBUTING.md",
    root / "package.json",
]
exclude_parts = {".git", "dist", "__pycache__", ".pytest_cache"}
exclude_suffixes = {".pyc", ".pyo", ".DS_Store"}

def should_include(path: Path) -> bool:
    rel = path.relative_to(root)
    if any(part in exclude_parts for part in rel.parts):
        return False
    if path.name in exclude_suffixes or path.suffix in exclude_suffixes:
        return False
    return path.is_file()

with ZipFile(out, "w", ZIP_DEFLATED) as zf:
    for file in include_files:
        if should_include(file):
            zf.write(file, file.relative_to(root))
    for base in include_roots:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if should_include(path):
                zf.write(path, path.relative_to(root))

print(out)
PY
```

Verify package contents:

```bash
zipinfo -1 dist/build-your-own-systems-portable.zip | rg 'project_contract|__pycache__|\\.pyc'
zipinfo -1 dist/build-your-own-systems-portable.zip | rg '^playgrounds/catalog/.+/exercises/.+\\.md$' | wc -l
```

The first command should print nothing. The second should print `350`.

## Publishing The npm Skill Installer

The npm package installs the portable coaching skill only. The GitHub repository remains the source of truth for the full curriculum and playground code.

Local smoke test:

```bash
rm -rf /tmp/byos-skill-smoke
node bin/install-build-your-own-systems-skill.js install generic --cwd /tmp/byos-skill-smoke
test -f /tmp/byos-skill-smoke/skills/interactive-learning-coach/SKILL.md
test -f /tmp/byos-skill-smoke/AGENTS.md
```

Publish beta:

```bash
npm publish --access public --tag beta
```

See [npm Package](npm-package.md) for details.

## Publication Notes

Recommended release label:

```text
v0.1-beta
```

Suggested positioning:

```text
Build Your Own Systems is a curriculum-as-code playground for learning systems,
databases, distributed systems, networking, AI agents, RAG, Kubernetes,
PostgreSQL administration, security, performance, and developer tooling by
implementing scaffolded projects with AI-coached review.
```

Before a public GitHub release, add:

- `CHANGELOG.md`
- release notes with the exercise count and beta status
