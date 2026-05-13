from __future__ import annotations

from pathlib import Path
import re
from typing import Any

if __package__ and __package__.startswith("app"):
    from .blackboard_items import ALLOWED_ITEM_TYPES, ALLOWED_PRIORITIES, ALLOWED_STATUSES
else:
    from blackboard_items import ALLOWED_ITEM_TYPES, ALLOWED_PRIORITIES, ALLOWED_STATUSES


_SECTION_HEADING_PATTERN = re.compile(r"^##\s+(.+?)\s*$")
_SUBSECTION_HEADING_PATTERN = re.compile(r"^###\s+(.+?)\s*$")
_INTERNAL_SECTION_HEADINGS = {
    "blackboard items to create",
    "blackboard items to update",
}
_V4_PLACEHOLDER_TEXTS = {
    "see above",
    "as above",
    "same as above",
    "see previous section",
    "tbd",
    "to be defined",
    "n/a",
    "none",
}
_V4_REQUIRED_SECTIONS = {
    "product": {
        "human": [
            "Product Problem",
            "Initial Wedge",
            "First Target User",
            "Existing Alternatives And Switching Trigger",
            "Core MVP Workflow",
            "In Scope",
            "Out of Scope",
            "MVP Build Vs Pilot Operations",
            "Business Model Hypothesis",
            "Critical Assumptions",
            "How To Test Quickly",
            "Acceptance Criteria",
            "Risks And Failure Modes",
            "Product Readiness",
            "Product Arbitration",
            "Product Locking",
        ],
        "internal": [
            "Blackboard Items To Create",
            "Blackboard Items To Update",
        ],
    },
    "growth": {
        "human": [
            "Go-To-Market Notes",
            "Review Summary",
            "Build Vs Pilot Operations",
            "Critical Assumptions",
            "Requested Changes",
            "Risks",
            "Open Questions",
            "Why This Could Fail Even With Good Execution",
            "GTM Readiness",
        ],
        "internal": [
            "Blackboard Items To Create",
            "Blackboard Items To Update",
        ],
    },
    "tech": {
        "human": [
            "Architecture Notes",
            "Review Summary",
            "Critical Assumptions",
            "Requested Changes",
            "Risks",
            "Open Questions",
            "Why This Could Fail Even With Good Execution",
            "Technical Readiness",
        ],
        "internal": [
            "Blackboard Items To Create",
            "Blackboard Items To Update",
        ],
    },
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
    for line_number, line in _iter_bullet_lines(section_text):
        parts = [part.strip() for part in line.split("|", 6)]
        if len(parts) != 7:
            raise ValueError(
                "V4 item creation lines must use: TYPE | AUTHOR | TARGETS | PRIORITY | TAGS | TITLE | CONTENT"
                f" (line {line_number}: {line})"
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
                "raw_line": line,
                "line_number": line_number,
            }
        )
    return items


def parse_item_updates(section_text: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for line_number, line in _iter_bullet_lines(section_text):
        parts = [part.strip() for part in line.split("|", 1)]
        if len(parts) != 2:
            raise ValueError(
                f"V4 item update lines must use: ITEM-001 | ANSWERED (line {line_number}: {line})"
            )
        item_id, status = parts
        items.append({"id": item_id, "status": status, "raw_line": line, "line_number": line_number})
    return items


def validate_v4_document(
    *,
    role: str,
    mode_label: str,
    parsed_response: dict[str, Any],
    raw_response_trace_path: str | Path | None = None,
) -> None:
    normalized_role = _normalize_role(role)
    sections = parsed_response.get("sections") or {}
    raw_response_trace_path = str(raw_response_trace_path or "").strip()

    for heading in _V4_REQUIRED_SECTIONS[normalized_role]["human"]:
        section_text = sections.get(heading, "")
        if not section_text.strip():
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name=heading,
                    detail="section is missing or empty",
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
        if _is_placeholder_only_section(section_text):
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name=heading,
                    detail=_first_placeholder_line(section_text),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )

    for heading in _V4_REQUIRED_SECTIONS[normalized_role]["internal"]:
        section_text = sections.get(heading, "")
        if not section_text.strip():
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name=heading,
                    detail="section is missing or empty",
                    raw_response_trace_path=raw_response_trace_path,
                )
            )

    if normalized_role == "tech":
        architecture_notes = sections.get("Architecture Notes", "")
        mermaid_block = _extract_subsection(architecture_notes, "Mermaid Diagram")
        if not mermaid_block.strip():
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name="Architecture Notes > Mermaid Diagram",
                    detail="subsection is missing or empty",
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
        if _is_placeholder_only_section(mermaid_block):
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name="Architecture Notes > Mermaid Diagram",
                    detail=_first_placeholder_line(mermaid_block),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )


