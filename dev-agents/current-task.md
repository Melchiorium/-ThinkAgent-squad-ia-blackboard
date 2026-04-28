# Step Correctif V12

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Return the project to a `V12-like` workflow baseline: keep `prompts V3`, but remove post-`V12` workflow and blackboard layers that were added after the strongest known results.

## Why
The best known results were obtained around:
- `outputs/tests/CareSync/version 12`
- `outputs/tests/LocalLoop/version 12`

After that point, several workflow/blackboard layers were added:
- `step 28`
- `step 28.1`
- `step 29`
- `step 30` preparation
- `step 31`
- `step 31.1`

Those additions increased internal instrumentation and extra workflow behavior, but did not improve the final deliverables and made the system harder to reason about.

## Snapshot Of Current State Before Rollback
- prompt family kept in use: `prompts V3`
- prompt selector still available through `BLACKBOARD_PROMPT_VERSION`
- current workflow contains:
  - targeted correction loop
  - product locking pass
  - extra solution-oriented correction behavior added after `V12`

## Corrective Decision
Rollback the workflow to the closest known-good baseline after V3 prompts and before the post-V12 workflow additions.

## Scope
- keep `prompts V3`
- keep prompt version switching
- keep readiness and correction loop baseline
- keep product locking pass baseline
- remove post-V12 solution-proposal workflow behavior
- remove post-V12 solution rendering behavior

## Files touched by this corrective rollback
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/blackboard.py`
- `app/main.py`
- `dev-agents/current-task.md`

## Result
- project returned to a simpler `V12-like` workflow baseline
- no prompt rewrite performed
- rollback focused on workflow / blackboard behavior only
