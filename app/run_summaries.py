from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from typing import Any

if __package__ and __package__.startswith("app"):
    from .llm import call_llm
    from .run_store import RunWorkspace, read_text_file, write_text_file
else:
    from llm import call_llm
    from run_store import RunWorkspace, read_text_file, write_text_file


SUMMARY_PROMPT_PATH = Path(__file__).resolve().parent / "prompts V4" / "summary_prompt.md"
SUMMARY_REQUIRED_FIELDS = (
    "source_document",
    "source_hash",
    "scope",
    "key_decisions",
    "unresolved_questions",
    "critical_risks",
)
SUMMARY_LIST_FIELDS = {
    "key_decisions",
    "unresolved_questions",
    "critical_risks",
}
SUMMARY_ALLOWED_FIELDS = set(SUMMARY_REQUIRED_FIELDS)


def generate_summary(
    run: RunWorkspace,
    source_document_path: str | Path,
    llm_call=call_llm,
) -> dict[str, Any]:
    source_path = _resolve_source_document_path(run, source_document_path)
    source_document = read_text_file(source_path)
    source_hash = sha256(source_document.encode("utf-8")).hexdigest()
    run_root = run.root.resolve()
    source_relative_path = source_path.relative_to(run_root)

    system_prompt = _load_summary_prompt()
    user_prompt = _build_user_prompt(run, source_relative_path, source_document, source_hash)
    response_text = llm_call(system_prompt, user_prompt)
    raw_trace_path = _summary_raw_trace_path(run, source_relative_path)
    write_text_file(raw_trace_path, response_text)
    try:
        summary = _parse_summary_response(response_text)
    except ValueError as exc:
        raise ValueError(
            _format_summary_error(
                stage="parsing",
                source_path=source_relative_path,
                expected_source_hash=source_hash,
                raw_trace_path=raw_trace_path,
                detail=str(exc),
            )
        ) from exc
    try:
        validated = _validate_summary(
            summary,
            expected_source=str(source_relative_path),
            expected_source_hash=source_hash,
        )
    except ValueError as exc:
        raise ValueError(
            _format_summary_error(
                stage="validation",
                source_path=source_relative_path,
                expected_source_hash=source_hash,
                raw_trace_path=raw_trace_path,
                detail=str(exc),
            )
        ) from exc
    summary_path = _summary_path(run, source_relative_path)
    write_text_file(summary_path, _render_summary_yaml(validated))
    return validated


def _load_summary_prompt() -> str:
    if not SUMMARY_PROMPT_PATH.exists():
        raise FileNotFoundError(f"Missing V4 summary prompt: {SUMMARY_PROMPT_PATH}")
    return SUMMARY_PROMPT_PATH.read_text(encoding="utf-8").strip()


def _build_user_prompt(
    run: RunWorkspace,
    source_path: Path,
    source_document: str,
    source_hash: str,
) -> str:
    return (
        "Source document only. Do not invent missing information.\n\n"
        f"Run id:\n{run.run_id}\n\n"
        f"Source document:\n{source_path}\n\n"
        f"Source hash:\n{source_hash}\n\n"
        f"Source content:\n{source_document}"
    )


def _resolve_source_document_path(run: RunWorkspace, source_document_path: str | Path) -> Path:
    path = Path(source_document_path)
    if not path.is_absolute():
        path = run.root / path
    path = path.resolve()
    run_root = run.root.resolve()
    try:
        path.relative_to(run_root)
    except ValueError as error:
        raise ValueError("source_document_path must be inside the run workspace") from error
    if not path.exists():
        raise FileNotFoundError(f"Missing source document: {path}")
    return path


def _summary_path(run: RunWorkspace, source_path: Path) -> Path:
    source_agent = source_path.parent.name
    return run.summaries_dir / f"{source_agent}-{source_path.stem}.summary.yaml"


