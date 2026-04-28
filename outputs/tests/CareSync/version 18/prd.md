# CareSync MVP Product Proposal

## Product Problem
Families coordinating care for an elderly relative use fragmented tools: phone calls, group chats, notes, calendars, and paper documents. The result is missed appointments, duplicated work, unclear ownership, and poor visibility for relatives and caregivers who are not physically present. The MVP must solve one narrow coordination problem with enough trust and reliability to replace ad hoc coordination for a single care cycle.

## Initial Wedge
A shared coordination hub for one elderly relative, centered on the next appointment, the next task, and the next reminder.

This wedge is not full home healthcare, messaging replacement, or agency software. It is a single shared care space that makes the immediate plan visible, assigns ownership, and reduces repeated coordination across a small trusted circle.

## First Target User
Primary user:
- An adult child coordinating care for one aging parent, especially one living in a different city

Secondary users:
- Siblings or other family members who share responsibilities
- One professional caregiver or home nurse who needs limited visibility into the care plan

This is the narrowest credible first segment: high pain, clear coordination need, and enough motivation to adopt a new tool for one real care cycle.

## Existing Alternatives And Switching Trigger
Existing alternatives:
- WhatsApp, iMessage, SMS threads
- Shared calendars
- Google Drive / Dropbox for documents
- Paper notes, email chains, spreadsheets
- Verbal coordination with caregivers

Switching trigger:
- Recurring coordination breakdowns: missed appointments, duplicated reminders, unclear task ownership, or repeated questions about documents and instructions
- A family needs one place where everyone can see what needs attention next without searching across multiple channels

## Core MVP Workflow
1. One family member creates a care space for one elder relative.
2. They invite a small trusted circle of participants.
3. They add the next appointment, the next task, and a simple medication reminder.
4. Participants with permission can view the shared plan and update task status.
5. The system sends reminders through one primary channel and one fallback path for missed critical updates.
6. Everyone can see recent updates in one timeline or dashboard.
7. The organizer confirms one completed care cycle, then repeats the same workflow for the next cycle.

The MVP must prove that a shared coordination hub is more useful than fragmented communication for one real care cycle.

## In Scope
- Create one care space per elder relative
- Invite a small circle of family members and one caregiver
- Shared view of upcoming appointments
- Task assignment and status tracking
- Simple medication reminder entries
- Upload and view essential care documents
- Basic notification delivery
- Simple activity history of updates
- Role-based access for owner, family member, caregiver, and viewer
- Basic audit trail of who changed what
- Care-space-scoped access enforcement
- Founder-led support/admin tooling for onboarding and troubleshooting
- One primary notification channel for the pilot
- One fallback channel only for missed critical updates
- Minimum permission matrix for owner, family member, caregiver, and viewer

## Out of Scope
- Full chat replacement for family communication
- Direct clinical decision support
- Electronic medical record integration
- Complex care plans or multi-condition coordination
- Payment handling
- Marketplace for caregivers or agencies
- Telehealth or video visits
- AI-generated medical guidance
- Advanced analytics or predictive alerts
- Multi-elder household support
- Cross-care-space sharing
- Broad home healthcare service expansion
- Full legal/compliance automation across countries
- Rich agency admin tools
- Native offline support
- Advanced permission hierarchies
- Full medication management beyond reminder schedules
- Multiple notification channels at launch
- Broader launch audience beyond geographically dispersed adult children managing one parent

## MVP Build Vs Pilot Operations
### Must Build Now
- One care space per elder relative
- Invite flow with role-based access
- Appointment list and reminders
- Task assignment and status tracking
- Simple medication reminder entries
- Document upload and viewing
- Activity history for updates
- Basic audit trail
- Care-space scoped access enforcement
- Minimum permission matrix for owner, family member, caregiver, and viewer
- Founder-led support/admin tooling for pilot operations
- One primary notification channel
- One fallback notification path for missed critical updates

