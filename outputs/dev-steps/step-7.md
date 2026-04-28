# Step 7

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Separate the internal agent blackboard from the human-readable reporting layer, so agents work on a structured machine-friendly state and `blackboard.md` becomes a derived human view.

## Files concerned
- `app/blackboard.py`
- `app/agents/product_agent.py`
- `app/main.py`

## Required behavior
- evolve the blackboard structure so the internal state is clearly machine-friendly and stable for agent collaboration
- keep the internal blackboard as plain Python structures that remain easily serializable to JSON if needed
- preserve the product draft before revision in dedicated blackboard data instead of relying only on final rendered text
- add structured revision-trace fields so the system can store:
  - the initial PRD state
  - the inputs coming from tech and growth review
  - a compact summary of what changed during the product revision
- update `product_agent.py` so the revision pass writes those structured trace fields into the internal blackboard
- update `app/main.py` so `outputs/blackboard.md` is produced by translating the internal blackboard into a human-readable report
- the Markdown rendering must present a clear collaboration story for a human reader:
  - initial PRD
  - tech input
  - growth input
  - final revised PRD
  - revision summary
- keep `blackboard.md` as the main readable artifact
- do not require agents to exchange in Markdown-oriented structures

## Constraints
- preserve the current architecture: explicit orchestrator plus shared blackboard
- use simple dictionary/list/string fields only
- no external dependency
- no generic diff engine
- no UI/frontend work
- do not redesign the full agent flow
- the internal blackboard should stay concise and operational for agents first
- the human-readable layer should be a rendering step, not the primary working format

## Acceptance criteria
- the internal blackboard contains structured collaboration data beyond the final PRD only
- the initial and revised PRD states are both preserved in the blackboard
- the product revision step records structured revision information
- `outputs/blackboard.md` is clearly derived from the internal blackboard and is easier for a human to follow
- a reader can understand what changed after tech and growth review without reading raw internal structures
- the implementation remains simple and maintainable

## Out of scope
- full prompt redesign for all agents
- automatic semantic diffing
- making `blackboard.json` a mandatory deliverable
- changing the input brief source
- adding new agents or new orchestration steps
- building a validation schema framework

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- agent collaboration should optimize for machine-readable stability, not human presentation
- human readability should come from a dedicated rendering layer built on top of the internal blackboard
- `blackboard.json` remains optional and only useful as a debug artifact, not as the primary human output

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Prefer a compact internal revision structure plus a dedicated Markdown renderer over mixing agent state and presentation concerns.
