# Step 27

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Reduce confusion between MVP product scope and pilot operations by preserving a clear separation between:
- product features that must be built now
- manual or operational support used to run the pilot
- items deferred until after proof

## Files concerned
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/agents/growth_agent.py`
- any blackboard rendering helper if one exists

## Architect scope
- minimal prompt changes have already been applied by the Architect in:
  - `app/prompts V2/product_prompt.md`
  - `app/prompts V2/growth_prompt.md`
- the developer must not redesign prompts in this step
- the developer scope here is workflow wiring, parsing, and rendering only

These prompt changes now make the distinction more explicit and parseable via dedicated sections, instead of leaving it only in free-form prose.

## Context
Recent runs show a recurring issue:
- the system identifies useful pilot or concierge actions
- but some of these actions leak back into the PRD as if they were MVP product features

Examples include:
- onboarding help becoming product scope
- support assets becoming feature scope
- analytics or promotional support being treated like required build scope
- manual launch operations being merged into the MVP instead of remaining operational

This weakens final scope discipline even when the overall dossier quality is acceptable.

## Required behavior
- preserve a clear distinction between:
  - product scope
  - manual / operational pilot support
  - deferred / later scope
- make this distinction visible in the blackboard
- give Product a cleaner surface for final arbitration

## Expected implementation
1. When parsing Growth and Product outputs, preserve any signal that distinguishes:
   - must-build-now
   - manual / operational / concierge
   - deferred / later
2. Store manual or operational pilot actions separately from product feature scope in the blackboard.
3. Ensure final PRD generation consumes this distinction instead of flattening everything into one recommendation layer.
4. Render the distinction clearly in `blackboard.md`.
5. Keep existing output formats compatible where possible.

## Minimum blackboard expectations
- for example:
```python
{
    "pilot_operations": {
        "growth": [
            "manual business outreach",
            "founder-led onboarding"
        ],
        "product": [
            "guided concierge onboarding during pilot"
        ]
    },
    "mvp_scope": {
        "confirmed_features": [...],
        "deferred_features": [...]
    }
}
```

## Output expectations
- `blackboard.md` should make it obvious what is:
  - product
  - operational
  - deferred
- `prd.md` should include fewer operational items disguised as product features
- final scope contradictions should decrease

## Constraints
- do not add a new agent
- do not redesign readiness
- do not change the core artifact set
- keep the implementation explicit and understandable

## Acceptance criteria
- manual / operational pilot actions are no longer flattened into product scope by default
- `blackboard.md` shows the distinction clearly
- final PRDs show fewer scope leaks from operational GTM or support activities
- the system remains compatible with current parsers and run structure

## Out of scope
- adding another collaboration loop
- redesigning Tech prompts
- introducing a full taxonomy overhaul

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- the current bottleneck is not only agent quality
- it is also the flattening of qualitatively different recommendations into one product scope
- this step aims to preserve that distinction through the workflow

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- If this works, the next improvement may be to protect a small set of non-negotiable constraints during Product arbitration.
