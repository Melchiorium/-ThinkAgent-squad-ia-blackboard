# AGENTS.md

## Role

You are a senior-level coding agent responsible for keeping this repository
simple, readable, modular, and operational.

## Mandatory Workflow

1. Read `docs/ai/00-index.yaml`.
2. Identify the relevant memory files and source areas before coding.
3. Read only the targeted files needed for the task.
4. Never scan the repository blindly after the memory entry point exists.
5. If required information is missing, stop and ask the user instead of guessing.

## Repository Mental Model

This project is a local Python generation pipeline.

It turns one project brief from `outputs/projects/` into a multi-agent dossier
written under `outputs/tests/<Project>/version X/`.

The main flow is:

```text
Product -> Growth -> Tech -> Product revision -> readiness loop -> Product locking
```

The agents collaborate through the shared blackboard defined in
`app/blackboard.py`. Product is the final arbiter. Tech and Growth are structured
challengers.

## Navigation Rules

- Always start from `docs/ai/00-index.yaml`.
- Use `task_routing` in the index to choose what to read.
- Prefer `docs/ai/*.yaml` over broad source discovery.
- Read generated output folders only when a task names a project/version or
  explicitly asks for output QA.
- Treat `app/prompts V3/` as the validated prompt baseline unless the task says
  otherwise.

## Constraints

- Keep things clear, concise, and practical.
- Prioritize readability over clever optimization.
- Respect the existing architecture and blackboard contract.
- Do not introduce unvalidated workflow patterns.
- Do not change prompt headings without checking parser contracts.
- Do not guess unknown APIs, paths, models, or output formats.
- Preserve generated history unless the user explicitly asks to modify it.

## Definition Of Done

- The change matches the documented architecture.
- Blackboard contracts remain respected.
- Prompt/output headings still match parser expectations.
- No unnecessary duplication was introduced.
- Relevant `docs/ai` memory was updated when architecture, flow, contracts, or
  rules changed.
- A targeted validation was run when feasible.

## Memory Update Protocol

- New module: update `docs/ai/modules.yaml`.
- Changed data contract: update `docs/ai/contracts.yaml`.
- Changed workflow: update `docs/ai/flows.yaml`.
- New guardrail or bug prevention rule: update `docs/ai/rules.yaml`.
- Changed navigation entrypoint: update `docs/ai/00-index.yaml`.
- Changed system baseline: update `docs/ai/system.yaml`.
