# Lot 67 - V4 Web Generation Compatibility

## Objective

Connect the V4 generation workflow to the existing web generation service while
preserving the current browser-facing behavior.

The web flow must remain:

```text
project title -> brief -> generation -> inline result
```

## Useful Project Context

- The web POC is Flask-based.
- Web jobs are persisted through the active web storage backend.
- The web viewer reads generated run artifacts from the existing public output
  contract.
- V4 internal run workspaces should not require a new user-facing route unless
  necessary.
- Existing access-token behavior and storage readiness behavior must remain
  unchanged.

## Files Allowed To Modify

- `app/web.py`
- `app/generation_service.py`
- `app/web_presenters.py`
- `app/web_storage.py` only if needed for artifact compatibility
- `app/web_progress.py` only if V4 progress stages require minor naming updates
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/contracts.yaml`

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/` manually
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `docs/supabase-schema.sql` unless a documented storage need requires it

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to web generation,
   web storage, presenters, progress, and generation service.
2. Make `run_generation_from_brief` use the V4 workflow when
   `BLACKBOARD_PROMPT_VERSION=V4` or when V4 is the documented active default.
3. Preserve the current public run output shape consumed by the web viewer.
4. Keep routes stable:
   - home page;
   - job creation;
   - job status;
   - API job status;
   - run detail;
   - artifact serving.
5. Preserve access-token behavior.
6. Preserve job status and progress behavior as much as possible.
7. Do not expose internal `runs/<run_id>/` paths unless there is a clear
   internal diagnostic need.
8. Ensure web generated results still display PRD, Architecture, GTM, Mermaid,
   blackboard, and activity log inline.
9. Update docs/ai memory to document V4 web generation flow.

## Expected Behaviors

- A web-submitted brief can run through V4.
- The result page displays the same public artifact sections as before.
- Existing session job history behavior remains intact.
- No secrets or internal connection strings are exposed.
- Runtime web job files remain ignored by git.

## Acceptance Criteria

- Web generation can create a run using V4.
- `/jobs/<job_id>` shows inline generated artifacts after completion.
- `/api/jobs/<job_id>` does not expose raw brief text.
- Existing run detail pages still work.
- `outputs/web-jobs/` remains clean in git status.
- V3 prompts are unchanged.

## Validation Commands

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); print(c.get('/healthz').status_code)"
git diff -- app docs/ai
git diff -- "app/prompts V3"
git status --short outputs/web-jobs
```

## Manual Verification Expected

- Run the web app locally when environment variables are available.
- Submit a short title and brief.
- Verify the job page progresses and then displays generated artifacts inline.
- Verify public run links still open.
- Verify no `runs/<run_id>` raw internal path is exposed unnecessarily.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep web behavior generation-first.
- Do not introduce full authentication.
- Do not change Supabase schema unless explicitly required.
- Do not modify V3 prompts.
- Do not touch generated run history manually.
