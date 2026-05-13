# Prompt Architecture

V4 keeps prompt layers separate on purpose.

That split keeps the orchestration readable and makes it easier to reason
about what changes when the project brief changes, when the step changes, or
when only the agent role changes.

## 1. Stable System Prompt

The stable system prompt defines the permanent role of the agent.

It contains:

- role identity
- collaboration rules
- blackboard-first behavior
- document discipline
- item creation and update discipline
- output boundaries

Examples:

- Product: framing, arbitration, MVP scope, and final locking
- Growth: market access, launch realism, and early traction
- Tech: feasibility, architecture, controls, and delivery realism

The system prompt should stay stable across the whole run.

## 2. Initial Project Brief

The initial project brief is the shared project context.

It contains:

- the project idea
- the business or product problem
- constraints
- expected outcomes
- the target context for the run

The brief is not a template. It is the actual input the agents work from.

## 3. Contextual Step Prompt

The contextual step prompt defines the current orchestration step.

It tells the agent:

- what it must do now
- which documents to read
- which open items matter now
- what to update or create
- what the current iteration goal is

This is the layer that changes the most during a run.

## 4. Summary Prompt

Summaries use their own strict prompt layer.

They are separate from the agent prompts because summaries are compressed
derivatives of exactly one source document.

The summary prompt must:

- forbid invention
- require a single source document
- require traceable source metadata
- keep the output in a strict machine-checkable shape

## Why The Split Matters

Without prompt layering:

- prompts become harder to audit
- role boundaries blur
- the orchestration logic becomes harder to change safely
- summaries and agent outputs get conflated

With prompt layering:

- permanent behavior stays stable
- the brief stays reusable
- step-specific instructions stay small
- debugging becomes easier
- future migration to V4 stays understandable

