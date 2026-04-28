## Go-To-Market Notes
- **Main market bottleneck:** merchant supply density and freshness in one neighborhood. If the app does not have enough verified, relevant coffee shops with current offers, consumers will bounce back to Google Maps/Yelp immediately.
- **Side of the market to secure first:** **merchant supply first**, then consumers. You need a dense, trustworthy local inventory before any consumer launch can be credible.
- **Structural GTM decisions:**
  1. **Founder-led merchant recruitment** is the primary acquisition motion for the pilot. No paid acquisition or broad consumer marketing yet.
  2. **One neighborhood, one category, one offer format** only. The product should feel curated, not comprehensive.
  3. **Concierge pilot with manual ops** until proof: manual onboarding, manual verification, manual curation, and manual follow-up on redemption value.
- **Initial target audience:** independent coffee shops and cafes in one walkable urban neighborhood, specifically owners/managers who can decide quickly and care about weekday foot traffic.
- **Positioning:** “A curated neighborhood discovery channel that brings nearby regulars to independent cafes with one simple offer and a lightweight loyalty loop.”
- **First acquisition motion:** founder-led in-person and direct outreach to local cafe owners, supported by walk-ins and neighborhood association introductions.
- **Operating assumptions for the first acquisition motion:**
  - The neighborhood has enough foot traffic and independent cafes to support a dense pilot.
  - Owners will respond to a promise of incremental visits, not abstract marketing value.
  - A simple, repeatable offer can be set up in minutes.
  - Verification and publishing can be done manually without slowing merchant sign-up too much.
- **Switching trigger:** users switch when the app reliably shows a small, trusted set of nearby independent cafes with a real offer attached, not just generic nearby listings.
- **First activation loop:** user discovers a nearby verified cafe → redeems one offer → merchant sees a visit/redemption → merchant agrees to stay/live with the listing → the app maintains freshness with a small set of active merchants.
- **What must exist before public launch:** at least one neighborhood with enough verified merchants to feel useful, one canonical redemption flow, clear offer validity, and enough merchant follow-through to avoid a dead directory experience.
- **Must be productized now vs manual during pilot:**
  - **Productized now:** nearby discovery, merchant profile pages, verified status, one redemption flow, offer display, basic loyalty action, admin approval gate, redemption tracking, basic merchant edit request flow.
  - **Manual during pilot:** merchant sourcing, onboarding, verification, offer selection, ranking overrides, moderation, customer support, renewal conversations.
  - **Deferred:** reviews, events, multi-category expansion, automated personalization, self-serve merchant onboarding at scale, analytics dashboard.

## Review Summary
The main launch challenge is not consumer acquisition; it is whether one neighborhood can be made dense, current, and trusted enough to beat generic search defaults. The recommended direction is a founder-led, merchant-first concierge pilot in one neighborhood with one category, one offer flow, and manual curation until merchant renewal and repeat use are proven.

## Build Vs Pilot Operations

### Must Be Productized Now
- Nearby discovery for the launch neighborhood
- Verified merchant profile pages
- One canonical offer/redemption flow
- Offer display and redemption status tracking
- Basic loyalty reward mechanic
- Admin review gate before publishing
- Merchant edit request flow
- Merchant suspension / re-activation states

### Can Stay Manual Or Operational During Pilot
- Merchant recruitment
- Merchant onboarding
- Merchant verification
- Offer creation and selection
- Manual ranking overrides
- Content moderation
- Customer support for redemption issues
- Merchant renewal conversations
- Neighborhood supply balancing

### Deferred Until After Proof
- Reviews
- Events feed
- Broad category expansion
- Multi-city launch
- Advanced personalization
- Push automation
- Merchant analytics dashboard
- Open self-serve onboarding
- Social features
- In-app payments

## Critical Assumptions
- A single neighborhood can support enough verified coffee shops to feel useful.
- Founder-led outreach can recruit merchants faster than a self-serve flow would.
- Merchants will join if setup is simple and redemption value is visible.
- One redemption flow is understandable enough for staff and users.
- Users will choose a curated local app over Google Maps when the supply is dense and current.

## Requested Changes
- Define the **minimum verified merchant count** needed before consumer launch, plus a freshness threshold for active offers. [market_motion]
- Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]

## Risks
- Merchant density is too thin, making the app feel empty. [market_motion]
- The app does not beat Google Maps on trust or convenience. [demand_validation]
- Offers are not compelling enough to change behavior. [behavior_change]
- Merchants join but do not renew after the pilot. [metrics_validation]
- Manual operations mask a weak core product and delay the real market signal. [operations]

## Open Questions
- How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]
- Is the first consumer audience limited to workers/lunch buyers, residents, or both? [market_motion]
- What is the maximum acceptable turnaround time for manual review before the pilot feels slow? [operations]

## Why This Could Fail Even With Good Execution
Even if the team executes well, this can fail if the neighborhood never reaches enough density and freshness to become a habit-forming alternative to Google Maps. In that case, consumers sample once, merchants see too little repeat value, and the product remains a curated directory instead of becoming a true local discovery channel.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- No quantified minimum merchant density for a credible neighborhood launch [market_motion]
- No single primary acquisition motion defined for merchant supply [market_motion]
- Launch audience is still too broad relative to the pilot wedge [market_motion]
- Merchant renewal proof is not yet tied to a clear threshold [metrics_validation]

Required Improvements:
- Set a minimum verified merchant count and freshness threshold before consumer launch. [market_motion]
- Commit to founder-led merchant recruitment as the primary acquisition motion. [market_motion]
- Narrow the first audience to nearby urban young professionals in the launch neighborhood. [market_motion]
- Define the merchant renewal trigger as a launch gate, not just a post-pilot interview. [metrics_validation]