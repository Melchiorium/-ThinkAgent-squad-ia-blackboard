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