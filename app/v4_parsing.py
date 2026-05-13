from __future__ import annotations

from pathlib import Path
import re
from typing import Any


_SECTION_HEADING_PATTERN = re.compile(r"^##\s+(.+?)\s*$")
_INTERNAL_SECTION_HEADINGS = {
    "blackboard items to create",
    "blackboard items to update",
}


def extract_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current_heading = ""
    current_lines: list[str] = []
    for line in text.splitlines():
        match = _SECTION_HEADING_PATTERN.match(line.strip())
        if match:
            if current_heading:
                sections[current_heading] = current_lines[:]
            current_heading = match.group(1).strip()
            current_lines = []
            continue
        if current_heading:
            current_lines.append(line)
    if current_heading:
        sections[current_heading] = current_lines
    return {
        heading: "\n".join(lines).strip()
        for heading, lines in sections.items()
    }


def extract_section(text: str, heading: str) -> str:
    normalized_heading = _normalize_heading(heading)
    for section_heading, section_text in extract_sections(text).items():
        if _normalize_heading(section_heading) == normalized_heading:
            return section_text
    return ""


def parse_v4_agent_response(text: str) -> dict[str, Any]:
    sections = extract_sections(text)
    document_sections = []
    for heading, section_text in sections.items():
        if _normalize_heading(heading) in _INTERNAL_SECTION_HEADINGS:
            continue
        document_sections.append(f"## {heading}\n\n{section_text}".rstrip())

    return {
        "raw_response": text,
        "document_text": "\n\n".join(document_sections).strip(),
        "sections": sections,
        "items_to_create": parse_item_creates(sections.get("Blackboard Items To Create", "")),
        "items_to_update": parse_item_updates(sections.get("Blackboard Items To Update", "")),
    }


def parse_item_creates(section_text: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line in _iter_bullet_lines(section_text):
        parts = [part.strip() for part in line.split("|", 6)]
        if len(parts) != 7:
            raise ValueError(
                "V4 item creation lines must use: TYPE | AUTHOR | TARGETS | PRIORITY | TAGS | TITLE | CONTENT"
            )
        item_type, author, targets, priority, tags, title, content = parts
        items.append(
            {
                "type": item_type,
                "author": author,
                "targets": _split_csv_field(targets),
                "priority": priority,
                "tags": _split_csv_field(tags),
                "title": title,
                "content": content,
            }
        )
    return items


def parse_item_updates(section_text: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for line in _iter_bullet_lines(section_text):
        parts = [part.strip() for part in line.split("|", 1)]
        if len(parts) != 2:
            raise ValueError("V4 item update lines must use: ITEM-001 | ANSWERED")
        item_id, status = parts
        items.append({"id": item_id, "status": status})
    return items


def _iter_bullet_lines(section_text: str) -> list[str]:
    lines = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped == "- None":
            continue
        if stripped.startswith("- "):
            lines.append(stripped[2:].strip())
        elif stripped.startswith("* "):
            lines.append(stripped[2:].strip())
    return lines


def _split_csv_field(value: str) -> list[str]:
    if not value or value == "None":
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def _normalize_heading(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.lstrip("#").strip()
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized
