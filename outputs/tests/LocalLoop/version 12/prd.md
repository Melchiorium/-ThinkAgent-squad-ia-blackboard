# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local independent businesses still default to large platforms because local discovery is fragmented, hard to trust, and inconvenient to act on in one place. Independent businesses need a low-cost way to get discovered by nearby customers and bring them back again, but they cannot rely on broad ad tools or complex marketing systems.

The MVP must prove one narrow outcome: a person who lives or works in the launch neighborhood can find a relevant nearby independent coffee or lunch spot, redeem one simple offer, and have that visit recorded reliably enough to support a repeat-visit loop.

## Initial Wedge
One dense neighborhood in one city, focused on two repeat-visit categories:

- coffee shops
- lunch / casual food spots

The wedge is a curated nearby feed, not a broad local commerce marketplace. It is narrow enough to test merchant supply, user interest, redemption behavior, and repeat usage without competing head-on with horizontal discovery platforms.

## First Target User
People who live or work in the launch neighborhood and make frequent coffee or lunch purchases.

Why this segment first:
- high frequency, repeatable use case
- easy to reach inside one dense area
- more likely to respond to simple neighborhood offers
- more likely to repeat if the experience is faster than checking existing apps

Broader audiences like families, tourists, and citywide users are deferred until the core loop is proven.

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- merchant punch cards or loyalty apps
- neighborhood newsletters and deal sites

Switching trigger:
- users want a faster, more curated way to find nearby independent coffee or lunch options than checking multiple existing apps
- merchants want visibility to nearby customers without buying broad ads or managing complex tools

LocalLoop does not need to replace general search or review platforms in the MVP. It only needs to be faster and more relevant for the narrow launch use case.

## Core MVP Workflow
1. User opens the app and allows location access.
2. App shows a curated feed of approved independent businesses within the launch neighborhood, ranked by location, category match, and manual curation.
3. User filters by coffee or lunch.
4. User opens a merchant profile with a short description, location, and one active offer.
5. User saves the place, gets directions, or shows a single redemption code in-store.
6. Merchant verifies the redemption through the same code flow.
7. If the merchant has a loyalty offer, the visit is recorded as a simple ledger event.

The workflow must prove that LocalLoop can surface relevant nearby businesses and support one reliable first conversion action.

## In Scope
- one-neighborhood launch
- two launch categories: coffee and lunch / casual food
- curated nearby feed of approved independent businesses
- rules-based ranking using location, category match, and manual curation
- merchant profile pages
- one simple offer per merchant
- one supported redemption mechanism only
- basic loyalty ledger tracking as visit count / stamp history
- save and navigate actions
- merchant approval state before listing
- merchant onboarding for a limited pilot set
- minimal quality controls to exclude unverified or low-value listings
- anonymous browsing with optional sign-in only if needed for loyalty recording

## Out of Scope
- citywide or multi-city expansion
- broad coverage across all local business types
- event feed as a launch feature
- reviews
- social sharing features
- advanced personalization
- multiple redemption methods
- automated merchant campaign tools
- sponsored ranking or bidding systems
- deep analytics suites
- full payments, wallet, or financing features
- reservations, delivery, or booking flows
- consumer community features

## MVP Build Vs Pilot Operations
### Must Build Now
- location-based curated feed for the launch neighborhood
- approved merchant profile pages
- one supported redemption mechanism
- basic loyalty ledger
- save and navigate actions
- merchant approval state
- simple user filters for coffee or lunch

### Manual Or Operational During Pilot
- recruiting initial merchants
- verifying business legitimacy
- selecting which merchants appear in the feed
- writing or editing merchant copy
- monitoring offer quality and relevance
- handling merchant onboarding
- resolving redemption issues manually
- encouraging merchant participation in the pilot area
- measuring repeat usage and user return behavior

### Deferred Until After Proof
- reviews
- event feed
- advanced personalization
- richer loyalty mechanics
- automated merchant marketing tools
- multi-city expansion
- sponsored placements
- social features
- multiple redemption methods

## Business Model Hypothesis
Primary hypothesis: independent businesses will pay a small monthly fee or per-location fee for visibility and repeat-customer acquisition if LocalLoop drives measurable nearby visits and redemptions.

Secondary hypothesis: the consumer app remains free, with monetization later through merchant subscriptions or featured placement after trust and traction are proven.

The MVP should not assume a complex ad model or broad marketplace monetization.

## Critical Assumptions
- enough independent businesses exist in one neighborhood to create a useful feed
- merchants are willing to join a curated pilot
- users will try a new app if nearby results feel faster and more relevant than existing tools
- a simple offer is enough to motivate a visit
- the single redemption flow is practical in real store settings
- a simple loyalty ledger is understandable and reliable
- relevance can be maintained without advanced personalization
- merchant approval can keep unverified businesses out of the live feed

## How To Test Quickly
- launch in one dense neighborhood with a target of 20 to 50 approved merchants across coffee and lunch
- run founder-led merchant onboarding and curation
- use one redemption method only
- measure profile views, saves, redemptions, and repeat visits
- interview merchants weekly on value and operational friction
- test whether users return after one successful redemption within 2 to 4 weeks

Decision rule:
- Proceed if the pilot reaches at least 20 approved merchants, at least 25% of active users redeem an offer, and at least 20% of redeemers return for a second visit or reward within 30 days.
- Revise if merchant density is met but redemption or repeat use falls below target.
- Reject or restart the wedge if the neighborhood cannot sustain enough approved merchants or the redemption flow breaks repeatedly in live use.

## Acceptance Criteria
- a new user can enable location and see approved nearby businesses within seconds
- the feed contains enough relevant merchants to feel curated rather than generic
- each listed merchant has an approved profile and one active offer
- a user can save, navigate to, and redeem an offer without assistance
- merchants can verify redemption reliably through the supported flow
- loyalty, if offered, is recorded as a simple ledger event
- pilot merchants report measurable customer interest or visits attributable to the app
- the consumer flow works without manual intervention once the merchant is listed
- the product can prove repeat usage, not just one-time browsing

## Risks And Failure Modes
- merchant supply is too thin to make the feed useful
- users stay with Google Maps, Yelp, or social discovery habits
- offers are too generic or low-value to drive action
- the single redemption flow is awkward for merchants or staff
- relevance degrades without strong curation
- unverified listings reduce trust
- manual merchant acquisition makes scaling expensive
- repeat usage does not emerge after the first redemption

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Verified merchant density in one neighborhood is unproven [supply_density]
- Consumer demand for a curated local discovery app remains unproven [demand_validation]
- The single redemption flow has not been validated in live merchant settings [redemption_flow]
- Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data [metrics_validation]

Required Improvements:
- Run a concierge pilot with real users and a small merchant set [concierge_pilot]
- Finalize and test one redemption mechanism before launch [redemption_flow]
- Validate that users return after one successful visit or reward [metrics_validation]
- Confirm the launch neighborhood can support enough approved merchants before public consumer rollout [supply_density]

## Recommendation
Proceed with a narrow concierge-backed MVP in one neighborhood and two categories. Keep the product as a curated nearby feed with one redemption path, merchant approval, and a simple loyalty ledger. Do not expand into personalization, reviews, events, or broader category coverage until merchant supply, redemption reliability, and repeat usage are proven.