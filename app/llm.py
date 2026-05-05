import os

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


def _resolve_llm_config() -> tuple[str | None, str, str, str]:
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1/").rstrip("/") + "/"
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    if not api_key and base_url != "https://api.openai.com/v1/":
        api_key = "local"
    return api_key, base_url, model, "OpenAI-compatible"


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
