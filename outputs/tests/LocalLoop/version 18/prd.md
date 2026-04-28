# LocalLoop MVP Product Proposal

## Product Problem
People who want to support independent local businesses default to Google Maps, Yelp, Instagram, and deal platforms because local discovery is fragmented, noisy, and hard to trust.

Independent businesses need nearby customer attention, but they cannot support complex marketing tools or broad platform overhead.

The MVP must prove a narrow claim: a curated, neighborhood-level discovery feed for independent businesses can create repeat user engagement and enough merchant value to justify expansion.

## Initial Wedge
A concierge-curated discovery feed for one dense neighborhood, focused first on independent coffee shops and quick-service restaurants.

This is the narrowest credible wedge because it concentrates supply, keeps relevance manageable, and avoids direct competition with horizontal discovery platforms.

## First Target User
Primary target:
- Urban residents and young professionals who live, work, or spend time within a 10–15 minute walk of the pilot neighborhood

Secondary pilot users:
- Nearby families and tourists already in the same area
- Independent merchants willing to trial a low-lift exposure channel

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- Groupon-style deals
- Word of mouth and neighborhood newsletters

Switching trigger:
- Existing tools are broad, cluttered, and not optimized for independent local businesses only
- Users want a faster, more relevant way to find nearby independent places without sorting through chains, stale listings, or unrelated content
- Merchants want local visibility without running full campaigns or adopting heavy tooling

## Core MVP Workflow
1. Admin curates and approves merchants for a single neighborhood.
2. Each merchant listing includes category, location, short description, and one active offer if available.
3. Every public listing shows a last-reviewed timestamp and is hidden automatically if stale.
4. User shares location and sees a small nearby feed ranked by proximity and a few explicit preferences.
5. User opens a merchant profile, saves the place, or redeems the offer.
6. Redemption is verified through a simple pilot flow and logged for both user and merchant tracking.
7. Admin monitors feed quality, pauses stale listings, and updates merchant content as needed.

## In Scope
- One-neighborhood launch
- One consumer segment: people within a 10–15 minute walk of pilot merchants
- Nearby discovery feed
- Rule-based preference matching for ranking
- Merchant profile pages with essential business info
- Offer display
- Save/favorite action
- Simple redemption verification and logging
- Admin-first merchant approval and publishing
- Publish / pause / expire listing states
- Mandatory last-reviewed timestamp for public listings
- Stale-listing hiding rule
- Basic analytics for views, saves, redemptions, active merchants, active offers, and freshness coverage
- Curated supply to maintain relevance
- Mobile-first consumer experience
- Minimum merchant supply threshold before consumer launch

## Out of Scope
- Multi-city expansion
- Open merchant self-serve onboarding
- Full loyalty points wallet
- Reviews and user-generated ratings
- Event feed
- Social sharing features
- Advanced machine learning recommendations
- Automated ad management
- Deep CRM or marketing automation
- Delivery, booking, or payment processing
- Chain businesses as a primary supply strategy
- Complex merchant dashboards
- Broad citywide consumer launch

## MVP Build Vs Pilot Operations
### Must Build Now
- Nearby discovery feed
- Rule-based ranking using a small set of preferences
- Merchant profile page
- Offer display
- Save/favorite action
- Simple redemption verification and logging
- Admin-first content management
- Publish / pause / expire listing states
- Last-reviewed timestamp display
- Stale-listing hiding rule
- Basic analytics for views, saves, redemptions, active merchants, active offers, and freshness coverage

### Manual Or Operational During Pilot
- Curate and approve merchants
- Write or clean up merchant descriptions
- Source and upload offers
- Verify listings are current
- Manually refresh stale content
- Support merchant onboarding and questions
- Monitor feed quality and suppress low-quality listings
- Run redemption verification if needed
- Enforce the minimum merchant supply threshold before opening to users

