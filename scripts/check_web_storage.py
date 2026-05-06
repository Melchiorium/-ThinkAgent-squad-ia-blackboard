#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
from pathlib import Path
from datetime import datetime, timezone


REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.web_storage import (  # noqa: E402
    create_job,
    create_session_id,
    delete_run,
    get_job,
    get_run,
    list_jobs,
    list_runs,
    load_run_sections,
    check_storage_readiness,
    persist_run_artifacts,
    read_run_artifact,
    WebStorageConfigurationError,
    WebStorageConnectionError,
    WebStorageDependencyError,
    WebStorageSchemaError,
    resolve_web_storage_backend,
    update_job,
)


PROJECT_NAME = "Storage Check"
VERSION_NAME = "version 1"
BRIEF_TEXT = "Storage validation brief."


def main() -> int:
    backend = resolve_web_storage_backend()
    print(f"Storage backend: {backend}")
    readiness = check_storage_readiness(backend)
    print(readiness["message"])

    with tempfile.TemporaryDirectory(prefix="squad-web-storage-") as temp_dir:
        temp_root = Path(temp_dir)
        outputs_root = temp_root / "outputs"
        jobs_root = temp_root / "web-jobs"

        output_dir = _write_fake_output_dir(outputs_root)
        session_id = create_session_id()
        job = create_job(
            BRIEF_TEXT,
            session_id,
            project_title=PROJECT_NAME,
            jobs_root=jobs_root,
            backend=backend,
        )
        _assert(job["status"] == "queued", "job starts queued")

        job = update_job(job["job_id"], {"status": "running"}, jobs_root=jobs_root, backend=backend)
        _assert(job["status"] == "running", "job updates to running")

        progress_timestamp = _utc_now()
        progress_blocks = [
            {
                "id": "brief_received",
                "group": "Brief",
                "label": "Brief reçu",
                "status": "done",
            },
            {
                "id": "product_problem",
                "group": "Product",
                "label": "Problème cible",
                "status": "active",
            },
        ]
        progress_events = [
            {
                "timestamp": progress_timestamp,
                "stage": "brief_received",
                "label": "Brief reçu",
                "detail": "Le brief est disponible pour la génération.",
            },
            {
                "timestamp": progress_timestamp,
                "stage": "product_problem",
                "label": "Product formule le problème cible",
                "detail": "Le cadrage produit avance.",
            },
        ]
        job = update_job(
            job["job_id"],
            {
                "progress_stage": "product_problem",
                "progress_label": "Product formule le problème cible",
                "progress_detail": "Le cadrage produit avance.",
                "progress_order": 3,
                "progress_total": 19,
                "progress_blocks": progress_blocks,
                "progress_events": progress_events,
                "progress_started_at": progress_timestamp,
                "progress_last_event_at": progress_timestamp,
                "progress_timeout_seconds": 600,
                "progress_error_type": "",
                "progress_error_message": "",
            },
            jobs_root=jobs_root,
            backend=backend,
        )
        _assert(job["progress_stage"] == "product_problem", "progress stage is stored")
        _assert(len(job["progress_blocks"]) == 2, "progress blocks are stored")
        _assert(len(job["progress_events"]) == 2, "progress events are stored")

        persist_run_artifacts(output_dir, backend=backend)

        job = update_job(
            job["job_id"],
            {
                "status": "done",
                "project_name": PROJECT_NAME,
                "output_dir": str(output_dir),
                "run_project": PROJECT_NAME,
                "run_version": VERSION_NAME,
                "error": "",
            },
            jobs_root=jobs_root,
            backend=backend,
        )
        _assert(job["status"] == "done", "job updates to done")

        fetched_job = get_job(job["job_id"], jobs_root=jobs_root, backend=backend)
        _assert(fetched_job is not None, "job can be re-read")
        _assert(fetched_job["job_id"] == job["job_id"], "re-read job id matches")
        _assert(fetched_job["run_project"] == PROJECT_NAME, "re-read job run project matches")
        _assert(fetched_job["progress_error_type"] == "", "progress error type remains empty")
        _assert(
            fetched_job["progress_timeout_seconds"] == 600,
            "progress timeout is preserved",
        )

        jobs = list_jobs(session_id=session_id, jobs_root=jobs_root, backend=backend)
        _assert(len(jobs) == 1, "session job list has one item")

        runs = list_runs(outputs_root=outputs_root, backend=backend)
        _assert(
            any(run["project"] == PROJECT_NAME and run["version"] == VERSION_NAME for run in runs),
            "run list contains the fake run",
        )

        run = get_run(PROJECT_NAME, VERSION_NAME, outputs_root=outputs_root, backend=backend)
        _assert(run is not None, "run can be re-read")

        sections = load_run_sections(PROJECT_NAME, VERSION_NAME, outputs_root=outputs_root, backend=backend)
        _assert(sections is not None, "run sections can be loaded")
        _assert(
            any(section["title"] == "PRD" and section["present"] for section in sections),
            "PRD section is present",
        )

        artifact = read_run_artifact(
            PROJECT_NAME,
            VERSION_NAME,
            "prd.md",
            outputs_root=outputs_root,
            backend=backend,
        )
        _assert(artifact is not None, "PRD artifact can be read")
        _assert(b"Storage Check" in artifact["content"], "PRD artifact contains project name")
        _assert(artifact["content_type"].startswith("text/"), "PRD artifact content type is text")

        _assert(
            delete_run(PROJECT_NAME, VERSION_NAME, outputs_root=outputs_root, backend=backend),
            "run delete returns success",
        )
        _assert(
            get_run(PROJECT_NAME, VERSION_NAME, outputs_root=outputs_root, backend=backend) is None,
            "deleted run can no longer be read",
        )
        _assert(
            not any(
                run["project"] == PROJECT_NAME and run["version"] == VERSION_NAME
                for run in list_runs(outputs_root=outputs_root, backend=backend)
            ),
            "deleted run disappears from inventory",
        )
        try:
            delete_run(
                "Bad/Project",
                VERSION_NAME,
                outputs_root=outputs_root,
                backend=backend,
            )
        except ValueError:
            pass
        else:
            raise AssertionError("invalid run coordinates were accepted")

    print("Storage validation passed.")
    return 0


