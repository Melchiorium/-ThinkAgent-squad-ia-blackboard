# Lot 70 - V4 Context Packet Builder And Deduplication

## Objective

Centralize V4 context assembly and remove duplicate prompt sections.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- Current V4 calls often pass summaries/documents through both structured
  arguments and `extra_context`.
- This creates large prompts without adding information.

## Files Allowed To Modify

- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `outputs/workflow.md`
- `outputs/V2/lot-70-v4-context-packet-builder-and-deduplication.md`

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Add explicit V4 context selection helpers in `app/orchestrator.py`.
2. Ensure summaries, full documents, and open item blocks are assembled once.
3. Filter duplicate `extra_context` entries for summary, document, and open item
   sections.
4. Preserve resolved item context when it is the only source for resolved
   decisions.
5. Add no-LLM assertions that duplicate summary/document context is removed.

## Expected Behaviors

- Prompt builders remain easy to read.
- The same context block is not injected twice under different labels.
- No workflow phase loses access to source truth.

## Acceptance Criteria

- A prompt built with duplicate `extra_context` includes each summary/document at
  most once.
- The harness confirms the optimized prompt still produces valid V4 output.
- V4 docs and blackboard validators are not relaxed.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
```

## Manual Verification Expected

- Inspect prompt metrics before/after on a fake run.
- Confirm no generated history is manually edited.

## AGENTS.md Constraints

- Start from `docs/ai/00-index.yaml`.
- Keep V4 explicit in Python.
- Do not touch V3 prompts.
