from __future__ import annotations

import os
import sys
from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory, url_for


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from app.web_runs import EXPECTED_RUN_FILES, get_run, list_runs
else:
    from .web_runs import EXPECTED_RUN_FILES, get_run, list_runs


app = Flask(__name__)


@app.get("/")
def index():
    runs = [_build_run_view(run) for run in list_runs()]
    return render_template("index.html", runs=runs, run_count=len(runs))


@app.get("/runs/<project>/<version>")
def run_detail(project: str, version: str):
    run = get_run(project, version)
    if run is None:
        abort(404)
    run_path = Path(run["path"])
    sections = _build_detail_sections(project, version, run_path)
    return render_template(
        "run_detail.html",
        run=_build_run_view(run),
        sections=sections,
        project=project,
        version=version,
    )


@app.get("/runs/<project>/<version>/artifacts/<filename>")
def run_artifact(project: str, version: str, filename: str):
    run = get_run(project, version)
    if run is None or not _is_allowed_artifact_filename(filename):
        abort(404)

    run_path = Path(run["path"])
    if not (run_path / filename).is_file():
        abort(404)
    return send_from_directory(run_path, filename)


def _host() -> str:
    return os.getenv("WEB_HOST", "127.0.0.1").strip() or "127.0.0.1"


def _port() -> int:
    raw_port = os.getenv("WEB_PORT", "8000").strip() or "8000"
    return int(raw_port)


def _build_run_view(run: dict) -> dict:
    present_file_count = len(run["files"]) - len(run["missing_files"])
    return {
        "project": run["project"],
        "version": run["version"],
        "present_file_count": present_file_count,
        "total_file_count": len(run["files"]),
        "missing_files": run["missing_files"],
    }


def _build_detail_sections(project: str, version: str, run_path: Path) -> list[dict]:
    sections = [
        _build_text_section("Brief", "project-brief.md", run_path),
        _build_text_section("PRD", "prd.md", run_path),
        _build_text_section("Architecture", "architecture.md", run_path),
        _build_mermaid_section(project, version, run_path),
        _build_text_section("GTM", "gtm.md", run_path),
        _build_text_section("Blackboard", "blackboard.md", run_path),
        _build_text_section("Activity Log", "activity_log.txt", run_path),
    ]
    return sections


def _build_text_section(title: str, filename: str, run_path: Path) -> dict:
    content = _read_text_file(run_path / filename)
    return {
        "title": title,
        "filename": filename,
        "content": content,
        "present": content is not None,
        "artifact_url": _artifact_url(run_path, filename) if content is not None else None,
    }


def _build_mermaid_section(project: str, version: str, run_path: Path) -> dict:
    filename = "architecture-diagram.mmd"
    content = _read_text_file(run_path / filename)
    png_filename = "architecture-diagram.png"
    png_present = (run_path / png_filename).is_file()
    return {
        "title": "Diagramme Mermaid",
        "filename": filename,
        "content": content,
        "present": content is not None,
        "png_present": png_present,
        "png_url": _artifact_url(run_path, png_filename) if png_present else None,
        "artifact_url": _artifact_url(run_path, filename) if content is not None else None,
    }


def _read_text_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _artifact_url(run_path: Path, filename: str) -> str:
    project = run_path.parent.name
    version = run_path.name
    return url_for("run_artifact", project=project, version=version, filename=filename)


def _is_allowed_artifact_filename(filename: str) -> bool:
    if not filename or filename not in EXPECTED_RUN_FILES:
        return False
    if "/" in filename or "\\" in filename or ".." in filename:
        return False
    return True


if __name__ == "__main__":
    app.run(host=_host(), port=_port(), debug=False)
