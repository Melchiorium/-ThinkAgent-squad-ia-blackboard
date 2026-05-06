from __future__ import annotations

import inspect
import hashlib
import hmac
import os
import re
import sys
from io import BytesIO
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
    send_file,
    url_for,
)


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from app.generation_service import run_generation_from_brief
    from app.web_presenters import (
        build_job_status_payload,
        build_job_view,
        build_rendered_sections,
        build_run_view,
    )
    from app.web_jobs import (
        DEFAULT_WEB_JOBS_DIRNAME,
        create_job,
        create_session_id,
        delete_jobs_for_run,
        get_job,
        list_jobs,
        update_job,
    )
    from app.web_runs import get_run, list_runs
    from app.web_storage import (
        WebStorageConfigurationError,
        WebStorageConnectionError,
        WebStorageDependencyError,
        WebStorageSchemaError,
        delete_run,
        check_storage_readiness,
        is_allowed_run_artifact_filename,
        load_run_sections,
        prepare_generation_workspace,
        persist_run_artifacts,
        read_run_artifact,
        resolve_web_storage_backend,
    )
    from app.web_progress import (
        DEFAULT_PROGRESS_TIMEOUT_SECONDS,
        apply_progress_update,
        normalize_progress_state,
    )
else:
    from .generation_service import run_generation_from_brief
    from .web_presenters import (
        build_job_status_payload,
        build_job_view,
        build_rendered_sections,
        build_run_view,
    )
    from .web_jobs import (
        DEFAULT_WEB_JOBS_DIRNAME,
        create_job,
        create_session_id,
        delete_jobs_for_run,
        get_job,
        list_jobs,
        update_job,
    )
    from .web_runs import get_run, list_runs
    from .web_storage import (
        WebStorageConfigurationError,
        WebStorageConnectionError,
        WebStorageDependencyError,
        WebStorageSchemaError,
        delete_run,
        check_storage_readiness,
        is_allowed_run_artifact_filename,
        load_run_sections,
        prepare_generation_workspace,
        persist_run_artifacts,
        read_run_artifact,
        resolve_web_storage_backend,
    )
    from .web_progress import (
        DEFAULT_PROGRESS_TIMEOUT_SECONDS,
        apply_progress_update,
        normalize_progress_state,
    )


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
    deletion_notice = bool(request.args.get("deleted", "").strip())
    session_id = g.web_session_id
    session_jobs = []
    for job in list_jobs(
        session_id=session_id,
        jobs_root=_jobs_root(),
        backend=_storage_backend(),
    ):
        run_url = _job_run_url(job)
        if _is_stale_done_job(job, run_url):
            continue
        session_jobs.append(
            build_job_view(
                job,
                status_url=url_for("job_status", job_id=job["job_id"]),
                status_api_url=url_for("job_status_api", job_id=job["job_id"]),
                run_url=run_url,
            )
        )
    return render_template(
        "index.html",
        jobs=session_jobs,
        job_count=len(session_jobs),
        max_brief_characters=MAX_BRIEF_CHARACTERS,
        deletion_notice=deletion_notice,
    )


@app.get("/api/jobs/<job_id>")
def job_status_api(job_id: str):
    job = get_job(job_id, jobs_root=_jobs_root(), backend=_storage_backend())
    if job is None:
        abort(404)
    return jsonify(build_job_status_payload(job, run_url=_job_run_url(job)))


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
        backend=_storage_backend(),
    )
    _update_job_progress(
        job["job_id"],
        stage="brief_received",
        label="Brief reçu",
        detail="Le brief a été soumis et peut être traité.",
        done_blocks=["brief_received"],
        set_started=False,
    )
    Thread(target=_start_generation_job, args=(job["job_id"],), daemon=True).start()
    return redirect(url_for("job_status", job_id=job["job_id"]))


@app.get("/jobs/<job_id>")
def job_status(job_id: str):
    job = get_job(job_id, jobs_root=_jobs_root(), backend=_storage_backend())
    if job is None:
        abort(404)
    run_url = _job_run_url(job)
    sections = None
    if run_url:
        run_sections = load_run_sections(
            job["run_project"],
            job["run_version"],
            outputs_root=_outputs_root(),
            backend=_storage_backend(),
        )
        sections = build_rendered_sections(
            run_sections,
            artifact_url_builder=lambda filename: url_for(
                "run_artifact",
                project=job["run_project"],
                version=job["run_version"],
                filename=filename,
            ),
        )
    return render_template(
        "job_status.html",
        job=build_job_view(
            job,
            status_url=url_for("job_status", job_id=job["job_id"]),
            status_api_url=url_for("job_status_api", job_id=job["job_id"]),
            run_url=run_url,
        ),
        sections=sections,
        run_url=run_url,
    )


