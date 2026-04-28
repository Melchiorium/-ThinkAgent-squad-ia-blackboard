# Step 26

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Formalize agent modes in the workflow so agents no longer need to infer their operating mode from context alone.

## Files concerned
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`

## Architect scope
- minimal prompt support for explicit mode labels has already been added by the Architect in `app/prompts V2/`
- the developer must not redesign the prompts in this step
- the developer scope here is workflow wiring only

## Context
The project now has several implicit operating modes:
- Product initial draft
- Product revision
- Product correction
- Product final locking pass
- Tech review
- Tech correction
- Growth review
- Growth correction

Today, some of these modes are only implied by the surrounding input.
This makes behavior less reliable and harder to debug.

The chosen direction is:
- keep the same workflow stages
- make the active mode explicit in every agent call
- use a simple textual `Mode: ...` contract

## Required behavior
- every agent call should include an explicit mode line in the user prompt
- the mode must be stable, short, and machine-visible
- agent behavior should depend on explicit mode first, not on inference from context shape

## Canonical modes

### Product
- `Mode: initial_draft`
- `Mode: revision`
- `Mode: correction`
- `Mode: final_locking_pass`

### Tech
- `Mode: review`
- `Mode: correction`

### Growth
- `Mode: review`
- `Mode: correction`

## Expected implementation
1. Update Product agent prompt builders to prepend the correct `Mode:` line for each call.
2. Update Tech agent prompt builder to prepend:
   - `Mode: review` for the normal pass
   - `Mode: correction` when correction tasks are provided
3. Update Growth agent prompt builder in the same way.
4. Keep the rest of the input structure unchanged as much as possible.
5. Preserve backward compatibility of current parsing and output formats.

## Output expectations
- agent inputs become easier to inspect and debug
- prompts no longer rely as much on mode inference
- behavior should become more stable across runs

## Constraints
- do not add a new agent
- do not redesign the workflow stages
- do not change output headings or parser contracts
- keep the change simple and explicit

## Acceptance criteria
- every Product, Tech, and Growth call includes an explicit `Mode:` line
- mode labels match the current workflow stage and task type
- no existing output parser needs to be rewritten
- the system remains compatible with current prompts and artifacts

## Out of scope
- redesigning readiness
- redesigning correction ownership
- introducing structured JSON inputs to the models

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the system now has enough workflow complexity that implicit modes are no longer robust enough
- explicit mode signaling is the simplest way to reduce ambiguity without changing the architecture

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step should improve reliability without materially changing the behavior contract of the agents.
- Product, Tech, and Growth now all receive an explicit `Mode:` line in their user prompts.
