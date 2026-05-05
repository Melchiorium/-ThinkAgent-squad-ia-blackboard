from __future__ import annotations

import os
import sys
from pathlib import Path
from threading import Lock, Thread

from flask import (
    Flask,
    abort,
    g,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from app.generation_service import run_generation_from_brief
    from app.web_jobs import (
        DEFAULT_WEB_JOBS_DIRNAME,
        create_job,
        create_session_id,
        get_job,
        list_jobs,
        update_job,
    )
    from app.web_runs import EXPECTED_RUN_FILES, get_run, list_runs
else:
    from .generation_service import run_generation_from_brief
    from .web_jobs import (
        DEFAULT_WEB_JOBS_DIRNAME,
        create_job,
        create_session_id,
        get_job,
        list_jobs,
        update_job,
    )
    from .web_runs import EXPECTED_RUN_FILES, get_run, list_runs


app = Flask(__name__)
MAX_BRIEF_CHARACTERS = 50_000
WEB_SESSION_COOKIE_NAME = "web_session_id"

generation_lock = Lock()
generation_runner = run_generation_from_brief
jobs_root: Path | None = None


@app.before_request
def _ensure_session_id() -> None:
    session_id = request.cookies.get(WEB_SESSION_COOKIE_NAME, "").strip()
    if session_id:
        g.web_session_id = session_id
        g.web_session_cookie_is_new = False
        return None

    g.web_session_id = create_session_id()
    g.web_session_cookie_is_new = True
    return None


@app.after_request
def _attach_session_cookie(response):
    if getattr(g, "web_session_cookie_is_new", False):
        response.set_cookie(
            WEB_SESSION_COOKIE_NAME,
            g.web_session_id,
            httponly=True,
            samesite="Lax",
            path="/",
        )
    return response


@app.get("/")
def index():
    runs = [_build_run_view(run) for run in list_runs()]
    session_id = g.web_session_id
    session_jobs = [
        _build_job_view(job) for job in list_jobs(session_id=session_id, jobs_root=_jobs_root())
    ]
    return render_template(
        "index.html",
        runs=runs,
        run_count=len(runs),
        jobs=session_jobs,
        job_count=len(session_jobs),
        max_brief_characters=MAX_BRIEF_CHARACTERS,
    )


@app.post("/jobs")
def create_job_route():
    brief_text = request.form.get("brief", "").strip()
    if not brief_text:
        return "Le brief ne doit pas être vide.", 400
    if len(brief_text) > MAX_BRIEF_CHARACTERS:
        return "Le brief dépasse la limite de 50 000 caractères.", 400

    job = create_job(brief_text, g.web_session_id, jobs_root=_jobs_root())
    Thread(target=_start_generation_job, args=(job["job_id"],), daemon=True).start()
    return redirect(url_for("job_status", job_id=job["job_id"]))


@app.get("/jobs/<job_id>")
def job_status(job_id: str):
    job = get_job(job_id, jobs_root=_jobs_root())
    if job is None:
        abort(404)
    run_url = None
    if job.get("status") == "done" and job.get("run_project") and job.get("run_version"):
        run_url = url_for(
            "run_detail",
            project=job["run_project"],
            version=job["run_version"],
        )
    return render_template(
        "job_status.html",
        job=_build_job_view(job),
        refresh=job.get("status") in {"queued", "running"},
        run_url=run_url,
    )


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


def _jobs_root() -> Path:
    if jobs_root is not None:
        return Path(jobs_root)
    configured_root = os.getenv("WEB_JOBS_ROOT", "").strip()
    if configured_root:
        return Path(configured_root)
    return Path(__file__).resolve().parent.parent / "outputs" / DEFAULT_WEB_JOBS_DIRNAME


def _build_run_view(run: dict) -> dict:
    present_file_count = len(run["files"]) - len(run["missing_files"])
    return {
        "project": run["project"],
        "version": run["version"],
        "present_file_count": present_file_count,
        "total_file_count": len(run["files"]),
        "missing_files": run["missing_files"],
    }


def _build_job_view(job: dict) -> dict:
    view = dict(job)
    view["status_url"] = url_for("job_status", job_id=job["job_id"])
    if job.get("status") == "done" and job.get("run_project") and job.get("run_version"):
        view["run_url"] = url_for(
            "run_detail",
            project=job["run_project"],
            version=job["run_version"],
        )
    else:
        view["run_url"] = None
    return view


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


def _start_generation_job(job_id: str) -> None:
    job = get_job(job_id, jobs_root=_jobs_root())
    if job is None:
        return

    with generation_lock:
        if get_job(job_id, jobs_root=_jobs_root()) is None:
            return

        update_job(job_id, {"status": "running"}, jobs_root=_jobs_root())
        try:
            result = generation_runner(
                job["brief_text"],
                project_brief_source=f"web://job/{job_id}",
            )
            output_dir = Path(result.output_dir)
            update_job(
                job_id,
                {
                    "status": "done",
                    "project_name": result.project_name,
                    "output_dir": str(output_dir),
                    "run_project": output_dir.parent.name,
                    "run_version": output_dir.name,
                    "error": "",
                },
                jobs_root=_jobs_root(),
            )
        except Exception as error:
            update_job(
                job_id,
                {
                    "status": "failed",
                    "error": str(error),
                },
                jobs_root=_jobs_root(),
            )


if __name__ == "__main__":
    app.run(host=_host(), port=_port(), debug=False)
