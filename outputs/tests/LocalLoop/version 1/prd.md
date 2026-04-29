# LocalLoop MVP Product Proposal

## Product Problem
People in Paris who want to support local independent businesses still default to Google Maps, Instagram, Deliveroo/Tripadvisor, or word of mouth because discovery is fragmented and not personalized enough.

Independent businesses want nearby customers and repeat visits, but they lack simple tools and distribution to compete for attention.

The MVP must prove one narrow thing first: whether a tightly curated Paris discovery loop can drive real visits to independent businesses better than generic search and social browsing.

## Initial Wedge
A Paris-only mobile app for frequent coffee/lunch decision-makers in one named micro-market, focused on independent coffee shops and lunch spots, with a simple offer and a verified visit-based loyalty loop.

This is narrow enough to control supply quality, keep the feed alive, and test repeat usage in a real neighborhood context.

## First Target User
Primary user:
- Urban residents in Paris who make frequent coffee and lunch decisions on weekdays
- Young professionals aged 22–40 within the pilot micro-market

First use case:
- “I want a good nearby independent place to go right now, with a reason to choose it over a chain.”

Secondary supply-side target:
- Independent coffee shops and casual lunch spots in the same pilot micro-market

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps for discovery and directions
- Instagram/TikTok for informal recommendations
- Deliveroo/Uber Eats for food discovery
- City guides and blogs for editorial discovery
- Paper loyalty cards or POS-linked loyalty tools for retention

Switching trigger:
- The user wants a curated local-only recommendation with an immediate incentive, not a generic map result or influencer content.
- The merchant wants first-time foot traffic or repeat visits without running paid ads or building their own app.

## Core MVP Workflow
1. User opens the app and sets a few preferences: neighborhood and category.
2. App shows a small feed of nearby independent businesses that are currently active.
3. Each listing includes:
   - short merchant description
   - distance
   - one offer or reward
   - basic loyalty status
4. User taps a merchant and sees enough detail to decide to visit.
5. User redeems the offer in-store through a single one-time token shown in-app and validated by staff or ops.
6. Redemption is marked consumed once validated; failed validation can be marked disputed for later support resolution.
7. Loyalty accrues through verified repeat visits to the same merchant.
8. Merchant sees basic activity and redemption metrics.

## In Scope
- Paris-only consumer app
- One named Paris micro-market for the pilot
- Independent coffee shops and lunch spots only
- Basic filtering by location and category
- Merchant profile page with essential details
- One offer per merchant
- One loyalty mechanic tied to verified repeat visits
- One redemption method using a one-time token
- Manual merchant onboarding for pilot
- Curated inventory to reduce irrelevant listings
- Required merchant quality checklist before activation
- Manual approval for live status
- Basic merchant analytics: views, redemptions, repeat visits
- Admin controls to manage merchant live/inactive state and suppress stale offers
- Audit logs and override permissions for support-side adjustments
- Disputed redemption handling
- Fixed category set for pilot

## Out of Scope
- Citywide expansion beyond Paris
- Multi-city marketplace mechanics
- Deep social features
- Open reviews and ratings
- Full event aggregation feed
- Advanced recommendation engine
- Merchant self-serve onboarding
- Ad marketplace or paid promotion system
- Delivery ordering
- Table booking
- Full CRM or marketing automation for merchants
- Chain businesses and horizontal retail coverage
- Heavy gamification
- Multiple redemption methods
- Complex loyalty tiers or cross-merchant rewards
- Broad category coverage beyond coffee and lunch
- Automated offer optimization
- Merchant-initiated live publishing without approval
- Uncurated open marketplace inventory

## MVP Build Vs Pilot Operations
### Must Build Now
- Consumer mobile app
- Merchant profile pages
- Nearby discovery feed
- Basic preference and location filtering
- Offer display
- Single redemption flow
- Verified loyalty tracking for repeat visits
- Basic merchant analytics
- Admin console for merchant status, offers, disputes, and support overrides
- Audit logging for manual adjustments
- Merchant quality checklist workflow
- Manual approval gate for live status
- Stale-offer suppression controls

