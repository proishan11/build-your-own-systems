# Portable Skill Installation

The source skill lives at:

```text
skills/interactive-learning-coach/
```

This folder is intentionally platform-neutral: it contains `SKILL.md` plus supporting Markdown references. Platform-specific files are thin adapters.

## npm Installer

The easiest install path is the npm skill installer:

```bash
npx build-your-own-systems-skill install codex
```

Other targets:

```bash
npx build-your-own-systems-skill install claude
npx build-your-own-systems-skill install windsurf
npx build-your-own-systems-skill install cursor --cwd .
npx build-your-own-systems-skill install generic --cwd .
```

Use `--force` to replace an existing install.

## Claude Code

Claude Code supports project and personal skills using `SKILL.md` folders.

Project install:

```bash
mkdir -p .claude/skills
cp -R skills/interactive-learning-coach .claude/skills/
```

Personal install:

```bash
mkdir -p ~/.claude/skills
cp -R skills/interactive-learning-coach ~/.claude/skills/
```

Invoke directly with:

```text
/interactive-learning-coach give me Hint 1 for the current exercise
```

Or ask naturally:

```text
Give me the next Go concurrency task and validate my implementation when I finish.
```

## Windsurf

Windsurf Cascade supports workspace and global skills using `SKILL.md` folders.

Workspace install:

```bash
mkdir -p .windsurf/skills
cp -R skills/interactive-learning-coach .windsurf/skills/
```

Global install:

```bash
mkdir -p ~/.codeium/windsurf/skills
cp -R skills/interactive-learning-coach ~/.codeium/windsurf/skills/
```

Windsurf can also discover cross-agent skills from `.agents/skills/`, so another portable option is:

```bash
mkdir -p .agents/skills
cp -R skills/interactive-learning-coach .agents/skills/
```

Invoke explicitly with:

```text
@interactive-learning-coach explain the approach without code
```

## Cursor

Cursor currently uses project rules rather than `SKILL.md` folders as its main reusable-instruction mechanism.

Install the Cursor adapter:

```bash
mkdir -p .cursor/rules
cp adapters/cursor/interactive-learning-coach.mdc .cursor/rules/
```

Keep the source skill folder in the repository so the Cursor rule can point the agent at:

```text
skills/interactive-learning-coach/SKILL.md
```

For tools that read `AGENTS.md`, copy:

```bash
cp adapters/generic/AGENTS.md ./AGENTS.md
```

## Codex

Install as a personal Codex skill:

```bash
mkdir -p ~/.codex/skills
cp -R skills/interactive-learning-coach ~/.codex/skills/
```

Invoke with:

```text
Use $interactive-learning-coach to validate and review my implementation.
```

## Generic Agents

For agents without native skill support:

1. Keep `skills/interactive-learning-coach/` in the repo.
2. Add the `AGENTS.md` adapter at the repo root.
3. Ask the agent to use `skills/interactive-learning-coach/SKILL.md`.

The skill is just Markdown plus references, so any capable coding agent can follow it if the files are visible in the workspace.

## Compatibility Notes

Current platform shape:

- Claude Code supports `SKILL.md` folders under `.claude/skills/` or `~/.claude/skills/`.
- Windsurf Cascade supports `SKILL.md` folders under `.windsurf/skills/`, `~/.codeium/windsurf/skills/`, and cross-agent `.agents/skills/`.
- Cursor's main reusable instruction mechanism is project rules in `.cursor/rules/*.mdc`; it also supports `AGENTS.md` as a simple project instruction file.
- Codex supports local skills under `~/.codex/skills/` in this environment.

Keep `skills/interactive-learning-coach/` as the source of truth and regenerate/copy adapters from it when publishing.
