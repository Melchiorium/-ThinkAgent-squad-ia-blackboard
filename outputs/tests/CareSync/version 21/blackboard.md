# Blackboard

## Project Brief

Project Name: CareSync

Pitch:
A digital platform that helps families coordinate care for elderly relatives by centralizing medical appointments, medication reminders, caregiving tasks, and communication between family members and professional caregivers.

Context:
Many families struggle to manage care for aging parents or relatives, especially when multiple siblings or caregivers are involved. Information is often fragmented across phone calls, messaging apps, handwritten notes, and hospital documents.

At the same time, professional caregivers and home assistance providers often lack visibility into family decisions and day-to-day coordination.

The platform aims to simplify elderly care coordination while reducing stress for families.

Target Users:
- Adults managing care for elderly parents
- Family members living in different cities
- Professional caregivers
- Home nurses
- Elderly care agencies

Potential Use Cases:
- Scheduling medical appointments
- Medication reminders
- Shared task management
- Emergency contact coordination
- Sharing medical documents
- Tracking caregiving responsibilities

Platform Capabilities:
- Shared family dashboard
- Calendar coordination
- Notifications/reminders
- Secure document storage
- Messaging system
- Permission management for family members and caregivers

Constraints:
- High trust and privacy expectations
- Sensitive medical-related information
- Elderly users may have low digital literacy
- Potential legal/data compliance issues depending on country

Challenges:
- Convincing families to adopt a new platform
- Balancing simplicity with complex coordination needs
- Building trust around sensitive personal information
- Identifying a sustainable business model

Long-term Vision:
Become the operating system for family caregiving coordination and eventually expand into broader home healthcare services.

## Project Brief Source

projects/project-CareSync.md

## Workflow Stage

first_pass_locked

## Source Version

_Aucun contenu._

## CEO Evaluation

_Aucun contenu._

## Artifacts

## Architecture Markdown Ready

True


## Architecture Visual Ready

True


## Architecture Visual Warning

_Aucun contenu._


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### scope
- [scope] First launch geography and compliance baseline must be fixed before build

### privacy_trust
- [privacy_trust] Exact role-to-data visibility rules for tasks, appointments, reminders, and notes must be finalized

### demand_validation
- [demand_validation] Willingness to pay by the primary coordinator is unproven

## Product Required Improvements

### scope
- [scope] Choose one launch market and codify minimum data-handling rules before public rollout

