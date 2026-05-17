from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

if __package__ and __package__.startswith("app"):
    from .llm import call_llm_json
    from .run_store import RunWorkspace, read_text_file, write_text_file
else:
    from llm import call_llm_json
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


def generate_summary(
    run: RunWorkspace,
    source_document_path: str | Path,
    llm_call=call_llm_json,
) -> dict[str, Any]:
    source_path = _resolve_source_document_path(run, source_document_path)
    source_document = read_text_file(source_path)
    source_hash = sha256(source_document.encode("utf-8")).hexdigest()
    run_root = run.root.resolve()
    source_relative_path = source_path.relative_to(run_root)

    system_prompt = _load_summary_prompt()
    user_prompt = _build_user_prompt(run, source_relative_path, source_document, source_hash)
    summary_schema = _build_summary_schema(
        expected_source=str(source_relative_path),
        expected_source_hash=source_hash,
    )
    summary = llm_call(
        system_prompt,
        user_prompt,
        summary_schema,
        schema_name="v4_summary",
    )
    raw_trace_path = _summary_raw_trace_path(run, source_relative_path)
    write_text_file(raw_trace_path, json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
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
        "Source document path to copy exactly into source_document:\n"
        f"{source_path}\n\n"
        "Source hash to copy exactly into source_hash:\n"
        f"{source_hash}\n\n"
        "Source content to summarize:\n"
        f"{source_document}"
    )


def _build_summary_schema(*, expected_source: str, expected_source_hash: str) -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": list(SUMMARY_REQUIRED_FIELDS),
        "properties": {
            "source_document": {"type": "string", "enum": [expected_source]},
            "source_hash": {"type": "string", "enum": [expected_source_hash]},
            "scope": {"type": "string"},
            "key_decisions": {"type": "array", "items": {"type": "string"}},
            "unresolved_questions": {"type": "array", "items": {"type": "string"}},
            "critical_risks": {"type": "array", "items": {"type": "string"}},
        },
    }


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
    base_name = f"{source_agent}-{source_path.stem}.summary.raw.json"
    candidate = summary_outputs_dir / base_name
    if not candidate.exists():
        return candidate
    index = 2
    while True:
        candidate = summary_outputs_dir / f"{source_agent}-{source_path.stem}_{index:02d}.summary.raw.json"
        if not candidate.exists():
            return candidate
        index += 1


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
