from __future__ import annotations

import re


READY_STATUSES = {"READY", "LIMITED", "INSUFFICIENT"}

_TAG_HINTS = {
    "privacy_trust": ("privacy", "trust", "permission", "consent", "confidential", "sensitive"),
    "demand_validation": ("demand", "interest", "willingness", "traction", "adoption", "validate"),
    "data_access": ("data access", "access", "permission", "integration", "permissions"),
    "quality_assurance": ("quality", "vetting", "moderation", "review", "submission", "abuse"),
    "market_motion": ("acquisition", "market", "pilot", "activation", "repeatability", "channel"),
    "metrics_validation": ("metric", "metrics", "success", "measurement", "kpi", "target"),
    "onboarding": ("onboarding", "usability", "training", "education", "first-time", "setup"),
    "scope": ("scope", "wedge", "segment", "mvp", "business model", "recommendation"),
    "operations": ("ops", "operational", "workflow", "handoff", "support", "process"),
    "compliance": ("compliance", "legal", "regulatory", "hipaa", "gdpr", "policy"),
}


def create_empty_readiness_block() -> dict:
    return {
        "status": "",
        "blocking_gaps": [],
        "required_improvements": [],
        "known_tags": [],
        "tag_registry": {},
        "parse_warning": "",
    }


def parse_readiness_block(
    text: str, headings: str | list[str], known_tags: list[str] | None = None
) -> dict:
    if isinstance(headings, str):
        headings = [headings]

    section = _extract_section(text, headings)
    readiness = create_empty_readiness_block()
    if not section:
        if known_tags:
            readiness["known_tags"] = _dedupe_tags(known_tags)
        readiness["parse_warning"] = "Readiness block missing or empty."
        return readiness

    active_bucket = ""
    known_tag_set = set(_dedupe_tags(known_tags or []))
    tag_registry: dict[str, dict] = {}

    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        normalized = _normalize_label(line)
        if line.lower().startswith("status:"):
            status = _extract_status_value(line)
            if status:
                readiness["status"] = status
            continue

        if normalized == "blocking gaps" or line.lower().startswith("blocking gaps:"):
            active_bucket = "blocking_gaps"
            inline_item = _extract_inline_value(line)
            if inline_item:
                item = _parse_tagged_item(
                    inline_item,
                    known_tag_set,
                    readiness["tag_registry"],
                )
                _append_item(readiness, active_bucket, item)
                _register_item(tag_registry, item, active_bucket)
            continue

        if normalized == "required improvements" or line.lower().startswith("required improvements:"):
            active_bucket = "required_improvements"
            inline_item = _extract_inline_value(line)
            if inline_item:
                item = _parse_tagged_item(
                    inline_item,
                    known_tag_set,
                    readiness["tag_registry"],
                )
                _append_item(readiness, active_bucket, item)
                _register_item(tag_registry, item, active_bucket)
            continue

        item_text = _extract_list_item(line)
        if item_text and active_bucket:
            item = _parse_tagged_item(
                item_text,
                known_tag_set,
                readiness["tag_registry"],
            )
            _append_item(readiness, active_bucket, item)
            _register_item(tag_registry, item, active_bucket)
            continue

        if active_bucket and not line.startswith("#"):
            item = _parse_tagged_item(
                line,
                known_tag_set,
                readiness["tag_registry"],
            )
            _append_item(readiness, active_bucket, item)
            _register_item(tag_registry, item, active_bucket)

    readiness["known_tags"] = _dedupe_tags(
        list(known_tag_set)
        + list(tag_registry.keys())
        + [item["tag"] for item in readiness["blocking_gaps"]]
        + [item["tag"] for item in readiness["required_improvements"]]
    )
    readiness["tag_registry"] = tag_registry
    if not readiness["status"]:
        readiness["parse_warning"] = "Readiness status missing or unparsable."
    elif not readiness["blocking_gaps"] and not readiness["required_improvements"]:
        readiness["parse_warning"] = "Readiness block parsed but contained no actionable items."
    return readiness


def aggregate_global_readiness(readiness_blocks: dict[str, dict]) -> dict:
    statuses = [
        _normalize_status(readiness_blocks.get(role, {}).get("status", ""))
        for role in ("product", "tech", "growth")
    ]

    if any(status == "INSUFFICIENT" for status in statuses):
        global_status = "INSUFFICIENT"
    elif any(status == "LIMITED" for status in statuses):
        global_status = "LIMITED"
    elif all(status == "READY" for status in statuses):
        global_status = "READY"
    else:
        global_status = ""

    blocking_gaps = _dedupe_tagged_items(
        item
        for role in ("product", "tech", "growth")
        for item in readiness_blocks.get(role, {}).get("blocking_gaps", [])
    )
    required_improvements = _dedupe_tagged_items(
        item
        for role in ("product", "tech", "growth")
        for item in readiness_blocks.get(role, {}).get("required_improvements", [])
    )
    known_tags = _dedupe_tags(
        tag
        for role in ("product", "tech", "growth")
        for tag in readiness_blocks.get(role, {}).get("known_tags", [])
    )

    return {
        "status": global_status,
        "blocking_gaps": blocking_gaps,
        "required_improvements": required_improvements,
        "known_tags": known_tags,
    }


