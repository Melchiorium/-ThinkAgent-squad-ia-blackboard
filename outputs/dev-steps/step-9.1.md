# Step 9.1

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Keep the final PRD clean and product-only by separating review metadata from the final product deliverable.

## Files concerned
- `app/agents/product_agent.py`
- `app/prompts/product_prompt.md`
- `app/main.py`

## Required behavior
- update `product_agent.py` so the revision pass produces a final PRD only
- the revised PRD must not include review sections such as:
  - `Architecture Notes`
  - `Review Summary`
  - `Requested Changes`
  - `Risks`
  - `Growth Review Notes`
  - `Tech Review Notes`
- keep review metadata in the blackboard structured fields only:
  - `requested_changes`
  - `review_summaries`
  - `applied_changes`
  - `rejected_changes`
  - `revision_trace`
- update the revision prompt contract so Product receives review inputs but returns only the revised PRD document
- in `app/main.py`, ensure:
  - `outputs/prd.md` contains only the final PRD
  - `outputs/blackboard.md` remains the place where review inputs, applied changes, and remaining open points are shown
- if needed, tighten the PRD export path so it writes only `blackboard["prd_draft"]` and never concatenates review fields into the PRD artifact

## Constraints
- do not redesign the orchestrator
- do not change Tech and Growth role boundaries in this step
- do not remove the structured collaboration data from the blackboard
- do not add new dependencies
- keep the implementation simple and explicit
- prefer prompt tightening and output hygiene over new logic

## Acceptance criteria
- `outputs/prd.md` contains only a PRD document
- `outputs/prd.md` no longer contains architecture review sections or review metadata
- `outputs/blackboard.md` still exposes the collaboration trace
- the final PRD remains informed by Tech and Growth inputs without embedding their raw review blocks
- the separation between deliverable output and collaboration trace is clear in the code

## Out of scope
- improving overall product quality drift
- redesigning Tech and Growth prompts again
- adding new blackboard fields
- changing brief loading
- changing the multi-agent order

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the final PRD is a deliverable, not a transport format for inter-agent review data
- all review metadata must stay in structured blackboard fields and human-readable blackboard rendering, not in `prd.md`

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- If the current revision prompt still leaks review headings into the PRD, tighten the prompt first before adding post-processing.
- If a small cleanup step is still needed after generation, keep it deterministic and minimal.
