import json
import os
import re
from typing import Any

import openai
from openai import OpenAI


def call_llm(system_prompt: str, user_prompt: str) -> str:
    """Send a minimal chat request and return the assistant text."""
    api_key, base_url, model, provider_name = _resolve_llm_config()

    if not api_key:
        raise RuntimeError("Missing required environment variable: OPENAI_API_KEY")

    client = OpenAI(base_url=base_url, api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
    except openai.APIConnectionError as error:
        raise RuntimeError(
            f"LLM request failed: cannot reach {provider_name} endpoint at {base_url}"
        ) from error
    except openai.APITimeoutError as error:
        raise RuntimeError(f"LLM request failed: timed out at {base_url}") from error
    except openai.APIStatusError as error:
        error_details = _extract_error_details(error)
        if error.status_code == 404:
            raise RuntimeError(
                f"LLM request failed: model '{model}' was not found at {base_url}. "
                f"Set OPENAI_MODEL to a valid model for this provider. Details: {error_details}"
            ) from error
        raise RuntimeError(
            f"LLM request failed: HTTP {error.status_code} from {base_url}. "
            f"Details: {error_details}"
        ) from error
    except openai.APIError as error:
        raise RuntimeError(f"LLM request failed: {error}") from error

    if not response.choices:
        raise RuntimeError("LLM request failed: empty response")

    content = response.choices[0].message.content
    if content is None:
        raise RuntimeError("LLM request failed: missing text content")
    if not isinstance(content, str):
        raise RuntimeError("LLM request failed: unexpected non-text response")

    return content


def call_llm_json(
    system_prompt: str,
    user_prompt: str,
    schema: dict[str, Any],
    *,
    schema_name: str = "structured_response",
) -> dict[str, Any]:
    """Return one JSON object that validates against the provided JSON schema."""
    api_key, base_url, model, provider_name = _resolve_llm_config()

    if not api_key:
        raise RuntimeError("Missing required environment variable: OPENAI_API_KEY")

    client = OpenAI(base_url=base_url, api_key=api_key)
    normalized_schema_name = _normalize_schema_name(schema_name)
    response = None
    schema_error: openai.APIStatusError | None = None

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": normalized_schema_name,
                    "schema": schema,
                    "strict": True,
                },
            },
        )
    except openai.APIStatusError as error:
        if not _is_response_format_unsupported(error):
            raise _format_llm_status_error(error, model=model, base_url=base_url) from error
        schema_error = error
    except openai.APIConnectionError as error:
        raise RuntimeError(
            f"LLM request failed: cannot reach {provider_name} endpoint at {base_url}"
        ) from error
    except openai.APITimeoutError as error:
        raise RuntimeError(f"LLM request failed: timed out at {base_url}") from error
    except openai.APIError as error:
        raise RuntimeError(f"LLM request failed: {error}") from error

    if response is None:
        response = _call_json_object_fallback(
            client=client,
            model=model,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            schema_error=schema_error,
        )

    content = _extract_text_response(response)
    parsed = _parse_json_response(content)
    _validate_json_schema(parsed, schema, path="$")
    if not isinstance(parsed, dict):
        raise RuntimeError("LLM JSON response must be a JSON object")
    return parsed


def _resolve_llm_config() -> tuple[str | None, str, str, str]:
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1/").rstrip("/") + "/"
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    if not api_key and base_url != "https://api.openai.com/v1/":
        api_key = "local"
    return api_key, base_url, model, "OpenAI-compatible"


def _call_json_object_fallback(
    *,
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_prompt: str,
    schema_error: openai.APIStatusError | None,
):
    fallback_prompt = (
        f"{user_prompt}\n\n"
        "Return exactly one JSON object. Do not wrap it in Markdown, do not add "
        "comments, and do not include text before or after the JSON object."
    )
    try:
        return client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": fallback_prompt},
            ],
            response_format={"type": "json_object"},
        )
    except openai.APIStatusError as error:
        if not _is_response_format_unsupported(error):
            raise _format_llm_status_error(
                error,
                model=model,
                base_url=str(client.base_url),
            ) from error
        try:
            return client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": fallback_prompt},
                ],
            )
        except openai.APIStatusError as text_error:
            raise _format_llm_status_error(
                text_error,
                model=model,
                base_url=str(client.base_url),
            ) from text_error
    except openai.APIError as error:
        if schema_error is not None:
            details = _extract_error_details(schema_error)
            raise RuntimeError(
                "LLM JSON request failed after schema fallback. "
                f"Initial schema error: {details}. Fallback error: {error}"
            ) from error
        raise RuntimeError(f"LLM JSON request failed: {error}") from error