### Deferred Until After Proof
- Full loyalty program
- Reviews and comments
- Event discovery
- Automated merchant self-serve tools
- Sophisticated recommendation models
- Multi-neighborhood or multi-city rollout
- In-app messaging
- Revenue optimization tooling for merchants

## Business Model Hypothesis
Primary hypothesis:
- Charge local businesses a monthly subscription for inclusion and ongoing featured exposure in a curated neighborhood feed

Pilot hypothesis:
- A small set of merchants will continue participating, or express willingness to pay, if the feed delivers measurable nearby attention or redemptions

Secondary later hypothesis:
- Premium placement or campaign boosts may become viable after discovery demand is proven

## Critical Assumptions
- A single neighborhood can generate enough supply to make the feed feel useful
- Users will engage with a local-only discovery app instead of defaulting to existing platforms
- Independent businesses will accept a manually managed pilot in exchange for exposure
- Rule-based matching is good enough to feel personalized at MVP stage
- Offers and save/redemption actions are sufficient to show value
- Supply can stay accurate enough to avoid stale or misleading listings
- One dense neighborhood with a sufficient merchant count can produce a credible discovery experience

## How To Test Quickly
- Launch in one dense neighborhood, not a full city
- Secure a minimum curated merchant set before consumer launch
- Run a concierge pilot with manual merchant approval and offer setup
- Make save or redeem the first activation event
- Track repeat opens over a short interval as the retention signal
- Track merchant continuation or willingness to pay after initial exposure
- Compare engagement to a simple curated list or neighborhood newsletter baseline

## Acceptance Criteria
- User can see nearby independent businesses in the pilot neighborhood
- User can apply basic preferences and receive a ranked feed
- User can open a merchant profile and view an active offer
- User can save a business
- User can redeem an offer through a defined pilot flow
- Redemption is logged and attributable
- Every public listing has a last-reviewed timestamp
- Stale listings are hidden automatically
- Merchants are manually approved before publish
- A minimum merchant supply threshold is met before consumer launch
- Feed quality remains high enough that users are not seeing obvious stale or irrelevant listings
- A pilot cohort shows save or redeem behavior within the test window
- A pilot cohort shows repeat opens within the test window
- A subset of merchants indicates willingness to continue or pay

## Risks And Failure Modes
- Supply risk: too few quality merchants in one neighborhood
- Freshness risk: stale or inaccurate listings erode trust quickly
- Relevance risk: rule-based personalization feels generic
- Adoption risk: users continue to rely on existing discovery tools
- Merchant value risk: businesses do not see enough lift to continue
- Operational risk: manual curation becomes too costly to sustain
- Positioning risk: the product drifts toward a broad local platform instead of a disciplined wedge

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Need proof that one neighborhood and a curated merchant set can beat default discovery habits [demand_validation]
- Need evidence that merchants will continue participation or pay after the pilot [market_motion]
- Need a defined success gate using activation, retention, merchant supply, and freshness coverage [metrics_validation]

Required Improvements:
- Run a concierge pilot in one dense neighborhood with real users and merchants [operations]
- Define the minimum merchant supply threshold before consumer launch [scope]
- Measure save or redeem as the first activation event [metrics_validation]
- Track repeat opens over a short interval as the retention signal [metrics_validation]
- Track merchant continuation or willingness-to-pay after initial exposure [market_motion]

## Recommendation
Proceed with a narrow concierge pilot, not a broader build.

Keep the MVP limited to one dense neighborhood, one consumer segment, curated supply, rule-based ranking, basic offers, and simple redemption tracking. Do not add loyalty, reviews, events, or automated self-serve tooling until the core loop proves that users engage repeatedly and merchants see enough value to stay.

Decision rule for the pilot:
- Proceed if at least 30% of activated users save or redeem within the test window, at least 20% of activated users return for a second open within 14 days, at least 10 merchants are active, at least 80% of live listings are fresh, and at least 5 merchants express willingness to continue or pay
- Revise if engagement is meaningful but one of the thresholds is missed
- Reject if the feed cannot stay fresh, users do not activate, or merchants do not see credible value