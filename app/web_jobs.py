from __future__ import annotations

import os
import json
import secrets
from datetime import datetime, timezone
from pathlib import Path

JOB_STATUSES = {"queued", "running", "done", "failed"}
DEFAULT_WEB_JOBS_DIRNAME = "web-jobs"


def create_session_id() -> str:
    return _build_short_id()


def create_job(
    brief_text: str,
    session_id: str,
    jobs_root: Path | None = None,
) -> dict:
    brief_text = brief_text.strip()
    now = _utc_now()
    job = {
        "job_id": _build_short_id(),
        "session_id": session_id.strip(),
        "status": "queued",
        "created_at": now,
        "updated_at": now,
        "brief_text": brief_text,
        "brief_preview": brief_text[:200],
        "project_name": "",
        "output_dir": "",
        "run_project": "",
        "run_version": "",
        "error": "",
    }
    _write_job(job, jobs_root)
    return job


def get_job(job_id: str, jobs_root: Path | None = None) -> dict | None:
    if not _is_safe_job_id(job_id):
        return None
    job_path = _job_path(job_id, jobs_root)
    if not job_path.is_file():
        return None
    with job_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def update_job(job_id: str, updates: dict, jobs_root: Path | None = None) -> dict:
    if not _is_safe_job_id(job_id):
        raise ValueError(f"Invalid job_id: {job_id!r}")

    job = get_job(job_id, jobs_root=jobs_root)
    if job is None:
        raise FileNotFoundError(f"Missing job: {job_id}")

    updated = dict(job)
    if "status" in updates:
        status = updates["status"]
        if status not in JOB_STATUSES:
            raise ValueError(f"Unknown job status: {status!r}")
        updated["status"] = status

    for key, value in updates.items():
        if key == "status":
            continue
        if key == "brief_text":
            value = str(value).strip()
            updated["brief_preview"] = value[:200]
        updated[key] = _coerce_value(value)

    updated["updated_at"] = _utc_now()
    _write_job(updated, jobs_root)
    return updated


def list_jobs(
    session_id: str | None = None,
    jobs_root: Path | None = None,
) -> list[dict]:
    root = _resolve_jobs_root(jobs_root)
    if not root.exists():
        return []

    jobs: list[dict] = []
    for job_path in sorted(root.glob("*.json")):
        with job_path.open("r", encoding="utf-8") as handle:
            job = json.load(handle)
        if session_id is not None and job.get("session_id") != session_id:
            continue
        jobs.append(job)

    return sorted(
        jobs,
        key=lambda job: (
            job.get("created_at", ""),
            job.get("job_id", ""),
        ),
        reverse=True,
    )


def _build_short_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    token = secrets.token_hex(4)
    return f"{timestamp}-{token}"


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve_jobs_root(jobs_root: Path | None = None) -> Path:
    if jobs_root is not None:
        return jobs_root
    configured_jobs_root = os.getenv("WEB_JOBS_ROOT", "").strip()
    if configured_jobs_root:
        return Path(configured_jobs_root)
    configured_outputs_root = os.getenv("WEB_OUTPUTS_ROOT", "").strip()
    if configured_outputs_root:
        return Path(configured_outputs_root) / DEFAULT_WEB_JOBS_DIRNAME
    repo_root = Path(__file__).resolve().parent.parent
    return repo_root / "outputs" / DEFAULT_WEB_JOBS_DIRNAME


def _job_path(job_id: str, jobs_root: Path | None = None) -> Path:
    return _resolve_jobs_root(jobs_root) / f"{job_id}.json"


def _write_job(job: dict, jobs_root: Path | None = None) -> None:
    root = _resolve_jobs_root(jobs_root)
    root.mkdir(parents=True, exist_ok=True)
    job_path = _job_path(job["job_id"], root)
    temp_path = job_path.with_suffix(".json.tmp")
    temp_path.write_text(
        json.dumps(job, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temp_path.replace(job_path)


def _coerce_value(value: object) -> object:
    if isinstance(value, Path):
        return str(value)
    return value


def _is_safe_job_id(job_id: str) -> bool:
    if not job_id:
        return False
    return "/" not in job_id and "\\" not in job_id and ".." not in job_id
