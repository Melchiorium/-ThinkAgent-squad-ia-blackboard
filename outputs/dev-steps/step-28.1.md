# Step 28.1

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Repair the `step 28` reconciliation logic so the blackboard stays faithful to the final deliverables without inventing retained decisions from simple text overlap.

## Files concerned
- `app/agents/product_agent.py`
- `app/main.py`
- `app/blackboard.py`
- any helper used for blackboard rendering or arbitration state

## Architect scope
- no prompt redesign is requested in this step
- do not change the final deliverables generation logic
- this is a technical fix to the reconciliation layer only

## Context
The current `step 28` implementation introduced a real problem:
- it treats `appears somewhere in PRD / architecture / GTM` as if it meant `retained decision`
- it can therefore move items from `deferred`, `rejected`, or `open_points` into `retained`
- this creates a misleading blackboard, even when the final deliverables are correct

This issue is especially visible in recent `V13` runs:
- `CareSync`
- `LocalLoop`

The regression of the final deliverables does **not** come from reconciliation alone.
But the blackboard contradictions do.

## Required behavior
- keep `raw_parsed` arbitration intact
- stop automatically promoting items to `retained` based on simple textual presence
- treat reconciliation as:
  - contradiction detection
  - warning generation
  - optional display adjustment
- not as a substitute for Product arbitration

## Expected implementation
1. Keep `raw_parsed` as the original parsed arbitration source of truth.
2. Replace the current promotion logic with a safer reconciliation model:
   - detect possible contradictions
   - record them in reconciliation notes or warnings
   - do not silently reclassify major items into `retained`
3. If a reconciled view is still rendered:
   - it must remain conservative
   - it may highlight mismatches
   - it must not claim a decision is retained unless that state is explicit enough
4. Preserve debuggability:
   - `raw_parsed`
   - `reconciled`
   - `reconciliation_notes`
   should remain inspectable separately

## Safer reconciliation direction
- acceptable:
  - "This item is marked rejected, but seems present in the final PRD."
  - "Potential contradiction between arbitration and final deliverables."
- not acceptable:
  - moving that item automatically into `retained`
  - clearing `open_points` only because related words appear somewhere in a final file

## Output expectations
- `blackboard.md` should no longer invent retained decisions
- `blackboard.md` may still show warnings about contradictions
- final deliverables remain untouched in role and priority

## Test requirement
Yes, test in the middle.

After implementing this step:
1. run at least:
   - `CareSync`
   - `LocalLoop`
2. verify whether:
   - blackboard contradictions decrease
   - retained/deferred/rejected become more trustworthy
   - final deliverables remain unchanged in role
3. only after this test should we decide whether to open the next workflow step on the upstream divergence (`revision -> correction -> locking`)

## Acceptance criteria
- no automatic promotion to `retained` from simple substring presence
- reconciliation remains explicit and debuggable
- blackboard becomes more trustworthy on arbitration state
- a test run is completed before moving to the next upstream workflow investigation

## Out of scope
- fixing the final PRD / GTM / architecture regression itself
- redesigning prompts
- changing the correction loop
- changing locking-pass behavior

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the blackboard must be coherent, but it must not overrule Product arbitration by heuristic text matching
- this step is a repair step before investigating the true upstream wedge regression

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] test run completed
- [x] ready for next step

## Notes
- Reconciliation now keeps `raw_parsed` intact and only records contradiction warnings for deferred, rejected, or open-point items that reappear in the final deliverables.
