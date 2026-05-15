# Lot 68 - V4 Batch Validation And Final Documentation

## Objective

Validate the completed V4 workflow on representative projects and update the
human and AI-facing documentation to mark V4 as the active baseline only after
evidence exists.

## Useful Project Context

- Recommended first validation projects are `CareSync` and `LocalLoop`.
- Real LLM runs require valid OpenAI-compatible environment variables.
- V4 should produce both internal run workspaces and historical public
  artifacts.
- Documentation must not claim success for a validation that was not actually
  run.
- V3 remains useful as historical reference.

## Files Allowed To Modify

- `README.md`
- `outputs/workflow.md`
- `docs/ai/system.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `docs/ai/00-index.yaml`
- `outputs/V2/` if validation notes need to be added to this lot file

## Files Not To Modify

- `app/`, except small corrective fixes that are directly required for V4
  validation and are documented in the final notes
- `app/prompts V3/`
- existing historical runs under `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to generation,
   contracts, flows, rules, and outputs.
2. Confirm V4 is wired as intended.
3. Run a V4 generation for `CareSync` if LLM environment variables are
   configured. Runs may take several minutes per agent.
4. Run a V4 generation for `LocalLoop` if LLM environment variables are
   configured.
5. Inspect the generated `runs/<run_id>/` workspaces:
   - documents;
   - summaries;
   - blackboard items;
   - activity log;
   - final outputs.
6. Inspect the generated public output folders under `outputs/tests/`.
7. Verify the final artifacts:
   - `prd.md`
   - `architecture.md`
   - `architecture-diagram.mmd`
   - `architecture-diagram.png` when available
   - `gtm.md`
   - `blackboard.md`
   - `activity_log.txt`.
8. Update documentation to describe:
   - V4 as the active baseline only if validation succeeded;
   - V3 as historical baseline;
   - run workspace structure;
   - commands to run V4;
   - remaining limitations.
9. If validation cannot run because environment variables are missing, document
   that V4 implementation is ready but validation is blocked by configuration.
10. Do not hide known limitations or unresolved workflow risks.

## Expected Behaviors

- V4 can be validated on at least two representative briefs when LLM access is
  available.
- Documentation reflects the real validation status.
- A future agent can reproduce the validation commands.
- Generated V4 internals and public artifacts are coherent.

## Acceptance Criteria

- `CareSync` and `LocalLoop` V4 runs complete, or the blocker is documented
  clearly.
- Internal V4 run folders contain documents, summaries, items, activity log,
  and final outputs.
- Public output folders contain the historical artifacts.
- `blackboard.md` clearly represents V4 coordination state.
- Documentation no longer points to V3 as active if V4 is validated.
- Documentation does not claim unverified results.
- V3 prompts remain unchanged.
- Runtime job files remain ignored.

## Validation Commands

```bash
python3 -m compileall app
# Run only when LLM environment variables are configured:
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=LocalLoop python3 app/main.py
git diff -- README.md outputs/workflow.md docs/ai outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/web-jobs
```

## Manual Verification Expected

- Read the CareSync V4 PRD, architecture, GTM, blackboard, and activity log.
- Read the LocalLoop V4 PRD, architecture, GTM, blackboard, and activity log.
- Verify summaries do not contain information absent from their source
  documents.
- Verify open items are surfaced during finalization.
- Verify documentation describes the actual validation status.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Do not mark V4 as validated unless the validation actually ran.
- Do not modify V3 prompts.
- Do not rewrite generated history manually.
- Do not commit secrets or print real credentials.

## Validation Note

- The repository `.env` traces `OPENAI_API_KEY` and `OPENAI_MODEL`; the shell
  must `source .env` before running the V4 validation commands.
- `OPENAI_BASE_URL` is only required when the validation uses a non-default
  OpenAI-compatible endpoint.
- The V4 runtime code and no-LLM harness are in place, but the representative
  CareSync validation run was still blocked at the V4 document-validation
  boundary before corrective lot 68d. The current failure happened in the
  `product` `item_resolution` trace at
  `runs/20260513-165821-caresync-6d1282/agent_outputs/product_item_resolution_02.raw.md`.
  LocalLoop was not run after the first representative failure because the
  user asked to stop after the first run.

## Failure Report

- The CareSync V4 run started successfully after `source .env`,
  `BLACKBOARD_PROMPT_VERSION=V4`, and `BLACKBOARD_PROJECT_NAME=CareSync`.
- The earlier blackboard item type blocker was addressed by lots 68b and 68c,
  but the current representative run now fails later, in the V4 document
  validation boundary that lot 68d hardens.
- The exception comes from `app/v4_parsing.py:validate_v4_document()`: the
  `product` `item_resolution` response is missing or empty for the required
  internal section `Blackboard Items To Create`.
- The failing trace is
  `runs/20260513-165821-caresync-6d1282/agent_outputs/product_item_resolution_02.raw.md`.
- This is still a runtime contract failure, not a viewer issue.
- The next step for the architect is to inspect the updated 68d harness and
  then rerun the representative LLM validation from `.env` if the runtime
  boundary checks are now green. The next representative attempt is now
  blocked on corrective lot 68f, which hardens the summary contract after the
  prompt/contextual guardrails from 68e.
- Corrective lot 68d now covers the follow-up defects found in this failed
  run: normalized internal section parsing, cross-role document pollution,
  readiness placeholder rejection, explicit item routing, update validation
  for pre-existing item IDs, and the broader live-output boundaries.
- Corrective lot 68f now covers the later summary-contract blocker found after
  68e: malformed PRD summary YAML and missing raw summary traces on failure.
- Corrective lot 68g now covers the next Growth review blocker: create/update
  item operation confusion caused by `ITEM-###` ids appearing in create-item
  rows and pipe-delimited item context that can be copied by the model.