### privacy_trust
- [privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders

### demand_validation
- [demand_validation] Run a paid concierge pilot to test activation, retention, and monetization

## Tech Status

LIMITED


## Tech Blocking Gaps

### privacy_trust
- [privacy_trust] Exact role-to-data visibility rules are still not fully specified for notes, appointments, tasks, and reminders.
- [privacy_trust] Notification content policy for sensitive care data is not defined.

### operations
- [operations] Admin/support recovery workflow is required but not yet operationalized as a controlled process.

## Tech Required Improvements

### privacy_trust
- [privacy_trust] Publish a fixed permission matrix with default visibility and edit rights per role and object type.
- [privacy_trust] Define safe notification payload rules, including what can appear in email/SMS previews.

### operations
- [operations] Implement an audit-backed support console and a documented recovery workflow for invite and role mistakes.

## Growth Status

LIMITED


## Growth Blocking Gaps

### demand_validation
- [demand_validation] No measurable threshold defines when pilot demand is real enough to proceed
- [demand_validation] Willingness to pay is still unproven for the primary coordinator
- [demand_validation] The minimum trust/permission model is not yet validated in live family usage

## Growth Required Improvements

### demand_validation
- [demand_validation] Set a concrete pilot success bar for active participants, repeated actions, and retention
- [demand_validation] Run a paid or price-tested concierge pilot with the coordinator as buyer
- [demand_validation] Validate the smallest trusted role/permission model in real usage

## Global Status

LIMITED


## Global Blocking Gaps

### scope
- [scope] First launch geography and compliance baseline must be fixed before build

### privacy_trust
- [privacy_trust] Exact role-to-data visibility rules for tasks, appointments, reminders, and notes must be finalized
- [privacy_trust] Exact role-to-data visibility rules are still not fully specified for notes, appointments, tasks, and reminders.
- [privacy_trust] Notification content policy for sensitive care data is not defined.

### demand_validation
- [demand_validation] Willingness to pay by the primary coordinator is unproven
- [demand_validation] No measurable threshold defines when pilot demand is real enough to proceed
- [demand_validation] Willingness to pay is still unproven for the primary coordinator
- [demand_validation] The minimum trust/permission model is not yet validated in live family usage

### operations
- [operations] Admin/support recovery workflow is required but not yet operationalized as a controlled process.

## Global Required Improvements

### scope
- [scope] Choose one launch market and codify minimum data-handling rules before public rollout

### privacy_trust
- [privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders
- [privacy_trust] Publish a fixed permission matrix with default visibility and edit rights per role and object type.
- [privacy_trust] Define safe notification payload rules, including what can appear in email/SMS previews.

### demand_validation
- [demand_validation] Run a paid concierge pilot to test activation, retention, and monetization
- [demand_validation] Set a concrete pilot success bar for active participants, repeated actions, and retention
- [demand_validation] Run a paid or price-tested concierge pilot with the coordinator as buyer
- [demand_validation] Validate the smallest trusted role/permission model in real usage

### operations
- [operations] Implement an audit-backed support console and a documented recovery workflow for invite and role mistakes.

## Known Tags

- scope
- demand_validation
- untagged
- privacy_trust
- operations


## Correction Loop

## Triggered

Yes


## Current Loop Count

2


## Max Loops

2


## Initial Global Status

LIMITED


## Final Outcome

LIMITED


## Correction Tasks

### Loop 1

#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] First launch geography and compliance baseline are not defined Define the first launch country and minimum compliance policy before launch Launch compliance scope is undefined Choose the initial launch country and codify the minimum data-handling rules before build First launch geography and compliance baseline are undefined Choose one launch market and confirm the privacy/compliance requirements before public rollout


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech
- growth


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Minimum trust and permission model for sensitive care data is not fully validated Willingness to pay by the primary coordinator is unproven Validate the smallest acceptable permission model for family and caregiver access Run a paid concierge pilot to test retention and monetization Minimum trust and permission model is not validated for sensitive care data Willingness to pay from the family coordinator is unproven Validate the smallest permission set that families and caregivers will trust Run a paid or clearly price-tested concierge pilot with 3–5 care circles


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] Add an admin/support console for invite and membership recovery


## Expected Output

A clear product decision on build-versus-manual scope.


## Contributors

- tech


### Loop 2

#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] First launch geography and compliance baseline must be fixed before build Choose one launch market and codify minimum data-handling rules for that market Launch compliance scope is undefined Choose the initial launch country and codify the minimum data-handling rules before build The first launch geography and compliance baseline remain undefined Define the first launch market and compliance requirements before any public rollout


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech
- growth


#### Tech Task

## Task

Define the smallest privacy and trust control needed before launch.


## Source Gap

[privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders Permission matrix for sensitive care data is not specified Define exact role-based visibility for tasks, notes, appointments, and reminders The smallest trusted permission model is not yet proven with real families


## Expected Output

A concrete minimum trust and privacy control set for MVP.


## Contributors

- growth


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Minimal permission model for coordinator, family member, and caregiver is not yet validated Willingness to pay by the primary coordinator is unproven Run a paid concierge pilot to test retention and monetization No concrete threshold defines whether demand is real enough to proceed beyond pilot Set a measurable pilot success threshold for paid or price-tested adoption Validate the minimum role and permission model in live pilot usage


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

_Aucun contributeur._


## Readiness History

### Loop 1 before

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### scope
- [scope] First launch geography and compliance baseline are not defined
- [scope] Launch compliance scope is undefined
- [scope] First launch geography and compliance baseline are undefined

### demand_validation
- [demand_validation] Minimum trust and permission model for sensitive care data is not fully validated
- [demand_validation] Willingness to pay by the primary coordinator is unproven
- [demand_validation] Minimum trust and permission model is not validated for sensitive care data
- [demand_validation] Willingness to pay from the family coordinator is unproven

### privacy_trust
- [privacy_trust] Permission matrix for sensitive care data is not specified

### untagged
- Reminder delivery reliability requirements are not defined

## Global Required Improvements

### scope
- [scope] Define the first launch country and minimum compliance policy before launch
- [scope] Choose the initial launch country and codify the minimum data-handling rules before build
- [scope] Choose one launch market and confirm the privacy/compliance requirements before public rollout

### demand_validation
- [demand_validation] Validate the smallest acceptable permission model for family and caregiver access
- [demand_validation] Run a paid concierge pilot to test retention and monetization
- [demand_validation] Validate the smallest permission set that families and caregivers will trust
- [demand_validation] Run a paid or clearly price-tested concierge pilot with 3–5 care circles

### privacy_trust
- [privacy_trust] Define exact role-based visibility for tasks, notes, appointments, and reminders

### untagged
- Set delivery expectations and fallback behavior for notification failures

### operations
- [operations] Add an admin/support console for invite and membership recovery

## Loop Tasks

##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] First launch geography and compliance baseline are not defined Define the first launch country and minimum compliance policy before launch Launch compliance scope is undefined Choose the initial launch country and codify the minimum data-handling rules before build First launch geography and compliance baseline are undefined Choose one launch market and confirm the privacy/compliance requirements before public rollout


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Minimum trust and permission model for sensitive care data is not fully validated Willingness to pay by the primary coordinator is unproven Validate the smallest acceptable permission model for family and caregiver access Run a paid concierge pilot to test retention and monetization Minimum trust and permission model is not validated for sensitive care data Willingness to pay from the family coordinator is unproven Validate the smallest permission set that families and caregivers will trust Run a paid or clearly price-tested concierge pilot with 3–5 care circles


## Expected Output

A concrete demand-validation approach with a signal threshold.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] Add an admin/support console for invite and membership recovery


## Expected Output

A clear product decision on build-versus-manual scope.


### Loop 1 after

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### scope
- [scope] First launch geography and compliance baseline must be fixed before build
- [scope] Launch compliance scope is undefined
- [scope] The first launch geography and compliance baseline remain undefined

### demand_validation
- [demand_validation] Minimal permission model for coordinator, family member, and caregiver is not yet validated
- [demand_validation] Willingness to pay by the primary coordinator is unproven
- [demand_validation] No concrete threshold defines whether demand is real enough to proceed beyond pilot

### privacy_trust
- [privacy_trust] Permission matrix for sensitive care data is not specified
- [privacy_trust] The smallest trusted permission model is not yet proven with real families

### untagged
- Reminder delivery reliability requirements are not defined

## Global Required Improvements

### scope
- [scope] Choose one launch market and codify minimum data-handling rules for that market
- [scope] Choose the initial launch country and codify the minimum data-handling rules before build
- [scope] Define the first launch market and compliance requirements before any public rollout

### privacy_trust
- [privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders
- [privacy_trust] Define exact role-based visibility for tasks, notes, appointments, and reminders

### demand_validation
- [demand_validation] Run a paid concierge pilot to test retention and monetization
- [demand_validation] Set a measurable pilot success threshold for paid or price-tested adoption
- [demand_validation] Validate the minimum role and permission model in live pilot usage

### untagged
- Set delivery expectations and fallback behavior for notification failures

### operations
- [operations] Add an admin/support console for invite and membership recovery

## Loop Tasks

##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] First launch geography and compliance baseline are not defined Define the first launch country and minimum compliance policy before launch Launch compliance scope is undefined Choose the initial launch country and codify the minimum data-handling rules before build First launch geography and compliance baseline are undefined Choose one launch market and confirm the privacy/compliance requirements before public rollout


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Minimum trust and permission model for sensitive care data is not fully validated Willingness to pay by the primary coordinator is unproven Validate the smallest acceptable permission model for family and caregiver access Run a paid concierge pilot to test retention and monetization Minimum trust and permission model is not validated for sensitive care data Willingness to pay from the family coordinator is unproven Validate the smallest permission set that families and caregivers will trust Run a paid or clearly price-tested concierge pilot with 3–5 care circles


## Expected Output

A concrete demand-validation approach with a signal threshold.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] Add an admin/support console for invite and membership recovery


## Expected Output

A clear product decision on build-versus-manual scope.


### Loop 2 before

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### scope
- [scope] First launch geography and compliance baseline must be fixed before build
- [scope] Launch compliance scope is undefined
- [scope] The first launch geography and compliance baseline remain undefined

### demand_validation
- [demand_validation] Minimal permission model for coordinator, family member, and caregiver is not yet validated
- [demand_validation] Willingness to pay by the primary coordinator is unproven
- [demand_validation] No concrete threshold defines whether demand is real enough to proceed beyond pilot

### privacy_trust
- [privacy_trust] Permission matrix for sensitive care data is not specified
- [privacy_trust] The smallest trusted permission model is not yet proven with real families

### untagged
- Reminder delivery reliability requirements are not defined

## Global Required Improvements

### scope
- [scope] Choose one launch market and codify minimum data-handling rules for that market
- [scope] Choose the initial launch country and codify the minimum data-handling rules before build
- [scope] Define the first launch market and compliance requirements before any public rollout

### privacy_trust
- [privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders
- [privacy_trust] Define exact role-based visibility for tasks, notes, appointments, and reminders

### demand_validation
- [demand_validation] Run a paid concierge pilot to test retention and monetization
- [demand_validation] Set a measurable pilot success threshold for paid or price-tested adoption
- [demand_validation] Validate the minimum role and permission model in live pilot usage

### untagged
- Set delivery expectations and fallback behavior for notification failures

### operations
- [operations] Add an admin/support console for invite and membership recovery

## Loop Tasks

##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] First launch geography and compliance baseline must be fixed before build Choose one launch market and codify minimum data-handling rules for that market Launch compliance scope is undefined Choose the initial launch country and codify the minimum data-handling rules before build The first launch geography and compliance baseline remain undefined Define the first launch market and compliance requirements before any public rollout


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Tech

## Task

Define the smallest privacy and trust control needed before launch.


## Source Gap

[privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders Permission matrix for sensitive care data is not specified Define exact role-based visibility for tasks, notes, appointments, and reminders The smallest trusted permission model is not yet proven with real families


## Expected Output

A concrete minimum trust and privacy control set for MVP.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Minimal permission model for coordinator, family member, and caregiver is not yet validated Willingness to pay by the primary coordinator is unproven Run a paid concierge pilot to test retention and monetization No concrete threshold defines whether demand is real enough to proceed beyond pilot Set a measurable pilot success threshold for paid or price-tested adoption Validate the minimum role and permission model in live pilot usage


## Expected Output

A concrete demand-validation approach with a signal threshold.


### Loop 2 after

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### scope
- [scope] First launch geography and compliance baseline must be fixed before build

### privacy_trust
- [privacy_trust] Exact role-to-data visibility rules for tasks, appointments, reminders, and notes must be finalized
- [privacy_trust] Exact role-to-data visibility rules are still not fully specified for notes, appointments, tasks, and reminders.
- [privacy_trust] Notification content policy for sensitive care data is not defined.

### demand_validation
- [demand_validation] Willingness to pay by the primary coordinator is unproven
- [demand_validation] No measurable threshold defines when pilot demand is real enough to proceed
- [demand_validation] Willingness to pay is still unproven for the primary coordinator
- [demand_validation] The minimum trust/permission model is not yet validated in live family usage

### operations
- [operations] Admin/support recovery workflow is required but not yet operationalized as a controlled process.

## Global Required Improvements

### scope
- [scope] Choose one launch market and codify minimum data-handling rules before public rollout
- [scope] Lock invite-only onboarding as the only MVP entry path

### privacy_trust
- [privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders
- [privacy_trust] Publish a fixed permission matrix with default visibility and edit rights per role and object type.
- [privacy_trust] Define safe notification payload rules, including what can appear in email/SMS previews.

### demand_validation
- [demand_validation] Run a paid concierge pilot to test activation, retention, and monetization
- [demand_validation] Set a concrete pilot success bar for active participants, repeated actions, and retention
- [demand_validation] Run a paid or price-tested concierge pilot with the coordinator as buyer
- [demand_validation] Validate the smallest trusted role/permission model in real usage

### operations
- [operations] Confirm admin recovery and access revocation procedures for pilot support
- [operations] Implement an audit-backed support console and a documented recovery workflow for invite and role mistakes.

## Loop Tasks

##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] First launch geography and compliance baseline must be fixed before build Choose one launch market and codify minimum data-handling rules for that market Launch compliance scope is undefined Choose the initial launch country and codify the minimum data-handling rules before build The first launch geography and compliance baseline remain undefined Define the first launch market and compliance requirements before any public rollout


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Tech

## Task

Define the smallest privacy and trust control needed before launch.


## Source Gap

[privacy_trust] Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders Permission matrix for sensitive care data is not specified Define exact role-based visibility for tasks, notes, appointments, and reminders The smallest trusted permission model is not yet proven with real families


## Expected Output

A concrete minimum trust and privacy control set for MVP.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Minimal permission model for coordinator, family member, and caregiver is not yet validated Willingness to pay by the primary coordinator is unproven Run a paid concierge pilot to test retention and monetization No concrete threshold defines whether demand is real enough to proceed beyond pilot Set a measurable pilot success threshold for paid or price-tested adoption Validate the minimum role and permission model in live pilot usage


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- [tech] Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]

## Growth Structural Decisions

### growth
- [growth] Add a **measurable demand threshold** for the pilot, such as: at least 3 of 5 invited participants active within 7 days, and at least 2 recurring coordination actions completed per week per circle. [demand_validation]
- [growth] Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]

## Product Locking

## Applied

True


## Confirmed In Scope

- One elder, one care circle
- Invite-only access only
- Coordinator, family member, caregiver roles
- Tasks, appointments, medication reminders, restricted notes
- Fixed visibility boundaries
- Audit log for permission and access changes
- Admin/support recovery for invites, roles, and revocation
- First-market compliance baseline


## Confirmed Deferred

- Secure document storage
- Rich chat
- Multi-elder support
- Care agency dashboards
- Calendar/EHR/pharmacy/messaging integrations
- Payments and billing
- Advanced analytics
- AI summaries
- Emergency escalation
- Public self-serve onboarding


## Confirmed Out Of Scope

_Aucun élément hors scope._


## Locking Note

- Scope remains intentionally narrow; no new features added. - Pilot support stays operational, not productized beyond proof-critical recovery and compliance. - Permission model and geography must be finalized before build.


## Expert Contributions

### Tech Summary

The biggest feasibility issue is not feature breadth but trust: the MVP needs a simple, enforceable permission model that families can understand and support can repair. The safest direction is a narrow invite-only care circle with fixed roles, object-level visibility rules, and mandatory audit logging, while keeping everything else operationally manual where possible.

## Tech Structural Decisions

- Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]


## Tech Recommendations

- Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]


