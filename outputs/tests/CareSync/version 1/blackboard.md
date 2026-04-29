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

## Human Clarifications

**Provided Answers:**

_None_

### Generated Clarification Questions

#### 1. Market Motion

**Question:**

What exact first launch segment, geography, or acquisition motion should the next run assume?


**Why It Matters:**

The first market motion drives GTM focus, product scope, and proof quality.


**Related Gap:**

The launch buyer and acquisition motion are still too broad and need a single Paris family-coordinator pilot path pinned down.


**Source:**

global_blocking_gap


#### 2. Market Motion

**Question:**

What exact first launch segment, geography, or acquisition motion should the next run assume?


**Why It Matters:**

The first market motion drives GTM focus, product scope, and proof quality.


**Related Gap:**

The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy


**Source:**

global_blocking_gap


#### 3. Market Motion

**Question:**

What exact first launch segment, geography, or acquisition motion should the next run assume?


**Why It Matters:**

The first market motion drives GTM focus, product scope, and proof quality.


**Related Gap:**

The reminder failure policy is not yet tied to a concrete pilot-safe activation loop.


**Source:**

global_blocking_gap


#### 4. Privacy Trust

**Question:**

What trust, consent, access, retention, or visibility rule should the next run assume?


**Why It Matters:**

Trust rules affect user adoption, architecture controls, and compliance posture.


**Related Gap:**

Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach


**Source:**

global_blocking_gap


#### 5. Supply Density

**Question:**

What minimum supply threshold or density condition should the next run use for the pilot?


**Why It Matters:**

Supply thresholds determine whether the pilot can create a credible user experience.


**Related Gap:**

Define a measurable activation threshold such as **3+ active participants and one completed weekly cycle**.


**Source:**

global_required_improvement


## Artifacts

## Architecture Markdown Ready

True


## Architecture Visual Ready

True


## Architecture Visual Warning

_Aucun contenu._


## Architecture Mermaid Ready

True


## Architecture Mermaid Source

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/CareSync/version 1/architecture-diagram.mmd


## Architecture Image Ready

True


## Architecture Image Path

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/CareSync/version 1/architecture-diagram.png


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### privacy_trust
- [privacy_trust] Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach
- [privacy_trust] The trust model for family and caregiver permissions is not yet validated in live use

### untagged
- The weekly care routine that best proves value still needs validation

## Product Required Improvements

### privacy_trust
- [privacy_trust] Define minimum privacy and consent rules for Paris deployment
- [privacy_trust] Validate the simplest role and permission model that families understand and accept

### operations
- [operations] Confirm which recurring weekly workflow best proves value before broadening scope

## Tech Status

LIMITED


## Tech Blocking Gaps

### privacy_trust
- [privacy_trust] The privacy, consent, and access-control model for sensitive care data in France is not fully specified

### market_motion
- [market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy

### data_access
- [data_access] The document handling model is too vague for safe implementation without deletion, access, and audit rules

## Tech Required Improvements

### privacy_trust
- [privacy_trust] Define the minimum French privacy posture, role permissions, and consent flow before build

### operations
- [operations] Choose the first notification transport and define retry/failure handling

### data_access
- [data_access] Specify document storage, access expiry, audit logging, and deletion behavior

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] The launch buyer and acquisition motion are still too broad and need a single Paris family-coordinator pilot path pinned down.
- [market_motion] The reminder failure policy is not yet tied to a concrete pilot-safe activation loop.

### demand_validation
- [demand_validation] The demand signal is not yet defined tightly enough to separate curiosity from real adoption.

## Growth Required Improvements

### market_motion
- [market_motion] Commit to a **Paris family-coordinator-led concierge pilot** as the only launch motion.
- [market_motion] Define a measurable activation threshold such as **3+ active participants and one completed weekly cycle**.
- [market_motion] Specify **email-first reminders with manual fallback** for the pilot so activation is not blocked by channel weakness.

## Global Status

LIMITED


## Global Blocking Gaps

### privacy_trust
- [privacy_trust] Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach
- [privacy_trust] The trust model for family and caregiver permissions is not yet validated in live use
- [privacy_trust] The privacy, consent, and access-control model for sensitive care data in France is not fully specified

### untagged
- The weekly care routine that best proves value still needs validation

### market_motion
- [market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy
- [market_motion] The launch buyer and acquisition motion are still too broad and need a single Paris family-coordinator pilot path pinned down.
- [market_motion] The reminder failure policy is not yet tied to a concrete pilot-safe activation loop.

### data_access
- [data_access] The document handling model is too vague for safe implementation without deletion, access, and audit rules

### demand_validation
- [demand_validation] The demand signal is not yet defined tightly enough to separate curiosity from real adoption.

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define minimum privacy and consent rules for Paris deployment
- [privacy_trust] Validate the simplest role and permission model that families understand and accept
- [privacy_trust] Define the minimum French privacy posture, role permissions, and consent flow before build

### operations
- [operations] Confirm which recurring weekly workflow best proves value before broadening scope
- [operations] Choose the first notification transport and define retry/failure handling

### data_access
- [data_access] Specify document storage, access expiry, audit logging, and deletion behavior

### market_motion
- [market_motion] Commit to a **Paris family-coordinator-led concierge pilot** as the only launch motion.
- [market_motion] Define a measurable activation threshold such as **3+ active participants and one completed weekly cycle**.
- [market_motion] Specify **email-first reminders with manual fallback** for the pilot so activation is not blocked by channel weakness.

## Known Tags

- market_motion
- operations
- scope
- privacy_trust
- onboarding
- data_access
- demand_validation
- untagged


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

#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy Choose one primary buyer and one primary acquisition path for the pilot


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The initial wedge may be too broad unless the first recurring care workflow is tightly defined Narrow the first use case to a single recurring care routine with measurable weekly value


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- growth


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] The first buyer and adoption path are still slightly ambiguous between family and caregiver-led entry


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

