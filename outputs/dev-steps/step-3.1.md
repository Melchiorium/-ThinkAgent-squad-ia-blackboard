# Step 3.1

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Adapt the shared LLM utility to use a local Ollama-backed model through an OpenAI-compatible client, without changing the overall project structure.

## Files concerned
- `app/llm.py`
- `requirements.txt`

## Required behavior
- replace the current direct HTTP implementation in `app/llm.py` with an implementation based on `from openai import OpenAI`
- keep a single shared function for model calls so existing and future agents continue to depend on the same module
- support a configurable `base_url` through environment variables
- default the `base_url` to the local Ollama-compatible endpoint:
  - `http://localhost:11434/v1`
- stop requiring a real external API key
- allow a simple placeholder key such as `ollama`
- keep model selection configurable through environment variables
- return plain generated text as a string
- surface clear runtime errors if the local endpoint is unreachable or returns an invalid response

## Constraints
- preserve the current module role of `app/llm.py`
- no agent-specific logic
- no orchestrator changes in this step
- no new abstraction layer beyond what is needed for local compatibility
- no token optimization logic
- no retries, async, streaming, or background processing
- prefer simple and robust prompt transport over feature completeness
- keep the code readable and easy to debug

## Acceptance criteria
- `app/llm.py` uses the OpenAI Python client
- `requirements.txt` declares the required dependency
- the LLM utility works with a local Ollama endpoint exposed as OpenAI-like API
- the utility no longer depends on an external OpenAI API key being present
- `base_url` and model can be configured via environment variables
- the function still returns plain text output
- connection and response failures produce clear errors

## Out of scope
- resuming the full V0 flow in this step
- changes to `app/main.py`
- changes to `app/orchestrator.py`
- creation of real domain agents
- prompt redesign across the project
- benchmarking, latency tuning, or model quality tuning

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the architecture remains unchanged: one shared LLM utility, one orchestrator, shared blackboard
- only the transport layer changes
- local Ollama with OpenAI-compatible client is now the reference integration path for V1

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Use `OpenAI(base_url=..., api_key=...)` with a local default such as `api_key="ollama"` when no real key is needed.