def _summary_raw_trace_path(run: RunWorkspace, source_path: Path) -> Path:
    summary_outputs_dir = run.root / "summary_outputs"
    summary_outputs_dir.mkdir(parents=True, exist_ok=True)
    source_agent = source_path.parent.name
    base_name = f"{source_agent}-{source_path.stem}.summary.raw.yaml"
    candidate = summary_outputs_dir / base_name
    if not candidate.exists():
        return candidate
    index = 2
    while True:
        candidate = summary_outputs_dir / f"{source_agent}-{source_path.stem}_{index:02d}.summary.raw.yaml"
        if not candidate.exists():
            return candidate
        index += 1


def _parse_summary_response(text: str) -> dict[str, Any]:
    cleaned_text = _strip_code_fences(text)
    if not cleaned_text:
        raise ValueError("Summary output is empty")
    lines = cleaned_text.splitlines()
    index = _skip_blank_lines(lines, 0)
    if index >= len(lines) or lines[index].strip() != "summary:":
        raise ValueError("Summary output must contain exactly one root key: summary")
    index += 1

    summary: dict[str, Any] = {}
    while index < len(lines):
        index = _skip_blank_lines(lines, index)
        if index >= len(lines):
            break
        line = lines[index]
        if not line.startswith("  "):
            if line.strip().startswith("-"):
                raise ValueError("Summary list items must be nested under a summary field")
            raise ValueError("Summary output may only contain fields under the root key summary")
        stripped = line[2:]
        if stripped.lstrip().startswith("-"):
            raise ValueError("Summary list items must be nested under a summary field")
        field_name, separator, remainder = stripped.partition(":")
        field_name = field_name.strip()
        if not separator:
            raise ValueError("Summary fields must use 'name:' under summary")
        if field_name not in SUMMARY_ALLOWED_FIELDS:
            raise ValueError(f"Unexpected summary field: {field_name}")
        if field_name in summary:
            raise ValueError(f"Duplicate summary field: {field_name}")

        remainder = remainder.strip()
        if field_name == "scope":
            if remainder == "|":
                scope, index = _consume_block_scalar(lines, index, "scope")
                if not scope.strip():
                    raise ValueError("Summary field 'scope' must not be empty")
                summary[field_name] = scope
                continue
            if not remainder:
                raise ValueError("Summary field 'scope' must be a scalar or block scalar")
            summary[field_name] = remainder
            index += 1
            continue
        if field_name in SUMMARY_LIST_FIELDS:
            if remainder:
                raise ValueError(f"Summary field '{field_name}' must be a list")
            values, index, saw_item = _consume_summary_list(lines, index, field_name)
            if not saw_item:
                raise ValueError(f"Summary field '{field_name}' must contain at least one list item")
            summary[field_name] = values
            continue
        if not remainder:
            raise ValueError(f"Summary field '{field_name}' must be a scalar value")
        summary[field_name] = remainder
        index += 1

    return summary


def _validate_summary(
    summary: dict[str, Any],
    *,
    expected_source: str,
    expected_source_hash: str,
) -> dict[str, Any]:
    validated: dict[str, Any] = {}
    for field in SUMMARY_REQUIRED_FIELDS:
        if field not in summary:
            raise ValueError(f"Summary is missing required field: {field}")

    source_document = str(summary["source_document"]).strip()
    if source_document != expected_source:
        raise ValueError(
            "Summary source_document does not match the source path: "
            f"expected '{expected_source}', got '{source_document}'"
        )
    validated["source_document"] = source_document

    source_hash = str(summary["source_hash"]).strip()
    if source_hash != expected_source_hash:
        raise ValueError(
            "Summary source_hash does not match the source document: "
            f"expected '{expected_source_hash}', got '{source_hash}'"
        )
    validated["source_hash"] = source_hash

    scope = str(summary["scope"]).strip()
    if not scope:
        raise ValueError("Summary scope must not be empty")
    validated["scope"] = scope

    for field in ("key_decisions", "unresolved_questions", "critical_risks"):
        validated[field] = _normalize_string_list(summary[field])

    return validated


