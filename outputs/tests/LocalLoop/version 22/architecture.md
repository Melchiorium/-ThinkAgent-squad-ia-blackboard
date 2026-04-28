## Architecture Notes
The decisive technical constraint is **supply integrity in a single neighborhood**: if merchant data, offers, and redemption state are inconsistent, the app will fail as a trust product before personalization matters. The MVP should therefore be built as a **concierge-assisted, single-city, single-neighborhood system** with tightly controlled merchant content and a very small operational surface.

### Macro architecture choice
Use a **mobile app + lightweight admin web console + centralized backend**. Do not build a distributed merchant self-serve platform yet. The backend should own identity, location, merchant profiles, offers, and redemption/loyalty state, while operations manually curate and approve content.

### Structural technical decisions
1. **Manual merchant content management first, self-serve later**  
   Merchant onboarding, profile creation, and offer updates should be administered by internal ops through a console or even database-backed internal tooling. This keeps the data quality high and avoids premature merchant UX complexity.

2. **Deterministic ranking, not ML personalization**  
   Recommend based on proximity, neighborhood, category fit, open status, and a small set of explicit user preferences. This is sufficient to prove discovery value and avoids the cold-start and relevance risks of ML.

3. **Redemption must be simple and auditable**  
   Use a short-lived code, QR check-in, or merchant-staff confirmation flow with an immutable redemption record. Do not rely on freeform “merchant says it happened” state. The app needs a verifiable event ledger for loyalty and support.

### Recommended implementation approach
Build a **single-tenant MVP** for one launch city:
- Mobile app for users
- Admin console for internal ops
- Merchant-facing lightweight access only if necessary for updating one or two fields
- Backend API with a relational database
- Map/location layer for nearby search
- Audit log for offer changes and redemptions

A relational schema is the right default because the core entities are structured and need strong consistency:
- users
- neighborhoods
- merchants
- merchant locations
- offers
- loyalty programs
- redemptions
- favorites/saves
- operational notes/approvals

### What must be built now
- Location-based browse feed for one city and a few neighborhoods
- Merchant profile pages with essential business data
- Offer display and expiration handling
- Category and distance filtering
- Save/favorite
- Loyalty state tracking per merchant
- Redemption recording flow
- Admin console for content curation, approval, and issue resolution
- Basic analytics for opens, taps, saves, redemptions, and active merchants
- Role-based access for internal operators

### What can be handled manually or operationally first
- Merchant recruitment
- Merchant profile creation
- Neighborhood selection
- Offer quality control
- Initial recommendation curation
- Customer support and redemption disputes
- Merchant verification
- Pilot reporting

### Main modules or components
- **Mobile client**
  - location permission
  - neighborhood selection
  - discovery feed
  - merchant profile
  - offer details
  - loyalty progress
  - save/favorite
  - redemption action

- **Backend API**
  - auth/session management
  - user profile and preferences
  - geo query and ranking
  - merchant data
  - offer data
  - loyalty/redemption processing
  - analytics event capture

- **Admin/ops console**
  - merchant creation/editing
  - offer approval and scheduling
  - neighborhood assignment
  - redemption review
  - issue resolution
  - data quality checks

- **Database**
  - authoritative source for merchants, offers, users, redemptions, and audit history

- **Analytics/logging**
  - event tracking for adoption and reliability
  - admin visibility into failed redemptions or stale listings

### Critical data or workflow states
The MVP needs explicit state transitions for trust:
- merchant: pending → verified → active → paused
- offer: draft → approved → live → expired → retired
- loyalty account: active → completed → reset/closed
- redemption: initiated → validated → confirmed → disputed/reversed
- listing freshness: current → stale → removed

These states must be visible in the admin console and enforceable by the backend.

### Minimum reliability, data, permission, or control requirements
- **Role-based access control** for ops vs. merchant vs. end user
- **Audit trail** for all merchant, offer, and redemption edits
- **Geo and location permission fallback** if location is denied: neighborhood selection by manual input
- **Offer expiry enforcement** so stale promotions do not remain visible
- **Duplicate redemption protection** using one-time codes or idempotent redemption records
- **Basic moderation/approval** before any merchant appears live
- **Data freshness checks** for hours, addresses, and offer validity
- **Support escalation path** for redemption disputes

### Control points, internal tools, or support needs
- Internal tool to create and edit merchant listings
- Internal approval queue for offers
- Manual override for redemption disputes
- Content freshness dashboard
- Merchant health view showing last update, live offers, and recent redemptions
- Support notes tied to merchant and user records

### Diagram Blueprint
**Main system blocks**
- Mobile app
- Backend API
- Relational database
- Admin/ops console
- Analytics/event store
- Optional maps/geocoding service

**Main flows between blocks**
- User opens app → mobile app calls backend for nearby merchants
- Backend reads merchant/offer data from database → returns ranked feed
- User views merchant profile → backend logs event
- User saves/favorites or redeems offer → backend writes redemption/loyalty state
- Ops creates/updates merchant and offers in admin console → backend persists changes
- Analytics collects usage and redemption events → ops reviews freshness and performance

**External actors or systems**
- End users
- Internal ops team
- Merchant staff only if needed for redemption confirmation
- Maps/geolocation provider

**Admin or operations control points**
- merchant approval
- offer publication
- redemption dispute handling
- stale listing removal
- neighborhood/feed curation

## Review Summary
The MVP is feasible only if it is treated as a controlled local pilot with manual merchant operations and a strict redemption ledger. The main risk is not feature breadth; it is whether the system can maintain accurate local supply and trustworthy offer state in one city without overbuilding merchant self-service or personalization.

## Critical Assumptions
- One city has enough dense independent business supply to keep the feed active.
- Internal ops can keep merchant and offer data current during the pilot.
- A simple redemption code or confirmation flow is acceptable to merchants.
- Deterministic ranking is good enough to produce relevant results without ML.
- Users will tolerate a concierge-shaped MVP if the discovery loop is reliable.

## Requested Changes
- Define the single launch city and 2–3 initial neighborhoods before implementation. [launch_focus]
- Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]

## Risks
- Inaccurate or stale business/offer data will quickly erode trust. [data_freshness]
- Redemption ambiguity could break loyalty and create support overhead. [redemption_reliability]
- Feed quality may be too weak if neighborhood supply is thin. [supply_validation]
- Manual operations may become the hidden bottleneck even in the pilot. [operations]
- The app may still feel too similar to generic map/search tools if ranking and curation are not disciplined. [user_differentiation]

## Open Questions
- None

## Why This Could Fail Even With Good Execution
Even with solid engineering and operations, the project can fail if one dense neighborhood cannot sustain enough high-quality, frequently updated independent merchants to make the feed feel consistently useful. In that case, the product will look like a thin directory with loyalty hooks, not a trusted local discovery system.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined. [supply_validation]
- The redemption model is not specified tightly enough to guarantee reliable loyalty state. [redemption_reliability]
- The operational ownership model for merchant data updates and dispute handling is still implicit. [operations]

Required Improvements:
- Lock the launch geography and minimum active merchant threshold before build start. [launch_focus]
- Choose one auditable redemption flow and encode it as the only MVP path. [redemption_reliability]
- Define the internal ops workflow and admin permissions for content approval, updates, and support. [ops_tooling]