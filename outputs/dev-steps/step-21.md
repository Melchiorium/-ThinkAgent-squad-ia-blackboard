# Step 21

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Reduce blackboard redundancy by introducing reusable gap tags with reuse-first behavior, while keeping tag creation possible when no existing tag fits.

## Files concerned
- `app/blackboard.py`
- `app/orchestrator.py`
- `app/main.py`
- any readiness parsing helper if one exists
- any blackboard rendering helper if one exists

## Architect scope
- minimal prompt changes have already been applied by the Architect in `app/prompts V2/`
- no further prompt redesign is requested from the developer in this step
- the developer scope here is technical implementation only

## Context
The blackboard still suffers from repeated gaps and repeated improvements across agents and loops.

Pure text normalization is not reliable enough on its own.

A full closed taxonomy is also too rigid for the current stage.

The chosen direction is therefore:
- reuse existing tags first
- create a new tag only when needed
- validate and track tags in code

## Required behavior
- introduce a lightweight shared tag system for blocking gaps and required improvements
- expose previously known tags to agents during runs when possible
- allow agents to create a new tag only if no existing tag fits
- parse and store the tags separately from the human-readable gap text
- use tags to improve grouping, deduplication, and rendering in `blackboard.md`

## Tagging principle
Each gap or improvement may now carry:
- a short tag in square brackets
- a human-readable description

Example:
- `[privacy_trust] Users may not trust the platform with sensitive information.`

The tag is not the full meaning.
It is only a reusable grouping key.

## Expected implementation
1. Extend parsing so readiness gaps and required improvements can extract:
   - `tag`
   - `text`
2. Maintain a run-level or project-level registry of already known tags.
3. Make existing tags available to the agent input when practical.
4. Validate tags with lightweight rules:
   - short
   - snake_case
   - reusable wording
5. If no valid tag is found:
   - fallback safely
   - optionally store as untagged or `other`
6. Use tags to group related gaps in `blackboard.md`.

## Validation rules
- prefer reuse of an already known tag
- new tags are allowed, but should be exceptional
- tag format should be validated in code
- near-duplicate tags should be visible for human review if detected

## Blackboard expectations
- keep the original text
- store tags separately
- make grouped rendering possible

## Minimum blackboard expectations
- for example:
```python
{
    "readiness": {
        "product": {
            "blocking_gaps": [
                {"tag": "privacy_trust", "text": "..."}
            ],
            "required_improvements": [
                {"tag": "privacy_trust", "text": "..."}
            ],
        },
        "known_tags": [
            "privacy_trust",
            "demand_validation",
            "data_access",
        ],
    }
}
```

## Output expectations
- `blackboard.md` should render grouped gaps more compactly
- repeated issues sharing the same tag should no longer read like fully separate items
- the raw text should still remain visible enough for human interpretation

## Constraints
- do not add a new agent
- do not require a rigid closed taxonomy at this stage
- do not remove the original human-readable gap texts
- keep the implementation explicit and reversible

## Acceptance criteria
- readiness gaps can carry reusable tags
- existing tags are reused when available
- new tags can still be created when needed
- `blackboard.md` becomes less redundant through tag-based grouping
- the system remains understandable to a human reader

## Out of scope
- semantic clustering with advanced NLP
- a fully governed enterprise taxonomy
- replacing all text with tags
- redesigning the correction loop itself

## Open questions
- [ ]

## Developer feedback
- [x] Readiness gaps now carry `tag` and `text` separately, known tags are reused across loops, and `blackboard.md` groups related gaps by tag.

## Developer status
done

## Architect decision
- the goal is not perfect semantic normalization
- the goal is a pragmatic grouping mechanism that is more reliable than free-form text alone
- reuse-first plus controlled creation is the chosen compromise

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step should improve readability and grouping without over-engineering the system.
