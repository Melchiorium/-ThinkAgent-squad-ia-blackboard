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