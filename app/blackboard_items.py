from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import re

if __package__ and __package__.startswith("app"):
    from .run_store import RunWorkspace, read_text_file, write_text_file
else:
    from run_store import RunWorkspace, read_text_file, write_text_file


ALLOWED_ITEM_TYPES = {
    "QUESTION",
    "RISK",
    "DECISION",
    "PROPOSAL",
    "FEEDBACK",
    "WARNING",
    "CONSTRAINT",
}
ALLOWED_PRIORITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
ALLOWED_STATUSES = {"OPEN", "ANSWERED", "ACCEPTED", "REJECTED", "OBSOLETE"}
ALLOWED_ROUTING_TARGETS = {"PRODUCT", "GROWTH", "TECH", "ALL", "EXTERNAL"}
ROLE_ROUTING_TARGETS = ("PRODUCT", "GROWTH", "TECH")
_ITEM_FILE_PATTERN = re.compile(r"^ITEM-(\d+)\.yaml$")


def create_item(
    run: RunWorkspace,
    *,
    type: str,
    author: str,
    targets: list[str],
    priority: str,
    tags: list[str],
    title: str,
    content: str,
    status: str = "OPEN",
) -> dict[str, Any]:
    item_type = _normalize_choice(type, ALLOWED_ITEM_TYPES, "type")
    item_author = _normalize_identifier(author, "author")
    item_targets = _normalize_targets(targets)
    item_priority = _normalize_choice(priority, ALLOWED_PRIORITIES, "priority")
    item_status = _normalize_choice(status, ALLOWED_STATUSES, "status")
    item_tags = _normalize_tags(tags)
    item_title = _normalize_title(title)
    item_content = _normalize_content(content)
    timestamp = _utc_now()

    item = {
        "id": _next_item_id(run),
        "type": item_type,
        "author": item_author,
        "targets": item_targets,
        "priority": item_priority,
        "status": item_status,
        "tags": item_tags,
        "title": item_title,
        "content": item_content,
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    _write_item(run, item)
    return item


def list_items(
    run: RunWorkspace,
    *,
    target: str | None = None,
    author: str | None = None,
    type: str | None = None,
    status: str | None = None,
    tag: str | None = None,
) -> list[dict[str, Any]]:
    items = [_read_item(path) for path in _item_paths(run)]
    if target:
        normalized_target = _normalize_identifier(target, "target")
        if normalized_target != "ALL":
            items = [item for item in items if normalized_target in item["targets"]]
    if author:
        normalized_author = _normalize_identifier(author, "author")
        items = [item for item in items if item["author"] == normalized_author]
    if type:
        normalized_type = _normalize_choice(type, ALLOWED_ITEM_TYPES, "type")
        items = [item for item in items if item["type"] == normalized_type]
    if status:
        normalized_status = _normalize_choice(status, ALLOWED_STATUSES, "status")
        items = [item for item in items if item["status"] == normalized_status]
    if tag:
        normalized_tag = _normalize_tag(tag)
        items = [item for item in items if normalized_tag in item["tags"]]
    return items


def list_open_items(run: RunWorkspace) -> list[dict[str, Any]]:
    return list_items(run, status="OPEN")


def update_item_status(run: RunWorkspace, item_id: str, status: str) -> dict[str, Any]:
    normalized_status = _normalize_choice(status, ALLOWED_STATUSES, "status")
    item_path = _item_path(run, item_id)
    if not item_path.exists():
        raise FileNotFoundError(f"Missing blackboard item: {item_id}")

    item = _read_item(item_path)
    item["status"] = normalized_status
    item["updated_at"] = _utc_now()
    _write_item(run, item)
    return item


def _next_item_id(run: RunWorkspace) -> str:
    numbers = []
    for path in _item_paths(run):
        match = _ITEM_FILE_PATTERN.match(path.name)
        if match:
            numbers.append(int(match.group(1)))
    return f"ITEM-{(max(numbers) if numbers else 0) + 1:03d}"


def _item_paths(run: RunWorkspace) -> list[Path]:
    if not run.items_dir.exists():
        return []
    return sorted(run.items_dir.glob("ITEM-*.yaml"), key=_item_sort_key)


def _item_sort_key(path: Path) -> tuple[int, str]:
    match = _ITEM_FILE_PATTERN.match(path.name)
    if match:
        return int(match.group(1)), path.name.lower()
    return 0, path.name.lower()


def _item_path(run: RunWorkspace, item_id: str) -> Path:
    normalized_item_id = _normalize_item_id(item_id)
    return run.items_dir / f"{normalized_item_id}.yaml"


def _write_item(run: RunWorkspace, item: dict[str, Any]) -> None:
    write_text_file(_item_path(run, item["id"]), _render_item_yaml(item))


def _read_item(path: Path) -> dict[str, Any]:
    return _parse_item_yaml(read_text_file(path))


def _render_item_yaml(item: dict[str, Any]) -> str:
    lines = [
        f"id: {item['id']}",
        f"type: {item['type']}",
        f"author: {item['author']}",
        _render_list_field("targets", item["targets"]),
        f"priority: {item['priority']}",
        f"status: {item['status']}",
        _render_list_field("tags", item["tags"]),
        f"title: {item['title']}",
        "content: |",
        *(_indent_block(item["content"]) or ["  "]),
        f"created_at: {item['created_at']}",
        f"updated_at: {item['updated_at']}",
    ]
    return "\n".join(lines) + "\n"


def _parse_item_yaml(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    index = 0

    item_id, index = _consume_scalar(lines, index, "id")
    item_type, index = _consume_scalar(lines, index, "type")
    author, index = _consume_scalar(lines, index, "author")
    targets, index = _consume_list(lines, index, "targets")
    priority, index = _consume_scalar(lines, index, "priority")
    status, index = _consume_scalar(lines, index, "status")
    tags, index = _consume_list(lines, index, "tags")
    title, index = _consume_scalar(lines, index, "title")
    content, index = _consume_block(lines, index, "content")
    created_at, index = _consume_scalar(lines, index, "created_at")
    updated_at, index = _consume_scalar(lines, index, "updated_at")
    index = _skip_blank_lines(lines, index)
    if index < len(lines):
        raise ValueError("Unexpected trailing content in blackboard item YAML.")

    return {
        "id": item_id,
        "type": item_type,
        "author": author,
        "targets": targets,
        "priority": priority,
        "status": status,
        "tags": tags,
        "title": title,
        "content": content,
        "created_at": created_at,
        "updated_at": updated_at,
    }


def _consume_scalar(lines: list[str], index: int, key: str) -> tuple[str, int]:
    index = _skip_blank_lines(lines, index)
    if index >= len(lines):
        raise ValueError(f"Missing {key} field in blackboard item YAML.")
    line = lines[index]
    prefix = f"{key}:"
    if not line.startswith(prefix):
        raise ValueError(f"Expected {key} field in blackboard item YAML.")
    value = line.split(":", 1)[1].strip()
    index += 1
    return value, index


def _consume_list(lines: list[str], index: int, key: str) -> tuple[list[str], int]:
    index = _skip_blank_lines(lines, index)
    if index >= len(lines):
        raise ValueError(f"Missing {key} field in blackboard item YAML.")
    line = lines[index]
    prefix = f"{key}:"
    if not line.startswith(prefix):
        raise ValueError(f"Expected {key} field in blackboard item YAML.")
    remainder = line.split(":", 1)[1].strip()
    values: list[str] = []
    index += 1
    if remainder == "[]":
        return values, index
    while index < len(lines):
        current = lines[index]
        if not current.startswith("  - "):
            break
        value = current[4:].strip()
        if value and value != "None":
            values.append(value)
        index += 1
    return values, index


def _consume_block(lines: list[str], index: int, key: str) -> tuple[str, int]:
    index = _skip_blank_lines(lines, index)
    if index >= len(lines):
        raise ValueError(f"Missing {key} block in blackboard item YAML.")
    line = lines[index]
    prefix = f"{key}:"
    if not line.startswith(prefix):
        raise ValueError(f"Expected {key} block in blackboard item YAML.")
    remainder = line.split(":", 1)[1].strip()
    index += 1
    if remainder and remainder != "|":
        return remainder, index

    block_lines: list[str] = []
    while index < len(lines):
        current = lines[index]
        if current.startswith("created_at:") or current.startswith("updated_at:"):
            break
        if current.startswith("  "):
            block_lines.append(current[2:])
            index += 1
            continue
        if not current.strip():
            block_lines.append("")
            index += 1
            continue
        break
    return "\n".join(block_lines).rstrip("\n"), index


def _skip_blank_lines(lines: list[str], index: int) -> int:
    while index < len(lines) and not lines[index].strip():
        index += 1
    return index


def _render_list_field(key: str, values: list[str]) -> str:
    if not values:
        return f"{key}: []"
    return "\n".join([f"{key}:", *[f"  - {value}" for value in values]])


def _indent_block(content: str) -> list[str]:
    text = str(content).rstrip("\n")
    if not text:
        return []
    return [f"  {line}" if line else "  " for line in text.splitlines()]


def _normalize_choice(value: Any, allowed: set[str], field_name: str) -> str:
    normalized = str(value).strip().upper()
    if normalized not in allowed:
        allowed_values = ", ".join(sorted(allowed))
        raise ValueError(f"{field_name} must be one of: {allowed_values}")
    return normalized


def _normalize_identifier(value: Any, field_name: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", str(value).strip()).strip("_").upper()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def _normalize_item_id(value: Any) -> str:
    normalized = str(value).strip().upper()
    if not re.fullmatch(r"ITEM-\d+", normalized):
        raise ValueError("item_id must look like ITEM-001")
    return normalized


def _normalize_targets(values: list[str]) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()
    has_external = False
    for value in values or []:
        item = _normalize_identifier(value, "target")
        if item not in ALLOWED_ROUTING_TARGETS:
            allowed_values = ", ".join(sorted(ALLOWED_ROUTING_TARGETS))
            raise ValueError(f"target must be one of: {allowed_values}")
        if item == "EXTERNAL":
            has_external = True
        expanded = list(ROLE_ROUTING_TARGETS) if item == "ALL" else [item]
        for target in expanded:
            if target in seen:
                continue
            seen.add(target)
            normalized.append(target)
    if not normalized:
        raise ValueError("targets must contain at least one recipient")
    if has_external and normalized != ["EXTERNAL"]:
        raise ValueError("EXTERNAL must be the only target when used")
    return normalized


def _normalize_tags(values: list[str]) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()
    for value in values or []:
        tag = _normalize_tag(value)
        if not tag or tag in seen:
            continue
        seen.add(tag)
        normalized.append(tag)
    return normalized


def _normalize_tag(value: Any) -> str:
    text = str(value).strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def _normalize_title(value: Any) -> str:
    title = " ".join(str(value).split()).strip()
    if not title:
        raise ValueError("title must not be empty")
    return title


def _normalize_content(value: Any) -> str:
    return str(value).rstrip()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
