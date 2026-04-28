from __future__ import annotations

import re
from pathlib import Path


PAGE_WIDTH = 792
PAGE_HEIGHT = 612
MARGIN = 24


def render_architecture_pdf(output_path: Path, project_name: str, blackboard: dict) -> dict:
    """Render a simple macro architecture PDF from the Tech output."""
    diagram = _build_diagram_data(blackboard)
    pdf_bytes = _build_pdf(project_name, diagram)
    output_path.write_bytes(pdf_bytes)
    return _assess_diagram_quality(diagram, blackboard)


def _build_diagram_data(blackboard: dict) -> dict[str, list[str]]:
    architecture_notes = blackboard.get("architecture_notes", "")
    diagram_blueprint = blackboard.get("diagram_blueprint", "")
    project_brief = blackboard.get("project_brief", "")

    blueprint_source = diagram_blueprint or _extract_section(
        architecture_notes, ["diagram blueprint"]
    )

    data = {
        "external_actors": _extract_blueprint_items(
            blueprint_source,
            ["external actors or systems", "external actors", "external systems"],
        ),
        "main_blocks": _extract_blueprint_items(
            blueprint_source,
            ["main system blocks", "main blocks", "system blocks"],
        ),
        "flows": _extract_blueprint_items(
            blueprint_source,
            ["main flows between blocks", "main flows", "flows"],
        ),
        "controls": _extract_blueprint_items(
            blueprint_source,
            [
                "admin or operations control points",
                "control points",
                "operations control points",
            ],
        ),
    }

    if not data["main_blocks"]:
        data["main_blocks"] = _collect_items_from_sections(
            architecture_notes,
            ["main modules or components", "what must be built now"],
        )
    if not data["controls"]:
        data["controls"] = _collect_items_from_sections(
            architecture_notes,
            ["control points, internal tools, or support needs"],
        )
    if not data["flows"]:
        data["flows"] = _collect_items_from_sections(
            architecture_notes,
            ["critical data or workflow states", "recommended implementation approach"],
        )
    if not data["external_actors"]:
        data["external_actors"] = _extract_actors_from_project_brief(project_brief)

    return {
        key: _dedupe(items, limit=5) for key, items in data.items()
    }


def _assess_diagram_quality(diagram: dict[str, list[str]], blackboard: dict) -> dict:
    missing_sections = [key for key, items in diagram.items() if not items]
    total_items = sum(len(items) for items in diagram.values())
    warning = ""
    if total_items == 0:
        warning = "Architecture visual fallback used: no diagram source items were detected."
    elif missing_sections:
        warning = "Architecture visual is partial; missing sections: " + ", ".join(missing_sections)
    return {
        "architecture_visual_ready": total_items > 0 and not (len(missing_sections) == 4),
        "architecture_visual_warning": warning,
        "architecture_markdown_ready": bool(blackboard.get("architecture_notes", "").strip()),
        "diagram_item_count": total_items,
        "missing_sections": missing_sections,
    }


def _extract_actors_from_project_brief(project_brief: str) -> list[str]:
    section = _extract_section(project_brief, ["target users"])
    items = _extract_bullets(section)
    if items:
        return items
    return ["Primary users", "Operations / support"]


def _build_pdf(project_name: str, diagram: dict[str, list[str]]) -> bytes:
    width = PAGE_WIDTH
    height = PAGE_HEIGHT
    content = _build_content_stream(project_name, diagram, width, height)
    content_bytes = content.encode("latin-1", errors="replace")
    objects = []
    objects.append("<< /Type /Catalog /Pages 2 0 R >>")
    objects.append("<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    objects.append(
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] "
        f"/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>"
    )
    objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    objects.append(f"<< /Length {len(content_bytes)} >>\nstream\n{content}\nendstream")

    pdf = bytearray()
    pdf.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{index} 0 obj\n".encode("ascii"))
        pdf.extend(obj.encode("latin-1", errors="replace"))
        pdf.extend(b"\nendobj\n")
    xref_offset = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    pdf.extend(
        (
            "trailer\n"
            f"<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            "startxref\n"
            f"{xref_offset}\n"
            "%%EOF\n"
        ).encode("ascii")
    )
    return bytes(pdf)