## Tech Risks

- Families may not understand the fixed roles and may expect flexible sharing. [privacy_trust]
- A single mistake in permissions or notifications could permanently damage trust. [privacy_trust]
- Support overhead may be higher than expected if invite and role recovery is frequent. [operations]


## Tech Open Questions

- Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]


### Growth Summary

The main launch challenge is not feature completeness but whether a single family coordinator can get a trusted care circle to adopt and keep using the product. The right GTM direction is a concierge-led, single-elder pilot aimed at proving recurring coordination usage and willingness to pay before expanding scope.

## Growth Structural Decisions

- Add a **measurable demand threshold** for the pilot, such as: at least 3 of 5 invited participants active within 7 days, and at least 2 recurring coordination actions completed per week per circle. [demand_validation]
- Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]


## Growth Recommendations

- Add a **measurable demand threshold** for the pilot, such as: at least 3 of 5 invited participants active within 7 days, and at least 2 recurring coordination actions completed per week per circle. [demand_validation]
- Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]
- Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]


## Growth Risks

- The coordinator signs up but cannot persuade siblings/caregivers to participate.
- Families continue using WhatsApp/text and never shift behavior.
- Privacy concerns block sharing of sensitive notes.


## Growth Open Questions

- What exact activation threshold will count as real demand in the pilot?
- What price point will the coordinator accept after trying the workflow?
- Which permission boundaries are required for trust versus convenience?


