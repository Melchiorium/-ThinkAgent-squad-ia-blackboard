# Step 9.3

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Refine the prompts only, to reduce over-prescription in Tech outputs and improve the purity of the final PRD without changing any code.

## Files concerned
- `app/prompts/product_prompt.md`
- `app/prompts/tech_prompt.md`
- `app/prompts/growth_prompt.md`

## Required behavior
- tighten `product_prompt.md` so the final PRD remains a pure product deliverable
- explicitly forbid preambles, meta-comments, revision notes, and review-summary leakage in the final PRD
- tighten `tech_prompt.md` so Tech recommends an MVP-fit architecture without jumping too quickly to heavyweight choices
- bias Tech toward proportional decisions based on the brief strength and MVP scope
- keep `growth_prompt.md` aligned with the same level of concreteness and proportion, without major structural changes
- preserve the current section headings used by the extraction workflow

## Prompt design decisions to implement
- `product_prompt.md` must forbid:
  - opening notes such as “this revised PRD reflects...”
  - revision summaries
  - meta commentary
  - any review headings in the final PRD
- `product_prompt.md` must insist on a clean deliverable tone from the first line
- `tech_prompt.md` must prefer:
  - the simplest credible MVP architecture
  - one proportional recommendation
  - low-complexity defaults unless the brief clearly justifies more
- `tech_prompt.md` must explicitly discourage:
  - microservices by default
  - premature scale assumptions
  - broad multi-stack alternatives
- `growth_prompt.md` must keep concrete GTM guidance while staying proportional to the maturity of the brief

## Constraints
- prompts only
- do not change Python code
- do not change parsing logic
- preserve extraction-compatible headings
- keep prompts concise and operational

## Acceptance criteria
- the prompts are updated without code changes
- Product prompt is stricter about final PRD purity
- Tech prompt is stricter about MVP proportionality
- Growth prompt remains concrete but not overbuilt
- the prompts stay compatible with the current structured blackboard flow

## Out of scope
- workflow changes
- parser changes
- blackboard schema changes
- output rendering changes

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- the next correction should come from prompt calibration only
- code remains untouched in this step

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- This step exists specifically to distinguish prompt issues from workflow/code issues.
