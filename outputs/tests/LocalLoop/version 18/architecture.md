## Architecture Notes
The main technical constraint is not the mobile app itself; it is **supply quality and trustworthiness of listings/offers**. If merchant data is stale, sparse, or inconsistent, the feed will fail regardless of recommendation quality. The MVP should therefore use a **concierge-first, content-controlled architecture** with a lightweight consumer app backed by an admin-curated merchant system.

Three structural decisions should shape the MVP:
1. **Centralized content control over merchant self-serve**: all listings, offers, and profile edits should flow through an internal admin tool first. This avoids low-quality supply and prevents broken or misleading offers.
2. **Rule-based personalization, not ML**: use location + a small preference profile + simple ranking rules. This is sufficient for proof and far easier to explain, tune, and debug.
3. **Redemption tracking via controlled tokens or check-in states**: do not build a full wallet or points engine. Track offer redemption with a simple state change that can be verified by merchant or admin.

Recommended implementation approach:
- Build a mobile-first consumer app with authenticated or anonymous user sessions.
- Back it with a simple backend API and relational database.
- Use an internal admin console for merchant CRUD, offer publishing, curation, and analytics review.
- Store location, category, offer status, and engagement events in structured tables.
- Use geospatial queries only at neighborhood/city MVP scale; do not over-engineer search or recommendation infrastructure.
- Keep merchant onboarding semi-manual: businesses can submit details, but internal ops approves, cleans, and publishes them.

What must be built now:
- Consumer feed showing nearby independent businesses
- Merchant profile pages
- Basic preferences capture
- Save/favorite action
- Active offer display
- Basic redemption event creation and attribution
- Admin tool for merchant/listing/offer management
- Simple analytics dashboard for views, saves, redemptions, and feed health
- Audit trail for edits to merchant data and offer status

What can be handled manually or operationally first:
- Merchant sourcing and onboarding
- Writing descriptions and cleaning business data
- Offer creation and expiration management
- Supply curation by neighborhood/category
- Quality control and removal of stale listings
- Merchant support and redemption disputes
- Initial personalization tuning and feed balancing

Main modules or components:
- Consumer mobile app
- Backend API
- Database with geospatial and event tables
- Internal admin console
- Content moderation/approval workflow
- Analytics/event logging pipeline
- Optional merchant-facing lightweight view later, but not required for MVP

Critical data or workflow states:
- Merchant: submitted → approved → published → paused/removed
- Offer: draft → active → expired → archived
- User preference: captured → updated
- Favorite: created → active → removed
- Redemption: initiated → verified/recorded → disputed if needed
- Listing freshness: current → needs review → stale/hidden

Minimum reliability, data, permission, or control requirements:
- Only approved merchants/offers can be visible to users
- Every public listing must have a last-reviewed timestamp
- Offers must have start/end dates and explicit active status
- Admin actions must be role-controlled and logged
- Redemptions must be traceable to a specific offer and user event
- Location handling must be consented and minimally stored
- Basic abuse controls to prevent duplicate redemptions or fake listings

Control points, internal tools, or support needs:
- Admin review queue for new merchants and edits
- Manual override to hide stale or problematic offers instantly
- Support screen to look up user redemption history
- Merchant contact record for issue resolution
- Lightweight content QA checklist before publishing

### Diagram Blueprint
- Main system blocks:
  - Mobile app
  - Backend API
  - Relational database
  - Admin console
  - Analytics/event store
  - Optional geocoding/location service
- Main flows between blocks:
  - User location/preferences → backend → ranked nearby listings → mobile app
  - Admin creates/edits merchants/offers → backend/database → consumer feed
  - User saves/redeems → backend → event store/database → analytics/admin view
- External actors or systems:
  - Consumer users
  - Merchant contacts
  - Mapping/geolocation service
- Admin or operations control points:
  - Listing approval
  - Offer publish/pause
  - Freshness review
  - Redemption dispute handling
  - Feed quality monitoring

## Review Summary
The biggest feasibility challenge is not building discovery, but keeping the local supply accurate, curated, and trustworthy enough to sustain a usable feed. The safest MVP is a centrally controlled, concierge-operated system with simple ranking and strict admin governance rather than a merchant self-serve platform.

## Critical Assumptions
- A small set of curated merchants in one neighborhood can make the feed feel useful.
- Manual curation and approval can keep offer quality high enough for pilot use.
- A simple rule-based ranking approach is sufficient for initial personalization.
- Redemptions can be tracked credibly without a full loyalty or payment system.
- Internal operations capacity exists to keep listings current and resolve disputes.

## Requested Changes
- Define a strict merchant approval workflow with publish/pause/expire states before build [workflow_control]
- Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]

## Risks
- Stale or inaccurate offers could quickly destroy trust [data_freshness]
- Merchant supply may be too thin to produce a credible feed [merchant_supply]
- Duplicate or fraudulent redemption events may distort value measurement [fraud_control]
- Manual curation workload may exceed pilot capacity [ops_load]
- User privacy or consent handling around location may be too weak if not designed carefully [privacy_control]

## Open Questions
- What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- What minimum merchant data is required for a listing to be publishable?
- Who is responsible for ongoing freshness checks and how often must they happen?
- What is the smallest credible neighborhood scope for the first pilot?

## Why This Could Fail Even With Good Execution
Even with solid engineering and operations, the project can fail if users do not perceive enough unique value versus Google Maps, Yelp, or social discovery. If the feed does not consistently surface better nearby options and real offers, the app becomes another local directory with higher maintenance cost and no lasting habit.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- Redemption verification is not defined well enough to build a trustworthy MVP [redemption_tracking]
- Listing freshness and approval controls are not yet specified tightly enough for safe publication [data_freshness]
- The MVP still implies personalization beyond what should be built first [rule_based_logic]

Required Improvements:
- Choose one simple redemption mechanism and make it auditable [redemption_tracking]
- Add mandatory admin approval, expiry, and stale-item suppression rules [workflow_control]
- Constrain personalization to deterministic preference and proximity ranking for the pilot [rule_based_logic]