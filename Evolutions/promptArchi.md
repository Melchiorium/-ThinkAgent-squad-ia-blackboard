# Prompt Architecture

The orchestration system must distinguish multiple prompt layers.

This separation is critical to:
- maintain agent consistency
- reduce prompt duplication
- improve orchestration clarity
- preserve deterministic behavior
- simplify iteration management

---

# 1. System Prompt

## Purpose

Defines:
- the permanent role of the agent
- global behavioral rules
- shared project context
- collaboration model
- output expectations

The system prompt is stable across the whole project.

It should rarely change during execution.

---

## Examples

PRODUCT agent:
- product reasoning
- user-centric thinking
- prioritization
- PRD ownership

TECH agent:
- architecture
- scalability
- feasibility
- technical constraints

GROWTH agent:
- adoption
- distribution
- business impact
- GTM strategy

---

## Shared Context

The system prompt may also include:
- agents work collaboratively
- blackboard-first workflow
- atomic item philosophy
- document conventions
- orchestration rules
- deterministic behavior expectations

Example:

```txt
You are part of a multi-agent product team.
Agents collaborate through a shared blackboard system.
Communication must remain atomic and traceable.
```

---

# 2. Initial Prompt

## Purpose

Represents the project brief.

This is the initial business/problem statement given to all agents.

It defines:
- the product idea
- objectives
- constraints
- expected outputs
- business context

The initial prompt is shared across all agents.

---

## Example

```txt
Build a workflow automation system for Figma Dev license management.

The system must:
- automate requests
- validate manager approval
- manage cost centers
- provision licenses
- remove inactive licenses after inactivity
```

---

# 3. Contextual Step Prompt

## Purpose

Defines the current orchestration step.

This prompt changes at every workflow stage.

It tells the agent:
- what it must do now
- which documents to read
- which agents to consider
- which outputs to produce
- what the current iteration goal is

This is the main orchestration control layer.

---

# Example

```txt
Step 3 — Technical Review

Read:
- PRD_V0
- open blackboard items

Your objectives:
- identify technical risks
- answer technical questions
- propose architecture decisions
- create Architecture_V0
```

---

# Why This Separation Matters

Without separation:
- prompts become huge
- responsibilities become blurry
- orchestration becomes difficult to control
- agents become inconsistent across iterations

With separation:

```txt
System Prompt
= permanent identity

Initial Prompt
= project brief

Contextual Step Prompt
= current task
```

This creates:
- cleaner orchestration
- better memory management
- more stable agent behavior
- easier debugging
- easier scalability