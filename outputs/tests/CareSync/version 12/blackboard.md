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

### privacy_trust
- [privacy_trust] Initial launch geography and its minimum privacy, retention, deletion, and consent rules are not yet fixed
- [privacy_trust] Reminder delivery, role permissions, and audit history need real-world validation with families

### demand_validation
- [demand_validation] Real switching behavior from chat/spreadsheets to CareSync is not yet proven

## Product Required Improvements

### privacy_trust
- [privacy_trust] Define one initial launch geography and attach the minimum privacy and deletion rules

### demand_validation
- [demand_validation] Validate coordination migration with concierge pilots using real families

### market_motion
- [market_motion] Test reminder delivery, permissions, audit history, and visible failure handling with pilot users

## Tech Status

LIMITED


## Tech Blocking Gaps

### privacy_trust
- [privacy_trust] Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized
- [privacy_trust] The permission model is not specific enough to safely enforce access boundaries for sensitive care data

### market_motion
- [market_motion] The internal support/admin surface is not yet defined, but pilot operations require audited staff controls

## Tech Required Improvements

### privacy_trust
- [privacy_trust] Choose one initial launch geography and document the minimum privacy/compliance requirements
- [privacy_trust] Define the exact role-to-resource permission matrix for coordinator, family member, and caregiver

### market_motion
- [market_motion] Specify the minimum internal admin actions and audit rules needed for pilot support

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] No single primary acquisition motion is defined yet
- [market_motion] The smallest credible launch audience is not yet narrowed enough for a focused pilot
- [market_motion] Reminder channel and failure handling are not specified tightly enough for trust-critical pilot use

### demand_validation
- [demand_validation] Switching behavior from chat/spreadsheets to CareSync is unproven and needs a measurable experiment

### privacy_trust
- [privacy_trust] Launch geography and minimum compliance posture remain undefined

## Growth Required Improvements

### market_motion
- [market_motion] Choose one founder-led acquisition motion and a clear launch threshold for the pilot
- [market_motion] Narrow the audience to one elder, one coordinator, and a small invited care circle
- [market_motion] Define reminder channels, retries, and visible failure states before pilot launch

### demand_validation
- [demand_validation] Run a 2+ week concierge pilot measuring actual migration of coordination items

### privacy_trust
- [privacy_trust] Lock one geography and minimum privacy/compliance requirements before inviting families

## Global Status

LIMITED


## Global Blocking Gaps

### privacy_trust
- [privacy_trust] Initial launch geography and its minimum privacy, retention, deletion, and consent rules are not yet fixed
- [privacy_trust] Reminder delivery, role permissions, and audit history need real-world validation with families
- [privacy_trust] Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized
- [privacy_trust] The permission model is not specific enough to safely enforce access boundaries for sensitive care data
- [privacy_trust] Launch geography and minimum compliance posture remain undefined

### demand_validation
- [demand_validation] Real switching behavior from chat/spreadsheets to CareSync is not yet proven
- [demand_validation] Switching behavior from chat/spreadsheets to CareSync is unproven and needs a measurable experiment

### market_motion
- [market_motion] The internal support/admin surface is not yet defined, but pilot operations require audited staff controls
- [market_motion] No single primary acquisition motion is defined yet
- [market_motion] The smallest credible launch audience is not yet narrowed enough for a focused pilot
- [market_motion] Reminder channel and failure handling are not specified tightly enough for trust-critical pilot use

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define one initial launch geography and attach the minimum privacy and deletion rules
- [privacy_trust] Choose one initial launch geography and document the minimum privacy/compliance requirements
- [privacy_trust] Define the exact role-to-resource permission matrix for coordinator, family member, and caregiver
- [privacy_trust] Lock one geography and minimum privacy/compliance requirements before inviting families

### demand_validation
- [demand_validation] Validate coordination migration with concierge pilots using real families
- [demand_validation] Run a 2+ week concierge pilot measuring actual migration of coordination items

### market_motion
- [market_motion] Test reminder delivery, permissions, audit history, and visible failure handling with pilot users
- [market_motion] Specify the minimum internal admin actions and audit rules needed for pilot support
- [market_motion] Choose one founder-led acquisition motion and a clear launch threshold for the pilot
- [market_motion] Narrow the audience to one elder, one coordinator, and a small invited care circle
- [market_motion] Define reminder channels, retries, and visible failure states before pilot launch

## Known Tags

- untagged
- demand_validation
- market_motion
- scope
- privacy_trust
- data_access


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

#### Tech Task

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Privacy and compliance requirements are not yet scoped to a specific launch geography Reminder reliability, role permissions, and audit history are trust-critical but not yet validated in real use Define one initial launch geography and minimum compliance requirements Test reminder delivery, permissions, and audit history with real families and caregivers Launch geography and baseline privacy/compliance requirements are undefined, which blocks final control design. Permission model is not specific enough to safely implement access boundaries for sensitive care data. Reminder delivery assumptions and fallback behavior are not defined, which makes reliability unproven. Lock the MVP to one region and define the minimum retention, deletion, and consent requirements. Specify exact role-based permissions for coordinator, family member, and caregiver. Define reminder channels, retry policy, and failure handling before implementation. No defined launch geography or compliance boundary for sensitive care data Trust-critical reminder and access behaviors are not yet validated in real family use Choose one initial geography and define the minimum privacy/compliance requirements for launch Test reminders, permissions, and audit history with real families and caregivers before public release


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


## Contributors

- growth


#### Growth Task

## Task

Replace the broad demand concern with one concrete validation experiment and a clear signal.


## Source Gap

[demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace Validate switching behavior with concierge pilots Unproven switch from chat-first coordination to a dedicated shared workspace Run concierge pilots that measure whether families actually replace part of their current coordination stack


## Expected Output

One demand experiment with an explicit audience, validation signal, and trust message.


## Contributors

_Aucun contributeur._


### Loop 2

#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Support recovery and delivery monitoring need an operational control surface for pilot use Operate an internal admin/support console during the pilot Reminder delivery channel and failure handling are undefined, so core workflow reliability is not yet implementable with confidence. Define the exact reminder channels, retry policy, and failure state handling. Pilot geography and minimum compliance posture are not yet defined Define one launch geography and the minimum privacy/compliance requirements before inviting pilot families Test reminder delivery, permissions, and audit history with real coordinators, family members, and caregivers in the pilot


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

- tech


#### Tech Task

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Initial launch geography and minimum compliance requirements are not yet fixed Reminder delivery, role permissions, and audit history are trust-critical and need real-world validation Define one initial launch geography and minimum compliance requirements Test reminder delivery, permissions, and audit history with real families and caregivers Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized. The permission model is not specific enough to safely enforce access boundaries for sensitive care data. Choose one initial launch geography and document the minimum privacy/compliance requirements.


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Replace the broad demand concern with one concrete validation experiment and a clear signal.


## Source Gap

[demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace Validate switching behavior with concierge pilots Unproven switch from chat-first coordination to a dedicated shared workspace Reminder reliability and access control are trust-critical but not yet validated in real family use Run a concierge pilot that measures actual migration of coordination items from chat/spreadsheets into CareSync and repeat use over 2+ weeks


## Expected Output

One demand experiment with an explicit audience, validation signal, and trust message.


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

### demand_validation
- [demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace
- [demand_validation] Unproven switch from chat-first coordination to a dedicated shared workspace

### privacy_trust
- [privacy_trust] Privacy and compliance requirements are not yet scoped to a specific launch geography
- [privacy_trust] Reminder reliability, role permissions, and audit history are trust-critical but not yet validated in real use
- [privacy_trust] Launch geography and baseline privacy/compliance requirements are undefined, which blocks final control design.
- [privacy_trust] Permission model is not specific enough to safely implement access boundaries for sensitive care data.
- [privacy_trust] Reminder delivery assumptions and fallback behavior are not defined, which makes reliability unproven.
- [privacy_trust] No defined launch geography or compliance boundary for sensitive care data
- [privacy_trust] Trust-critical reminder and access behaviors are not yet validated in real family use

## Global Required Improvements

### demand_validation
- [demand_validation] Validate switching behavior with concierge pilots
- [demand_validation] Run concierge pilots that measure whether families actually replace part of their current coordination stack

### privacy_trust
- [privacy_trust] Define one initial launch geography and minimum compliance requirements
- [privacy_trust] Test reminder delivery, permissions, and audit history with real families and caregivers
- [privacy_trust] Lock the MVP to one region and define the minimum retention, deletion, and consent requirements.
- [privacy_trust] Specify exact role-based permissions for coordinator, family member, and caregiver.
- [privacy_trust] Define reminder channels, retry policy, and failure handling before implementation.
- [privacy_trust] Choose one initial geography and define the minimum privacy/compliance requirements for launch
- [privacy_trust] Test reminders, permissions, and audit history with real families and caregivers before public release

## Loop Tasks

##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Privacy and compliance requirements are not yet scoped to a specific launch geography Reminder reliability, role permissions, and audit history are trust-critical but not yet validated in real use Define one initial launch geography and minimum compliance requirements Test reminder delivery, permissions, and audit history with real families and caregivers Launch geography and baseline privacy/compliance requirements are undefined, which blocks final control design. Permission model is not specific enough to safely implement access boundaries for sensitive care data. Reminder delivery assumptions and fallback behavior are not defined, which makes reliability unproven. Lock the MVP to one region and define the minimum retention, deletion, and consent requirements. Specify exact role-based permissions for coordinator, family member, and caregiver. Define reminder channels, retry policy, and failure handling before implementation. No defined launch geography or compliance boundary for sensitive care data Trust-critical reminder and access behaviors are not yet validated in real family use Choose one initial geography and define the minimum privacy/compliance requirements for launch Test reminders, permissions, and audit history with real families and caregivers before public release


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


##### Growth

## Task

Replace the broad demand concern with one concrete validation experiment and a clear signal.


## Source Gap

[demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace Validate switching behavior with concierge pilots Unproven switch from chat-first coordination to a dedicated shared workspace Run concierge pilots that measure whether families actually replace part of their current coordination stack


## Expected Output

One demand experiment with an explicit audience, validation signal, and trust message.


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

### demand_validation
- [demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace
- [demand_validation] Unproven switch from chat-first coordination to a dedicated shared workspace
- [demand_validation] Reminder reliability and access control are trust-critical but not yet validated in real family use

### privacy_trust
- [privacy_trust] Initial launch geography and minimum compliance requirements are not yet fixed
- [privacy_trust] Reminder delivery, role permissions, and audit history are trust-critical and need real-world validation
- [privacy_trust] Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized.
- [privacy_trust] The permission model is not specific enough to safely enforce access boundaries for sensitive care data.

### market_motion
- [market_motion] Support recovery and delivery monitoring need an operational control surface for pilot use
- [market_motion] Reminder delivery channel and failure handling are undefined, so core workflow reliability is not yet implementable with confidence.
- [market_motion] Pilot geography and minimum compliance posture are not yet defined

## Global Required Improvements

### demand_validation
- [demand_validation] Validate switching behavior with concierge pilots
- [demand_validation] Run a concierge pilot that measures actual migration of coordination items from chat/spreadsheets into CareSync and repeat use over 2+ weeks

### privacy_trust
- [privacy_trust] Define one initial launch geography and minimum compliance requirements
- [privacy_trust] Test reminder delivery, permissions, and audit history with real families and caregivers
- [privacy_trust] Choose one initial launch geography and document the minimum privacy/compliance requirements.

### market_motion
- [market_motion] Operate an internal admin/support console during the pilot
- [market_motion] Define the exact reminder channels, retry policy, and failure state handling.
- [market_motion] Define one launch geography and the minimum privacy/compliance requirements before inviting pilot families
- [market_motion] Test reminder delivery, permissions, and audit history with real coordinators, family members, and caregivers in the pilot

### data_access
- [data_access] Finalize the role-based access matrix for coordinator, family member, and caregiver.
- [data_access] Add an internal admin/support console for access recovery, delivery monitoring, and controlled deletion.

## Loop Tasks

##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Privacy and compliance requirements are not yet scoped to a specific launch geography Reminder reliability, role permissions, and audit history are trust-critical but not yet validated in real use Define one initial launch geography and minimum compliance requirements Test reminder delivery, permissions, and audit history with real families and caregivers Launch geography and baseline privacy/compliance requirements are undefined, which blocks final control design. Permission model is not specific enough to safely implement access boundaries for sensitive care data. Reminder delivery assumptions and fallback behavior are not defined, which makes reliability unproven. Lock the MVP to one region and define the minimum retention, deletion, and consent requirements. Specify exact role-based permissions for coordinator, family member, and caregiver. Define reminder channels, retry policy, and failure handling before implementation. No defined launch geography or compliance boundary for sensitive care data Trust-critical reminder and access behaviors are not yet validated in real family use Choose one initial geography and define the minimum privacy/compliance requirements for launch Test reminders, permissions, and audit history with real families and caregivers before public release


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


##### Growth

## Task

Replace the broad demand concern with one concrete validation experiment and a clear signal.


## Source Gap

[demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace Validate switching behavior with concierge pilots Unproven switch from chat-first coordination to a dedicated shared workspace Run concierge pilots that measure whether families actually replace part of their current coordination stack


## Expected Output

One demand experiment with an explicit audience, validation signal, and trust message.


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

### demand_validation
- [demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace
- [demand_validation] Unproven switch from chat-first coordination to a dedicated shared workspace
- [demand_validation] Reminder reliability and access control are trust-critical but not yet validated in real family use

### privacy_trust
- [privacy_trust] Initial launch geography and minimum compliance requirements are not yet fixed
- [privacy_trust] Reminder delivery, role permissions, and audit history are trust-critical and need real-world validation
- [privacy_trust] Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized.
- [privacy_trust] The permission model is not specific enough to safely enforce access boundaries for sensitive care data.

### market_motion
- [market_motion] Support recovery and delivery monitoring need an operational control surface for pilot use
- [market_motion] Reminder delivery channel and failure handling are undefined, so core workflow reliability is not yet implementable with confidence.
- [market_motion] Pilot geography and minimum compliance posture are not yet defined

## Global Required Improvements

### demand_validation
- [demand_validation] Validate switching behavior with concierge pilots
- [demand_validation] Run a concierge pilot that measures actual migration of coordination items from chat/spreadsheets into CareSync and repeat use over 2+ weeks

### privacy_trust
- [privacy_trust] Define one initial launch geography and minimum compliance requirements
- [privacy_trust] Test reminder delivery, permissions, and audit history with real families and caregivers
- [privacy_trust] Choose one initial launch geography and document the minimum privacy/compliance requirements.

### market_motion
- [market_motion] Operate an internal admin/support console during the pilot
- [market_motion] Define the exact reminder channels, retry policy, and failure state handling.
- [market_motion] Define one launch geography and the minimum privacy/compliance requirements before inviting pilot families
- [market_motion] Test reminder delivery, permissions, and audit history with real coordinators, family members, and caregivers in the pilot

### data_access
- [data_access] Finalize the role-based access matrix for coordinator, family member, and caregiver.
- [data_access] Add an internal admin/support console for access recovery, delivery monitoring, and controlled deletion.

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Support recovery and delivery monitoring need an operational control surface for pilot use Operate an internal admin/support console during the pilot Reminder delivery channel and failure handling are undefined, so core workflow reliability is not yet implementable with confidence. Define the exact reminder channels, retry policy, and failure state handling. Pilot geography and minimum compliance posture are not yet defined Define one launch geography and the minimum privacy/compliance requirements before inviting pilot families Test reminder delivery, permissions, and audit history with real coordinators, family members, and caregivers in the pilot


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Initial launch geography and minimum compliance requirements are not yet fixed Reminder delivery, role permissions, and audit history are trust-critical and need real-world validation Define one initial launch geography and minimum compliance requirements Test reminder delivery, permissions, and audit history with real families and caregivers Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized. The permission model is not specific enough to safely enforce access boundaries for sensitive care data. Choose one initial launch geography and document the minimum privacy/compliance requirements.


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


##### Growth

## Task

Replace the broad demand concern with one concrete validation experiment and a clear signal.


## Source Gap

[demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace Validate switching behavior with concierge pilots Unproven switch from chat-first coordination to a dedicated shared workspace Reminder reliability and access control are trust-critical but not yet validated in real family use Run a concierge pilot that measures actual migration of coordination items from chat/spreadsheets into CareSync and repeat use over 2+ weeks


## Expected Output

One demand experiment with an explicit audience, validation signal, and trust message.


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
- [privacy_trust] Initial launch geography and its minimum privacy, retention, deletion, and consent rules are not yet fixed
- [privacy_trust] Reminder delivery, role permissions, and audit history need real-world validation with families
- [privacy_trust] Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized
- [privacy_trust] The permission model is not specific enough to safely enforce access boundaries for sensitive care data
- [privacy_trust] Launch geography and minimum compliance posture remain undefined

### demand_validation
- [demand_validation] Real switching behavior from chat/spreadsheets to CareSync is not yet proven
- [demand_validation] Switching behavior from chat/spreadsheets to CareSync is unproven and needs a measurable experiment

### market_motion
- [market_motion] The internal support/admin surface is not yet defined, but pilot operations require audited staff controls
- [market_motion] No single primary acquisition motion is defined yet
- [market_motion] The smallest credible launch audience is not yet narrowed enough for a focused pilot
- [market_motion] Reminder channel and failure handling are not specified tightly enough for trust-critical pilot use

## Global Required Improvements

### privacy_trust
- [privacy_trust] Define one initial launch geography and attach the minimum privacy and deletion rules
- [privacy_trust] Choose one initial launch geography and document the minimum privacy/compliance requirements
- [privacy_trust] Define the exact role-to-resource permission matrix for coordinator, family member, and caregiver
- [privacy_trust] Lock one geography and minimum privacy/compliance requirements before inviting families

### demand_validation
- [demand_validation] Validate coordination migration with concierge pilots using real families
- [demand_validation] Run a 2+ week concierge pilot measuring actual migration of coordination items

### market_motion
- [market_motion] Test reminder delivery, permissions, audit history, and visible failure handling with pilot users
- [market_motion] Specify the minimum internal admin actions and audit rules needed for pilot support
- [market_motion] Choose one founder-led acquisition motion and a clear launch threshold for the pilot
- [market_motion] Narrow the audience to one elder, one coordinator, and a small invited care circle
- [market_motion] Define reminder channels, retries, and visible failure states before pilot launch

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Support recovery and delivery monitoring need an operational control surface for pilot use Operate an internal admin/support console during the pilot Reminder delivery channel and failure handling are undefined, so core workflow reliability is not yet implementable with confidence. Define the exact reminder channels, retry policy, and failure state handling. Pilot geography and minimum compliance posture are not yet defined Define one launch geography and the minimum privacy/compliance requirements before inviting pilot families Test reminder delivery, permissions, and audit history with real coordinators, family members, and caregivers in the pilot


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Initial launch geography and minimum compliance requirements are not yet fixed Reminder delivery, role permissions, and audit history are trust-critical and need real-world validation Define one initial launch geography and minimum compliance requirements Test reminder delivery, permissions, and audit history with real families and caregivers Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized. The permission model is not specific enough to safely enforce access boundaries for sensitive care data. Choose one initial launch geography and document the minimum privacy/compliance requirements.


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


##### Growth

## Task

Replace the broad demand concern with one concrete validation experiment and a clear signal.


## Source Gap

[demand_validation] Unclear whether families will switch from chat-based coordination to a dedicated workspace Validate switching behavior with concierge pilots Unproven switch from chat-first coordination to a dedicated shared workspace Reminder reliability and access control are trust-critical but not yet validated in real family use Run a concierge pilot that measures actual migration of coordination items from chat/spreadsheets into CareSync and repeat use over 2+ weeks


## Expected Output

One demand experiment with an explicit audience, validation signal, and trust message.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Define the initial launch geography and attach the minimum privacy, retention, consent, and deletion rules to it [privacy_trust]
- [tech] Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]

## Growth Structural Decisions

### growth
- [growth] Define **one primary acquisition motion** explicitly: founder-led concierge outreach/referrals to coordinator-led family pilots. [market_motion]
- [growth] Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]

## Product Locking

## Applied

True


## Confirmed In Scope

- One care space per relative
- Fixed coordinator, family member, and caregiver roles
- Server-side access enforcement
- Explicit consent and policy acceptance for one launch geography
- Shared task list, appointment tracking, medication reminders, notes/timeline, document upload
- Reminder delivery with visible failure states
- Basic audit history
- Delete/archive behavior for care spaces and documents
- Restricted internal support/admin console
- Minimum privacy and compliance controls for one launch geography


## Confirmed Deferred

- Native caregiver agency workflows
- EHR / pharmacy integrations
- In-app messaging
- Advanced permissions matrix
- Multi-language support
- Mobile-first optimization for elderly users
- Billing, subscriptions, and payments
- AI summaries and recommendations
- Broad self-serve acquisition
- Expanded archive management


## Confirmed Out Of Scope

- Full telehealth or clinical decision support
- Emergency response workflows
- Direct integration with hospitals, pharmacies, or EHR systems
- Advanced AI care planning
- Broad home healthcare marketplace
- Insurance, billing, or payments
- Complex multi-patient agency operations
- Elderly-user-first UX optimization
- In-app chat as a replacement for messaging apps
- Multi-language support in MVP
- Advanced permissions beyond the fixed role model
- Long-term archive management beyond MVP needs
- Full global compliance coverage for every country
- Self-serve launch at broad scale
- Native caregiver agency workflows
- Premium tiers or expanded pricing mechanics


## Locking Note

Scope remains deliberately narrow: one coordinator, one older relative, a small care circle, and a shared coordination record. Anything not needed to prove migration from chat, trust, or core usability stays deferred.


## Expert Contributions

### Tech Summary

The main feasibility issue is not feature scope but trust boundary definition: CareSync needs one fixed launch geography and a strict server-enforced privacy model before any pilot can be considered safe. The right direction is a narrow, operationally supported MVP with explicit retention, deletion, and access-control rules rather than a broader product build.

## Tech Structural Decisions

- Define the initial launch geography and attach the minimum privacy, retention, consent, and deletion rules to it [privacy_trust]
- Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]


## Tech Recommendations

- Define the initial launch geography and attach the minimum privacy, retention, consent, and deletion rules to it [privacy_trust]
- Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]


## Tech Risks

- The selected geography may require stronger retention or deletion handling than the MVP can safely support [privacy_trust]
- Role-based access may be implemented inconsistently across resources if the backend model is not strictly enforced [data_access]
- Reminder delivery failures may erode trust if failure states and retries are not visible and operationally monitored [ops_tooling]


## Tech Open Questions

- Which single country or region is the initial launch geography?
- For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Is audit history retained after deletion, and if so, for how long?


### Growth Summary

The launch challenge is not feature breadth but **proof of real behavior change**: CareSync must get one family coordinator to move meaningful coordination activity out of chat and into a trusted shared workspace. The recommended direction is a **concierge-led pilot for a single elder care circle**, focused on reminders, ownership, and visible status rather than a broad platform launch.

## Growth Structural Decisions

- Define **one primary acquisition motion** explicitly: founder-led concierge outreach/referrals to coordinator-led family pilots. [market_motion]
- Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]


## Growth Recommendations

- Define **one primary acquisition motion** explicitly: founder-led concierge outreach/referrals to coordinator-led family pilots. [market_motion]
- Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]


## Growth Risks

- Families keep using WhatsApp and never shift enough behavior.
- The product becomes a passive document repository instead of a coordination tool.
- Trust concerns around sensitive information block invitations.


## Growth Open Questions

- Which exact launch geography will be used for the pilot?
- Which reminder channels are in scope first: SMS, email, push, or a combination?
- What is the minimum migration threshold that counts as real adoption?


## Product Arbitration

## Source

heuristic_fallback


## Retained

_Aucun élément retenu._


## Deferred

_Aucun élément différé._


## Rejected

- Tech: Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Tech: Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Tech: Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]
- Growth: Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Growth: Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]


