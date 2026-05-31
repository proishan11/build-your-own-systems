# Contributing

Thanks for helping improve Build Your Own Systems.

This repository is a curriculum-as-code project. Contributions should make it easier for learners to understand concepts, implement real systems components, validate their work, and review their designs with Staff-level rigor.

## What To Contribute

Good contributions include:

- new scaffolded exercises
- stronger tests for existing exercises
- clearer concept explanations
- better hints that do not reveal full solutions too early
- references to primary papers, official docs, or excellent teaching material
- fixes for broken validators, imports, paths, or docs
- improvements to the portable coaching skill and adapters

Avoid contributing complete learner solutions into the scaffold paths. The main branch should preserve the learning experience: stubs should fail until the learner implements them.

## Exercise Quality Bar

Every substantial exercise should include:

- concept primer
- why this matters
- mental model
- core invariant
- tiny example
- common misconceptions
- self-check questions
- files to edit
- implementation contract
- design hints
- validation command
- further reading
- Staff-level review questions

Placeholder code should compile or import successfully and fail for the intended learner-work reason, such as `NotImplementedError`, `ErrNotImplemented`, or a focused behavior mismatch.

## Validation Before Opening A PR

Run these checks from the repository root:

```bash
python3 -m json.tool curriculum/curriculum.json >/tmp/curriculum-json-ok
python3 tools/scaffold_catalog.py
python3 -m py_compile tools/learn.py tools/scaffold_catalog.py
tools/learn.py validate-all
```

`validate-all` is expected to report scaffold failures on a fresh checkout. That command is healthy when it reaches every exercise and failures point at learner stubs, not missing files, syntax errors, or broken imports.

If you changed the skill, also run the skill validator if available:

```bash
python3 /Users/proishan/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/interactive-learning-coach
```

If that local validator is unavailable, at minimum inspect `skills/interactive-learning-coach/SKILL.md` and keep the frontmatter valid.

## Adding A New Exercise

1. Add exercise markdown under the relevant `playgrounds/.../exercises/` directory.
2. Add placeholder implementation files.
3. Add tests or validators.
4. Add or reuse a concept chapter under `curriculum/concepts/`.
5. Add a manifest entry in `curriculum/curriculum.json`.
6. Run the validation checks above.

Use [curriculum/templates/exercise-template.md](curriculum/templates/exercise-template.md) as the base structure.

## Concept Chapter Standard

Concept chapters should be self-contained teaching material, not short project blurbs. A learner should be able to read the chapter before opening the exercise and understand the vocabulary, mental model, invariant, worked example, implementation shape, and common failure modes.

Use [curriculum/concepts/INDEX.md](curriculum/concepts/INDEX.md) as the source of truth for the required chapter shape.

## Adding A Project Ladder

Project ladders should be real implementation work, not just project ideas.

Each project ladder currently has five exercises:

1. core mechanism and first invariant
2. state model and invariants
3. operation planner and deterministic diffs
4. failure, retry, and recovery boundary
5. integration simulation and operational report

After adding a project ladder, update:

- the relevant chapter under `curriculum/catalog/chapters/`
- `curriculum/catalog/project-catalog.md` if the chapter index or counts change
- `curriculum/curriculum.json`
- `playgrounds/catalog/<track>/<project>/`
- any relevant concept chapter or reading list

Then run:

```bash
python3 tools/scaffold_catalog.py
```

## Documentation Shape

Prefer chapter-sized documents over mega-documents. As a rule of thumb, split a learner-facing Markdown file once it grows past roughly 400 lines or starts mixing unrelated purposes.

Use tables for catalogs, roadmaps, comparisons, and maintenance checklists. Use prose for mental models, learning arcs, and design rationale. Bullets are still useful for short checklists, but they should not be the default shape for long curriculum material.

## Documentation Style

Write for a learner who is seeing the topic for the first time but wants to grow into Staff-level reasoning.

Prefer:

- concrete invariants
- small examples
- explicit failure modes
- deterministic validation
- references with a short reason why they matter

Avoid:

- vague slogans
- giant projects with no first milestone
- hidden setup requirements
- tests that only verify shape but not behavior
- hints that directly solve the exercise

## Release Changes

If a change affects packaging or publishing, update:

- [README.md](README.md)
- [docs/maintainer-guide.md](docs/maintainer-guide.md)
- [docs/npm-package.md](docs/npm-package.md)
- `package.json`

The GitHub repository is the source of truth. The npm package installs the portable coaching skill only; it should not distribute the full curriculum codebase.
