# LocalLoop MVP Product Proposal

## Product Problem
People who want to discover and support local independent businesses default to Google Maps, Yelp, and social platforms because local discovery is fragmented and inconsistent. Independent businesses also struggle to earn repeat visits without expensive marketing tools. LocalLoop’s MVP should prove a narrow wedge: a trusted, neighborhood-specific discovery experience for one dense area that helps users find relevant places and gives merchants a simple way to attract first visits.

## Initial Wedge
Launch in one neighborhood in one city with a tightly curated set of independent coffee shops, cafes, and casual lunch spots. The wedge is not all local commerce; it is a repeat-use local discovery loop where density, freshness, and relevance can be maintained manually.

## First Target User
People who live or work in the launch neighborhood and already use mobile search or maps for nearby decisions. They are most likely to try a new app if results feel clearly local, current, and better than generic search.

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps and Apple Maps for nearby search and directions
- Yelp for ratings and reviews
- Instagram/TikTok for local discovery
- Merchant websites and social pages for offers
- Deal apps for discounts

Switching trigger:
- The app surfaces a better nearby option from the immediate neighborhood
- The result includes a verified current offer or reward
- The feed feels denser and more trustworthy than generic search because it is manually curated and freshness-checked

## Core MVP Workflow
1. User opens the app and shares location.
2. App shows a small set of nearby independent businesses in the launch neighborhood.
3. Results are ranked with simple rules based on proximity, category fit, freshness, and available offer.
4. Each merchant listing shows hours, distance, category, short description, freshness status, and one current offer or loyalty reward.
5. User taps to save, get directions, or redeem a reward.
6. Redemption is verified using one predefined MVP method.
7. User can mark the result useful or not useful.
8. Merchant activity and redemptions are tracked for pilot review.

## In Scope
- One launch neighborhood only
- Independent businesses only
- One category cluster for dense repeat use
- Rules-based ranking, not advanced AI personalization
- Merchant profile pages with hours, location, category, short description, and freshness status
- One current offer or loyalty reward per merchant
- Single MVP redemption/visit verification method
- Save/favorite functionality
- Map handoff for directions
- Basic useful / not useful feedback
- Operator-only approval before anything goes live
- Immutable audit log for merchant, offer, suspension, and redemption events
- Manual merchant onboarding for pilot supply
- Basic admin controls for offer approval, suspension, and support override
- Automatic hiding of stale listings
- Minimum required fields before a listing can go live
- Freshness-control workflow with required fields and check cadence

## Out of Scope
- Reviews and public ratings
- Event discovery feed
- Citywide or multi-city rollout
- Broad category expansion beyond the launch cluster
- In-app ordering, booking, or payments
- Delivery
- Paid promotions or sponsored placement
- Complex recommendation models
- Merchant self-serve onboarding
- Deep merchant analytics dashboard
- User-to-merchant messaging
- Social feed mechanics
- Horizontal competition with general-purpose local search platforms
- Multiple redemption methods
- Automatic merchant onboarding
- Broader personalization experiments

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based discovery for one neighborhood
- Merchant profile pages
- Rules-based ranking
- Freshness status on listings
- Automatic hiding of stale entries
- One redemption/visit verification method
- Save/favorite and map handoff
- Basic feedback signal
- Operator-only approval queue
- Immutable audit log
- Minimum fields required before go-live
- Basic admin controls for approval, suspension, and support override
- Freshness-control workflow

### Manual Or Operational During Pilot
- Merchant sourcing and onboarding
- Offer setup and verification
- Freshness checks
- Category curation
- Consumer recruitment in the launch neighborhood
- Customer support for merchant issues
- Renewal check-ins with merchants
- Fallback handling when redemption verification fails

### Deferred Until After Proof
- Reviews and ratings
- Event feed
- Advanced personalization models
- Automated self-serve merchant onboarding
- Merchant analytics dashboard
- Paid placements
- Multi-city expansion
- In-app payments or ordering

## Business Model Hypothesis
The early model is a merchant subscription or monthly fee for inclusion, offer participation, and loyalty exposure within a dense neighborhood, potentially preceded by a free pilot period. A later model could add premium placement or performance-based promotion, but the MVP should only test whether merchants value incremental visits enough to continue after the pilot.

## Critical Assumptions
- A dense enough set of independent businesses can be assembled and kept current in one neighborhood
- Users will try a neighborhood-specific app if results feel relevant and verified
- Simple offers or loyalty rewards are enough to motivate first visits
- Merchants will participate without requiring a full self-serve platform
- Users will prefer this curated local layer over default behavior in Maps or social apps
- A single redemption method can be executed reliably by merchants and users
- A minimal onboarding flow is sufficient for merchants to join and stay active through the pilot

## How To Test Quickly
- Manually recruit a small cohort of independent businesses in one neighborhood
- Keep onboarding to a founder-led process that collects only required business details, validates hours and location, agrees on one offer, and obtains operator approval before publishing
- Curate only the chosen category cluster to maintain density
- Launch to a small local user group
- Compare engagement on curated recommendations versus a basic directory view
- Track saves, taps to directions, redemptions, and repeat opens
- Review merchant willingness to continue after the pilot period
- Monitor whether freshness and verification reduce trust issues
- Measure how long onboarding takes and how many merchants complete the process without follow-up

## Acceptance Criteria
- One launch neighborhood is fully defined and populated with a dense set of participating businesses
- At least 60% of listed businesses have verified hours, location, and one current offer
- Each listing shows freshness status and stale entries are hidden automatically
- Users can discover, save, and navigate to a business in under 60 seconds
- One redemption/visit verification method works reliably in pilot
- At least 25% of activated users engage with a listing in their first session
- At least 10% of activated users return within 30 days
- A meaningful subset of merchants indicates willingness to continue after the pilot
- Merchant onboarding can be completed with a minimal founder-led flow and no product-heavy setup
- No merchant or offer appears without operator approval and required minimum fields

## Risks And Failure Modes
- Supply density is too weak, making the app feel empty [supply_density]
- Listings become stale and trust erodes [quality_assurance]
- The chosen category cluster does not create repeat use [market_motion]
- Rules-based ranking is still too generic to beat Maps or social apps [demand_validation]
- Merchants do not see enough value to continue [merchant_value]
- Manual curation and freshness checks create too much operational burden [onboarding]
- Redemption is confusing or unreliable for merchants and users [quality_assurance]
- The app tries to broaden scope before the neighborhood wedge is proven [scope]

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete [supply_density]
- No proof that the curated, rules-based recommendation experience is better than existing alternatives [demand_validation]
- No proof that merchants will renew after a pilot period [merchant_value]

Required Improvements:
- Run a concierge pilot in one neighborhood with manual curation and freshness checks [quality_assurance]
- Validate merchant renewal intent with a small pilot cohort [merchant_value]
- Test the curated feed against a simple baseline directory [demand_validation]
- Confirm a single redemption/visit verification method before launch [quality_assurance]
- Keep merchant onboarding to a minimal founder-led flow with strict approval gates [onboarding]

## Recommendation
Proceed only as a concierge-first pilot in one neighborhood with a narrow category cluster and manually maintained supply. Keep the MVP focused on proving density, freshness, redemption, and merchant willingness to continue. Do not expand into reviews, events, broader personalization, or multi-city rollout until the pilot shows repeat user engagement and credible merchant retention.