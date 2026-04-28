# Step 19

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Generate a visual architecture deliverable from the Tech output, so the architecture result is no longer only a Markdown note but also a real schema export in image or PDF form.

## Files concerned
- `app/main.py`
- `app/agents/tech_agent.py`
- any architecture-render helper if one exists
- any output/export helper if one exists

## Architect scope
- the Tech prompt has already been adjusted to produce a macro architecture and a `Diagram Blueprint`
- no prompt rewrite is requested from the developer in this step
- the developer scope here is technical implementation only

## Context
The expected deliverables include:
- final PRD
- architecture + schemas
- GTM plan

At the moment, `architecture.md` is still only a textual note.

The system now needs a true visual architecture artifact derived from the Tech output.

## Required behavior
- keep the existing `architecture.md` export
- additionally generate a visual architecture artifact from the Tech output
- the visual artifact may be:
  - `PNG`
  - `JPG`
  - or `PDF`
- the rendering must be based on the macro structure described in the Tech output, especially the `Diagram Blueprint`

## Expected implementation
1. Read the Tech output after generation.
2. Extract the architecture information needed for a macro schema.
3. Build a renderable diagram representation from that structure.
4. Export at least one visual architecture file alongside the text architecture output.
5. Keep the export path explicit and versioned with the rest of the run outputs.

## Acceptable output shape
For a run folder such as:
- `outputs/tests/<Project>/version X/`

The run may now contain:
- `architecture.md`
- `architecture.png`
or
- `architecture.pdf`

If both are easy to support, that is acceptable, but only one visual export is required for this step.

## Diagram expectations
- the diagram should stay macro-level
- it should reflect:
  - main system blocks
  - major flows
  - external actors or systems
  - admin or operations control points when relevant
- it does not need to show low-level classes, endpoints, or infrastructure internals

## Constraints
- do not ask the developer to redesign the Tech prompt
- do not over-engineer a complex diagramming system
- prefer a simple, robust rendering pipeline
- keep the implementation readable and explicit
- preserve the current text export in addition to the visual one

## Acceptance criteria
- a run produces `architecture.md` as before
- a run also produces one visual architecture artifact (`PNG`, `JPG`, or `PDF`)
- the visual artifact is derived from the Tech output, not handwritten manually outside the pipeline
- the resulting schema is macro-level and understandable by a non-technical stakeholder

## Out of scope
- redesigning the full architecture prompt
- producing multiple diagram types
- generating polished slideware
- redesigning the whole output pipeline

## Open questions
- [ ]

## Developer feedback
- [x] The run now exports a visual architecture PDF derived from the Tech output blueprint.

## Developer status
done

## Architect decision
- the textual architecture note remains useful, but it is no longer sufficient as the only architecture deliverable
- the diagram should be generated from the Tech output, not authored manually after the fact
- the target is a macro architecture schema, not a detailed engineering design diagram

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- The goal is to bridge architecture reasoning and stakeholder-readable visual output.