_Aucun contributeur._


### Loop 2

#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy The launch buyer and acquisition motion are still not pinned to one narrow, credible entry path The first reminder channel and fallback behavior are not yet tied to a pilot-safe activation model Define the pilot as **family-coordinator-led in Paris**, with founder-led concierge outreach as the only launch motion Set a measurable pilot success threshold, such as one completed weekly coordination cycle with 3+ active participants and no full reversion to WhatsApp Specify email-first reminder handling plus manual fallback during pilot if reminders are missed or ignored


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] The demand signal threshold is not explicit enough to distinguish interest from real adoption


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] Confirm which recurring weekly workflow best proves value before broadening scope Choose the first notification transport and define retry/failure handling


## Expected Output

A clear product decision on build-versus-manual scope.


## Contributors

- tech


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

### privacy_trust
- [privacy_trust] Privacy, consent, and data handling requirements for sensitive care information in France need a clear implementation approach
- [privacy_trust] The trust model for family and caregiver permissions is not yet validated
- [privacy_trust] The privacy, consent, and access-control model for sensitive care data in France is not fully specified
- [privacy_trust] The trust and privacy model for sensitive care information in France is not yet validated

### untagged
- The first care routine still needs confirmation as the strongest proof point

### market_motion
- [market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy

### data_access
- [data_access] The document handling model is too vague for safe implementation without deletion, access, and audit rules

### demand_validation
- [demand_validation] The first buyer and adoption path are still slightly ambiguous between family and caregiver-led entry

### scope
- [scope] The initial wedge may be too broad unless the first recurring care workflow is tightly defined

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define minimum privacy and consent rules for French deployment
- [privacy_trust] Validate the simplest role and permission model that families will actually understand
- [privacy_trust] Define the minimum French privacy posture, role permissions, and consent flow before build
- [privacy_trust] Define the minimum French privacy/consent posture and user-facing trust cues

### operations
- [operations] Confirm which recurring workflow best proves value: appointments, medication, or task ownership
- [operations] Choose the first notification transport and define retry/failure handling

### data_access
- [data_access] Specify document storage, access expiry, audit logging, and deletion behavior

### market_motion
- [market_motion] Choose one primary buyer and one primary acquisition path for the pilot

### scope
- [scope] Narrow the first use case to a single recurring care routine with measurable weekly value

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy Choose one primary buyer and one primary acquisition path for the pilot


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The initial wedge may be too broad unless the first recurring care workflow is tightly defined Narrow the first use case to a single recurring care routine with measurable weekly value


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] The first buyer and adoption path are still slightly ambiguous between family and caregiver-led entry


## Expected Output

A concrete demand-validation approach with a signal threshold.


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

### privacy_trust
- [privacy_trust] Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach
- [privacy_trust] The trust model for family and caregiver permissions is not yet validated in live use
- [privacy_trust] The privacy, consent, and access-control model for sensitive care data in France is not fully specified

### untagged
- The weekly care routine that best proves value still needs validation

### market_motion
- [market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy
- [market_motion] The launch buyer and acquisition motion are still not pinned to one narrow, credible entry path
- [market_motion] The first reminder channel and fallback behavior are not yet tied to a pilot-safe activation model

### data_access
- [data_access] The document handling model is too vague for safe implementation without deletion, access, and audit rules

### demand_validation
- [demand_validation] The demand signal threshold is not explicit enough to distinguish interest from real adoption

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define minimum privacy and consent rules for Paris deployment
- [privacy_trust] Validate the simplest role and permission model that families understand and accept
- [privacy_trust] Define the minimum French privacy posture, role permissions, and consent flow before build

### operations
- [operations] Confirm which recurring weekly workflow best proves value before broadening scope
- [operations] Choose the first notification transport and define retry/failure handling

### data_access
- [data_access] Specify document storage, access expiry, audit logging, and deletion behavior

### market_motion
- [market_motion] Define the pilot as **family-coordinator-led in Paris**, with founder-led concierge outreach as the only launch motion
- [market_motion] Set a measurable pilot success threshold, such as one completed weekly coordination cycle with 3+ active participants and no full reversion to WhatsApp
- [market_motion] Specify email-first reminder handling plus manual fallback during pilot if reminders are missed or ignored

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy Choose one primary buyer and one primary acquisition path for the pilot


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The initial wedge may be too broad unless the first recurring care workflow is tightly defined Narrow the first use case to a single recurring care routine with measurable weekly value


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] The first buyer and adoption path are still slightly ambiguous between family and caregiver-led entry


## Expected Output

A concrete demand-validation approach with a signal threshold.


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

### privacy_trust
- [privacy_trust] Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach
- [privacy_trust] The trust model for family and caregiver permissions is not yet validated in live use
- [privacy_trust] The privacy, consent, and access-control model for sensitive care data in France is not fully specified

