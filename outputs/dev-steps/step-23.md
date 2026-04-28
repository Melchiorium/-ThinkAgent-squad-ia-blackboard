# Step 23

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Make the Tech contribution reliable end-to-end by fixing Tech readiness capture in the blackboard and ensuring consistency between `architecture.md` and the visual architecture deliverable.

## Files concerned
- `app/orchestrator.py`
- `app/main.py`
- `app/blackboard.py`
- any readiness parsing helper if one exists
- any architecture rendering/export helper if one exists

## Architect scope
- no prompt redesign is requested from the developer in this step
- the current issue appears to be technical reliability, not agent role definition
- the developer scope here is implementation and output consistency only

## Context
Recent runs show a useful but incomplete improvement:
- `Tech` contributes better upstream decisions
- evaluation quality improves slightly
- but the pipeline still shows reliability issues on the Tech path

Observed problems:
- `Tech Status` can be empty in `blackboard.md` even when the architecture deliverable exists
- `architecture.pdf` can be materially poorer than `architecture.md`
- the blackboard can therefore under-represent the actual technical contribution

This creates two risks:
- Product arbitration is made on incomplete technical signals
- evaluation quality penalizes delivery inconsistency rather than just project quality

## Required behavior
- ensure the Tech readiness block is always parsed and stored when present
- ensure missing Tech readiness is visible as a technical parsing/export issue, not silently treated as empty
- ensure the visual architecture deliverable reflects the key structure of `architecture.md`
- preserve enough raw Tech output for debugging when inconsistencies occur

## Expected implementation
1. Audit the Tech parsing path and guarantee that `Technical Readiness` is captured when returned by the agent.
2. If the Tech readiness block is missing or unparsable:
   - record a clear fallback state
   - surface the issue in the blackboard or activity log
   - do not leave the Tech section silently empty
3. Audit the architecture rendering path so the generated `architecture.pdf` or image includes:
   - main blocks
   - main flows
   - external systems
   - admin / ops control points
4. Add a lightweight consistency check between `architecture.md` and the rendered diagram source.
5. If the diagram source is too poor to render a meaningful visual:
   - fail clearly
   - or emit a visible warning
   - but do not silently produce a low-information artifact

## Minimum blackboard expectations
- for example:
```python
{
    "readiness": {
        "tech": {
            "status": "LIMITED",
            "blocking_gaps": [...],
            "required_improvements": [...],
            "parse_warning": ""
        }
    },
    "artifacts": {
        "architecture_markdown_ready": True,
        "architecture_visual_ready": True,
        "architecture_visual_warning": ""
    }
}
```

## Output expectations
- `blackboard.md` should never show an empty Tech section when a Tech output was actually produced
- `activity_log.txt` should help explain parsing or rendering failures
- `architecture.pdf` should no longer contradict `architecture.md` on the presence of flows or control points

## Constraints
- do not add a new agent
- do not redesign the architecture prompt in this step
- do not redesign the readiness model
- keep the implementation explicit and debuggable

## Acceptance criteria
- Tech readiness is reliably captured or clearly flagged as missing
- `blackboard.md` no longer silently drops the Tech contribution
- visual architecture output is materially aligned with `architecture.md`
- inconsistencies become diagnosable from artifacts or logs

## Out of scope
- a new Product-only locking pass
- additional prompt tuning
- major blackboard redesign

## Open questions
- [ ]

## Developer feedback
- [x] Tech readiness now carries an explicit parse warning when needed, artifacts expose architecture markdown/visual readiness, and the Lila run confirms the visual output is aligned with the markdown structure.

## Developer status
done

## Architect decision
- the next bottleneck is not role definition
- it is the reliability of the Tech signal through parsing, storage, and rendering
- this must be fixed before adding more workflow sophistication

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Once the Tech path is reliable, a short Product-only locking pass may become the next best improvement.
