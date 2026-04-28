## Go-To-Market Notes
The main bottleneck is not product functionality; it is whether LocalLoop can secure enough **high-quality local supply in one neighborhood** to make the feed feel meaningfully better than Google Maps/Yelp, while also attracting a small, reachable user cohort that will actually try a new habit. The side of the market to secure first is **merchants/supply**, because without a dense, fresh, curated set of businesses and offers, consumer discovery will fail immediately.

2 to 3 structural GTM decisions:
1. **Launch as a concierge-curated neighborhood pilot, not a scalable marketplace.**
2. **Secure supply first from one dense neighborhood cluster, then recruit consumers from that same local context.**
3. **Use one primary acquisition motion: merchant-led distribution through participating businesses plus one nearby partner channel.**

Initial target audience:
- **Primary:** urban residents and young professionals who already live, work, or spend time in the pilot neighborhood
- **Smallest credible launch audience:** people within a 10–15 minute walk of the participating merchants, especially those who already visit independent coffee shops, quick-service restaurants, or small retail

Positioning:
- “A curated neighborhood feed for independent local businesses you can actually trust and use”
- Not a broad local search app, not a deals marketplace, and not a loyalty platform yet

First acquisition motion:
- **Merchant-led acquisition**
- Each participating merchant promotes LocalLoop to its own customers via a simple in-store QR prompt, counter card, receipt mention, or staff mention
- Add one nearby partner channel such as a neighborhood newsletter, apartment building, coworking space, or local community group

Operating assumptions for the first acquisition motion:
- Participating merchants are willing to introduce the app to customers because the pilot is low-lift and focused on exposure
- The neighborhood has enough walkable density that nearby consumers can be reached repeatedly
- A small number of merchants can generate enough credible consumer discovery to test repeat use
- The app can deliver enough freshness and relevance that users do not bounce after one session

Switching trigger:
- Existing discovery tools are too broad, stale, or cluttered for independent local businesses only
- Users switch when LocalLoop reliably surfaces a short, relevant list of nearby places with current offers
- Merchants continue only if the pilot produces visible nearby attention, saves, visits, or redemptions

First activation loop:
- User opens app near the neighborhood → sees a short curated nearby feed → saves or redeems one place → receives a reason to return because the feed updates when nearby merchants change offers or get refreshed
- The loop is not “browse endlessly”; it is “discover one useful place, then come back when the neighborhood feed changes”

What must exist before public launch:
- At least one dense neighborhood with a curated merchant set that is genuinely fresh
- Enough merchant supply to avoid an empty or repetitive feed
- A defined redemption and logging flow
- A simple, understandable consumer onboarding path
- A manual process to keep stale listings out of the live feed
- A clear activation metric and a short retention check window

What must be productized now:
- Nearby curated feed
- Merchant profile page with active offer
- Save/favorite action
- Simple redemption verification and logging
- Publish/pause/expire states
- Last-reviewed timestamp and stale-listing hiding

What can stay manual during the pilot:
- Merchant sourcing and approval
- Offer creation and cleanup
- Merchant outreach and onboarding
- Neighborhood partner recruitment
- Freshness checks
- Feed moderation and quality control
- Redemption support and issue resolution

## Review Summary
The draft is directionally sound, but the launch risk is supply density and habit change, not feature breadth. The right GTM move is a narrow, concierge-led neighborhood pilot with merchant-first acquisition and one adjacent local channel, proving that a curated supply set can generate enough consumer activation and merchant interest to justify expansion.

## Build Vs Pilot Operations

### Must Be Productized Now
- Nearby discovery feed
- Merchant profile page
- Offer display
- Save/favorite action
- Simple redemption verification and logging
- Publish / pause / expire listing states
- Last-reviewed timestamp display
- Stale-listing hiding rule
- Basic analytics for views, saves, and redemptions

### Can Stay Manual Or Operational During Pilot
- Curate and approve merchants
- Write or clean up merchant descriptions
- Source and upload offers
- Verify listings are current
- Manually refresh stale content
- Support merchant onboarding and questions
- Monitor feed quality and suppress low-quality listings
- Run redemption verification if needed
- Merchant-led user invite push
- Partner outreach to one neighborhood channel

### Deferred Until After Proof
- Full loyalty program
- Reviews and comments
- Event discovery
- Automated merchant self-serve tools
- Sophisticated recommendation models
- Multi-neighborhood or multi-city rollout
- In-app messaging
- Revenue optimization tooling for merchants

## Critical Assumptions
- One dense neighborhood can supply enough quality merchants to make the feed feel valuable
- Merchants will cooperate with a concierge pilot if the lift is low and exposure is visible
- Users within the neighborhood can be reached through merchant-led distribution and one local partner channel
- A simple save/redeem activation event is enough to demonstrate meaningful interest
- Repeat opens within a short window can indicate enough habit potential to justify expansion

## Requested Changes
- Define one primary acquisition motion explicitly as merchant-led distribution plus one neighborhood partner channel [market_motion]
- Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Add a minimum merchant supply threshold required before consumer launch [scope]
- Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]
- Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]

## Risks
- The neighborhood feed may still feel too thin even if it is curated well [scope]
- Users may not adopt a new discovery habit when Google Maps and social platforms already exist [demand_validation]
- Merchants may participate initially but not continue after the pilot [market_motion]
- Merchant-led acquisition may not produce enough consumer volume without a strong local partner channel [market_motion]
- Manual curation may become too labor-intensive if the merchant base expands too early [operations]

## Open Questions
- How many merchants are required to make one neighborhood feel genuinely useful?
- Which exact merchant category mix produces the strongest first-session engagement?
- What is the one neighborhood partner channel most likely to reach the target audience efficiently?
- What is the minimum repeat-open threshold that would justify continuing the pilot?
- What merchant outcome will count as credible evidence of value: saves, visits, redemptions, or stated willingness to pay?

## Why This Could Fail Even With Good Execution
Even with solid execution, the plan can fail if the market simply does not reward a new local-discovery habit. If users continue defaulting to Google Maps, Yelp, and social platforms, LocalLoop may generate some curiosity but not enough repeat behavior or merchant value to become a durable channel.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- The primary acquisition motion is not yet explicit enough to support a credible launch plan [market_motion]
- The smallest launch audience is still too broad to reliably test local habit formation [scope]
- The merchant-side minimum supply threshold is not defined, so the feed could launch too thin [scope]

Required Improvements:
- Lock one merchant-led acquisition motion plus one neighborhood partner channel for the pilot [market_motion]
- Define the smallest credible audience as users within walking distance of the pilot merchants [scope]
- Set a minimum active merchant count and freshness threshold before public launch [scope]
- Tie launch success to one activation metric and one retention metric [metrics_validation]