### untagged
- The weekly care routine that best proves value still needs validation

### market_motion
- [market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy
- [market_motion] The launch buyer and acquisition motion are still not pinned to one narrow, credible entry path
- [market_motion] The first reminder channel and fallback behavior are not yet tied to a pilot-safe activation model

### data_access
- [data_access] The document handling model is too vague for safe implementation without deletion, access, and audit rules

### demand_validation
- [demand_validation] The demand signal threshold is not explicit enough to distinguish interest from real adoption

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define minimum privacy and consent rules for Paris deployment
- [privacy_trust] Validate the simplest role and permission model that families understand and accept
- [privacy_trust] Define the minimum French privacy posture, role permissions, and consent flow before build

### operations
- [operations] Confirm which recurring weekly workflow best proves value before broadening scope
- [operations] Choose the first notification transport and define retry/failure handling

### data_access
- [data_access] Specify document storage, access expiry, audit logging, and deletion behavior

### market_motion
- [market_motion] Define the pilot as **family-coordinator-led in Paris**, with founder-led concierge outreach as the only launch motion
- [market_motion] Set a measurable pilot success threshold, such as one completed weekly coordination cycle with 3+ active participants and no full reversion to WhatsApp
- [market_motion] Specify email-first reminder handling plus manual fallback during pilot if reminders are missed or ignored

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy The launch buyer and acquisition motion are still not pinned to one narrow, credible entry path The first reminder channel and fallback behavior are not yet tied to a pilot-safe activation model Define the pilot as **family-coordinator-led in Paris**, with founder-led concierge outreach as the only launch motion Set a measurable pilot success threshold, such as one completed weekly coordination cycle with 3+ active participants and no full reversion to WhatsApp Specify email-first reminder handling plus manual fallback during pilot if reminders are missed or ignored


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] The demand signal threshold is not explicit enough to distinguish interest from real adoption


## Expected Output

A concrete demand-validation approach with a signal threshold.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] Confirm which recurring weekly workflow best proves value before broadening scope Choose the first notification transport and define retry/failure handling


## Expected Output

A clear product decision on build-versus-manual scope.


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

### privacy_trust
- [privacy_trust] Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach
- [privacy_trust] The trust model for family and caregiver permissions is not yet validated in live use
- [privacy_trust] The privacy, consent, and access-control model for sensitive care data in France is not fully specified

### untagged
- The weekly care routine that best proves value still needs validation

### market_motion
- [market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy
- [market_motion] The launch buyer and acquisition motion are still too broad and need a single Paris family-coordinator pilot path pinned down.
- [market_motion] The reminder failure policy is not yet tied to a concrete pilot-safe activation loop.

### data_access
- [data_access] The document handling model is too vague for safe implementation without deletion, access, and audit rules

### demand_validation
- [demand_validation] The demand signal is not yet defined tightly enough to separate curiosity from real adoption.

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define minimum privacy and consent rules for Paris deployment
- [privacy_trust] Validate the simplest role and permission model that families understand and accept
- [privacy_trust] Define the minimum French privacy posture, role permissions, and consent flow before build

### operations
- [operations] Confirm which recurring weekly workflow best proves value before broadening scope
- [operations] Choose the first notification transport and define retry/failure handling

### data_access
- [data_access] Specify document storage, access expiry, audit logging, and deletion behavior

### market_motion
- [market_motion] Commit to a **Paris family-coordinator-led concierge pilot** as the only launch motion.
- [market_motion] Define a measurable activation threshold such as **3+ active participants and one completed weekly cycle**.
- [market_motion] Specify **email-first reminders with manual fallback** for the pilot so activation is not blocked by channel weakness.

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The reminder and notification delivery model is not yet pinned to a reliable first channel and failure policy The launch buyer and acquisition motion are still not pinned to one narrow, credible entry path The first reminder channel and fallback behavior are not yet tied to a pilot-safe activation model Define the pilot as **family-coordinator-led in Paris**, with founder-led concierge outreach as the only launch motion Set a measurable pilot success threshold, such as one completed weekly coordination cycle with 3+ active participants and no full reversion to WhatsApp Specify email-first reminder handling plus manual fallback during pilot if reminders are missed or ignored


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] The demand signal threshold is not explicit enough to distinguish interest from real adoption


## Expected Output

A concrete demand-validation approach with a signal threshold.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] Confirm which recurring weekly workflow best proves value before broadening scope Choose the first notification transport and define retry/failure handling


## Expected Output

A clear product decision on build-versus-manual scope.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP [scope]
- [tech] Replace “secure messaging system” with structured notes/updates on tasks and appointments [scope]

## Growth Structural Decisions

### growth
- [growth] Add a **single explicit pilot definition**: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp. [market_motion]
- [growth] Specify the **first demand signal threshold**: an invited coordinator must complete onboarding and activate at least 2 additional participants within a set time window. [demand_validation]

## Product Locking

## Applied

True


## Confirmed In Scope

- One care space per relative
- Invitation-only access
- Family coordinator, family member, and caregiver roles
- Simple role-based read/write permissions
- Shared appointments and task ownership
- Structured notes / updates
- Emergency contact list
- Limited document upload for essential care items
- Email-first notifications
- Audit trail for invites, permission changes, document access, and deletions
- Explicit per-relative care-space security boundary
- No cross-space sharing in MVP