## Product Arbitration

## Source

heuristic_fallback


## Retained

- Tech: Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Growth: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]


## Deferred

- Growth: Add a **measurable demand threshold** for the pilot, such as: at least 3 of 5 invited participants active within 7 days, and at least 2 recurring coordination actions completed per week per circle. [demand_validation]


## Rejected

- Tech: Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Tech: Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Tech: Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]
- Growth: Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Growth: Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]


## Open Points

- Tech: Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Growth: Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Tech: Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Tech: Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Tech: Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- Growth: What exact activation threshold will count as real demand in the pilot?
- Growth: What price point will the coordinator accept after trying the workflow?
- Growth: Which permission boundaries are required for trust versus convenience?
- Tech recommendation needing arbitration: Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Tech recommendation needing arbitration: Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Tech recommendation needing arbitration: Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Tech recommendation needing arbitration: Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]
- Growth recommendation needing arbitration: Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]
- Growth recommendation needing arbitration: Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Growth recommendation needing arbitration: Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]
- Tech open question: Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Tech open question: Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Tech open question: Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- Growth open question: What exact activation threshold will count as real demand in the pilot?
- Growth open question: What price point will the coordinator accept after trying the workflow?
- Growth open question: Which permission boundaries are required for trust versus convenience?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care are using fragmented tools for high-stakes tasks: calls, text threads, paper notes, email, and ad hoc reminders. This creates missed appointments, duplicated effort, unclear responsibility, and poor visibility for siblings and professional caregivers. The core problem is not “all care management”; it is reliable coordination among a small care circle around one older adult.