## Open Points

- Tech: Define the initial launch geography and attach the minimum privacy, retention, consent, and deletion rules to it [privacy_trust]
- Tech: Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Growth: Define **one primary acquisition motion** explicitly: founder-led concierge outreach/referrals to coordinator-led family pilots. [market_motion]
- Growth: Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Growth: Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Tech: Which single country or region is the initial launch geography?
- Tech: For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Tech: Is audit history retained after deletion, and if so, for how long?
- Growth: Which exact launch geography will be used for the pilot?
- Growth: Which reminder channels are in scope first: SMS, email, push, or a combination?
- Growth: What is the minimum migration threshold that counts as real adoption?
- Tech recommendation needing arbitration: Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Tech recommendation needing arbitration: Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Tech recommendation needing arbitration: Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Tech recommendation needing arbitration: Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]
- Growth recommendation needing arbitration: Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Growth recommendation needing arbitration: Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Growth recommendation needing arbitration: Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]
- Tech open question: Which single country or region is the initial launch geography?
- Tech open question: For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Tech open question: Is audit history retained after deletion, and if so, for how long?
- Growth open question: Which exact launch geography will be used for the pilot?
- Growth open question: Which reminder channels are in scope first: SMS, email, push, or a combination?
- Growth open question: What is the minimum migration threshold that counts as real adoption?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care today rely on fragmented tools: phone calls, group chats, paper notes, calendars, and scattered documents. That creates missed appointments, duplicated effort, unclear responsibility, and stress, especially when siblings or paid caregivers are distributed across locations.