## Confirmed Deferred

- Push notifications as a required channel
- Multiple relatives per account
- Rich messaging
- Clinical integrations
- Payments
- Care agency tools
- AI assistance
- Document intelligence
- Elder-facing accessibility mode
- Cross-space sharing


## Confirmed Out Of Scope

- Full electronic health record replacement
- Doctor or hospital integrations
- Prescription ordering or medication fulfillment
- Telemedicine
- AI-generated care plans
- Complex clinical workflows
- Elderly-user-first interface for low-literacy users
- Marketplace for home care services
- Billing, payments, and insurance handling
- Multi-relative household management
- Advanced document OCR or medical document parsing
- General-purpose secure messaging replacing existing chat apps
- Agency admin tools
- Broad medication management workflows beyond a simple reminder if already part of the family routine


## Locking Note

- Keep the MVP locked to one relative, one coordinator, and one recurring weekly routine. - Do not add new channels, broader messaging, or multi-relative support. - Use pilot operations for onboarding and fallback support, not product expansion.


## Expert Contributions

### Tech Summary

The key feasibility issue is not feature breadth but **safe coordination of sensitive care information in a closed family-and-caregiver space**. The MVP should stay narrow: one relative, one care space, invitation-only access, structured tasks/appointments, limited documents, and email-first reminders, with manual onboarding and support to compensate for the lack of automation.

## Tech Structural Decisions

- Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP [scope]
- Replace “secure messaging system” with structured notes/updates on tasks and appointments [scope]


## Tech Recommendations

- Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP [scope]
- Replace “secure messaging system” with structured notes/updates on tasks and appointments [scope]
- Specify an email-first notification policy and make push optional, not required for launch [onboarding]
- Add a minimum audit trail for invites, permission changes, document access, and deletions [privacy_trust]
- Clarify the exact role model and what each role can read, edit, and share [privacy_trust]


## Tech Risks

- Health-adjacent data may trigger privacy expectations that the MVP cannot safely meet if controls are weak [privacy_trust]
- Reminder delivery failures or duplicate notifications could quickly destroy trust [operational_reliability]
- Overlapping permissions between family and caregivers may create accidental disclosure [access_control]


## Tech Open Questions

- Which data elements are considered mandatory versus optional in the first release, especially around medication and documents?
- Should caregivers have write access to tasks and notes, or read-only access initially?
- Is email sufficient for all reminder flows during pilot, or must push be supported from day one?


### Growth Summary

The main launch challenge is not product breadth but proving that a Paris family coordinator will actually move one real care routine into CareSync and keep using it after the first week. The recommended direction is a founder-led, concierge pilot with a very narrow audience, one relative, and one recurring weekly routine, using email-first reminders plus manual fallback to validate real adoption.

## Growth Structural Decisions

- Add a **single explicit pilot definition**: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp. [market_motion]
- Specify the **first demand signal threshold**: an invited coordinator must complete onboarding and activate at least 2 additional participants within a set time window. [demand_validation]


## Growth Recommendations

- Add a **single explicit pilot definition**: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp. [market_motion]
- Specify the **first demand signal threshold**: an invited coordinator must complete onboarding and activate at least 2 additional participants within a set time window. [demand_validation]
- Clarify the **first reminder policy**: email-first during pilot, with manual fallback if reminders are missed or ignored. [market_motion]
- Define the **narrowest launch audience** more concretely as adult children in Paris coordinating one parent’s care, not all family caregivers broadly. [market_motion]
- Add a **pilot success metric** tied to repeated use, not just sign-up: at least one full weekly cycle plus continued use in week two. [demand_validation]


## Growth Risks

- Families may agree to try the product but fail to move actual coordination behavior out of WhatsApp. [demand_validation]
- The coordinator may sign up, but other relatives or caregivers may not participate. [onboarding]
- Email-only reminders may be too weak for real-world care coordination. [operations]


## Growth Open Questions

- What exact Paris recruitment channel will produce the first 10–15 family coordinators? [market_motion]
- What is the minimum acceptable participant activation rate for a valid pilot? [demand_validation]
- Is the first weekly routine best centered on appointments, task handoffs, or both? [value_proof]


## Product Arbitration

## Source

parsed


## Retained

- Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP
- Replace secure messaging with structured notes/updates on tasks and appointments
- Specify an email-first notification policy and make push optional, not required for launch
- Add a minimum audit trail for invites, permission changes, document access, and deletions
- Clarify the exact role model and what each role can read, edit, and share
- Add a single explicit pilot definition: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp
- Clarify the first reminder policy: email-first during pilot, with manual fallback if reminders are missed or ignored
- Define the narrowest launch audience more concretely as adult children in Paris coordinating one parent’s care, not all family caregivers broadly
- Add a pilot success metric tied to repeated use, not just sign-up: at least one full weekly cycle plus continued use in week two


## Deferred

- Push notifications as a required channel
- Multiple relatives per account
- Rich messaging
- Clinical integrations
- Payments
- Care agency tools
- AI assistance
- Document intelligence
- Elder-facing accessibility mode
- Cross-space sharing


## Rejected

- General-purpose secure messaging replacing existing chat apps
- Full electronic health record replacement
- Doctor or hospital integrations
- Prescription ordering or medication fulfillment
- Telemedicine
- AI-generated care plans
- Complex clinical workflows
- Marketplace for home care services
- Billing, payments, and insurance handling
- Multi-relative household management
- Advanced document OCR or medical document parsing
- Agency admin tools
- Broad medication management workflows beyond a simple reminder if already part of the family routine


