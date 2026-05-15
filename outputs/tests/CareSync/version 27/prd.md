## Product Problem

- Fragmented information flows across families coordinating elderly care.
- Siloed calendars, documents, reminders, and tasks create miscoordination.
- Privacy and trust concerns slow adoption among families and care providers.
- Providers and home nurses lack visibility into day-to-day family decisions.

## Initial Wedge

- Privacy-first centralized hub as MVP core for elder-care coordination (calendar, reminders, documents, messaging, permissions).
- Validate with a small real-family pilot before broader rollout to manage scope and risk.

## First Target User

- Adults managing care for elderly relatives across cities.
- Primary persona: family caregiver seeking a simple, trusted way to organize appointments, medications, tasks, and care plans.

## Existing Alternatives And Switching Trigger

- WhatsApp/SMS, shared calendars, handwritten notes, and scattered documents.
- Switching triggers: missed appointments/medications, caregiver confusion, desire for a single trusted platform with clear access controls.

## Core MVP Workflow

- Create a care group and invite family members and caregivers.
- Add elder recipient profile with essential medical and contact details.
- Schedule appointments in a shared calendar with reminders.
- Set up medication reminders with dosage instructions.
- Create and assign caregiving tasks with due dates and assignees.
- Upload and share important documents (care plans, emergency contacts, test results).
- Enable secure messaging and role-based permissions.
- Provide emergency quick-contact access for vetted contacts.

## In Scope

- Shared family dashboard with calendar and reminders.
- Secure document storage and retrieval.
- Messaging system with group and direct messages.
- Permission management for family members and caregivers.
- Emergency contact coordination.

## Out of Scope

- Telehealth or real-time video visits.
- EHR or hospital system integrations in the MVP.
- Global regulatory compliance coverage beyond foundational protections.
- Advanced analytics or optimization beyond basic reminders.
- Offline-first functionality or multi-language support in the MVP.

## MVP Build Vs Pilot Operations

- MVP Build: Web and mobile app with core features (dashboard, calendar, reminders, docs, messaging, permissions).
- Pilot Operations: 6–8 week pilot with 2–3 real families; measure engagement, task completion, onboarding experience; collect qualitative feedback to refine onboarding and UI.

## Business Model Hypothesis

- Primary: B2C freemium with paid tiers (expanded storage, advanced permission controls, priority support).
- Optional partnerships with elder care agencies for co-branded experiences and referrals.
- Additional revenue from templates, care planning guides, or add-ons in later iterations.

## Critical Assumptions

- Families will adopt a centralized care coordination tool when privacy and simplicity are demonstrated.
- Users will keep caregiver and contact data up-to-date; engage with reminders and tasks.
- Privacy controls and consent flows meet expectations and build trust.
- Freemium monetization is viable after initial adoption; agency partnerships can broaden distribution.

## How To Test Quickly

- Run a 2–3 family remote pilot; track activation, first-week retention, feature usage.
- Usability tests focused on onboarding, permission settings, and calendar reminders.
- Gather qualitative feedback on trust, privacy perceptions, and willingness to pay.
- A/B test onboarding flows and reminder formats to boost engagement.

## Acceptance Criteria

- 2–3 active families over a 6-week pilot.
- Core features used: calendar events, reminders, tasks, and messaging with >60% task completion.
- User satisfaction rating ≥4.0/5 from pilot participants.
- No critical privacy incidents; basic consent flows implemented; data access controls defined.

## Risks And Failure Modes

- Privacy/data protection risks across jurisdictions.
- Low user adoption due to perceived complexity or distrust.
- Compliance challenges delaying broader rollout.
- Dependence on users maintaining accurate caregiver and contact data.
- Scope creep if onboarding expands beyond MVP boundaries.

## Product Readiness

Status: LIMITED

Blocking Gaps:
- [privacy] Data ownership, consent management, and access controls across jurisdictions; baseline encryption plans needed.
- [compliance] Clarify country-specific privacy and medical data regulations applicable to MVP regions.
- [onboarding] Define minimum viable onboarding flow to reduce friction for elderly users and non-tech-savvy family members.

Required Improvements:
- [privacy] Document data model, access controls, and retention policy; implement basic encryption in transit and at rest; define incident response process.
- [compliance] Produce a regulatory readiness plan outlining applicable laws and mitigations for target launch regions.
- [onboarding] Design and validate a low-friction onboarding flow with accessibility considerations and language options.

## Product Arbitration

### Retained
- Core MVP features: shared dashboard, calendar/reminders, secure document storage, messaging, and permission management.

### Deferred
- EHR integration, telehealth, offline mode, and multi-language support beyond MVP scope.

### Rejected
- None identified at this draft stage.

### Open Points
- MVP feature prioritization and scope confirmation.
- Pricing strategy and monetization thresholds to validate viability.
- Privacy and data residency approach across potential launch regions.
- Plan for accessibility improvements and language support.

### Rationales
- Prioritizing core coordination features aligns with the primary user need: reduce fragmentation and improve caregiving visibility.
- Deferring EHR integration reduces complexity and regulatory risk for the initial release.
- Privacy and compliance gaps must be addressed early to enable user trust and lawful operation.

## Product Locking

### Confirmed In Scope
- Shared family dashboard; calendar; reminders; secure document storage; messaging; permission management; emergency contacts.

### Confirmed Deferred
- EHR integration; telehealth capabilities; offline mode; advanced analytics; multi-language support for MVP.

### Confirmed Out Of Scope
- Global regulatory coverage beyond initial privacy/compliance groundwork; hospital system interoperability beyond basic documents.

### Locking Note
- This is an early MVP draft with a scoped, defensible MVP. Locking targets focus on core coordination features, privacy foundations, and a pilot with a small number of families. Further scope adjustments will follow after pilots and validation.
