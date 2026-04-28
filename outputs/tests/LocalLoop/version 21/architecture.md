## Architecture Notes
The decisive constraint is **quality control for a tiny, trusted supply set**: if freshness, approval, and redemption verification are not explicit and auditable, the MVP will fail as a trust product before it proves discovery value. The simplest viable architecture is a **concierge-operated supply system** with a thin consumer app and an operator admin console; do not build merchant self-serve for MVP.

### Macro architecture choice
- **Consumer mobile app** + **operator/admin web app** + **simple backend API** + **managed database/storage**
- Treat the platform as a **curated neighborhood directory with controlled state**, not as a marketplace
- Use **manual onboarding, manual freshness checks, and operator-approved publishing**
- Keep recommendations **rules-based** and deterministic so changes are explainable and auditable

### Main technical decisions
1. **Single source of truth with operator-controlled publishing**
   - All merchant, offer, and redemption data lives in a central backend database
   - Nothing becomes visible until it passes required validation and operator approval
   - Every change is versioned and logged

2. **One redemption method only**
   - Use a single MVP verification flow such as a **time-boxed redeem code** shown in-app and validated by an operator or merchant confirmation screen
   - No alternate redemption paths, no payments, no complex QR variants, no multiple reward types
   - Redemption state must be deterministic: `issued -> presented -> verified -> consumed` or `expired`

3. **Freshness is a data state, not a content promise**
   - Listings and offers carry freshness metadata: `verified_at`, `expires_at`, `last_checked_at`, `status`
   - Anything stale is auto-hidden or demoted by backend rule
   - Freshness checking remains manual/concierge, but the system enforces visibility automatically

### Recommended implementation approach
- Build the backend as a **modular monolith** with:
  - auth
  - merchant/listing management
  - offers and rewards
  - ranking/feed
  - redemption verification
  - audit log
  - admin actions
- Use a managed relational database for all core entities and audit history
- Use an object store only for images/media if needed
- Use push/email only if absolutely necessary for internal workflows; avoid extra product complexity
- Keep the consumer experience minimal: nearby feed, merchant detail, save, directions, redeem, feedback

### What must be built now
- **Operator approval queue**
  - Required fields check before publish
  - approve/reject/suspend actions
  - reason codes
- **Audit log**
  - immutable record of all merchant, offer, and redemption changes
  - who changed what, when, and why
- **Freshness workflow**
  - required freshness fields
  - manual check cadence
  - stale auto-hide rule
- **Single redemption verification workflow**
  - generate one-use or time-boxed token
  - verify token
  - mark consumed/expired
  - record verifier and timestamp
- **Consumer browse and redemption flow**
  - location-based list/map handoff
  - merchant detail
  - save/favorite
  - basic useful/not useful feedback
- **Admin support controls**
  - suspend listing
  - override stale status in exceptional cases
  - invalidate redemption state when needed

### What can be handled manually or operationally first
- Merchant sourcing and onboarding
- Offer entry and periodic refresh
- Category curation
- Freshness checks
- Customer support and exception handling
- Redemption fallback handling
- Neighborhood supply curation and density management

### Main modules or components
- **Consumer app**
  - location permission
  - nearby feed
  - merchant profile
  - save/favorite
  - directions handoff
  - redeem action
  - feedback signal
- **Admin console**
  - merchant CRUD
  - offer CRUD
  - approval queue
  - freshness review
  - redemption verification oversight
  - suspension/override
  - audit log viewer
- **Backend services**
  - identity/auth
  - listing state engine
  - ranking engine
  - redemption service
  - audit event service
  - notification hooks if needed
- **Database**
  - merchants
  - locations
  - offers
  - freshness checks
  - redemption tokens
  - redemption events
  - user saves
  - feedback
  - audit events

### Critical data or workflow states
- **Merchant status**: `draft -> pending_review -> approved -> live -> stale -> suspended -> archived`
- **Offer status**: `draft -> pending_review -> live -> expired -> revoked`
- **Freshness state**: `fresh -> needs_check -> stale -> hidden`
- **Redemption state**: `issued -> verified -> consumed` or `expired` or `voided`
- **Listing visibility**: computed from approval + freshness + active offer rules
- **Audit trail**: append-only event history for all state transitions