## Open Points

- Minimum privacy and consent implementation approach for France
- Whether caregivers should have write access or read-only access initially
- Exact weekly routine to prioritize first: appointments, task handoffs, or both
- Minimum acceptable participant activation rate for a valid pilot
- Which Paris recruitment channel will produce the first 10–15 family coordinators


## Rationales

- The MVP must prove that one family coordinator will move one real care routine into a dedicated tool and keep using it
- Structured notes are sufficient for coordination proof; full messaging is not needed to validate value
- Email-first is the narrowest launch channel with the lowest implementation burden
- Auditability and permission clarity are non-negotiable because trust is central to adoption
- Concierge onboarding and manual fallback are operational supports, not product scope
- The product is not ready for a broad launch because privacy/compliance and live trust behavior remain unproven


## Reconciliation Notes

- Parsed Product Arbitration supplied by Product; heuristic reconciliation was not needed.


## Reconciliation Warnings

_Aucune contradiction détectée._


## Source PRD

_Aucun contenu._

## Initial PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating care for an elderly relative lose time and confidence because information is fragmented across calls, chat threads, paper notes, and ad hoc caregiver updates. The core problem is not “full healthcare management”; it is reliable shared coordination so the right person knows the next appointment, task, or medication-related action.

## Initial Wedge
Start with one narrow wedge: shared coordination for one elderly relative among 2–5 family caregivers in Paris, focused on appointments and caregiving tasks, with a simple shared timeline and responsibility assignment.

This wedge is credible because it solves a frequent, recurring coordination failure without requiring deep clinical integrations or complex elder-facing workflows.

## First Target User
Primary user: an adult child in Paris who is the informal care coordinator for an aging parent.

Secondary users in the first use case:
- one or two siblings living elsewhere
- one professional caregiver or home assistant who already interacts with the family

The elderly relative is not the primary product user in the MVP unless they are digitally comfortable.

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp / SMS groups
- shared calendars
- paper notebooks and printed documents
- phone calls between siblings and caregivers
- generic task apps

Switching trigger:
- coordination is failing often enough that people miss appointments, duplicate tasks, or do not know who is responsible
- the family needs one shared source of truth with simple permissions and reminders
- the coordinator wants less repetition and fewer “who is doing what?” messages

## Core MVP Workflow
1. The coordinator creates a care space for one relative.
2. They invite family members and optionally one caregiver.
3. They add a few essential items:
   - upcoming appointments
   - recurring medication reminders
   - caregiving tasks
   - key contacts
4. Each item has one owner and due time/date.
5. Participants receive reminders and can mark tasks complete or note a change.
6. The group sees a simple shared timeline and current responsibilities.
7. Basic document upload is available only for key items needed to support coordination, not as a full records system.

## In Scope
- Shared care space for one elderly relative
- Invite family members and one or more caregivers
- Appointment list with date, time, place, and owner
- Recurring medication reminders at a basic level
- Task assignment and completion tracking
- Emergency contact list
- Simple shared notes / updates
- Limited document upload for essential care documents
- Basic permissioning by role
- Notifications/reminders by email and/or push
- Simple mobile-friendly interface

## Out of Scope
- Full electronic health record replacement
- Doctor or hospital integrations
- Prescription ordering or medication fulfillment
- Telemedicine
- AI-generated care plans
- Complex clinical workflows
- Elderly-user-first interface for low-literacy users
- Marketplace for home care services
- Billing, payments, and insurance handling
- Multi-relative household management as a first release
- Advanced document OCR or medical document parsing
- End-to-end secure messaging replacing existing chat apps

## MVP Build Vs Pilot Operations
### Must Build Now
- Care space for one relative
- Invitations and role-based access
- Shared appointments
- Basic recurring reminders
- Task assignment and completion
- Shared notes
- Emergency contacts
- Essential document upload
- Notifications

### Manual Or Operational During Pilot
- Onboarding families and caregivers
- Helping define the first care structure
- Importing initial appointments and tasks
- Customer support for setup issues
- Moderating permission requests
- Answering privacy/trust questions

### Deferred Until After Proof
- Multiple relatives per account
- Advanced permissions and audit logs
- Clinical integrations
- Rich messaging
- Payments
- Care agency admin tools
- AI assistance
- Document intelligence
- Elder-facing accessibility mode

## Business Model Hypothesis
Best initial model: family-paid subscription for the coordinating household, with optional later expansion to caregiver or agency plans.

Why this is plausible:
- the primary value is reduced family coordination stress and fewer missed actions
- the family coordinator is the buyer and feels the pain immediately
- a simple subscription is easier than depending on providers or insurers early

## Critical Assumptions
- Families will adopt a new tool if it clearly reduces coordination friction
- The coordinator can get at least a few other participants to use it
- Basic reminders and shared task visibility are enough to prove value
- Trust can be established without heavy enterprise-style tooling at MVP stage
- Users will not require full medical-record functionality to see value
- A narrow family-centric product is sufficient before serving agencies broadly

