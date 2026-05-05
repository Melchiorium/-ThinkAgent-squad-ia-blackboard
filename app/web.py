from __future__ import annotations

import inspect
import hashlib
import hmac
import os
import sys
from pathlib import Path
from threading import Lock, Thread

from flask import (
    Flask,
    abort,
    g,
    jsonify,
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
WEB_ACCESS_COOKIE_NAME = "web_access_granted"

generation_lock = Lock()
generation_runner = run_generation_from_brief
jobs_root: Path | None = None
EPHEMERAL_OUTPUTS_ROOT = Path("/tmp/squad-ia-blackboard/outputs")


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
    if getattr(g, "web_access_cookie_is_new", False):
        response.set_cookie(
            WEB_ACCESS_COOKIE_NAME,
            _access_cookie_value(_access_token()),
            httponly=True,
            samesite="Lax",
            path="/",
        )
    return response


@app.before_request
def _guard_secret_access():
    token = _access_token()
    if not token or request.endpoint in {"static", "healthz"}:
        return None

    if _has_valid_access_query_token(token):
        g.web_access_cookie_is_new = True
        return None

    if _has_valid_access_cookie(token):
        return None

    return render_template("access_denied.html"), 403


@app.get("/")
def index():
    runs = [_build_run_view(run) for run in list_runs(outputs_root=_outputs_root())]
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


@app.get("/api/jobs/<job_id>")
def job_status_api(job_id: str):
    job = get_job(job_id, jobs_root=_jobs_root())
    if job is None:
        abort(404)
    return jsonify(_build_job_status_payload(job))


@app.post("/jobs")
def create_job_route():
    project_title = request.form.get("project_title", "").strip()
    brief_text = request.form.get("brief", "").strip()
    if not project_title:
        return "Le titre du projet ne doit pas être vide.", 400
    if len(project_title) > 120:
        return "Le titre du projet dépasse la limite de 120 caractères.", 400
    if _has_invalid_project_title_characters(project_title):
        return "Le titre du projet contient des caractères interdits.", 400
    if not brief_text:
        return "Le brief ne doit pas être vide.", 400
    if len(brief_text) > MAX_BRIEF_CHARACTERS:
        return "Le brief dépasse la limite de 50 000 caractères.", 400

    job = create_job(
        brief_text,
        g.web_session_id,
        project_title=project_title,
        jobs_root=_jobs_root(),
    )
    Thread(target=_start_generation_job, args=(job["job_id"],), daemon=True).start()
    return redirect(url_for("job_status", job_id=job["job_id"]))


@app.get("/jobs/<job_id>")
def job_status(job_id: str):
    job = get_job(job_id, jobs_root=_jobs_root())
    if job is None:
        abort(404)
    run_url = None
    sections = None
    if job.get("status") == "done" and job.get("run_project") and job.get("run_version"):
        run_url = url_for(
            "run_detail",
            project=job["run_project"],
            version=job["run_version"],
        )
        run = get_run(job["run_project"], job["run_version"], outputs_root=_outputs_root())
        if run is not None:
            sections = _build_job_result_sections(Path(run["path"]))
    return render_template(
        "job_status.html",
        job=_build_job_view(job),
        sections=sections,
        run_url=run_url,
    )


@app.get("/runs/<project>/<version>")
def run_detail(project: str, version: str):
    run = get_run(project, version, outputs_root=_outputs_root())
    if run is None:
        abort(404)
    run_path = Path(run["path"])
    sections = _build_run_detail_sections(run_path)
    return render_template(
        "run_detail.html",
        run=_build_run_view(run),
        sections=sections,
        project=project,
        version=version,
    )


@app.get("/runs/<project>/<version>/artifacts/<filename>")
def run_artifact(project: str, version: str, filename: str):
    run = get_run(project, version, outputs_root=_outputs_root())
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
    outputs_root = _outputs_root()
    if outputs_root.name == "outputs":
        return outputs_root / DEFAULT_WEB_JOBS_DIRNAME
    return outputs_root / DEFAULT_WEB_JOBS_DIRNAME


def _outputs_root() -> Path:
    configured_root = os.getenv("WEB_OUTPUTS_ROOT", "").strip()
    if configured_root:
        return Path(configured_root)
    repo_outputs_root = Path(__file__).resolve().parent.parent / "outputs"
    if _is_writable_directory(repo_outputs_root):
        return repo_outputs_root
    return EPHEMERAL_OUTPUTS_ROOT


def _is_writable_directory(path: Path) -> bool:
    try:
        path.mkdir(parents=True, exist_ok=True)
        probe_path = path / ".web-write-check"
        probe_path.write_text("ok", encoding="utf-8")
        probe_path.unlink(missing_ok=True)
    except OSError:
        return False
    return True


def _access_token() -> str:
    return os.getenv("WEB_ACCESS_TOKEN", "").strip()


def _access_cookie_value(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def _has_valid_access_cookie(token: str) -> bool:
    cookie_value = request.cookies.get(WEB_ACCESS_COOKIE_NAME, "").strip()
    if not cookie_value:
        return False
    expected_value = _access_cookie_value(token)
    return hmac.compare_digest(cookie_value, expected_value)


def _has_valid_access_query_token(token: str) -> bool:
    query_token = request.args.get("access_token", "").strip()
    if not query_token:
        return False
    return hmac.compare_digest(query_token, token)


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
    view["display_title"] = _job_display_title(job)
    view["status_label"] = _status_label(job.get("status", ""))
    view["status_url"] = url_for("job_status", job_id=job["job_id"])
    view["status_api_url"] = url_for("job_status_api", job_id=job["job_id"])
    if job.get("status") == "done" and job.get("run_project") and job.get("run_version"):
        view["run_url"] = url_for(
            "run_detail",
            project=job["run_project"],
            version=job["run_version"],
        )
    else:
        view["run_url"] = None
    return view


def _status_label(status: str) -> str:
    labels = {
        "queued": "En attente",
        "running": "En cours",
        "done": "Terminé",
        "failed": "Échec",
    }
    return labels.get(status, status)


def _build_job_status_payload(job: dict) -> dict:
    run_url = None
    if job.get("status") == "done" and job.get("run_project") and job.get("run_version"):
        run_url = url_for(
            "run_detail",
            project=job["run_project"],
            version=job["run_version"],
        )
    return {
        "job_id": job["job_id"],
        "status": job["status"],
        "created_at": job["created_at"],
        "updated_at": job["updated_at"],
        "brief_preview": job.get("brief_preview", ""),
        "project_title": job.get("project_title", ""),
        "display_title": _job_display_title(job),
        "error": job.get("error", ""),
        "run_url": run_url,
    }


def _build_run_detail_sections(run_path: Path) -> list[dict]:
    return _build_sections(
        run_path,
        order=[
            "Brief",
            "PRD",
            "Architecture",
            "Diagramme Mermaid",
            "GTM",
            "Blackboard",
            "Activity Log",
        ],
    )


def _build_job_result_sections(run_path: Path) -> list[dict]:
    return _build_sections(
        run_path,
        order=[
            "PRD",
            "Architecture",
            "Diagramme Mermaid",
            "GTM",
            "Brief",
            "Blackboard",
            "Activity Log",
        ],
    )


def _build_sections(run_path: Path, order: list[str]) -> list[dict]:
    all_sections = {
        "Brief": _build_text_section("Brief", "project-brief.md", run_path),
        "PRD": _build_text_section("PRD", "prd.md", run_path),
        "Architecture": _build_text_section("Architecture", "architecture.md", run_path),
        "Diagramme Mermaid": _build_mermaid_section(run_path),
        "GTM": _build_text_section("GTM", "gtm.md", run_path),
        "Blackboard": _build_text_section("Blackboard", "blackboard.md", run_path),
        "Activity Log": _build_text_section("Activity Log", "activity_log.txt", run_path),
    }
    return [all_sections[title] for title in order]


def _build_text_section(title: str, filename: str, run_path: Path) -> dict:
    content = _read_text_file(run_path / filename)
    return {
        "title": title,
        "filename": filename,
        "content": content,
        "present": content is not None,
        "artifact_url": _artifact_url(run_path, filename) if content is not None else None,
    }


def _build_mermaid_section(run_path: Path) -> dict:
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


def _job_display_title(job: dict) -> str:
    project_title = str(job.get("project_title", "")).strip()
    if project_title:
        return project_title
    project_name = str(job.get("project_name", "")).strip()
    if project_name:
        return project_name
    return "Génération"


def _has_invalid_project_title_characters(project_title: str) -> bool:
    if "/" in project_title or "\\" in project_title or ".." in project_title:
        return True
    return any(ord(character) < 32 or ord(character) == 127 for character in project_title)


@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok"})


def _start_generation_job(job_id: str) -> None:
    job = get_job(job_id, jobs_root=_jobs_root())
    if job is None:
        return
    effective_brief = _build_effective_brief(job)
    project_title = str(job.get("project_title", "")).strip()

    with generation_lock:
        if get_job(job_id, jobs_root=_jobs_root()) is None:
            return

        update_job(job_id, {"status": "running"}, jobs_root=_jobs_root())
        try:
            result = _run_generation_runner(
                effective_brief,
                job_id,
                project_name_override=project_title or None,
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


def _build_effective_brief(job: dict) -> str:
    project_title = str(job.get("project_title", "")).strip()
    brief_text = str(job.get("brief_text", "")).strip()
    if project_title:
        return f"Project name: {project_title}\n\n{brief_text}"
    return brief_text


def _run_generation_runner(
    brief_text: str,
    job_id: str,
    project_name_override: str | None = None,
):
    runner = generation_runner
    kwargs = {"project_brief_source": f"web://job/{job_id}"}
    try:
        signature = inspect.signature(runner)
    except (TypeError, ValueError):
        signature = None

    if signature is None:
        if project_name_override is not None:
            kwargs["project_name_override"] = project_name_override
        return runner(brief_text, **kwargs)

    if "outputs_root" in signature.parameters or any(
        parameter.kind == inspect.Parameter.VAR_KEYWORD
        for parameter in signature.parameters.values()
    ):
        kwargs["outputs_root"] = _outputs_root()
    if project_name_override is not None and (
        "project_name_override" in signature.parameters
        or any(
            parameter.kind == inspect.Parameter.VAR_KEYWORD
            for parameter in signature.parameters.values()
        )
    ):
        kwargs["project_name_override"] = project_name_override
    return runner(brief_text, **kwargs)


if __name__ == "__main__":
    app.run(host=_host(), port=_port(), debug=False)
