## Architecture Notes
The main technical constraint is not discovery UI, it is trustworthy content control: every merchant, offer, and redemption must pass through an ops-controlled workflow before users can act on it. For this MVP, the safest architecture is a concierge pilot with a single backend of record, a mobile client, and a lightweight admin console. Do not build a self-serve marketplace yet.

Three structural decisions should shape the MVP:
1. **Admin-first publishing model**: no merchant or offer can appear in the app until it is reviewed and approved by ops.
2. **Canonical redemption state machine**: redemption must move through fixed states so support can resolve disputes consistently.
3. **Manual ranking overrides with simple rules**: use geolocation plus ops-curated ordering instead of automated recommendation logic.

Recommended implementation approach:
- Mobile app for users with location permission, a small feed of verified nearby merchants, merchant profile pages, offer display, loyalty marker, and redemption initiation.
- Backend API as the single source of truth for merchant, offer, redemption, and audit data.
- Admin web console for verification, moderation, publish approval, suspension, re-verification, ranking override, and support actions.
- Relational database for stateful records and audit logging; avoid complex event streaming or ML services.
- Object storage only for merchant images and static assets.

What must be built now:
- Merchant verification workflow with verify / re-verify / suspend / reactivate states
- Ops moderation queue for all merchant profile and offer submissions
- Publish gate so no content is visible without approval
- Nearby discovery endpoint with a limited sorted list
- Merchant profile page
- One offer per merchant
- One loyalty action
- Redemption initiation and redemption recording
- Dispute and void handling
- Admin audit log with reason codes
- Manual ranking override tool
- Basic support view for redemption status and merchant lifecycle state

What can be handled manually or operationally first:
- Merchant recruitment and onboarding setup
- Offer creation and refresh
- Content quality checks on photos and descriptions
- Customer support for redemption issues
- Neighborhood supply balancing
- Merchant follow-up and renewal conversations
- Initial ranking curation

Main modules or components:
- **User app**: discovery, profile view, offer view, redemption flow, loyalty display
- **Merchant data service**: merchant profile, location, hours, category, verification state
- **Offer service**: one active offer per merchant, approval status, publish state
- **Redemption service**: redeem, void, dispute, support resolution
- **Moderation service**: submission review queue, approval/rejection/suspension, reason codes
- **Admin console**: verification, publish controls, overrides, audit inspection
- **Audit log**: immutable record of admin actions and content changes
- **Support view**: lookup by merchant, user, or redemption ID

Critical data or workflow states:
- Merchant lifecycle: `draft -> submitted -> verified -> published -> suspended -> re_verify_pending -> re_verified -> reactivated`
- Offer lifecycle: `draft -> submitted -> approved -> active -> paused -> rejected -> retired`
- Redemption lifecycle: `initiated -> redeemed -> disputed -> voided -> resolved`
- Moderation decision: `pending -> approved/rejected/suspended`
- Ranking state: `default_ranked -> manually_overridden`

Minimum reliability, data, permission, or control requirements:
- Role-based access control for ops/admin/support
- Reason code required on every approval, rejection, suspension, void, and override
- Immutable audit log for all state transitions
- Idempotent redemption endpoints to avoid double redemption
- Duplicate protection for merchant and offer submissions
- Visibility rules enforced server-side, not in the client
- Basic tamper resistance for redemption records
- Clear timezone and location storage for neighborhood filtering

Control points, internal tools, or support needs:
- Review queue for moderation and verification
- Support console for redemption lookup and resolution
- Manual override tool for ranking and publishing
- Merchant suspension and re-verification workflow
- Audit log viewer for all administrative actions

Diagram Blueprint
- Main system blocks:
  - Mobile app
  - Backend API
  - Merchant/offer database
  - Redemption state service
  - Moderation and admin console
  - Audit log store
- Main flows between blocks:
  - Merchant submitted -> moderation queue -> approved -> published to app
  - User discovers merchant -> views offer -> initiates redemption -> redemption recorded
  - Support reviews redemption -> dispute/void/resolution state updated
  - Ops applies verification/suspension/ranking override -> audit log written
- External actors or systems:
  - User
  - Merchant
  - Ops/admin/support
  - Maps/geolocation provider
- Admin or operations control points:
  - Approve/reject/suspend
  - Publish/unpublish
  - Verify/re-verify
  - Void/dispute resolution
  - Ranking override

## Review Summary
The feasibility risk is not building the app; it is controlling quality and trust with a very small ops team. The right direction is a concierge MVP with strict admin review, a single redemption state machine, and manual curation until the pilot proves reliable behavior.

## Critical Assumptions
- Ops can review merchant and offer submissions fast enough to avoid launch delays
- A single neighborhood and one category can be kept dense enough to feel useful
- Merchants will accept a simple redemption process without custom integrations
- The team can enforce server-side publish and redemption controls reliably
- Manual curation plus basic ranking is sufficient for pilot discovery quality

## Requested Changes
- Add one explicit moderation workflow that blocks all submissions until reviewed and approved by ops [moderation_workflow]
- Define the canonical redemption state machine with dispute and void paths [state_machine]
- Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Require reason codes and audit logging for every admin decision [audit_log]
- Specify a support resolution screen or workflow for redemption disputes [support_workflow]

## Risks
- Merchant or offer quality slips if moderation is not consistently applied [quality_assurance]
- Redemption disputes damage trust if state transitions are ambiguous [state_machine]
- Ops turnaround becomes the bottleneck if the queue is too manual [operations_bottleneck]
- Manual ranking may mask weak product relevance until later [manual_curation]
- Server-side visibility rules may be bypassed if publish logic is not centralized [access_control]

## Open Questions
- What exact fields are required for merchant submission review?
- What evidence is needed to mark a merchant verified?
- What are the allowed redemption proof methods at the point of use?
- Who on the team can resolve disputes and void redemptions?
- What is the maximum review turnaround time acceptable for pilot operations?

## Why This Could Fail Even With Good Execution
Even if the team ships cleanly, the project can still fail if one neighborhood does not produce enough high-quality, repeatable merchant density. In that case, the app will feel curated but not essential, and the controlled workflow will simply slow down access to insufficient supply.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish [moderation_workflow]
- No canonical redemption/dispute state machine defined for reliable support handling [state_machine]
- No explicit role model for who can verify, suspend, reactivate, or override merchant ranking [rbac]

Required Improvements:
- Implement a review queue with approve/reject/suspend actions and required reason codes [moderation_workflow]
- Define and implement redemption states including dispute and void paths in the backend [state_machine]
- Add re-verification and suspension controls for merchant lifecycle management [state_machine]
- Restrict admin actions through role-based permissions and log all actions immutably [rbac]