## How To Test Quickly
- Run concierge pilots with 10–15 families in Paris caring for one elderly relative each
- Manually onboard each family and load their first appointments/tasks
- Measure whether the coordinator uses it weekly for 3–4 weeks
- Track whether reminders reduce missed or duplicated tasks
- Interview participants about whether it replaced WhatsApp/paper for coordination
- Test willingness to pay after demonstrating recurring usage

## Acceptance Criteria
- A coordinator can create a care space in under 5 minutes
- At least 2 family members and 1 caregiver can be invited successfully
- Users can add and assign appointments and tasks
- Reminders are delivered reliably
- Users can see current ownership and upcoming items at a glance
- Basic document upload works for a small set of files
- Permissioning prevents unauthorized access to shared information
- Pilot families can complete a full weekly coordination cycle without reverting entirely to informal channels

## Risks And Failure Modes
- Adoption friction: family members refuse to install or use another app
- Trust risk: users hesitate to share sensitive information
- Scope creep: product becomes too broad for a narrow MVP
- Compliance risk: handling medical-related data without enough controls
- Value risk: reminders and task lists may not be differentiated enough from existing tools
- Operational burden: setup support may be too manual to scale
- Elderly-user mismatch: the intended beneficiary may not be the actual user

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Privacy, consent, and data handling requirements for sensitive care information in France need a clear implementation approach [privacy_compliance]
- The trust model for family and caregiver permissions is not yet validated [trust_model]
- The first use case may still be too close to generic task management unless onboarding clearly centers care-specific recurring coordination [value_proof]

Required Improvements:
- Define minimum privacy and consent rules for French deployment [privacy_compliance]
- Validate whether the coordinator will invite caregivers into the shared space or keep them outside the product [trust_model]
- Tighten onboarding and first-time setup around one recurring care routine [value_proof]

## Recommendation
Proceed with a narrow concierge-style MVP focused on one relative, one coordinating family, and one recurring care workflow in Paris. Do not expand into broader healthcare services, agency tooling, or complex medical features until this wedge proves repeated weekly usage and clear willingness to pay.

## Retained Decisions

- Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP
- Replace secure messaging with structured notes/updates on tasks and appointments
- Specify an email-first notification policy and make push optional, not required for launch
- Add a minimum audit trail for invites, permission changes, document access, and deletions
- Clarify the exact role model and what each role can read, edit, and share
- Add a single explicit pilot definition: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp
- Clarify the first reminder policy: email-first during pilot, with manual fallback if reminders are missed or ignored
- Define the narrowest launch audience more concretely as adult children in Paris coordinating one parent’s care, not all family caregivers broadly
- Add a pilot success metric tied to repeated use, not just sign-up: at least one full weekly cycle plus continued use in week two

## Deferred Decisions

- Push notifications as a required channel
- Multiple relatives per account
- Rich messaging
- Clinical integrations
- Payments
- Care agency tools
- AI assistance
- Document intelligence
- Elder-facing accessibility mode
- Cross-space sharing

## Rejected Recommendations

- General-purpose secure messaging replacing existing chat apps
- Full electronic health record replacement
- Doctor or hospital integrations
- Prescription ordering or medication fulfillment
- Telemedicine
- AI-generated care plans
- Complex clinical workflows
- Marketplace for home care services
- Billing, payments, and insurance handling
- Multi-relative household management
- Advanced document OCR or medical document parsing
- Agency admin tools
- Broad medication management workflows beyond a simple reminder if already part of the family routine

## Unresolved Tensions

- Tech recommendation needing arbitration: Replace “secure messaging system” with structured notes/updates on tasks and appointments [scope]
- Tech recommendation needing arbitration: Specify an email-first notification policy and make push optional, not required for launch [onboarding]
- Tech recommendation needing arbitration: Add a minimum audit trail for invites, permission changes, document access, and deletions [privacy_trust]
- Tech recommendation needing arbitration: Clarify the exact role model and what each role can read, edit, and share [privacy_trust]
- Growth recommendation needing arbitration: Specify the **first demand signal threshold**: an invited coordinator must complete onboarding and activate at least 2 additional participants within a set time window. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **first reminder policy**: email-first during pilot, with manual fallback if reminders are missed or ignored. [market_motion]
- Growth recommendation needing arbitration: Define the **narrowest launch audience** more concretely as adult children in Paris coordinating one parent’s care, not all family caregivers broadly. [market_motion]
- Growth recommendation needing arbitration: Add a **pilot success metric** tied to repeated use, not just sign-up: at least one full weekly cycle plus continued use in week two. [demand_validation]
- Tech open question: Which data elements are considered mandatory versus optional in the first release, especially around medication and documents?
- Tech open question: Should caregivers have write access to tasks and notes, or read-only access initially?
- Tech open question: Is email sufficient for all reminder flows during pilot, or must push be supported from day one?
- Growth open question: What exact Paris recruitment channel will produce the first 10–15 family coordinators? [market_motion]
- Growth open question: What is the minimum acceptable participant activation rate for a valid pilot? [demand_validation]
- Growth open question: Is the first weekly routine best centered on appointments, task handoffs, or both? [value_proof]

## Applied Changes

- Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP
- Replace secure messaging with structured notes/updates on tasks and appointments
- Specify an email-first notification policy and make push optional, not required for launch
- Add a minimum audit trail for invites, permission changes, document access, and deletions
- Clarify the exact role model and what each role can read, edit, and share
- Add a single explicit pilot definition: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp
- Clarify the first reminder policy: email-first during pilot, with manual fallback if reminders are missed or ignored
- Define the narrowest launch audience more concretely as adult children in Paris coordinating one parent’s care, not all family caregivers broadly
- Add a pilot success metric tied to repeated use, not just sign-up: at least one full weekly cycle plus continued use in week two

