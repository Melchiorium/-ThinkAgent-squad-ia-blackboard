# Step 10

## Status
- [x] todo
- [ ] in_progress
- [x] blocked
- [ ] done

## Objective
Replace the current Ollama-based LLM integration with the Gemini API through the OpenAI-compatible client layer.

## Files concerned
- `app/llm.py`
- `requirements.txt`
- `.env`

## Required behavior
- update `app/llm.py` so model calls use the OpenAI Python client against the Gemini OpenAI-compatible endpoint
- use this base URL:
  - `https://generativelanguage.googleapis.com/v1beta/openai/`
- use `GEMINI_API_KEY` as the environment variable for authentication
- default the model to:
  - `gemini-2.5-flash`
- keep the existing `call_llm(system_prompt, user_prompt)` interface unchanged for the rest of the app
- keep returning plain text output as a string
- provide clear runtime errors for:
  - missing API key
  - unreachable endpoint
  - invalid model or invalid response
- update `.env` so the runtime reads the Gemini key from environment configuration instead of the previous Ollama/OpenAI local setup
- update `requirements.txt` only as needed for the active client dependency

## Constraints
- do not hardcode the API key in Python code
- do not print the API key in logs or outputs
- preserve the existing app-level interface so agents and orchestrator code do not need changes
- no workflow change in this step
- no prompt changes in this step
- keep the implementation simple and explicit

## Acceptance criteria
- `app/llm.py` targets Gemini through the OpenAI-compatible endpoint
- the app reads the key from `GEMINI_API_KEY`
- the default model is `gemini-2.5-flash`
- `call_llm(...)` still works with the existing codebase contract
- missing key or API failure produces a clear error
- no secret is hardcoded in source files

## Out of scope
- changing prompts
- changing orchestrator logic
- changing blackboard schema
- supporting multiple providers in parallel
- fallback backends

## Open questions
- [ ]

## Developer feedback
- issue: the Gemini endpoint now returns `400 API key expired`
- impact: the code reaches Gemini successfully, but the hosted model call cannot complete until a valid active API key is provided
- minimal suggested resolution: replace the expired key with a valid active Gemini API key, then rerun the project

## Developer status
blocked

## Architect decision
- Gemini becomes the reference hosted model backend for the project
- the integration must remain isolated inside `app/llm.py`
- the API key must remain environment-based, never embedded in code

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- The user has already provided the Gemini key out of band; the Developer must wire the environment variable usage, not copy secrets into application source.
