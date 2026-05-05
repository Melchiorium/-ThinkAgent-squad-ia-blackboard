from __future__ import annotations

import json
import os
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


JOB_STATUSES = {"queued", "running", "done", "failed"}
DEFAULT_WEB_JOBS_DIRNAME = "web-jobs"
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
_RUN_DETAIL_SECTION_ORDER = [
    "Brief",
    "PRD",
    "Architecture",
    "Diagramme Mermaid",
    "GTM",
    "Blackboard",
    "Activity Log",
]
_JOB_SECTION_ORDER = [
    "PRD",
    "Architecture",
    "Diagramme Mermaid",
    "GTM",
    "Brief",
    "Blackboard",
    "Activity Log",
]
_VERSION_PATTERN = re.compile(r"^version (\d+)$")
_TEXT_ARTIFACT_CONTENT_TYPES = {
    "project-brief.md": "text/markdown; charset=utf-8",
    "prd.md": "text/markdown; charset=utf-8",
    "architecture.md": "text/markdown; charset=utf-8",
    "architecture-diagram.mmd": "text/plain; charset=utf-8",
    "gtm.md": "text/markdown; charset=utf-8",
    "blackboard.md": "text/markdown; charset=utf-8",
    "activity_log.txt": "text/plain; charset=utf-8",
}
_BINARY_ARTIFACT_CONTENT_TYPES = {
    "architecture-diagram.png": "image/png",
}


def create_session_id() -> str:
    return _build_short_id()


def resolve_web_storage_backend(backend: str | None = None) -> str:
    raw_backend = backend
    if raw_backend is None:
        raw_backend = os.getenv("WEB_STORAGE_BACKEND", "")
    normalized_backend = raw_backend.strip().lower()
    if not normalized_backend:
        return "file"
    if normalized_backend not in {"file", "supabase"}:
        raise ValueError(
            "WEB_STORAGE_BACKEND must be 'file' or 'supabase'."
        )
    return normalized_backend


def create_job(
    brief_text: str,
    session_id: str,
    project_title: str = "",
    jobs_root: Path | None = None,
    backend: str | None = None,
) -> dict:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_create_job(brief_text, session_id, project_title)
    return _file_create_job(brief_text, session_id, project_title, jobs_root)


def get_job(
    job_id: str,
    jobs_root: Path | None = None,
    backend: str | None = None,
) -> dict | None:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_get_job(job_id)
    return _file_get_job(job_id, jobs_root)


def update_job(
    job_id: str,
    updates: dict,
    jobs_root: Path | None = None,
    backend: str | None = None,
) -> dict:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_update_job(job_id, updates)
    return _file_update_job(job_id, updates, jobs_root)


def list_jobs(
    session_id: str | None = None,
    jobs_root: Path | None = None,
    backend: str | None = None,
) -> list[dict]:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_list_jobs(session_id)
    return _file_list_jobs(session_id, jobs_root)


def list_runs(
    outputs_root: Path | None = None,
    backend: str | None = None,
) -> list[dict]:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_list_runs()
    return _file_list_runs(outputs_root)


def get_run(
    project: str,
    version: str,
    outputs_root: Path | None = None,
    backend: str | None = None,
) -> dict | None:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_get_run(project, version)
    return _file_get_run(project, version, outputs_root)


def load_run_sections(
    project: str,
    version: str,
    outputs_root: Path | None = None,
    backend: str | None = None,
) -> list[dict] | None:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_load_run_sections(project, version)
    return _file_load_run_sections(project, version, outputs_root)


def read_run_artifact(
    project: str,
    version: str,
    filename: str,
    outputs_root: Path | None = None,
    backend: str | None = None,
) -> dict | None:
    if not is_allowed_run_artifact_filename(filename):
        return None
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend == "supabase":
        return _supabase_read_run_artifact(project, version, filename)
    return _file_read_run_artifact(project, version, filename, outputs_root)


def persist_run_artifacts(
    output_dir: Path,
    backend: str | None = None,
) -> None:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend != "supabase":
        return
    _supabase_persist_run_artifacts(output_dir)


def prepare_generation_workspace(
    project_name: str,
    outputs_root: Path,
    backend: str | None = None,
) -> None:
    storage_backend = resolve_web_storage_backend(backend)
    if storage_backend != "supabase":
        return

    project_name = project_name.strip()
    if not project_name:
        return

    project_dir = _resolve_tests_root(outputs_root) / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    for run in _supabase_list_runs():
        if run["project"] != project_name:
            continue
        (project_dir / run["version"]).mkdir(parents=True, exist_ok=True)


