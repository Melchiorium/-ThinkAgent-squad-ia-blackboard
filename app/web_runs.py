from __future__ import annotations

import re
from pathlib import Path

EXPECTED_RUN_FILES = [
    "project-brief.md",
    "prd.md",
    "architecture.md",
    "architecture-diagram.mmd",
    "architecture-diagram.png",
    "gtm.md",
    "blackboard.md",
    "activity_log.txt",
]

_VERSION_PATTERN = re.compile(r"^version (\d+)$")


def list_runs(outputs_root: Path | None = None) -> list[dict]:
    tests_root = _resolve_tests_root(outputs_root)
    if not tests_root.exists():
        return []

    runs: list[dict] = []
    for project_dir in sorted(
        (path for path in tests_root.iterdir() if path.is_dir()),
        key=lambda path: path.name.lower(),
    ):
        project_runs = _collect_project_runs(project_dir)
        runs.extend(project_runs)

    return sorted(
        runs,
        key=lambda run: (run["project"].lower(), run["version_number"]),
    )


def get_run(project: str, version: str, outputs_root: Path | None = None) -> dict | None:
    for run in list_runs(outputs_root):
        if run["project"] == project and run["version"] == version:
            return run
    return None


def _resolve_outputs_root(outputs_root: Path | None) -> Path:
    if outputs_root is None:
        return Path(__file__).resolve().parent.parent / "outputs"
    return outputs_root.resolve()


def _resolve_tests_root(outputs_root: Path | None) -> Path:
    outputs_base = _resolve_outputs_root(outputs_root)
    if outputs_base.name == "tests":
        return outputs_base
    return outputs_base / "tests"


def _collect_project_runs(project_dir: Path) -> list[dict]:
    runs: list[dict] = []
    for version_dir in sorted(
        (path for path in project_dir.iterdir() if path.is_dir()),
        key=_version_sort_key,
    ):
        version_match = _VERSION_PATTERN.fullmatch(version_dir.name)
        if not version_match:
            continue
        version_number = int(version_match.group(1))
        files = {
            file_name: (version_dir / file_name).is_file()
            for file_name in EXPECTED_RUN_FILES
        }
        runs.append(
            {
                "project": project_dir.name,
                "version": version_dir.name,
                "version_number": version_number,
                "path": str(version_dir.resolve()),
                "files": files,
                "missing_files": [
                    file_name for file_name, present in files.items() if not present
                ],
                "has_architecture_png": files["architecture-diagram.png"],
            }
        )
    return runs


def _version_sort_key(path: Path) -> tuple[int, str]:
    match = _VERSION_PATTERN.fullmatch(path.name)
    if not match:
        return (10**9, path.name.lower())
    return (int(match.group(1)), path.name.lower())