## Initial Wedge
A shared care coordination hub for one elder and their immediate family/caregiver circle, focused on:
- one shared schedule
- one shared task list
- one medication reminder stream
- one place for key care notes

The wedge is to reduce missed actions and confusion in the first week of use, not to replace full medical records or become a general health platform.

## First Target User
Primary user:
- An adult child who is the de facto care coordinator for an aging parent

Secondary users in the first workflow:
- 1–3 siblings or relatives
- 1 professional caregiver or home aide, if present

This user already feels the coordination burden and is motivated to set up the system for others.

## Existing Alternatives And Switching Trigger
Current alternatives:
- Group texts / WhatsApp threads
- Shared calendars
- Paper notebooks
- Notes app / email chains
- Generic task apps like Todoist or Trello
- Caregiver agency portals, if available

Switching trigger:
- information is getting lost across too many channels
- siblings disagree on responsibilities
- appointments or medication actions are being missed
- the coordinator needs a single source of truth with simple access for non-technical family members

## Core MVP Workflow
1. Primary user creates a care circle for one elder.
2. Invites family members and, optionally, one professional caregiver.
3. Adds the few recurring essentials:
   - appointments
   - medications with reminder times
   - shared tasks
   - contact notes / care notes
4. Each participant sees only what they need.
5. Notifications remind the right person at the right time.
6. Family members mark tasks complete and add short updates.
7. The coordinator gets a simple view of what is done, overdue, or pending.

## In Scope
- Single elder care circle setup
- Invite-only access for family/caregivers
- Shared task list with ownership and due dates
- Basic calendar/appointment entries
- Medication reminders as reminders only, not clinical guidance
- Lightweight notes for care instructions and updates
- Basic permission levels for family vs caregiver access
- Simple notification delivery
- Minimal audit trail of updates/completions for trust

## Out of Scope
- Full electronic health record replacement
- Live clinical decision support
- Prescription management or pharmacy integrations
- Emergency response / 911 escalation
- Broad marketplace for hiring caregivers
- Telehealth visits
- Advanced AI summaries or care recommendations
- Insurance claims, billing, or payments
- Multi-elder household management
- Complex agency workflows
- Deep document management beyond basic upload/view of key files

## MVP Build Vs Pilot Operations
### Must Build Now
- Invite-only care circle
- Shared task management
- Appointment entries and reminders
- Medication reminder schedules
- Basic notes feed
- Basic role-based permissions
- Notification system
- Activity log for key changes

