# Lot 68e - V4 Contextual Prompt Guardrails

## Objective

Fix the live V4 failure that remains after lot 68d.

The V4 runtime guards are now correctly rejecting invalid blackboard operations,
but the Product prompt still lets the LLM copy a template item line as if it
were a real blackboard operation.

This lot must make the prompt contract and contextual step instructions
unambiguous, then add no-LLM regressions for the exact live failure pattern.

Keep the workflow explicit and readable. Do not introduce a generic prompt
engine or agent graph.

## Useful Project Context

- Lot 68d no-LLM validation passed.
- The representative CareSync live run then failed at:
  `runs/20260513-180526-caresync-bf8154/agent_outputs/product_initial_draft.raw.md`.
- The failure is:
  `field 'targets': invalid value 'TARGET1, TARGET2'`.
- In that raw output, the model copied this template line as an actual item:
  `- TYPE | AUTHOR | TARGET1, TARGET2 | PRIORITY | tag1, tag2 | Title | Content`.
- The same raw output also tried to update `ITEM-001` during `initial_draft`,
  even though no pre-existing item can exist in the first Product draft.
- The runtime behavior from 68d is correct: invalid targets and non-existing
  item updates must fail.
- The remaining correction is prompt/contextual-instruction hardening plus
  regression tests.
- V4 prompts are architect-owned. The developer must not invent prompt text.
  If exact prompt text is missing from this lot, stop and ask the architect.
- Developer model: `GPT-5.4-mini`, reasoning `high`.

## Files Allowed To Modify

- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if a short V4 validation note is needed
- `outputs/workflow.md` only if the V4 contextual prompt behavior needs a
  human-facing explanation
- `outputs/V2/lot-68-v4-batch-validation-and-final-docs.md` only if its
  validation note needs to reference this corrective lot

## Files Not To Modify

- `app/prompts V4/`, unless the architect has already provided an exact patch
  or explicitly asks for a prompt-file edit in this lot
- `app/prompts V3/`
- existing historical runs under `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- existing `runs/` folders manually
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Architect-Owned Prompt Patch

The architect must remove copyable placeholder item bullets from all V4 role
prompts before the next live validation.

Replace this pattern wherever it appears:

```text
`- TYPE | AUTHOR | TARGET1, TARGET2 | PRIORITY | tag1, tag2 | Title | Content`
```

with non-copyable prose such as:

```text
Create-item fields, in order:
TYPE | AUTHOR | ROUTING_TARGETS | PRIORITY | TAGS | TITLE | CONTENT