The core product problem is not “general elder care management.” It is:  
**How can a family quickly create a trusted, shared source of truth for care coordination without forcing every participant to learn a complex new system?**

## Initial Wedge
A **shared care coordination hub for one elderly relative and their close family/caregiver circle**.

The wedge is narrow:
- one care recipient
- 2–6 family members
- optional one professional caregiver
- one place to track appointments, tasks, and care notes

The MVP should prove that families will adopt a dedicated workspace if it clearly reduces coordination misses and ambiguity better than group chat plus calendar.

## First Target User
**Primary user:** an adult child who is the de facto care coordinator for an elderly parent.

This user:
- already manages appointments, medication reminders, and family updates
- feels the pain most acutely
- can invite others into the workflow
- is likely to pay if the product meaningfully reduces stress and coordination errors

Secondary participants in the first use case:
- siblings in other cities
- one professional caregiver or home nurse

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp / SMS group chats
- shared calendars
- handwritten notes or spreadsheets
- paper medication lists
- hospital portals and scattered PDFs
- agency-specific caregiver logs

Why they are used:
- zero learning curve
- already familiar
- easy to message in real time

Switching trigger:
- coordination is breaking down because information is fragmented across channels
- multiple people need the same current information
- missed appointments, duplicate tasks, or uncertainty about who did what
- the family wants a more reliable record than chat threads

