# LocalLoop MVP Product Proposal

## Product Problem
Consumers who want local independent businesses still default to Google Maps, Yelp, Instagram, and large horizontal platforms because local discovery is fragmented and inconsistent. Independent businesses lack a simple, affordable way to get discovered and to bring nearby customers back.

The MVP should prove one narrow loop: a nearby consumer discovers a vetted local business, redeems a simple offer, and the merchant sees enough value to continue.

## Initial Wedge
Launch in one city, one walkable neighborhood, and one high-frequency category: independent coffee shops and cafes.

The wedge is:
- nearby discovery
- verified merchants only
- one neighborhood
- one category
- one canonical offer/redemption flow
- a simple loyalty reward
- founder-led merchant recruitment
- manual curation during pilot
- admin-controlled publishing and moderation

This is the narrowest credible wedge to test supply density, repeat usage, and merchant willingness to continue.

## First Target User
Primary user:
- Nearby urban young professionals who live or work in the launch neighborhood

Secondary user:
- Independent coffee shop and cafe owners in the same neighborhood

Why this segment:
- frequent purchase behavior
- high local intent
- easy to test repeat visits
- merchants can judge foot traffic value quickly
- lower operational complexity than restaurants, events, or broad local commerce

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- neighborhood newsletters
- paper punch cards and in-store loyalty

Switching trigger:
- the user wants a better local recommendation than generic search results
- the user wants a nearby offer without searching across multiple apps
- the user wants a curated set of independent businesses in one neighborhood, not the whole city

LocalLoop must be better at one thing: trusted neighborhood discovery with a repeat-visit incentive. If it becomes a generic directory, users and merchants will not switch.

## Core MVP Workflow
1. Merchant is recruited by ops and submitted for review.
2. Ops approves or rejects the merchant profile and offer before publication.
3. User opens the app, shares location, and optionally sets a few preference signals.
4. App shows a small ranked list of verified nearby independent coffee shops/cafes.
5. Each listing includes merchant details, one active offer, and one loyalty action.
6. User opens a merchant profile, gets directions, and redeems the offer through one canonical method.
7. Redemption is recorded in a defined status flow and can be disputed or voided by support.
8. Merchant can request profile or offer updates, which go through admin review before publishing.
9. Ops can verify, re-verify, suspend, reactivate, or override ranking with reason codes and audit logging.

The core proof is whether the app can drive first visits and repeat visits in a dense neighborhood.

## In Scope
- Neighborhood-level discovery for one category: independent coffee shops/cafes
- One city, one launch neighborhood
- Nearby urban young professionals as the launch audience
- Verified merchant listings only
- Location-based ranking and basic preference capture
- Merchant profile pages
- One active offer per merchant
- One canonical redemption method
- Basic loyalty reward mechanic
- Merchant onboarding and offer updates through admin review
- Redemption tracking with dispute/void handling
- Merchant verification, re-verification, suspension, and reactivation states
- Ops-approved publishing gate for all merchant content
- Manual ranking overrides during the pilot
- Minimal user feedback signal, such as save or like
- Basic moderation of listings before launch
- Audit logging for merchant edits and admin actions
- Founder-led merchant recruitment for the pilot
- Merchant renewal checkpoint based on observed redemption value

## Out of Scope
- Multiple cities
- Broad category coverage beyond coffee/cafes
- Events feed
- Social feed or following graph
- User-generated reviews at launch
- Advanced personalization
- Complex recommendation engine
- In-app payments or checkout
- Delivery, reservations, or ordering
- Deep merchant CRM, email marketing, or campaign automation
- Open self-serve marketplace for any business type
- Automated consumer growth features before supply density exists
- Full-scale merchant analytics dashboard
- Public self-serve publishing without review
- Broad launch audience beyond nearby urban young professionals

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based nearby discovery
- Merchant profile pages
- Verified merchant status
- Merchant verification and re-verification states
- Required admin review gate before publishing
- One canonical redemption flow
- Offer display and redemption tracking
- Simple loyalty reward mechanic
- Basic preference capture
- Basic merchant admin for profile and offer update requests
- Merchant suspension, reactivation, and override states
- Reason-coded admin actions with audit logging
- Basic ops tools for ranking override and verification review
- Redemption dispute and void handling
- Moderation workflow that blocks all submissions until approved
- Canonical redemption state machine

### Manual Or Operational During Pilot
- Founder-led merchant recruitment in the launch neighborhood
- Merchant onboarding setup
- Merchant verification and re-verification review
- Curation of initial offers
- Quality control on listings and images
- Customer support for redemption issues
- Neighborhood supply balancing
- Hand-review of suspicious submissions
- Merchant renewal conversations

