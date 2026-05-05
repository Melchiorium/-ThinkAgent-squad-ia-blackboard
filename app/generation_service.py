from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import re
import sys
from pathlib import Path

if __package__ and __package__.startswith("app"):
    from .artifact_writer import write_run_artifacts
    from .orchestrator import run_v0_flow
else:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from artifact_writer import write_run_artifacts
    from orchestrator import run_v0_flow


@dataclass(frozen=True)
class GenerationResult:
    project_name: str
    project_brief_source: str
    output_dir: Path
    blackboard: dict


def run_generation_from_brief(
    brief_text: str,
    project_brief_source: str = "web://brief",
    outputs_root: Path | None = None,
    evaluator_report_text: str = "",
    flow_runner: Callable[[str, str], dict] | None = None,
    project_name_override: str | None = None,
) -> GenerationResult:
    brief_text = brief_text.strip()
    if not brief_text:
        raise ValueError("Project brief is empty.")

    project_name = (
        _normalize_project_name(project_name_override)
        if project_name_override is not None
        else extract_project_name(brief_text)
    )
    output_dir = next_project_version_outputs_dir(project_name, outputs_root)
    runner = flow_runner or run_v0_flow
    blackboard = runner(brief_text, project_brief_source)
    write_run_artifacts(output_dir, blackboard, brief_text, evaluator_report_text)
    return GenerationResult(
        project_name=project_name,
        project_brief_source=project_brief_source,
        output_dir=output_dir,
        blackboard=blackboard,
    )


def extract_project_name(brief_text: str) -> str:
    for line in brief_text.strip().splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("project name:"):
            value = stripped.split(":", 1)[1].strip()
            return _normalize_project_name(value)
    return "Untitled Project"


def next_project_version_outputs_dir(
    project_name: str, outputs_root: Path | None = None
) -> Path:
    normalized_project_name = _normalize_project_name(project_name)
    outputs_base = _resolve_outputs_root(outputs_root)
    project_tests_dir = outputs_base / "tests" / normalized_project_name
    project_tests_dir.mkdir(parents=True, exist_ok=True)

    version_numbers = []
    for child in project_tests_dir.iterdir():
        if not child.is_dir():
            continue
        match = re.fullmatch(r"version (\d+)", child.name)
        if match:
            version_numbers.append(int(match.group(1)))

    next_version = max(version_numbers, default=0) + 1
    version_dir = project_tests_dir / f"version {next_version}"
    version_dir.mkdir(parents=True, exist_ok=False)
    return version_dir


def _resolve_outputs_root(outputs_root: Path | None) -> Path:
    if outputs_root is None:
        return Path(__file__).resolve().parent.parent / "outputs"
    return outputs_root.resolve()


def _normalize_project_name(project_name: str) -> str:
    normalized = project_name.strip()
    if not normalized:
        return "Untitled Project"
    if "/" in normalized or "\\" in normalized or ".." in normalized:
        raise ValueError(f"Invalid project name: {project_name!r}")
    return normalized