def _extract_text_response(response) -> str:
    if not response.choices:
        raise RuntimeError("LLM request failed: empty response")

    content = response.choices[0].message.content
    if content is None:
        raise RuntimeError("LLM request failed: missing text content")
    if not isinstance(content, str):
        raise RuntimeError("LLM request failed: unexpected non-text response")
    return content


def _parse_json_response(content: str) -> Any:
    raw = content.strip()
    if not raw:
        raise RuntimeError("LLM JSON response was empty")
    if raw.startswith("```"):
        raise RuntimeError("LLM JSON response must not be wrapped in Markdown fences")
    try:
        parsed, end_index = json.JSONDecoder().raw_decode(raw)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"LLM JSON response is invalid: {error.msg}") from error
    if raw[end_index:].strip():
        raise RuntimeError("LLM JSON response contains trailing non-JSON content")
    return parsed


def _validate_json_schema(value: Any, schema: dict[str, Any], *, path: str) -> None:
    any_of = schema.get("anyOf")
    if isinstance(any_of, list):
        for option in any_of:
            try:
                _validate_json_schema(value, option, path=path)
                return
            except RuntimeError:
                continue
        raise RuntimeError(
            f"JSON schema validation failed at {path}: value did not match any allowed schema"
        )

    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(value, dict):
            raise RuntimeError(f"JSON schema validation failed at {path}: expected object")
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                raise RuntimeError(
                    f"JSON schema validation failed at {path}: missing required field '{key}'"
                )
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            unknown_keys = set(value) - set(properties)
            if unknown_keys:
                raise RuntimeError(
                    f"JSON schema validation failed at {path}: unexpected field "
                    + ", ".join(sorted(str(key) for key in unknown_keys))
                )
        for key, item in value.items():
            if key in properties:
                _validate_json_schema(item, properties[key], path=f"{path}.{key}")
        return

    if expected_type == "array":
        if not isinstance(value, list):
            raise RuntimeError(f"JSON schema validation failed at {path}: expected array")
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            raise RuntimeError(
                f"JSON schema validation failed at {path}: expected at least {min_items} items"
            )
        max_items = schema.get("maxItems")
        if isinstance(max_items, int) and len(value) > max_items:
            raise RuntimeError(
                f"JSON schema validation failed at {path}: expected at most {max_items} items"
            )
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                _validate_json_schema(item, item_schema, path=f"{path}[{index}]")
        return

    if expected_type == "string":
        if not isinstance(value, str):
            raise RuntimeError(f"JSON schema validation failed at {path}: expected string")
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(value) < min_length:
            raise RuntimeError(
                f"JSON schema validation failed at {path}: expected at least {min_length} characters"
            )
        max_length = schema.get("maxLength")
        if isinstance(max_length, int) and len(value) > max_length:
            raise RuntimeError(
                f"JSON schema validation failed at {path}: expected at most {max_length} characters"
            )
        pattern = schema.get("pattern")
        if pattern and re.match(pattern, value) is None:
            raise RuntimeError(
                f"JSON schema validation failed at {path}: value does not match pattern"
            )

    if "enum" in schema and value not in schema["enum"]:
        raise RuntimeError(
            f"JSON schema validation failed at {path}: invalid enum value '{value}'"
        )


def _normalize_schema_name(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9_-]+", "_", value.strip())
    return normalized.strip("_") or "structured_response"


def _is_response_format_unsupported(error: openai.APIStatusError) -> bool:
    if error.status_code not in {400, 404, 422}:
        return False
    details = _extract_error_details(error).lower()
    return "response_format" in details or "json_schema" in details or "json object" in details


def _format_llm_status_error(error: openai.APIStatusError, *, model: str, base_url: str) -> RuntimeError:
    error_details = _extract_error_details(error)
    if error.status_code == 404:
        return RuntimeError(
            f"LLM request failed: model '{model}' was not found at {base_url}. "
            f"Set OPENAI_MODEL to a valid model for this provider. Details: {error_details}"
        )
    return RuntimeError(
        f"LLM request failed: HTTP {error.status_code} from {base_url}. "
        f"Details: {error_details}"
    )


def _extract_error_details(error: Exception) -> str:
    response = getattr(error, "response", None)
    if response is None:
        return str(error)

    try:
        body = response.text
    except Exception:
        body = ""

    if body:
        return body.strip()

    return str(error)