### Deferred Until After Proof
- Reviews
- Events feed
- Multi-category expansion
- Multi-city expansion
- Advanced personalization
- Push notification automation
- Merchant analytics dashboards
- In-app payments
- Social features
- Open self-serve merchant onboarding at scale
- Consumer growth automation

## Business Model Hypothesis
Primary hypothesis:
- Merchants pay a simple monthly fee for inclusion and local promotion once redemption value is proven
- or merchants pay for a featured placement tier after foot traffic value is demonstrated

Secondary hypothesis:
- consumer monetization is not the MVP focus
- loyalty economics may support a later subscription or transaction fee, but not now

The first goal is to prove merchants will pay for measurable foot traffic and repeat visits.

## Critical Assumptions
- Consumers will use a neighborhood-specific app instead of general search for local discovery
- A curated set of coffee shops is enough to create repeat usage
- Merchants will participate if setup is simple and value is visible
- A single redemption method can be understood by staff and users without confusion
- Offers and loyalty rewards can drive measurable repeat visits
- Supply density in one neighborhood is sufficient to make the app feel useful
- Simple ranking plus manual ops can produce acceptable discovery quality in the pilot
- One neighborhood can sustain enough verified merchants to feel worthwhile
- Merchant data can be kept trustworthy through review and audit controls
- Merchants will renew after seeing real redemption activity

## How To Test Quickly
- Recruit 10 to 20 verified coffee shops in one walkable neighborhood
- Launch to a small group of nearby urban young professionals
- Use manual merchant onboarding and curated offers
- Use one canonical redemption method for all pilot merchants
- Track:
  - profile views
  - offer redemptions
  - repeat visits
  - merchant renewal interest
- Interview users and merchants after 2 weeks
- Test willingness to continue with a renewal conversation after pilot activity is visible
- Use a simple decision rule:
  - Proceed if at least 30% of launched merchants record redemptions and at least 20% of active users return for a second session within 14 days
  - Revise if one metric clears and the other misses modestly
  - Reject or reframe if both miss materially or merchants do not express renewal intent

## Acceptance Criteria
- Users can see relevant verified coffee shops within the defined neighborhood
- Each merchant profile loads with accurate location, hours, and one active offer
- No merchant or offer is visible without admin approval
- The neighborhood includes enough verified merchants to feel meaningfully usable
- A user can redeem an offer or loyalty reward through one clear flow
- The system records redemptions reliably
- Failed redemptions can be voided or disputed by support
- Merchant can request one offer update without product team intervention during the pilot
- Ops can verify, re-verify, suspend, reactivate, and override merchants
- Ops actions are reason-coded and auditable
- A meaningful subset of users return for a second discovery session in the test period
- A meaningful subset of merchants say they would continue after the pilot
- Pilot metrics support the proceed/revise/reject decision rule above

## Risks And Failure Modes
- Insufficient merchant density makes the product feel empty
- Recommendations are too generic and users fall back to Google Maps
- Offers are not compelling enough to change behavior
- Merchants do not see measurable value and churn quickly
- Loyalty mechanics are too weak to drive repeat use
- Manual pilot operations hide a product that will not scale
- Expanding categories too early dilutes quality and supply density
- Redemption disputes create trust issues if the flow is unclear
- Admin review may slow the launch if operational turnaround is too slow
- The launch audience is too broad to create a repeatable wedge

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Need proof that one neighborhood can sustain enough verified merchant density to feel useful [market_motion]
- Need evidence that simple offers plus loyalty can change behavior versus existing tools [behavior_change]
- Need validation that merchants will renew after seeing redemption value [metrics_validation]
- Need enough pilot data to apply the proceed/revise/reject decision rule [metrics_validation]

Required Improvements:
- Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers [concierge_pilot]
- Define and use one canonical redemption method across the pilot [redemption_flow]
- Measure first-visit and repeat-visit behavior before expanding scope [repeat_usage]
- Validate merchant willingness to continue through direct renewal conversations [merchant_willingness]
- Collect pilot metrics against the explicit success threshold before launch expansion [metrics_validation]

## Recommendation
Proceed with a narrow concierge pilot, not a full product build.

Build only the neighborhood coffee-shop discovery loop with verified merchants, one redemption flow, admin review gates, and loyalty as the proof mechanism. Keep reviews, events, broader categories, multi-city expansion, and consumer growth automation out of scope until the pilot shows repeat usage, merchant renewal intent, and minimum success metrics. If the pilot does not meet the decision rule, revise or stop before scaling.