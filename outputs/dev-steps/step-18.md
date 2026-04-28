# Step 18

## Status
- [ ] todo
- [ ] in_progress
- [x] blocked
- [ ] done

## Objective
Distinguish between gaps that can be improved inside the generated dossier and gaps that require external validation, so the system stops treating every blocking issue as fixable through more rewriting.

## Files concerned
- `app/blackboard.py`
- `app/orchestrator.py`
- `app/main.py`
- any readiness or correction-loop helper if one exists

## Architect scope
- no prompt rewrite is requested from the developer in this step
- no agent-role redesign is requested from the developer in this step
- if agent wording or readiness prompts need refinement later, it remains an Architect responsibility
- the developer scope here is technical implementation only

## Context
After `Step 17`, `17.1`, and `17.2`, the system now:
- produces readiness
- triggers a bounded correction loop on `LIMITED`
- generates more explicit correction tasks with ownership

However, the latest runs show a structural limit:
- some gaps improve with rewriting
- some gaps do not
- some blocking issues are not document-quality problems at all

Typical examples:
- legal ambiguity
- willingness to pay
- trust validation
- actual adoption proof
- field-quality validation

These are often not solvable by agents alone.

## Required behavior
- add an explicit distinction between:
  - `resolvable_in_dossier`
  - `requires_external_validation`
- allow readiness gaps to carry this distinction
- ensure the correction loop only targets gaps that are considered resolvable in the dossier
- ensure external-validation gaps are surfaced clearly, but not treated as rewrite tasks

## Goal of the step
The system must stop behaving as if every `LIMITED` gap can be fixed through another round of writing.

Instead, it should:
- improve what can be improved internally
- clearly flag what needs research, pilot evidence, legal clarification, or field validation

## Expected implementation
1. Extend the blackboard readiness structure to distinguish gap types.
2. Update readiness aggregation so gaps can be classified into:
   - internal/document-resolvable
   - external/validation-required
3. Update correction-task planning so only internal/document-resolvable gaps generate correction tasks.
4. Preserve external-validation gaps in the final output as unresolved blockers.
5. Render both categories clearly in `blackboard.md`.

## Minimum blackboard expectations
- for example:
```python
{
    "readiness": {
        "product": {
            "status": "",
            "blocking_gaps": [],
            "required_improvements": [],
            "external_validation_gaps": [],
        },
        "tech": {
            "status": "",
            "blocking_gaps": [],
            "required_improvements": [],
            "external_validation_gaps": [],
        },
        "growth": {
            "status": "",
            "blocking_gaps": [],
            "required_improvements": [],
            "external_validation_gaps": [],
        },
        "global_status": "",
        "global_external_validation_gaps": [],
    }
}
```

## Behavioral rules
- a gap such as “clarify the launch segment” can be treated as document-resolvable
- a gap such as “prove willingness to pay” should be treated as external validation
- a gap such as “legal ambiguity across regions” should generally be treated as external validation unless the issue is only one of document framing
- the correction loop must not repeatedly try to rewrite external-validation gaps

## Output expectations
- `blackboard.md` should make visible:
  - what was improved through writing
  - what still requires validation outside the system
- the final dossier should become more honest and more useful:
  - not only “here is what is weak”
  - but also “here is what cannot be solved from the desk”

## Constraints
- do not ask the developer to redesign prompts
- do not add a new evaluator agent
- do not redesign the full readiness model from scratch
- keep the correction loop bounded as it is
- keep the implementation explicit and understandable

## Acceptance criteria
- the system distinguishes internal gaps from external-validation gaps
- correction tasks are generated only from internal/document-resolvable gaps
- external-validation gaps remain visible in the outputs
- the correction loop becomes more selective and less repetitive
- `blackboard.md` helps a human understand what still needs real-world proof

## Out of scope
- prompt redesign
- changing model provider
- removing the correction loop
- adding automated legal research
- adding a separate evaluator workflow

## Open questions
- Step paused by Architect decision for now.

## Developer feedback
- [ ]

## Developer status
on_hold

## Architect decision
- the current system is now good enough at detecting some unresolved issues
- the next maturity step is to stop pretending all unresolved issues are solvable by better writing
- the system must distinguish between “rewrite this better” and “go validate this in the real world”
- this step is intentionally paused for now and should not be implemented until reactivated explicitly

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- This step should make the pipeline more honest, not just more elaborate.
- It is an important safeguard against overfitting the dossier instead of testing the idea.
- Status: paused / abandoned for now.