### Minimum reliability, data, permission, or control requirements
- Operator-only permission for publishing, suspending, and overriding freshness
- No public merchant edits in MVP
- Required fields validation before a listing can go live:
  - business name
  - address / geo point
  - category
  - hours
  - contact/admin owner
  - offer or reward text
  - freshness timestamp
  - approval state
- Auto-hide stale records after a defined TTL
- One redemption token must be single-use or time-boxed
- All approvals, edits, and redemptions recorded in immutable audit history
- Support role separated from publish role where possible
- Basic abuse controls:
  - prevent duplicate redemptions
  - prevent manual state edits without audit entry
  - prevent live status without required fields

### Control points, internal tools, or support needs
- **Approval queue** for new merchants and offer changes
- **Freshness dashboard** showing items approaching staleness
- **Redemption monitor** for failed or disputed redemptions
- **Support override panel** with explicit reason logging
- **Audit log review** for incident resolution
- **Manual checklist** for concierge onboarding and freshness checks

### Diagram Blueprint
- **Main system blocks**
  - Consumer mobile app
  - Admin/operator web console
  - Backend API
  - Relational database
  - Audit log store
  - Optional media storage
- **Main flows between blocks**
  - Consumer app -> API -> database for discovery, save, redeem
  - Admin console -> API -> database for approvals, freshness updates, suspension
  - API -> audit log on every state-changing event
  - API -> consumer app for ranked feed and listing status
- **External actors or systems**
  - Merchant provides business details and offer info operationally
  - User shares location and redeems offer
- **Admin or operations control points**
  - approve/reject queue
  - freshness check update
  - stale hide override
  - redemption verification
  - support suspension/restore

## Review Summary
The MVP is only feasible if it is treated as a concierge-controlled supply system with hard freshness rules, one redemption method, and operator approval on every publishable change. Anything more automated or merchant-driven would introduce trust and quality risk before the neighborhood wedge is proven.

## Critical Assumptions
- A small operator team can keep merchant and offer data current enough for one neighborhood
- Users will tolerate a curated supply model if freshness is visibly enforced
- One redemption method is enough to validate repeat behavior
- Operators can reliably handle exceptions and support during the pilot
- The backend can enforce visibility, state transitions, and audit logging without complex workflows

## Requested Changes
- Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Add an **operator-only approval queue** for all merchant and offer changes
- Require an **immutable audit log** for publishing, edits, suspension, and redemption events
- Clarify the **minimum required fields** for a listing to become live

## Risks
- Freshness operations may become too manual to sustain even a narrow pilot [onboarding]
- Single redemption flow may still fail in real-world merchant execution [quality_assurance]
- Operator approval latency could make the experience feel stale [quality_assurance]
- Audit and state logic may be underbuilt, causing trust-breaking inconsistencies [quality_assurance]
- The supply set may remain too small to maintain perceived completeness [supply_density]

## Open Questions
- What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- What is the freshness TTL for a listing before it is hidden?
- Who is allowed to approve, edit, and override supply states?
- What is the minimum merchant data set required before publishing?
- How will disputed or failed redemptions be resolved operationally?

## Why This Could Fail Even With Good Execution
Even with solid implementation, the project can fail if the curated neighborhood supply cannot be kept current enough to feel trustworthy and complete. If operators cannot maintain freshness and redemption consistency at low cost, the product will still collapse into a manual directory that users do not trust or revisit.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- No single, specified redemption verification mechanism with enforced token lifecycle [quality_assurance]
- No explicit freshness-control policy with stale visibility rules and required check cadence [quality_assurance]
- No operator-only approval and immutable audit workflow defined for supply changes [quality_assurance]

Required Improvements:
- Define one redemption flow and enforce single-use or time-boxed state transitions [quality_assurance]
- Specify freshness TTL, check cadence, and auto-hide logic for stale listings [quality_assurance]
- Add operator approval queue plus append-only audit logging for every merchant and offer change [quality_assurance]