def validate_v4_item_operations(
    *,
    role: str,
    mode_label: str,
    parsed_response: dict[str, Any],
    raw_response_trace_path: str | Path | None = None,
    allowed_create_types: set[str] | None = None,
    allow_updates: bool = True,
) -> None:
    normalized_role = str(role).strip().lower() or "unknown"
    raw_response_trace_path = str(raw_response_trace_path or "").strip()
    allowed_create_types = {str(value).strip().upper() for value in (allowed_create_types or ALLOWED_ITEM_TYPES)}

    for item in parsed_response.get("items_to_create", []):
        item_type = str(item.get("type", "")).strip().upper()
        if item_type not in allowed_create_types:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="type",
                    invalid_value=item.get("type", ""),
                    allowed_values=sorted(allowed_create_types),
                    raw_line=item.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
        priority = str(item.get("priority", "")).strip().upper()
        if priority not in ALLOWED_PRIORITIES:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="priority",
                    invalid_value=item.get("priority", ""),
                    allowed_values=sorted(ALLOWED_PRIORITIES),
                    raw_line=item.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )

    updates = parsed_response.get("items_to_update", [])
    if not allow_updates and updates:
        first_update = updates[0]
        raise ValueError(
            _format_item_validation_error(
                role=normalized_role,
                mode_label=mode_label,
                field_name="items_to_update",
                invalid_value="updates are not allowed in this phase",
                allowed_values=["no updates"],
                raw_line=first_update.get("raw_line", ""),
                raw_response_trace_path=raw_response_trace_path,
            )
        )

    for update in updates:
        status = str(update.get("status", "")).strip().upper()
        if status not in ALLOWED_STATUSES:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="status",
                    invalid_value=update.get("status", ""),
                    allowed_values=sorted(ALLOWED_STATUSES),
                    raw_line=update.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )


def _iter_bullet_lines(section_text: str) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    for line_number, line in enumerate(section_text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped == "- None":
            continue
        if stripped.startswith("- "):
            lines.append((line_number, stripped[2:].strip()))
        elif stripped.startswith("* "):
            lines.append((line_number, stripped[2:].strip()))
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


def _normalize_role(role: str) -> str:
    normalized = str(role).strip().lower()
    if normalized not in _V4_REQUIRED_SECTIONS:
        raise ValueError("role must be one of: product, growth, tech")
    return normalized


def _extract_subsection(text: str, subsection_heading: str) -> str:
    capture = False
    captured: list[str] = []
    target_heading = subsection_heading.strip().lower()
    for line in text.splitlines():
        stripped = line.strip()
        match = _SUBSECTION_HEADING_PATTERN.match(stripped)
        if match:
            heading = match.group(1).strip().lower()
            if capture and heading != target_heading:
                break
            capture = heading == target_heading
            continue
        if capture:
            captured.append(line)
    return "\n".join(captured).strip()


def _is_placeholder_only_section(text: str) -> bool:
    meaningful_lines = _meaningful_lines(text)
    if not meaningful_lines:
        return True
    return all(_normalize_placeholder_line(line) in _V4_PLACEHOLDER_TEXTS for line in meaningful_lines)


def _meaningful_lines(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith(("```", "~~~")):
            continue
        lines.append(stripped)
    return lines


def _normalize_placeholder_line(line: str) -> str:
    normalized = line.strip().lower()
    normalized = re.sub(r"^[\-*>]+\s*", "", normalized)
    normalized = normalized.strip("`\"' ")
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def _first_placeholder_line(text: str) -> str:
    for line in _meaningful_lines(text):
        normalized = _normalize_placeholder_line(line)
        if normalized in _V4_PLACEHOLDER_TEXTS:
            return line.strip()
    return "placeholder-only content"


def _format_document_validation_error(
    *,
    role: str,
    mode_label: str,
    section_name: str,
    detail: str,
    raw_response_trace_path: str,
) -> str:
    trace_suffix = f" Raw trace: {raw_response_trace_path}." if raw_response_trace_path else ""
    return (
        f"V4 {role} {mode_label} document validation failed for section '{section_name}': "
        f"{detail}.{trace_suffix}"
    )


def _format_item_validation_error(
    *,
    role: str,
    mode_label: str,
    field_name: str,
    invalid_value: str,
    allowed_values: list[str],
    raw_line: str,
    raw_response_trace_path: str,
) -> str:
    trace_suffix = f" Raw trace: {raw_response_trace_path}." if raw_response_trace_path else ""
    raw_line_suffix = f" Offending line: {raw_line}." if raw_line else ""
    allowed_text = ", ".join(allowed_values)
    return (
        f"V4 {role} {mode_label} item validation failed for field '{field_name}': "
        f"invalid value '{invalid_value}'. Allowed values: {allowed_text}."
        f"{raw_line_suffix}{trace_suffix}"
    )
