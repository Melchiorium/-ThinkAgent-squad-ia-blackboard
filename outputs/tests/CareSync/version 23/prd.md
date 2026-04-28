# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care lose track of who is doing what, when it is due, and what changed since the last update. The information is scattered across texts, calls, paper notes, and generic chat apps, which creates missed follow-through and repeated coordination effort.

The MVP should solve only the coordination loop: a shared source of truth for tasks, reminders, status updates, and optional document sharing for one elder.

## Initial Wedge
A single shared care space for **one elder and one family coordinator**, with optional access for a small number of family members and one professional caregiver if needed.

The wedge is intentionally narrow:
- shared tasks
- appointment and reminder tracking
- simple status view
- optional document storage for care coordination only

This wedge exists to prove that families will switch from chat/spreadsheets to a dedicated care space for recurring coordination.

## First Target User
**Primary user:** an adult child coordinating care for one aging parent who lives at home or mostly at home.

Why this user first:
- they feel the coordination pain most directly
- they are usually the person who can set up the system
- they are the most likely adoption driver for the rest of the family
- they can evaluate whether the product reduces coordination burden

## Existing Alternatives And Switching Trigger
### Existing Alternatives
- Family group chats and phone calls
- Shared notes, calendars, and spreadsheets
- Paper notebooks and printed instructions
- Generic task apps
- Basic caregiver agency tools
- Hospital and insurer portals that do not coordinate day-to-day care

### Switching Trigger
Families switch when:
- multiple people are involved and accountability is failing
- appointments or follow-through are being missed
- the primary coordinator is overwhelmed
- someone needs visibility without repeated calling or texting

The trigger is coordination breakdown, not feature richness.

## Core MVP Workflow
1. The primary user creates a care space for one elder.
2. The primary user invites a few participants.
3. The primary user adds:
   - upcoming appointments
   - recurring reminders
   - a short task list
   - optional care-related documents for coordination only
4. Participants receive email notifications and can view the shared status.
5. Participants can mark tasks complete or add a short update.
6. The coordinator can see what is upcoming, what is done, and what still needs attention.

This workflow must prove that CareSync reduces coordination friction better than messaging and spreadsheets.

## In Scope
- One care space per elder
- One primary coordinator plus a small number of family members
- Optional one caregiver participant
- Invite-based access
- Shared task list with due dates and completion status
- Appointment entries
- Recurring reminders
- Simple activity/status feed
- Email notifications only
- Mobile-friendly web experience
- Coarse role-based permissions
- Consent on invite acceptance
- Visible privacy notice for each participant
- Audit log for key actions
- Access revocation
- One launch geography with a defined minimum privacy/compliance baseline
- Data limited to coordination metadata plus optional uploaded documents; no clinical records ingestion

## Out of Scope
- Full medical records management
- Clinical decision support
- Prescriptions, refills, or pharmacy integrations
- AI-generated care plans or summaries
- Emergency response functionality
- Billing, insurance, or claims workflows
- Agency marketplace or caregiver matching
- Rich in-product messaging
- Multi-elder household management
- Native mobile apps
- Advanced permission hierarchies
- SMS notifications
- Multi-country localization
- Elder-first onboarding as the primary path
- Complex document workflows beyond simple file storage and viewing
- Rich health-content data models beyond basic coordination metadata
- Public launch before the launch geography and compliance baseline are defined
- Clinical system ingestion of any kind

## MVP Build Vs Pilot Operations
### Must Build Now
- Care space creation for one elder
- Invite-based access
- Shared task list
- Appointment and reminder scheduling
- Optional document upload and viewing
- Simple status/activity feed
- Coarse permissions by role
- Invite acceptance consent
- Visible privacy notice
- Audit log for membership, document, task, reminder, and access actions
- Access revocation
- Email notifications
- Minimal admin tooling for deletion, export, revocation, and audit review

### Manual Or Operational During Pilot
- Concierge onboarding for first families
- Help setting up roles, tasks, and reminders
- Human support for invite and notification issues
- Manual handling of edge cases during pilot
- Pilot feedback collection from family coordinators