def _render_summary_yaml(summary: dict[str, Any]) -> str:
    lines = ["summary:"]
    lines.extend(_render_scalar_field("source_document", summary["source_document"]))
    lines.extend(_render_scalar_field("source_hash", summary["source_hash"]))
    lines.extend(_render_block_scalar_field("scope", summary["scope"]))
    lines.extend(_render_string_list_field("key_decisions", summary["key_decisions"]))
    lines.extend(_render_string_list_field("unresolved_questions", summary["unresolved_questions"]))
    lines.extend(_render_string_list_field("critical_risks", summary["critical_risks"]))
    return "\n".join(lines) + "\n"


def _render_scalar_field(name: str, value: str) -> list[str]:
    return [f"  {name}: {value}"]


def _render_block_scalar_field(name: str, value: str) -> list[str]:
    block = str(value).rstrip("\n")
    if not block:
        return [f"  {name}: |", "    "]
    return [f"  {name}: |", *[f"    {line}" if line else "    " for line in block.splitlines()]]


def _render_string_list_field(name: str, values: list[str]) -> list[str]:
    if not values:
        return [f"  {name}:", "    - None"]
    return [f"  {name}:", *[f"    - {value}" for value in values]]


def _consume_block_scalar(lines: list[str], index: int, key: str) -> tuple[str, int]:
    line = lines[index]
    stripped = line[2:]
    prefix = f"{key}:"
    if not stripped.startswith(prefix):
        raise ValueError(f"Expected {key} block in summary output")
    remainder = stripped.split(":", 1)[1].strip()
    index += 1
    if remainder and remainder != "|":
        return remainder, index

    block_lines: list[str] = []
    while index < len(lines):
        current = lines[index]
        if current.startswith("  ") and not current.startswith("    "):
            break
        if current.startswith("    "):
            block_lines.append(current[4:])
            index += 1
            continue
        if not current.strip():
            block_lines.append("")
            index += 1
            continue
            break
    return "\n".join(block_lines).rstrip("\n"), index


def _consume_summary_list(
    lines: list[str], index: int, key: str
) -> tuple[list[str], int, bool]:
    line = lines[index]
    stripped = line[2:]
    prefix = f"{key}:"
    if not stripped.startswith(prefix):
        raise ValueError(f"Expected {key} list in summary output")
    index += 1
    values: list[str] = []
    saw_item = False
    while index < len(lines):
        current = lines[index]
        if current.startswith("  ") and not current.startswith("    "):
            break
        if current.startswith("    "):
            item_text = current[4:]
            item_text = item_text.lstrip()
            if not item_text.startswith("- "):
                raise ValueError(
                    f"Summary field '{key}' must contain list bullets indented under the field"
                )
            saw_item = True
            value = item_text[2:].strip()
            if value and value.lower() != "none":
                values.append(value)
            index += 1
            continue
        if current.lstrip().startswith("-"):
            raise ValueError(
                f"Summary list items under '{key}' must be indented by at least four spaces"
            )
        if not current.strip():
            index += 1
            continue
        break
    return values, index, saw_item


def _normalize_string_list(values: Any) -> list[str]:
    if values is None:
        raise ValueError("Summary list fields must be lists of strings")
    if not isinstance(values, list):
        raise ValueError("Summary list fields must be lists of strings")
    normalized: list[str] = []
    for value in values:
        text = str(value).strip()
        if not text or text.lower() == "none":
            continue
        normalized.append(text)
    return normalized


def _strip_code_fences(text: str) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    if not lines:
        return ""
    if lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _skip_blank_lines(lines: list[str], index: int) -> int:
    while index < len(lines) and not lines[index].strip():
        index += 1
    return index


def _format_summary_error(
    *,
    stage: str,
    source_path: Path,
    expected_source_hash: str,
    raw_trace_path: Path,
    detail: str,
) -> str:
    return (
        f"Summary {stage} failed for source '{source_path}' "
        f"(expected hash {expected_source_hash}, raw trace {raw_trace_path}): {detail}"
    )
