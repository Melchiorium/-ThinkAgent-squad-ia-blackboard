# Step 3.0

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Implement the V0 end-to-end flow with one temporary test agent, a minimal orchestrator, and one exported output file.

## Files concerned
- `app/agents/test_agent.py`
- `app/orchestrator.py`
- `app/main.py`

## Required behavior
- create a temporary `test_agent` module that uses `call_llm(...)`
- the test agent must read the project brief from the blackboard
- the test agent must write one generated text into `blackboard["prd_draft"]`
- the test agent must append a simple trace entry to `blackboard["activity_log"]`
- implement a minimal orchestrator function that:
  - creates a fresh blackboard from one hardcoded brief
  - runs the temporary test agent once
  - returns the updated blackboard
- implement `main.py` so the V0 flow can be launched locally
- `main.py` must write one text output file to `outputs/prd.md`
- keep the flow explicit and deterministic

## Constraints
- use the existing `app/blackboard.py` and `app/llm.py`
- keep the implementation simple and readable
- no classes unless clearly necessary
- no multi-agent flow yet
- no prompt files yet unless truly needed
- no JSON export yet
- no architecture or GTM output yet
- no retries, async, or background processing
- no hidden orchestration

## Acceptance criteria
- `python app/main.py` runs the V0 flow
- one hardcoded brief is used as input
- the temporary agent performs one model call through `app/llm.py`
- `blackboard["prd_draft"]` is populated
- `blackboard["activity_log"]` contains at least one entry
- `outputs/prd.md` is created with generated content
- the code remains understandable by a confirmed Python developer

## Out of scope
- real product, tech, and growth agents
- multi-step orchestration
- prompt file loading
- blackboard JSON export
- architecture and GTM outputs
- CLI arguments and config system

## Open questions
- [ ]

## Developer feedback
- issue: the V0 flow reached a remote OpenAI path that no longer matches the project runtime target
- impact: this step is no longer the valid next implementation path after the stack decision change
- minimal suggested resolution: replace the shared LLM transport with the local Ollama-compatible integration, then resume the V0 flow from the updated adapter

## Developer status
abandoned

## Architect decision
- this step is abandoned due to a stack change
- the project now targets a local Ollama-based LLM through an OpenAI-compatible client
- the follow-up work continues in `step-3.1.md`

## Completion check
- [x] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- Historical step kept for traceability only.
