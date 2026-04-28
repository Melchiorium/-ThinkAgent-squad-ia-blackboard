# Step 25

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Make the final `Product-only` locking pass effective by introducing an explicit locking mode contract, so Product cuts scope instead of simply resynthesizing.

## Files concerned
- `app/orchestrator.py`
- `app/main.py`
- any Product agent call site if one exists
- any prompt-loading helper if one exists

## Architect scope
- a minimal Product prompt update has already been applied by the Architect in `app/prompts V2/product_prompt.md`
- the developer must not redesign the Product prompt in this step
- the developer scope here is workflow wiring only

## Context
`Step 24` validated that a final locking pass exists, but it did not improve the final outputs.

The most likely reason is:
- the workflow adds a final Product pass
- but Product still behaves like a normal synthesizer
- so it rewrites or rephrases instead of cutting scope

The chosen direction is:
- keep the locking pass
- make its mission explicit in the input contract
- keep the change minimal and local to that final pass

## Required behavior
- the final Product-only pass must run in an explicit locking mode
- this locking mode must tell Product to:
  - lock the MVP scope
  - avoid redesign
  - avoid adding new ideas
  - remove or defer accessory features
  - keep previously deferred items deferred unless proof-critical

## Expected implementation
1. Update the final Product-only pass input so it clearly says this is a `final locking pass`.
2. Pass only the minimum context needed to lock scope:
   - current final PRD
   - retained / deferred / rejected decisions
   - main expert decisions from Tech and Growth
   - remaining open tensions
3. Avoid giving the pass broad wording that invites re-ideation.
4. Preserve the existing arbitration parsing/export flow.
5. Keep the final output contract unchanged:
   - clean PRD first
   - separate `Product Arbitration` block second

## Minimum workflow expectations
- for example, the locking call should frame the task like:
```text
This is a final locking pass.
Do not redesign the project.
Do not add new ideas.
Confirm only the minimum MVP scope needed now.
Move non-critical items to deferred or out of scope.
```

## Output expectations
- `prd.md` should become narrower or equal in scope, never broader
- the arbitration block should show clearer cuts
- deferred items should stop leaking back into the final deliverable

## Constraints
- do not add a new agent
- do not create a full new prompt file unless strictly necessary
- do not redesign the whole Product role
- keep the change local to the final locking pass

## Acceptance criteria
- the final Product pass is explicitly invoked in locking mode
- final PRDs show stronger scope discipline than `step 24`
- the locking pass stops behaving like a generic rewrite
- the existing output and parsing format remains compatible

## Out of scope
- redesigning Tech or Growth prompts
- changing readiness
- adding another collaboration loop

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the workflow change of `step 24` was not enough on its own
- the locking pass needs a small but explicit behavioral contract
- this should stay minimal and targeted

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- If this still does not improve final PRDs, the next question will be whether the locking pass should use a dedicated prompt variant instead of the shared Product prompt.
- The final locking pass now uses an explicit contract and only the minimum context needed to cut scope.