### Manual Or Operational During Pilot
- Merchant sourcing and onboarding in Paris
- Offer setup and validation
- Content curation to keep feed relevant
- Quality checks on listings and merchant details
- Customer support for redemption issues
- Outreach to merchants and initial users
- Micro-market selection and inventory balancing
- Manual review of active/inactive merchant status
- Manual verification of repeat visits when needed
- Dispute resolution for failed redemptions

### Deferred Until After Proof
- Self-serve merchant portal
- Advanced personalization
- Reviews and social features
- Event discovery feed
- Multi-city rollout
- Paid merchant tools and campaigns
- Cross-merchant rewards
- Automated offer optimization
- Broad category expansion
- Multiple redemption paths
- Full merchant CRM tooling

## Business Model Hypothesis
Primary hypothesis:
- Charge merchants a simple monthly subscription for visibility, offers, and basic retention tools once the product proves it can drive visits.

Secondary hypothesis:
- Later add premium analytics or promoted placements, but only after proving merchant ROI and user engagement.

For the pilot, the objective is not monetization optimization; it is validating willingness to pay after measurable foot traffic and repeat visits.

## Critical Assumptions
- Users will trust the app enough to try a local recommendation instead of using Google Maps.
- Enough independent businesses in one fixed Paris micro-market will participate.
- Coffee and lunch use cases can generate enough repeat use to create habit.
- Offers and loyalty rewards will be compelling enough to change behavior.
- The app can keep recommendations relevant without a large inventory.
- Merchants will see value in simple visit and repeat-visit tracking.
- The redemption flow can be made simple and reliable.
- The experience can avoid looking like a noisy coupon directory.

## How To Test Quickly
- Run a concierge pilot in one fixed Paris micro-market with 20–30 independent businesses.
- Manually curate a small set of merchants in coffee and lunch.
- Launch a limited beta focused on “where should I go nearby?”
- Track:
  - app opens
  - listing clicks
  - offer redemptions
  - repeat visits
  - merchant willingness to continue
- Interview users after visits to understand what made them choose the business.
- Interview merchants to determine whether the app delivered incremental traffic or retention.

## Acceptance Criteria
- A user can find a relevant nearby independent business in under 30 seconds.
- A merchant profile clearly shows location, offer, and reason to visit.
- The one-time token redemption flow works reliably with minimal staff confusion.
- A required merchant quality checklist is completed before activation for every live merchant.
- At least 20 participating businesses are active in the pilot area.
- Users can redeem an offer or loyalty reward without support intervention in most cases.
- Merchants can see basic activity metrics.
- A meaningful share of users return for a second visit to the same merchant within a short test window.
- Pilot results show enough repeat visits and redemptions to justify continued investment.

## Risks And Failure Modes
- Poor supply density makes the app feel empty [supply_density]
- Recommendations are too generic and users revert to Google Maps [recommendation_quality]
- Merchants do not see enough ROI to stay active [merchant_roi]
- Offers attract deal-seekers who do not convert into repeat customers [low_quality_traffic]
- Manual curation does not scale beyond the pilot [ops_scalability]
- Redemption friction causes failure at the point of visit [redemption_friction]
- The product becomes another irrelevant local listing app [category_blur]
- Quality control is too burdensome and slows supply activation [quality_assurance]

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No proof yet that curated local discovery changes user behavior in Paris [demand_validation]
- No proof yet that merchants will provide enough quality inventory and continue participation [supply_validation]
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use [redemption_friction]

Required Improvements:
- Run a concierge pilot with real users and merchants in one fixed Paris micro-market [concierge_pilot]
- Validate repeat visit and redemption behavior with coffee and lunch only [behavior_proof]
- Confirm merchant willingness to continue after initial traffic testing [merchant_roi]

## Recommendation
Proceed with a tightly scoped Paris concierge pilot.

Do not build a broad marketplace yet. The right next step is to prove one repeatable use case: nearby independent business discovery with a simple offer and verified loyalty loop.

If pilot results show weak user pull or merchant retention, stop or re-scope before expanding beyond a few neighborhoods.