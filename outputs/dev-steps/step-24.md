# Step 24

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Add a short final `Product-only` locking pass that tightens the MVP scope after the multi-agent collaboration, without reopening the whole dossier.

## Files concerned
- `app/orchestrator.py`
- `app/main.py`
- `app/blackboard.py`
- any Product agent call site if one exists
- any blackboard rendering helper if one exists

## Architect scope
- no broad prompt redesign is requested from the developer in this step
- the role split stays the same
- the developer scope here is workflow and output handling only

## Context
Recent runs show that:
- `Tech` and `Growth` are now more reliable contributors
- the Tech path is better captured after `step 23`
- dossiers improve, but accessory scope still tends to survive into the final state

The current limit is no longer mainly upstream signal quality.
It is the lack of a final locking step that says:
- what is definitely in
- what is definitely out for now
- what remains intentionally deferred

The goal is not a third full rewrite.
The goal is a short closing arbitration by Product.

## Required behavior
- after the normal final Product synthesis, run one short additional `Product-only` pass
- give this pass the consolidated blackboard, retained/deferred/rejected decisions, and final PRD state
- ask it to lock the MVP scope, not to redesign the project
- keep the final PRD clean and concise

## Expected implementation
1. Add one extra Product pass at the end of the first-pass workflow.
2. This pass should consume:
   - current final PRD
   - expert decisions already captured from Tech and Growth
   - current Product arbitration state
   - remaining tensions or open points
3. The pass should output a tighter final product state with:
   - confirmed in-scope MVP items
   - confirmed out-of-scope or deferred items
   - no reintroduction of previously deferred non-critical features
4. Store the locking result separately in the blackboard for traceability.
5. Export the final locked PRD as the main `prd.md`.

## Minimum blackboard expectations
- for example:
```python
{
    "product_locking": {
        "applied": True,
        "confirmed_in_scope": [
            "appointment scheduling",
            "medication reminders"
        ],
        "confirmed_deferred": [
            "document sharing",
            "advanced messaging"
        ],
        "locking_note": "Final MVP narrowed after Product closing pass."
    }
}
```

## Output expectations
- `prd.md` should become slightly tighter, not longer
- `blackboard.md` should show that a final locking pass occurred
- previously deferred items should be less likely to reappear in the final deliverable

## Constraints
- do not add a new agent
- do not introduce a full extra collaboration loop
- do not let this pass rewrite Tech or GTM outputs
- keep the pass short and explicitly scope-focused

## Acceptance criteria
- a final Product-only locking pass runs after the current synthesis
- the blackboard records the locking outcome
- `prd.md` is cleaner on scope discipline
- deferred items are less likely to leak back into the final PRD

## Out of scope
- redesigning readiness
- redesigning the correction loop
- major prompt rewrite for all agents

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- the next useful gain is not more upstream contribution
- it is a firmer final Product arbitration
- this should be implemented as a short locking pass, not as another broad rewrite

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- If this step works well, the next question will be whether the Product locking pass needs a small dedicated prompt variant.
