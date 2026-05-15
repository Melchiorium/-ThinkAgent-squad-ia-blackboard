from __future__ import annotations

from pathlib import Path
import re
from typing import Any

if __package__ and __package__.startswith("app"):
    from .blackboard_items import (
        ALLOWED_ITEM_TYPES,
        ALLOWED_PRIORITIES,
        ALLOWED_ROUTING_TARGETS,
        ALLOWED_STATUSES,
    )
    from .readiness import READY_STATUSES
else:
    from blackboard_items import (
        ALLOWED_ITEM_TYPES,
        ALLOWED_PRIORITIES,
        ALLOWED_ROUTING_TARGETS,
        ALLOWED_STATUSES,
    )
    from readiness import READY_STATUSES


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
_V4_READINESS_SECTIONS = {
    "product": "Product Readiness",
    "growth": "GTM Readiness",
    "tech": "Technical Readiness",
}
_V4_ABSENCE_SECTION_REPLACEMENTS = {
    "open questions": "- No open questions remain for this role at this step.",
    "requested changes": "- No requested changes remain for this role at this step.",
    "risks": "- No new risks are identified for this role at this step.",
}


def extract_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    seen_exact: set[str] = set()
    seen_normalized: dict[str, str] = {}
    current_heading = ""
    current_lines: list[str] = []
    for line in text.splitlines():
        match = _SECTION_HEADING_PATTERN.match(line.strip())
        if match:
            if current_heading:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = match.group(1).strip()
            normalized_heading = _normalize_heading(current_heading)
            if current_heading in seen_exact:
                raise ValueError(f"Duplicate top-level heading: '{current_heading}'.")
            if normalized_heading in seen_normalized:
                previous_heading = seen_normalized[normalized_heading]
                raise ValueError(
                    "Duplicate top-level heading after normalization: "
                    f"'{current_heading}' conflicts with '{previous_heading}'."
                )
            seen_exact.add(current_heading)
            seen_normalized[normalized_heading] = current_heading
            current_lines = []
            continue
        if current_heading:
            current_lines.append(line)
    if current_heading:
        sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def extract_section(text: str, heading: str) -> str:
    normalized_heading = _normalize_heading(heading)
    for section_heading, section_text in extract_sections(text).items():
        if _normalize_heading(section_heading) == normalized_heading:
            return section_text
    return ""


def parse_v4_agent_response(text: str, *, role: str | None = None) -> dict[str, Any]:
    source_text = text
    parsed_text = text
    if role:
        normalized_role = _normalize_role(role)
        parsed_text = _strip_ignorable_preamble_sections(parsed_text, role)
        parsed_text = _normalize_bare_contract_headings(parsed_text, normalized_role)
        if normalized_role == "product":
            parsed_text = _insert_missing_product_arbitration_heading(parsed_text)
            parsed_text = _move_product_locking_before_internal_sections(parsed_text)
        parsed_text = _strip_human_sections_between_internal_sections(parsed_text, role)
        parsed_text = _strip_trailing_content_after_internal_sections(parsed_text, role)
        parsed_text = _strip_ignorable_trailing_duplicate_sections(parsed_text, role)
        parsed_text = _normalize_placeholder_only_absence_sections(parsed_text, normalized_role)
        if normalized_role == "tech":
            parsed_text = _normalize_tech_mermaid_subsection(parsed_text)
    sections = extract_sections(parsed_text)
    document_sections = []
    for heading, section_text in sections.items():
        if _normalize_heading(heading) in _INTERNAL_SECTION_HEADINGS:
            continue
        document_sections.append(f"## {heading}\n\n{section_text}".rstrip())

    return {
        "raw_response": source_text,
        "document_text": "\n\n".join(document_sections).strip(),
        "sections": sections,
        "items_to_create": parse_item_creates(
            _get_section_by_normalized_heading(sections, "Blackboard Items To Create")
        ),
        "items_to_update": parse_item_updates(
            _get_section_by_normalized_heading(sections, "Blackboard Items To Update")
        ),
    }


