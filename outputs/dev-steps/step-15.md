# Step 15

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Test a more decision-oriented agent behavior without overwriting the current prompt set, by introducing a separate `prompts V2` folder and switching the app to use it explicitly.

## Files concerned
- `app/prompts V2/product_prompt.md`
- `app/prompts V2/tech_prompt.md`
- `app/prompts V2/growth_prompt.md`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- any prompt-loading helper if one exists

## Architect changes already completed
- created a new prompt set in:
  - `app/prompts V2/product_prompt.md`
  - `app/prompts V2/tech_prompt.md`
  - `app/prompts V2/growth_prompt.md`
- kept the existing prompt files in `app/prompts/` unchanged

## Required behavior
- keep the current prompt set as-is for backward compatibility
- switch the agent code to load prompts from `app/prompts V2/` for this test phase
- ensure all three agents use the V2 prompt set consistently
- do not mix V1 and V2 prompts in the same run

## Intent of V2 prompts
- move from descriptive outputs to decision-ready outputs
- make each agent express critical assumptions more clearly
- surface unresolved critical uncertainties instead of hiding them
- strengthen wedge discipline, MVP proof logic, and launch realism
- add an explicit failure-mode perspective

## Expected implementation
1. Identify where each agent currently loads its prompt file.
2. Update those references so this test uses the corresponding files in `app/prompts V2/`.
3. Keep the change explicit and easy to revert.
4. Do not redesign the workflow in this step.

## Constraints
- do not overwrite or delete the existing prompts in `app/prompts/`
- do not redesign the prompt contents; they are already authored by the Architect
- keep the implementation simple and readable
- avoid introducing a large prompt-management framework
- preserve current behavior outside the prompt source switch

## Acceptance criteria
- the three V2 prompt files exist and are readable by the app
- Product, Tech, and Growth all use the V2 prompt set during the test
- the current V1 prompt files remain untouched
- the code change is explicit enough that we can later compare V1 vs V2 behavior

## Out of scope
- adding new agents
- changing the blackboard structure
- changing the orchestration sequence
- deleting old outputs
- tuning the V1 prompts

## Open questions
- [ ]

## Developer feedback
- [x] The app now loads prompts from `app/prompts V2/` for Product, Tech, and Growth, while the original V1 prompt files remain untouched.

## Developer status
ready_for_review

## Architect decision
- we will test prompt evolution safely by isolating the new prompt set in `app/prompts V2/`
- the developer should only handle the code-side switch to these prompts, not rewrite them
- V1 remains the reference baseline until V2 proves better

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- The goal is not to make the prompts domain-specific.
- The goal is to make the agents more decision-oriented while keeping them generic across projects.
- V1 prompts were left unchanged.
