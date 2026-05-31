# Repository Tour

This repository has three layers:

1. curriculum content
2. runnable playgrounds
3. portable AI coaching instructions

## Top-Level Layout

```text
README.md
CONTRIBUTING.md
LICENSE
package.json
bin/
curriculum/
playgrounds/
skills/
adapters/
docs/
tools/
dist/
```

## `curriculum/`

The curriculum directory is the source of truth for course structure.

Important files:

- `curriculum/curriculum.json`: machine-readable manifest used by `tools/learn.py`.
- `curriculum/catalog/project-catalog.md`: broad project catalog across systems, databases, distributed systems, AI, tooling, security, performance, and operations.
- `curriculum/concepts/`: reusable concept chapters.
- `curriculum/projects/`: deeper project descriptions for major tracks.
- `curriculum/roadmap/`: planning, implementation status, and scaffolding sequence.
- `curriculum/rubrics/staff-engineer-review.md`: review criteria.
- `curriculum/templates/exercise-template.md`: structure for new exercises.
- `curriculum/state/progress.json`: local progress state.

## `playgrounds/`

The playgrounds directory contains the code learners edit.

There are two kinds of playgrounds:

- first-wave deeper exercises, such as Go concurrency, MiniDB, networking, OS, and tooling foundations
- catalog ladders under `playgrounds/catalog/`

Catalog ladder shape:

```text
playgrounds/catalog/<track>/<project>/
  exercises/
    001-project-kickoff.md
    002-state-model.md
    003-operation-planner.md
    004-failure-recovery.md
    005-integration-simulation.md
  lab.py
  lab_002.py
  lab_003.py
  lab_004.py
  lab_005.py
  tests/
    test_lab.py
    test_lab_002.py
    test_lab_003.py
    test_lab_004.py
    test_lab_005.py
```

Each exercise has its own validator in `curriculum/curriculum.json`, so learners can work one milestone at a time.

## `skills/`

The portable coaching skill lives here:

```text
skills/interactive-learning-coach/
```

It contains:

- `SKILL.md`: the main agent behavior instructions
- `references/exercise-format.md`
- `references/hinting.md`
- `references/lesson-format.md`
- `references/project-map.md`
- `references/reading-list.md`
- `references/staff-review.md`

This is the source of truth for all platform adapters.

## `adapters/`

Adapters let tools without native skill support use the same coaching behavior.

- `adapters/cursor/interactive-learning-coach.mdc`: Cursor rule.
- `adapters/generic/AGENTS.md`: generic agent instruction file.

## `tools/`

Main learner CLI:

```bash
tools/learn.py tracks
tools/learn.py list
tools/learn.py next
tools/learn.py show <exercise-id> --open exercise
tools/learn.py validate <exercise-id>
tools/learn.py validate-all
tools/learn.py complete <exercise-id>
```

Catalog audit:

```bash
python3 tools/scaffold_catalog.py
```

Despite the name, `scaffold_catalog.py` is now conservative. It audits the generated catalog ladders rather than overwriting them.

## `bin/` and `package.json`

The npm skill installer entry point lives at:

```text
bin/install-build-your-own-systems-skill.js
```

It installs the portable coaching skill into a supported agent environment when users run:

```bash
npx build-your-own-systems-skill install codex
```

The package metadata lives in `package.json`. The npm package is intentionally limited to the skill, adapters, and install docs; it does not distribute `curriculum/`, `playgrounds/`, or `tools/`.

## `dist/`

The portable package is built here:

```text
dist/build-your-own-systems-portable.zip
```

The package includes curriculum docs, playgrounds, tools, skill source, and adapters.

## How The Manifest Works

Each manifest exercise contains:

- `id`: stable exercise identifier
- `track`: track grouping
- `title`: human-readable title
- `level`: foundation, intermediate, or advanced
- `duration_minutes`: rough estimate
- `concept`: concept chapter path
- `exercise`: exercise markdown path
- `workspace`: directory where validation runs
- `validate`: validation command
- `status`: scaffolded/completed state for curriculum authors
- `catalog_project`: optional project name
- `depends_on`: optional previous exercise

The CLI reads this manifest rather than discovering exercises from the filesystem.