ROUTING_TARGETS must contain only PRODUCT, GROWTH, TECH, or ALL.
Do not output the field names themselves as an item.
```

Do not add project-specific examples to stable role prompts. Keep the role
prompts general.

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to V4 prompts,
   contracts, flows, modules, rules, and validation.
2. Confirm the architect-owned V4 prompt patch is present:
   - no V4 prompt contains `TARGET1`;
   - no V4 prompt contains a bullet that starts with
     ``- TYPE | AUTHOR |``;
   - no V4 prompt contains a copyable fake create item.
3. If the prompt patch is missing, stop and ask the architect. Do not invent or
   rewrite V4 prompt text yourself.
4. Add explicit contextual step instructions in `app/orchestrator.py`.
   Keep them small, mode-specific, and readable.
5. The contextual instructions must be appended by `_build_v4_user_prompt()`
   before the final return instruction.
6. Use the exact contextual instruction text from this lot. Do not paraphrase it.
7. For `initial_draft`, append exactly:

```text
Contextual step instruction:
- This is the first Product draft for this run.
- No blackboard item exists yet unless it is shown in Open items context.
- In Blackboard Items To Update, write `- None`.
- In Blackboard Items To Create, create only real unresolved questions, risks, decisions, proposals, constraints, warnings, or feedback.
- Do not output template rows, field names, or placeholder values as items.
```

8. For every mode, append exactly:

```text
Blackboard operation reminder:
- In create items, ROUTING_TARGETS must contain only PRODUCT, GROWTH, TECH, or ALL.
- Put topic labels such as pricing, privacy, onboarding, data-model, or compliance in TAGS, not in ROUTING_TARGETS.
- Do not output TYPE, AUTHOR, TARGET1, TARGET2, PRIORITY, TAGS, TITLE, or CONTENT as literal item values.
- Update only item IDs that appear in Open items context or Resolved items context for this step.
- If there is no valid operation, write `- None`.
```

9. Keep stable role prompts general. Do not add stage-specific detail to the
   role prompts.
10. Add no-LLM regression coverage in `scripts/check_v4_flow_no_llm.py` for the
    exact live failure:
    - a raw Product `initial_draft` response containing the copied template line
      must fail before persistence;
    - the error must mention `field 'targets'`;
    - the error must include the run-local raw trace path;
    - a raw Product `initial_draft` response that tries to update `ITEM-001`
      when no item exists must fail before persistence;
    - the error must mention `field 'id'`;
    - a valid Product `initial_draft` with real routing targets and
      `Blackboard Items To Update` set to `- None` must pass.
11. Add a harness assertion that the V4 user prompt for `initial_draft`
    contains the exact `Contextual step instruction` block above.
12. Add a harness assertion that every V4 user prompt contains the exact
    `Blackboard operation reminder` block above.
13. Add a harness assertion that V4 role prompts no longer contain `TARGET1`
    or a copyable ``- TYPE | AUTHOR |`` bullet.
14. Update `docs/ai` memory where the V4 prompt/contextual-prompt contract or
    guardrail changed.
15. Update lot 68 only to mention that the next representative validation is
    blocked on this prompt/contextual-instruction corrective lot.
16. Do not rerun CareSync or LocalLoop live validation until:
    - the architect-owned prompt patch is present;
    - `python3 scripts/check_v4_flow_no_llm.py` passes;
    - `git diff -- "app/prompts V3"` is empty.

## Expected Behaviors

- The LLM no longer sees copyable fake item rows in stable V4 role prompts.
- The first Product draft is explicitly told not to update blackboard items.
- Topic labels are kept in tags instead of routing targets.
- Contextual step instructions guide stage behavior without making stable role
  prompts overly specific.
- Runtime validation still rejects invalid targets and invalid updates.
- The no-LLM harness catches the exact failure seen in the live CareSync run.
- Public final artifacts remain compatible with the existing viewer and
  artifact names.
- V3 prompts remain unchanged.

## Acceptance Criteria

- No file under `app/prompts V4/` contains `TARGET1`.
- No file under `app/prompts V4/` contains a copyable bullet starting with
  ``- TYPE | AUTHOR |``.
- `_build_v4_user_prompt()` includes a clear contextual instruction block for
  `initial_draft`.
- `_build_v4_user_prompt()` includes a blackboard operation reminder for all
  modes.
- Product `initial_draft` is explicitly instructed to write `- None` in
  `Blackboard Items To Update`.
- The no-LLM harness fails a raw response that copies the old template item
  line.
- The no-LLM harness fails a raw Product `initial_draft` response that updates
  `ITEM-001` when no item exists.
- The no-LLM harness passes a valid Product `initial_draft` with concrete
  routing targets and no updates.
- `app/prompts V3/` remains untouched.
- Existing generated history, run folders, environment files, and web job files
  remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
rg -n "TARGET1|^- TYPE \\| AUTHOR \\|" "app/prompts V4" || true
git diff -- app scripts docs/ai README.md outputs/workflow.md outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs .env .env.local
```

Optional real-LLM validation, only after the no-LLM harness passes and the
environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

## Manual Verification Expected

- Read all V4 role prompts and verify they contain no copyable fake item row.
- Verify stable role prompts remain general and do not contain stage-specific
  workflow detail.
- Read the V4 user prompt builder and verify contextual instructions are small,
  mode-specific, and appended consistently.
- Verify the `initial_draft` contextual instruction forbids item updates.
- Verify the blackboard operation reminder tells agents to use routing targets
  only for routing, and tags for topics.
- Verify the no-LLM harness covers the exact live failure from
  `product_initial_draft.raw.md`.
- Verify no V3 prompt file changed.
- Verify no existing generated run was manually edited.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the V4 workflow explicit in Python.
- Keep stable role prompts general.
- Use contextual step instructions for stage-specific behavior.
- Do not let the developer invent prompt text.
- Do not introduce a generic prompt engine or graph engine.
- Do not modify V3 prompts.
- Do not manually edit generated run history.
- Do not touch `.env` or `.env.local`.
- Do not print real credentials.

## Validation Attempt

- The no-LLM harness passed after the contextual prompt blocks, prompt guardrails,
  and parser hardening were added.
- A single representative live run was then started with:

  ```bash
  set -a; source .env; export BLACKBOARD_PROMPT_VERSION=V4; export BLACKBOARD_PROJECT_NAME=CareSync; set +a; python3 app/main.py
  ```

- LocalLoop was not started.

## Failure Report

- The representative CareSync run now gets past the initial Product draft and
  then fails while generating the PRD summary.
- The failure is:
  `ValueError: Unexpected summary field: - MVP core features defined`
- The blocker comes from the summary parser in `app/run_summaries.py`, not from
  the V4 prompt guardrails that this lot hardens.
- The next architect step is to inspect the summary prompt / summary parser
  contract so the generated summary remains strict YAML instead of emitting a
  bullet line.
- Corrective lot 68f now covers this summary-contract blocker, including raw
  summary traces, stricter parser errors, and no-LLM regressions for malformed
  summary YAML.
- Representative live validation is now blocked on 68f, not on 68e.
