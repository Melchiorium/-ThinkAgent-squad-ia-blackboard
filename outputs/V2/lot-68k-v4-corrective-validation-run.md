# Lot 68k - V4 Corrective Validation Run And Quality Audit

## Objective

Run one controlled CareSync V4 validation after lots 68h, 68i, and 68j pass,
then audit whether the version 63 findings are fixed.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- This lot validates behavior. It should not make broad code or prompt
  changes.
- The next live run must use `gpt-5.4-mini`.
- If the live run fails, stop immediately and perform review before any retry.
- The version 63 findings to verify are:
  - resolved item-resolution decisions missing from final documents;
  - invented external market/compliance decisions;
  - duplicate external blackboard items;
  - inaccurate resolution loop telemetry;
  - missing or unclear Mermaid PNG artifact status.

## Files Allowed To Modify

- `outputs/V2/lot-68k-v4-corrective-validation-run.md` for validation notes
- `README.md` only if validation status documentation needs correction
- `outputs/workflow.md` only if validation status documentation needs
  correction
- `docs/ai/*.yaml` only if validation status documentation needs correction

## Files Not To Modify

- `app/`, except for a small documented fix required by validation
- `app/prompts V3/`
- `.env`
- `.env.local`
- existing historical runs
- `outputs/web-jobs/`
- `app/promptsV5/`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then V4 flow, contract, rules, and output
   memory.
2. Confirm lots 68h, 68i, and 68j are implemented and their static validations
   pass.
3. Run static validations before any live run.
4. Run exactly one live CareSync V4 generation with:
   - `BLACKBOARD_PROMPT_VERSION=V4`;
   - `BLACKBOARD_PROJECT_NAME=CareSync`;
   - `OPENAI_MODEL=gpt-5.4-mini`.
5. If the live run fails, stop. Do not relaunch. Document:
   - failing stage;
   - raw trace path;
   - suspected code or prompt boundary;
   - corrective plan needed before retry.
6. If the live run succeeds, audit final artifacts for:
   - resolved blackboard decisions present in final documents;
   - no invented external market/compliance decisions;
   - no duplicate `EXTERNAL` items;
   - truthful activity log loop status;
   - visible Mermaid PNG status;
   - coherent PRD, GTM, and Architecture.
7. Add validation notes to this lot file only if useful for handoff.
8. Do not manually edit generated outputs.

## Expected Behaviors

- One controlled run provides evidence that the corrective lots worked.
- The audit explicitly checks the version 63 regressions.
- Any failure triggers review and a corrective plan, not trial-and-error.
- Generated public artifacts remain compatible with the existing viewer.

## Acceptance Criteria

- Static checks pass before the live run.
- At most one live run is executed.
- Audit confirms or rejects each fixed finding explicitly.
- Validation notes are clear enough for the next architect or developer.
- No generated outputs are manually patched after the run.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
set -a; source .env; export BLACKBOARD_PROMPT_VERSION=V4; export BLACKBOARD_PROJECT_NAME=CareSync; export OPENAI_MODEL=gpt-5.4-mini; set +a; python3 app/main.py
```

## Manual Verification Expected

- Compare the latest final `prd.md` with resolved item-resolution traces.
- Inspect `blackboard.md` for duplicate `EXTERNAL` items.
- Inspect `activity_log.txt` for accurate loop changes.
- Inspect architecture diagram source and PNG or render-warning status.
- Inspect final PRD, GTM, and Architecture for cross-document coherence and
  absence of fabricated external decisions.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Stop after the first live failure.
- Do not manually edit generated outputs.
- Do not touch V3 prompts.
- Do not touch `.env`, `.env.local`, `outputs/web-jobs/`, historical runs, or
  `app/promptsV5/`.

## Validation Note

- Static validations passed after lots 68h-68j implementation:
  - `python3 -m compileall app scripts/check_v4_flow_no_llm.py`
  - `python3 scripts/check_v4_flow_no_llm.py`
  - `git diff --check`
- One live CareSync V4 run was launched with `OPENAI_MODEL=gpt-5.4-mini`.
- Run id: `20260517-172731-caresync-792c05`.
- The run failed during `growth_verification` blackboard application because
  Growth attempted to create an `EXTERNAL` launch-market/compliance item that
  duplicated `ITEM-011`, already created by Product verification.
- Review conclusion: duplicate detection was correct, but failing the whole run
  was too strict for multi-agent verification. Runtime application should reuse
  the existing open item and log the duplicate instead of persisting another
  item or aborting.
- Corrective patch applied after the failed run: `_apply_v4_item_operations(...)`
  now logs `blackboard_duplicate_item_reused` and skips duplicate persistence
  while `create_item(...)` still rejects direct duplicate writes.
- No second live run was launched after this failure, per the one-run and
  review-before-retry rule.
