# Step 17.1

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Add a targeted correction loop when the global readiness is `LIMITED`, so the system can improve specific blocking weaknesses instead of rerunning a full generic rewrite.

## Files concerned
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/main.py`

## Architect scope
- no prompt rewrite is requested from the developer in this step
- the current V2 prompt contract remains the source of truth
- the developer scope here is workflow and data-flow implementation only

## Context
`Step 17` introduced explicit local readiness and a global readiness signal.

The next improvement is to make this signal operational:
- if the dossier is `READY`, the pipeline stops normally
- if the dossier is `LIMITED`, the pipeline runs a short targeted correction pass
- if the dossier is `INSUFFICIENT`, the pipeline stops and exposes the blocking issues clearly

## Required behavior
- add a correction-loop capability driven by readiness results
- only trigger the loop when global readiness is `LIMITED`
- do not trigger the loop when global readiness is `READY`
- do not attempt an automatic recovery loop when global readiness is `INSUFFICIENT`
- limit the number of correction loops to a small fixed maximum:
  - recommended: `2`

## Principle of the targeted correction loop
The correction loop must not ask agents to rewrite everything.

It must:
- identify the most important blocking gaps from readiness
- transform them into targeted correction tasks
- send these focused tasks back to the relevant agent or agents
- produce an updated dossier and updated readiness

## Expected workflow
1. Run the normal generation flow:
   - Product draft
   - Tech review + Technical Readiness
   - Growth review + GTM Readiness
   - Product final proposal + Product Readiness
   - global readiness aggregation
2. If global readiness is `READY`:
   - stop normally
3. If global readiness is `INSUFFICIENT`:
   - stop normally
   - expose the blocking readiness state in the outputs
4. If global readiness is `LIMITED`:
   - build a small targeted correction plan from the local readiness gaps
   - run one short correction pass
   - recompute local readiness
   - recompute global readiness
   - repeat only until:
     - readiness becomes `READY`, or
     - readiness becomes `INSUFFICIENT`, or
     - the max loop count is reached

## Correction task expectations
- targeted correction tasks must be explicit and short
- they must be derived from:
  - `blocking_gaps`
  - `required_improvements`
- they must avoid broad “rewrite the whole document” instructions
- examples of valid task styles:
  - clarify the initial target segment
  - replace a vague acquisition path with one concrete pilot motion
  - define the minimum permission model required before launch
  - state the business model hypothesis more explicitly

## Blackboard expectations
- extend the blackboard so the correction loop is traceable
- store at least:
  - current loop count
  - max loop count
  - correction tasks issued
  - readiness history per loop
  - final loop outcome
- keep this structure machine-friendly and renderable in `blackboard.md`

## Minimum blackboard expectations
- for example:
```python
{
    "readiness": {
        "product": {...},
        "tech": {...},
        "growth": {...},
        "global_status": "",
        "loop_count": 0,
        "max_loops": 2,
        "history": [],
        "correction_tasks": [],
        "final_outcome": "",
    }
}
```

## Output expectations
- `blackboard.md` must show:
  - the initial readiness state
  - whether a correction loop was triggered
  - the targeted tasks issued
  - the updated readiness after correction
  - the final readiness outcome
- the main deliverables should remain:
  - `prd.md`
  - `architecture.md`
  - `gtm.md`
  - `blackboard.md`
- no additional file format is required in this step unless implementation really needs it

## Constraints
- do not redesign prompts in this step
- do not introduce free-form agent-to-agent chat
- do not create unbounded or recursive loops
- keep the maximum loop count hard-limited and explicit
- preserve the current orchestrator-first architecture
- keep the implementation understandable and deterministic

## Acceptance criteria
- when global readiness is `LIMITED`, a targeted correction loop is triggered
- the correction loop uses explicit tasks derived from readiness fields
- readiness is recomputed after each correction pass
- the loop stops on `READY`, `INSUFFICIENT`, or max loops reached
- `blackboard.md` makes the correction logic understandable to a human reader
- no prompt redesign is requested from the developer

## Out of scope
- changing model provider
- redesigning prompts
- adding a separate evaluator agent
- second-pass CEO review workflow changes
- unlimited self-improvement loops

## Open questions
- [ ]

## Developer feedback
- [x] The correction loop is implemented in the orchestrator with bounded targeted tasks and traceable history.
- [x] Validation run on `outputs/tests/CareSync/version 5/` confirms the loop is triggered and capped at two iterations.

## Developer status
done

## Architect decision
- readiness must now have workflow consequences
- `LIMITED` should trigger focused improvement, not a full rerun
- `INSUFFICIENT` should block the pipeline rather than force low-quality automatic recovery
- the system should stay conservative and bounded

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step should convert readiness from a reporting feature into a real control mechanism.
- If needed later, a future step can refine how correction tasks are prioritized.
