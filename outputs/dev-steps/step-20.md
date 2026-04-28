# Step 20

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Make Product arbitration explicit and reliable by separating the final PRD deliverable from a structured arbitration artifact stored in the blackboard.

## Files concerned
- `app/agents/product_agent.py`
- `app/blackboard.py`
- `app/main.py`
- any parsing helper used for Product outputs

## Architect scope
- the Product prompt has already been minimally adjusted by the Architect to support a separate `Product Arbitration` block
- no prompt rewrite is requested from the developer in this step
- no redesign of Product role is requested from the developer in this step
- if prompt evolution becomes necessary later, it remains an Architect responsibility
- the developer scope here is technical implementation only

## Context
The current arbitration logic is still too heuristic:
- retained / deferred / rejected decisions are partially inferred after the fact
- lexical matching is fragile
- real decisions may be missed when Product rewrites them differently

The goal is to keep:
- a clean final `prd.md`
- a reliable arbitration trace in the blackboard

## Required behavior
- keep `prd.md` as a pure product deliverable
- do not mix arbitration metadata into the visible PRD artifact
- add a separate structured arbitration artifact produced by Product
- parse that artifact and store it in the blackboard
- use this artifact as the source of truth for:
  - `retained_decisions`
  - `deferred_decisions`
  - `rejected_changes`
  - `open_points`
  - short rationales when available

## Separation principle
Product should now have two logical outputs:
1. a final PRD for humans
2. a structured arbitration block for the system

The structured arbitration block is now part of the Product prompt contract under:
- `## Product Arbitration`

With these exact subsections:
- `### Retained`
- `### Deferred`
- `### Rejected`
- `### Open Points`
- `### Rationales`

The developer should implement this separation so that:
- `prd.md` only contains the PRD
- `blackboard.md` contains the arbitration trace
- the app no longer depends primarily on heuristic inference for final arbitration state

## Expected implementation
1. Update Product output handling so the `## Product Arbitration` block can be captured separately from the final PRD.
2. Extend the blackboard with an explicit arbitration structure if needed.
3. Parse the arbitration block into machine-friendly fields.
4. Populate the existing decision-related blackboard fields from that parsed artifact.
5. Keep a safe fallback path if the arbitration artifact is missing or malformed.
6. Render the arbitration information clearly in `blackboard.md`.

## Minimum blackboard expectations
- for example:
```python
{
    "arbitration": {
        "retained": [],
        "deferred": [],
        "rejected": [],
        "open_points": [],
        "rationales": [],
    }
}
```

This structure may be adapted, but the separation of concerns must remain explicit.

## Constraints
- do not pollute `prd.md` with review notes or arbitration metadata
- do not ask the developer to redesign prompts in this step
- do not remove the current fallback behavior entirely unless a robust replacement is in place
- keep the implementation explicit and easy to debug

## Acceptance criteria
- `prd.md` remains a clean product-only deliverable
- Product arbitration is stored separately in structured form
- decision fields in the blackboard come from the arbitration artifact rather than mainly from heuristics
- `blackboard.md` shows clearer retained / deferred / rejected / open decisions
- fallback behavior exists if parsing fails

## Out of scope
- prompt redesign
- changing other agents
- redesigning the whole blackboard
- changing model provider

## Open questions
- [ ]

## Developer feedback
- [x] Product arbitration is now parsed from the explicit `## Product Arbitration` block when present, with a heuristic fallback only if the block is missing or malformed.

## Developer status
done

## Architect decision
- the problem is real: arbitration is currently too heuristic
- the preferred solution is not to embed more meta-output in the PRD
- the correct direction is to separate the human deliverable from the machine-readable arbitration trace

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- The goal is better arbitration fidelity without degrading the final PRD.
