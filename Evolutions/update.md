# Multi-Agent Blackboard Workflow Architecture

## Objective

Build a lightweight but structured multi-agent orchestration system based on a shared blackboard architecture.

The system must:
- coordinate multiple agents
- preserve structured memory
- track decisions/questions/risks/proposals
- maintain traceability across iterations
- avoid duplicated work and contradictions
- support iterative document production (PRD, architecture, GTM...)

The architecture must remain:
- deterministic
- simple to reason about
- easy to inspect manually
- file-system first

---

# Global Folder Structure

```txt
/blackboard
    /items

/documents
    /product
    /tech
    /growth

/summaries

/activity_log

/final_outputs
```

---

# Blackboard

## Core Principle

The blackboard is the shared coordination layer between agents.

Agents do not communicate directly.

Instead:
- they read documents
- they read blackboard items
- they create/update blackboard items
- they produce document versions

---

# Blackboard Items

## Concept

A blackboard item is an atomic coordination object shared between agents.

An item may represent:
- a question
- a risk
- a proposal
- a decision
- feedback
- a warning
- a constraint
- an unresolved issue

All items are stored inside:

```txt
/blackboard/items
```

The item category is defined through the `type` field.

---

# Item Structure

Example:

```yaml
id: ITEM-014

type: QUESTION

author: TECH

targets:
  - PRODUCT

priority: HIGH

status: OPEN

tags:
  - auth
  - scalability
  - workflow

title: Need clarification on temporary license lifecycle

content: |
  The current workflow does not specify
  how temporary licenses expire
  or how renewals should be handled.

created_at:
updated_at:
```

---

# Item Fields

| Field | Description |
|---|---|
| id | Unique item identifier |
| type | QUESTION / RISK / DECISION / PROPOSAL / FEEDBACK |
| author | Agent that created the item |
| targets | Intended recipient agents |
| priority | LOW / MEDIUM / HIGH / CRITICAL |
| status | OPEN / ANSWERED / ACCEPTED / REJECTED / OBSOLETE |
| tags | Topic categorization keywords |
| title | Short readable summary |
| content | Main item body |
| created_at | Creation timestamp |
| updated_at | Last update timestamp |

---

# Tags

## Purpose

Tags are lightweight topic identifiers attached to items.

They help agents:
- filter relevant items
- identify related discussions
- navigate the blackboard
- reduce duplicated work

Examples:

```yaml
tags:
  - auth
  - workflow
  - scalability
  - seat-management
```

---

## Tag Generation

Tags are generated directly by agents when creating items.

Agents should:
- use short stable keywords
- avoid long natural language tags
- reuse existing tags whenever possible
- prefer normalized naming conventions

Good examples:

```txt
auth
workflow
api
pricing
security
performance
seat-management
multi-tenant
```

Bad examples:

```txt
question-about-the-authentication-system
important-workflow-problem
```

---

# Documents

## Purpose

Documents are the long-form outputs produced iteratively by agents.

Structure:

```txt
/documents
    /product
    /tech
    /growth
```

Examples:
- PRD V0
- PRD V1
- Architecture V0
- GTM V0

Documents are:
- versioned
- mutable
- refined across iterations

Blackboard items are:
- atomic
- granular
- discussion-oriented

Documents and blackboard items must remain separate concepts.

---

# Summaries

## Purpose

Summaries reduce context size and improve orchestration efficiency.

Examples:

```txt
/summaries
    prd_summary
    gtm_summary
    architecture_summary
    decisions_summary
```

The orchestrator should prioritize summaries as the default inter-agent communication layer.

Instead of continuously sending full raw documents between agents, the orchestrator should inject:
- summaries
- relevant blackboard items
- targeted contextual information

Full documents should only be injected when necessary:
- document creation
- review phases
- convergence phases
- finalization

This reduces:
- context size
- token usage
- duplicated reasoning
- orchestration noise

---

# Activity Log

## Purpose

Tracks global workflow activity.

Examples:
- agent execution
- document creation
- item creation
- item resolution
- iteration transitions

The activity log is chronological and append-only.

---

# Final Outputs

Contains finalized validated deliverables.

Examples:
- final PRD
- final architecture
- final GTM
- exported reports

---

# Prompt Architecture

The orchestration system must distinguish multiple prompt layers.

This separation is critical to:
- maintain agent consistency
- reduce prompt duplication
- improve orchestration clarity
- preserve deterministic behavior
- simplify iteration management

---

## 1. System Prompt

Defines:
- permanent role of the agent
- behavioral rules
- shared project context
- collaboration model
- output expectations