CareSync must win on:
- clarity of responsibilities
- reliable reminders
- shared visibility
- reduced back-and-forth

## Core MVP Workflow
1. Primary user creates a care space for one relative.
2. Invites family members and, optionally, one caregiver.
3. Adds basic care items:
   - appointments
   - recurring tasks
   - medication reminders
   - important notes
4. Assigns responsibility to a person for each item.
5. Participants receive reminders and can mark tasks complete.
6. Care updates and key documents are visible in one shared timeline or feed.
7. The coordinator checks what is done, what is due next, and who is responsible.

The MVP must make coordination simpler than chat, not broader than it needs to be.

## In Scope
- One care space per elderly relative
- Family and caregiver invitations
- Shared task list with assignment and due dates
- Basic calendar view for appointments
- Medication reminder entries
- Simple update feed or timeline
- Document upload for a limited set of care documents
- Permission controls for invited participants
- Notifications/reminders for assigned items
- Basic auditability of who updated what

## Out of Scope
- Full telehealth or clinical decision support
- Emergency response workflows
- Direct integration with hospitals, pharmacies, or EHR systems
- Advanced AI care planning
- Broader home healthcare marketplace
- Insurance, billing, or payments
- Complex multi-patient agency operations
- Elderly-user-first UX optimization
- Real-time chat replacement
- Full legal/compliance product for every country
- Long-term archive management beyond MVP needs

