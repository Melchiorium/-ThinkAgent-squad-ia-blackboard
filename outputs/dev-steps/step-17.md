# Step 17

## Status
- [ ] todo
- [x] in_progress
- [ ] blocked
- [ ] done

## Objective
Add a readiness layer to the generation workflow so the system can qualify whether a generated dossier is actionable, limited, or insufficient before moving forward.

## Files concerned
- `app/blackboard.py`
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/main.py`

## Architect scope
- readiness prompt changes have already been handled by the Architect in `app/prompts V2/`
- no prompt rewrite is requested from the developer in this step
- the developer scope here is technical implementation only

## Objective of the readiness layer
Transform agent critiques, open questions, and contradictions into explicit workflow consequences.

The system must stop treating every generated dossier as equally usable.

Instead, it must classify each dossier with a simple readiness signal:
- `READY`
- `LIMITED`
- `INSUFFICIENT`

## Required behavior
- extend the blackboard so each specialist role can store a local readiness assessment
- store one readiness block for:
  - Product
  - Tech
  - Growth
- each readiness block must contain at least:
  - `status`
  - `blocking_gaps`
  - `required_improvements`
- add a global readiness section in the blackboard
- compute a global readiness status from local statuses with these rules:
  - if at least one agent is `INSUFFICIENT`, global status is `INSUFFICIENT`
  - else if at least one agent is `LIMITED`, global status is `LIMITED`
  - else if all three are `READY`, global status is `READY`

## Readiness source of truth
- readiness must not be inferred heuristically from generic narrative sections
- the source of truth is a dedicated readiness block returned by each agent
- the developer must parse these explicit sections from agent outputs:
  - `## Product Readiness`
  - `## Technical Readiness`
  - `## GTM Readiness`
- each readiness block contains:
  - `Status: READY / LIMITED / INSUFFICIENT`
  - `Blocking Gaps`
  - `Required Improvements`

## Expected implementation
1. Extend the blackboard structure with machine-friendly readiness fields.
2. Update Tech output parsing so `## Technical Readiness` is extracted and stored.
3. Update Growth output parsing so `## GTM Readiness` is extracted and stored.
4. Update Product output parsing so `## Product Readiness` is extracted and stored.
5. Add orchestration logic to aggregate local readiness into one global readiness value.
6. Export this readiness information clearly in `blackboard.md`.

## Minimum blackboard expectations
- a dedicated readiness section, for example:
```python
{
    "readiness": {
        "product": {
            "status": "",
            "blocking_gaps": [],
            "required_improvements": [],
        },
        "tech": {
            "status": "",
            "blocking_gaps": [],
            "required_improvements": [],
        },
        "growth": {
            "status": "",
            "blocking_gaps": [],
            "required_improvements": [],
        },
        "global_status": "",
    }
}
```
- keep the structure simple, explicit, and easy to render

## Global readiness behavior
- `READY`
  - the dossier is sufficiently concrete, coherent, and actionable for the next stage
- `LIMITED`
  - the dossier is understandable but still has important weaknesses
- `INSUFFICIENT`
  - the dossier is not serious enough to move forward without major correction

## Constraints
- do not implement the targeted correction loop yet in this step
- do not redesign the overall collaboration workflow yet
- do not ask the developer to redesign prompts
- preserve the current explicit orchestrator pattern
- keep the implementation parseable and deterministic
- keep the status vocabulary exactly:
  - `READY`
  - `LIMITED`
  - `INSUFFICIENT`

## Acceptance criteria
- Product, Tech, and Growth each have a stored local readiness result in the blackboard
- the orchestrator computes a global readiness status
- `blackboard.md` displays both local and global readiness clearly
- the logic is deterministic and readable in code
- no correction loop is triggered yet in this step

## Out of scope
- prompt redesign
- heuristic readiness inference from old sections
- automatic targeted revision loops
- stopping the run early
- evaluator integration changes
- changing model provider

## Open questions
- [ ]

## Developer feedback
- [x] Clarified: readiness must come from explicit dedicated sections in agent outputs, not from heuristic inference over existing narrative sections.
- [x] Implemented deterministic readiness parsing and global aggregation, but did not run the full generation flow in this step.
- [x] The validated CareSync run for this step is `outputs/tests/CareSync/version 4/`, not `version 3/`.

## Developer status
ready_for_review

## Architect decision
- readiness is now a first-class workflow signal, not just an interpretation left to the human reader
- the first implementation should focus on storing and aggregating readiness, not yet on automated looping
- the dedicated readiness sections are now part of the V2 prompt contract and are the only source of truth for this step

## Completion check
- [x] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- A likely next step will be a `step 17.1` introducing a targeted correction loop when global readiness is `LIMITED`.
- This step should turn generation quality into an explicit operational signal.
- For CareSync, `version 4` is the correct reference run for the readiness layer.
