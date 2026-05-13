# Lot 66 - V4 Final Output Compilation

## Objective

Compile a completed V4 run into the historical artifact set expected by the
repository and web viewer.

This lot bridges the new internal run structure with the existing public output
contract.

## Useful Project Context

- Existing public artifacts are written under
  `outputs/tests/<Project>/version X/`.
- The web viewer expects familiar files such as `prd.md`, `architecture.md`,
  `gtm.md`, `blackboard.md`, and `activity_log.txt`.
- Mermaid rendering currently writes `architecture-diagram.mmd` and optionally
  `architecture-diagram.png`.
- V4 final outputs must come from the V4 run workspace, not from the old
  aggregated blackboard dictionary.

## Files Allowed To Modify

- `app/artifact_writer.py`
- `app/architecture_render.py` only if needed
- `app/generation_service.py`
- V4 helper modules added by earlier lots
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/` manually
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- Mermaid config unless rendering behavior truly requires it

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to artifact writing,
   contracts, flows, and rendering.
2. Add a V4 finalization or compilation helper.
3. Select latest validated documents from the V4 run workspace:
   - latest Product PRD;
   - latest Tech architecture;
   - latest Growth GTM.
4. Write compiled files under `runs/<run_id>/final_outputs/`.
5. Copy or render the same final output set into
   `outputs/tests/<Project>/version X/` through the existing generation output
   path.
6. Preserve historical artifact names:
   - `project-brief.md`
   - `prd.md`
   - `architecture.md`
   - `architecture-diagram.mmd`
   - `architecture-diagram.png` when Mermaid rendering succeeds
   - `gtm.md`
   - `blackboard.md`
   - `activity_log.txt`
   - `evaluator-report.md` when provided.
7. Generate `blackboard.md` from V4 items, item statuses, decisions, summaries,
   and activity logs.
8. Explicitly surface remaining open items as open questions or unresolved
   points in final human-readable output.
9. Keep Mermaid rendering behavior compatible with the existing renderer.
10. Update docs/ai contracts and flows to document the V4-to-public-artifact
    compilation path.

## Expected Behaviors

- The new V4 internals remain inspectable under `runs/<run_id>/`.
- The public generated output remains compatible with existing tooling.
- Open questions do not disappear during finalization.
- Mermaid artifacts continue to be produced when a valid diagram exists.

## Acceptance Criteria

- A V4 run produces `final_outputs/`.
- The public output directory contains the expected historical artifact files.
- `blackboard.md` reflects V4 items and activity, not only old dictionary
  fields.
- Remaining open items are visible in final outputs.
- The web viewer can still read run artifacts without major route changes.
- V3 prompts are unchanged.

## Validation Commands

```bash
python3 -m compileall app
npm run mmdc -- -h
# Run only when LLM environment variables are configured:
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
git diff -- app docs/ai
git diff -- "app/prompts V3"
git status --short outputs/web-jobs
```

## Manual Verification Expected

- Open the generated `outputs/tests/<Project>/version X/` folder.
- Verify all expected artifact files exist.
- Read `blackboard.md` and confirm it includes V4 item status and activity.
- Verify unresolved questions are still visible.
- Verify the Mermaid source is present and the PNG is generated when local
  tooling is available.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Preserve generated history; do not patch old runs manually.
- Keep the public artifact contract stable.
- Do not modify V3 prompts.
- Do not hide unresolved questions during finalization.
