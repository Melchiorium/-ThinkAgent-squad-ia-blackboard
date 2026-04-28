## Go-To-Market Notes
- **Main market bottleneck:** trust plus behavior change. Families already have a functional if messy coordination stack (WhatsApp, calls, calendars). The product only gets credible early proof if it can replace a small but painful slice of that workflow fast enough that the coordinator feels immediate relief.
- **Side of the market to secure first:** the **family coordinator / remote adult child** side first. They are the only side likely to set up the space, invite others, and keep the pilot moving. Do not start with caregivers or agencies as the acquisition wedge.
- **Structural GTM decisions:**
  1. **Sell a single-family pilot for one elder, not a platform.** One care recipient, one coordinator, one invited caregiver if needed.
  2. **Founder-led, concierge-first launch.** The first motion is not self-serve marketing; it is direct outreach plus assisted setup.
  3. **Position as “shared care coordination record,” not eldercare management.** Narrow promise: reduce missed handoffs, unclear ownership, and repeat chasing.
- **Initial target audience:** remote adult children in the US/English-speaking markets who manage one parent’s care with 2–4 family participants and possibly one outside caregiver.
- **Positioning:** “A private shared workspace for one parent’s care coordination so siblings and caregivers stop relying on scattered texts, calls, and notes.”
- **First acquisition motion:** founder-led outbound to a tightly defined list of prospective coordinators, sourced from personal network, caregiver communities, parent-care forums, and referral from local elder care advisors. The CTA is a **2-week concierge pilot**, not a generic signup.
- **Operating assumptions for the first acquisition motion:**
  - Target users already feel coordination pain weekly, not occasionally.
  - The coordinator can name the other participants and will invite them.
  - At least one other person will post updates if the flow is simple and the founder helps launch it.
  - Reminder delivery and access control must work visibly enough that users trust the space.
  - A pilot can be run with manual help behind the scenes.
- **Switching trigger:** missed appointments, repeated reminder chasing, or unclear responsibility across 3+ people. If the family says “we need one place to know what happened and who owns the next step,” that is the conversion moment.
- **First activation loop:** coordinator creates one care space → invites siblings/caregiver → adds 3–5 recurring items or recent events → reminder/update is posted → someone else confirms or completes a task → coordinator sees the updated shared record.
- **What must exist before public launch:**
  - Invite-only access for one care recipient
  - Role-based permissions for coordinator, family member, caregiver
  - Reminder delivery with visible status/failure handling
  - Structured updates tied to tasks/events
  - Basic audit trail for sensitive actions
  - Manual onboarding flow that gets families live quickly
- **What must be productized now vs manual during pilot:**
  - **Productized now:** invitation flow, permission model, shared care space, reminders, structured updates, task/event status, access review, audit log, revocation.
  - **Manual during pilot:** setup, participant onboarding, migration from chat/paper, reminder rescue, troubleshooting, coaching the coordinator.
  - **Deferred:** chat replacement, agencies, multi-recipient support, integrations, compliance automation, analytics, marketplace features.

## Review Summary
The main launch challenge is not feature completeness; it is whether one coordinator will consistently move part of an existing care workflow out of chat and into a new shared record. The recommended GTM direction is a founder-led concierge pilot aimed at remote adult children managing one elder, with a very narrow promise and a measured loop around invitations, reminders, and structured updates.

## Build Vs Pilot Operations

### Must Be Productized Now
- One care space per elderly relative
- Invite-only access
- Fixed role-based permissions
- Reminder delivery with status visibility
- Structured task/event updates
- Access review on activation
- Basic audit logging
- Revocation of access
- Emergency contact list
- Basic secure document upload

### Can Stay Manual Or Operational During Pilot
- Founder-led acquisition and outreach
- Concierge onboarding and setup
- Mapping existing WhatsApp/text/paper workflows into the product
- Coordinating the first invite set
- Reminder follow-up if delivery fails
- Troubleshooting permissions and access issues
- Coaching families on how to use the shared record
- Monitoring participation and prompting the first update loop

### Deferred Until After Proof
- Native chat
- Multi-recipient support
- Agency dashboards
- Organization hierarchy
- External integrations
- Billing and payments
- AI features
- Advanced compliance tooling
- Marketplace or service booking
- Granular custom permissions

## Critical Assumptions
- Remote adult children feel enough pain to try a new tool for one parent’s care.
- The coordinator can and will bring the rest of the family into the workflow.
- At least one non-coordinator participant will post updates when the flow is simple.
- A fixed permission model is trusted enough for early sensitive sharing.
- A concierge pilot can create enough value before users revert to WhatsApp.

## Requested Changes
- Add one explicit primary acquisition motion: founder-led outbound into a concierge pilot. [market_motion]
- Define the smallest launch audience as remote adult children coordinating one parent with 2–4 other participants. [market_motion]
- Specify reminder channels and visible failure handling before pilot launch. [operations]
- Clarify the first activation loop as invite → add 3–5 items → receive update → confirm completion. [metrics_validation]
- Tighten the positioning to “shared care coordination record” and avoid broader eldercare platform language. [demand_validation]

## Risks
- Families keep using WhatsApp because it remains faster and socially embedded. [demand_validation]
- Caregivers do not consistently post updates. [metrics_validation]
- Privacy concerns reduce willingness to invite others. [privacy_trust]
- The coordinator is willing to try it but not to sustain it weekly. [metrics_validation]
- The product is seen as too narrow unless it solves a concrete coordination failure immediately. [demand_validation]

## Open Questions
- Which reminder channels will be used in the pilot: SMS, email, push, or all three? [operations]
- What is the minimum number of participants needed for a family to feel the product is useful? [metrics_validation]
- What exact family pain signals best predict conversion to pilot? [demand_validation]
- How often do non-coordinators need to post for the product to feel “alive”? [metrics_validation]
- What trust proof is required before a family will share sensitive documents? [privacy_trust]

## Why This Could Fail Even With Good Execution
Even with strong onboarding and reliable reminders, the product can fail if the family still experiences WhatsApp plus calls as the faster and more emotionally natural place to coordinate. In that case, the team may execute well on the pilot but still not displace enough of the existing workflow to justify habitual use.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- No explicit primary acquisition motion tied to a defined launch audience. [market_motion]
- Reminder channels and failure handling are not specified for pilot reliability. [operations]
- The smallest credible activation threshold is not yet precise enough to judge whether the pilot is working. [metrics_validation]

Required Improvements:
- Define founder-led outbound as the first acquisition motion and limit it to remote adult children coordinating one parent. [market_motion]
- Specify the reminder delivery path and what users see when delivery fails. [operations]
- Set a concrete launch threshold for first activation and weekly participation in the pilot. [metrics_validation]