def group_tagged_items(items: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    for item in items:
        tag = _normalize_tag(item.get("tag", "untagged"))
        if tag not in grouped:
            grouped[tag] = []
            order.append(tag)
        grouped[tag].append(item)
    return [{"tag": tag, "items": grouped[tag]} for tag in order]


def render_tagged_item(item: dict) -> str:
    tag = _normalize_tag(item.get("tag", "untagged"))
    text = item.get("text", "").strip()
    if tag and tag != "untagged":
        return f"[{tag}] {text}"
    return text


def _append_item(readiness: dict, bucket: str, item: dict) -> None:
    readiness[bucket].append(item)


def _register_item(tag_registry: dict[str, dict], item: dict, bucket: str) -> None:
    tag = _normalize_tag(item.get("tag", "untagged"))
    entry = tag_registry.setdefault(tag, {"count": 0, "buckets": [], "samples": []})
    entry["count"] += 1
    if bucket not in entry["buckets"]:
        entry["buckets"].append(bucket)
    if item.get("text") and item["text"] not in entry["samples"]:
        entry["samples"].append(item["text"])


def _parse_tagged_item(
    raw_text: str, known_tags: set[str], tag_registry: dict[str, dict]
) -> dict:
    text = raw_text.strip()
    if not text:
        return {"tag": "untagged", "text": ""}

    explicit_tag, stripped_text = _split_explicit_tag(text)
    if explicit_tag:
        tag = _normalize_tag(explicit_tag)
        resolved_text = stripped_text
    else:
        resolved_text = text
        tag = _infer_tag_from_text(resolved_text, known_tags, tag_registry)

    tag = _normalize_tag(tag) or "untagged"
    resolved_text = _strip_trailing_tag_suffix(resolved_text, tag)
    if tag != "untagged":
        known_tags.add(tag)
    return {"tag": tag, "text": resolved_text}


def _infer_tag_from_text(
    text: str, known_tags: set[str], tag_registry: dict[str, dict]
) -> str:
    normalized_text = _normalize_text(text)

    for tag in _dedupe_tags(list(known_tags) + list(tag_registry.keys())):
        if _tag_matches_text(tag, normalized_text):
            return tag

    for tag, keywords in _TAG_HINTS.items():
        if any(keyword in normalized_text for keyword in keywords):
            return tag

    if any(term in normalized_text for term in ("privacy", "trust", "permission", "consent")):
        return "privacy_trust"
    if any(term in normalized_text for term in ("demand", "interest", "traction", "adoption")):
        return "demand_validation"
    if any(term in normalized_text for term in ("metric", "success", "measure")):
        return "metrics_validation"
    if any(term in normalized_text for term in ("onboarding", "training", "usability")):
        return "onboarding"
    if any(term in normalized_text for term in ("scope", "wedge", "mvp", "segment")):
        return "scope"

    return "untagged"


def _tag_matches_text(tag: str, normalized_text: str) -> bool:
    tag = _normalize_tag(tag)
    if not tag:
        return False

    if tag in _TAG_HINTS:
        return any(keyword in normalized_text for keyword in _TAG_HINTS[tag])

    tag_parts = [part for part in tag.split("_") if part]
    if tag_parts and all(part in normalized_text for part in tag_parts):
        return True
    return tag in normalized_text


def _split_explicit_tag(text: str) -> tuple[str, str]:
    match = re.match(r"^\[([a-zA-Z0-9_]+)\]\s*(.+)$", text)
    if not match:
        return "", text
    return match.group(1), match.group(2).strip()


def _dedupe_tagged_items(items) -> list[dict]:
    result = []
    seen = set()
    for item in items:
        tag = _normalize_tag(item.get("tag", "untagged"))
        text = item.get("text", "").strip()
        key = (tag, _normalize_text(text))
        if not text or key in seen:
            continue
        seen.add(key)
        result.append({"tag": tag, "text": text})
    return result


def _extract_section(text: str, headings: list[str]) -> str:
    lines = text.splitlines()
    capture = False
    collected = []
    target_headings = {heading.strip().lower() for heading in headings}
    for line in lines:
        stripped = line.strip()
        if not capture and stripped.lower() in target_headings:
            capture = True
            continue
        if capture and stripped.startswith("## "):
            break
        if capture:
            collected.append(line)
    return "\n".join(collected).strip()


def _extract_status_value(line: str) -> str:
    if ":" not in line:
        return ""
    value = line.split(":", 1)[1].strip().upper()
    return value if value in READY_STATUSES else ""


def _extract_list_item(line: str) -> str:
    if line.startswith("- "):
        return line[2:].strip()
    if line.startswith("* "):
        return line[2:].strip()
    match = re.match(r"^\d+[.)]\s+(.*)$", line)
    if match:
        return match.group(1).strip()
    return ""


def _extract_inline_value(line: str) -> str:
    if ":" not in line:
        return ""
    value = line.split(":", 1)[1].strip()
    return value if value else ""


def _normalize_label(line: str) -> str:
    normalized = line.strip().lower()
    normalized = normalized.lstrip("#").strip()
    return re.sub(r"[:#*\\-]+$", "", normalized)


def _normalize_status(value: str) -> str:
    normalized = value.strip().upper()
    return normalized if normalized in READY_STATUSES else ""


def _normalize_tag(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9_]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def _normalize_text(text: str) -> str:
    normalized = text.lower().strip()
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def _strip_trailing_tag_suffix(text: str, tag: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        return cleaned

    if tag and tag != "untagged":
        suffix_pattern = rf"(\s*\[{re.escape(tag)}\]\s*)+$"
        cleaned = re.sub(suffix_pattern, "", cleaned, flags=re.IGNORECASE).strip()

    cleaned = re.sub(r"(\s*\[[a-zA-Z0-9_]+\]\s*)+$", "", cleaned).strip()
    return cleaned


def _dedupe_tags(values) -> list[str]:
    result = []
    seen = set()
    for value in values:
        tag = _normalize_tag(value)
        if not tag or tag in seen:
            continue
        seen.add(tag)
        result.append(tag)
    return result
