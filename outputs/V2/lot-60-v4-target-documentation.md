# Lot 60 - V4 Target Documentation

## Objective

Update the project evolution documentation so the V4 target architecture is
clear before any runtime implementation starts.

This lot must not implement V4. It only documents the agreed target and updates
the AI memory files so future developer agents can navigate the change safely.

## Useful Project Context

- The current validated workflow is the historical standard workflow with V3
  prompts.
- V4 is a larger workflow evolution, not a small patch.
- The repository should not be restarted from scratch.
- The V4 target keeps useful existing pieces: LLM client, Mermaid rendering,
  brief selection, generated artifact names, web viewer compatibility, and
  docs/ai navigation.
- V4 introduces a root-level run workspace under `runs/<run_id>/`.
- The system should keep structural genericity through reusable models and
  helpers, but must not become a generic graph-based agent engine.
- Summaries are compressed derivatives of documents. They are never a source of
  truth and must not introduce new information.
- V4 prompts must live in `app/prompts V4/`. V3 must remain untouched.
- Default developer model for later lots: GPT-5.4-mini with high reasoning.

## Files Allowed To Modify

- `Evolutions/update.md`
- `Evolutions/promptArchi.md`
- `docs/ai/system.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/00-index.yaml`
- `README.md` only if a short note avoids a contradiction about V3/V4 status
- `outputs/workflow.md` only if a short forward-looking note is needed

## Files Not To Modify

- `app/`
- `app/prompts V3/`
- `app/prompts V4/`
- `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files relevant to workflow,
   contracts, modules, and rules.
2. Rewrite `Evolutions/update.md` so the target folder structure is explicitly:

```text
runs/<run_id>/
  blackboard/items/
  documents/product/
  documents/tech/
  documents/growth/
  summaries/
  activity_log/
  final_outputs/
```

3. Document that `run_id` is required to avoid multiple runs overwriting each
   other.
4. Document that final historical artifacts are still produced:
   - `prd.md`
   - `architecture.md`
   - `architecture-diagram.mmd`
   - `architecture-diagram.png` when Mermaid rendering succeeds
   - `gtm.md`
   - `blackboard.md`
   - `activity_log.txt`
5. Document the intended summary shape:

```yaml
summary:
  source_document:
  source_hash:
  scope:
  key_decisions:
  unresolved_questions:
  critical_risks:
```

6. Document that summary generation is LLM-based but strictly grounded in a
   single source document.
7. Update `Evolutions/promptArchi.md` to state that V4 separates:
   - stable system prompts;
   - initial project brief prompt;
   - contextual step prompts.
8. Update `docs/ai/*` to describe V4 as the target architecture, not as already
   implemented runtime behavior.
9. Keep V3 documented as the previous validated baseline until a later lot
   validates V4 end to end.

## Expected Behaviors

- A future developer can understand the V4 target without reading the whole
  conversation.
- The documentation makes clear that root-level folders are scoped by
  `runs/<run_id>/`.
- The documentation does not imply that V4 is already implemented.
- The documentation does not tell agents to mutate generated history.

## Acceptance Criteria

- `Evolutions/update.md` reflects the agreed V4 run structure.
- `Evolutions/update.md` explains why summaries are not a source of truth.
- `Evolutions/promptArchi.md` describes system, initial, and contextual prompt
  layers for V4.
- `docs/ai/*` names V4 as the target workflow where appropriate.
- V3 remains described as the current or previous validated baseline, depending
  on wording, but is not modified.
- No runtime code is changed.
- No generated run output is changed.
- No secrets are added.

## Validation Commands

```bash
python3 -m compileall app
git diff -- Evolutions docs/ai README.md outputs/workflow.md
git diff -- app
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Manual Verification Expected

- Read `Evolutions/update.md` and verify that it no longer describes a single
  global `/blackboard` shared by every run.
- Read `Evolutions/promptArchi.md` and verify that V4 prompt layering is clear.
- Read `docs/ai/flows.yaml` and verify that it does not present V4 as validated
  before implementation.
- Verify that generated history and runtime job folders are untouched.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the documentation clear, concise, and practical.
- Do not edit runtime code.
- Do not edit V3 prompts.
- Do not touch generated runs.
- Do not write secrets.
