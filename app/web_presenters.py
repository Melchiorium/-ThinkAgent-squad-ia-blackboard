from __future__ import annotations

from collections.abc import Callable


def build_run_view(run: dict) -> dict:
    present_file_count = len(run["files"]) - len(run["missing_files"])
    return {
        "project": run["project"],
        "version": run["version"],
        "present_file_count": present_file_count,
        "total_file_count": len(run["files"]),
        "missing_files": run["missing_files"],
    }


def build_job_view(
    job: dict,
    *,
    status_url: str,
    status_api_url: str,
    run_url: str | None = None,
) -> dict:
    view = dict(job)
    view["display_title"] = job_display_title(job)
    view["status_label"] = status_label(job.get("status", ""))
    view["status_url"] = status_url
    view["status_api_url"] = status_api_url
    view["run_url"] = run_url
    return view


def build_job_status_payload(job: dict, *, run_url: str | None = None) -> dict:
    return {
        "job_id": job["job_id"],
        "status": job["status"],
        "created_at": job["created_at"],
        "updated_at": job["updated_at"],
        "brief_preview": job.get("brief_preview", ""),
        "project_title": job.get("project_title", ""),
        "display_title": job_display_title(job),
        "error": job.get("error", ""),
        "run_url": run_url,
    }


def build_rendered_sections(
    sections: list[dict] | None,
    *,
    artifact_url_builder: Callable[[str], str],
) -> list[dict] | None:
    if sections is None:
        return None

    rendered_sections: list[dict] = []
    for section in sections:
        rendered = dict(section)
        filename = str(rendered.get("filename", ""))
        if rendered.get("present"):
            rendered["artifact_url"] = artifact_url_builder(filename)
        else:
            rendered["artifact_url"] = None

        if filename == "architecture-diagram.mmd":
            rendered["png_url"] = (
                artifact_url_builder("architecture-diagram.png")
                if rendered.get("png_present")
                else None
            )
        rendered_sections.append(rendered)
    return rendered_sections


def status_label(status: str) -> str:
    labels = {
        "queued": "En attente",
        "running": "En cours",
        "done": "Terminé",
        "failed": "Échec",
    }
    return labels.get(status, status)


def job_display_title(job: dict) -> str:
    project_title = str(job.get("project_title", "")).strip()
    if project_title:
        return project_title
    project_name = str(job.get("project_name", "")).strip()
    if project_name:
        return project_name
    return "Génération"
