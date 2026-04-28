# Step 31.1

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Correct `step 31` by moving the solution-proposal phase out of the final agent deliverables and into an explicit intermediate workflow layer.

## Files concerned
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/blackboard.py`
- `app/main.py`
- any helper used for correction loop storage or rendering

## Architect scope
- do not redesign the full prompts yet unless strictly necessary
- do not keep solution-option prose inside final `gtm.md` / `architecture.md`
- prefer a workflow correction over another prompt-heavy patch

## Context
`Step 31` validated the intuition that we need more solution proposals.

But the implementation path appears wrong:
- solution options are leaking into final deliverables
- problems are still often too generic
- Product receives more text, but not a clean intermediate arbitration layer

This creates:
- noisier `architecture.md`
- noisier `gtm.md`
- more prose without enough stronger final decisions

## Required behavior
- keep the idea of a solution-oriented loop
- but do **not** use final deliverables as the place where those options are stored
- create an intermediate structured layer in the blackboard for:
  - problem
  - owner
  - option A / B
  - tradeoffs
  - recommended option
  - or no viable solution yet / required information

## Expected implementation
1. Split the correction loop into two logical substeps:
   - `solution proposal phase`
   - `product arbitration phase`
2. During the solution proposal phase:
   - Tech and Growth should return structured solution options for their assigned problems
   - those options should be parsed and stored in the blackboard
   - they should not be appended as normal prose into the final architecture / GTM deliverables
3. During the Product arbitration phase:
   - Product receives the structured solution proposals
   - Product chooses one option, rejects one, or marks the issue unresolved
4. Only after that should the final PRD revision be generated.
5. Final deliverables should stay clean:
   - `architecture.md` = architecture deliverable
   - `gtm.md` = GTM deliverable
   - `blackboard.md` = place where intermediate solution proposals and decisions can appear

## Suggested blackboard structure
For example:
```python
"solution_proposals": [
  {
    "problem": "...",
    "owner": "tech",
    "option_a": "...",
    "option_b": "...",
    "tradeoffs": "...",
    "recommended_option": "...",
    "required_information": "...",
  }
]
```

And later:
```python
"solution_decisions": [
  {
    "problem": "...",
    "chosen_option": "...",
    "decision": "chosen / rejected / unresolved",
    "reason": "...",
    "impact_on_mvp": "...",
  }
]
```

## Acceptance criteria
- solution options no longer pollute final `gtm.md` / `architecture.md`
- solution proposals are stored in a structured intermediate workflow state
- Product arbitrates from structured options, not from extra document prose
- `blackboard.md` becomes the place where intermediate solution reasoning is visible
- test runs completed on:
  - `CareSync`
  - `LocalLoop`
  - ideally `Melody`

## Out of scope
- redesigning all prompts again immediately
- changing the number of agents
- changing the core first-pass architecture
- solving all weak runs in one step

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the solution-oriented idea is valid
- the current placement is not
- intermediate workflow state is the right place for these options

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] test runs completed
- [x] ready for next step