def _build_content_stream(project_name: str, diagram: dict[str, list[str]], width: int, height: int) -> str:
    lines = []
    lines.extend(_draw_text(28, height - 36, f"Architecture Diagram - {project_name}", 20, font="F2"))
    lines.extend(
        _draw_text(
            28,
            height - 58,
            "Macro architecture derived from the Tech output",
            10,
            font="F1",
        )
    )

    left_box = (24, 324, 200, 228)
    center_box = (244, 186, 308, 366)
    right_box = (576, 324, 192, 228)
    bottom_box = (24, 24, 744, 136)

    lines.extend(_draw_box(left_box, "External Actors / Systems", diagram["external_actors"]))
    lines.extend(_draw_box(right_box, "Admin / Ops Control Points", diagram["controls"]))
    lines.extend(_draw_flow_box(bottom_box, "Major Flows", diagram["flows"]))
    lines.extend(_draw_center_blocks(center_box, diagram["main_blocks"]))

    # Arrows indicating the broad directional flow.
    lines.extend(_draw_arrow(224, 438, 244, 438))
    lines.extend(_draw_arrow(552, 250, 576, 250))

    return "\n".join(lines)


def _draw_box(box: tuple[int, int, int, int], title: str, items: list[str]) -> list[str]:
    x, y, w, h = box
    content = []
    content.append(_rect(x, y, w, h))
    content.extend(_draw_text(x + 10, y + h - 18, title, 11, font="F2"))
    text_y = y + h - 36
    if not items:
        items = ["None"]
    for item in items[:4]:
        for line in _wrap_text(item, 26):
            content.extend(_draw_text(x + 10, text_y, f"- {line}", 9, font="F1"))
            text_y -= 12
        text_y -= 2
    return content


def _draw_flow_box(box: tuple[int, int, int, int], title: str, items: list[str]) -> list[str]:
    x, y, w, h = box
    content = []
    content.append(_rect(x, y, w, h))
    content.extend(_draw_text(x + 10, y + h - 18, title, 11, font="F2"))
    text_y = y + h - 36
    if not items:
        items = ["No explicit flow captured"]
    for index, item in enumerate(items[:5], start=1):
        for line in _wrap_text(item, 78):
            content.extend(_draw_text(x + 10, text_y, f"{index}. {line}", 8.5, font="F1"))
            text_y -= 11
        text_y -= 2
    return content


def _draw_center_blocks(box: tuple[int, int, int, int], items: list[str]) -> list[str]:
    x, y, w, h = box
    content = []
    content.append(_rect(x, y, w, h))
    content.extend(_draw_text(x + 10, y + h - 18, "Main System Blocks", 11, font="F2"))

    if not items:
        items = ["Core application", "Persistence layer", "Operations / controls"]

    block_height = 52
    gap = 10
    current_top = y + h - 40
    max_blocks = min(len(items), 5)
    centers = []
    for idx in range(max_blocks):
        block_y = current_top - block_height
        block_label = items[idx]
        content.append(_rect(x + 18, block_y, w - 36, block_height))
        lines = _wrap_text(block_label, 34)
        text_y = block_y + block_height / 2 + 4
        for line in lines[:2]:
            content.extend(
                _draw_text(x + 28, text_y, line, 9.5, font="F1")
            )
            text_y -= 11
        centers.append((x + w / 2, block_y + block_height / 2))
        current_top = block_y - gap

    for (x1, y1), (x2, y2) in zip(centers, centers[1:]):
        content.extend(_draw_arrow(int(x1), int(y1 - 26), int(x2), int(y2 + 26)))

    return content


