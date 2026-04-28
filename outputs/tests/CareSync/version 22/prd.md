# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care are forced to manage appointments, medications, tasks, documents, and responsibility handoffs across texts, calls, paper notes, and scattered apps. This creates missed follow-through, repeated explanations, and low confidence that everyone is acting on the same plan.

The narrow problem to solve first is one primary organizer needing a trusted shared coordination space for one elderly relative and a small care circle, with visible ownership, reminder reliability, and enough structure to replace repeated coordination across informal tools.

## Initial Wedge
A single shared coordination workspace for one elderly care recipient, used by:
- one primary family organizer
- one invited family member
- one professional caregiver

The wedge is limited to recurring coordination around:
- appointments
- medication reminders
- assigned tasks
- short structured updates
- essential document reference

The MVP must prove that a purpose-built coordination space is better than group texts and shared calendars for this one use case.

## First Target User
Primary target user: an adult child who is the main coordinator for an aging parent.

First use case: coordinating a parent’s recurring medical appointments, medication reminders, and caregiving tasks with one sibling and one paid caregiver.

Why this user first:
- they feel the coordination pain most directly
- they can set up the workspace and invite others
- they are most likely to pay if value is proven
- they can evaluate whether the tool reduces follow-up work and missed tasks

## Existing Alternatives And Switching Trigger
Existing alternatives:
- group texts and phone calls
- shared calendars
- notes apps and spreadsheets
- paper binders
- caregiver agency tools

Switching trigger:
- coordination is becoming too messy to manage in informal tools
- appointment and medication follow-through is slipping
- multiple people need the same current plan and responsibility list
- one person is repeatedly re-explaining the care situation

CareSync must be more structured and trustworthy than generic collaboration tools, but much narrower than a full health record system.

## Core MVP Workflow
1. Primary organizer creates one care space for one elderly relative.
2. Organizer enters the basic care profile, key contacts, and primary responsibilities.
3. Organizer acknowledges authority/consent to share coordination information for this care space.
4. Organizer invites a small set of participants with defined roles.
5. Organizer adds appointments, medication reminders, and care tasks.
6. Participants receive reminders and can post short structured updates tied to tasks or appointments.
7. Everyone sees the current schedule, task ownership, and recent activity.
8. Organizer uploads a small set of essential documents for reference.
9. Reminder delivery and acknowledgements are visible so the organizer can tell whether important items were seen.

The workflow must make it easy to answer: what needs to happen, who owns it, and what changed.

## In Scope
- One care space per elderly person
- Invite-based access
- Defined roles for organizer, family member, and caregiver
- Shared appointment calendar
- Medication reminders
- Shared task list with owner and status
- Structured updates/comments tied to tasks or appointments
- Essential document upload and storage
- Simple permission controls by role
- Default visibility rules for core objects
- Delivery notifications for reminders and task changes
- Basic activity log and audit trail
- Organizer consent/authority acknowledgement during onboarding
- Support-only revocation and invite correction workflow
- Basic read-status or acknowledgement on critical reminders
- One launch market with a defined privacy/consent baseline
- Shareable-vs-private defaults for documents

## Out of Scope
- Full medical record management
- Provider or pharmacy integrations
- Free-form chat or messaging replacement
- Emergency response features
- Clinical decision support
- Medication verification or adherence monitoring
- Insurance, billing, or claims workflows
- Elder-facing UX as the primary workflow
- Multi-elder household optimization
- Caregiver marketplace or agency marketplace
- Home healthcare operations
- Advanced permission granularity
- Analytics and reporting
- Broad self-serve marketing motion for launch

## MVP Build Vs Pilot Operations
### Must Build Now
- One care space per elder
- Invite-based access with organizer, family member, and caregiver roles
- Shared calendar, reminders, tasks, and structured updates
- Essential document upload and retrieval
- Activity log and audit trail
- Notification delivery
- Organizer consent/authority acknowledgement
- Default visibility rules for core objects
- Basic read-status or acknowledgement for critical reminders
- Basic admin controls for access revocation and invite correction
- One launch-market privacy/consent baseline
- Shareable-vs-private document defaults

### Manual Or Operational During Pilot
- White-glove onboarding for the primary organizer
- Manual setup help for the first care plan and invite list
- Support for permission questions and document handling issues
- Manual review of regional privacy/consent requirements for the launch market
- Founder-led outreach to recruit pilot families
- Pilot follow-up to check return use and blocked workflows

