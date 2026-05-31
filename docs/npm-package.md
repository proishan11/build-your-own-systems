# npm Skill Package

The npm package installs the portable `interactive-learning-coach` skill. It does not distribute the full curriculum codebase.

The GitHub repository remains the source of truth for:

- curriculum content
- playground code
- validators
- docs
- package source

Use npm when you want a one-command way to install the skill into an AI coding tool.

## Package Name

```text
build-your-own-systems-skill
```

## Install Into Codex

```bash
npx build-your-own-systems-skill install codex
```

This installs:

```text
~/.codex/skills/interactive-learning-coach/
```

## Install Into Claude Code

Personal install:

```bash
npx build-your-own-systems-skill install claude
```

Project install:

```bash
npx build-your-own-systems-skill install claude --scope project --cwd .
```

## Install Into Windsurf

Personal install:

```bash
npx build-your-own-systems-skill install windsurf
```

Workspace install:

```bash
npx build-your-own-systems-skill install windsurf --scope project --cwd .
```

Cross-agent workspace install:

```bash
npx build-your-own-systems-skill install windsurf --scope agents --cwd .
```

## Install Into Cursor

Cursor uses project rules, so the installer copies both the skill source and a Cursor rule into the current project:

```bash
npx build-your-own-systems-skill install cursor --cwd .
```

This installs:

```text
skills/interactive-learning-coach/
.cursor/rules/interactive-learning-coach.mdc
```

## Install For Generic Agents

```bash
npx build-your-own-systems-skill install generic --cwd .
```

This installs:

```text
skills/interactive-learning-coach/
AGENTS.md
```

## Updating An Existing Install

The installer does not overwrite existing skill files by default. Re-run with `--force` to replace an existing install:

```bash
npx build-your-own-systems-skill install codex --force
```

## After Installing

Open a curriculum workspace and start with:

```text
Use $interactive-learning-coach. Start the next exercise.
First read the local exercise, tests, and source files. Then teach me the concept before I implement anything.
```

See [Using The AI Coach](using-the-ai-coach.md) for a full step-by-step example workflow.

## Local Smoke Test

From the repo root:

```bash
node bin/install-build-your-own-systems-skill.js install generic --cwd /tmp/byos-skill-smoke
test -f /tmp/byos-skill-smoke/skills/interactive-learning-coach/SKILL.md
test -f /tmp/byos-skill-smoke/AGENTS.md
```

Inspect package contents:

```bash
npm pack --dry-run
```

The package should include only:

- `README.md`
- `LICENSE`
- skill installer CLI
- `skills/interactive-learning-coach/`
- `adapters/`
- npm/skill install docs

It should not include `curriculum/`, `playgrounds/`, or `tools/`.

## Publish

Publish beta:

```bash
npm publish --access public --tag beta
```

After the beta is stable:

```bash
npm dist-tag add build-your-own-systems-skill@0.1.0 latest
```

## Release Checklist

Before publishing:

```bash
python3 /Users/proishan/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/interactive-learning-coach
node --check bin/install-build-your-own-systems-skill.js
node bin/install-build-your-own-systems-skill.js install generic --cwd /tmp/byos-skill-smoke --force
npm pack --dry-run
```

For npm, keep `package.json` at `0.1.0` and publish with `--tag beta`.