@app.get("/runs/<project>/<version>")
def run_detail(project: str, version: str):
    run = get_run(
        project,
        version,
        outputs_root=_outputs_root(),
        backend=_storage_backend(),
    )
    if run is None:
        abort(404)
    sections = build_rendered_sections(
        load_run_sections(
            project,
            version,
            outputs_root=_outputs_root(),
            backend=_storage_backend(),
        ),
        artifact_url_builder=lambda filename: url_for(
            "run_artifact",
            project=project,
            version=version,
            filename=filename,
        ),
    )
    if sections is None:
        abort(404)
    return render_template(
        "run_detail.html",
        run=build_run_view(run),
        sections=sections,
        project=project,
        version=version,
    )


@app.get("/runs/<project>/<version>/artifacts/<filename>")
def run_artifact(project: str, version: str, filename: str):
    if not is_allowed_run_artifact_filename(filename):
        abort(404)
    run = get_run(
        project,
        version,
        outputs_root=_outputs_root(),
        backend=_storage_backend(),
    )
    if run is None:
        abort(404)
    payload = read_run_artifact(
        project,
        version,
        filename,
        outputs_root=_outputs_root(),
        backend=_storage_backend(),
    )
    if payload is None:
        abort(404)
    return send_file(
        BytesIO(payload["content"]),
        mimetype=payload["content_type"],
        download_name=filename,
    )


@app.post("/runs/<project>/<version>/delete")
def delete_run_route(project: str, version: str):
    run = get_run(
        project,
        version,
        outputs_root=_outputs_root(),
        backend=_storage_backend(),
    )
    if run is None:
        abort(404)

    try:
        deleted = delete_run(
            project,
            version,
            outputs_root=_outputs_root(),
            backend=_storage_backend(),
        )
    except ValueError:
        abort(404)
    except Exception:
        return "Suppression du run impossible.", 500

    if not deleted:
        abort(404)

    try:
        delete_jobs_for_run(
            project,
            version,
            jobs_root=_jobs_root(),
            backend=_storage_backend(),
        )
    except Exception:
        return "Run supprimé, mais nettoyage de l'historique impossible.", 500

    return redirect(url_for("index", deleted="1"))


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
    if _storage_backend() == "supabase":
        return EPHEMERAL_OUTPUTS_ROOT
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


def _has_invalid_project_title_characters(project_title: str) -> bool:
    if "/" in project_title or "\\" in project_title or ".." in project_title:
        return True
    return any(ord(character) < 32 or ord(character) == 127 for character in project_title)


def _storage_backend() -> str:
    return resolve_web_storage_backend()


def _job_run_url(job: dict) -> str | None:
    if job.get("status") != "done":
        return None
    project = str(job.get("run_project", "")).strip()
    version = str(job.get("run_version", "")).strip()
    if not project or not version:
        return None
    run = get_run(
        project,
        version,
        outputs_root=_outputs_root(),
        backend=_storage_backend(),
    )
    if run is None:
        return None
    return url_for("run_detail", project=project, version=version)


def _is_stale_done_job(job: dict, run_url: str | None) -> bool:
    if job.get("status") != "done":
        return False
    has_run_reference = bool(
        str(job.get("run_project", "")).strip()
        and str(job.get("run_version", "")).strip()
    )
    return has_run_reference and run_url is None


def _web_agent_step_timeout_seconds() -> int:
    raw_value = os.getenv("WEB_AGENT_STEP_TIMEOUT_SECONDS", "").strip()
    if not raw_value:
        return DEFAULT_PROGRESS_TIMEOUT_SECONDS
    try:
        timeout = int(raw_value)
    except ValueError:
        return DEFAULT_PROGRESS_TIMEOUT_SECONDS
    return timeout if timeout > 0 else DEFAULT_PROGRESS_TIMEOUT_SECONDS


