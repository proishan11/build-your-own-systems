#!/usr/bin/env python3
"""Audit the generated catalog implementation ladders.

The catalog scaffolds are concrete per-project ladders under
`playgrounds/catalog/**`. This script is intentionally conservative: it reports
missing files and manifest drift, but it does not overwrite the generated labs.
"""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "curriculum" / "catalog" / "project-catalog.md"
MANIFEST = ROOT / "curriculum" / "curriculum.json"


SECTION_TO_TRACK = {
    "Systems Programming": "systems-programming",
    "Operating Systems and Kernels": "os-kernel-labs",
    "Networking": "networking",
    "Deep Networking": "deep-networking",
    "Go Concurrency": "go-concurrency",
    "Distributed Systems": "distributed-systems",
    "Database Systems": "database-systems",
    "ML Systems and Deep Learning Infrastructure": "ml-systems",
    "LLM Application Engineering": "llm-engineering",
    "AI, RAG, and Agents": "ai-rag-agents",
    "Kubernetes": "containers-kubernetes",
    "Containers": "containers-kubernetes",
    "Unix Command Line": "tooling-foundations",
    "Vim": "tooling-foundations",
    "Git": "tooling-foundations",
    "PostgreSQL Administration": "postgres-administration",
    "System Design and SRE": "sre-system-design",
    "Security Engineering": "security-engineering",
    "Performance Engineering": "performance-engineering",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def parse_catalog() -> list[tuple[str, str]]:
    section = None
    projects = []
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        elif line.startswith("### ") and section not in {
            "How To Read This Catalog",
            "Recommended Staff-Level Path",
        }:
            projects.append((section, line[4:].strip()))
    return projects


EXERCISES = [
    ("001-project-kickoff", "lab.py", "tests/test_lab.py"),
    ("002-state-model", "lab_002.py", "tests/test_lab_002.py"),
    ("003-operation-planner", "lab_003.py", "tests/test_lab_003.py"),
    ("004-failure-recovery", "lab_004.py", "tests/test_lab_004.py"),
    ("005-integration-simulation", "lab_005.py", "tests/test_lab_005.py"),
]


def expected_paths(section: str, project: str) -> tuple[list[str], Path, list[Path]]:
    track = SECTION_TO_TRACK[section]
    project_slug = slugify(project)
    workspace = ROOT / "playgrounds" / "catalog" / track / project_slug
    exercise_ids = [f"catalog/{track}/{project_slug}/{slug}" for slug, _lab, _test in EXERCISES]
    paths = []
    for slug, lab, test in EXERCISES:
        paths.extend(
            [
                workspace / "exercises" / f"{slug}.md",
                workspace / lab,
                workspace / test,
            ]
        )
    return (
        exercise_ids,
        workspace,
        paths,
    )


def main() -> int:
    projects = parse_catalog()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest_ids = {exercise["id"] for exercise in manifest["exercises"]}

    missing_files = []
    missing_manifest_entries = []
    for section, project in projects:
        exercise_ids, _workspace, paths = expected_paths(section, project)
        for exercise_id in exercise_ids:
            if exercise_id not in manifest_ids:
                missing_manifest_entries.append(exercise_id)
        for path in paths:
            if not path.exists():
                missing_files.append(path.relative_to(ROOT))

    print(f"Catalog projects: {len(projects)}")
    print(f"Expected exercises per project: {len(EXERCISES)}")
    print("Expected files per exercise: exercise markdown, lab module, test module")
    print(f"Manifest exercises: {len(manifest['exercises'])}")

    if missing_manifest_entries or missing_files:
        if missing_manifest_entries:
            print("\nMissing manifest entries:")
            for exercise_id in missing_manifest_entries:
                print(f"- {exercise_id}")
        if missing_files:
            print("\nMissing scaffold files:")
            for path in missing_files:
                print(f"- {path}")
        return 1

    print("Catalog implementation ladders are complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
