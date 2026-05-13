from __future__ import annotations

from pathlib import Path
import re

if __package__ and __package__.startswith("app"):
    from .run_store import RunWorkspace, read_text_file, write_text_file
else:
    from run_store import RunWorkspace, read_text_file, write_text_file


ALLOWED_DOCUMENT_AGENTS = {"product", "tech", "growth"}
_VERSION_PATTERN = re.compile(r"^(?P<stem>.+)_V(?P<version>\d+)$", re.IGNORECASE)


def write_document(run: RunWorkspace, agent: str, filename: str, content: str) -> Path:
    document_dir = _document_dir(run, agent)
    safe_filename = _normalize_filename(filename)
    path = document_dir / safe_filename
    write_text_file(path, content)
    return path


def list_documents(run: RunWorkspace, agent: str) -> list[str]:
    document_dir = _document_dir(run, agent)
    if not document_dir.exists():
        return []
    paths = sorted(document_dir.glob("*.md"), key=_document_sort_key)
    return [path.name for path in paths]


def read_named_document(run: RunWorkspace, agent: str, filename: str) -> str:
    path = _document_path(run, agent, filename)
    return read_text_file(path)


def read_latest_document(run: RunWorkspace, agent: str) -> str:
    filenames = list_documents(run, agent)
    if not filenames:
        raise FileNotFoundError(f"No documents found for agent: {agent}")
    return read_named_document(run, agent, filenames[-1])


def _document_path(run: RunWorkspace, agent: str, filename: str) -> Path:
    return _document_dir(run, agent) / _normalize_filename(filename)


def _document_dir(run: RunWorkspace, agent: str) -> Path:
    normalized_agent = _normalize_agent(agent)
    return run.document_dir(normalized_agent)


def _normalize_agent(agent: str) -> str:
    normalized = str(agent).strip().lower()
    if normalized not in ALLOWED_DOCUMENT_AGENTS:
        allowed = ", ".join(sorted(ALLOWED_DOCUMENT_AGENTS))
        raise ValueError(f"agent must be one of: {allowed}")
    return normalized


def _normalize_filename(filename: str) -> str:
    normalized = str(filename).strip()
    if not normalized:
        raise ValueError("filename must not be empty")
    if normalized != Path(normalized).name or ".." in Path(normalized).parts:
        raise ValueError("filename must be a simple file name without path segments")
    return normalized


def _document_sort_key(path: Path) -> tuple[int, int, str]:
    match = _VERSION_PATTERN.match(path.stem)
    if match:
        return int(match.group("version")), 1, path.name.lower()
    return -1, 0, path.name.lower()
