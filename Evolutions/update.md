# V4 Target Run Workspace

This note describes the planned V4 target architecture. It is not the current
validated runtime baseline.

## Why V4 Exists

The current runtime still writes final dossiers under `outputs/tests/<Project>/version X/`.
That works for the existing baseline, but it does not isolate intermediate run
state cleanly when multiple runs share the same project title.

V4 introduces a run-scoped workspace keyed by `run_id` so two runs for the same
project never overwrite each other.

## Target Folder Structure

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

## Run Identity

`run_id` is required.

It should be readable, based on a UTC timestamp, and include a normalized
project slug plus a short suffix so repeated runs stay distinct.

## Final Historical Artifacts

The V4 target still produces the same historical dossier artifacts at the end
of a run:

- `prd.md`
- `architecture.md`
- `architecture-diagram.mmd`
- `architecture-diagram.png` when Mermaid rendering succeeds
- `gtm.md`
- `blackboard.md`
- `activity_log.txt`

Those files remain the human-facing end result. The workspace structure only
changes where the intermediate and final data are organized during the run.

## Summary Contract

Summaries are compressed derivatives of a single source document.
They are not a source of truth.

Required shape:

```yaml
summary:
  source_document:
  source_hash:
  scope:
  key_decisions:
  unresolved_questions:
  critical_risks:
```

Rules:

- one summary must come from exactly one source document
- the source document path and hash must stay traceable
- summaries must not invent information that is absent from the source document
- summaries are for compression and navigation, not for adding new knowledge

## Prompt Layering

V4 separates prompt responsibilities into three layers:

1. stable system prompts
2. the initial project brief
3. contextual step prompts

That split keeps permanent role behavior distinct from the shared project
context and from the current orchestration step.

## V3 Baseline

V3 remains the current validated baseline until a later lot validates V4 end to
end.