def _build_job_progress_callback(job_id: str, backend: str):
    def _callback(
        *,
        stage: str,
        label: str,
        detail: str = "",
        active_blocks: list[str] | None = None,
        done_blocks: list[str] | None = None,
        skipped_blocks: list[str] | None = None,
        failed_blocks: list[str] | None = None,
    ) -> None:
        current_job = get_job(job_id, jobs_root=_jobs_root(), backend=backend)
        if current_job is None:
            return
        if current_job.get("status") not in {"queued", "running"}:
            return
        updates = _update_job_progress_payload(
            current_job,
            stage=stage,
            label=label,
            detail=detail,
            active_blocks=active_blocks or [],
            done_blocks=done_blocks or [],
            skipped_blocks=skipped_blocks or [],
            failed_blocks=failed_blocks or [],
            set_started=current_job.get("status") == "running"
            and not current_job.get("progress_started_at"),
        )
        update_job(job_id, updates, jobs_root=_jobs_root(), backend=backend)

    return _callback


def _update_job_progress(
    job_id: str,
    *,
    stage: str,
    label: str,
    detail: str = "",
    active_blocks: list[str] | None = None,
    done_blocks: list[str] | None = None,
    skipped_blocks: list[str] | None = None,
    failed_blocks: list[str] | None = None,
    set_started: bool = False,
) -> dict | None:
    backend = _storage_backend()
    current_job = get_job(job_id, jobs_root=_jobs_root(), backend=backend)
    if current_job is None:
        return None
    updates = _update_job_progress_payload(
        current_job,
        stage=stage,
        label=label,
        detail=detail,
        active_blocks=active_blocks or [],
        done_blocks=done_blocks or [],
        skipped_blocks=skipped_blocks or [],
        failed_blocks=failed_blocks or [],
        set_started=set_started,
    )
    return update_job(job_id, updates, jobs_root=_jobs_root(), backend=backend)


def _update_job_progress_payload(
    job: dict,
    *,
    stage: str,
    label: str,
    detail: str = "",
    active_blocks: list[str] | None = None,
    done_blocks: list[str] | None = None,
    skipped_blocks: list[str] | None = None,
    failed_blocks: list[str] | None = None,
    set_started: bool = False,
    error_type: str = "",
    error_message: str = "",
) -> dict:
    timeout_seconds = _web_agent_step_timeout_seconds()
    return apply_progress_update(
        job,
        stage=stage,
        label=label,
        detail=detail,
        active_blocks=active_blocks or [],
        done_blocks=done_blocks or [],
        skipped_blocks=skipped_blocks or [],
        failed_blocks=failed_blocks or [],
        set_started=set_started,
        timeout_seconds=timeout_seconds,
        error_type=error_type,
        error_message=error_message,
    )


def _mark_generation_job_failed(job_id: str, error: Exception, *, backend: str) -> None:
    current_job = get_job(job_id, jobs_root=_jobs_root(), backend=backend)
    if current_job is None:
        return

    normalized_progress = normalize_progress_state(current_job)
    active_blocks = [
        block.get("id", "")
        for block in normalized_progress.get("progress_blocks", [])
        if block.get("status") == "active"
    ]
    error_type, error_message = _classify_progress_error(error)
    if not error_message:
        error_message = "Une erreur est survenue pendant la génération."
    updates = _update_job_progress_payload(
        current_job,
        stage=normalized_progress.get("progress_stage", "") or "failed",
        label=normalized_progress.get("progress_label", "") or "Génération interrompue",
        detail=error_message,
        active_blocks=[],
        done_blocks=[],
        skipped_blocks=[],
        failed_blocks=active_blocks,
        error_type=error_type,
        error_message=error_message,
    )
    updates["status"] = "failed"
    updates["error"] = error_message
    update_job(job_id, updates, jobs_root=_jobs_root(), backend=backend)


def _classify_progress_error(error: Exception) -> tuple[str, str]:
    message = _sanitize_progress_error_message(str(error))
    lowered = message.lower()
    if isinstance(error, TimeoutError) or "timed out" in lowered or "dépassé" in lowered:
        return "timeout", message
    if "llm request failed" in lowered or "model" in lowered and "not found" in lowered:
        return "llm", message
    if any(keyword in lowered for keyword in ("cannot reach", "connection", "network", "dns", "http")):
        return "network", message
    if any(keyword in lowered for keyword in ("supabase", "storage", "database")):
        return "storage", message
    return "unknown", message


