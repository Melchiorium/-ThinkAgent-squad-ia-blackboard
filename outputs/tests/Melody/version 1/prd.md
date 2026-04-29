# Melody MVP Product Proposal

## Product Problem
Music is a strong identity signal, but people currently need separate tools for different outcomes: dating apps for romance, event apps for concerts, and community platforms for social discovery. That fragmentation makes it hard to find one meaningful local connection that feels culturally aligned.

Melody should not launch as a broad music social network. The first product problem is:
- help Paris-based music lovers find one compatible local concert companion based on shared taste
- turn that connection into a concrete next step: a message and a concert plan
- prove that music compatibility creates better intent than generic social matching

## Initial Wedge
A Paris-only concert-companion matching product for music-active people who want to meet someone local around a shared live music plan.

The wedge is:
- “Find one compatible person in Paris to go to a concert with, based on music taste”

This is the narrowest credible wedge because it:
- avoids becoming a generic dating clone at launch
- proves music taste as a matching signal
- creates a concrete activation path
- is easier to test than a broad social ecosystem

## First Target User
Primary target:
- concert-goers in Paris, roughly 22–35, who use music as part of identity and want a companion for live events

Secondary, only if density requires it later:
- music-active singles who are open to dating, but only after the concert-companion wedge is working

Not first target:
- band-member seekers
- marketplace users
- general community users
- broad music discovery users

## Existing Alternatives And Switching Trigger
Current alternatives:
- Tinder / Bumble / Hinge for dating
- Resident Advisor, Shotgun, Dice, Bandsintown for events
- Spotify social sharing for taste signaling
- Facebook groups, Discord, Reddit, WhatsApp for local music communities
- LeBonCoin / Facebook Marketplace for gear
- MeetUp and informal groups for social matching

Switching trigger:
- existing dating apps do not make music taste a first-class compatibility engine
- users want a local companion for a specific concert or scene, not endless swiping
- the app offers a higher-intent match around a real plan
- users want a product that feels music-native rather than dating-first

## Core MVP Workflow
1. User signs up in Paris.
2. User enters mandatory music preferences: top artists, genres, and one music identity prompt.
3. User chooses one primary intent: concert companion.
4. User selects one specific Paris music scene or event context.
5. App moves the profile to `pending_review`.
6. A moderator approves the profile, moving it to `active`.
7. Only `active` profiles appear in match results.
8. User sees a small set of nearby compatible profiles.
9. User likes, skips, or matches.
10. On match, users can exchange a basic message.
11. The app prompts users to propose a concert plan or meetup.

The workflow must prove:
- music taste can be used as a useful match signal
- local relevance is strong enough in Paris
- users will take the first step after matching

## In Scope
- Paris-only matching
- account creation and basic profile
- mandatory music entry with top artists, genres, and one identity prompt
- one selected primary intent per user: concert companion
- one specific Paris scene or event context
- hard profile state machine: `draft` → `pending_review` → `active` → `reported` / `suspended`
- moderator review queue for activation
- only `active` profiles can appear in matching
- simple compatibility score based on shared artists and genres
- swipe or list-based match flow
- basic messaging after match
- lightweight profile fields relevant to music identity
- coarse Paris-level location filtering
- reporting and blocking
- immediate removal from matching when reported or blocked, pending review
- audit log for moderator actions
- core analytics for match-to-message conversion
- lightweight prompt to propose a concert plan
- one optional manual-only music enrichment source, if needed for pilot density, but not a built product dependency

## Out of Scope
- dating-first positioning at launch
- band member recruiting
- equipment marketplace
- broad community groups
- artist recommendation engine
- event ticketing or in-app booking
- complex social feeds
- algorithmic discovery across France
- multiple cities at launch
- advanced search and filters
- full dating-app feature parity
- music streaming playback inside the app
- monetization optimization in MVP
- exact-location sharing
- multiple external music connectors
- broad multi-purpose social matching

## MVP Build Vs Pilot Operations
### Must Build Now
- Mandatory music preference onboarding
- Profile state machine with `draft`, `pending_review`, `active`, `reported`, `suspended`
- Moderator review queue
- Only `active` profiles in matching
- Paris-only compatibility matching
- One intent selection per user: concert companion
- One specific Paris scene or event context
- Match flow
- Basic messaging
- Reporting and blocking
- Audit log for moderation actions
- Coarse Paris location handling
- Core analytics
- Concert-plan prompt after match