## Remaining Open Points

- Minimum privacy and consent implementation approach for France
- Whether caregivers should have write access or read-only access initially
- Exact weekly routine to prioritize first: appointments, task handoffs, or both
- Minimum acceptable participant activation rate for a valid pilot
- Which Paris recruitment channel will produce the first 10–15 family coordinators

## Risks

- Families may see it as “yet another app” and refuse adoption [adoption_friction]
- Caregivers may prefer existing communication channels and ignore the platform [channel_resistance]
- Sensitive information may slow conversion before trust is established [privacy_trust]
- Health-adjacent data may trigger privacy expectations that the MVP cannot safely meet if controls are weak [privacy_trust]
- Reminder delivery failures or duplicate notifications could quickly destroy trust [operational_reliability]
- Overlapping permissions between family and caregivers may create accidental disclosure [access_control]
- Families may treat this as “another app” and refuse to adopt.
- Caregivers may not actively participate, reducing the perceived value.
- Trust concerns around sensitive data may block invitation acceptance.
- Families may agree to try the product but fail to move actual coordination behavior out of WhatsApp. [demand_validation]
- The coordinator may sign up, but other relatives or caregivers may not participate. [onboarding]
- Email-only reminders may be too weak for real-world care coordination. [operations]

## Open Questions

- Will the first buyer be a family coordinator, or can a caregiver initiate adoption credibly?
- Which exact recurring routine creates the strongest proof: appointments, medications, or task ownership?
- How many external participants must actively use the product for the coordinator to feel value?
- Which data elements are considered mandatory versus optional in the first release, especially around medication and documents?
- Should caregivers have write access to tasks and notes, or read-only access initially?
- Is email sufficient for all reminder flows during pilot, or must push be supported from day one?
- Which specific recurring care event best creates repeat use in Paris: appointments, task handoffs, or medication checks?
- What minimum privacy and consent posture is required for a Paris pilot with family and caregiver participants?
- How many invited participants must be active in week 1 for the family to count as a validated pilot?
- What exact Paris recruitment channel will produce the first 10–15 family coordinators? [market_motion]
- What is the minimum acceptable participant activation rate for a valid pilot? [demand_validation]
- Is the first weekly routine best centered on appointments, task handoffs, or both? [value_proof]

## Final Revised PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating care for an elderly relative lose time and confidence because information is fragmented across calls, chat threads, paper notes, and ad hoc caregiver updates. The first problem to solve is not full healthcare management; it is reliable shared coordination for one relative.

## Initial Wedge
A single invitation-only care space for one elderly relative in Paris, used by one family coordinator and 2–4 other participants, to manage one recurring weekly care routine.

The narrowest credible wedge is:
- one relative
- one coordinator
- one recurring routine
- one shared source of truth for appointments and task ownership

This is narrow enough to prove value without drifting into full caregiving software.

## First Target User
Primary user: an adult child in Paris who coordinates care for an aging parent.

First use case:
- a weekly family coordination routine around appointments and task handoffs for one relative

Secondary users in the first use case:
- 1–2 siblings or relatives in other locations
- optionally one professional caregiver or home assistant already involved in the routine

The elderly relative is not the primary user in the MVP unless they are unusually comfortable with digital tools.

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp / SMS groups
- shared calendars
- paper notebooks and printed documents
- phone calls between family members and caregivers
- generic task apps

Switching trigger:
- a recent coordination failure caused a missed appointment, duplicated task, or confusion about responsibility
- the coordinator needs one shared source of truth for one relative
- the family wants fewer repeated status calls and fewer scattered updates

## Core MVP Workflow
1. The coordinator creates one care space for one relative.
2. They invite family members and optionally one caregiver.
3. They assign each participant a role with simple read/write permissions.
4. They add the recurring weekly routine:
   - appointments
   - care task handoffs
5. Each item has one owner and one due date/time.
6. Participants receive email reminders.
7. Participants mark items complete or add a structured update.
8. The group sees a simple shared timeline and current responsibilities.
9. Essential documents can be uploaded only when needed for coordination.

## In Scope
- One care space per relative
- Invitation-only access
- Family coordinator, family member, and caregiver roles
- Simple role-based read/write permissions
- One recurring weekly routine per care space
- Shared appointments
- Task assignment and completion tracking
- Structured notes / updates on tasks and appointments
- Emergency contact list
- Limited document upload for essential care items
- Invite, permission, document-access, and deletion audit trail
- Email-first notifications
- Simple mobile-friendly interface
- Explicit per-relative care-space security boundary
- No cross-space sharing in MVP

## Out of Scope
- Full electronic health record replacement
- Doctor or hospital integrations
- Prescription ordering or medication fulfillment
- Telemedicine
- AI-generated care plans
- Complex clinical workflows
- Elderly-user-first interface for low-literacy users
- Marketplace for home care services
- Billing, payments, and insurance handling
- Multi-relative household management
- Advanced document OCR or medical document parsing
- General-purpose secure messaging replacing existing chat apps
- Push notifications as a required launch channel
- Cross-space sharing between relatives
- Agency admin tools
- Broad medication management workflows beyond a simple reminder if already part of the family routine

