from __future__ import annotations


def normalize_heading(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.lstrip("#").strip()
    return normalized


def split_section(text: str, headings: str | tuple[str, ...] | list[str]) -> tuple[str, str]:
    if not text.strip():
        return "", ""

    if isinstance(headings, str):
        heading_list = [headings]
    else:
        heading_list = list(headings)

    targets = {normalize_heading(heading) for heading in heading_list}
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if normalize_heading(line) in targets:
            return "\n".join(lines[:index]).strip(), "\n".join(lines[index:]).strip()
    return text.strip(), ""


def parse_solution_proposal_items(
    text: str,
    owner: str,
    source: str,
    correction_tasks: list[dict] | None = None,
) -> list[dict]:
    if not text.strip():
        return []

    blocks = _split_records(text, marker_prefix="problem")
    if not blocks:
        blocks = [text.strip()]

    items = []
    tasks = correction_tasks or []
    for index, block in enumerate(blocks):
        record = _parse_record_block(
            block,
            field_aliases={
                "problem": ("problem",),
                "owner": ("owner",),
                "option_a": ("option a", "option one", "option 1", "first option"),
                "option_b": ("option b", "option two", "option 2", "second option"),
                "tradeoffs": ("tradeoffs", "trade-offs", "trade off", "pros and cons"),
                "recommended_option": ("recommended option", "recommendation"),
                "required_information": ("required information", "missing information"),
                "suggested_next_validation": (
                    "suggested next validation",
                    "next validation",
                    "next step",
                ),
            },
            unresolved_markers=("no viable solution yet",),
        )
        task = tasks[index] if index < len(tasks) else {}
        record["owner"] = record.get("owner") or owner
        record["source"] = source
        record["mode"] = "correction" if tasks else "review"
        record["task"] = task.get("task", "")
        record["tag"] = task.get("tag", "")
        record["contributors"] = list(task.get("contributors", []))
        record["problem"] = record.get("problem") or task.get("problem") or task.get("task", "")
        record["status"] = record.get("status") or ("unresolved" if not record.get("recommended_option") else "proposed")
        record["parsed"] = bool(
            record.get("problem")
            or record.get("option_a")
            or record.get("option_b")
            or record.get("tradeoffs")
            or record.get("recommended_option")
            or record.get("required_information")
        )
        record["raw"] = block.strip()
        items.append(record)
    return items


def parse_solution_decision_items(
    text: str,
    source: str,
    correction_tasks: list[dict] | None = None,
) -> list[dict]:
    if not text.strip():
        return []

    blocks = _split_records(text, marker_prefix="problem")
    if not blocks:
        blocks = [text.strip()]

    items = []
    tasks = correction_tasks or []
    for index, block in enumerate(blocks):
        record = _parse_record_block(
            block,
            field_aliases={
                "problem": ("problem",),
                "chosen_option": ("chosen option",),
                "decision": ("decision",),
                "reason": ("reason",),
                "impact_on_mvp": ("impact on mvp",),
                "required_information": ("required information",),
                "suggested_next_validation": (
                    "suggested next validation",
                    "next validation",
                    "next step",
                ),
            },
            unresolved_markers=("no viable solution yet",),
        )
        task = tasks[index] if index < len(tasks) else {}
        record["source"] = source
        record["mode"] = "correction" if tasks else "review"
        record["task"] = task.get("task", "")
        record["tag"] = task.get("tag", "")
        record["contributors"] = list(task.get("contributors", []))
        record["problem"] = record.get("problem") or task.get("problem") or task.get("task", "")
        record["parsed"] = bool(
            record.get("problem")
            or record.get("chosen_option")
            or record.get("decision")
            or record.get("reason")
            or record.get("impact_on_mvp")
            or record.get("required_information")
        )
        record["raw"] = block.strip()
        items.append(record)
    return items


def _split_records(text: str, marker_prefix: str) -> list[str]:
    blocks = []
    current = []
    seen_record = False
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            if seen_record and current:
                current.append("")
            continue

        normalized = normalize_heading(stripped)
        if normalized in {"solution proposals", "solution proposal", "solution arbitration"}:
            continue

        if normalized.startswith(marker_prefix):
            if seen_record and current:
                block = "\n".join(current).strip()
                if block:
                    blocks.append(block)
            current = [line]
            seen_record = True
            continue

        if not seen_record:
            continue

        current.append(line)

    if current:
        block = "\n".join(current).strip()
        if block:
            blocks.append(block)
    return blocks


def _parse_record_block(
    block: str,
    field_aliases: dict[str, tuple[str, ...]],
    unresolved_markers: tuple[str, ...] = (),
) -> dict:
    record = {field: "" for field in field_aliases}
    record["status"] = ""
    record["raw"] = block.strip()
    record["parsed"] = False

    current_field = ""
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        normalized = normalize_heading(line)
        if normalized in {"solution proposals", "solution proposal", "solution arbitration"}:
            continue

        if any(normalized.startswith(marker) for marker in unresolved_markers):
            record["status"] = "unresolved"
            inline = _extract_inline_value(line)
            if inline and not record.get("required_information"):
                record["required_information"] = inline
            current_field = ""
            continue

        matched_field = _match_field(normalized, field_aliases)
        if matched_field:
            value = _extract_inline_value(line)
            if value:
                record[matched_field] = _append_text(record.get(matched_field, ""), value)
            current_field = matched_field
            continue

        list_item = _extract_list_item(line)
        if list_item:
            if current_field:
                record[current_field] = _append_text(record.get(current_field, ""), list_item)
            elif not record.get("problem"):
                record["problem"] = list_item
            continue

        if current_field:
            record[current_field] = _append_text(record.get(current_field, ""), line)
        elif not record.get("problem"):
            record["problem"] = line

    if not record.get("problem"):
        record["problem"] = _first_meaningful_line(block)

    record["parsed"] = bool(
        record.get("problem")
        or record.get("chosen_option")
        or record.get("decision")
        or record.get("option_a")
        or record.get("option_b")
        or record.get("tradeoffs")
        or record.get("reason")
        or record.get("required_information")
        or record.get("recommended_option")
    )
    return record


def _match_field(normalized_line: str, field_aliases: dict[str, tuple[str, ...]]) -> str:
    for field, aliases in field_aliases.items():
        for alias in aliases:
            if normalized_line.startswith(alias):
                return field
    return ""


def _extract_inline_value(line: str) -> str:
    if ":" not in line:
        return ""
    value = line.split(":", 1)[1].strip()
    return value if value and value.lower() != "none" else ""


def _extract_list_item(line: str) -> str:
    if line.startswith("- "):
        value = line[2:].strip()
    elif line.startswith("* "):
        value = line[2:].strip()
    elif ". " in line:
        prefix, value = line.split(". ", 1)
        if prefix.isdigit():
            value = value.strip()
        else:
            return ""
    else:
        return ""

    if value and value.lower() != "none":
        return value
    return ""


def _append_text(existing: str, addition: str) -> str:
    pieces = [piece for piece in (existing, addition) if piece]
    if not pieces:
        return ""
    return " ".join(pieces).strip()


def _first_meaningful_line(text: str) -> str:
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        return stripped
    return ""
