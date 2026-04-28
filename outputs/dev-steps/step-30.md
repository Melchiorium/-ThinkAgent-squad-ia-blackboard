# Step 30

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Improve the quality of readiness gaps and correction tasks so the workflow reacts to the right problem: MVP wedge dilution, weak proof loop, and poor build-vs-manual decisions, not only generic risk categories.

## Files concerned
- `app/orchestrator.py`
- `app/readiness.py`
- `app/blackboard.py`
- any helper involved in gap aggregation, tagging, prioritization, or correction-task generation

## Architect scope
- no prompt redesign is requested in this step
- do not change the prompt set yet
- this step is about better qualification, grouping, prioritization, and task generation

## Context
`Step 29` made the workflow diagnosable.

What it showed:
- the final locking pass is not the main source of scope re-expansion
- the narrowing never really happens strongly enough earlier
- correction tasks often target broad risk categories such as:
  - `privacy_trust`
  - `compliance`
  - `market_motion`
  - `demand_validation`
- but miss the more decisive MVP questions, such as:
  - what is the narrow wedge?
  - what is the proof loop?
  - what must be built now vs kept manual?
  - what behavior proves adoption?

As a result:
- alerts are visible
- but they are not turned into the most useful corrective work

## Required behavior
- keep existing risk tags such as `privacy_trust`, `compliance`, `market_motion`
- add or support a complementary layer of MVP-qualification themes, for example:
  - `mvp_scope`
  - `proof_loop`
  - `must_build_now`
  - `manual_vs_productized`
  - `core_validation_metric`
- make the correction loop capable of prioritizing these themes when the run is drifting on wedge or proof quality

## Expected implementation
1. Extend the gap classification / normalization layer so that broad gaps can also map to MVP-qualification themes when relevant.
2. Improve prioritization:
   - if the run is suffering from wedge dilution, proof-loop weakness, or scope ambiguity, those themes should outrank generic secondary gaps
3. Improve correction-task generation:
   - tasks should target scope and proof decisions more directly
   - tasks should more often ask for:
     - one wedge decision
     - one proof-loop clarification
     - one build-now vs manual-now decision
     - one validation metric tied to real behavior
4. Preserve transparency in the blackboard:
   - show the final chosen priority gaps
   - show which ones are risk/constraint themes
   - show which ones are MVP-qualification themes

## Important clarification
This step does **not** remove existing tags like:
- `privacy_trust`
- `compliance`
- `market_motion`
- `demand_validation`

It complements them with stronger decision-oriented tags so the workflow can react to:
- a bad MVP core
- a weak proof loop
- too much productized scope
- poor validation criteria

## Test requirement
After implementation, run at least:
- `CareSync`
- `LocalLoop`

Then verify:
- whether correction tasks become more decision-oriented
- whether the workflow starts targeting the real wedge problem earlier
- whether `evaluation-quality` improves specifically on:
  - Product
  - Collaboration
  - Deliverables quality

## Acceptance criteria
- correction tasks are more explicit about MVP wedge / proof loop / build-vs-manual decisions
- broad risk tags still exist, but no longer dominate every correction cycle by default
- blackboard makes the selected priority gaps understandable
- test runs completed on `CareSync` and `LocalLoop`

## Out of scope
- prompt redesign
- changing the number of agents
- redesigning readiness statuses
- rewriting the final locking pass

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- the next useful gain is not another prompt tweak
- it is to make the workflow react to the right class of problem

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] test runs completed
- [ ] ready for next step