## MVP Build Vs Pilot Operations
### Must Build Now
- Care space for one relative
- Invitations and role-based access
- Task assignment with reminders
- Basic appointment tracking
- Medication reminder entries
- Shared notes/timeline
- Document upload
- Change history for trust

### Manual Or Operational During Pilot
- Onboarding families directly
- Helping set up the first care space
- Defining what counts as a task vs note
- Supporting document organization
- Customer support for access issues
- Compliance review for pilot geography

### Deferred Until After Proof
- Native caregiver agency workflows
- EHR/pharmacy integrations
- Advanced permissions matrix
- Multi-language support
- Mobile-first optimization for elderly users
- In-app messaging
- Billing, subscriptions, and payments
- AI summaries and recommendations

## Business Model Hypothesis
Best initial model: **subscription paid by the family coordinator**.

Hypothesis:
- families will pay a modest monthly fee for reduced stress and fewer missed coordination steps
- pricing can later expand to caregiver agencies or premium family plans

Initial pricing direction:
- simple family subscription
- optional higher tier for more participants, document storage, or advanced sharing

## Critical Assumptions
- Families will adopt a dedicated tool instead of staying in chat
- The coordinator has enough pain to onboard others
- Shared visibility and reminders are valuable enough to change behavior
- Caregivers will participate if the workflow is simple
- Privacy and trust barriers can be addressed well enough for early adoption
- The product can be used without elderly users needing strong digital skills

## How To Test Quickly
- Run concierge pilots with 5–10 families coordinating one elder each
- Measure whether they replace at least part of their current chat/spreadsheet workflow
- Track missed appointments, forgotten tasks, and time spent coordinating before vs after
- Test whether families consistently assign tasks and check the shared record
- Validate willingness to pay after the pilot period
- Interview caregivers to see if they will actually use the shared workspace

## Acceptance Criteria
- A coordinator can create a care space in under 10 minutes
- At least 3 participants can be invited and given access successfully
- A family can add and assign an appointment, task, and medication reminder
- Reminders are delivered reliably to assigned participants
- Participants can mark items complete and see update history
- Documents can be uploaded and viewed by permitted users
- The coordinator can understand current status without needing a separate chat thread
- Pilot users report the tool is clearer than their current coordination method

## Risks And Failure Modes
- Families keep using WhatsApp and ignore the platform
- The product becomes too broad and loses simplicity
- Privacy concerns prevent adoption
- Caregivers do not consistently update the system
- Elderly users are assumed to be primary users when they are not
- Compliance requirements vary too much by region
- The product becomes a document vault instead of a coordination tool
- Reminder fatigue reduces usefulness

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Unclear whether families will switch from chat-based coordination to a dedicated workspace [switching_behavior]
- Privacy and compliance requirements are not yet scoped to a specific launch geography [compliance_scope]
- Reminder reliability and access control are trust-critical but not yet validated in real use [trust_controls]

Required Improvements:
- Validate switching behavior with concierge pilots [switching_behavior]
- Define one initial launch geography and minimum compliance requirements [compliance_scope]
- Test reminder delivery, permissions, and audit history with real families and caregivers [trust_controls]

## Recommendation
Proceed with a narrow concierge-style MVP focused on one family coordinating one elderly relative.

Do not launch as a broad elder-care platform.  
Do not start with agencies, marketplace features, or deep integrations.

The best path is to prove a single, reliable coordination workflow:
- invite participants
- assign responsibilities
- share current status
- deliver reminders
- maintain trust through permissions and history

If families do not meaningfully replace part of their current chat/spreadsheet process, the product should be revised before building beyond the wedge.

## Retained Decisions

_Aucune décision retenue._

## Deferred Decisions

_Aucune décision différée._

## Rejected Recommendations

- Tech: Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Tech: Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Tech: Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]
- Growth: Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Growth: Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]

## Unresolved Tensions

- Tech recommendation needing arbitration: Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Tech recommendation needing arbitration: Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Tech recommendation needing arbitration: Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Tech recommendation needing arbitration: Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]
- Growth recommendation needing arbitration: Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Growth recommendation needing arbitration: Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Growth recommendation needing arbitration: Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]
- Tech open question: Which single country or region is the initial launch geography?
- Tech open question: For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Tech open question: Is audit history retained after deletion, and if so, for how long?
- Growth open question: Which exact launch geography will be used for the pilot?
- Growth open question: Which reminder channels are in scope first: SMS, email, push, or a combination?
- Growth open question: What is the minimum migration threshold that counts as real adoption?

## Applied Changes

_Aucun changement appliqué._

## Remaining Open Points

- Tech: Define the initial launch geography and attach the minimum privacy, retention, consent, and deletion rules to it [privacy_trust]
- Tech: Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Growth: Define **one primary acquisition motion** explicitly: founder-led concierge outreach/referrals to coordinator-led family pilots. [market_motion]
- Growth: Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Growth: Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Tech: Which single country or region is the initial launch geography?
- Tech: For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Tech: Is audit history retained after deletion, and if so, for how long?
- Growth: Which exact launch geography will be used for the pilot?
- Growth: Which reminder channels are in scope first: SMS, email, push, or a combination?
- Growth: What is the minimum migration threshold that counts as real adoption?
- Tech recommendation needing arbitration: Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Tech recommendation needing arbitration: Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Tech recommendation needing arbitration: Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Tech recommendation needing arbitration: Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]
- Growth recommendation needing arbitration: Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Growth recommendation needing arbitration: Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Growth recommendation needing arbitration: Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Growth recommendation needing arbitration: Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]
- Tech open question: Which single country or region is the initial launch geography?
- Tech open question: For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Tech open question: Is audit history retained after deletion, and if so, for how long?
- Growth open question: Which exact launch geography will be used for the pilot?
- Growth open question: Which reminder channels are in scope first: SMS, email, push, or a combination?
- Growth open question: What is the minimum migration threshold that counts as real adoption?

