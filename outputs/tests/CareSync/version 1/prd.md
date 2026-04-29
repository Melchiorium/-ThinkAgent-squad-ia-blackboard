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