### Manual Or Operational During Pilot
- White-glove onboarding for the first care circle
- Help importing initial appointments and reminders
- Support for setting up family roles and permissions
- Manual customer support for troubleshooting
- Compliance review for launch geography
- Optional guidance on best-practice setup

### Deferred Until After Proof
- Secure document vault with advanced organization
- Rich messaging/chat
- Multi-elder support
- Care agency dashboards
- Integrations with calendars, EHRs, pharmacies, or messaging apps
- Payments and billing
- Advanced analytics
- AI-generated summaries
- Emergency escalation workflows

## Business Model Hypothesis
A subscription model for the coordinating family is the most plausible starting point:
- monthly fee for a single care circle
- optional premium tier for added caregivers, reminders, or storage

Alternative hypothesis if family willingness to pay is weak:
- B2B2C licensing through elder care agencies or home care providers

The first test is whether a family coordinator will pay for reduced confusion and fewer missed actions.

## Critical Assumptions
- The primary pain is frequent enough to justify a new tool.
- One trusted family member is willing to set up and maintain the system.
- Other family members and caregivers will actually use a lightweight shared tool.
- Notifications and simple task ownership are enough to create visible value.
- Trust and privacy concerns do not block adoption if permissions are clear.
- The product can be launched in a compliant way for the initial geography.

## How To Test Quickly
- Run 10–15 interviews with adult children coordinating elder care.
- Test whether current workflows rely on fragmented channels and where failures happen.
- Concierge pilot with 3–5 families using a lightweight prototype or no-code version.
- Measure whether the platform reduces missed tasks and duplicated reminders in 2–4 weeks.
- Test willingness to invite siblings/caregivers and keep them active.
- Test willingness to pay after the first coordination cycle.
- Validate which features are actually used: tasks, reminders, notes, or calendar.

## Acceptance Criteria
- A coordinator can set up a care circle in under 10 minutes.
- Family members can be invited and granted simple access without training.
- A task can be assigned, reminded, and marked complete.
- A medication reminder can be scheduled and delivered reliably.
- Appointment details can be added and seen by the right participants.
- Users can see who changed what and when.
- Access controls prevent unintended visibility of sensitive notes.
- The system works for at least one complete care coordination cycle without manual re-entry across multiple tools.

## Risks And Failure Modes
- Low adoption by siblings or caregivers who prefer existing chat tools.
- Trust/privacy concerns block sharing of sensitive information.
- The product becomes too broad and loses the simplicity needed for adoption.
- Reminder fatigue causes users to ignore notifications.
- The coordinator still has to duplicate work across other channels.
- Compliance requirements vary by country and complicate launch.
- A family tool may be valuable but not monetizable enough on its own.

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Compliance scope and launch geography are not defined [compliance_scope]
- Trust model for sensitive health-related data is not fully validated [trust_validation]
- Willingness to pay by the primary coordinator is unproven [willingness_to_pay]

Required Improvements:
- Define the first launch country and required privacy/compliance baseline [compliance_scope]
- Validate the minimum permission model needed for families and caregivers [trust_validation]
- Run a paid concierge pilot to test retention and monetization [willingness_to_pay]

## Recommendation
Proceed with a narrow MVP focused on one elder, one coordinator, and one shared care circle. Do not expand into messaging, document management, or broader home healthcare until the core coordination loop proves retention and willingness to pay. The fastest credible path is a concierge pilot with limited scope and strict access controls.

## Retained Decisions

- Tech: Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Growth: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]

## Deferred Decisions

- Growth: Add a **measurable demand threshold** for the pilot, such as: at least 3 of 5 invited participants active within 7 days, and at least 2 recurring coordination actions completed per week per circle. [demand_validation]

## Rejected Recommendations

- Tech: Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Tech: Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Tech: Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]
- Growth: Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Growth: Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]

## Unresolved Tensions

- Tech recommendation needing arbitration: Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Tech recommendation needing arbitration: Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Tech recommendation needing arbitration: Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Tech recommendation needing arbitration: Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]
- Growth recommendation needing arbitration: Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]
- Growth recommendation needing arbitration: Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Growth recommendation needing arbitration: Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]
- Tech open question: Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Tech open question: Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Tech open question: Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- Growth open question: What exact activation threshold will count as real demand in the pilot?
- Growth open question: What price point will the coordinator accept after trying the workflow?
- Growth open question: Which permission boundaries are required for trust versus convenience?

## Applied Changes

- Tech: Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Growth: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]

## Remaining Open Points

- Tech: Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Growth: Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Tech: Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Tech: Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Tech: Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- Growth: What exact activation threshold will count as real demand in the pilot?
- Growth: What price point will the coordinator accept after trying the workflow?
- Growth: Which permission boundaries are required for trust versus convenience?
- Tech recommendation needing arbitration: Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Tech recommendation needing arbitration: Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Tech recommendation needing arbitration: Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Tech recommendation needing arbitration: Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]
- Growth recommendation needing arbitration: Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]
- Growth recommendation needing arbitration: Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Growth recommendation needing arbitration: Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]
- Tech open question: Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Tech open question: Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Tech open question: Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- Growth open question: What exact activation threshold will count as real demand in the pilot?
- Growth open question: What price point will the coordinator accept after trying the workflow?
- Growth open question: Which permission boundaries are required for trust versus convenience?

