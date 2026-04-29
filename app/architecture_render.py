from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


def render_architecture_diagram(output_dir: Path, blackboard: dict) -> dict:
    """Render Mermaid architecture artifacts from the Tech output."""
    mermaid_source = blackboard.get("mermaid_diagram", "").strip()
    if not mermaid_source:
        mermaid_source = _extract_mermaid_diagram(blackboard.get("architecture_notes", ""))
    if mermaid_source:
        blackboard["mermaid_diagram"] = mermaid_source

    image_state = _render_mermaid_image(output_dir, mermaid_source)
    return _assess_diagram_quality(mermaid_source, image_state, blackboard)


def _render_mermaid_image(output_dir: Path, mermaid_source: str) -> dict:
    mmd_path = output_dir / "architecture-diagram.mmd"
    png_path = output_dir / "architecture-diagram.png"
    state = {
        "source_path": "",
        "image_path": "",
        "image_ready": False,
        "render_warning": "",
    }
    if not mermaid_source:
        state["render_warning"] = "No Mermaid diagram found in the Tech output."
        return state

    mmd_path.write_text(mermaid_source + "\n", encoding="utf-8")
    state["source_path"] = str(mmd_path)
    mmdc_path = _find_mmdc()
    if not mmdc_path:
        state["render_warning"] = (
            "Mermaid source written, but PNG was not generated because `mmdc` is not installed."
        )
        return state

    command = [
        mmdc_path,
        "-i",
        str(mmd_path),
        "-o",
        str(png_path),
        "-b",
        "transparent",
    ]
    puppeteer_config = _project_root() / "mermaid-puppeteer-config.json"
    if puppeteer_config.exists():
        command.extend(["-p", str(puppeteer_config)])
    try:
        subprocess.run(command, check=True, capture_output=True, text=True, timeout=45)
    except (OSError, subprocess.SubprocessError) as error:
        state["render_warning"] = f"Mermaid PNG generation failed: {error}"
        return state

    state["image_path"] = str(png_path)
    state["image_ready"] = png_path.exists() and png_path.stat().st_size > 0
    if not state["image_ready"]:
        state["render_warning"] = "Mermaid PNG generation finished without creating a non-empty image."
    return state


def _find_mmdc() -> str:
    local_mmdc = _project_root() / "node_modules" / ".bin" / "mmdc"
    if local_mmdc.exists():
        return str(local_mmdc)
    return shutil.which("mmdc") or ""


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _assess_diagram_quality(mermaid_source: str, image_state: dict, blackboard: dict) -> dict:
    warning = image_state.get("render_warning", "")
    return {
        "architecture_visual_ready": bool(image_state.get("image_ready")),
        "architecture_visual_warning": warning,
        "architecture_markdown_ready": bool(blackboard.get("architecture_notes", "").strip()),
        "architecture_mermaid_ready": bool(mermaid_source),
        "architecture_mermaid_source": image_state.get("source_path", ""),
        "architecture_image_ready": bool(image_state.get("image_ready")),
        "architecture_image_path": image_state.get("image_path", ""),
    }


def _extract_mermaid_diagram(text: str) -> str:
    section = _extract_section(text, ["mermaid diagram"])
    fenced = _extract_mermaid_code_block(section)
    if fenced:
        return fenced
    return _extract_mermaid_code_block(text)


def _extract_mermaid_code_block(text: str) -> str:
    lines = text.splitlines()
    capture = False
    collected = []
    for line in lines:
        stripped = line.strip()
        if not capture and stripped.startswith("```") and "mermaid" in stripped.lower():
            capture = True
            continue
        if capture and stripped.startswith("```"):
            break
        if capture:
            collected.append(line.rstrip())
    return "\n".join(collected).strip()


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


def _normalize_heading(value: str) -> str:
    normalized = value.lower().strip()
    normalized = re.sub(r"[/_]+", " ", normalized)
    normalized = re.sub(r"^[-*]\s+", "", normalized)
    normalized = re.sub(r"^\d+[.)]\s+", "", normalized)
    normalized = normalized.lstrip("#").strip()
    normalized = normalized.strip("*`_ ")
    normalized = re.sub(r"[:#*`_\\-]+$", "", normalized)
    normalized = normalized.strip("*`_ ")
    return normalized
