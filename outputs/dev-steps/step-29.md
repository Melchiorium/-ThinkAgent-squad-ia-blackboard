# Step 29

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Identify and fix the upstream workflow step where a strong narrow wedge degrades into a broader, weaker final deliverable.

## Files concerned
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/blackboard.py`
- any helper used to store revision / locking traces

## Architect scope
- no prompt redesign is requested in this step
- do not change the prompt set yet
- this step is about workflow tracing, state visibility, and stage-specific behavior

## Context
`Step 28.1` repaired the blackboard reconciliation layer enough to make it more trustworthy.

The remaining problem is upstream:
- `CareSync V15` is still much weaker than `V12`
- `LocalLoop V15` is still much weaker than `V12`

The main symptom is not blackboard contradiction anymore.
It is wedge dilution:
- a narrow MVP framing exists or almost exists at one stage
- then broadens again later in the workflow

Likely suspect stages:
1. `run_product_revision`
2. targeted correction loop re-entry
3. `run_product_locking_pass`

## Required behavior
- make the workflow auditable stage by stage
- expose what the product scope looks like:
  - after initial Product draft
  - after Product revision
  - after each correction loop pass
  - after final locking pass
- allow us to detect exactly where the wedge widens again

## Expected implementation
1. Add explicit stage trace storage for Product outputs, at minimum:
   - `product_initial_draft`
   - `product_revised_draft`
   - `product_post_correction_draft` or per-loop snapshots
   - `product_locked_draft`
2. Preserve these traces in the blackboard state so they can be inspected after a run.
3. Render a compact comparison section in `blackboard.md`, for example:
   - workflow checkpoints
   - stage labels
   - short notes or excerpts if useful
4. Make the correction loop trace clearer:
   - which task set triggered a rerun
   - what Product received
   - whether Product had owned tasks or only re-synthesized anyway
5. If the current workflow always reruns Product too broadly during correction:
   - narrow that behavior only if the code evidence is clear
   - otherwise, first expose the trace before changing behavior

## What we are trying to answer
- Does the wedge already widen during `run_product_revision`?
- Or does it widen during correction-loop resynthesis?
- Or does the final locking pass re-expand scope instead of trimming it?

## Acceptance criteria
- after a run, we can clearly inspect where scope broadening happened
- the blackboard contains enough stage trace to compare Product outputs across the workflow
- the implementation makes the divergence diagnosable, not hidden
- test runs are produced on:
  - `CareSync`
  - `LocalLoop`

## Out of scope
- changing prompts
- redesigning readiness
- reworking tag taxonomy
- adding a new agent
- fixing every quality issue in the same step

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the next useful gain is not another blackboard cleanup
- it is to locate the exact stage where the good V12 wedge is lost

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] test runs completed
- [x] ready for next step

## Notes
- The blackboard now keeps explicit product checkpoints for initial draft, revision, correction loops, and final locking, plus workflow checkpoints that show correction-task ownership.