## Risks

- Families may continue using chat as the source of truth and ignore the workspace. [demand_validation]
- Access control mistakes could expose sensitive care information. [privacy_trust]
- Reminder delivery failures could undermine trust quickly. [privacy_trust]
- Families continue using WhatsApp/SMS and treat this as a duplicate admin burden.
- The product is perceived as a document vault instead of an active coordination tool.
- Caregivers do not update the system consistently, weakening trust.
- A vague compliance boundary leads to underbuilt trust controls or expensive rework. [privacy_trust]
- Reminder delivery failures undermine confidence in the core product promise. [reliability]
- Permission mistakes could expose sensitive family or medical information. [access_control]
- Families keep using WhatsApp and treat CareSync as extra work. [demand_validation]
- The product becomes too broad and loses the clarity needed for first adoption. [scope]
- Privacy fears prevent families from uploading documents or adding caregivers. [privacy_trust]
- The selected geography may require stronger retention or deletion handling than the MVP can safely support [privacy_trust]
- Role-based access may be implemented inconsistently across resources if the backend model is not strictly enforced [data_access]
- Reminder delivery failures may erode trust if failure states and retries are not visible and operationally monitored [ops_tooling]
- Families keep using WhatsApp and never shift enough behavior.
- The product becomes a passive document repository instead of a coordination tool.
- Trust concerns around sensitive information block invitations.

## Open Questions

- Which single country or region is the initial launch boundary?
- Which reminder channels are mandatory for MVP: email, SMS, push, or a combination?
- Should caregivers have edit rights for all items or only for assigned items?
- What exact user segment has the strongest pain and highest willingness to try a new system?
- Which country or region can serve as the safest initial launch geography?
- What minimum reminder reliability is required before users will trust it for medication or appointments?
- Which country or region is the initial launch geography?
- What minimum consent and retention rules apply in that geography for caregiver and family access?
- Which reminder channels are allowed and reliable enough for the pilot?
- What exact behavior change counts as “switching” for the pilot?
- Which launch geography is compliant enough to support the first pilot?
- Which family coordinator segment is most likely to feel urgent pain now?
- Which single country or region is the initial launch geography?
- For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Is audit history retained after deletion, and if so, for how long?
- Which exact launch geography will be used for the pilot?
- Which reminder channels are in scope first: SMS, email, push, or a combination?
- What is the minimum migration threshold that counts as real adoption?

## Final Revised PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care use fragmented tools: chat threads, phone calls, paper notes, shared calendars, and scattered documents. That creates missed appointments, duplicated effort, unclear ownership, and stress.

The core problem is not general elder-care management. It is:

**How can one family maintain a trusted shared source of truth for one older relative’s care coordination without forcing everyone to learn a complex system?**

## Initial Wedge
A **single shared care coordination workspace for one elderly relative and their close care circle**.

This wedge is intentionally narrow:
- one care recipient
- one primary coordinator
- 2–4 family participants
- optionally one professional caregiver
- appointments, responsibilities, reminders, notes, and a small set of key documents in one place

The MVP must prove that families will move meaningful coordination activity out of chat and into a dedicated workspace when it clearly reduces misses and ambiguity.

## First Target User
**Primary user:** an adult child who is the de facto coordinator for an elderly parent.

Why this user:
- already manages appointments, reminders, and family updates
- feels the coordination pain most acutely
- can invite others into the workflow
- is the most likely first buyer

Secondary participants:
- siblings in other cities
- one caregiver or home nurse

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp / SMS group chats
- shared calendars
- handwritten notes or spreadsheets
- paper medication lists
- hospital portals and scattered PDFs
- agency caregiver logs

Why these are used:
- zero learning curve
- familiar
- immediate messaging

Switching trigger:
- coordination is breaking down because information is fragmented across channels
- multiple people need the same current information
- missed appointments, duplicated tasks, or uncertainty about responsibility
- the family wants a more reliable record than chat threads

CareSync must win on:
- clear ownership
- reliable reminders
- shared visibility
- reduced back-and-forth
- trust and access control for sensitive information

## Core MVP Workflow
1. Primary user creates a care space for one relative.
2. Invites family members and optionally one caregiver.
3. Accepts required consent and privacy terms for the launch geography.
4. Sets fixed roles and permissions.
5. Adds appointments, recurring tasks, medication reminders, and important notes.
6. Assigns responsibility to a person for each item.
7. Participants receive reminders and can mark items complete.
8. Participants can view a shared timeline of updates and permitted documents.
9. The coordinator checks what is due, what is complete, and who is responsible without relying on a separate chat thread.

## In Scope
- One care space per elderly relative
- Founder-led onboarding for pilot users
- Invitations and fixed role-based access
- Coordinator, family member, caregiver roles only
- Server-enforced access rules for each role
- Explicit consent and policy acceptance for the launch geography
- Shared task list with assignment and due dates
- Basic calendar view for appointments
- Medication reminder entries
- Shared notes / timeline feed
- Document upload for a limited set of care documents
- Notifications / reminders for assigned items
- Visible reminder failure states
- Basic audit history of updates and completion
- Delete / archive behavior for care spaces and uploaded documents
- Minimum privacy, retention, and deletion controls for one initial launch geography
- Restricted internal support/admin tooling with audited staff actions

