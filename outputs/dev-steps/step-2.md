# Step 2

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Implement a minimal shared LLM call utility for future agents.

## Files concerned
- `app/llm.py`

## Required behavior
- define one small function that sends a prompt to a chat model
- accept the minimum required inputs for V1:
  - a system prompt
  - a user prompt
- return the generated text as a plain string
- keep the utility reusable by product, tech, and growth agents later
- fail explicitly if the required API key is missing

## Constraints
- use Python only
- keep the file small and readable
- no framework
- no agent-specific logic
- no orchestration logic
- no retries
- no streaming
- no async
- no persistence
- no prompt templating layer
- read configuration only from environment variables

## Acceptance criteria
- `app/llm.py` exists
- it exposes one clear function for a simple model call
- the function returns plain text output
- missing API key produces a clear error
- the code is understandable by a junior Python developer

## Out of scope
- multi-model support
- retries and backoff
- cost tracking
- logging system
- structured output parsing
- agent implementations

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- use one minimal shared utility now; postpone wrappers, abstractions, and resilience features until real agent needs appear

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Prefer a single straightforward function over a client class for this step.