## Risks

- Permission mistakes could expose sensitive notes or medication details to the wrong participant. [privacy_trust]
- Reminder delivery failures could undermine the core value proposition. [reliability]
- The product could become too broad if messaging and documents are added too early. [scope]
- Families may keep coordination in group chats because switching feels unnecessary.
- Siblings or caregivers may not adopt the tool after the coordinator invites them.
- Privacy concerns may prevent sharing of sensitive notes and schedules.
- Families may still default back to group text even after setup [adoption]
- Privacy concerns may block sharing sensitive notes [privacy_trust]
- Only the coordinator may use the product, leaving the rest of the circle passive [adoption]
- Families may not understand the fixed roles and may expect flexible sharing. [privacy_trust]
- A single mistake in permissions or notifications could permanently damage trust. [privacy_trust]
- Support overhead may be higher than expected if invite and role recovery is frequent. [operations]
- The coordinator signs up but cannot persuade siblings/caregivers to participate.
- Families continue using WhatsApp/text and never shift behavior.
- Privacy concerns block sharing of sensitive notes.

## Open Questions

- Which country or region is the initial launch target?
- Are medication reminders informational only, or do they include anything that could be construed as clinical guidance?
- What exact note/document types are visible to family members versus caregivers?
- Which country or legal jurisdiction is the first launch market?
- What is the minimum trust/privacy model families will accept?
- How many participants must actively use the circle for the product to be valuable?
- What exact demand signal counts as success: paid pilot, verbal willingness to pay, or repeated weekly use?
- Which country or state is the first compliant launch market?
- What is the minimum permission structure that still feels safe enough to share care information?
- Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- What exact activation threshold will count as real demand in the pilot?
- What price point will the coordinator accept after trying the workflow?
- Which permission boundaries are required for trust versus convenience?

## Final Revised PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care are using fragmented tools for high-stakes tasks: calls, text threads, paper notes, email, and ad hoc reminders. This causes missed appointments, duplicated effort, unclear ownership, and poor visibility between siblings and professional caregivers. The MVP problem is narrow: reliable coordination for one older adult across a small trusted circle, with trust and access control strong enough to handle sensitive care information.

## Initial Wedge
An invite-only coordination hub for one elder and their immediate care circle, focused on:
- one shared task list
- one appointment schedule
- one medication reminder stream
- one lightweight care notes feed
- one fixed permission model

The wedge is to make the first coordination cycle visibly easier without trying to replace medical records, chat apps, document repositories, or full caregiver software.

## First Target User
Primary user:
- An adult child who is the de facto coordinator for an aging parent

Secondary users in the first workflow:
- 1–3 siblings or relatives
- 1 professional caregiver or home aide, if present

This user already feels the burden of coordination and has a strong reason to centralize it.

## Existing Alternatives And Switching Trigger
Current alternatives:
- Group texts / WhatsApp threads
- Shared calendars
- Paper notebooks
- Notes app / email chains
- Generic task apps like Todoist or Trello
- Agency portals, if available

Switching trigger:
- information is getting lost across too many channels
- siblings disagree on responsibilities
- appointments or medication actions are being missed
- the coordinator needs a single source of truth that is simple enough for non-technical family members

## Core MVP Workflow
1. Primary user creates a care circle for one elder.
2. Invites family members and, optionally, one professional caregiver.
3. Adds recurring essentials:
   - appointments
   - medication reminder times
   - shared tasks
   - short care notes
4. Each participant sees only the data allowed by their role.
5. Notifications remind the right person at the right time.
6. Family members mark tasks complete and add short updates where permitted.
7. The coordinator sees what is done, overdue, or pending in one place.
8. All permission and access changes are recorded in an audit log.

## In Scope
- Single elder care circle setup
- Invite-only access for family and caregivers
- Fixed roles for coordinator, family member, and caregiver
- Shared task list with ownership and due dates
- Basic appointment entries and reminders
- Medication reminder schedules, informational only
- Lightweight care notes for instructions and updates
- Restricted visibility rules for notes, with default private visibility and explicit sharing
- Object-level visibility rules for tasks, appointments, medication reminders, and notes
- Notification delivery
- Activity log for key changes, completions, permission changes, and access events
- Support/admin ability to recover invites, correct roles, and revoke access during pilot
- Defined first launch geography
- Minimum compliance policy for that geography

## Out of Scope
- Full electronic health record replacement
- Clinical decision support
- Prescription management or pharmacy integrations
- Emergency response / 911 escalation
- Broad marketplace for hiring caregivers
- Telehealth visits
- Advanced AI summaries or care recommendations
- Insurance claims, billing, or payments
- Multi-elder household management
- Complex agency workflows
- Secure document storage
- Deep integrations with calendars, EHRs, pharmacies, or messaging apps
- Rich in-app chat
- Advanced analytics
- Public self-serve onboarding outside invite-only access