### Manual Or Operational During Pilot
- Seed the first user base in Paris
- Review suspicious profiles manually
- Curate invites to maintain density
- Monitor reported content
- Manually inspect match quality
- Prompt first meetup outcomes

### Deferred Until After Proof
- Community groups
- Marketplace
- Band member discovery
- Artist recommendations
- Event logistics and ticketing
- Advanced recommendations
- Rich social graph features
- Multi-city expansion
- Dating-first mode
- Multiple enrichment connectors

## Business Model Hypothesis
Primary hypothesis:
- freemium matching product with paid visibility or premium match controls

Secondary later:
- local event or concert partnerships
- affiliate revenue from relevant music experiences

MVP should not optimize monetization before proving:
- users match
- users message
- users return
- matches feel meaningfully better than generic alternatives

## Critical Assumptions
- Music taste is strong enough to improve match quality
- Paris has enough density for local matching to feel worthwhile
- Users will provide accurate enough music preferences manually
- Users will trust a new platform enough to share intent
- A small number of matches can create repeat usage
- The product can avoid feeling like a generic dating clone
- Basic trust controls are sufficient for a limited pilot
- One specific Paris scene can supply enough supply for a usable pool
- Manual review can keep low-volume matching trustworthy

## How To Test Quickly
- Run a concierge pilot in Paris around one specific music scene
- Recruit concert-goers through local communities and event audiences
- Require manual entry of top artists, genres, and one identity prompt
- Test only concert-companion intent first
- Keep profile activation behind review before visibility
- Use manual moderation to maintain trust and quality
- Measure whether matches lead to messages
- Interview users after first matches to assess perceived fit
- Track repeat usage and match-to-message conversion
- Validate whether one scene generates enough density before expanding

## Acceptance Criteria
- A user can onboard with required music preferences in under 3 minutes
- A user can choose concert-companion intent clearly
- A profile cannot appear in matching before moderator approval
- Only `active` profiles appear in match results
- The app can show a small set of local compatible matches in Paris
- Matched users can exchange messages successfully
- Users can report and block others
- Reported or blocked users are removed from matching pending review
- User profiles are reviewed before becoming matchable
- Location is exposed only at coarse Paris level
- The pilot can measure match-to-message conversion
- Early users report that matches feel more relevant than generic alternatives

## Risks And Failure Modes
- Not enough density in Paris to make matching feel alive
- Music taste may be too weak alone to drive durable compatibility
- Product may collapse into a dating app with a music skin
- Users may prefer existing apps and simply mention music there
- Trust and safety issues may appear quickly in a matching context
- Manual curation may be needed longer than expected
- The app may succeed for messaging but fail to produce repeat usage
- Expanding to too many use cases too early will dilute the wedge
- Approval latency may slow activation if operations are under-resourced

## Product Readiness
Status: LIMITED

Blocking Gaps:
- The strength of music taste as a matching signal is unproven in this context [signal_validity]
- Paris density requirements are unknown and may block early match quality [density_risk]
- Trust and safety requirements for a matching product need validation before launch [trust_controls]

Required Improvements:
- Run a concierge pilot to validate match relevance and message conversion [pilot_validation]
- Confirm one specific Paris scene can supply enough density for usable matching [demand_validation]
- Maintain a minimum viable trust layer with reporting, blocking, moderator review, and immediate removal on report [trust_controls]

## Recommendation
Proceed with a narrow concierge pilot in Paris focused on concert companionship only.

Build only the matching core, mandatory music intake, review-gated activation, messaging, and trust controls needed to prove value and safety.

Do not add the broader ecosystem yet.
Do not include marketplace, band discovery, community groups, artist recommendations, or multiple external music connectors in MVP.

The fastest path to a decision is to prove one thing:
- whether shared music taste creates enough matching value to justify a standalone product

If the pilot does not show strong match relevance, usable density, and repeat usage, the project should be revised into a tighter concert-companion utility or rejected as a standalone product.