## Out of Scope
- Full telehealth or clinical decision support
- Emergency response workflows
- Direct integration with hospitals, pharmacies, or EHR systems
- Advanced AI care planning
- Broad home healthcare marketplace
- Insurance, billing, or payments
- Complex multi-patient agency operations
- Elderly-user-first UX optimization
- In-app chat as a replacement for messaging apps
- Multi-language support in MVP
- Advanced permissions beyond the fixed role model
- Long-term archive management beyond MVP needs
- Full global compliance coverage for every country
- Self-serve launch at broad scale
- Native caregiver agency workflows
- Premium tiers or expanded pricing mechanics

## MVP Build Vs Pilot Operations
### Must Build Now
- One care space per relative
- Invitations and role-based access
- Fixed coordinator / family member / caregiver roles
- Server-side access enforcement
- Explicit consent and policy acceptance
- Task assignment with reminders
- Basic appointment tracking
- Medication reminder entries
- Shared notes / timeline
- Document upload
- Change history / audit log
- Delete / archive care space and documents
- Reminder delivery with visible failure states
- Restricted internal support/admin console
- Minimum privacy and compliance controls for one launch geography

### Manual Or Operational During Pilot
- Founder-led onboarding for first families
- Helping set up the first care space
- Defining what counts as a task vs note
- Supporting document organization
- Customer support for access issues
- Compliance review for pilot geography
- Monitoring reminder delivery failures
- Directly collecting feedback on switching behavior
- Tracking whether real coordination moves from chat/spreadsheets into CareSync

### Deferred Until After Proof
- Native caregiver agency workflows
- EHR / pharmacy integrations
- In-app messaging
- Advanced permissions matrix
- Multi-language support
- Mobile-first optimization for elderly users
- Billing, subscriptions, and payments
- AI summaries and recommendations
- Broad self-serve acquisition
- Expanded archive management

## Business Model Hypothesis
Best initial model: **subscription paid by the family coordinator**.

Hypothesis:
- families will pay a modest monthly fee for reduced stress and fewer missed coordination steps
- pricing can later expand to caregiver agencies or premium family plans

Initial pricing direction:
- simple family subscription
- no pricing complexity in the MVP

## Critical Assumptions
- Families will adopt a dedicated tool instead of staying in chat
- The coordinator has enough pain to onboard others
- Shared visibility and reminders are valuable enough to change behavior
- Caregivers will participate if the workflow is simple
- Privacy, permissions, consent, and deletion behavior are strong enough to earn trust
- The product can be used without elderly users needing strong digital skills
- One launch geography can support a compliant pilot with minimal scope
- Reminder delivery is reliable enough to be trusted for basic coordination
- Internal support tooling is enough to manage pilot access and recovery safely

## How To Test Quickly
- Run concierge pilots with 5–10 families coordinating one elder each
- Measure whether they move real coordination items from chat / spreadsheets into CareSync
- Track weekly repeat use over at least 2 weeks
- Track missed appointments, forgotten tasks, and time spent coordinating before vs after
- Test whether families consistently assign tasks and check the shared record
- Confirm invited participant acceptance rate
- Interview coordinators on whether they would be disappointed if the product were removed
- Validate willingness to pay after the pilot period
- Test reminder delivery, permissions, audit history, consent, deletion behavior, and staff recovery workflows with real families in the launch geography

## Acceptance Criteria
- A coordinator can create a care space in under 10 minutes
- At least 3 participants can be invited and given access successfully
- Fixed roles are understandable and enforced correctly
- Required consent and policy acceptance are completed before use
- A family can add and assign an appointment, task, and medication reminder
- Reminders are delivered reliably or fail visibly with fallback handling
- Participants can mark items complete and see update history
- Documents can be uploaded and viewed by permitted users
- The coordinator can understand current status without needing a separate chat thread
- Users can delete or archive a care space and documents according to the chosen geography rules
- Pilot users report the tool is clearer than their current coordination method
- The pilot shows repeated weekly use from the same family group
- Pilot usage demonstrates meaningful migration of coordination activity from chat/spreadsheets into CareSync

## Risks And Failure Modes
- Families keep using WhatsApp and ignore the platform
- The product becomes too broad and loses simplicity
- Privacy concerns prevent adoption
- Caregivers do not consistently update the system
- Elderly users are assumed to be primary users when they are not
- Compliance requirements vary too much by region
- Reminder delivery is not trusted enough for appointments or medication
- The product becomes a document vault instead of a coordination tool
- Reminder fatigue reduces usefulness
- Permission confusion undermines trust
- Support burden is too high without internal admin tooling
- Launch geography rules are under-specified and block safe pilot use

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Initial launch geography and its minimum privacy, retention, deletion, and consent rules are not yet fixed [privacy_trust]
- Real switching behavior from chat/spreadsheets to CareSync is not yet proven [demand_validation]
- Reminder delivery, role permissions, and audit history need real-world validation with families [trust_controls]

Required Improvements:
- Define one initial launch geography and attach the minimum privacy and deletion rules [privacy_trust]
- Validate coordination migration with concierge pilots using real families [demand_validation]
- Test reminder delivery, permissions, audit history, and visible failure handling with pilot users [trust_controls]

## Recommendation
Proceed with a narrow concierge-style MVP focused on one family coordinating one elderly relative.

Do not launch as a broad elder-care platform.  
Do not start with agencies, marketplace features, in-app chat, or deep integrations.

The best path is to prove one reliable coordination workflow:
- invite participants
- assign responsibilities
- share current status
- deliver reminders
- maintain trust through permissions, consent, audit history, deletion controls, and operational support

If families do not meaningfully replace part of their current chat / spreadsheet process, revise before building beyond the wedge.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

_Aucune décision._

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
