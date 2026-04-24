# Step 6

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Add the product revision pass so the final PRD is updated after the tech and growth reviews, and export the consolidated blackboard trace.

## Files concerned
- `app/agents/product_agent.py`
- `app/orchestrator.py`
- `app/main.py`

## Required behavior
- extend `product_agent.py` so it supports a second pass after `tech_agent` and `growth_agent`
- the revision pass must:
  - read `project_brief`
  - read the current `prd_draft`
  - read `architecture_notes`
  - read `gtm_notes`
  - generate an updated PRD
  - write the revised content back to `blackboard["prd_draft"]`
  - append a distinct activity log entry for the revision step
- update the orchestrator to run this explicit sequence:
  - create blackboard
  - run `product_agent` first pass
  - run `tech_agent`
  - run `growth_agent`
  - run `product_agent` revision pass
  - return the final blackboard
- update `main.py` to export, in addition to the existing result files:
  - `outputs/blackboard.json`
  - `outputs/activity_log.txt`

## Constraints
- keep the orchestration explicit and deterministic
- do not introduce direct agent-to-agent conversation
- keep using the shared blackboard as the only collaboration surface
- keep `product_agent.py` readable; do not build a generic agent framework
- no classes unless clearly necessary
- no async, retries, or background processing
- no CLI/config redesign in this step
- do not change the role boundaries of the three agents

## Acceptance criteria
- the orchestrator runs a second product pass after tech and growth
- the final `prd_draft` reflects inputs from `architecture_notes` and `gtm_notes`
- `activity_log` contains separate entries for product draft generation and product revision
- `outputs/blackboard.json` is written
- `outputs/activity_log.txt` is written
- the flow remains understandable and easy to trace for a confirmed Python developer

## Out of scope
- restructuring the agent modules
- prompt refactoring across all agents
- adding validation of blackboard fields
- changing the input brief source
- advanced conflict resolution between agents
- cleanup of historical output filename mistakes

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the next architectural milestone is not more agents, but the first real collaboration loop
- the product revision pass is required to match the target orchestration model from the brief

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Keep the first-pass and revision-pass behavior explicit, even if they share helper code.
