import os
import re
from pathlib import Path

from artifact_writer import write_run_artifacts
from generation_service import run_generation_from_brief
from orchestrator import run_v2_flow


def _load_project_brief() -> tuple[str, str, str]:
    project_brief_path = _select_project_brief_path()
    brief_text = project_brief_path.read_text(encoding="utf-8").strip()
    if not brief_text:
        raise ValueError(f"Project brief file is empty: {project_brief_path}")

    project_name = _extract_project_name(brief_text, project_brief_path)
    return brief_text, project_name, str(project_brief_path.relative_to(_outputs_root()))


def _select_project_brief_path() -> Path:
    outputs_dir = _outputs_root() / "projects"
    if not outputs_dir.exists():
        raise FileNotFoundError(f"Missing projects directory: {outputs_dir}")

    requested_name = os.getenv("BLACKBOARD_PROJECT_NAME", "").strip()
    requested_brief = os.getenv("BLACKBOARD_PROJECT_BRIEF", "").strip()

    if requested_brief:
        brief_path = Path(requested_brief)
        if not brief_path.is_absolute():
            brief_path = _outputs_root() / requested_brief
        if not brief_path.exists():
            raise FileNotFoundError(f"Missing project brief file: {brief_path}")
        return brief_path

    project_files = sorted(outputs_dir.glob("*.md"))
    if not project_files:
        raise FileNotFoundError(f"No project brief files found in: {outputs_dir}")

    if requested_name:
        normalized_requested = _normalize_name(requested_name)
        for candidate in project_files:
            candidate_name = _extract_project_name(
                candidate.read_text(encoding="utf-8"), candidate
            )
            if _normalize_name(candidate_name) == normalized_requested:
                return candidate
            if normalized_requested in _normalize_name(candidate.stem):
                return candidate
        raise FileNotFoundError(
            f"No project brief found for BLACKBOARD_PROJECT_NAME={requested_name!r} in {outputs_dir}"
        )

    if len(project_files) == 1:
        return project_files[0]

    available = ", ".join(path.name for path in project_files)
    raise RuntimeError(
        "Multiple project briefs found in outputs/projects/. "
        "Set BLACKBOARD_PROJECT_NAME or BLACKBOARD_PROJECT_BRIEF. "
        f"Available: {available}"
    )


def _extract_project_name(brief_text: str, brief_path: Path) -> str:
    for line in brief_text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("project name:"):
            value = stripped.split(":", 1)[1].strip()
            if value:
                return value
    stem = brief_path.stem
    if stem.lower().startswith("project-"):
        return stem.split("project-", 1)[1].replace("_", " ").strip()
    return stem.replace("_", " ").strip()


def _normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _outputs_root() -> Path:
    return Path(__file__).resolve().parent.parent / "outputs"


def _load_second_pass_sources() -> tuple[Path, str] | None:
    if os.getenv("BLACKBOARD_WORKFLOW_MODE", "").strip().lower() != "second_pass":
        return None

    outputs_dir = _outputs_root()
    version_dir = outputs_dir / "version 13"
    evaluation_path = outputs_dir / "evaluation-version-13.md"
    if not version_dir.exists() or not evaluation_path.exists():
        return None
    evaluation_text = evaluation_path.read_text(encoding="utf-8").strip()
    if not evaluation_text:
        raise ValueError(f"Evaluation file is empty: {evaluation_path}")
    return version_dir, evaluation_text


def _load_evaluator_report_if_any() -> str:
    evaluator_report = os.getenv("BLACKBOARD_EVALUATOR_REPORT", "").strip()
    if not evaluator_report:
        return ""

    report_path = Path(evaluator_report)
    if not report_path.is_absolute():
        report_path = _outputs_root() / evaluator_report
    if not report_path.exists():
        raise FileNotFoundError(f"Missing evaluator report file: {report_path}")

    report_text = report_path.read_text(encoding="utf-8").strip()
    if not report_text:
        raise ValueError(f"Evaluator report file is empty: {report_path}")
    return report_text


def _read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8").strip()


def main() -> None:
    """Run the flow and write the main output files."""
    second_pass_sources = _load_second_pass_sources()
    if second_pass_sources is not None:
        version_dir, evaluation_text = second_pass_sources
        blackboard = run_v2_flow(version_dir, evaluation_text)
        write_run_artifacts(
            version_dir,
            blackboard,
            _read_text_file(version_dir / "project-brief.md"),
            evaluation_text,
        )
        return

    project_brief, project_name, project_brief_source = _load_project_brief()
    evaluator_report_text = _load_evaluator_report_if_any()
    run_generation_from_brief(
        project_brief,
        project_brief_source=project_brief_source,
        outputs_root=_outputs_root(),
        evaluator_report_text=evaluator_report_text,
        project_name_override=project_name,
    )


if __name__ == "__main__":
    main()
