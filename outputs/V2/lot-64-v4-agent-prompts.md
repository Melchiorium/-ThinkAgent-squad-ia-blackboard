# Lot 64 - V4 Agent Prompts

## Objective

Create the V4 Product, Growth, and Tech prompts that support the new
blackboard-first workflow.

This lot creates prompt files and contracts only. It must not rewrite the full
runtime orchestration.

## Useful Project Context

- V3 prompts are the previous validated baseline and must remain unchanged.
- V4 prompts must live under `app/prompts V4/`.
- V4 separates:
  - stable system prompts;
  - the initial project brief;
  - contextual step prompts built by the orchestrator.
- Agents collaborate through documents, blackboard items, summaries, and
  activity logs.
- Product remains the final arbiter.
- Tech and Growth remain structured challengers.

## Files Allowed To Modify

- `app/prompts V4/`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `app/agents/` only if a minimal prompt-loading helper is absolutely needed

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to prompts, agent
   behavior, contracts, and parser expectations.
2. Create V4 prompt files for:
   - Product;
   - Growth;
   - Tech;
   - summary generation if not already created in Lot 63.
3. Preserve agent responsibilities:
   - Product owns PRD framing, arbitration, MVP scope, and final locking.
   - Growth challenges market access, launch realism, adoption, and GTM.
   - Tech challenges architecture, feasibility, controls, and delivery risk.
4. Add blackboard-first rules to each prompt:
   - read relevant open items;
   - answer or update targeted items when possible;
   - create atomic new items for questions, risks, decisions, proposals, and
     constraints;
   - never hide unresolved uncertainty inside polished prose.
5. Require outputs that can be parsed into:
   - the agent's main document;
   - items to create;
   - items to update;
   - readiness or finalization notes when relevant.
6. Keep headings stable and document them in `docs/ai/contracts.yaml`.
7. Keep the Paris/France deployment assumption unless the brief explicitly
   contradicts it.
8. Do not add broad marketing content to Tech prompts.
9. Do not add architecture content to Growth prompts.

## Expected Behaviors

- V4 prompts make agents operate against documents, summaries, and items.
- Agents produce structured sections that later code can parse.
- Product remains the role that resolves conflicts and arbitrates scope.
- Unresolved questions remain explicit.

## Acceptance Criteria

- `app/prompts V4/` contains Product, Growth, Tech, and summary prompt files.
- V3 prompt files are unchanged.
- V4 prompt headings and parse expectations are documented.
- Prompts explicitly state that summaries must not introduce new information.
- Prompts avoid turning V4 into a generic autonomous swarm.
- No runtime workflow implementation is required in this lot.

## Validation Commands

```bash
python3 -m compileall app
git diff -- "app/prompts V4" docs/ai
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Manual Verification Expected

- Read each V4 prompt and verify role boundaries are clear.
- Verify Product has arbitration authority.
- Verify Tech and Growth are challengers, not co-authors of the final PRD.
- Verify every prompt names item creation/update expectations.
- Verify V3 prompts remain untouched.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Check parser contracts before defining new required headings.
- Do not modify V3 prompts.
- Do not modify generated output history.
- Keep prompts practical and easy to inspect.
