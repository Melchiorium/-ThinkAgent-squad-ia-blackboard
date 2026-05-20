# Lot 68j - V4 Final Artifact Quality Gate And Mermaid PNG Preflight

## Objective

Make final artifact completeness visible and prevent successful V4 runs from
hiding missing critical artifacts such as `architecture-diagram.png`.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- Version 63 produced Mermaid source but no PNG because Chrome/Puppeteer was
  missing.
- The PNG is currently conditional, but quality evaluation treats the missing
  visual artifact as an incomplete delivery.
- The runtime should distinguish a valid Markdown run from a fully rendered
  deliverable set.

## Files Allowed To Modify

- `app/architecture_render.py`
- `app/artifact_writer.py`
- `scripts/check_v4_flow_no_llm.py`
- `README.md`
- `outputs/workflow.md`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `outputs/V2/lot-68j-v4-final-artifact-quality-gate-and-mermaid-png-preflight.md`
  for implementation notes

## Files Not To Modify

- `node_modules/`
- `.cache/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/prompts V3/`
- `app/promptsV5/`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then V4 output/rendering memory.
2. Inspect the current Mermaid rendering flow in `app/architecture_render.py`
   and final artifact compilation in `app/artifact_writer.py`.
3. Add or document a deterministic Mermaid renderer preflight command that
   checks Mermaid CLI and the Puppeteer browser cache without modifying tracked
   files.
4. Ensure missing Chrome/Puppeteer is reported as a concise artifact-quality
   warning with an actionable remediation command.
5. Add final-output metadata or activity-log wording that distinguishes:
   - Markdown artifacts ready;
   - Mermaid source ready;
   - PNG render ready;
   - PNG render failed with actionable reason.
6. Keep `architecture-diagram.mmd` generation independent from PNG generation.
7. Do not vendor browser binaries, modify `node_modules/`, or commit `.cache/`.
8. Add no-LLM harness coverage for PNG render failure metadata without
   requiring Chrome to be installed.
9. Update `README.md`, `outputs/workflow.md`, and `docs/ai` memory with the
   preflight command and the expected warning behavior.

## Expected Behaviors

- Missing PNG is not silent.
- A future evaluator can clearly see whether architecture visual rendering
  passed, failed, or was skipped.
- Mermaid source still exists when PNG rendering fails.
- The code does not vendor browser binaries or edit cache folders.

## Acceptance Criteria

- Failure to render PNG records a concise actionable warning.
- Final artifact state distinguishes Markdown readiness, Mermaid source
  readiness, and PNG readiness.
- No-LLM harness validates render-warning propagation.
- Docs include a reproducible preflight or install command for the required
  Puppeteer browser cache.
- No generated history or cache artifacts are committed.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
git status --short outputs/tests outputs/web-jobs runs node_modules .cache app/promptsV5
```

## Manual Verification Expected

- Inspect final artifact metadata in a fake run.
- Confirm `architecture-diagram.mmd` remains available when PNG rendering
  fails.
- Confirm warning text is actionable but does not print secrets or environment
  values.
- Confirm no generated run or cache artifact is committed.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Do not modify generated history.
- Do not add dependencies unless strictly necessary.
- Do not touch `.env`, `.env.local`, `outputs/web-jobs/`, `node_modules/`,
  `.cache/`, or V3 prompts.
