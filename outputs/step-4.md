# Step 4

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Replace the temporary test agent with the real `product_agent` and route the current V0 flow through it.

## Files concerned
- `app/agents/product_agent.py`
- `app/orchestrator.py`
- `app/prompts/product_prompt.md`

## Required behavior
- implement `app/agents/product_agent.py` as the first real domain agent
- the product agent must:
  - read `project_brief` from the blackboard
  - call the shared `call_llm(...)` utility
  - write the generated PRD text into `blackboard["prd_draft"]`
  - append at least one meaningful entry to `blackboard["activity_log"]`
- move the product system prompt content into `app/prompts/product_prompt.md`
- load that prompt file from the product agent instead of hardcoding the system prompt inline
- update `app/orchestrator.py` so the current flow uses `product_agent` instead of `test_agent`
- keep the current flow explicit and deterministic

## Constraints
- keep the step focused on the product path only
- do not introduce tech or growth agent behavior yet
- do not redesign the blackboard structure
- no prompt templating framework
- no classes unless clearly necessary
- keep prompt loading simple and local
- no JSON export
- no multi-step orchestration beyond the current single-agent pass
- no changes to `app/llm.py` in this step unless strictly required for compatibility

## Acceptance criteria
- `app/agents/product_agent.py` is implemented and used by the orchestrator
- `app/prompts/product_prompt.md` contains the product system prompt
- the product agent reads from the blackboard and writes back to it
- the orchestrator no longer depends on `test_agent` for the active flow
- running the current flow still produces `prd.md`
- the generated PRD is more aligned with the project scope than the temporary test-agent output

## Out of scope
- removal of `app/agents/test_agent.py`
- implementation of `tech_agent.py`
- implementation of `growth_agent.py`
- architecture notes and GTM outputs
- final multi-agent orchestration
- prompt tuning across all agents

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the first real agent introduced in the codebase must be `product_agent`, because the target orchestration starts with PRD generation
- prompt text should now live in a dedicated file to make future agent behavior easier to inspect and refine

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Keep `test_agent.py` untouched for now as fallback history; the active flow just should not depend on it anymore.
