## Architecture Notes
The main technical constraint is **trustworthy, low-friction merchant redemption in the real world**. If redemption is ambiguous, slow, or easy to game, the MVP cannot prove value to either side. The simplest viable architecture is a **curated single-city marketplace with manual merchant onboarding and a controlled redemption code flow**, not an automated local commerce platform.

Three structural decisions should shape the MVP:
1. **Curated supply, not open marketplace ingestion**: only admin-approved merchants can appear in the app. No self-serve public listings at launch.
2. **Deterministic redemption, not “visit inference”**: use a simple merchant-facing confirmation method such as a rotating code, one-time QR, or staff tap-to-confirm. Avoid GPS-based redemption validation as the primary mechanism.
3. **Rules-based feed, not personalization**: start with location + category + manual curation + simple ranking rules. “Personalized recommendations” should be limited to a few explicit user preferences, not an ML recommender.

Recommended implementation approach:
- Build a **mobile consumer app** plus a **lightweight merchant/admin web console**.
- Store all businesses, offers, redemptions, and loyalty events in one backend with strong state tracking.
- Use a single city / neighborhood boundary and a small number of categories.
- Keep merchant onboarding operationally assisted; the system should support it, but not require full automation.
- Instrument every key event: app open, location grant, feed impression, profile view, navigation tap, save, redemption attempt, redemption success, repeat visit marker.

What must be built now:
- Consumer app:
  - location permission + neighborhood detection
  - curated nearby business feed
  - merchant profile page
  - offer display
  - save / navigate / redeem actions
  - basic loyalty status display
- Merchant/admin console:
  - create/edit merchant profile
  - create one active offer/reward
  - view redemption logs
  - confirm or reverse a redemption if needed
- Backend:
  - merchant and offer data model
  - redemption state machine
  - minimal user account identity
  - event logging and audit trail
  - admin approval workflow for listings
- Operational tooling:
  - manual merchant review queue
  - support tooling for redemption disputes
  - curation controls for which merchants appear in feed

What can be handled manually or operationally first:
- merchant recruiting and onboarding
- business verification
- copywriting / photo cleanup
- feed curation and ranking
- dispute resolution for redemptions
- initial neighborhood boundary selection
- offer quality review and removal of low-value listings

Main modules or components:
- Consumer mobile app
- Merchant/admin web console
- Authentication and identity service
- Merchant catalog service
- Offer/reward service
- Redemption service
- Loyalty ledger
- Curation/feed service
- Analytics/event tracking pipeline
- Support/admin audit tools

Critical data or workflow states:
- Merchant: draft -> verified -> approved -> active -> paused -> removed
- Offer: draft -> active -> expired -> disabled
- User: anonymous -> identified -> location-permitted -> engaged
- Redemption: initiated -> presented -> confirmed -> settled -> disputed/reversed
- Loyalty: earned -> available -> redeemed -> expired
- Feed item: eligible -> ranked -> shown -> clicked -> acted on

Minimum reliability, data, permission, or control requirements:
- Explicit user consent for location access
- Merchant approval before listing
- Audit log for all merchant profile and offer changes
- Idempotent redemption confirmation to prevent double counting
- Role-based access for admin vs merchant users
- Basic fraud controls: one redemption per code/event, timestamped confirmation, manual exception handling
- Data retention policy for location and behavioral data, even if minimal
- Ability to disable a merchant or offer immediately

Control points, internal tools, or support needs:
- Admin review queue for merchant approval
- Merchant dispute resolution view
- Feed override/curation tool
- Offer expiration and pause controls
- Manual replay of failed redemption events
- Support notes tied to merchant and redemption records

Diagram Blueprint
- Main system blocks: Consumer App, Merchant/Admin Console, Backend API, Merchant Catalog DB, Redemption/Loyalty Service, Event Tracking, Support/Operations Tooling
- Main flows between blocks: App requests nearby merchants -> Backend returns curated feed -> User views merchant and taps redeem -> Redemption Service records event -> Merchant Console confirms redemption -> Loyalty Service updates state -> Event Tracking logs actions
- External actors or systems: consumer users, merchant staff, internal ops/admin users, mobile OS location permissions
- Admin or operations control points: merchant approval queue, feed curation overrides, offer activation/pausing, redemption dispute review

## Review Summary
The MVP is feasible only if LocalLoop is built as a curated, controlled local marketplace with manual supply operations and a deterministic redemption flow. The biggest challenge is not the mobile app—it is proving a reliable merchant-side redemption loop and keeping the feed relevant without an overbuilt recommendation system.

## Critical Assumptions
- A small number of approved merchants in one dense area can create enough useful supply.
- Merchants will accept a simple confirmation flow at the point of redemption.
- Manual curation can maintain acceptable relevance for the pilot.
- Basic location-based ranking plus category filters is sufficient for the first proof.
- The team can operate onboarding and dispute resolution with lightweight internal tooling.

## Requested Changes
- Replace “personalized recommendations” with explicit location + category + curated ranking for MVP [recommendation_scope]
- Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]

## Risks
- Redemption may be too awkward for merchant staff, causing unreliable proof [redemption_flow]
- Feed quality may degrade if curation is inconsistent or supply is thin [market_motion]
- Merchant onboarding may require more manual effort than the team can sustain [ops_load]
- Location permissions or geofencing may be unreliable enough to harm the core flow [location_permission]
- Loyalty or offer abuse may appear if the redemption state machine is too loose [fraud_control]

## Open Questions
- What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- What minimum merchant data is required for approval and listing?
- Is the first experience restricted to one neighborhood, or one city with multiple neighborhoods?
- What is the exact definition of a “repeatable action” for proving value: save, navigate, redeem, or return visit?

## Why This Could Fail Even With Good Execution
Even with solid engineering and operations, the project can fail if merchants do not find the redemption workflow simple enough to use during normal service, or if the curated feed still feels less useful than existing maps and review tools. In that case, the app becomes a thin wrapper around local listings rather than a better discovery and conversion system.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- The redemption mechanism is not defined tightly enough to build a reliable proof loop [redemption_flow]
- The MVP recommendation model is too broad for the available supply and operations model [recommendation_scope]
- Merchant approval and listing controls need a concrete state model before implementation [merchant_verification]

Required Improvements:
- Select one deterministic redemption method and make it the only supported MVP path [redemption_flow]
- Replace advanced personalization with rules-based curation and explicit user filters [recommendation_scope]
- Define merchant lifecycle states, approval rules, and immediate disable controls [merchant_verification]