def _write_fake_output_dir(outputs_root: Path) -> Path:
    output_dir = outputs_root / "tests" / PROJECT_NAME / VERSION_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "project-brief.md": f"Project name: {PROJECT_NAME}\n\n{BRIEF_TEXT}\n",
        "prd.md": "# Storage Check PRD\n\nFake PRD content.\n",
        "architecture.md": "# Storage Check Architecture\n\nFake architecture content.\n",
        "architecture-diagram.mmd": "flowchart LR A --> B\n",
        "gtm.md": "# Storage Check GTM\n\nFake GTM content.\n",
        "blackboard.md": "# Blackboard\n\nFake blackboard content.\n",
        "activity_log.txt": "main | storage_check | scripts/check_web_storage.py\n",
    }
    for filename, content in files.items():
        (output_dir / filename).write_text(content, encoding="utf-8")
    return output_dir


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except WebStorageDependencyError as error:
        print(f"Storage validation failed [dependency]: {error}", file=sys.stderr)
        raise SystemExit(1)
    except WebStorageConfigurationError as error:
        print(f"Storage validation failed [configuration]: {error}", file=sys.stderr)
        raise SystemExit(1)
    except WebStorageConnectionError as error:
        print(f"Storage validation failed [connection]: {error}", file=sys.stderr)
        raise SystemExit(1)
    except WebStorageSchemaError as error:
        print(f"Storage validation failed [schema]: {error}", file=sys.stderr)
        raise SystemExit(1)
    except ValueError as error:
        print(f"Storage validation failed [configuration]: {error}", file=sys.stderr)
        raise SystemExit(1)
    except Exception as error:
        print(f"Storage validation failed: {error}", file=sys.stderr)
        raise
