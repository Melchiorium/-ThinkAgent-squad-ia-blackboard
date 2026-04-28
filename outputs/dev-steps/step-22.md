# Step 22

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Force `Tech` and `Growth` to produce fewer ideas and more structural decisions, so the final dossier converges faster and reopens the scope less often.

## Files concerned
- `app/orchestrator.py`
- any agent input builder if one exists
- any parsing helper for `Requested Changes`, readiness, or blackboard rendering

## Architect scope
- minimal prompt changes have already been applied by the Architect in `app/prompts V2/tech_prompt.md` and `app/prompts V2/growth_prompt.md`
- the developer must not redesign the prompts in this step
- the developer scope here is technical implementation only

## Context
Recent runs show a recurring pattern:
- `Tech` and `Growth` are better than before, but still reopen or expand the scope
- the final result loses points when accessory ideas come back into the MVP
- the system needs stronger structural decisions before the final Product arbitration

The chosen direction is:
- keep the current roles
- force upstream outputs to be more decisive
- make the workflow consume these decisions more explicitly

## Required behavior
- treat `Tech` and `Growth` outputs as decision-oriented expert contributions, not idea collections
- preserve and expose their main structural decisions inside the blackboard
- make those decisions easier for Product to arbitrate without reinterpreting long prose

## Expected implementation
1. Parse the key structural decisions from `Tech` and `Growth` outputs when available.
2. Store them explicitly in the blackboard, separate from free-form notes.
3. Render them clearly in `blackboard.md`, before lower-priority risks or open questions.
4. Keep only a short set of decision-level items visible in the human summary.
5. Preserve the full raw outputs for traceability.

## Minimum blackboard expectations
- for example:
```python
{
    "expert_decisions": {
        "tech": [
            "Use a centralized MVP architecture around the main dependency.",
            "Keep matching manual until the critical data source is validated."
        ],
        "growth": [
            "Secure supply first before broad user acquisition.",
            "Use one founder-led pilot channel before public launch."
        ]
    }
}
```

## Output expectations
- `blackboard.md` should make structural decisions immediately visible
- lower-value suggestion noise should be less prominent
- Product should receive a cleaner decision surface for final arbitration

## Constraints
- do not add a new agent
- do not redesign the correction loop in this step
- do not remove raw notes from the blackboard
- keep the implementation simple and explicit

## Acceptance criteria
- key structural decisions from `Tech` and `Growth` are captured separately from prose
- `blackboard.md` highlights these decisions clearly
- the workflow makes it harder for accessory suggestions to dominate the final synthesis
- the implementation stays understandable and reversible

## Out of scope
- adding a third Product-only pass
- redesigning Product arbitration again
- changing the global readiness model

## Open questions
- [ ]

## Developer feedback
- [x] Structural decisions from Tech and Growth are now parsed separately, exposed early in the blackboard, and passed into Product revision prompts as a cleaner decision surface.

## Developer status
done

## Architect decision
- the current problem is not only prompt drift
- the workflow also needs to surface decisive upstream choices more explicitly
- this step addresses that without adding a new pass or a new agent

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- A possible next step could be a short Product-only locking pass, but only if this stronger upstream decision framing is not sufficient.