## MVP Build Vs Pilot Operations
### Must Build Now
- One relative per care space
- Invitation-only access
- Role-based permissions
- Shared appointments
- Task assignment and completion
- Structured notes / updates
- Emergency contacts
- Limited document upload
- Email-first notifications
- Audit trail for invites, permission changes, document access, and deletions
- Explicit per-relative care-space security boundary

### Manual Or Operational During Pilot
- Founder-led concierge onboarding
- Setting up the first weekly routine
- Loading initial appointments and tasks
- Customer support for setup and trust questions
- Explaining privacy and consent expectations
- Moderating permission disputes
- Manual reminder fallback if email is missed
- Manual follow-up to keep the pilot moving if a participant does not activate

### Deferred Until After Proof
- Push notifications as a required channel
- Multiple relatives per account
- Rich messaging
- Clinical integrations
- Payments
- Care agency tools
- AI assistance
- Document intelligence
- Elder-facing accessibility mode
- Cross-space sharing

## Business Model Hypothesis
Initial model: family-paid subscription for the coordinating household.

Why this is plausible:
- the family coordinator feels the pain directly
- value comes from reducing confusion and missed actions
- a simple subscription is easier than relying on providers or insurers early

## Critical Assumptions
- One family coordinator can recruit a small circle of participants into the tool
- A weekly appointment + task ownership workflow is enough to show recurring value
- Users trust an invitation-only, role-based space for sensitive care information
- Email reminders are sufficient for the first pilot
- The product is distinct enough from generic task apps because it is care-specific
- A narrow family-led product can prove value before serving agencies
- Caregivers can participate without needing a full messaging layer

## How To Test Quickly
- Run concierge pilots with 10–15 Paris families caring for one relative each
- Start each pilot with one recurring weekly coordination cycle
- Manually onboard each family and set up the first routine
- Measure whether the coordinator uses the product for the full weekly cycle
- Track missed, duplicated, or delayed tasks before and after adoption
- Track whether invited relatives and caregivers actually participate
- Interview users about trust, clarity, and whether the product replaced part of WhatsApp or paper
- Ask for willingness to pay after repeated use is demonstrated
- If email reminders fail, keep reminder fallback manual during the pilot rather than expanding channels
- Validate that at least 2 additional participants activate after coordinator onboarding in a set time window

## Acceptance Criteria
- A coordinator can create one care space in under 5 minutes
- The coordinator can invite at least 2 family members and 1 caregiver
- Each participant can be assigned a clear role and permission level
- Users can add and update appointments and tasks
- Email reminders are delivered reliably
- Users can see ownership and upcoming items at a glance
- Structured notes can be attached to items
- Essential documents can be uploaded and accessed only by authorized users
- An audit trail records invites, permission changes, document access, and deletions
- A pilot family can complete at least one full weekly coordination cycle without reverting entirely to WhatsApp for that cycle
- At least one pilot family continues into week two after the first completed cycle

## Risks And Failure Modes
- Adoption friction: family members refuse to join another tool
- Trust risk: users hesitate to share sensitive information
- Scope creep: the product expands beyond a narrow coordination wedge
- Compliance risk: sensitive care data is handled without enough safeguards
- Value risk: the product feels too similar to generic task tools
- Operational burden: onboarding support is too manual to scale
- Participation risk: invited caregivers do not actively use the space
- Usage mismatch: the elderly relative is not the actual user
- Reminder failure: email alone is not enough for some families

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Minimum privacy, consent, and data handling requirements for sensitive care information in France need a confirmed implementation approach [privacy_compliance]
- The trust model for family and caregiver permissions is not yet validated in live use [trust_model]
- The weekly care routine that best proves value still needs validation [value_proof]

Required Improvements:
- Define minimum privacy and consent rules for Paris deployment [privacy_compliance]
- Validate the simplest role and permission model that families understand and accept [trust_model]
- Confirm which recurring weekly workflow best proves value before broadening scope [value_proof]

## Recommendation
Proceed with a concierge-led MVP in Paris focused on one relative, one family coordinator, and one recurring weekly coordination routine. Keep the product invitation-only, care-specific, and centered on appointments plus task ownership. Do not expand into agency tooling, rich messaging, multi-relative management, or broader healthcare features until the MVP proves repeated weekly use, clear trust, and willingness to pay.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Define one explicit care-space security boundary per relative and prohibit cross-space sharing in MVP
- Replace secure messaging with structured notes/updates on tasks and appointments
- Specify an email-first notification policy and make push optional, not required for launch
- Add a minimum audit trail for invites, permission changes, document access, and deletions
- Clarify the exact role model and what each role can read, edit, and share
- Add a single explicit pilot definition: Paris-based, family-coordinator-led, one relative, one weekly routine, 3+ active participants, one completed cycle without full reversion to WhatsApp
- Clarify the first reminder policy: email-first during pilot, with manual fallback if reminders are missed or ignored
- Define the narrowest launch audience more concretely as adult children in Paris coordinating one parent’s care, not all family caregivers broadly
- Add a pilot success metric tied to repeated use, not just sign-up: at least one full weekly cycle plus continued use in week two

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- growth_agent: gtm_notes_generated
- tech_agent: architecture_notes_generated
- product_agent: prd_draft_revised
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
- product_agent: arbitration_reconciled