def _draw_arrow(x1: int, y1: int, x2: int, y2: int) -> list[str]:
    dx = x2 - x1
    dy = y2 - y1
    angle = 0 if dx == 0 and dy == 0 else 18
    head_len = 8
    content = [
        f"0 0 0 RG",
        f"1 w",
        f"{x1} {y1} m {x2} {y2} l S",
        f"{x2} {y2} m {x2 - head_len} {y2 + head_len/2} l {x2 - head_len} {y2 - head_len/2} l h f",
    ]
    return content


def _rect(x: int, y: int, w: int, h: int) -> str:
    return f"0 0 0 RG 1 w {x} {y} {w} {h} re S"


def _draw_text(x: int, y_top: float, text: str, size: float, font: str = "F1") -> list[str]:
    safe = _escape_pdf_text(text)
    y = max(0, int(y_top))
    return [
        f"BT /{font} {size} Tf {x} {y} Td ({safe}) Tj ET",
    ]


def _wrap_text(text: str, max_chars: int) -> list[str]:
    cleaned = " ".join(text.split())
    if len(cleaned) <= max_chars:
        return [cleaned]
    words = cleaned.split(" ")
    lines = []
    current = []
    current_len = 0
    for word in words:
        extra = len(word) + (1 if current else 0)
        if current and current_len + extra > max_chars:
            lines.append(" ".join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len += extra
    if current:
        lines.append(" ".join(current))
    return lines


def _extract_section(text: str, headings: list[str]) -> str:
    lines = text.splitlines()
    capture = False
    collected = []
    targets = {heading.strip().lower() for heading in headings}
    for line in lines:
        stripped = line.strip()
        normalized = _normalize_heading(stripped)
        if not capture and normalized in targets:
            capture = True
            continue
        if capture and stripped.startswith("#"):
            break
        if capture:
            collected.append(line)
    return "\n".join(collected).strip()


def _extract_blueprint_items(section: str, labels: list[str]) -> list[str]:
    if not section:
        return []
    lines = section.splitlines()
    current = None
    collected = {label: [] for label in labels}
    label_targets = {label: _normalize_heading(label) for label in labels}
    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        normalized = _normalize_heading(stripped)
        matched_label = None
        for label, target in label_targets.items():
            if normalized.startswith(target):
                matched_label = label
                break
        if matched_label:
            current = matched_label
            inline = _inline_value(stripped)
            if inline:
                collected[current].append(inline)
            continue
        if stripped.startswith("#") and current is not None:
            break
        if current:
            item = _extract_list_item(stripped)
            if item:
                collected[current].append(item)
            elif not stripped.startswith("-") and not stripped.startswith("*"):
                # Continuation line for the current bucket.
                collected[current].append(stripped)

    merged = []
    for label in labels:
        merged.extend(collected[label])
    return merged


def _collect_items_from_sections(text: str, headings: list[str]) -> list[str]:
    items = []
    for heading in headings:
        section = _extract_section(text, [heading])
        items.extend(_extract_bullets(section))
    return items


def _extract_bullets(section: str) -> list[str]:
    items = []
    for line in section.splitlines():
        value = _extract_list_item(line.strip())
        if value:
            items.append(value)
    return items


def _extract_list_item(line: str) -> str:
    if line.startswith("- "):
        return line[2:].strip()
    if line.startswith("* "):
        return line[2:].strip()
    match = re.match(r"^\d+[.)]\s+(.*)$", line)
    if match:
        return match.group(1).strip()
    return ""


def _inline_value(line: str) -> str:
    if ":" not in line:
        return ""
    value = line.split(":", 1)[1].strip()
    return value


def _normalize_heading(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.lstrip("#").strip()
    normalized = re.sub(r"[:#*\\-]+$", "", normalized)
    return normalized


def _dedupe(items: list[str], limit: int = 5) -> list[str]:
    result = []
    seen = set()
    for item in items:
        cleaned = " ".join(item.split())
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        result.append(cleaned)
        if len(result) >= limit:
            break
    return result


def _escape_pdf_text(text: str) -> str:
    cleaned = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return cleaned.encode("ascii", errors="replace").decode("ascii")