### Deferred Until After Proof
- Full chat or messaging system
- Integrations with hospitals, pharmacies, or EHRs
- Advanced permissions and granular sharing rules
- Elder self-service experiences
- Analytics dashboards and reporting
- Automation beyond basic reminders
- Agency-specific workflows
- Broader home healthcare services

## Business Model Hypothesis
Primary hypothesis: a subscription paid by the family organizer for one care space.

Initial pricing hypothesis:
- one plan per care recipient
- optional higher tier for additional participants or storage
- later, agency licensing only if family usage proves repeatable

The business model should be tested only after the product proves recurring value in family coordination.

## Critical Assumptions
- A family organizer will adopt a dedicated tool if setup is simple enough.
- Structured updates and clear ownership are more useful than generic chat for this workflow.
- One care recipient is the right unit for the initial product.
- Family members and caregivers will trust the platform with sensitive information.
- Reminder delivery and visible acknowledgement are enough to create measurable value.
- A launch market can be chosen with a workable privacy and consent baseline.
- The organizer can legitimately share coordination information for the care circle in the chosen launch market.

## How To Test Quickly
- Run concierge pilots with 5–10 families coordinating one elderly relative.
- Manually onboard each organizer and care circle.
- Observe whether the workspace replaces repeated texts and calls.
- Measure whether task completion and reminder follow-through improve.
- Track whether caregivers and siblings actually return to the workspace.
- Test willingness to pay after 2–4 weeks of use.
- Validate whether permissioning, consent, and document access feel trustworthy enough for sensitive coordination.
- Check whether critical reminders are actually seen via acknowledgements or read-status.
- Define success for the pilot as:
  - organizer and at least one invited participant return without founder prompting within 2–4 weeks
  - the workspace is used for recurring coordination in the next care cycle
  - at least 3–5 critical items are entered and acknowledged
  - families prefer the workspace over texts/spreadsheets for those items
- If those thresholds are not met, do not expand scope; revise or stop.

## Acceptance Criteria
- A primary organizer can create a care space in under 10 minutes.
- The organizer can assign at least two participant roles correctly.
- Users can view one shared calendar, one task list, and one reminder schedule.
- Reminder notifications are delivered reliably.
- Critical reminders show whether they were seen or acknowledged.
- Participants can post updates tied to a task or appointment.
- Uploaded documents are visible only to authorized users.
- Activity history shows who changed what and when.
- The organizer can revoke access and correct an invite without support intervention.
- Pilot users can complete the core workflow without training beyond initial setup.
- The pilot produces repeat use within 2–4 weeks from the organizer and at least one invited participant.

## Risks And Failure Modes
- Families stay with texts and shared calendars instead of switching.
- The product feels too complex for the organizer to maintain.
- Trust concerns around sensitive information block adoption.
- Caregivers do not actively use the workspace.
- Reminder delivery or acknowledgement is unreliable enough to undermine confidence.
- The product becomes a generic collaboration tool instead of a care-specific workflow.
- Privacy and consent expectations vary by launch market.
- Access control issues undermine trust immediately.
- Pilot usage is too shallow to justify broader build-out.

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Launch geography and minimum privacy/consent baseline are not yet defined [privacy_compliance]
- Trust expectations for organizer, family, and caregiver access are not yet validated [trust_model]
- Value versus generic group text and calendar tools is not yet proven [value_proof]
- Critical reminder acknowledgment behavior is not yet validated [notification_reliability]
- Success metrics for repeat use and return behavior are not yet confirmed [metrics_validation]

Required Improvements:
- Select one launch market and define the minimum compliance baseline [privacy_compliance]
- Validate role and access expectations with real organizers and caregivers [trust_model]
- Run a concierge pilot to prove recurring coordination value and repeat use [value_proof]
- Confirm that critical reminders need visible acknowledgements or read-status to create trust [notification_reliability]
- Set explicit MVP decision metrics for repeat use, invite acceptance, and recurring coordination activity [metrics_validation]

## Recommendation
Proceed with a narrow concierge pilot, not a broad build. Keep the MVP limited to one care recipient, one organizer, a small care circle, and structured coordination only. Build the minimum trust layer needed for sensitive sharing: consent acknowledgement, object-level visibility defaults, auditability, and visible confirmation for critical reminders.

Do not expand into messaging, integrations, or broader healthcare workflows until the pilot proves that families will adopt, trust, and repeatedly use the workspace.

If the pilot does not show clear repeated usage and coordination improvement, stop or reposition before adding more features.