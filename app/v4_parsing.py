from __future__ import annotations

import json
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
_H1_HEADING_PATTERN = re.compile(r"^#\s+(.+?)\s*$")
_BLACKBOARD_JSON_MARKER = "BLACKBOARD_OPERATIONS:"
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
    "product": [
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
    "growth": [
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
    "tech": [
        "Architecture Notes",
        "Review Summary",
        "Critical Assumptions",
        "Requested Changes",
        "Risks",
        "Open Questions",
        "Why This Could Fail Even With Good Execution",
        "Technical Readiness",
    ],
}
_V4_READINESS_SECTIONS = {
    "product": "Product Readiness",
    "growth": "GTM Readiness",
    "tech": "Technical Readiness",
}
_V4_STRUCTURED_LIST_SECTIONS = {
    ("product", "Product Arbitration"): [
        ("retained", "Retained"),
        ("deferred", "Deferred"),
        ("rejected", "Rejected"),
        ("open_points", "Open Points"),
        ("rationales", "Rationales"),
    ],
    ("product", "Product Locking"): [
        ("confirmed_in_scope", "Confirmed In Scope"),
        ("confirmed_deferred", "Confirmed Deferred"),
        ("confirmed_out_of_scope", "Confirmed Out Of Scope"),
        ("locking_note", "Locking Note"),
    ],
    ("growth", "Build Vs Pilot Operations"): [
        ("must_be_productized_now", "Must Be Productized Now"),
        (
            "can_stay_manual_or_operational_during_pilot",
            "Can Stay Manual Or Operational During Pilot",
        ),
        ("deferred_until_after_proof", "Deferred Until After Proof"),
    ],
}
_V4_ARRAY_SECTIONS = {
    "product": {
        "In Scope",
        "Out of Scope",
        "Critical Assumptions",
        "How To Test Quickly",
        "Acceptance Criteria",
        "Risks And Failure Modes",
    },
    "growth": {
        "Critical Assumptions",
        "Requested Changes",
        "Risks",
        "Open Questions",
        "Why This Could Fail Even With Good Execution",
    },
    "tech": {
        "Critical Assumptions",
        "Requested Changes",
        "Risks",
        "Open Questions",
        "Why This Could Fail Even With Good Execution",
    },
}
_V4_EMPTY_ARRAY_SECTION_TEXT = {
    "Requested Changes": "- No requested changes remain.",
    "Risks": "- No material risk remains.",
    "Open Questions": "- No open questions remain.",
    "Why This Could Fail Even With Good Execution": "- No additional failure mode is identified.",
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
    _reject_machine_protocol_in_document(text)
    sections = extract_sections(text)
    document_sections = [
        f"## {heading}\n\n{section_text}".rstrip()
        for heading, section_text in sections.items()
    ]
    return {
        "raw_response": text,
        "document_text": "\n\n".join(document_sections).strip(),
        "sections": sections,
        "items_to_create": [],
        "items_to_update": [],
        "blackboard_operation_format": "separate_json",
    }


def v4_required_document_sections(role: str) -> list[str]:
    """Return the canonical V4 document section headings for a role."""
    normalized_role = _normalize_role(role)
    return list(_V4_REQUIRED_SECTIONS[normalized_role])


def build_v4_document_schema(role: str) -> dict[str, Any]:
    """Build a strict JSON schema for a role document payload."""
    normalized_role = _normalize_role(role)
    headings = v4_required_document_sections(normalized_role)
    return {
        "type": "object",
        "additionalProperties": False,
        "required": headings,
        "properties": {
            heading: _v4_document_section_schema(normalized_role, heading)
            for heading in headings
        },
    }


def parse_v4_structured_document(document_payload: Any, *, role: str) -> dict[str, Any]:
    """Render and parse a structured V4 role document payload."""
    normalized_role = _normalize_role(role)
    if not isinstance(document_payload, dict):
        raise ValueError("V4 document payload must be a JSON object.")

    headings = _V4_REQUIRED_SECTIONS[normalized_role]
    allowed_keys = set(headings)
    actual_keys = set(document_payload)
    unknown_keys = actual_keys - allowed_keys
    missing_keys = allowed_keys - actual_keys
    if unknown_keys:
        raise ValueError(
            "Unexpected V4 document section field: "
            + ", ".join(sorted(str(key) for key in unknown_keys))
        )
    if missing_keys:
        raise ValueError(
            "Missing V4 document section field: "
            + ", ".join(sorted(str(key) for key in missing_keys))
        )

    sections: dict[str, Any] = {}
    for heading in headings:
        sections[heading] = document_payload[heading]

    document_text = render_v4_structured_document(role=normalized_role, sections=sections)
    parsed = parse_v4_agent_response(document_text, role=normalized_role)
    parsed["structured_document_format"] = "json_sections"
    return parsed


def render_v4_structured_document(*, role: str, sections: dict[str, Any]) -> str:
    """Render canonical Markdown from structured V4 section bodies."""
    normalized_role = _normalize_role(role)
    blocks: list[str] = []
    for heading in _V4_REQUIRED_SECTIONS[normalized_role]:
        body = _render_v4_section_body(
            role=normalized_role,
            heading=heading,
            value=sections.get(heading, ""),
        )
        blocks.append(f"## {heading}\n\n{body}".rstrip())
    return "\n\n".join(blocks).strip()


def _render_v4_section_body(*, role: str, heading: str, value: Any) -> str:
    if heading == _V4_READINESS_SECTIONS[role]:
        return _render_v4_readiness_section(value, heading=heading)
    if role == "tech" and heading == "Architecture Notes":
        return _render_v4_architecture_notes(value)
    if heading in _V4_ARRAY_SECTIONS.get(role, set()):
        return _render_v4_array_section(value, heading=heading)
    list_section_fields = _V4_STRUCTURED_LIST_SECTIONS.get((role, heading))
    if list_section_fields:
        return _render_v4_structured_list_section(
            value,
            heading=heading,
            fields=list_section_fields,
        )
    if not isinstance(value, str):
        raise ValueError(f"V4 document section '{heading}' must be a string.")
    return value.strip()


def _render_v4_array_section(value: Any, *, heading: str) -> str:
    if not isinstance(value, list):
        raise ValueError(f"V4 document section '{heading}' must be an array.")
    return _render_markdown_list(
        value,
        section_name=heading,
        empty_text=_V4_EMPTY_ARRAY_SECTION_TEXT.get(heading),
    )


def _render_v4_readiness_section(value: Any, *, heading: str) -> str:
    if not isinstance(value, dict):
        raise ValueError(f"V4 document section '{heading}' must be a readiness object.")
    allowed_keys = {"status", "blocking_gaps", "required_improvements"}
    _validate_structured_object_keys(value, allowed_keys=allowed_keys, section_name=heading)
    status = str(value["status"]).strip().upper()
    if status not in READY_STATUSES:
        raise ValueError(f"V4 document section '{heading}' has invalid status: {value['status']}")
    return "\n\n".join(
        [
            f"Status: {status}",
            "Blocking Gaps:\n" + _render_markdown_list(value["blocking_gaps"], section_name=heading),
            "Required Improvements:\n"
            + _render_markdown_list(value["required_improvements"], section_name=heading),
        ]
    ).strip()


def _render_v4_architecture_notes(value: Any) -> str:
    section_name = "Architecture Notes"
    if not isinstance(value, dict):
        raise ValueError("V4 document section 'Architecture Notes' must be an object.")
    _validate_structured_object_keys(
        value,
        allowed_keys={"mermaid_diagram", "notes"},
        section_name=section_name,
    )
    mermaid_source = str(value["mermaid_diagram"]).strip()
    if not mermaid_source:
        raise ValueError("V4 document section 'Architecture Notes' has empty mermaid_diagram.")
    if "```" in mermaid_source:
        raise ValueError(
            "V4 document section 'Architecture Notes' mermaid_diagram must not include code fences."
        )
    notes = str(value["notes"]).strip()
    return "\n\n".join(
        [
            "### Mermaid Diagram\n```mermaid\n" + mermaid_source + "\n```",
            notes,
        ]
    ).strip()


def _render_v4_structured_list_section(
    value: Any,
    *,
    heading: str,
    fields: list[tuple[str, str]],
) -> str:
    if not isinstance(value, dict):
        raise ValueError(f"V4 document section '{heading}' must be an object.")
    allowed_keys = {field_name for field_name, _ in fields}
    _validate_structured_object_keys(value, allowed_keys=allowed_keys, section_name=heading)
    blocks = []
    for field_name, label in fields:
        blocks.append(
            f"### {label}\n"
            + _render_markdown_list(value[field_name], section_name=heading)
        )
    return "\n\n".join(blocks).strip()


def _render_markdown_list(
    value: Any,
    *,
    section_name: str,
    empty_text: str | None = None,
) -> str:
    if not isinstance(value, list):
        raise ValueError(f"V4 document section '{section_name}' expected a list.")
    if not value:
        return empty_text or "- None"
    lines = []
    for item in value:
        text = str(item).strip()
        if not text:
            continue
        if _normalize_placeholder_line(text) in _V4_PLACEHOLDER_TEXTS:
            raise ValueError(
                f"V4 document section '{section_name}' contains placeholder list item '{text}'. "
                "Use an empty array when there is no content."
            )
        lines.append("- " + text.replace("\n", "\n  "))
    return "\n".join(lines) if lines else (empty_text or "- None")


def _validate_structured_object_keys(
    value: dict[str, Any],
    *,
    allowed_keys: set[str],
    section_name: str,
) -> None:
    actual_keys = set(value)
    unknown_keys = actual_keys - allowed_keys
    missing_keys = allowed_keys - actual_keys
    if unknown_keys:
        raise ValueError(
            f"Unexpected V4 document field in section '{section_name}': "
            + ", ".join(sorted(unknown_keys))
        )
    if missing_keys:
        raise ValueError(
            f"Missing V4 document field in section '{section_name}': "
            + ", ".join(sorted(missing_keys))
        )


def _v4_document_section_schema(role: str, heading: str) -> dict[str, Any]:
    if heading == _V4_READINESS_SECTIONS[role]:
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["status", "blocking_gaps", "required_improvements"],
            "properties": {
                "status": {"enum": sorted(READY_STATUSES)},
                "blocking_gaps": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "required_improvements": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        }
    if role == "tech" and heading == "Architecture Notes":
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["mermaid_diagram", "notes"],
            "properties": {
                "mermaid_diagram": {
                    "type": "string",
                    "description": (
                        "Mermaid source only. Do not include code fences; the runtime "
                        "renders the ```mermaid fence."
                    ),
                },
                "notes": {
                    "type": "string",
                    "description": "Markdown notes for the architecture section.",
                },
            },
        }
    if heading in _V4_ARRAY_SECTIONS.get(role, set()):
        return {
            "type": "array",
            "items": {"type": "string"},
        }
    list_section_fields = _V4_STRUCTURED_LIST_SECTIONS.get((role, heading))
    if list_section_fields:
        return {
            "type": "object",
            "additionalProperties": False,
            "required": [field_name for field_name, _ in list_section_fields],
            "properties": {
                field_name: {
                    "type": "array",
                    "items": {"type": "string"},
                }
                for field_name, _ in list_section_fields
            },
        }
    schema: dict[str, Any] = {
        "type": "string",
        "description": (
            "Markdown body for this section only. Do not include the "
            "`##` heading; the runtime renders headings."
        ),
    }
    return schema


def parse_v4_blackboard_operations(
    operations: Any,
    *,
    line_number: int = 1,
) -> dict[str, list[dict[str, Any]]]:
    if not isinstance(operations, dict):
        raise ValueError("BLACKBOARD_OPERATIONS must be a JSON object.")
    allowed_keys = {"create", "update"}
    actual_keys = set(operations)
    unknown_keys = actual_keys - allowed_keys
    missing_keys = allowed_keys - actual_keys
    if unknown_keys:
        raise ValueError(
            "Unexpected BLACKBOARD_OPERATIONS field: "
            + ", ".join(sorted(str(key) for key in unknown_keys))
        )
    if missing_keys:
        raise ValueError(
            "Missing BLACKBOARD_OPERATIONS field: "
            + ", ".join(sorted(str(key) for key in missing_keys))
        )
    if not isinstance(operations["create"], list):
        raise ValueError("BLACKBOARD_OPERATIONS.create must be a list.")
    if not isinstance(operations["update"], list):
        raise ValueError("BLACKBOARD_OPERATIONS.update must be a list.")
    return {
        "items_to_create": [
            _parse_json_create_operation(item, line_number=line_number)
            for item in operations["create"]
        ],
        "items_to_update": [
            _parse_json_update_operation(item, line_number=line_number)
            for item in operations["update"]
        ],
    }


def validate_v4_document(
    *,
    role: str,
    mode_label: str,
    parsed_response: dict[str, Any],
    raw_response_trace_path: str | Path | None = None,
) -> None:
    normalized_role = _normalize_role(role)
    raw_response_trace_path = str(raw_response_trace_path or "").strip()
    raw_document = str(
        parsed_response.get("raw_response")
        or parsed_response.get("document_text")
        or ""
    )
    _reject_machine_protocol_in_document(raw_document)
    _reject_h1_headings(
        raw_document,
        role=normalized_role,
        mode_label=mode_label,
        raw_response_trace_path=raw_response_trace_path,
    )
    sections = parsed_response.get("sections") or {}
    allowed_headings = {
        _normalize_heading(heading)
        for heading in _V4_REQUIRED_SECTIONS[normalized_role]
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

    for heading in _V4_REQUIRED_SECTIONS[normalized_role]:
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

    if normalized_role == "tech":
        architecture_notes = _get_section_by_normalized_heading(sections, "Architecture Notes")
        mermaid_block = _extract_subsection(architecture_notes, "Mermaid Diagram")
        if not mermaid_block.strip() or "```mermaid" not in mermaid_block:
            raise ValueError(
                _format_document_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    section_name="Architecture Notes > Mermaid Diagram",
                    detail="subsection must contain a fenced Mermaid block",
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
    allow_creates: bool = True,
    allow_updates: bool = True,
    existing_item_ids: set[str] | None = None,
    existing_items_by_id: dict[str, dict[str, Any]] | None = None,
) -> None:
    normalized_role = str(role).strip().lower() or "unknown"
    raw_response_trace_path = str(raw_response_trace_path or "").strip()
    if allowed_create_types is None:
        normalized_allowed_create_types = set(ALLOWED_ITEM_TYPES)
    else:
        normalized_allowed_create_types = {
            str(value).strip().upper()
            for value in allowed_create_types
        }
    existing_item_ids = {
        str(item_id).strip().upper()
        for item_id in (existing_item_ids or set())
        if str(item_id).strip()
    }
    normalized_existing_items = {
        str(item_id).strip().upper(): item
        for item_id, item in (existing_items_by_id or {}).items()
        if str(item_id).strip()
    }
    current_role_target = _role_to_routing_target(normalized_role)

    if not allow_creates and parsed_response.get("items_to_create", []):
        first_item = parsed_response["items_to_create"][0]
        raise ValueError(
            _format_item_validation_error(
                role=normalized_role,
                mode_label=mode_label,
                field_name="create",
                invalid_value="item creation",
                allowed_values=["no create operations in this phase"],
                raw_line=first_item.get("raw_line", ""),
                raw_response_trace_path=raw_response_trace_path,
            )
        )

    for item in parsed_response.get("items_to_create", []):
        item_type = str(item.get("type", "")).strip().upper()
        if _looks_like_item_id(item_type):
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="type",
                    invalid_value=item_type,
                    allowed_values=sorted(normalized_allowed_create_types),
                    raw_line=item.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
        if item_type not in normalized_allowed_create_types:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="type",
                    invalid_value=item.get("type", ""),
                    allowed_values=sorted(normalized_allowed_create_types),
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
        if "EXTERNAL" in targets and targets != ["EXTERNAL"]:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="targets",
                    invalid_value=", ".join(targets),
                    allowed_values=["EXTERNAL alone", "PRODUCT", "GROWTH", "TECH", "ALL"],
                    raw_line=item.get("raw_line", ""),
                    raw_response_trace_path=raw_response_trace_path,
                )
            )
        if current_role_target and targets == [current_role_target]:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="targets",
                    invalid_value=", ".join(targets),
                    allowed_values=["another role", "ALL", "EXTERNAL when no agent can decide"],
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
        existing_item = normalized_existing_items.get(item_id, {})
        existing_targets = [
            str(target).strip().upper()
            for target in existing_item.get("targets", [])
            if str(target).strip()
        ]
        if existing_targets == ["EXTERNAL"]:
            raise ValueError(
                _format_item_validation_error(
                    role=normalized_role,
                    mode_label=mode_label,
                    field_name="id",
                    invalid_value=item_id,
                    allowed_values=["non-EXTERNAL item id"],
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


def _parse_json_create_operation(item: Any, *, line_number: int) -> dict[str, Any]:
    if not isinstance(item, dict):
        raise ValueError("BLACKBOARD_OPERATIONS.create items must be objects.")
    allowed_keys = {"type", "targets", "priority", "tags", "title", "content"}
    actual_keys = set(item)
    unknown_keys = actual_keys - allowed_keys
    missing_keys = allowed_keys - actual_keys
    if unknown_keys:
        raise ValueError(
            "Unexpected create operation field: "
            + ", ".join(sorted(str(key) for key in unknown_keys))
        )
    if missing_keys:
        raise ValueError(
            "Missing create operation field: "
            + ", ".join(sorted(str(key) for key in missing_keys))
        )
    if not isinstance(item["targets"], list):
        raise ValueError("Create operation targets must be a list.")
    if not isinstance(item["tags"], list):
        raise ValueError("Create operation tags must be a list.")
    return {
        "type": str(item["type"]).strip().upper(),
        "targets": [
            str(target).strip().upper()
            for target in item["targets"]
            if str(target).strip()
        ],
        "priority": str(item["priority"]).strip().upper(),
        "tags": [str(tag).strip() for tag in item["tags"] if str(tag).strip()],
        "title": str(item["title"]).strip(),
        "content": str(item["content"]).strip(),
        "raw_line": json.dumps(item, ensure_ascii=False, sort_keys=True),
        "line_number": line_number,
    }


def _parse_json_update_operation(item: Any, *, line_number: int) -> dict[str, Any]:
    if not isinstance(item, dict):
        raise ValueError("BLACKBOARD_OPERATIONS.update items must be objects.")
    allowed_keys = {"id", "status"}
    actual_keys = set(item)
    unknown_keys = actual_keys - allowed_keys
    missing_keys = allowed_keys - actual_keys
    if unknown_keys:
        raise ValueError(
            "Unexpected update operation field: "
            + ", ".join(sorted(str(key) for key in unknown_keys))
        )
    if missing_keys:
        raise ValueError(
            "Missing update operation field: "
            + ", ".join(sorted(str(key) for key in missing_keys))
        )
    return {
        "id": str(item["id"]).strip().upper(),
        "status": str(item["status"]).strip().upper(),
        "raw_line": json.dumps(item, ensure_ascii=False, sort_keys=True),
        "line_number": line_number,
    }


def _reject_machine_protocol_in_document(text: str) -> None:
    forbidden_markers = {
        "blackboard",
        "blackboard assignment",
        "blackboard operations",
        "blackboard output",
        "blackboard output contract",
        "blackboard items to create",
        "blackboard items to update",
    }
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        normalized = _normalize_heading(stripped).replace("_", " ")
        if stripped == _BLACKBOARD_JSON_MARKER or normalized in forbidden_markers:
            raise ValueError(
                "V4 documents must not contain blackboard operation protocol "
                f"(line {line_number}: {stripped})"
            )


def _reject_h1_headings(
    text: str,
    *,
    role: str,
    mode_label: str,
    raw_response_trace_path: str,
) -> None:
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if _H1_HEADING_PATTERN.match(stripped):
            raise ValueError(
                _format_document_validation_error(
                    role=role,
                    mode_label=mode_label,
                    section_name=stripped,
                    detail=f"unsupported heading level at line {line_number}; use only declared ## sections",
                    raw_response_trace_path=raw_response_trace_path,
                )
            )


def _validate_v4_readiness_section(
    *,
    role: str,
    mode_label: str,
    section_name: str,
    section_text: str,
    raw_response_trace_path: str,
) -> None:
    status_lines = [
        re.sub(r"^[-*]\s+", "", line.strip())
        for line in section_text.splitlines()
        if re.sub(r"^[-*]\s+", "", line.strip()).lower().startswith("status:")
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
    normalized_lines = [
        re.sub(r"^[-*]\s+", "", line.strip()).lower()
        for line in section_text.splitlines()
    ]
    if "blocking gaps:" not in normalized_lines:
        raise ValueError(
            _format_document_validation_error(
                role=role,
                mode_label=mode_label,
                section_name=section_name,
                detail="missing literal 'Blocking Gaps:' label",
                raw_response_trace_path=raw_response_trace_path,
            )
        )
    if "required improvements:" not in normalized_lines:
        raise ValueError(
            _format_document_validation_error(
                role=role,
                mode_label=mode_label,
                section_name=section_name,
                detail="missing literal 'Required Improvements:' label",
                raw_response_trace_path=raw_response_trace_path,
            )
        )


def _extract_subsection(text: str, subsection_heading: str) -> str:
    capture = False
    captured: list[str] = []
    target_heading = _normalize_heading(subsection_heading)
    for line in text.splitlines():
        stripped = line.strip()
        match = _SUBSECTION_HEADING_PATTERN.match(stripped)
        if match:
            heading = _normalize_heading(match.group(1))
            if capture and heading != target_heading:
                break
            capture = heading == target_heading
            continue
        if capture:
            captured.append(line)
    return "\n".join(captured).strip()


def _is_placeholder_only_section(text: str) -> bool:
    meaningful_lines = _meaningful_lines(text)
    return bool(meaningful_lines) and all(
        _normalize_placeholder_line(line) in _V4_PLACEHOLDER_TEXTS
        for line in meaningful_lines
    )


def _first_placeholder_line(text: str) -> str:
    for line in _meaningful_lines(text):
        normalized = _normalize_placeholder_line(line)
        if normalized in _V4_PLACEHOLDER_TEXTS:
            return f"placeholder-only content '{line.strip()}'"
    return "placeholder-only content"


def _meaningful_lines(text: str) -> list[str]:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("### "):
            continue
        stripped = re.sub(r"^[-*]\s+", "", stripped).strip()
        if stripped:
            lines.append(stripped)
    return lines


def _get_section_by_normalized_heading(sections: dict[str, str], heading: str) -> str:
    normalized_heading = _normalize_heading(heading)
    for section_heading, section_text in sections.items():
        if _normalize_heading(section_heading) == normalized_heading:
            return section_text
    return ""


def _normalize_heading(value: str) -> str:
    value = value.strip().strip("#").strip().rstrip(":")
    return re.sub(r"\s+", " ", value).lower()


def _normalize_role(role: str) -> str:
    normalized = str(role).strip().lower()
    if normalized not in _V4_REQUIRED_SECTIONS:
        raise ValueError(f"Unknown V4 role: {role}")
    return normalized


def _normalize_placeholder_line(line: str) -> str:
    stripped = re.sub(r"^[-*]\s+", "", line.strip())
    return re.sub(r"[.?!]+$", "", stripped).strip().lower()


def _looks_like_item_id(value: str) -> bool:
    return bool(re.match(r"^ITEM-\d+$", str(value).strip().upper()))


def _role_to_routing_target(role: str) -> str:
    role = role.strip().upper()
    if role in {"PRODUCT", "GROWTH", "TECH"}:
        return role
    return ""


def _format_document_validation_error(
    *,
    role: str,
    mode_label: str,
    section_name: str,
    detail: str,
    raw_response_trace_path: str,
) -> str:
    trace = f" Raw trace: {raw_response_trace_path}." if raw_response_trace_path else ""
    return (
        f"V4 {role} {mode_label} document validation failed in section "
        f"'{section_name}': {detail}.{trace}"
    )


def _format_item_validation_error(
    *,
    role: str,
    mode_label: str,
    field_name: str,
    invalid_value: Any,
    allowed_values: list[str],
    raw_line: str,
    raw_response_trace_path: str,
) -> str:
    trace = f" Raw trace: {raw_response_trace_path}." if raw_response_trace_path else ""
    return (
        f"V4 {role} {mode_label} item validation failed for field '{field_name}': "
        f"invalid value '{invalid_value}'. Allowed values: {', '.join(allowed_values)}. "
        f"Raw line: {raw_line}.{trace}"
    )
