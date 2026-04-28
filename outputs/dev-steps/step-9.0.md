# Step 9

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Implement a structured collaboration layer in the blackboard so Tech and Growth outputs can be extracted reliably and rendered clearly for a human reader.

## Files concerned
- `app/blackboard.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/agents/product_agent.py`
- `app/main.py`

## Required behavior
- extend the blackboard with these explicit fields:
  - `requested_changes`
  - `review_summaries`
  - `applied_changes`
  - `rejected_changes`
- use this exact internal shape:
```python
{
    "requested_changes": {
        "tech": [],
        "growth": [],
    },
    "review_summaries": {
        "tech": "",
        "growth": "",
    },
    "applied_changes": [],
    "rejected_changes": [],
}
```
- in `tech_agent.py`, after the existing narrative note is produced:
  - extract a short summary paragraph and store it in `review_summaries["tech"]`
  - extract up to 5 requested changes and store them in `requested_changes["tech"]`
  - extract up to 3 risks and append them to the existing `risks` blackboard field
  - extract up to 3 open questions and append them to the existing `open_questions` blackboard field
- in `growth_agent.py`, apply the same logic for:
  - `review_summaries["growth"]`
  - `requested_changes["growth"]`
  - `risks`
  - `open_questions`
- in `product_agent.py`, during the revision pass:
  - read `requested_changes["tech"]` and `requested_changes["growth"]`
  - use them explicitly in the revision input
  - write a short list of applied items into `applied_changes`
  - write a short list of not-applied or still-open items into `rejected_changes`
- in `app/main.py`, update `blackboard.md` so it shows these sections explicitly:
  - `Initial PRD`
  - `Tech Summary`
  - `Tech Requested Changes`
  - `Growth Summary`
  - `Growth Requested Changes`
  - `Applied Changes`
  - `Remaining Open Points`
  - `Risks`
  - `Open Questions`
  - `Final Revised PRD`

## Constraints
- do not redesign the orchestrator
- do not add new agents
- do not introduce a generic parser framework
- use simple deterministic extraction rules only
- keep extraction conservative:
  - if a section is missing, store an empty value instead of guessing
- keep all values as plain Python strings or string lists
- do not add external dependencies
- do not change the brief-loading mechanism

## Acceptance criteria
- a normal run populates `requested_changes` for Tech and Growth
- a normal run populates `risks` and `open_questions` when present in the agent outputs
- Product revision visibly consumes the requested changes
- `blackboard.md` makes the collaboration loop understandable without reading every raw note
- the implementation is based on explicit field mapping, not implicit prose-only interpretation

## Out of scope
- redesigning prompts at a conceptual level
- building a schema-validation layer
- adding unit-test infrastructure
- changing the orchestration order
- solving overall content quality drift in this step

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the structured collaboration contract is now fixed
- the Developer should implement extraction and rendering against this contract, not invent a new one
- prompt/agent strategy decisions are already made in this handoff and should not be re-scoped during implementation

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Use explicit labeled sections in the existing agent outputs as anchors for extraction.
- If the current agent outputs do not already expose stable anchors, stop and report the exact missing anchor instead of improvising a broad parser.
