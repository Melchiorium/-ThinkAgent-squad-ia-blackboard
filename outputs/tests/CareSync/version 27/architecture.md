## Architecture Notes

- High-level approach: privacy-first MVP central hub for elder-care coordination with core workflows (dashboard, calendar/reminders, document storage, messaging) atop a single CareSync Services layer and unified data store; RBAC with consent-driven data exposure; pilot-focused telemetry.
- Key components:
  - CareSync Services (SG) orchestrating core workflows: Calendar (CAL), Reminders (REM), Document Storage (DOC), Messaging (MSG), Permissions (PERM), Recipient Profile & Contacts (PROFILE)
  - Data Layer (DB) providing centralized, consent-governed storage for profiles, calendars, documents, messages, and permissions
  - API Gateway & Auth (OIDC) providing authentication and secure API access
  - Notification System (NOTIF) and Logging/Audit (LOG) for telemetry, privacy/compliance tracing
  - User devices (Web/Mobile) interfacing via HTTPS to API Gateway
- Security and privacy guardrails:
  - Role-based access control with consent-driven data exposure
  - Encryption in transit and at rest (baseline)
  - Audit logging and incident response plan
  - Data residency considerations baked into MVP regions, with regulatory readiness planned
- Deployment and telemetry:
  - Web and mobile clients
  - Pilot instrumentation for activation, onboarding friction, engagement, and privacy/compliance telemetry
- Important diagram: see Mermaid Diagram block for high-level component relationships.

### Mermaid Diagram
```mermaid
graph TD
  U[User Devices (Web / Mobile)]
  API[API Gateway & Auth (OIDC)]
  SG[CareSync Services]
  CAL[Calendar Service]
  REM[Reminders Service]
  DOC[Document Storage Service]
  MSG[Messaging Service]
  PERM[Permissions Service]
  PROFILE[Recipient Profile & Contacts]
  DB[Data Layer: Databases + Storage]
  NOTIF[Notification System]
  LOG[Logging & Audit]

  U -->|HTTPS| API
  API --> SG
  SG --> CAL
  SG --> REM
  SG --> DOC
  SG --> MSG
  SG --> PERM
  SG --> PROFILE
  API --> NOTIF
  PROFILE --> DB
  CAL --> DB
  REM --> DB
  DOC --> DB
  MSG --> DB
  PERM --> DB
  NOTIF --> DB
  LOG --> DB
```

## Review Summary

- Final PRD locked for this run; privacy-first MVP scope anchored around core care-coordination features with a 6–8 week pilot (2–3 real families).
- Open questions from prior iterations have been transitioned into the final architecture plan and guardrails; no broad scope changes anticipated.
- Product readiness remains LIMITED due to remaining gaps around regulatory readiness, onboarding design for low-literacy/elderly users, accessibility, and language options; a concrete regulatory plan and low-friction onboarding are required before broader rollout.
- GTM and tech governance continue to emphasize a single MVP pilot with guardrails to prevent scope creep and rapid iteration after pilot learnings.

## Critical Assumptions

- Families will adopt a centralized care coordination tool when privacy and simplicity are demonstrated.
- Users will keep caregiver and contact data up to date and engage with reminders and tasks.
- Privacy controls and consent flows meet expectations across jurisdictions.
- Freemium monetization is viable after initial adoption; agency partnerships can broaden distribution.
- MVP regions can be defined with baseline encryption, consent flows, and incident response plan.

## Requested Changes

- Finalize MVP scope and feature prioritization by a defined date to prevent scope creep.
- Produce regulatory readiness plan for target launch regions, with mitigations and owners.
- Define a low-friction onboarding flow with accessibility considerations and initial language options (English first).
- Clarify data residency, ownership, and consent management across jurisdictions.
- Outline a concrete pricing strategy and monetization thresholds to validate viability in pilot.

## Risks

- Privacy/data protection risks across multiple jurisdictions.
- Low user adoption due to perceived complexity or distrust.
- Compliance delays slowing broader rollout.
- Dependence on users maintaining accurate caregiver and contact data.
- Scope creep beyond MVP boundaries.

## Open Questions

- MVP feature prioritization and scope confirmation.
- Pricing strategy and monetization thresholds to validate viability.
- Privacy and data residency approach across potential launch regions.
- Plan to implement accessibility improvements and language support.

## Why This Could Fail Even With Good Execution

- Privacy or data protection incidents across regions erode trust and block rollout.
- Onboarding friction reduces adoption among non-tech-savvy elder caregivers.
- Regulatory delays or misalignment stall launch timelines.
- Data quality issues undermine perceived value.
- Monetization timing or value realization misaligned with user expectations.

## Technical Readiness

Status: LIMITED

Blocking Gaps:
- [privacy] Data ownership, consent management, and access controls across jurisdictions; baseline encryption plans needed
- [compliance] Clarify country-specific privacy and medical data regulations applicable to MVP regions
- [onboarding] Define minimum viable onboarding flow to reduce friction for elderly users and non-tech-savvy family members

Required Improvements:
- [privacy] Document data model, access controls, and retention policy; implement basic encryption in transit and at rest; define incident response process
- [compliance] Produce a regulatory readiness plan outlining applicable laws and mitigations for target launch regions
- [onboarding] Design and validate a low-friction onboarding flow with accessibility considerations and language options
