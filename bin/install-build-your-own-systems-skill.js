#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const PACKAGE_ROOT = path.resolve(__dirname, "..");
const SKILL_NAME = "interactive-learning-coach";
const SKILL_SOURCE = path.join(PACKAGE_ROOT, "skills", SKILL_NAME);
const CURSOR_ADAPTER = path.join(PACKAGE_ROOT, "adapters", "cursor", `${SKILL_NAME}.mdc`);
const GENERIC_ADAPTER = path.join(PACKAGE_ROOT, "adapters", "generic", "AGENTS.md");

function usage() {
  console.log(`Usage:
  npx build-your-own-systems-skill install codex [--force]
  npx build-your-own-systems-skill install claude [--scope user|project] [--cwd <path>] [--force]
  npx build-your-own-systems-skill install windsurf [--scope user|project|agents] [--cwd <path>] [--force]
  npx build-your-own-systems-skill install cursor [--cwd <path>] [--force]
  npx build-your-own-systems-skill install generic [--cwd <path>] [--force]

Targets:
  codex      ~/.codex/skills/interactive-learning-coach
  claude     ~/.claude/skills or .claude/skills
  windsurf   ~/.codeium/windsurf/skills, .windsurf/skills, or .agents/skills
  cursor     ./skills/interactive-learning-coach plus .cursor/rules adapter
  generic    ./skills/interactive-learning-coach plus AGENTS.md
`);
}

function parseArgs(argv) {
  const args = {
    command: argv[2],
    target: argv[3],
    scope: "user",
    cwd: process.cwd(),
    force: false,
  };

  for (let i = 4; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--force") {
      args.force = true;
    } else if (arg === "--scope") {
      args.scope = argv[++i];
    } else if (arg === "--cwd") {
      args.cwd = path.resolve(argv[++i]);
    } else if (arg === "-h" || arg === "--help") {
      args.command = "help";
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return args;
}

function ensureSourceExists() {
  if (!fs.existsSync(SKILL_SOURCE)) {
    throw new Error(`Missing skill source: ${SKILL_SOURCE}`);
  }
}

function copyDirectory(source, destination, force) {
  if (fs.existsSync(destination)) {
    if (!force) {
      throw new Error(`Destination already exists: ${destination}\nRe-run with --force to replace it.`);
    }
    fs.rmSync(destination, { recursive: true, force: true });
  }
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.cpSync(source, destination, { recursive: true });
}

function copyFile(source, destination, force) {
  if (fs.existsSync(destination) && !force) {
    throw new Error(`Destination already exists: ${destination}\nRe-run with --force to replace it.`);
  }
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.copyFileSync(source, destination);
}

function installSkill(parentDir, force) {
  const destination = path.join(parentDir, SKILL_NAME);
  copyDirectory(SKILL_SOURCE, destination, force);
  return destination;
}

function installProjectSkill(cwd, force) {
  return installSkill(path.join(cwd, "skills"), force);
}

function targetInstall(args) {
  const home = os.homedir();
  const cwd = path.resolve(args.cwd);

  if (args.target === "codex") {
    return [installSkill(path.join(home, ".codex", "skills"), args.force)];
  }

  if (args.target === "claude") {
    if (args.scope === "project") {
      return [installSkill(path.join(cwd, ".claude", "skills"), args.force)];
    }
    if (args.scope !== "user") {
      throw new Error("Claude scope must be user or project.");
    }
    return [installSkill(path.join(home, ".claude", "skills"), args.force)];
  }

  if (args.target === "windsurf") {
    if (args.scope === "project") {
      return [installSkill(path.join(cwd, ".windsurf", "skills"), args.force)];
    }
    if (args.scope === "agents") {
      return [installSkill(path.join(cwd, ".agents", "skills"), args.force)];
    }
    if (args.scope !== "user") {
      throw new Error("Windsurf scope must be user, project, or agents.");
    }
    return [installSkill(path.join(home, ".codeium", "windsurf", "skills"), args.force)];
  }

  if (args.target === "cursor") {
    const skillPath = installProjectSkill(cwd, args.force);
    const rulePath = path.join(cwd, ".cursor", "rules", `${SKILL_NAME}.mdc`);
    copyFile(CURSOR_ADAPTER, rulePath, args.force);
    return [skillPath, rulePath];
  }

  if (args.target === "generic") {
    const skillPath = installProjectSkill(cwd, args.force);
    const agentsPath = path.join(cwd, "AGENTS.md");
    copyFile(GENERIC_ADAPTER, agentsPath, args.force);
    return [skillPath, agentsPath];
  }

  throw new Error(`Unknown target: ${args.target}`);
}

function main() {
  let args;
  try {
    args = parseArgs(process.argv);
  } catch (error) {
    console.error(error.message);
    usage();
    process.exit(1);
  }

  if (args.command === "help" || args.command === "-h" || args.command === "--help") {
    usage();
    return;
  }

  if (args.command !== "install" || !args.target) {
    usage();
    process.exit(1);
  }

  try {
    ensureSourceExists();
    const installed = targetInstall(args);
    console.log("Installed Build Your Own Systems skill:");
    for (const item of installed) {
      console.log(`  ${item}`);
    }
    console.log("");
    console.log("Try:");
    console.log("  Use $interactive-learning-coach to teach me the next concept before I code.");
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

main();