## MVP Build Vs Pilot Operations
### Must Build Now
- Invite-only care circle
- Fixed roles with defined visibility boundaries
- Shared task management
- Appointment entries and reminders
- Medication reminder schedules
- Lightweight notes feed with restricted visibility
- Notification system
- Activity log for access, permission, and content changes
- Admin/support tools for invite recovery, role fixes, and access revocation
- First-market compliance controls for stored care notes and reminders

### Manual Or Operational During Pilot
- White-glove onboarding for the first care circle
- Manual entry of initial tasks, appointments, and reminders if needed
- Support for setting up family roles and permissions
- Manual customer support for troubleshooting
- Compliance review for the first launch geography
- Pilot success tracking and follow-up with the coordinator

### Deferred Until After Proof
- Secure document storage and document organization
- Rich messaging/chat
- Multi-elder support
- Care agency dashboards
- Integrations with calendars, EHRs, pharmacies, or messaging apps
- Payments and billing
- Advanced analytics
- AI-generated summaries
- Emergency escalation workflows
- Public self-serve registration

## Business Model Hypothesis
The most plausible starting model is a subscription paid by the coordinating family:
- monthly fee for one care circle
- optional higher tier for additional participants or storage later

Pilot pricing should be tested explicitly, even if manually collected, to validate willingness to pay.

If consumer willingness to pay is weak, a later alternative is B2B2C licensing through elder care agencies or home care providers. That model should not be built into the MVP unless consumer demand fails.

## Critical Assumptions
- The coordination pain is frequent and severe enough to motivate adoption.
- One trusted family member is willing to set up and maintain the system.
- Other family members and caregivers will use a lightweight shared tool.
- Notifications and task ownership are enough to create visible value quickly.
- The permission model can be simple enough to understand and strong enough to earn trust.
- The product can be launched in a compliant way in the first geography.
- The coordinator will see enough value to pay, or at least continue after the pilot.

## How To Test Quickly
- Interview 10–15 adult children coordinating elder care.
- Map where tasks, reminders, and updates currently break down.
- Run a concierge pilot with 3–5 families using a lightweight prototype or no-code workflow.
- Measure whether the platform reduces missed tasks and duplicate reminders within 2–4 weeks.
- Test whether siblings and caregivers stay active after invitation.
- Test whether coordinators are willing to pay after the first coordination cycle.
- Confirm which features are actually used: tasks, reminders, notes, and permissions.
- Validate the first launch country’s minimum compliance requirements before any broader rollout.
- Use a paid pilot or committed deposit to test willingness to pay.

## Acceptance Criteria
- A coordinator can set up a care circle in under 10 minutes.
- Family members can be invited and granted access without training.
- A task can be assigned, reminded, and marked complete.
- A medication reminder can be scheduled and delivered reliably.
- Appointment details can be added and seen only by the right participants.
- Notes can be shared intentionally, with default private visibility for sensitive entries.
- Users can see who changed what, when, and which access changes occurred.
- Invite recovery and role correction can be handled quickly during pilot.
- The system supports at least one full care coordination cycle without requiring manual re-entry into other tools.
- At least 3 of 5 invited participants are active within 7 days in pilot.
- At least 2 recurring coordination actions are completed per week per circle in pilot.

## Risks And Failure Modes
- Siblings or caregivers do not adopt the system and keep using chat threads.
- Trust and privacy concerns block sharing of sensitive information.
- The product becomes too broad and loses the simplicity needed for adoption.
- Reminder fatigue causes users to ignore notifications.
- The coordinator still duplicates work across other channels.
- Compliance requirements vary by country and slow launch.
- The family subscription is useful but not compelling enough to sustain revenue.
- The permission model is either too loose to trust or too restrictive to be useful.
- Audit and recovery flows are insufficient when access mistakes happen.

## Product Readiness
Status: LIMITED

Blocking Gaps:
- First launch geography and compliance baseline must be fixed before build [compliance_scope]
- Exact role-to-data visibility rules for tasks, appointments, reminders, and notes must be finalized [privacy_trust]
- Willingness to pay by the primary coordinator is unproven [demand_validation]

Required Improvements:
- Choose one launch market and codify minimum data-handling rules before public rollout [compliance_scope]
- Finalize the smallest trusted visibility/edit model for care notes, tasks, and reminders [privacy_trust]
- Run a paid concierge pilot to test activation, retention, and monetization [demand_validation]

## Recommendation
Proceed with a narrow MVP focused on one elder, one coordinator, and one care circle in a single launch geography. Build only the shared coordination loop: tasks, appointments, medication reminders, restricted notes, permissions, notifications, auditability, and support recovery tools. Defer documents, chat, integrations, multi-elder support, and agency workflows until the core loop proves repeated use and willingness to pay. The fastest credible path is a concierge pilot with explicit pilot pricing and a fixed compliance baseline.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Tech: Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Growth: Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
