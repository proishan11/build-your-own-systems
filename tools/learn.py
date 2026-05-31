#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "curriculum" / "curriculum.json"


def load_manifest():
    with MANIFEST.open("r", encoding="utf-8") as f:
        return json.load(f)


def progress_path(manifest):
    return ROOT / manifest.get("default_progress_file", "curriculum/state/progress.json")


def load_progress(manifest):
    path = progress_path(manifest)
    if not path.exists():
        return {"completed": []}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(manifest, progress):
    path = progress_path(manifest)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)
        f.write("\n")


def exercises(manifest):
    return manifest["exercises"]


def tracks(manifest):
    return {track["id"]: track for track in manifest["tracks"]}


def find_exercise(manifest, exercise_id):
    for exercise in exercises(manifest):
        if exercise["id"] == exercise_id:
            return exercise
    raise SystemExit(f"Unknown exercise: {exercise_id}")


def command_list(args):
    manifest = load_manifest()
    progress = load_progress(manifest)
    done = set(progress.get("completed", []))
    track_map = tracks(manifest)

    current_track = None
    for exercise in exercises(manifest):
        if args.track and exercise["track"] != args.track:
            continue
        if exercise["track"] != current_track:
            current_track = exercise["track"]
            title = track_map.get(current_track, {}).get("title", current_track)
            print(f"\n{title}")
        mark = "x" if exercise["id"] in done else " "
        print(f"  [{mark}] {exercise['id']}: {exercise['title']}")


def command_tracks(_args):
    manifest = load_manifest()
    for track in manifest["tracks"]:
        print(f"{track['id']}: {track['title']}")
        print(f"  {track['description']}")


def command_next(args):
    manifest = load_manifest()
    progress = load_progress(manifest)
    done = set(progress.get("completed", []))
    for exercise in exercises(manifest):
        if args.track and exercise["track"] != args.track:
            continue
        if exercise["id"] not in done:
            print_exercise_summary(exercise)
            return
    if args.track:
        print(f"No remaining exercises in track: {args.track}")
    else:
        print("No remaining exercises.")


def print_exercise_summary(exercise):
    print(f"{exercise['id']}: {exercise['title']}")
    print(f"Level: {exercise['level']}")
    print(f"Estimated time: {exercise['duration_minutes']} minutes")
    print(f"Concept: {exercise['concept']}")
    print(f"Exercise: {exercise['exercise']}")
    print(f"Validate: {exercise['validate']}")


def command_show(args):
    manifest = load_manifest()
    exercise = find_exercise(manifest, args.exercise_id)
    print_exercise_summary(exercise)

    if args.open == "concept":
        path = ROOT / exercise["concept"]
    elif args.open == "exercise":
        path = ROOT / exercise["exercise"]
    else:
        return

    print()
    if not path.exists():
        print(f"Missing file: {path}")
        return
    print(path.read_text(encoding="utf-8"))


def command_validate(args):
    manifest = load_manifest()
    exercise = find_exercise(manifest, args.exercise_id)
    command = exercise["validate"]
    if args.race and exercise.get("race_validate"):
        command = exercise["race_validate"]
    cwd = ROOT / exercise["workspace"]
    print(f"$ {command}")
    print(f"cwd: {cwd}")
    result = subprocess.run(command, cwd=cwd, shell=True)
    raise SystemExit(result.returncode)


def command_validate_all(args):
    manifest = load_manifest()
    failures = 0
    for exercise in exercises(manifest):
        if args.track and exercise["track"] != args.track:
            continue
        command = exercise["validate"]
        cwd = ROOT / exercise["workspace"]
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            text=True,
            capture_output=True,
            timeout=args.timeout,
        )
        if result.returncode != 0:
            failures += 1
        lines = (result.stdout + result.stderr).strip().splitlines()
        summary = " | ".join(lines[:2]) if lines else "no output"
        print(f"{exercise['id']}: exit={result.returncode} :: {summary[:220]}")
    if failures:
        print(f"\n{failures} validator(s) failed. This is expected for unimplemented scaffolds.")
    raise SystemExit(1 if failures and args.strict else 0)


def command_complete(args):
    manifest = load_manifest()
    find_exercise(manifest, args.exercise_id)
    progress = load_progress(manifest)
    completed = set(progress.get("completed", []))
    completed.add(args.exercise_id)
    progress["completed"] = sorted(completed)
    save_progress(manifest, progress)
    print(f"Marked complete: {args.exercise_id}")


def command_reset(args):
    manifest = load_manifest()
    progress = load_progress(manifest)
    completed = set(progress.get("completed", []))
    if args.exercise_id:
        completed.discard(args.exercise_id)
    else:
        completed.clear()
    progress["completed"] = sorted(completed)
    save_progress(manifest, progress)
    print("Progress updated.")


def main(argv):
    parser = argparse.ArgumentParser(description="Interactive curriculum helper")
    sub = parser.add_subparsers(dest="command", required=True)

    list_parser = sub.add_parser("list", help="List exercises")
    list_parser.add_argument("--track")
    list_parser.set_defaults(func=command_list)

    tracks_parser = sub.add_parser("tracks", help="List tracks")
    tracks_parser.set_defaults(func=command_tracks)

    next_parser = sub.add_parser("next", help="Show the next incomplete exercise")
    next_parser.add_argument("--track")
    next_parser.set_defaults(func=command_next)

    show_parser = sub.add_parser("show", help="Show exercise metadata")
    show_parser.add_argument("exercise_id")
    show_parser.add_argument("--open", choices=["concept", "exercise"])
    show_parser.set_defaults(func=command_show)

    validate_parser = sub.add_parser("validate", help="Run an exercise validator")
    validate_parser.add_argument("exercise_id")
    validate_parser.add_argument("--race", action="store_true", help="Use race validator when available")
    validate_parser.set_defaults(func=command_validate)

    validate_all_parser = sub.add_parser("validate-all", help="Run all scaffold validators")
    validate_all_parser.add_argument("--track")
    validate_all_parser.add_argument("--strict", action="store_true", help="Exit nonzero if any validator fails")
    validate_all_parser.add_argument("--timeout", type=int, default=20)
    validate_all_parser.set_defaults(func=command_validate_all)

    complete_parser = sub.add_parser("complete", help="Mark an exercise complete")
    complete_parser.add_argument("exercise_id")
    complete_parser.set_defaults(func=command_complete)

    reset_parser = sub.add_parser("reset", help="Clear completion state")
    reset_parser.add_argument("exercise_id", nargs="?")
    reset_parser.set_defaults(func=command_reset)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(sys.argv[1:])