def is_allowed_run_artifact_filename(filename: str) -> bool:
    if not filename or filename not in EXPECTED_RUN_FILES:
        return False
    if "/" in filename or "\\" in filename or ".." in filename:
        return False
    return True


def _file_create_job(
    brief_text: str,
    session_id: str,
    project_title: str,
    jobs_root: Path | None,
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
        "project_title": project_title.strip(),
        "project_name": "",
        "output_dir": "",
        "run_project": "",
        "run_version": "",
        "error": "",
    }
    _file_write_job(job, jobs_root)
    return job


def _file_get_job(job_id: str, jobs_root: Path | None = None) -> dict | None:
    if not _is_safe_job_id(job_id):
        return None
    job_path = _file_job_path(job_id, jobs_root)
    if not job_path.is_file():
        return None
    with job_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _file_update_job(
    job_id: str,
    updates: dict,
    jobs_root: Path | None = None,
) -> dict:
    if not _is_safe_job_id(job_id):
        raise ValueError(f"Invalid job_id: {job_id!r}")

    job = _file_get_job(job_id, jobs_root=jobs_root)
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
    _file_write_job(updated, jobs_root)
    return updated


def _file_list_jobs(
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


def _file_list_runs(outputs_root: Path | None = None) -> list[dict]:
    tests_root = _resolve_tests_root(outputs_root)
    if not tests_root.exists():
        return []

    runs: list[dict] = []
    for project_dir in sorted(
        (path for path in tests_root.iterdir() if path.is_dir()),
        key=lambda path: path.name.lower(),
    ):
        runs.extend(_file_collect_project_runs(project_dir))

    return sorted(
        runs,
        key=lambda run: (run["project"].lower(), run["version_number"]),
    )


def _file_get_run(
    project: str,
    version: str,
    outputs_root: Path | None = None,
) -> dict | None:
    for run in _file_list_runs(outputs_root):
        if run["project"] == project and run["version"] == version:
            return run
    return None


def _file_load_run_sections(
    project: str,
    version: str,
    outputs_root: Path | None = None,
) -> list[dict] | None:
    run_path = _file_run_path(project, version, outputs_root)
    if not run_path.is_dir():
        return None
    return _build_sections_from_run_path(run_path)


def _file_read_run_artifact(
    project: str,
    version: str,
    filename: str,
    outputs_root: Path | None = None,
) -> dict | None:
    run_path = _file_run_path(project, version, outputs_root)
    artifact_path = run_path / filename
    if not artifact_path.is_file():
        return None
    return {
        "content": artifact_path.read_bytes(),
        "content_type": _artifact_content_type(filename),
    }


def _file_collect_project_runs(project_dir: Path) -> list[dict]:
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


def _supabase_create_job(
    brief_text: str,
    session_id: str,
    project_title: str,
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
        "project_title": project_title.strip(),
        "project_name": "",
        "output_dir": "",
        "run_project": "",
        "run_version": "",
        "error": "",
    }
    _supabase_execute(
        """
        insert into web_jobs (
          job_id,
          session_id,
          status,
          created_at,
          updated_at,
          brief_text,
          brief_preview,
          project_title,
          project_name,
          output_dir,
          run_project,
          run_version,
          error
        ) values (
          %(job_id)s,
          %(session_id)s,
          %(status)s,
          %(created_at)s,
          %(updated_at)s,
          %(brief_text)s,
          %(brief_preview)s,
          %(project_title)s,
          %(project_name)s,
          %(output_dir)s,
          %(run_project)s,
          %(run_version)s,
          %(error)s
        )
        """,
        job,
    )
    return job


def _supabase_get_job(job_id: str) -> dict | None:
    if not _is_safe_job_id(job_id):
        return None
    rows = _supabase_fetch_all(
        """
        select
          job_id,
          session_id,
          status,
          created_at,
          updated_at,
          brief_text,
          brief_preview,
          project_title,
          project_name,
          output_dir,
          run_project,
          run_version,
          error
        from web_jobs
        where job_id = %s
        """,
        (job_id,),
    )
    if not rows:
        return None
    return _normalize_supabase_job_row(rows[0])


def _supabase_update_job(job_id: str, updates: dict) -> dict:
    if not _is_safe_job_id(job_id):
        raise ValueError(f"Invalid job_id: {job_id!r}")

    current = _supabase_get_job(job_id)
    if current is None:
        raise FileNotFoundError(f"Missing job: {job_id}")

    updated = dict(current)
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
    _supabase_execute(
        """
        update web_jobs
        set
          session_id = %(session_id)s,
          status = %(status)s,
          created_at = %(created_at)s,
          updated_at = %(updated_at)s,
          brief_text = %(brief_text)s,
          brief_preview = %(brief_preview)s,
          project_title = %(project_title)s,
          project_name = %(project_name)s,
          output_dir = %(output_dir)s,
          run_project = %(run_project)s,
          run_version = %(run_version)s,
          error = %(error)s
        where job_id = %(job_id)s
        """,
        updated,
    )
    return updated


def _supabase_list_jobs(session_id: str | None = None) -> list[dict]:
    if session_id is None:
        rows = _supabase_fetch_all(
            """
            select
              job_id,
              session_id,
              status,
              created_at,
              updated_at,
              brief_text,
              brief_preview,
              project_title,
              project_name,
              output_dir,
              run_project,
              run_version,
              error
            from web_jobs
            order by created_at desc, job_id desc
            """
        )
    else:
        rows = _supabase_fetch_all(
            """
            select
              job_id,
              session_id,
              status,
              created_at,
              updated_at,
              brief_text,
              brief_preview,
              project_title,
              project_name,
              output_dir,
              run_project,
              run_version,
              error
            from web_jobs
            where session_id = %s
            order by created_at desc, job_id desc
            """,
            (session_id,),
        )
    return [_normalize_supabase_job_row(row) for row in rows]


def _supabase_list_runs() -> list[dict]:
    rows = _supabase_fetch_all(
        """
        select
          run_project,
          run_version,
          version_number,
          filename
        from web_run_artifacts
        order by lower(run_project), version_number, filename
        """
    )
    grouped: dict[tuple[str, str, int], set[str]] = {}
    for row in rows:
        key = (
            str(row["run_project"]),
            str(row["run_version"]),
            int(row["version_number"]),
        )
        grouped.setdefault(key, set()).add(str(row["filename"]))

    runs: list[dict] = []
    for (project, version, version_number), filenames in grouped.items():
        files = {filename: filename in filenames for filename in EXPECTED_RUN_FILES}
        runs.append(
            {
                "project": project,
                "version": version,
                "version_number": version_number,
                "files": files,
                "missing_files": [
                    filename for filename, present in files.items() if not present
                ],
                "has_architecture_png": files["architecture-diagram.png"],
            }
        )

    return sorted(
        runs,
        key=lambda run: (run["project"].lower(), run["version_number"]),
    )


def _supabase_get_run(project: str, version: str) -> dict | None:
    rows = _supabase_fetch_all(
        """
        select
          run_project,
          run_version,
          version_number,
          filename
        from web_run_artifacts
        where run_project = %s and run_version = %s
        order by filename
        """,
        (project, version),
    )
    if not rows:
        return None
    version_number = int(rows[0]["version_number"])
    filenames = {str(row["filename"]) for row in rows}
    files = {filename: filename in filenames for filename in EXPECTED_RUN_FILES}
    return {
        "project": project,
        "version": version,
        "version_number": version_number,
        "files": files,
        "missing_files": [
            filename for filename, present in files.items() if not present
        ],
        "has_architecture_png": files["architecture-diagram.png"],
    }


def _supabase_load_run_sections(
    project: str,
    version: str,
) -> list[dict] | None:
    artifact_rows = _supabase_fetch_all(
        """
        select
          filename,
          content_text,
          content_bytes,
          content_type
        from web_run_artifacts
        where run_project = %s and run_version = %s
        """,
        (project, version),
    )
    if not artifact_rows:
        return None

    artifacts = {
        str(row["filename"]): row for row in artifact_rows
    }
    return _build_sections_from_artifacts(artifacts)


def _supabase_read_run_artifact(
    project: str,
    version: str,
    filename: str,
) -> dict | None:
    rows = _supabase_fetch_all(
        """
        select
          content_text,
          content_bytes,
          content_type
        from web_run_artifacts
        where run_project = %s and run_version = %s and filename = %s
        """,
        (project, version, filename),
    )
    if not rows:
        return None
    row = rows[0]
    content_type = str(row["content_type"])
    if row["content_bytes"] is not None:
        return {
            "content": bytes(row["content_bytes"]),
            "content_type": content_type,
        }
    if row["content_text"] is not None:
        return {
            "content": str(row["content_text"]).encode("utf-8"),
            "content_type": content_type,
        }
    return None


def _supabase_persist_run_artifacts(output_dir: Path) -> None:
    if not output_dir.is_dir():
        raise FileNotFoundError(f"Missing run output directory: {output_dir}")

    run_project = output_dir.parent.name
    run_version = output_dir.name
    version_number = _parse_version_number(run_version)

    present_filenames: set[str] = set()
    artifact_records: dict[str, dict[str, Any]] = {}
    for filename in EXPECTED_RUN_FILES:
        file_path = output_dir / filename
        if not file_path.is_file():
            continue
        present_filenames.add(filename)
        artifact_records[filename] = _build_artifact_record(file_path, filename)

    _supabase_execute(
        """
        delete from web_run_artifacts
        where run_project = %s and run_version = %s and filename = %s
        """,
        [
            (run_project, run_version, filename)
            for filename in EXPECTED_RUN_FILES
            if filename not in present_filenames
        ],
        many=True,
    )

    for filename, record in artifact_records.items():
        _supabase_execute(
            """
            insert into web_run_artifacts (
              run_project,
              run_version,
              version_number,
              filename,
              content_text,
              content_bytes,
              content_type
            ) values (
              %(run_project)s,
              %(run_version)s,
              %(version_number)s,
              %(filename)s,
              %(content_text)s,
              %(content_bytes)s,
              %(content_type)s
            )
            on conflict (run_project, run_version, filename) do update set
              version_number = excluded.version_number,
              content_text = excluded.content_text,
              content_bytes = excluded.content_bytes,
              content_type = excluded.content_type
            """,
            {
                "run_project": run_project,
                "run_version": run_version,
                "version_number": version_number,
                "filename": filename,
                "content_text": record["content_text"],
                "content_bytes": record["content_bytes"],
                "content_type": record["content_type"],
            },
        )


def _build_sections_from_run_path(run_path: Path) -> list[dict]:
    return _build_sections_from_artifacts(
        {
            "project-brief.md": _build_file_artifact_record(
                run_path / "project-brief.md", "project-brief.md"
            ),
            "prd.md": _build_file_artifact_record(run_path / "prd.md", "prd.md"),
            "architecture.md": _build_file_artifact_record(
                run_path / "architecture.md", "architecture.md"
            ),
            "architecture-diagram.mmd": _build_file_artifact_record(
                run_path / "architecture-diagram.mmd", "architecture-diagram.mmd"
            ),
            "architecture-diagram.png": _build_file_artifact_record(
                run_path / "architecture-diagram.png", "architecture-diagram.png"
            ),
            "gtm.md": _build_file_artifact_record(run_path / "gtm.md", "gtm.md"),
            "blackboard.md": _build_file_artifact_record(
                run_path / "blackboard.md", "blackboard.md"
            ),
            "activity_log.txt": _build_file_artifact_record(
                run_path / "activity_log.txt", "activity_log.txt"
            ),
        }
    )


def _build_sections_from_artifacts(artifacts: dict[str, dict[str, Any]]) -> list[dict]:
    return [
        _build_text_section(
            "Brief",
            "project-brief.md",
            _artifact_text(artifacts.get("project-brief.md")),
        ),
        _build_text_section(
            "PRD",
            "prd.md",
            _artifact_text(artifacts.get("prd.md")),
        ),
        _build_text_section(
            "Architecture",
            "architecture.md",
            _artifact_text(artifacts.get("architecture.md")),
        ),
        _build_mermaid_section(
            _artifact_text(artifacts.get("architecture-diagram.mmd")),
            bool(artifacts.get("architecture-diagram.png")),
        ),
        _build_text_section(
            "GTM",
            "gtm.md",
            _artifact_text(artifacts.get("gtm.md")),
        ),
        _build_text_section(
            "Blackboard",
            "blackboard.md",
            _artifact_text(artifacts.get("blackboard.md")),
        ),
        _build_text_section(
            "Activity Log",
            "activity_log.txt",
            _artifact_text(artifacts.get("activity_log.txt")),
        ),
    ]


def _build_text_section(title: str, filename: str, content: str | None) -> dict:
    return {
        "title": title,
        "filename": filename,
        "content": content,
        "present": content is not None,
    }


def _build_mermaid_section(content: str | None, png_present: bool) -> dict:
    return {
        "title": "Diagramme Mermaid",
        "filename": "architecture-diagram.mmd",
        "content": content,
        "present": content is not None,
        "png_present": png_present,
    }


def _artifact_text(artifact_row: dict[str, Any] | None) -> str | None:
    if artifact_row is None:
        return None
    if artifact_row.get("content_text") is not None:
        return str(artifact_row["content_text"])
    if artifact_row.get("content_bytes") is not None:
        return bytes(artifact_row["content_bytes"]).decode("utf-8")
    return None


def _build_artifact_record(file_path: Path, filename: str) -> dict[str, Any]:
    if filename == "architecture-diagram.png":
        return {
            "content_text": None,
            "content_bytes": file_path.read_bytes(),
            "content_type": _artifact_content_type(filename),
        }
    return {
        "content_text": file_path.read_text(encoding="utf-8"),
        "content_bytes": None,
        "content_type": _artifact_content_type(filename),
    }


def _build_file_artifact_record(file_path: Path, filename: str) -> dict[str, Any] | None:
    if not file_path.is_file():
        return None
    return _build_artifact_record(file_path, filename)


def _artifact_content_type(filename: str) -> str:
    return _TEXT_ARTIFACT_CONTENT_TYPES.get(
        filename,
        _BINARY_ARTIFACT_CONTENT_TYPES.get(filename, "application/octet-stream"),
    )


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


def _resolve_tests_root(outputs_root: Path | None) -> Path:
    outputs_base = _resolve_outputs_root(outputs_root)
    if outputs_base.name == "tests":
        return outputs_base
    return outputs_base / "tests"


def _resolve_outputs_root(outputs_root: Path | None) -> Path:
    if outputs_root is None:
        return Path(__file__).resolve().parent.parent / "outputs"
    return outputs_root.resolve()


def _file_job_path(job_id: str, jobs_root: Path | None = None) -> Path:
    return _resolve_jobs_root(jobs_root) / f"{job_id}.json"


def _file_write_job(job: dict, jobs_root: Path | None = None) -> None:
    root = _resolve_jobs_root(jobs_root)
    root.mkdir(parents=True, exist_ok=True)
    job_path = _file_job_path(job["job_id"], root)
    temp_path = job_path.with_suffix(".json.tmp")
    temp_path.write_text(
        json.dumps(job, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temp_path.replace(job_path)


def _file_run_path(
    project: str,
    version: str,
    outputs_root: Path | None = None,
) -> Path:
    return _resolve_tests_root(outputs_root) / project / version


def _build_short_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    token = secrets.token_hex(4)
    return f"{timestamp}-{token}"


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _coerce_value(value: object) -> object:
    if isinstance(value, Path):
        return str(value)
    return value


def _is_safe_job_id(job_id: str) -> bool:
    if not job_id:
        return False
    return "/" not in job_id and "\\" not in job_id and ".." not in job_id


def _version_sort_key(path: Path) -> tuple[int, str]:
    match = _VERSION_PATTERN.fullmatch(path.name)
    if not match:
        return (10**9, path.name.lower())
    return (int(match.group(1)), path.name.lower())


def _parse_version_number(version: str) -> int:
    match = _VERSION_PATTERN.fullmatch(version)
    if not match:
        raise ValueError(f"Invalid run version: {version!r}")
    return int(match.group(1))


def _normalize_supabase_job_row(row: dict[str, Any]) -> dict:
    normalized = dict(row)
    normalized["created_at"] = _format_timestamp(normalized["created_at"])
    normalized["updated_at"] = _format_timestamp(normalized["updated_at"])
    for key in ("session_id", "status", "brief_text", "brief_preview", "project_title", "project_name", "output_dir", "run_project", "run_version", "error", "job_id"):
        normalized[key] = str(normalized.get(key, ""))
    return normalized


def _format_timestamp(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return str(value)


def _supabase_database_url() -> str:
    database_url = os.getenv("SUPABASE_DATABASE_URL", "").strip()
    if not database_url:
        raise RuntimeError(
            "WEB_STORAGE_BACKEND=supabase requires SUPABASE_DATABASE_URL."
        )
    return database_url


def _supabase_connection():
    try:
        import psycopg
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "Supabase storage requires psycopg[binary] to be installed."
        ) from error
    return psycopg.connect(_supabase_database_url())


def _supabase_fetch_all(query: str, params: tuple[Any, ...] | None = None) -> list[dict]:
    try:
        from psycopg.rows import dict_row
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "Supabase storage requires psycopg[binary] to be installed."
        ) from error

    with _supabase_connection() as connection:
        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(query, params or ())
            rows = cursor.fetchall()
    return [dict(row) for row in rows]


def _supabase_execute(
    query: str,
    params: Any | list[Any] | tuple[Any, ...] | None = None,
    *,
    many: bool = False,
) -> None:
    with _supabase_connection() as connection:
        with connection.cursor() as cursor:
            if many:
                for item in params or []:
                    cursor.execute(query, item)
                return
            cursor.execute(query, params or ())
