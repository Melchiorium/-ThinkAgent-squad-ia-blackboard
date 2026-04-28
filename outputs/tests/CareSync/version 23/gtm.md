## Go-To-Market Notes
- **Main market bottleneck:** trust + behavior change, not feature completeness. CareSync will not win because it has more coordination features; it wins only if one exhausted family coordinator is willing to move real coordination out of chats/spreadsheets and let others participate without friction.
- **Side of the market to secure first:** the **family coordinator** side first. If the primary adult child does not adopt and actively maintain the space, caregivers and relatives will not have a reason to join.
- **Structural GTM decisions:**
  1. **Founder-led concierge pilot first, not self-serve launch.** The product is too trust-sensitive and workflow-specific for broad public acquisition.
  2. **Email-first only for pilot activation.** Do not solve notification-channel breadth yet; it adds support burden and does not validate the core switching problem.
  3. **One elder, one coordinator, small invited circle.** Start with the smallest coordination unit that can actually create repeated use.
- **Initial target audience:** adult children in their 30s–60s coordinating care for **one aging parent living at home or mostly at home**, especially when siblings or one external caregiver are involved.
- **Positioning:** “A private shared care space for one family to coordinate tasks, appointments, and updates for one parent without losing track in texts and calls.”
- **First acquisition motion:** founder-led outreach into caregiver-adjacent networks and warm referrals from people already exposed to elder-care stress: local caregiving communities, home-care agency contacts, elder-care support groups, and personal introductions from pilot families. The motion should recruit the coordinator, not the whole family.
- **Operating assumptions for the first acquisition motion:**
  - The coordinator is reachable through warm intros or referral-heavy channels, not mass marketing.
  - A concise promise of reduced coordination stress is enough to get pilot conversations.
  - The first users will tolerate white-glove setup if the setup burden is low.
  - Email notifications are sufficient for a credible pilot.
  - At least some families already feel acute coordination pain.
- **Switching trigger:** missed follow-through, repeated status-chasing, sibling coordination conflict, or an overwhelmed primary caregiver who is already using chat/spreadsheets and wants a single source of truth.
- **First activation loop:** coordinator creates the care space → invites 2–4 participants → adds the next appointments/tasks/reminders → participants receive email and confirm access → someone marks a task complete or posts an update → coordinator sees fewer status-chasing pings and keeps the space active.
- **What must exist before public launch:**
  - invite-only shared care space for one elder
  - coordinator-first setup
  - task/reminder tracking
  - participant access via email
  - simple activity/status view
  - coarse permissions and revocation
  - visible privacy notice and consent gate
  - audit trail for key actions
  - a defined launch geography and minimum compliance baseline
- **What must be productized now:** the shared care space, invites/consent, task and reminder tracking, activity/status view, permissions, revocation, audit log, email notifications, and basic document upload/view only if it is needed for coordination.
- **What can stay manual during the pilot:** onboarding, role setup, support, notification troubleshooting, edge-case handling, and feedback collection.
- **What should stay deferred:** SMS, native mobile apps, rich messaging, multi-elder support, caregiver marketplace/workforce features, integrations, AI summaries, and public self-serve launch.

## Review Summary
The launch challenge is not building a bigger care platform; it is proving that one overwhelmed family coordinator will actually switch a real care workflow out of chat and into a dedicated shared space. The right direction is a founder-led, concierge pilot aimed at adult children coordinating one parent, with email-only delivery and a very narrow activation loop.

## Build Vs Pilot Operations

### Must Be Productized Now
- One elder care space
- Invite-based access
- Consent on invite acceptance
- Shared task list
- Appointment and reminder tracking
- Simple status/activity feed
- Coarse role permissions
- Access revocation
- Audit log for key actions
- Email notifications
- Privacy notice
- Limited document upload/view only if required for coordination

### Can Stay Manual Or Operational During Pilot
- Concierge onboarding
- Setup help for family roles and tasks
- Human support for invite issues
- Manual handling of edge cases
- Pilot feedback interviews
- Founder-led follow-up with inactive families

### Deferred Until After Proof
- SMS notifications
- Native mobile apps
- Rich in-product messaging
- Advanced permission hierarchies
- Multi-elder households
- Agency marketplace or matching
- EHR, calendar, pharmacy, or payer integrations
- AI-generated summaries or care plans
- Elder-first onboarding
- Country expansion

## Critical Assumptions
- Adult children coordinating one parent feel enough pain to switch from chat/spreadsheets.
- A small invite-only family workspace is sufficient to create repeat use.
- The primary coordinator can recruit the rest of the participants with minimal friction.
- Email-only notifications are enough for the pilot audience.
- Trust can be established through clear consent, permissions, and revocation.
- Concierge setup is acceptable during pilot and does not invalidate the product test.

## Requested Changes
- Clarify the launch motion as **founder-led concierge pilot** for adult children coordinating one parent. [market_motion]
- Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]
- Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]
- Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]

## Risks
- Families may agree in principle but still keep using group chats for real coordination. [demand_validation]
- Trust concerns may block invite acceptance, document sharing, or permissions use. [privacy_trust]
- Email-only notifications may be insufficient for some families, reducing engagement. [market_motion]
- The product could drift into generic task management instead of care-specific coordination. [scope]
- Concierge support may mask weak product pull if the pilot is not measured tightly. [demand_validation]

## Open Questions
- Which exact launch geography will be used for the pilot? [compliance]
- What minimum compliance posture is required for that geography? [compliance]
- Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]
- What is the minimum acceptable retention threshold for deciding the workflow is sticky enough to continue? [demand_validation]
- Will families tolerate document sharing in the pilot, or should documents remain optional and secondary? [privacy_trust]

## Why This Could Fail Even With Good Execution
Even with strong concierge execution, the project can fail if the market still defaults to chat and phone coordination because the perceived switching cost is higher than the pain of staying fragmented. If the coordinator does not feel a sharp enough before/after improvement in coordination burden, CareSync will look like “another tool” instead of a necessary operating layer.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- The first launch audience and acquisition motion are still too broad for a credible pilot [market_motion]
- The pilot notification strategy is not fully locked to the lowest-support path [market_motion]
- The smallest proof of switching behavior is not defined as a measurable activation event [demand_validation]

Required Improvements:
- Commit to a founder-led concierge pilot focused on adult children coordinating one parent, sourced through warm referrals and caregiver-adjacent outreach [market_motion]
- Lock the pilot to email-first delivery and defer SMS until the pilot proves it is necessary [market_motion]
- Define a single activation threshold: one coordinator plus 2–4 invited participants completing a real task or appointment workflow in the shared space [demand_validation]