def _sanitize_progress_error_message(message: str) -> str:
    sanitized = re.sub(r"(access_token=)[^&\s]+", r"\1***", message)
    sanitized = re.sub(
        r"(postgres(?:ql)?://)([^:@\s]+):([^@\s]+)@",
        r"\1***:***@",
        sanitized,
        flags=re.IGNORECASE,
    )
    sanitized = re.sub(r"(https?://)[^\s]+", r"\1…", sanitized)
    sanitized = " ".join(sanitized.split())
    if len(sanitized) > 220:
        sanitized = sanitized[:217].rstrip() + "..."
    return sanitized


def _readyz_error_payload(error_type: str, message: str, backend: str) -> dict:
    return {
        "status": "error",
        "backend": backend,
        "error_type": error_type,
        "message": message,
    }


@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok"})


@app.get("/readyz")
def readyz():
    try:
        backend = _storage_backend()
        readiness = check_storage_readiness(backend)
    except ValueError as error:
        return (
            jsonify(
                {
                    "status": "error",
                    "backend": "unknown",
                    "error_type": "invalid_backend",
                    "message": str(error),
                }
            ),
            503,
        )
    except WebStorageDependencyError as error:
        return jsonify(_readyz_error_payload("dependency_error", str(error), backend)), 503
    except WebStorageConfigurationError as error:
        return jsonify(_readyz_error_payload("configuration_error", str(error), backend)), 503
    except WebStorageConnectionError as error:
        return jsonify(_readyz_error_payload("connection_error", str(error), backend)), 503
    except WebStorageSchemaError as error:
        return jsonify(_readyz_error_payload("schema_error", str(error), backend)), 503

    return jsonify(readiness)


def _start_generation_job(job_id: str) -> None:
    backend = _storage_backend()
    job = get_job(job_id, jobs_root=_jobs_root(), backend=backend)
    if job is None:
        return
    effective_brief = _build_effective_brief(job)
    project_title = str(job.get("project_title", "")).strip()

    with generation_lock:
        if get_job(job_id, jobs_root=_jobs_root(), backend=backend) is None:
            return

        update_job(job_id, {"status": "running"}, jobs_root=_jobs_root(), backend=backend)
        _update_job_progress(
            job_id,
            stage="product_initial",
            label="Product structure le PRD initial",
            detail="Analyse du brief, problème cible, utilisateurs et objectifs MVP.",
            active_blocks=[
                "product_brief_analysis",
                "product_problem",
                "product_users_goals",
                "product_user_stories",
            ],
            done_blocks=["brief_received"],
            set_started=True,
        )
        try:
            prepare_generation_workspace(
                project_title,
                _outputs_root(),
                backend=backend,
            )
            result = _run_generation_runner(
                effective_brief,
                job_id,
                project_name_override=project_title or None,
                progress_callback=_build_job_progress_callback(job_id, backend),
                step_timeout_seconds=_web_agent_step_timeout_seconds(),
            )
            output_dir = Path(result.output_dir)
            _update_job_progress(
                job_id,
                stage="artifacts_persistence",
                label="Persistance des artefacts",
                detail="Les artefacts du run sont en cours de persistance.",
                active_blocks=["artifacts_persistence"],
            )
            persist_run_artifacts(output_dir, backend=backend)
            _update_job_progress(
                job_id,
                stage="done",
                label="Génération terminée",
                detail="Les artefacts ont été persistés avec succès.",
                done_blocks=["artifacts_persistence", "done"],
            )
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
                backend=backend,
            )
        except Exception as error:
            _mark_generation_job_failed(
                job_id,
                error,
                backend=backend,
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
    progress_callback=None,
    step_timeout_seconds: int | None = None,
):
    runner = generation_runner
    kwargs = {
        "project_brief_source": f"web://job/{job_id}",
        "progress_callback": progress_callback,
        "step_timeout_seconds": step_timeout_seconds,
    }
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
    accepts_var_kwargs = any(
        parameter.kind == inspect.Parameter.VAR_KEYWORD
        for parameter in signature.parameters.values()
    )
    if not accepts_var_kwargs:
        if "progress_callback" not in signature.parameters:
            kwargs.pop("progress_callback", None)
        if "step_timeout_seconds" not in signature.parameters:
            kwargs.pop("step_timeout_seconds", None)
    return runner(brief_text, **kwargs)


if __name__ == "__main__":
    app.run(host=_host(), port=_port(), debug=False)
