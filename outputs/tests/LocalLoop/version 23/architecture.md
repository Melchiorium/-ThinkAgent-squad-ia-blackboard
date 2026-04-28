## Architecture Notes
The decisive technical constraint is **merchant supply density and redemption reliability in one city**: if the app cannot keep offers current and prove visits with low-friction merchant confirmation, the MVP will not be trustworthy or repeatable. The simplest viable architecture is a **city-scoped, curated marketplace with semi-manual merchant operations** rather than a fully self-serve platform.

### Macro architecture choice
Use a **mobile-first app + lightweight merchant admin + ops back office** with a single shared backend. Keep recommendations rule-based and inventory curated, not ML-driven. The MVP should behave like a **managed local inventory system** for nearby offers and loyalty stamps.

### Structural technical decisions
1. **Curated supply, not open marketplace**
   - Only approved merchants in one city/neighborhood cluster.
   - No public merchant signup flow until the pilot proves supply quality.
   - Prevents empty inventory and stale listings from undermining trust.

2. **Simple redemption confirmation**
   - Use a merchant-facing confirmation code, QR scan, or one-tap “confirm visit” in an internal merchant web page.
   - Do not build payments or complex fraud scoring in MVP.
   - The redemption proof must be easy for staff to execute in under 10 seconds.

3. **Rules-based recommendation and filtering**
   - Rank by distance, open now, category match, and merchant status.
   - Use only basic preference signals that can be captured at onboarding.
   - This avoids false precision and keeps the system explainable.

### Recommended implementation approach
Build a **single backend service** with:
- authentication/identity
- merchant inventory management
- offer and loyalty state management
- location-based feed generation
- redemption confirmation API
- ops moderation tools

Use a **managed database** for core state, a **geo-indexable query layer** or location fields with indexed radius queries, and a **simple CMS/admin UI** for internal staff to create/update merchants, offers, and verification status. The mobile app should consume only published, verified content.

### What must be built now
- User mobile app with:
  - nearby feed
  - merchant profile
  - offer display
  - loyalty progress display
  - basic account/login or guest-to-account conversion
- Merchant-facing confirmation flow:
  - confirm redemption
  - view merchant offer status
- Internal ops/admin console:
  - create/edit merchants
  - approve and verify merchants
  - publish/unpublish offers
  - correct stale hours/promos
  - resolve disputes or duplicate redemptions
- Backend state management for:
  - merchant status
  - offer status
  - redemption events
  - loyalty stamps/progress
  - audit history

### What can be handled manually or operationally first
- merchant recruitment and initial onboarding
- verification of business legitimacy
- initial offer entry and updates
- neighborhood curation
- quality control of stale or irrelevant listings
- redemption issue resolution
- merchant support and training

### Main modules or components
- **Mobile client**
  - discovery feed
  - merchant detail page
  - redemption view
  - loyalty progress view
- **API backend**
  - auth/session
  - merchant catalog
  - offer catalog
  - loyalty ledger
  - redemption confirmation
  - recommendation query
- **Admin/ops console**
  - merchant approval
  - offer publishing
  - content moderation
  - issue handling
  - audit log
- **Merchant confirmation surface**
  - minimal web page or lightweight merchant mode
  - QR/code confirmation
- **Data store**
  - users
  - merchants
  - locations
  - offers
  - redemptions
  - loyalty state
  - audit events

### Critical data or workflow states
- **Merchant status:** draft → verified → published → suspended
- **Offer status:** draft → active → paused → expired
- **User state:** anonymous → registered → active redeemer
- **Redemption state:** initiated → confirmed → rejected → reversed
- **Loyalty state:** earned stamps → threshold reached → reward available → redeemed
- **Trust state:** verified merchant flag with audit trail

### Minimum reliability, data, permission, or control requirements
- Every published merchant and offer must have a clear owner and timestamp.
- Redemption confirmation must be idempotent to avoid double-stamping.
- Expired offers must auto-hide or be manually suppressible.
- Merchant verification must be recorded by internal staff, not self-asserted.
- Loyalty stamps must be append-only with an audit trail.
- Staff actions in admin must be role-gated and logged.
- The feed must only surface verified, active merchants within the selected city boundary.

### Control points, internal tools, or support needs
- **Internal ops console** for publishing, suspension, and edits
- **Merchant support queue** for failed redemption or disputed visits
- **Audit log** for all offer and loyalty changes
- **Manual refresh mechanism** for stale hours/offers
- **Fraud review path** for duplicate or suspicious redemptions

### Diagram Blueprint
- **Main system blocks**
  - Mobile app
  - Backend API
  - Database
  - Admin console
  - Merchant confirmation page
  - Ops support queue
- **Main flows between blocks**
  - Mobile app → backend: fetch nearby verified merchants and offers
  - Mobile app → backend: user redemption request
  - Merchant confirmation page → backend: confirm/reject redemption
  - Admin console → backend: publish merchants/offers, verify status
  - Backend → database: persist profiles, offers, redemptions, loyalty state
- **External actors or systems**
  - Users
  - Merchant staff
  - Internal ops staff
  - Optional maps/geolocation service
  - Optional push notification service
- **Admin or operations control points**
  - merchant approval
  - offer publish/unpublish
  - loyalty adjustment
  - redemption dispute resolution
  - suspension of bad listings

## Review Summary
The main feasibility challenge is not the app itself but **keeping a city-local inventory of verified merchants, offers, and loyalty redemptions trustworthy enough to use**. The recommended direction is a tightly controlled pilot with curated supply, a simple redemption confirmation flow, and a lightweight ops console rather than a broad self-serve marketplace.

## Critical Assumptions
- One city/neighborhood cluster can supply enough verified merchants to make the feed feel useful.
- Merchant staff will accept a very simple redemption confirmation workflow.
- Manual or semi-manual content operations are affordable for the pilot duration.
- Basic distance/open-now/category ranking is sufficient for early usefulness.
- Loyalty stamps can be managed as a simple ledger without complex rules.

## Requested Changes
- Add an explicit **merchant verification and publishing workflow** with internal approval before any listing goes live. [onboarding]
- Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]

## Risks
- Merchant participation may remain too sparse for the city-scoped feed to feel credible. [supply_density]
- Redemption may be too slow or confusing for merchant staff if the confirmation flow is not extremely simple. [workflow]
- Stale offers or wrong hours could damage trust quickly if ops review is weak. [data_quality]
- Loyalty may not create enough repeat behavior if the reward threshold is poorly chosen. [retention_loop]
- Manual curation could become operationally heavy if the pilot expands beyond one neighborhood. [ops_tooling]

## Open Questions
- What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- What is the pilot city and the maximum geographic boundary for the first feed?
- How will merchant verification be performed and recorded operationally?
- What is the initial loyalty rule: fixed stamp count, per-visit reward, or merchant-specific offer threshold?

## Why This Could Fail Even With Good Execution
Even if the team builds the system correctly, the project can still fail if the city inventory never becomes dense and fresh enough to feel meaningfully better than Google Maps or Yelp. In that case, users will not return, and the loyalty loop will not matter because the discovery layer itself will not earn trust or habitual use.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- City inventory and merchant verification process are not yet operationally defined. [supply_density]
- Redemption confirmation method is not fixed to a single reliable workflow. [workflow]
- Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation. [audit_log]

Required Improvements:
- Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline. [onboarding]
- Choose one redemption mechanism and remove fallback complexity from MVP scope. [workflow]
- Specify immutable redemption and loyalty event storage with admin-only corrections. [audit_log]