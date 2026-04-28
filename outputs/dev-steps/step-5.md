# Step 5

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Implement the first real multi-agent orchestration pass with `product_agent`, `tech_agent`, and `growth_agent`, and export the three main outputs.

## Files concerned
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/prompts/tech_prompt.md`
- `app/prompts/growth_prompt.md`
- `app/orchestrator.py`
- `app/main.py`

## Required behavior
- implement `tech_agent.py` as a real domain agent
- the tech agent must:
  - read at least `project_brief` and `prd_draft` from the blackboard
  - call the shared `call_llm(...)` utility
  - write its result to `blackboard["architecture_notes"]`
  - append at least one activity entry
- implement `growth_agent.py` as a real domain agent
- the growth agent must:
  - read at least `project_brief` and `prd_draft` from the blackboard
  - call the shared `call_llm(...)` utility
  - write its result to `blackboard["gtm_notes"]`
  - append at least one activity entry
- create the two prompt files for tech and growth
- update the orchestrator to run this explicit sequence:
  - create blackboard from the current hardcoded brief
  - run `product_agent`
  - run `tech_agent`
  - run `growth_agent`
  - return the updated blackboard
- update `main.py` to export:
  - `outputs/prd.md`
  - `outputs/architecture.md`
  - `outputs/gtm.md`

## Constraints
- keep the orchestration explicit and deterministic
- do not add direct agent-to-agent conversation
- agents must communicate only through the blackboard
- no classes unless clearly necessary
- no prompt framework
- no JSON export in this step
- no product revision pass yet
- no conflict resolution logic yet
- keep the flow readable and easy to debug

## Acceptance criteria
- `tech_agent.py` and `growth_agent.py` are implemented
- both agents use their own prompt files
- the orchestrator runs the three-agent sequence in order
- `architecture_notes` and `gtm_notes` are populated after a run
- `outputs/prd.md`, `outputs/architecture.md`, and `outputs/gtm.md` are written by `main.py`
- `activity_log` contains entries from all three agents
- the resulting structure remains understandable by a confirmed Python developer

## Out of scope
- product revision after tech and growth review
- `open_questions`, `risks`, `decisions`, and `conflicts` enrichment beyond minimal future compatibility
- blackboard JSON export
- CLI input for project brief
- advanced prompt tuning
- test removal or cleanup of historical fallback files

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the next meaningful increment is no longer a single-agent refinement
- we now need the first useful shared-blackboard collaboration loop with the three specialist roles, but still without the final product revision pass

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Keep prompts concrete and role-specific to reduce local-model drift.