The system prompt is stable across the whole workflow.

Example:

```txt
You are part of a multi-agent product team.
Agents collaborate through a shared blackboard system.
Communication must remain atomic and traceable.
```

---

## 2. Initial Prompt

Represents the initial project brief.

Defines:
- business problem
- objectives
- constraints
- expected outputs

Shared across all agents.

---

## 3. Contextual Step Prompt

Defines the current workflow step.

Tells the agent:
- what to do now
- which documents to read
- which summaries to read
- which items to process
- which outputs to produce

This is the main orchestration control layer.

Example:

```txt
Step 3 — Technical Review

Read:
- PRD_V0
- prd_summary
- open blackboard items

Your objectives:
- identify technical risks
- answer technical questions
- propose architecture decisions
- create Architecture_V0
```

---

# Workflow

## Step 0 — Initialization

The orchestrator initializes:
- agents
- prompts
- context
- shared rules

Initial documents and summaries may be empty.

---

## Step 1 — Product Phase

PRODUCT agent:
- analyzes the brief
- creates PRD V0
- creates initial blackboard items

Possible item types:
- QUESTIONS
- RISKS
- PROPOSALS
- DECISIONS

Outputs:
- `/documents/product/PRD_V0.md`
- blackboard items

---

## Step 2 — Review Phase

TECH and GROWTH agents:
- read PRD V0
- read summaries
- read blackboard items
- analyze implications

Agents create new items:
- feedback
- risks
- technical constraints
- business concerns
- open questions

---

## Step 3 — Specialized Outputs

TECH agent:
- creates Architecture V0

GROWTH agent:
- creates GTM V0

Both agents:
- answer existing items
- create additional items if necessary

Outputs:
- `/documents/tech/architecture_V0.md`
- `/documents/growth/gtm_V0.md`

---

## Step 4 — Product Review

PRODUCT agent:
- reviews TECH and GROWTH outputs
- reviews summaries
- reviews blackboard items
- resolves or answers items
- updates PRD

Output:
- `PRD_V1.md`

---

## Step 5+ — Iterative Loop

### TECH agent receives

- latest PRD
- latest GTM
- relevant summaries
- open blackboard items

TECH agent responsibilities:
- review updated product direction
- review GTM implications
- answer unresolved items
- create/update technical items
- update Architecture VX

---

### GROWTH agent receives

- latest PRD
- latest Architecture
- relevant summaries
- open blackboard items

GROWTH agent responsibilities:
- review updated product direction
- review technical constraints
- answer unresolved items
- create/update business items
- update GTM VX

---

### PRODUCT agent receives

- latest Architecture
- latest GTM
- summaries
- unresolved items

PRODUCT agent responsibilities:
- arbitrate decisions
- refine requirements
- resolve conflicts
- update PRD VX

---

## Iterative Outputs

Each iteration may produce:

```txt
PRD_VX
Architecture_VX
GTM_VX
```

Iterations continue until:
- convergence
- approval
- max iteration count

Agents must continuously:
- refine outputs
- resolve items
- reduce ambiguity
- improve convergence

---

## Finalization Phase

Once convergence is reached:
- agents finalize documents
- outputs are rewritten for human readability
- formatting and structure are improved
- unresolved points are explicitly surfaced

Final outputs are stored inside:

```txt
/final_outputs
```

---

## Open Questions Handling

If unresolved blackboard items still exist during finalization:
- they must not disappear
- they must remain visible
- they must be surfaced explicitly

Unresolved items become:

```txt
OPEN QUESTIONS
```

inside final human-readable deliverables.

Example:

```txt
Open Questions

- Should temporary licenses expire automatically after 30 days?
- Should managers receive monthly inactive seat reports?
- Should contractors receive restricted Dev seats?
```

The orchestration system must prioritize:
- traceability
- explicit uncertainty
- visible unresolved decisions

The system must never pretend convergence was reached if important questions remain unresolved.

---

# Important Design Rules

## Blackboard First

Agents must prioritize:
- reading blackboard items
- updating item statuses
- creating atomic items

before producing large documents.

---

## Atomic Communication

Discussion points must remain atomic.

Avoid:
- huge mixed discussions
- giant monolithic feedback documents

Prefer:
- small traceable items

---

## Deterministic Workflow

The orchestration should remain:
- explicit
- traceable
- reproducible

Avoid uncontrolled autonomous behaviors.

---

## Separation of Concerns

Documents:
- long-form outputs

Blackboard items:
- coordination and reasoning units

Summaries:
- compressed orchestration memory

Activity log:
- historical execution tracking

These concepts must remain distinct.