### Deferred Until After Proof
- SMS notifications
- Native mobile apps
- Rich messaging features
- Advanced permission hierarchies
- Care agency workflows
- EHR, calendar, or pharmacy integrations
- AI automation
- Multi-elder support
- Country-specific expansion
- Elder self-service workflows
- Rich clinical data capture

## Business Model Hypothesis
A subscription model is the best initial hypothesis.

- **Primary hypothesis:** family-paid monthly subscription per care space
- **Why:** simplest to validate, closest to the user who feels the pain, and avoids enterprise sales complexity
- **Later possibility:** B2B2C licensing for agencies or home-care providers if the family workflow proves valuable

The MVP should not depend on agency procurement to succeed.

## Critical Assumptions
- Families will move at least part of coordination out of chat apps into a dedicated tool
- A narrow shared workspace is enough to create repeat use
- The primary coordinator can onboard others with low friction
- Email-only reminders are enough for the pilot
- Coarse permissions and auditability are sufficient to establish trust early
- The product can be useful without deep clinical integrations
- Professional caregivers will participate if the workflow is simple and low burden
- A defined launch geography and baseline compliance posture are enough for a safe pilot
- Optional document sharing is necessary for proof, but only if limited to coordination use

## How To Test Quickly
- Run 10–15 concierge-led pilots with families coordinating one elder
- Use one launch geography and one minimum compliance baseline
- Compare current coordination methods vs. CareSync on:
  - missed tasks
  - time spent coordinating
  - perceived stress
  - willingness to continue using the tool
- Test whether families actually use:
  - shared tasks
  - reminders
  - optional document upload/view
  - status updates
- Measure:
  - weekly active use by the coordinator
  - completion rate of assigned tasks/reminders
  - retention after 2–4 weeks
  - willingness to pay after pilot
- Validate whether invite acceptance and privacy notice flows reduce trust friction
- Define activation as at least one coordinator plus 2–4 invited participants using the shared space for a real upcoming task or appointment

## Acceptance Criteria
- A primary user can create a care space in under 5 minutes
- At least 3 other participants can be invited and granted access successfully
- A task or reminder can be created, assigned, and completed reliably
- Optional documents can be uploaded and viewed only by permitted users
- Participants can see a clear current status without asking the coordinator
- Email notifications are delivered consistently
- Key actions are recorded in an audit log
- Access can be revoked successfully
- Invite acceptance consent and privacy notice are visible before access is granted
- Admin can export, delete, or review audit data for a pilot account
- The workflow is understandable without training beyond a short setup guide
- Pilot users report reduced coordination friction compared with chat or spreadsheets
- No clinical records ingestion is required for successful use

## Risks And Failure Modes
- Families do not change behavior from existing group chats
- The product is still too broad for a simple workflow
- Trust concerns block document sharing and permission use
- Professional caregivers refuse to adopt another tool
- Email-only delivery is not enough for some families
- Compliance requirements vary by launch geography and delay release
- The product drifts into generic project management instead of care-specific coordination
- The MVP becomes too dependent on operational support instead of proving product value
- Optional document support creates compliance complexity without improving proof enough

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Switching behavior is not yet validated in real family coordination [demand_validation]
- Launch geography and minimum privacy/compliance baseline are not yet fixed [compliance]
- Trust and access flows are not yet validated with real users [privacy_trust]

Required Improvements:
- Run concierge pilots to validate actual switching behavior and retention [demand_validation]
- Define the initial launch geography and minimum compliance baseline before any public launch [compliance]
- Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope [privacy_trust]

## Recommendation
Proceed with a narrow concierge-led MVP focused on one elder, one family coordinator, a small set of family participants, and optional one caregiver.

Keep the product centered on shared tasks, reminders, status, optional coordination-only documents, coarse permissions, consent, and auditability. Use email-only notifications and one launch geography for the pilot. Defer richer messaging, SMS, clinical data, integrations, and multi-elder support until the product proves recurring use and willingness to pay.