# Step 17.2

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Improve the effectiveness of the `LIMITED` correction loop by introducing correction-task ownership, gap deduplication, and more actionable correction tasks.

## Files concerned
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/main.py`
- any correction-loop helper if one exists

## Architect scope
- no prompt rewrite is requested from the developer in this step
- no agent-role redesign is requested from the developer in this step
- if an agent-behavior change becomes necessary later, it remains an Architect responsibility
- the developer scope here is technical implementation only

## Context
`Step 17.1` introduced a bounded correction loop for `LIMITED` dossiers.

The mechanism works, but the current correction tasks are still too weak:
- repeated gaps are often duplicated across Product, Tech, and Growth
- tasks are often phrased too generically
- ownership is implicit, which makes responsibility blurry
- the loop improves structure more than decision quality

## Required behavior
- improve the correction-loop planner before tasks are sent back to agents
- deduplicate or merge overlapping gaps before issuing correction tasks
- cap the number of priority correction themes per loop
  - recommended: `2` or `3`
- give each correction task a single explicit owner
- optionally allow contributors, but never more than one owner
- make correction tasks more decision-oriented and operational

## Ownership model
- `Product` owns:
  - wedge clarity
  - target segment clarity
  - MVP scope discipline
  - business model hypothesis
  - recommendation maturity (`research`, `pilot`, `build`, `revise`, `reject`)
- `Tech` owns:
  - feasibility gaps
  - reliability/control/data/permission gaps
  - operational or compliance constraints affecting buildability
- `Growth` owns:
  - market bottleneck gaps
  - acquisition-motion gaps
  - activation / supply-demand / trust / repeatability gaps
- `Product` remains the final arbiter after corrections

## Correction task contract
Each correction task should contain at least:
- `owner`
- `task`
- `source_gap`
- `expected_output`

Optional:
- `contributors`

For example:
```python
{
    "owner": "growth",
    "task": "Replace the broad acquisition plan with one concrete concierge pilot motion for one launch segment.",
    "source_gap": "Acquisition path remains too vague.",
    "expected_output": "One primary acquisition motion with basic operating assumptions and a success threshold.",
    "contributors": ["product"],
}
```

## Expected implementation
1. Review how `blocking_gaps` and `required_improvements` are currently aggregated.
2. Add a normalization/deduplication pass before correction tasks are generated.
3. Build a small correction-task planner that:
   - groups similar issues
   - selects only the highest-priority correction themes
   - assigns one owner per task
   - generates a more actionable task sentence
4. Update the correction loop so tasks are routed according to ownership.
5. Preserve Product as the final synthesis and arbitration step after corrections.
6. Render correction task ownership clearly in `blackboard.md`.

## Blackboard expectations
- extend the correction task trace so each task stores ownership explicitly
- preserve readability for humans
- keep the structure machine-friendly

## Minimum blackboard expectations
- for example:
```python
{
    "readiness": {
        "correction_tasks": [
            {
                "loop": 1,
                "owner": "product",
                "task": "...",
                "source_gap": "...",
                "expected_output": "...",
                "contributors": [],
            }
        ]
    }
}
```

## Output expectations
- `blackboard.md` should show:
  - deduplicated correction themes
  - who owns each correction
  - what each correction is expected to resolve
  - the updated readiness after correction
- the output should make it clear that the loop is coordinated, not just repeated

## Constraints
- do not ask the developer to redesign prompts
- do not ask the developer to redesign agent responsibilities
- do not introduce free-form agent-to-agent chat
- keep the loop bounded as already defined
- keep the implementation explicit and deterministic

## Acceptance criteria
- correction tasks are no longer raw duplicated gap strings
- each correction task has one explicit owner
- only a small number of prioritized correction themes are sent per loop
- `blackboard.md` makes task ownership and purpose understandable
- Product still performs final arbitration after corrections

## Out of scope
- prompt redesign
- changing model provider
- removing the readiness system
- unlimited correction loops
- changing the CEO second-pass workflow
- adding a separate evaluator agent

## Open questions
- [ ]

## Developer feedback
- [x] Correction tasks are now deduplicated, owned explicitly, and prioritized before being routed back to agents.
- [x] Validation run on `outputs/tests/SkillBridge/version 2/` confirms the task planner outputs dedicated owners and merged themes.

## Developer status
done

## Architect decision
- the main weakness is no longer the existence of the correction loop, but the quality and ownership of the tasks inside it
- the loop must become more selective, more explicit, and more accountable
- Product remains the final decision-maker even when another agent owns a correction task

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step is about improving correction-task quality, not about adding more loops.
- If later needed, a future step can refine prioritization heuristics or add a small correction-task taxonomy.