### Manual Or Operational During Pilot
- Founder-led onboarding of families
- Converting existing notes, texts, and paper into the care space
- Confirming caregiver participation and roles
- Setting up first care spaces
- Handling support questions and setup issues
- Monitoring reminder delivery and user feedback
- Nudging each family to complete one real care cycle

### Deferred Until After Proof
- Native messaging system
- Advanced permission hierarchies
- Agency admin tooling
- EMR integrations
- Smart alerts and automation
- Multi-elder household support
- Payment collection
- Advanced analytics
- Complex medication management
- Broader home healthcare services
- Additional notification channels
- Broader market expansion beyond the initial launch boundary

## Business Model Hypothesis
Primary hypothesis:
- Paid family subscription for coordination features

Secondary hypothesis:
- B2B2C licensing through elder care agencies or home care providers if family adoption proves strong but distribution is slow

Initial monetization should be tested with families first, because the first wedge is family coordination and the product should not depend on agency sales before proving usage.

## Critical Assumptions
- Families will trust a new platform with sensitive care information
- The product can be simpler than messaging apps while still being useful
- A shared dashboard creates enough coordination value to change behavior
- Non-technical family members and caregivers can use it without heavy training
- Reminder, task ownership, and document sharing are sufficient to prove value before adding chat or automation
- The initial pilot can be run within a defined privacy/compliance boundary
- Caregivers can participate with minimal access without breaking trust
- One completed care cycle is enough to show repeatable value
- One primary notification channel is reliable enough for the pilot

## How To Test Quickly
- Run a concierge pilot with 5–10 families managing one elder each
- Manually onboard each family and convert their current coordination process into the product
- Test one completed coordination cycle per family: next appointment, next task, and related reminder
- Measure whether users continue using the shared care space after the first week
- Measure missed tasks, duplicate reminders, and repeated questions compared with their prior method
- Interview caregivers on whether visibility improved their work
- Test willingness to pay after initial usage
- Validate that the primary reminder channel is received reliably enough for a real pilot cycle

## Acceptance Criteria
- A family can set up a care space for one elder in under 15 minutes
- At least three participants can be invited with distinct access roles
- Users can add an appointment, a task, a medication reminder, and a document
- Reminders are delivered reliably through the chosen primary channel
- Fallback notification works for missed critical updates
- Updates and changes are visible in an activity history
- Family members and caregivers can understand what needs attention next without training
- Pilot users complete at least one real coordination cycle in the product
- Access controls prevent users from seeing records outside their care space
- The organizer can confirm a completed cycle and reuse the same workflow for the next one

## Risks And Failure Modes
- Families may not switch from familiar messaging tools
- Privacy and trust concerns may block adoption
- The workflow may be too complex for low-digital-literacy users
- Reminders may create noise if not precise enough
- Sharing sensitive documents without strong controls may create risk
- The product may become a generic task app without enough caregiving-specific value
- Compliance needs may vary by country and slow launch
- Support burden may be high if onboarding is not tightly managed
- Notification delivery failures could undermine trust quickly

## Product Readiness
Status: LIMITED

Blocking Gaps:
- The initial pilot country or compliance boundary is not yet fixed [privacy_trust]
- The minimum permission matrix for owner, family member, caregiver, and viewer is not yet finalized [privacy_trust]
- The primary notification channel and fallback rule are not yet locked [reliability]

Required Improvements:
- Choose one launch market or compliance boundary before broader rollout [privacy_trust]
- Finalize the minimum access and visibility model for the first care space [privacy_trust]
- Lock one primary notification channel and define fallback behavior for missed critical updates [reliability]

## Recommendation
Proceed with a narrow MVP focused on one elder, one organizer, and a small invited care circle. Build only the shared care space, task and appointment coordination, simple medication reminders, document sharing, role-based access, auditability, and reliable notifications with fallback. Use founder-led pilot operations to validate trust, usability, reminder reliability, and repeated use before expanding into messaging, automation, agency tools, or broader healthcare features.