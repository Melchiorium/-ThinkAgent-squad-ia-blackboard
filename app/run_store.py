from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import re
import secrets


RUNS_ROOT_DIRNAME = "runs"
_RUN_ID_SLUG_PATTERN = re.compile(r"[^a-z0-9]+")


@dataclass(slots=True)
class RunWorkspace:
    run_id: str
    project_title: str
    project_slug: str
    root: Path
    blackboard_dir: Path
    items_dir: Path
    documents_dir: Path
    product_documents_dir: Path
    tech_documents_dir: Path
    growth_documents_dir: Path
    summaries_dir: Path
    activity_log_dir: Path
    activity_log_path: Path
    final_outputs_dir: Path

    def ensure_directories(self) -> None:
        for path in (
            self.root,
            self.blackboard_dir,
            self.items_dir,
            self.documents_dir,
            self.product_documents_dir,
            self.tech_documents_dir,
            self.growth_documents_dir,
            self.summaries_dir,
            self.activity_log_dir,
            self.final_outputs_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)

    def document_dir(self, agent: str) -> Path:
        normalized_agent = _normalize_agent(agent)
        return {
            "product": self.product_documents_dir,
            "tech": self.tech_documents_dir,
            "growth": self.growth_documents_dir,
        }[normalized_agent]


def create_run_workspace(project_title: str, base_root: Path | None = None) -> RunWorkspace:
    project_title = str(project_title).strip()
    if not project_title:
        raise ValueError("project_title must not be empty.")

    root = resolve_runs_root(base_root)
    root.mkdir(parents=True, exist_ok=True)

    while True:
        run_id = _build_run_id(project_title)
        workspace_root = root / run_id
        try:
            workspace_root.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            continue
        workspace = _build_workspace(workspace_root, project_title, run_id)
        workspace.ensure_directories()
        return workspace


def resolve_runs_root(base_root: Path | None = None) -> Path:
    if base_root is not None:
        return Path(base_root)
    return Path(__file__).resolve().parent.parent / RUNS_ROOT_DIRNAME


def write_text_file(path: Path, content: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def read_text_file(path: Path) -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing text file: {path}")
    return path.read_text(encoding="utf-8")


def append_activity_log_entry(workspace: RunWorkspace, entry: str | dict[str, Any]) -> Path:
    workspace.activity_log_dir.mkdir(parents=True, exist_ok=True)
    line = _format_activity_log_entry(entry)
    with workspace.activity_log_path.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return workspace.activity_log_path


def _build_workspace(root: Path, project_title: str, run_id: str) -> RunWorkspace:
    documents_dir = root / "documents"
    product_documents_dir = documents_dir / "product"
    tech_documents_dir = documents_dir / "tech"
    growth_documents_dir = documents_dir / "growth"
    blackboard_dir = root / "blackboard"
    items_dir = blackboard_dir / "items"
    summaries_dir = root / "summaries"
    activity_log_dir = root / "activity_log"
    final_outputs_dir = root / "final_outputs"
    return RunWorkspace(
        run_id=run_id,
        project_title=project_title,
        project_slug=_normalize_slug(project_title),
        root=root,
        blackboard_dir=blackboard_dir,
        items_dir=items_dir,
        documents_dir=documents_dir,
        product_documents_dir=product_documents_dir,
        tech_documents_dir=tech_documents_dir,
        growth_documents_dir=growth_documents_dir,
        summaries_dir=summaries_dir,
        activity_log_dir=activity_log_dir,
        activity_log_path=activity_log_dir / "activity_log.txt",
        final_outputs_dir=final_outputs_dir,
    )


def _build_run_id(project_title: str) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    slug = _normalize_slug(project_title)
    suffix = secrets.token_hex(3)
    return f"{timestamp}-{slug}-{suffix}"


def _normalize_slug(value: str) -> str:
    slug = _RUN_ID_SLUG_PATTERN.sub("-", value.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "run"


def _normalize_agent(agent: str) -> str:
    normalized = str(agent).strip().lower()
    if normalized not in {"product", "tech", "growth"}:
        raise ValueError("agent must be one of: product, tech, growth")
    return normalized


def _format_activity_log_entry(entry: str | dict[str, Any]) -> str:
    if isinstance(entry, str):
        details = entry.strip()
        timestamp = _utc_now()
        return " | ".join(part for part in (timestamp, details) if part)

    timestamp = str(entry.get("timestamp", "")).strip() or _utc_now()
    agent = str(entry.get("agent", "")).strip()
    event = str(entry.get("event", "")).strip()
    source = str(entry.get("source", "")).strip()
    details = str(entry.get("details", "")).strip()
    parts = [timestamp, agent, event, source]
    if details:
        parts.append(details)
    return " | ".join(part for part in parts if part)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