def parse_item_creates(section_text: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line_number, line in _iter_bullet_lines(section_text):
        parts = [part.strip() for part in line.split("|", 6)]
        if len(parts) == 7:
            item_type, author, targets, priority, tags, title, content = parts
        elif len(parts) == 6:
            if parts[2].strip().upper() in ALLOWED_PRIORITIES:
                item_type, targets, priority, tags, title, content = parts
                author = ""
            else:
                item_type, author, targets, priority, tags = parts[:5]
                title, content = _split_title_content_fallback(
                    title_content=parts[5],
                    line_number=line_number,
                    line=line,
                )
        else:
            raise ValueError(
                "V4 item creation lines must use: TYPE | AUTHOR | TARGETS | PRIORITY | TAGS | TITLE | CONTENT"
                f" (line {line_number}: {line})"
            )
        parsed_targets, parsed_tags = _normalize_create_targets_and_tags(targets, tags)
        item_type, parsed_tags = _normalize_create_type_and_tags(item_type, parsed_tags)
        items.append(
            {
                "type": item_type,
                "author": author,
                "targets": parsed_targets,
                "priority": priority,
                "tags": parsed_tags,
                "title": title,
                "content": content,
                "raw_line": line,
                "line_number": line_number,
            }
        )
    return items


def _normalize_create_targets_and_tags(targets: str, tags: str) -> tuple[list[str], list[str]]:
    parsed_targets = _split_csv_field(targets)
    parsed_tags = _split_csv_field(tags)
    valid_targets = [
        target for target in parsed_targets if target.strip().upper() in ALLOWED_ROUTING_TARGETS
    ]
    misplaced_tags = [
        target for target in parsed_targets if target.strip().upper() not in ALLOWED_ROUTING_TARGETS
    ]
    if valid_targets and misplaced_tags:
        existing_tags = {tag.strip().lower() for tag in parsed_tags}
        for misplaced_tag in misplaced_tags:
            if misplaced_tag.strip().lower() not in existing_tags:
                parsed_tags.append(misplaced_tag)
    return valid_targets or parsed_targets, parsed_tags


def _normalize_create_type_and_tags(item_type: str, tags: list[str]) -> tuple[str, list[str]]:
    normalized_type = item_type.strip().upper()
    if normalized_type in ALLOWED_ITEM_TYPES:
        return normalized_type, tags
    if _looks_like_item_id(normalized_type):
        return item_type, tags
    embedded_type = _extract_embedded_item_type(normalized_type)
    if embedded_type:
        if normalized_type not in {tag.strip().upper() for tag in tags}:
            tags.append(normalized_type)
        return embedded_type, tags
    if _looks_like_custom_item_code(normalized_type):
        if normalized_type not in {tag.strip().upper() for tag in tags}:
            tags.append(normalized_type)
        return "QUESTION", tags
    return item_type, tags


def _split_title_content_fallback(
    *,
    title_content: str,
    line_number: int,
    line: str,
) -> tuple[str, str]:
    """Accept the common `Title: Content` slip while keeping `|` canonical."""
    if ":" not in title_content:
        raise ValueError(
            "V4 item creation lines must use: TYPE | AUTHOR | TARGETS | PRIORITY | TAGS | TITLE | CONTENT"
            f" (line {line_number}: {line})"
        )
    title, content = [part.strip() for part in title_content.split(":", 1)]
    if not title or not content:
        raise ValueError(
            "V4 item creation fallback requires non-empty TITLE and CONTENT"
            f" (line {line_number}: {line})"
        )
    return title, content


def parse_item_updates(section_text: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for line_number, line in _iter_bullet_lines(section_text):
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 2:
            raise ValueError(
                "V4 item update lines in Blackboard Items To Update must use exactly: "
                f"ITEM-001 | ANSWERED (line {line_number}: {line})"
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
    allowed_headings = {
        _normalize_heading(heading)
        for heading in (
            _V4_REQUIRED_SECTIONS[normalized_role]["human"]
            + _V4_REQUIRED_SECTIONS[normalized_role]["internal"]
        )
    }

    for original_heading in sections:
        normalized_heading = _normalize_heading(original_heading)
        if normalized_heading not in allowed_headings:
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name=original_heading,
                    detail="unexpected top-level heading",
                    raw_response_trace_path=raw_response_trace_path,
                )
            )

    for heading in _V4_REQUIRED_SECTIONS[normalized_role]["human"]:
        section_text = _get_section_by_normalized_heading(sections, heading)
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
        if heading == _V4_READINESS_SECTIONS[normalized_role]:
            _validate_v4_readiness_section(
                role=normalized_role,
                mode_label=mode_label,
                section_name=heading,
                section_text=section_text,
                raw_response_trace_path=raw_response_trace_path,
            )
        elif _is_placeholder_only_section(section_text):
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
        section_text = _get_section_by_normalized_heading(sections, heading)
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
        architecture_notes = _get_section_by_normalized_heading(sections, "Architecture Notes")
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
    existing_item_ids: set[str] | None = None,
) -> None:
    normalized_role = str(role).strip().lower() or "unknown"
    raw_response_trace_path = str(raw_response_trace_path or "").strip()
    allowed_create_types = {str(value).strip().upper() for value in (allowed_create_types or ALLOWED_ITEM_TYPES)}
    existing_item_ids = {
        str(item_id).strip().upper()
        for item_id in (existing_item_ids or set())
        if str(item_id).strip()
    }

    for item in parsed_response.get("items_to_create", []):
        item_type = str(item.get("type", "")).strip().upper()
        if _looks_like_item_id(item_type):
            raise ValueError(
                _format_create_update_confusion_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    item_id=item_type,
                    raw_line=item.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
        targets = [
            str(value).strip().upper()
            for value in item.get("targets", [])
            if str(value).strip()
        ]
        if not targets or any(target not in ALLOWED_ROUTING_TARGETS for target in targets):
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="targets",
                    invalid_value=", ".join(targets) or "missing",
                    allowed_values=sorted(ALLOWED_ROUTING_TARGETS),
                    raw_line=item.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
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
        item_id = str(update.get("id", "")).strip().upper()
        if item_id not in existing_item_ids:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="id",
                    invalid_value=update.get("id", ""),
                    allowed_values=sorted(existing_item_ids) if existing_item_ids else ["pre-existing item id"],
                    raw_line=update.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
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
        if not stripped:
            continue
        is_bullet = False
        while stripped.startswith("- ") or stripped.startswith("* "):
            is_bullet = True
            stripped = stripped[2:].strip()
        if not stripped:
            continue
        if _normalize_placeholder_line(stripped) in _V4_PLACEHOLDER_TEXTS:
            continue
        if is_bullet:
            lines.append((line_number, stripped))
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


def _top_level_heading_ranges(text: str) -> list[tuple[int, int, str]]:
    lines = text.splitlines()
    positions: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = _SECTION_HEADING_PATTERN.match(line.strip())
        if match:
            positions.append((index, match.group(1).strip()))

    ranges: list[tuple[int, int, str]] = []
    for position, (start, heading) in enumerate(positions):
        end = positions[position + 1][0] if position + 1 < len(positions) else len(lines)
        ranges.append((start, end, heading))
    return ranges


def _looks_like_item_id(value: str) -> bool:
    return bool(re.fullmatch(r"ITEM-\d+", str(value).strip().upper()))


def _looks_like_custom_item_code(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)*-\d+", str(value).strip().upper()))


def _extract_embedded_item_type(value: str) -> str:
    normalized = str(value).strip().upper()
    for item_type in sorted(ALLOWED_ITEM_TYPES, key=len, reverse=True):
        if normalized.endswith(f"_{item_type}") or normalized.endswith(f"-{item_type}"):
            return item_type
    return ""


def _looks_like_mermaid_start(value: str) -> bool:
    lowered = value.strip().lower()
    return lowered.startswith(
        (
            "graph ",
            "flowchart ",
            "sequencediagram",
            "classdiagram",
            "statediagram",
            "erdiagram",
            "journey",
            "gantt",
            "pie ",
            "mindmap",
            "timeline",
        )
    )


def _get_section_by_normalized_heading(sections: dict[str, str], heading: str) -> str:
    normalized_heading = _normalize_heading(heading)
    matches: list[tuple[str, str]] = []
    for section_heading, section_text in sections.items():
        if _normalize_heading(section_heading) == normalized_heading:
            matches.append((section_heading, section_text))
    if not matches:
        return ""
    if len(matches) > 1:
        match_labels = ", ".join(f"'{heading}'" for heading, _ in matches)
        raise ValueError(
            f"Duplicate top-level heading after normalization for '{heading}': {match_labels}."
        )
    return matches[0][1]


def _strip_ignorable_preamble_sections(text: str, role: str | None) -> str:
    if not role:
        return text
    normalized_role = _normalize_role(role)
    allowed_headings = {
        _normalize_heading(heading)
        for heading in (
            _V4_REQUIRED_SECTIONS[normalized_role]["human"]
            + _V4_REQUIRED_SECTIONS[normalized_role]["internal"]
        )
    }
    lines = text.splitlines()
    heading_indexes: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = _SECTION_HEADING_PATTERN.match(line.strip())
        if match:
            heading_indexes.append((index, match.group(1).strip()))
    if not heading_indexes:
        return text

    first_allowed_position: int | None = None
    for position, (_, heading) in enumerate(heading_indexes):
        if _normalize_heading(heading) in allowed_headings:
            first_allowed_position = position
            break
    if first_allowed_position is None or first_allowed_position == 0:
        return text

    preamble_headings = heading_indexes[:first_allowed_position]
    if not all(_is_ignorable_preamble_heading(heading) for _, heading in preamble_headings):
        return text

    first_allowed_line = heading_indexes[first_allowed_position][0]
    return "\n".join(lines[first_allowed_line:]).strip()


def _strip_ignorable_trailing_duplicate_sections(text: str, role: str | None) -> str:
    if not role:
        return text
    normalized_role = _normalize_role(role)
    allowed_human_headings = {
        _normalize_heading(heading)
        for heading in _V4_REQUIRED_SECTIONS[normalized_role]["human"]
    }
    internal_headings = {
        _normalize_heading(heading)
        for heading in _V4_REQUIRED_SECTIONS[normalized_role]["internal"]
    }
    lines = text.splitlines()
    heading_positions: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = _SECTION_HEADING_PATTERN.match(line.strip())
        if match:
            heading_positions.append((index, match.group(1).strip()))
    if not heading_positions:
        return text

    seen_headings: set[str] = set()
    internal_seen = False
    ranges_to_drop: list[tuple[int, int]] = []
    for position, (start_index, heading) in enumerate(heading_positions):
        normalized_heading = _normalize_heading(heading)
        next_start = heading_positions[position + 1][0] if position + 1 < len(heading_positions) else len(lines)
        section_text = "\n".join(lines[start_index + 1:next_start]).strip()
        is_duplicate = normalized_heading in seen_headings
        if (
            is_duplicate
            and internal_seen
            and normalized_heading in allowed_human_headings
            and _is_cross_reference_only_section(section_text)
        ):
            ranges_to_drop.append((start_index, next_start))
        seen_headings.add(normalized_heading)
        if normalized_heading in internal_headings:
            internal_seen = True

    if not ranges_to_drop:
        return text

    kept_lines: list[str] = []
    for index, line in enumerate(lines):
        if any(start <= index < end for start, end in ranges_to_drop):
            continue
        kept_lines.append(line)
    return "\n".join(kept_lines).strip()


def _strip_trailing_content_after_internal_sections(text: str, role: str | None) -> str:
    if not role:
        return text
    normalized_role = _normalize_role(role)
    internal_headings = {
        _normalize_heading(heading)
        for heading in _V4_REQUIRED_SECTIONS[normalized_role]["internal"]
    }
    lines = text.splitlines()
    seen_internal: set[str] = set()
    for index, line in enumerate(lines):
        match = _SECTION_HEADING_PATTERN.match(line.strip())
        if not match:
            continue
        normalized_heading = _normalize_heading(match.group(1))
        if normalized_heading in internal_headings:
            seen_internal.add(normalized_heading)
            continue
        if seen_internal == internal_headings:
            return "\n".join(lines[:index]).strip()
    return text


def _strip_human_sections_between_internal_sections(text: str, role: str | None) -> str:
    if not role:
        return text
    normalized_role = _normalize_role(role)
    internal_headings = {
        _normalize_heading(heading)
        for heading in _V4_REQUIRED_SECTIONS[normalized_role]["internal"]
    }
    heading_ranges = _top_level_heading_ranges(text)
    if not heading_ranges:
        return text

    seen_internal: set[str] = set()
    ranges_to_drop: list[tuple[int, int]] = []
    for start, end, heading in heading_ranges:
        normalized_heading = _normalize_heading(heading)
        if normalized_heading in internal_headings:
            seen_internal.add(normalized_heading)
            continue
        if seen_internal and seen_internal != internal_headings:
            ranges_to_drop.append((start, end))

    if not ranges_to_drop:
        return text

    lines = text.splitlines()
    kept_lines: list[str] = []
    for index, line in enumerate(lines):
        if any(start <= index < end for start, end in ranges_to_drop):
            continue
        kept_lines.append(line)
    return "\n".join(kept_lines).strip()


def _normalize_bare_contract_headings(text: str, role: str) -> str:
    normalized_role = _normalize_role(role)
    allowed_headings = {
        _normalize_heading(heading): heading
        for heading in (
            _V4_REQUIRED_SECTIONS[normalized_role]["human"]
            + _V4_REQUIRED_SECTIONS[normalized_role]["internal"]
        )
    }
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        normalized_line = _normalize_heading(stripped)
        if (
            stripped
            and not stripped.startswith("#")
            and not stripped.startswith("-")
            and not stripped.startswith("*")
            and normalized_line in allowed_headings
        ):
            lines.append(f"## {allowed_headings[normalized_line]}")
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _move_product_locking_before_internal_sections(text: str) -> str:
    heading_ranges = _top_level_heading_ranges(text)
    if not heading_ranges:
        return text

    first_internal_position: int | None = None
    product_locking_before_internal = False
    product_locking_after_internal: tuple[int, int, int] | None = None
    internal_headings = {
        "blackboard items to create",
        "blackboard items to update",
    }

    for position, (start, end, heading) in enumerate(heading_ranges):
        normalized_heading = _normalize_heading(heading)
        if normalized_heading in internal_headings and first_internal_position is None:
            first_internal_position = position
        if normalized_heading != "product locking":
            continue
        if first_internal_position is None:
            product_locking_before_internal = True
        elif product_locking_after_internal is None:
            product_locking_after_internal = (start, end, position)

    if (
        first_internal_position is None
        or product_locking_before_internal
        or product_locking_after_internal is None
    ):
        return text

    lines = text.splitlines()
    locking_start, locking_end, _ = product_locking_after_internal
    insert_before = heading_ranges[first_internal_position][0]
    locking_block = lines[locking_start:locking_end]
    rebuilt = (
        lines[:insert_before]
        + [""] if lines[:insert_before] and lines[insert_before - 1].strip() else lines[:insert_before]
    )
    rebuilt = rebuilt + locking_block + [""]
    rebuilt.extend(lines[insert_before:locking_start])
    rebuilt.extend(lines[locking_end:])
    return "\n".join(rebuilt).strip()


def _insert_missing_product_arbitration_heading(text: str) -> str:
    headings = {_normalize_heading(heading) for _, _, heading in _top_level_heading_ranges(text)}
    if "product arbitration" in headings:
        return text

    lines = text.splitlines()
    product_readiness_seen = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        top_heading = _SECTION_HEADING_PATTERN.match(stripped)
        if top_heading:
            normalized_heading = _normalize_heading(top_heading.group(1))
            if normalized_heading == "product readiness":
                product_readiness_seen = True
                continue
            if normalized_heading in {"product locking", "blackboard items to create"}:
                return text
        if product_readiness_seen and stripped == "### Retained":
            return "\n".join(lines[:index] + ["## Product Arbitration", ""] + lines[index:]).strip()
    return text


def _normalize_placeholder_only_absence_sections(text: str, role: str) -> str:
    normalized_role = _normalize_role(role)
    allowed_human_headings = {
        _normalize_heading(heading)
        for heading in _V4_REQUIRED_SECTIONS[normalized_role]["human"]
    }
    heading_ranges = _top_level_heading_ranges(text)
    if not heading_ranges:
        return text

    lines = text.splitlines()
    normalized_lines: list[str] = []
    cursor = 0
    for start, end, heading in heading_ranges:
        normalized_lines.extend(lines[cursor:start])
        normalized_heading = _normalize_heading(heading)
        section_text = "\n".join(lines[start + 1:end]).strip()
        replacement = _V4_ABSENCE_SECTION_REPLACEMENTS.get(normalized_heading)
        if (
            normalized_heading in allowed_human_headings
            and replacement
            and _is_placeholder_only_section(section_text)
        ):
            normalized_lines.append(lines[start])
            normalized_lines.append(replacement)
        else:
            normalized_lines.extend(lines[start:end])
        cursor = end
    normalized_lines.extend(lines[cursor:])
    return "\n".join(normalized_lines).strip()


def _normalize_tech_mermaid_subsection(text: str) -> str:
    lines = text.splitlines()
    normalized_lines: list[str] = []
    in_architecture_notes = False
    after_mermaid_heading = False
    raw_mermaid_fence_open = False
    raw_mermaid_started = False

    for line in lines:
        stripped = line.strip()
        top_heading = _SECTION_HEADING_PATTERN.match(stripped)
        if top_heading:
            if raw_mermaid_fence_open:
                normalized_lines.append("```")
                raw_mermaid_fence_open = False
            in_architecture_notes = _normalize_heading(top_heading.group(1)) == "architecture notes"
            after_mermaid_heading = False
            raw_mermaid_started = False
            normalized_lines.append(line)
            continue

        if not in_architecture_notes:
            normalized_lines.append(line)
            continue

        if _SUBSECTION_HEADING_PATTERN.match(stripped):
            if raw_mermaid_fence_open:
                normalized_lines.append("```")
                raw_mermaid_fence_open = False
            after_mermaid_heading = _normalize_heading(stripped) == "mermaid diagram"
            raw_mermaid_started = False
            normalized_lines.append(line)
            continue

        if _normalize_loose_heading(stripped) == "mermaid diagram":
            if raw_mermaid_fence_open:
                normalized_lines.append("```")
                raw_mermaid_fence_open = False
            normalized_lines.append("### Mermaid Diagram")
            after_mermaid_heading = True
            raw_mermaid_started = False
            continue

        if after_mermaid_heading:
            if not raw_mermaid_started and _normalize_loose_heading(stripped) == "mermaid diagram":
                continue
            if stripped.startswith("```"):
                after_mermaid_heading = False
                normalized_lines.append(line)
                continue
            if _looks_like_mermaid_start(stripped):
                normalized_lines.append("```mermaid")
                normalized_lines.append(stripped)
                raw_mermaid_fence_open = True
                raw_mermaid_started = True
                continue
            if raw_mermaid_fence_open:
                if stripped.startswith("- ") or stripped.startswith("* "):
                    normalized_lines.append("```")
                    raw_mermaid_fence_open = False
                    after_mermaid_heading = False
                    raw_mermaid_started = False
                    normalized_lines.append(line)
                    continue
                normalized_lines.append(stripped)
                continue

        normalized_lines.append(line)

    if raw_mermaid_fence_open:
        normalized_lines.append("```")
    return "\n".join(normalized_lines).strip()


def _is_ignorable_preamble_heading(heading: str) -> bool:
    normalized = _normalize_heading(heading)
    return (
        normalized == "role"
        or normalized.startswith("role ")
        or normalized.startswith("role (")
        or normalized == "context"
        or normalized.startswith("context ")
        or normalized.startswith("context (")
    )


def _normalize_loose_heading(value: str) -> str:
    return _normalize_heading(re.sub(r"^[-*]\s+", "", value.strip()))


def _is_cross_reference_only_section(text: str) -> bool:
    meaningful_lines = _meaningful_lines(text)
    if not meaningful_lines:
        return True
    for line in meaningful_lines:
        normalized = _normalize_placeholder_line(line)
        if normalized in _V4_PLACEHOLDER_TEXTS:
            continue
        if normalized.startswith("see ") and "above" in normalized:
            continue
        return False
    return True


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


def _validate_v4_readiness_section(
    *,
    role: str,
    mode_label: str,
    section_name: str,
    section_text: str,
    raw_response_trace_path: str,
) -> None:
    status_lines = [
        line.strip()
        for line in section_text.splitlines()
        if line.strip().lower().startswith("status:")
    ]
    if not status_lines:
        raise ValueError(
            _format_document_validation_error(
                role=role,
                mode_label=mode_label,
                section_name=section_name,
                detail="missing readiness status line",
                raw_response_trace_path=raw_response_trace_path,
            )
        )
    if len(status_lines) > 1:
        raise ValueError(
            _format_document_validation_error(
                role=role,
                mode_label=mode_label,
                section_name=section_name,
                detail="multiple readiness status lines",
                raw_response_trace_path=raw_response_trace_path,
            )
        )

    raw_status = status_lines[0].split(":", 1)[1].strip()
    normalized_status = raw_status.upper()
    if normalized_status not in READY_STATUSES:
        raise ValueError(
            _format_document_validation_error(
                role=role,
                mode_label=mode_label,
                section_name=section_name,
                detail=f"invalid status '{raw_status}'",
                raw_response_trace_path=raw_response_trace_path,
            )
        )


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
    while True:
        stripped = re.sub(r"^[\-*>]+\s*", "", normalized)
        if stripped == normalized:
            break
        normalized = stripped
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


def _format_create_update_confusion_error(
    *,
    role: str,
    mode_label: str,
    item_id: str,
    raw_line: str,
    raw_response_trace_path: str,
) -> str:
    trace_suffix = f" Raw trace: {raw_response_trace_path}." if raw_response_trace_path else ""
    raw_line_suffix = f" Offending line: {raw_line}." if raw_line else ""
    return (
        f"V4 {role} {mode_label} item validation failed: "
        f"Blackboard Items To Create starts with existing item id '{item_id}'. "
        "Create items must start with a valid item type. "
        "Existing item ids belong in Blackboard Items To Update, where updates contain only item id and status."
        f"{raw_line_suffix}{trace_suffix}"
    )
