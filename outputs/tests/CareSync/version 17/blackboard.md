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

### metrics_validation
- [metrics_validation] Proof that families will switch part of their coordination workflow
- [metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates

### privacy_trust
- [privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing

## Product Required Improvements

### market_motion
- [market_motion] Run a small concierge pilot before expanding scope

### privacy_trust
- [privacy_trust] Validate the fixed permission matrix and access controls with real families

### metrics_validation
- [metrics_validation] Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot

## Tech Status

LIMITED


## Tech Blocking Gaps

### privacy_trust
- [privacy_trust] No concrete role-by-role access policy for sensitive objects
- [privacy_trust] No defined trust gate before first sharing of documents or private updates
- [privacy_trust] No confirmed support workflow for permission disputes or revocation
- [privacy_trust] Reminder delivery requirements are not specified tightly enough for pilot trust

## Tech Required Improvements

### privacy_trust
- [privacy_trust] Define and implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts
- [privacy_trust] Add an explicit access review and consent step at care-space activation

### data_access
- [data_access] Build immediate revocation plus internal support tooling for access disputes and recovery

### metrics_validation
- [metrics_validation] Specify delivery-status visibility and retry rules for reminders

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] No explicit primary acquisition motion tied to a defined launch audience.
- [market_motion] Reminder channels and failure handling are not specified for pilot reliability.

### metrics_validation
- [metrics_validation] The smallest credible activation threshold is not yet precise enough to judge whether the pilot is working.

## Growth Required Improvements

### market_motion
- [market_motion] Define founder-led outbound as the first acquisition motion and limit it to remote adult children coordinating one parent.

### untagged
- Specify the reminder delivery path and what users see when delivery fails.

### metrics_validation
- [metrics_validation] Set a concrete launch threshold for first activation and weekly participation in the pilot.

## Global Status

LIMITED


## Global Blocking Gaps

### metrics_validation
- [metrics_validation] Proof that families will switch part of their coordination workflow
- [metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates
- [metrics_validation] The smallest credible activation threshold is not yet precise enough to judge whether the pilot is working.

### privacy_trust
- [privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing
- [privacy_trust] No concrete role-by-role access policy for sensitive objects
- [privacy_trust] No defined trust gate before first sharing of documents or private updates
- [privacy_trust] No confirmed support workflow for permission disputes or revocation
- [privacy_trust] Reminder delivery requirements are not specified tightly enough for pilot trust

### market_motion
- [market_motion] No explicit primary acquisition motion tied to a defined launch audience.
- [market_motion] Reminder channels and failure handling are not specified for pilot reliability.

## Global Required Improvements

### market_motion
- [market_motion] Run a small concierge pilot before expanding scope
- [market_motion] Define founder-led outbound as the first acquisition motion and limit it to remote adult children coordinating one parent.

### privacy_trust
- [privacy_trust] Validate the fixed permission matrix and access controls with real families
- [privacy_trust] Define and implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts
- [privacy_trust] Add an explicit access review and consent step at care-space activation

### metrics_validation
- [metrics_validation] Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot
- [metrics_validation] Specify delivery-status visibility and retry rules for reminders
- [metrics_validation] Set a concrete launch threshold for first activation and weekly participation in the pilot.

### data_access
- [data_access] Build immediate revocation plus internal support tooling for access disputes and recovery

### untagged
- Specify the reminder delivery path and what users see when delivery fails.

## Known Tags

- privacy_trust
- metrics_validation
- market_motion
- demand_validation
- data_access
- operations
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

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a small concierge pilot before expanding scope Notification reliability requirements are not specified by channel or retry behavior Specify the reminder delivery channels and failure handling required for pilot viability No evidence yet that families will abandon familiar chat-based coordination for a new shared system Run a concierge pilot with 5–10 targeted families managing one relative


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

- tech


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Proof that caregivers will reliably post structured updates Measure weekly retention and update posting in the pilot Measure whether at least one non-coordinator participant posts or updates weekly


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


#### Tech Task

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Confirmation that the minimum permission model is trusted for sensitive sharing Validate the minimum permission matrix and access controls Undefined permission matrix for sensitive sharing and editing Define role-by-role access rules for tasks, notes, documents, and emergency contacts No tested trust threshold for permissions and sensitive document handling Validate the smallest trustable permission model before public launch


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


## Contributors

- growth


### Loop 2

#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a small concierge pilot before expanding scope No explicit primary acquisition motion with a defined launch audience Specify reminder delivery channels and visible failure handling before pilot launch


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot Commit to founder-led concierge acquisition for 5–10 families, targeted at remote adult child coordinators managing one parent Define the minimum proof of access: 3 of 5 pilot families using the space weekly for 2 weeks


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


#### Tech Task

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing Validate the fixed permission matrix and access controls No concrete role-by-role access policy for sensitive objects No defined trust gate before first sharing of documents or private updates No confirmed support workflow for permission disputes or revocation Implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts Add an explicit access review and consent step at care-space activation Reminder delivery requirements are not specified tightly enough for pilot trust


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


## Contributors

- growth


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
- [demand_validation] Proof that families will switch part of their coordination workflow
- [demand_validation] No validated proof that caregivers will reliably post updates in the product

### metrics_validation
- [metrics_validation] Proof that caregivers will reliably post structured updates

### privacy_trust
- [privacy_trust] Confirmation that the minimum permission model is trusted for sensitive sharing
- [privacy_trust] Undefined permission matrix for sensitive sharing and editing
- [privacy_trust] No tested trust threshold for permissions and sensitive document handling

### data_access
- [data_access] No explicit audit and recovery model for access disputes or invite errors

### market_motion
- [market_motion] Notification reliability requirements are not specified by channel or retry behavior
- [market_motion] No evidence yet that families will abandon familiar chat-based coordination for a new shared system

## Global Required Improvements

### market_motion
- [market_motion] Run a small concierge pilot before expanding scope
- [market_motion] Specify the reminder delivery channels and failure handling required for pilot viability
- [market_motion] Run a concierge pilot with 5–10 targeted families managing one relative

### privacy_trust
- [privacy_trust] Validate the minimum permission matrix and access controls
- [privacy_trust] Define role-by-role access rules for tasks, notes, documents, and emergency contacts
- [privacy_trust] Validate the smallest trustable permission model before public launch

### metrics_validation
- [metrics_validation] Measure weekly retention and update posting in the pilot
- [metrics_validation] Measure whether at least one non-coordinator participant posts or updates weekly

### operations
- [operations] Add audit logging, invite expiry, and support recovery flows to the MVP scope

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a small concierge pilot before expanding scope Notification reliability requirements are not specified by channel or retry behavior Specify the reminder delivery channels and failure handling required for pilot viability No evidence yet that families will abandon familiar chat-based coordination for a new shared system Run a concierge pilot with 5–10 targeted families managing one relative


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Proof that caregivers will reliably post structured updates Measure weekly retention and update posting in the pilot Measure whether at least one non-coordinator participant posts or updates weekly


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Confirmation that the minimum permission model is trusted for sensitive sharing Validate the minimum permission matrix and access controls Undefined permission matrix for sensitive sharing and editing Define role-by-role access rules for tasks, notes, documents, and emergency contacts No tested trust threshold for permissions and sensitive document handling Validate the smallest trustable permission model before public launch


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


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
- [demand_validation] Proof that families will switch part of their coordination workflow
- [demand_validation] No launch threshold proving families will adopt the new shared workflow

### metrics_validation
- [metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates

### privacy_trust
- [privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing
- [privacy_trust] No concrete role-by-role access policy for sensitive objects
- [privacy_trust] No defined trust gate before first sharing of documents or private updates
- [privacy_trust] No confirmed support workflow for permission disputes or revocation
- [privacy_trust] Reminder delivery requirements are not specified tightly enough for pilot trust

### market_motion
- [market_motion] No explicit primary acquisition motion with a defined launch audience

## Global Required Improvements

### market_motion
- [market_motion] Run a small concierge pilot before expanding scope
- [market_motion] Specify reminder delivery channels and visible failure handling before pilot launch

### privacy_trust
- [privacy_trust] Validate the fixed permission matrix and access controls
- [privacy_trust] Implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts
- [privacy_trust] Add an explicit access review and consent step at care-space activation

### metrics_validation
- [metrics_validation] Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot
- [metrics_validation] Commit to founder-led concierge acquisition for 5–10 families, targeted at remote adult child coordinators managing one parent
- [metrics_validation] Define the minimum proof of access: 3 of 5 pilot families using the space weekly for 2 weeks

### data_access
- [data_access] Build audit-visible revocation and support tooling for access issues

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a small concierge pilot before expanding scope Notification reliability requirements are not specified by channel or retry behavior Specify the reminder delivery channels and failure handling required for pilot viability No evidence yet that families will abandon familiar chat-based coordination for a new shared system Run a concierge pilot with 5–10 targeted families managing one relative


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Proof that caregivers will reliably post structured updates Measure weekly retention and update posting in the pilot Measure whether at least one non-coordinator participant posts or updates weekly


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Confirmation that the minimum permission model is trusted for sensitive sharing Validate the minimum permission matrix and access controls Undefined permission matrix for sensitive sharing and editing Define role-by-role access rules for tasks, notes, documents, and emergency contacts No tested trust threshold for permissions and sensitive document handling Validate the smallest trustable permission model before public launch


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


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
- [demand_validation] Proof that families will switch part of their coordination workflow
- [demand_validation] No launch threshold proving families will adopt the new shared workflow

### metrics_validation
- [metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates

### privacy_trust
- [privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing
- [privacy_trust] No concrete role-by-role access policy for sensitive objects
- [privacy_trust] No defined trust gate before first sharing of documents or private updates
- [privacy_trust] No confirmed support workflow for permission disputes or revocation
- [privacy_trust] Reminder delivery requirements are not specified tightly enough for pilot trust

### market_motion
- [market_motion] No explicit primary acquisition motion with a defined launch audience

## Global Required Improvements

### market_motion
- [market_motion] Run a small concierge pilot before expanding scope
- [market_motion] Specify reminder delivery channels and visible failure handling before pilot launch

### privacy_trust
- [privacy_trust] Validate the fixed permission matrix and access controls
- [privacy_trust] Implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts
- [privacy_trust] Add an explicit access review and consent step at care-space activation

### metrics_validation
- [metrics_validation] Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot
- [metrics_validation] Commit to founder-led concierge acquisition for 5–10 families, targeted at remote adult child coordinators managing one parent
- [metrics_validation] Define the minimum proof of access: 3 of 5 pilot families using the space weekly for 2 weeks

### data_access
- [data_access] Build audit-visible revocation and support tooling for access issues

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a small concierge pilot before expanding scope No explicit primary acquisition motion with a defined launch audience Specify reminder delivery channels and visible failure handling before pilot launch


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot Commit to founder-led concierge acquisition for 5–10 families, targeted at remote adult child coordinators managing one parent Define the minimum proof of access: 3 of 5 pilot families using the space weekly for 2 weeks


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing Validate the fixed permission matrix and access controls No concrete role-by-role access policy for sensitive objects No defined trust gate before first sharing of documents or private updates No confirmed support workflow for permission disputes or revocation Implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts Add an explicit access review and consent step at care-space activation Reminder delivery requirements are not specified tightly enough for pilot trust


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


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

### metrics_validation
- [metrics_validation] Proof that families will switch part of their coordination workflow
- [metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates
- [metrics_validation] The smallest credible activation threshold is not yet precise enough to judge whether the pilot is working.

### privacy_trust
- [privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing
- [privacy_trust] No concrete role-by-role access policy for sensitive objects
- [privacy_trust] No defined trust gate before first sharing of documents or private updates
- [privacy_trust] No confirmed support workflow for permission disputes or revocation
- [privacy_trust] Reminder delivery requirements are not specified tightly enough for pilot trust

### market_motion
- [market_motion] No explicit primary acquisition motion tied to a defined launch audience.
- [market_motion] Reminder channels and failure handling are not specified for pilot reliability.

## Global Required Improvements

### market_motion
- [market_motion] Run a small concierge pilot before expanding scope
- [market_motion] Define founder-led outbound as the first acquisition motion and limit it to remote adult children coordinating one parent.

### privacy_trust
- [privacy_trust] Validate the fixed permission matrix and access controls with real families
- [privacy_trust] Define and implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts
- [privacy_trust] Add an explicit access review and consent step at care-space activation

### metrics_validation
- [metrics_validation] Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot
- [metrics_validation] Specify delivery-status visibility and retry rules for reminders
- [metrics_validation] Set a concrete launch threshold for first activation and weekly participation in the pilot.

### data_access
- [data_access] Build immediate revocation plus internal support tooling for access disputes and recovery

### untagged
- Specify the reminder delivery path and what users see when delivery fails.

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a small concierge pilot before expanding scope No explicit primary acquisition motion with a defined launch audience Specify reminder delivery channels and visible failure handling before pilot launch


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Proof that caregivers or other non-coordinators will reliably post structured updates Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot Commit to founder-led concierge acquisition for 5–10 families, targeted at remote adult child coordinators managing one parent Define the minimum proof of access: 3 of 5 pilot families using the space weekly for 2 weeks


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Tech

## Task

Define the minimum privacy and trust controls required before launch.


## Source Gap

[privacy_trust] Confirmation that the fixed permission model is trusted for sensitive sharing Validate the fixed permission matrix and access controls No concrete role-by-role access policy for sensitive objects No defined trust gate before first sharing of documents or private updates No confirmed support workflow for permission disputes or revocation Implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts Add an explicit access review and consent step at care-space activation Reminder delivery requirements are not specified tightly enough for pilot trust


## Expected Output

A concrete privacy and trust control that can be implemented in the next iteration.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Add an explicit **privacy/trust gate** before activation: show participants, roles, and exactly which object types they can access.
- [tech] Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.

## Growth Structural Decisions

### growth
- [growth] Add one explicit primary acquisition motion: founder-led outbound into a concierge pilot. [market_motion]
- [growth] Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]

## Product Locking

## Applied

True


## Confirmed In Scope

- One care space per elderly relative
- Invite-only access
- Fixed role-based permissions
- Privacy and trust gate
- Coordinator consent confirmation
- Shared calendar, tasks, reminders, structured updates
- Emergency contact list
- Limited secure document upload
- Audit log
- Immediate access revocation


## Confirmed Deferred

- Native chat
- Multi-recipient support
- Agency dashboards
- External integrations
- Billing and payments
- Advanced compliance tooling
- AI assistance
- Marketplace features
- Granular custom permissions
- Expanded document management


## Confirmed Out Of Scope

- Multi-recipient or household management
- Organization hierarchies for agencies
- Real-time chat or chat replacement
- AI recommendations or predictive alerts
- Complex clinical records management
- Direct integrations with hospitals, pharmacies, or EHR systems
- Billing, claims, or payments
- Marketplace or service booking
- Advanced analytics
- Broad compliance automation across countries
- Elder-facing self-service as a primary workflow
- Custom permission builder beyond the fixed MVP matrix
- Broad document library or open-ended file sharing


## Locking Note

- MVP scope remains narrow and unchanged; only proof-critical trust, access, and coordination primitives are included. - Access revocation is retained as proof-critical. - Document handling remains limited to critical files only.


## Expert Contributions

### Tech Summary

The key feasibility issue is not feature breadth but whether the product can safely expose sensitive care data with a fixed permission model that families trust. The right MVP is a single-care-space, server-enforced access-control system with explicit activation, auditability, and manual support for edge cases—not a flexible collaboration platform.

## Tech Structural Decisions

- Add an explicit **privacy/trust gate** before activation: show participants, roles, and exactly which object types they can access.
- Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.


## Tech Recommendations

- Add an explicit **privacy/trust gate** before activation: show participants, roles, and exactly which object types they can access.
- Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.
- Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.


## Tech Risks

- Families may still distrust shared document storage even with fixed permissions.
- A fixed role model may be too rigid for some real caregiving arrangements.
- Notification failures could undermine the core trust loop.


## Tech Open Questions

- Which exact document types are allowed in MVP, and which are blocked?
- Should caregivers be able to upload documents or only comment on task/event updates?
- What are the default permissions for emergency contacts: view-only or editable by coordinator only?


### Growth Summary

The main launch challenge is not feature completeness; it is whether one coordinator will consistently move part of an existing care workflow out of chat and into a new shared record. The recommended GTM direction is a founder-led concierge pilot aimed at remote adult children managing one elder, with a very narrow promise and a measured loop around invitations, reminders, and structured updates.

## Growth Structural Decisions

- Add one explicit primary acquisition motion: founder-led outbound into a concierge pilot. [market_motion]
- Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]


## Growth Recommendations

- Add one explicit primary acquisition motion: founder-led outbound into a concierge pilot. [market_motion]
- Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Specify reminder channels and visible failure handling before pilot launch. [operations]
- Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]


## Growth Risks

- Families keep using WhatsApp because it remains faster and socially embedded. [demand_validation]
- Caregivers do not consistently post updates. [metrics_validation]
- Privacy concerns reduce willingness to invite others. [privacy_trust]


## Growth Open Questions

- Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- What exact family pain signals best predict conversion to pilot? [demand_validation]


## Product Arbitration

## Source

heuristic_fallback


## Retained

- Tech: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.


## Deferred

- Tech: Add an explicit **privacy/trust gate** before activation: show participants, roles, and exactly which object types they can access.
- Growth: Add one explicit primary acquisition motion: founder-led outbound into a concierge pilot. [market_motion]


## Rejected

- Tech: Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Tech: Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Growth: Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]


## Open Points

- Tech: Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.
- Growth: Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Growth: Specify reminder channels and visible failure handling before pilot launch. [operations]
- Growth: Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Tech: Which exact document types are allowed in MVP, and which are blocked?
- Tech: Should caregivers be able to upload documents or only comment on task/event updates?
- Tech: What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- Growth: Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- Growth: What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- Growth: What exact family pain signals best predict conversion to pilot? [demand_validation]
- Tech recommendation needing arbitration: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.
- Tech recommendation needing arbitration: Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Tech recommendation needing arbitration: Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Tech recommendation needing arbitration: Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.
- Growth recommendation needing arbitration: Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Growth recommendation needing arbitration: Specify reminder channels and visible failure handling before pilot launch. [operations]
- Growth recommendation needing arbitration: Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Growth recommendation needing arbitration: Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]
- Tech open question: Which exact document types are allowed in MVP, and which are blocked?
- Tech open question: Should caregivers be able to upload documents or only comment on task/event updates?
- Tech open question: What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- Growth open question: Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- Growth open question: What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- Growth open question: What exact family pain signals best predict conversion to pilot? [demand_validation]


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# CareSync MVP Product Proposal

## Product Problem
Families caring for elderly relatives coordinate across too many fragmented channels: calls, texts, paper notes, emails, and ad hoc caregiver updates. That creates missed appointments, medication confusion, duplicated effort, and stress. Existing tools are either too generic or too clinical, and they do not give one shared, trusted view of who is doing what and when.

## Initial Wedge
A shared family care coordination hub for one elderly relative that solves the most immediate recurring problem: keeping appointments, responsibilities, and time-sensitive updates visible to everyone involved.

The narrow wedge is not “full eldercare management.” It is:
- one care recipient
- one shared family/caregiver coordination space
- one source of truth for tasks, appointments, and status updates

## First Target User
Primary user:
- One adult child or family coordinator managing care for an elderly parent who has multiple siblings or caregivers involved

Secondary users:
- Other family members who need visibility but do not want to manage the whole process
- A professional caregiver or home nurse who needs to receive updates and post status changes

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp/iMessage groups
- Shared Google Calendar
- Paper notes and phone calls
- Caregiver agency portals
- Generic task apps like Todoist, Notion, or Trello

Why they are insufficient:
- Messages get buried and lack structure
- Calendars do not capture care tasks, responsibility, or status
- Generic tools are not designed for caregiving permissions, reminders, or health context
- Agency portals usually work only within one provider, not across the whole family network

Switching trigger:
- A family is already missing appointments, duplicating tasks, or arguing over responsibility
- Coordination now involves 3+ people across locations
- A caregiver needs a structured way to post updates and handoffs
- The current mix of chat + calendar feels unreliable and stressful

## Core MVP Workflow
1. A family coordinator creates a care space for one elderly relative.
2. They invite a small set of participants: family members and optionally one professional caregiver.
3. They add a basic care schedule:
   - appointments
   - medications
   - recurring tasks
   - contact list for emergencies
4. The system sends reminders and shows task ownership/status.
5. Caregivers and family members can mark tasks complete and post short updates.
6. Everyone sees the current care view in one place.

## In Scope
- Single-care-recipient care space
- Invite-only family and caregiver access
- Shared calendar for appointments and recurring care tasks
- Task assignment and completion status
- Basic reminders and notifications
- Simple caregiver updates/log notes
- Emergency contact list
- Role-based permissions for family vs caregiver access
- Secure document upload for a small set of critical files, if needed for coordination
- Mobile-first and low-friction onboarding

## Out of Scope
- Broad “elder care operating system”
- Multi-household or multi-recipient management
- AI-driven care recommendations
- Complex clinical records management
- Live chat replacing existing messaging apps
- Billing, claims, or payment processing
- Direct integration with hospitals, pharmacies, or EHR systems
- Full compliance tooling for every country at launch
- Advanced analytics or predictive alerts
- Marketplace for services or home healthcare booking
- Elder-facing self-service as a primary workflow

## MVP Build Vs Pilot Operations
### Must Build Now
- Shared care space for one relative
- Invitations and basic access control
- Calendar and task coordination
- Reminders/notifications
- Status updates and notes
- Emergency contact list
- Basic secure document upload

### Manual Or Operational During Pilot
- Onboarding families into the system
- Setting up the initial care plan
- Helping users migrate from text messages and paper notes
- Customer support for permissions and setup issues
- Monitoring whether reminders are actually being acted on

### Deferred Until After Proof
- Native messaging system
- Multi-recipient family management
- Deep document workflows and versioning
- External system integrations
- Billing and payment features
- Advanced compliance automation
- AI assistance
- Service marketplace

## Business Model Hypothesis
The most plausible early model is subscription-based pricing for families, with a later extension to caregiver agencies.

Hypothesis:
- Families pay a modest monthly fee for one care space and premium coordination features
- Agencies may later pay for multi-client coordination and team access
- The first revenue test should focus on willingness of families to pay for reduced coordination stress, not on enterprise procurement

## Critical Assumptions
- Families will adopt a new tool if it clearly reduces missed tasks and confusion
- A single shared view is more valuable than continued use of chat threads and paper
- The primary user can do the initial setup without heavy training
- Caregivers will participate in a lightweight update workflow
- Trust and privacy concerns will not block adoption if permissions are clear
- The product can be useful without deep clinical integrations

## How To Test Quickly
- Run concierge-style pilots with 5–10 families managing one elderly relative
- Measure whether they replace at least part of their existing coordination workflow within 2 weeks
- Test the smallest useful flow:
  - create care space
  - assign 5–10 tasks/appointments
  - send reminders
  - capture completion and updates
- Interview family coordinators after one week on what they would miss if the product disappeared
- Test willingness to pay with a simple pricing prompt after pilot use
- Observe whether caregivers actually post updates without extra chasing

## Acceptance Criteria
- A family coordinator can create a care space in under 10 minutes
- At least 3 invited participants can access the same care view
- Users can add appointments, tasks, and reminders without training
- Task completion and updates are visible to all permitted users
- Permissions prevent unauthorized access to sensitive information
- Reminder delivery works reliably for the pilot cohort
- Pilot users can share at least one critical document securely
- At least half of pilot families use the product weekly for 2+ weeks

## Risks And Failure Modes
- Families continue using chat apps because they feel faster and more familiar
- The product becomes too broad and loses simplicity
- Privacy and trust concerns prevent families from uploading sensitive information
- Elderly participants are assumed to be direct users when the real buyer is the family coordinator
- Caregivers do not consistently update the system, reducing its value
- Compliance requirements vary by market and can slow launch
- Reminder fatigue makes notifications easy to ignore

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Clear proof that families will switch from existing coordination habits [switching_trigger]
- Evidence that caregivers will reliably participate in lightweight updates [caregiver_participation]
- Confirmation that privacy and permissions are sufficient for sensitive information [privacy_trust]

Required Improvements:
- Run a small concierge pilot with real families before building more features [pilot_validation]
- Validate the minimum permission model and document handling expectations [permissions_model]
- Test the smallest recurring workflow and measure weekly retention [retention_signal]

## Recommendation
Proceed with a narrow concierge pilot, not a broad build.

Build only the shared coordination hub for one elderly relative, with tasks, appointments, reminders, basic updates, and permissions. Use manual support to onboard families and set up the first care plan. Defer messaging, integrations, and broader platform ambitions until the pilot proves that families will actually replace parts of their current workflow and continue using the product weekly.

## Retained Decisions

- Tech: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.

## Deferred Decisions

- Tech: Add an explicit **privacy/trust gate** before activation: show participants, roles, and exactly which object types they can access.
- Growth: Add one explicit primary acquisition motion: founder-led outbound into a concierge pilot. [market_motion]

## Rejected Recommendations

- Tech: Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Tech: Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Growth: Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]

## Unresolved Tensions

- Tech recommendation needing arbitration: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.
- Tech recommendation needing arbitration: Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Tech recommendation needing arbitration: Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Tech recommendation needing arbitration: Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.
- Growth recommendation needing arbitration: Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Growth recommendation needing arbitration: Specify reminder channels and visible failure handling before pilot launch. [operations]
- Growth recommendation needing arbitration: Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Growth recommendation needing arbitration: Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]
- Tech open question: Which exact document types are allowed in MVP, and which are blocked?
- Tech open question: Should caregivers be able to upload documents or only comment on task/event updates?
- Tech open question: What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- Growth open question: Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- Growth open question: What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- Growth open question: What exact family pain signals best predict conversion to pilot? [demand_validation]

## Applied Changes

- Tech: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.

## Remaining Open Points

- Tech: Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.
- Growth: Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Growth: Specify reminder channels and visible failure handling before pilot launch. [operations]
- Growth: Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Tech: Which exact document types are allowed in MVP, and which are blocked?
- Tech: Should caregivers be able to upload documents or only comment on task/event updates?
- Tech: What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- Growth: Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- Growth: What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- Growth: What exact family pain signals best predict conversion to pilot? [demand_validation]
- Tech recommendation needing arbitration: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.
- Tech recommendation needing arbitration: Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Tech recommendation needing arbitration: Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Tech recommendation needing arbitration: Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.
- Growth recommendation needing arbitration: Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Growth recommendation needing arbitration: Specify reminder channels and visible failure handling before pilot launch. [operations]
- Growth recommendation needing arbitration: Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Growth recommendation needing arbitration: Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]
- Tech open question: Which exact document types are allowed in MVP, and which are blocked?
- Tech open question: Should caregivers be able to upload documents or only comment on task/event updates?
- Tech open question: What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- Growth open question: Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- Growth open question: What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- Growth open question: What exact family pain signals best predict conversion to pilot? [demand_validation]

## Risks

- Permission complexity grows faster than the rest of the product and breaks trust [privacy_trust]
- Reminder delivery becomes unreliable across channels and users stop depending on the system [operations]
- Families revert to chat apps if structured updates feel too slow or rigid [market_motion]
- Families may like the idea but never fully switch from chat-based coordination.
- Caregivers may not keep the system updated consistently.
- Trust and privacy concerns may suppress document sharing and participation.
- The permission model may still feel too coarse for some families. [privacy_trust]
- Users may share sensitive information in notes or documents beyond intended scope. [privacy_trust]
- Notification content may accidentally expose private details if not carefully constrained. [data_access]
- Families continue using WhatsApp because it feels faster and already has network effects. [market_motion]
- Caregivers do not reliably post updates, breaking the shared record. [operations]
- Privacy concerns slow or block adoption of shared documents and notes. [privacy_trust]
- Families may still distrust shared document storage even with fixed permissions.
- A fixed role model may be too rigid for some real caregiving arrangements.
- Notification failures could undermine the core trust loop.
- Families keep using WhatsApp because it remains faster and socially embedded. [demand_validation]
- Caregivers do not consistently post updates. [metrics_validation]
- Privacy concerns reduce willingness to invite others. [privacy_trust]

## Open Questions

- What exact role permissions are required for the pilot, and which fields/documents are sensitive enough to hide from caregivers?
- Which notification channels are acceptable for MVP: email only, SMS, or both?
- Are documents strictly optional, or must they support a pilot-critical workflow from day one?
- What exact family profile has the highest pain and fastest willingness to adopt?
- Who is the true buyer: the coordinator, the whole family, or an agency partner?
- What is the minimum permission model that families will trust without feeling exposed?
- What exact role matrix is acceptable for the pilot without custom permissions?
- Which document categories are allowed in MVP, and which are prohibited?
- Should coordinators be able to revoke access immediately or require confirmation?
- What is the exact trigger event that makes a family accept switching into the product? [demand_validation]
- Which reminder channel is most trustworthy for the pilot: email, SMS, push, or all three? [operations]
- Will caregivers participate when invited, or is the product only usable with family updates? [metrics_validation]
- Which exact document types are allowed in MVP, and which are blocked?
- Should caregivers be able to upload documents or only comment on task/event updates?
- What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- What exact family pain signals best predict conversion to pilot? [demand_validation]

## Final Revised PRD

# CareSync MVP Product Proposal

## Product Problem
Families caring for one elderly relative coordinate across calls, texts, paper notes, email, and caregiver handoffs. That fragments responsibilities, causes missed appointments and duplicated effort, and makes it hard to know what changed, who is responsible, and whether a task was completed. Current tools are either too generic or too chat-driven to serve as a trusted shared record for care coordination.

## Initial Wedge
A narrow, invite-only coordination space for one elderly relative that gives the family a single shared view of appointments, recurring tasks, and structured updates.

The wedge is not full eldercare management. It is:
- one care recipient
- one care space
- one trusted coordination record for tasks, events, updates, and access control

## First Target User
Primary user:
- A remote adult child or family coordinator managing care for one parent with help from 2–4 other participants

Secondary users:
- Other family members who need visibility without owning setup
- One caregiver or home nurse who needs to see assignments and post brief updates

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp or iMessage groups
- Shared Google Calendar
- Paper notes and phone calls
- Generic task tools like Todoist, Notion, or Trello
- Caregiver agency portals

Why they are insufficient:
- Messages are unstructured and hard to audit
- Calendars do not capture task ownership or status
- Generic tools do not handle permissions or care-specific context well
- Agency portals do not coordinate across the whole family network

Switching trigger:
- Coordination is already failing: missed appointments, repeated reminders, or unclear ownership
- 3+ people are involved across locations
- A caregiver needs a structured place to post updates or handoffs
- The current mix of chat, calls, and notes feels unreliable enough to replace

## Core MVP Workflow
1. The coordinator creates a care space for one elderly relative.
2. They invite a small set of family members and optionally one caregiver.
3. They review an explicit privacy and trust gate showing:
   - who is invited
   - what each role can see and do
   - which object types are shared
4. They confirm consent before the care space becomes active.
5. They add the recurring coordination items that matter most:
   - appointments
   - medication reminders
   - caregiving tasks
   - emergency contacts
6. The system sends reminders and shows delivery status.
7. Family members and caregivers post structured updates tied to tasks or events.
8. Everyone with permission sees the current care view in one place.
9. The coordinator can revoke access immediately if needed.

## In Scope
- One care recipient per care space
- Invite-only access
- Fixed role-based permissions for coordinator, family member, caregiver, and admin
- Explicit permission matrix for tasks, events, updates, documents, and emergency contacts
- Privacy and trust gate before activation
- Coordinator consent confirmation before activation and before sensitive document sharing
- Shared calendar for appointments and recurring tasks
- Task assignment and completion status
- Reminder notifications with visible delivery status
- Structured updates attached to tasks or events
- Emergency contact list
- Basic secure document upload for a small number of critical files
- Audit log for sensitive actions such as sharing, uploading, permission changes, revocation, and access review
- Immediate access revocation path
- Mobile-first onboarding

## Out of Scope
- Multi-recipient or household management
- Organization hierarchies for agencies
- Real-time chat or chat replacement
- AI recommendations or predictive alerts
- Complex clinical records management
- Direct integrations with hospitals, pharmacies, or EHR systems
- Billing, claims, or payments
- Marketplace or service booking
- Advanced analytics
- Broad compliance automation across countries
- Elder-facing self-service as a primary workflow
- Custom permission builder beyond the fixed MVP matrix
- Broad document library or open-ended file sharing

## MVP Build Vs Pilot Operations
### Must Build Now
- One care space per elderly relative
- Invitations and role-based access control
- Fixed permission matrix for core roles and object types
- Privacy and trust gate showing participants, roles, and access
- Coordinator consent confirmation before activation
- Calendar and task coordination
- Reminder and notification delivery with visible status
- Structured updates on tasks/events
- Emergency contact list
- Basic secure document upload for limited critical files
- Audit logging for sensitive actions
- Immediate access revocation
- Simple access review flow at activation

### Manual Or Operational During Pilot
- Founder-led onboarding
- Setting up the initial care plan with the family
- Helping families map existing WhatsApp/text/paper workflows into the product
- Support for invitation issues, permission questions, and revocation requests
- Manual reminder retry support if delivery fails
- Monitoring whether reminders and updates are actually used

### Deferred Until After Proof
- Native chat
- Multi-recipient support
- Agency dashboards and organization hierarchy
- External system integrations
- Billing and payments
- Advanced compliance tooling
- AI assistance
- Marketplace features
- Granular custom permissions
- Expanded document management

## Business Model Hypothesis
Initial pricing should likely be a family subscription for one care space.

Hypothesis:
- A remote family coordinator will pay a modest monthly fee if the product clearly reduces coordination failures and stress
- Later, caregiver agencies may pay for team access or multi-client support
- The first revenue test should focus on willingness to pay from families, not on enterprise sales

## Critical Assumptions
- A narrow shared care space is valuable enough to replace part of existing chat-based coordination
- The coordinator is willing to set up the system for the family
- Caregivers will post structured updates without much friction
- Families will trust the product if permissions are explicit and access is auditable
- Reminder delivery is reliable enough to matter
- The product can be useful without deep medical integrations

## How To Test Quickly
- Run concierge pilots with 5–10 families managing one elderly relative
- Focus on remote adult children coordinating care across siblings or one caregiver
- Test the smallest useful loop:
  - create one care space
  - invite participants
  - add 3–5 tasks, appointments, or reminders
  - receive one structured update
  - confirm completion
- Measure whether the product replaces part of their current coordination process within 2 weeks
- Interview coordinators after week one about what they would miss if the product disappeared
- Test willingness to pay after the pilot with a simple pricing prompt
- Observe whether caregivers and family members actually post updates without repeated chasing

Decision rule:
- Proceed if at least 3 of 5 pilot families are active in week 2, and at least one non-coordinator participant posts or updates weekly in each active family, and at least one reminder-response-update loop is completed in week 1 for most pilot families
- Revise if fewer than 3 of 5 families remain active in week 2, or non-coordinator posting is inconsistent across the pilot
- Reject if the product cannot get at least one reminder-response-update loop completed within the first week for most pilot families, or families refuse to move even a small part of coordination out of chat/calls

## Acceptance Criteria
- A coordinator can create a care space in under 10 minutes
- At least 3 invited participants can access the same care view
- Users can add appointments, tasks, and reminders without training
- Family members and caregivers can post structured updates tied to tasks or events
- Permissions block unauthorized access to sensitive information
- Reminder delivery works reliably for the pilot cohort
- Sensitive actions are captured in an audit log
- At least half of pilot families use the product weekly for 2+ weeks
- At least one non-coordinator participant posts an update weekly in active pilot families
- The privacy and trust gate clearly shows who can access each object type before activation

## Risks And Failure Modes
- Families stay on WhatsApp and phone calls because they feel faster
- The product becomes too broad and loses focus
- Privacy concerns block adoption of shared notes or documents
- Caregivers do not consistently update the system
- Notification fatigue reduces engagement
- Compliance needs vary by country and slow launch
- The coordinator is not the actual buyer, making payment conversion weak
- Fixed permissions may feel too rigid if they do not match family expectations

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Proof that families will switch part of their coordination workflow [metrics_validation]
- Proof that caregivers or other non-coordinators will reliably post structured updates [metrics_validation]
- Confirmation that the fixed permission model is trusted for sensitive sharing [privacy_trust]

Required Improvements:
- Run a small concierge pilot before expanding scope [pilot_validation]
- Validate the fixed permission matrix and access controls with real families [privacy_trust]
- Measure weekly retention, reminder-response-update loops, and non-coordinator posting in the pilot [metrics_validation]

## Recommendation
Proceed with a narrow concierge pilot, not a broader build.

Build only the shared coordination space for one elderly relative, with tasks, appointments, reminders, structured updates, permissions, and minimal secure document handling. Use manual onboarding and setup during the pilot. Defer chat, integrations, multi-recipient support, and broader platform ambitions until the product proves that families will replace part of their current workflow, keep using it weekly, and get at least one non-coordinator participant contributing updates.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Tech: Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.

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
