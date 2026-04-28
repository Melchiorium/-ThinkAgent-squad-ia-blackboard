# Step 28

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Make the internal blackboard consistent with the final deliverables, so it remains a faithful working memory without contradicting `prd.md`, `architecture.md`, or `gtm.md`.

## Files concerned
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/main.py`
- `app/blackboard.py`
- any blackboard rendering helper if one exists

## Architect scope
- no prompt redesign is requested in this step
- the current issue is primarily workflow / state consistency
- the developer scope here is parsing, reconciliation, storage, and rendering only

## Context
The latest `V3` runs show a good improvement in final deliverables.

`prd.md`, `architecture.md`, and `gtm.md` are now often better than the internal blackboard view, which is acceptable.

What is not acceptable is when the blackboard contradicts the final files, for example:
- an item marked as rejected although it appears in the final PRD
- an item left open although it is effectively required by the final architecture
- structural decisions present in final documents but missing or misclassified in the blackboard

The blackboard is not the final deliverable.
But it must stay internally faithful to the decisions that the final deliverables actually embody.

## Required behavior
- preserve final deliverables as the source of final expression
- reconcile the blackboard with the final deliverables after final arbitration / locking
- reduce contradictions between:
  - `retained`
  - `deferred`
  - `rejected`
  - `open`
and what the final files actually contain

## Expected implementation
1. After final Product revision and locking, reconcile blackboard decision state against the final deliverables.
2. Detect when a supposedly rejected or deferred item is clearly present in the final PRD, architecture, or GTM.
3. Reclassify those items or flag them explicitly as reconciliation issues.
4. Keep a trace of the original parsed arbitration state if needed, but expose a reconciled decision state for rendering.
5. Use the reconciled decision state in `blackboard.md` so the displayed memory matches the final outcome.

## Minimum blackboard expectations
- for example:
```python
{
    "arbitration": {
        "raw_parsed": {...},
        "reconciled": {
            "retained": [...],
            "deferred": [...],
            "rejected": [...],
            "open_points": [...]
        },
        "reconciliation_notes": [
            "Moved item X from rejected to retained because it appears in final PRD."
        ]
    }
}
```

## Output expectations
- `blackboard.md` should no longer contradict the final deliverables on major decisions
- reconciliation notes should make silent corrections understandable
- final files remain the user-facing source of truth

## Constraints
- do not add a new agent
- do not redesign prompts in this step
- do not change the final artifact set
- keep the implementation explicit and debuggable

## Acceptance criteria
- major contradictions between blackboard arbitration and final deliverables are reduced
- `blackboard.md` reflects the actual final outcome more faithfully
- reconciliation logic is understandable from code and/or rendered notes
- final deliverables remain unchanged in role and priority

## Out of scope
- making the blackboard “better” than the final files
- redesigning readiness
- another correction loop
- prompt rewriting

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the final deliverables are the intended polished outputs
- the blackboard remains an internal memory and trace
- the next useful gain is to make that internal memory consistent with the final outputs

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- If this works well, the next follow-up may be a smaller cleanup step on tag quality and `untagged` reduction.
- The blackboard now keeps a raw arbitration trace and renders a reconciled state aligned with the final deliverables.
