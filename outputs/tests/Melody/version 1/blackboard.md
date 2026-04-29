# Blackboard

## Project Brief

Project Name: Melody

Pitch:
A social and dating platform built around music compatibility.

The app helps music lovers connect through shared musical tastes, discover new artists, attend concerts together, find band members, and participate in local music communities.

Context:
Music plays a central role in many people's identity, relationships, and social lives. Traditional dating apps rarely account for deep lifestyle compatibility, and music communities are fragmented across multiple platforms.

Melody aims to combine relationship matching, music discovery, and community interaction into one platform.

Target Users:
- Music enthusiasts
- Amateur musicians
- Concert-goers
- Singles looking for deeper compatibility
- People looking for band members
- Music communities

Potential Use Cases:
- Dating based on music compatibility
- Finding concert partners
- Discovering new artists
- Finding musicians to jam with
- Buying/selling music equipment
- Joining local music communities

Platform Capabilities:
- Music taste onboarding
- Compatibility scoring
- Messaging
- Concert discovery
- Community groups
- Music marketplace
- Artist recommendations

Constraints:
- Need access to music preference data
- Must avoid becoming "just another dating app"
- Need strong early retention loop
- Limited initial funding

Challenges:
- Building enough user density
- Prioritizing features for MVP
- Competing with existing dating/social platforms
- Defining a sustainable business model

Long-term Vision:
Become the leading social ecosystem for people whose identity is deeply tied to music.

## Project Brief Source

projects/project-Melody.md

## Workflow Stage

first_pass_locked

## Source Version

_Aucun contenu._

## CEO Evaluation

_Aucun contenu._

## Artifacts

## Architecture Markdown Ready

True


## Architecture Visual Ready

True


## Architecture Visual Warning

_Aucun contenu._


## Architecture Mermaid Ready

True


## Architecture Mermaid Source

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/Melody/version 1/architecture-diagram.mmd


## Architecture Image Ready

True


## Architecture Image Path

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/Melody/version 1/architecture-diagram.png


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### untagged
- The strength of music taste as a matching signal is unproven in this context

### quality_assurance
- [quality_assurance] Paris density requirements are unknown and may block early match quality

### privacy_trust
- [privacy_trust] Trust and safety requirements for a matching product need validation before launch

## Product Required Improvements

### market_motion
- [market_motion] Run a concierge pilot to validate match relevance and message conversion

### demand_validation
- [demand_validation] Confirm one specific Paris scene can supply enough density for usable matching

### privacy_trust
- [privacy_trust] Maintain a minimum viable trust layer with reporting, blocking, moderator review, and immediate removal on report

## Tech Status

LIMITED


## Tech Blocking Gaps

### market_motion
- [market_motion] The minimum profile quality-control mechanism was not fully specified and must be enforced before activation

### quality_assurance
- [quality_assurance] The profile state model needs a hard `pending_review` gate to prevent low-quality supply from entering matching

### privacy_trust
- [privacy_trust] Moderation handling is missing an explicit audit trail and review queue for trust enforcement

## Tech Required Improvements

### quality_assurance
- [quality_assurance] Define and implement the required music submission schema and completeness rules
- [quality_assurance] Add a profile state machine with `draft`, `pending_review`, `active`, `reported`, and `suspended` states
- [quality_assurance] Build a small admin review console with logged moderation actions

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] The launch audience is still too broad and needs one scene-based wedge before launch can be credible.
- [market_motion] The first acquisition motion is not tied to a measurable density target.
- [market_motion] The activation threshold for moving profiles from pending to matchable is undefined.
- [market_motion] The required manual music fields are not explicitly specified as mandatory before activation.

## Growth Required Improvements

### market_motion
- [market_motion] Choose one Paris scene and define it as the only initial market segment.
- [market_motion] Set a pilot density target for the first cohort and use it as the launch gate.
- [market_motion] Define the exact mandatory music fields and the activation rule for matchability.
- [market_motion] Tie founder-led sourcing to a repeatable outreach channel from venues or communities.

## Global Status

LIMITED


## Global Blocking Gaps

### untagged
- The strength of music taste as a matching signal is unproven in this context

### quality_assurance
- [quality_assurance] Paris density requirements are unknown and may block early match quality
- [quality_assurance] The profile state model needs a hard `pending_review` gate to prevent low-quality supply from entering matching

### privacy_trust
- [privacy_trust] Trust and safety requirements for a matching product need validation before launch
- [privacy_trust] Moderation handling is missing an explicit audit trail and review queue for trust enforcement

### market_motion
- [market_motion] The minimum profile quality-control mechanism was not fully specified and must be enforced before activation
- [market_motion] The launch audience is still too broad and needs one scene-based wedge before launch can be credible.
- [market_motion] The first acquisition motion is not tied to a measurable density target.
- [market_motion] The activation threshold for moving profiles from pending to matchable is undefined.
- [market_motion] The required manual music fields are not explicitly specified as mandatory before activation.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot to validate match relevance and message conversion
- [market_motion] Choose one Paris scene and define it as the only initial market segment.
- [market_motion] Set a pilot density target for the first cohort and use it as the launch gate.
- [market_motion] Define the exact mandatory music fields and the activation rule for matchability.
- [market_motion] Tie founder-led sourcing to a repeatable outreach channel from venues or communities.

### demand_validation
- [demand_validation] Confirm one specific Paris scene can supply enough density for usable matching

### privacy_trust
- [privacy_trust] Maintain a minimum viable trust layer with reporting, blocking, moderator review, and immediate removal on report

### quality_assurance
- [quality_assurance] Define and implement the required music submission schema and completeness rules
- [quality_assurance] Add a profile state machine with `draft`, `pending_review`, `active`, `reported`, and `suspended` states
- [quality_assurance] Build a small admin review console with logged moderation actions

## Known Tags

- privacy_trust
- market_motion
- quality_assurance
- operations
- demand_validation
- untagged
- scope


## Correction Loop

## Triggered

Yes


## Current Loop Count

2


## Max Loops

2


## Initial Global Status

LIMITED


## Final Outcome

LIMITED


## Correction Tasks

### Loop 1

#### Tech Task

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Paris density requirements are unknown and may block early match quality The music data ingestion path is not defined strongly enough to guarantee usable compatibility inputs Make manual music entry a required fallback and define the primary external connector if used


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to validate match relevance and message conversion Confirm whether dating-first or concert-companion-first performs better in the pilot Define a Paris pilot density target and only launch once it is reachable


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The primary wedge is not yet fixed, so the launch message and first cohort are still ambiguous Choose one launch wedge: dating-first or concert-companion-first


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- growth


### Loop 2

#### Tech Task

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Paris density requirements are unknown and may block early match quality The minimum music submission schema is not yet fixed, so quality control cannot be enforced consistently Add a hard profile state machine with `pending_review` and `active` states


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to validate match relevance and message conversion The activation threshold for moving profiles from pending to matchable is undefined Define the required manual music fields and make them mandatory before activation The launch audience is still too broad and needs a single scene-based wedge The first acquisition motion is not yet tied to a measurable density target Commit to one primary acquisition motion, led by founder sourcing from live-music venues and communities


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The optional external music connector has not been chosen, so ingestion reliability is unresolved Select at most one enrichment connector, or proceed manual-only for the MVP The product’s primary intent remains split between dating and companionship, which weakens launch focus Decide the first intent as concert-companion-first, with dating as secondary only after match


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech
- growth


## Readiness History

### Loop 1 before

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### untagged
- The strength of music taste as a matching signal is unproven in this context
- The minimum density required to make Paris feel active is unknown

### quality_assurance
- [quality_assurance] Paris density requirements are unknown and may block early match quality
- [quality_assurance] The music data ingestion path is not defined strongly enough to guarantee usable compatibility inputs

### privacy_trust
- [privacy_trust] Trust and safety requirements for a dating-adjacent product need validation before launch
- [privacy_trust] The trust and moderation workflow is not yet specified enough for a dating-adjacent product
- [privacy_trust] Trust and safety expectations for a dating-adjacent product are not yet hardened enough for broad launch

### operations
- [operations] The minimum user density model for Paris is not operationalized into the product

### scope
- [scope] The primary wedge is not yet fixed, so the launch message and first cohort are still ambiguous

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot to validate match relevance and message conversion
- [market_motion] Confirm whether dating-first or concert-companion-first performs better in the pilot
- [market_motion] Define a Paris pilot density target and only launch once it is reachable

### privacy_trust
- [privacy_trust] Define and enforce a minimum viable trust layer with reporting, blocking, and profile moderation
- [privacy_trust] Add moderation states, audit logging, and admin review actions before launch
- [privacy_trust] Implement a minimum viable trust layer before opening the product to public users

### quality_assurance
- [quality_assurance] Make manual music entry a required fallback and define the primary external connector if used

### untagged
- Define the Paris launch gating rule for profile surfacing and feed availability

### scope
- [scope] Choose one launch wedge: dating-first or concert-companion-first

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Paris density requirements are unknown and may block early match quality The music data ingestion path is not defined strongly enough to guarantee usable compatibility inputs Make manual music entry a required fallback and define the primary external connector if used


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to validate match relevance and message conversion Confirm whether dating-first or concert-companion-first performs better in the pilot Define a Paris pilot density target and only launch once it is reachable


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The primary wedge is not yet fixed, so the launch message and first cohort are still ambiguous Choose one launch wedge: dating-first or concert-companion-first


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


### Loop 1 after

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### untagged
- The strength of music taste as a matching signal is unproven in this context

### quality_assurance
- [quality_assurance] Paris density requirements are unknown and may block early match quality
- [quality_assurance] The minimum music submission schema is not yet fixed, so quality control cannot be enforced consistently

### privacy_trust
- [privacy_trust] Trust and safety requirements for a matching product need validation before launch

### market_motion
- [market_motion] The activation threshold for moving profiles from pending to matchable is undefined
- [market_motion] The launch audience is still too broad and needs a single scene-based wedge
- [market_motion] The first acquisition motion is not yet tied to a measurable density target

### scope
- [scope] The optional external music connector has not been chosen, so ingestion reliability is unresolved
- [scope] The product’s primary intent remains split between dating and companionship, which weakens launch focus

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot to validate match relevance and message conversion
- [market_motion] Define the required manual music fields and make them mandatory before activation
- [market_motion] Commit to one primary acquisition motion, led by founder sourcing from live-music venues and communities

### privacy_trust
- [privacy_trust] Define and enforce a minimum viable trust layer with reporting, blocking, and profile moderation

### demand_validation
- [demand_validation] Confirm whether one Paris music scene can supply enough density for usable matching
- [demand_validation] Choose one Paris micro-scene and define the first invite list size needed for usable match density

### quality_assurance
- [quality_assurance] Add a hard profile state machine with `pending_review` and `active` states

### scope
- [scope] Select at most one enrichment connector, or proceed manual-only for the MVP
- [scope] Decide the first intent as concert-companion-first, with dating as secondary only after match

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Paris density requirements are unknown and may block early match quality The music data ingestion path is not defined strongly enough to guarantee usable compatibility inputs Make manual music entry a required fallback and define the primary external connector if used


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to validate match relevance and message conversion Confirm whether dating-first or concert-companion-first performs better in the pilot Define a Paris pilot density target and only launch once it is reachable


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The primary wedge is not yet fixed, so the launch message and first cohort are still ambiguous Choose one launch wedge: dating-first or concert-companion-first


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


### Loop 2 before

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### untagged
- The strength of music taste as a matching signal is unproven in this context

### quality_assurance
- [quality_assurance] Paris density requirements are unknown and may block early match quality
- [quality_assurance] The minimum music submission schema is not yet fixed, so quality control cannot be enforced consistently

### privacy_trust
- [privacy_trust] Trust and safety requirements for a matching product need validation before launch

### market_motion
- [market_motion] The activation threshold for moving profiles from pending to matchable is undefined
- [market_motion] The launch audience is still too broad and needs a single scene-based wedge
- [market_motion] The first acquisition motion is not yet tied to a measurable density target

### scope
- [scope] The optional external music connector has not been chosen, so ingestion reliability is unresolved
- [scope] The product’s primary intent remains split between dating and companionship, which weakens launch focus

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot to validate match relevance and message conversion
- [market_motion] Define the required manual music fields and make them mandatory before activation
- [market_motion] Commit to one primary acquisition motion, led by founder sourcing from live-music venues and communities

### privacy_trust
- [privacy_trust] Define and enforce a minimum viable trust layer with reporting, blocking, and profile moderation

### demand_validation
- [demand_validation] Confirm whether one Paris music scene can supply enough density for usable matching
- [demand_validation] Choose one Paris micro-scene and define the first invite list size needed for usable match density

### quality_assurance
- [quality_assurance] Add a hard profile state machine with `pending_review` and `active` states

### scope
- [scope] Select at most one enrichment connector, or proceed manual-only for the MVP
- [scope] Decide the first intent as concert-companion-first, with dating as secondary only after match

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Paris density requirements are unknown and may block early match quality The minimum music submission schema is not yet fixed, so quality control cannot be enforced consistently Add a hard profile state machine with `pending_review` and `active` states


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to validate match relevance and message conversion The activation threshold for moving profiles from pending to matchable is undefined Define the required manual music fields and make them mandatory before activation The launch audience is still too broad and needs a single scene-based wedge The first acquisition motion is not yet tied to a measurable density target Commit to one primary acquisition motion, led by founder sourcing from live-music venues and communities


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The optional external music connector has not been chosen, so ingestion reliability is unresolved Select at most one enrichment connector, or proceed manual-only for the MVP The product’s primary intent remains split between dating and companionship, which weakens launch focus Decide the first intent as concert-companion-first, with dating as secondary only after match


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


### Loop 2 after

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### untagged
- The strength of music taste as a matching signal is unproven in this context

### quality_assurance
- [quality_assurance] Paris density requirements are unknown and may block early match quality
- [quality_assurance] The profile state model needs a hard `pending_review` gate to prevent low-quality supply from entering matching

### privacy_trust
- [privacy_trust] Trust and safety requirements for a matching product need validation before launch
- [privacy_trust] Moderation handling is missing an explicit audit trail and review queue for trust enforcement

### market_motion
- [market_motion] The minimum profile quality-control mechanism was not fully specified and must be enforced before activation
- [market_motion] The launch audience is still too broad and needs one scene-based wedge before launch can be credible.
- [market_motion] The first acquisition motion is not tied to a measurable density target.
- [market_motion] The activation threshold for moving profiles from pending to matchable is undefined.
- [market_motion] The required manual music fields are not explicitly specified as mandatory before activation.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot to validate match relevance and message conversion
- [market_motion] Choose one Paris scene and define it as the only initial market segment.
- [market_motion] Set a pilot density target for the first cohort and use it as the launch gate.
- [market_motion] Define the exact mandatory music fields and the activation rule for matchability.
- [market_motion] Tie founder-led sourcing to a repeatable outreach channel from venues or communities.

### demand_validation
- [demand_validation] Confirm one specific Paris scene can supply enough density for usable matching

### privacy_trust
- [privacy_trust] Maintain a minimum viable trust layer with reporting, blocking, moderator review, and immediate removal on report

### quality_assurance
- [quality_assurance] Define and implement the required music submission schema and completeness rules
- [quality_assurance] Add a profile state machine with `draft`, `pending_review`, `active`, `reported`, and `suspended` states
- [quality_assurance] Build a small admin review console with logged moderation actions

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Paris density requirements are unknown and may block early match quality The minimum music submission schema is not yet fixed, so quality control cannot be enforced consistently Add a hard profile state machine with `pending_review` and `active` states


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to validate match relevance and message conversion The activation threshold for moving profiles from pending to matchable is undefined Define the required manual music fields and make them mandatory before activation The launch audience is still too broad and needs a single scene-based wedge The first acquisition motion is not yet tied to a measurable density target Commit to one primary acquisition motion, led by founder sourcing from live-music venues and communities


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The optional external music connector has not been chosen, so ingestion reliability is unresolved Select at most one enrichment connector, or proceed manual-only for the MVP The product’s primary intent remains split between dating and companionship, which weakens launch focus Decide the first intent as concert-companion-first, with dating as secondary only after match


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] **Hard profile state machine**
- [tech] `draft` → `pending_review` → `active` → `reported` / `suspended`
- [tech] only `active` profiles appear in matching
- [tech] moderators can move profiles back to `pending_review` or suspend them

## Growth Structural Decisions

### growth
- [growth] Define **one specific Paris scene** as the launch wedge instead of “music lovers” broadly. [market_motion]
- [growth] Make **music onboarding fields mandatory** before a profile becomes matchable, and specify the minimum set required for activation. [quality_assurance]

## Product Locking

## Applied

True


## Confirmed In Scope

- Paris-only concert-companion matching
- Mandatory music onboarding with top artists, genres, and one identity prompt
- One primary intent: concert companion
- One specific Paris scene or event context
- Profile review before visibility
- `draft` → `pending_review` → `active` → `reported` / `suspended`
- Only `active` profiles in matching
- Basic matching, messaging, reporting, blocking, audit log
- Coarse Paris-level location filtering


## Confirmed Deferred

- Dating-first mode
- Band member discovery
- Equipment marketplace
- Broad community groups
- Artist recommendation engine
- Event ticketing or booking
- Advanced recommendations
- Rich social graph features
- Multi-city expansion
- Multiple external music connectors
- Monetization optimization


## Confirmed Out Of Scope

- Broad music social network launch
- Full dating-app feature parity
- Multiple intents at launch
- General-purpose marketplace
- Exact-location sharing


## Locking Note

- The MVP remains intentionally narrow: prove one Paris concert-companion workflow before any expansion. - Optional manual-only enrichment stays operational, not product scope. - No additional wedge, intent, or ecosystem layer is added in this locking pass.


## Expert Contributions

### Tech Summary

The main feasibility issue is not feature breadth but **whether low-volume Paris supply can be kept high-quality enough to trust the matching pool**. The MVP should therefore be built around a hard review gate, a small state machine, and manual moderation support, with everything else kept minimal and deterministic.

## Tech Structural Decisions

- **Hard profile state machine**
- `draft` → `pending_review` → `active` → `reported` / `suspended`
- only `active` profiles appear in matching
- moderators can move profiles back to `pending_review` or suspend them


## Tech Recommendations

- Add an explicit `pending_review` state before any profile becomes discoverable [quality_assurance]
- Define the minimum required onboarding schema for activation: top artists, genres, identity prompt, intent, and Paris scene [quality_assurance]
- Clarify that only `active` profiles can appear in match results [scope]
- Add a moderator review queue and audit log to the MVP scope [operations]
- Specify that report/block actions immediately remove a user from matching pending review [privacy_trust]


## Tech Risks

- Manual review may become a bottleneck if invite volume grows faster than expected [operations]
- Weak or inconsistent music input will reduce match quality even if the product works technically [quality_assurance]
- Abuse or spam may bypass review if submission rules are too loose [privacy_trust]


## Tech Open Questions

- What exact fields are mandatory for a profile to move from `draft` to `pending_review`?
- How many profiles per day can the team manually review during the pilot?
- Should approval be required before first visibility, or only before first match?


### Growth Summary

The main launch challenge is not product completeness but density: Melody needs one scene-based Paris cohort large enough to produce trustworthy matches and prove that music taste is a real compatibility signal. The recommended direction is a founder-led concierge pilot focused only on concert companionship in one Paris scene, with mandatory music input and a strict activation gate.

## Growth Structural Decisions

- Define **one specific Paris scene** as the launch wedge instead of “music lovers” broadly. [market_motion]
- Make **music onboarding fields mandatory** before a profile becomes matchable, and specify the minimum set required for activation. [quality_assurance]


## Growth Recommendations

- Define **one specific Paris scene** as the launch wedge instead of “music lovers” broadly. [market_motion]
- Make **music onboarding fields mandatory** before a profile becomes matchable, and specify the minimum set required for activation. [quality_assurance]
- Add a **clear activation threshold** for when a profile becomes visible or matchable, based on completed music inputs. [scope]
- Remove or clearly defer non-wedge use cases from the MVP framing so the launch is not interpreted as a multi-purpose music platform. [scope]
- Add a measurable **first-market motion** tied to founder-led sourcing from venues and communities, with a target volume for the pilot cohort. [market_motion]


## Growth Risks

- The chosen Paris scene may be too small to sustain useful matching.
- Users may treat the product like a dating app despite the concert-companion framing.
- Music taste may not be strong enough on its own to drive repeated usage.


## Growth Open Questions

- Which exact Paris music scene will be the first wedge?
- What is the minimum viable number of activated users needed before launch is credible?
- Which mandatory music fields are required before activation?


## Product Arbitration

## Source

parsed


## Retained

- Define the wedge as Paris-only concert-companion matching
- Make concert companion the sole first intent
- Require mandatory music onboarding
- Use top artists, genres, and one identity prompt as the minimum music schema
- Use a hard profile state machine
- Add `pending_review` before any profile becomes visible
- Restrict matching to `active` profiles only
- Include moderator review queue and audit log
- Keep basic messaging after match
- Keep reporting and blocking
- Remove users from matching pending review after report or block
- Keep coarse Paris-level location filtering
- Keep only one specific Paris scene or event context
- Keep one optional manual-only enrichment source, not a product dependency


## Deferred

- Dating-first mode
- Band member recruiting
- Equipment marketplace
- Broad community groups
- Artist recommendation engine
- Event ticketing or booking
- Multiple cities
- Advanced recommendations
- Rich social graph features
- Multiple external music connectors
- Monetization optimization


## Rejected

- Broad music social network launch
- Full dating-app feature parity
- Multiple intents at launch
- Multiple external music connectors in MVP
- General-purpose marketplace in MVP
- Exact-location sharing


## Open Points

- Which exact Paris music scene should be the first wedge?
- What is the minimum viable manual review capacity during pilot operations?
- What exact threshold should move a profile from `pending_review` to `active`?
- Is one optional manual-only enrichment source needed at all, or can the MVP run fully manual?


## Rationales

- The strongest proof path is a single intent and a single local use case
- Review gating is necessary because low-volume matching trust is a core adoption risk
- Optional enrichment is not needed to prove value unless manual onboarding quality proves insufficient
- Dating should remain secondary to avoid product ambiguity and category confusion
- Extra use cases would dilute density and delay proof of the core matching loop


## Reconciliation Notes

- Parsed Product Arbitration supplied by Product; heuristic reconciliation was not needed.


## Reconciliation Warnings

_Aucune contradiction détectée._


## Source PRD

_Aucun contenu._

## Initial PRD

# Melody MVP Product Proposal

## Product Problem
Music is a strong identity signal, but people currently have to use separate tools for different outcomes: dating apps for romance, social platforms for community, concert apps for events, and classifieds for gear or bandmates. The result is fragmented discovery and weak compatibility matching.

Melody should not try to be a general music social network at launch. The product problem to solve first is:
- help Paris-based music lovers find one meaningful connection through shared taste
- turn that shared taste into a concrete meetup context
- prove that music compatibility creates better intent and retention than generic social matching

## Initial Wedge
A narrow, city-specific matching product for:
- music fans in Paris who want a concert companion or a dating match based on shared taste

The wedge is not “all music social use cases.”  
The wedge is:
- “Find one compatible person in Paris for a concert or date, based on music taste”

This is the smallest credible use case that can prove:
- music taste is a useful matching signal
- users will act on the match
- local density can create a repeatable loop

## First Target User
Primary target:
- Singles in Paris, aged roughly 22–35, who actively use music as part of identity and want dating with deeper compatibility

Secondary, only if needed for density:
- concert-goers in Paris who want a companion, regardless of dating intent

Not first target:
- band-member seekers
- marketplace users
- general communities
- broad music discovery users

## Existing Alternatives And Switching Trigger
Current alternatives:
- Tinder / Bumble / Hinge for dating
- Spotify social sharing for taste signaling
- Resident Advisor, Shotgun, Dice, Bandsintown for concerts
- Facebook groups, Discord, Reddit, WhatsApp for music communities
- LeBonCoin / Facebook Marketplace for gear
- MeetUp or informal groups for social matching

Switching trigger:
- existing dating apps do not make music taste a first-class compatibility engine
- users want matches with a higher likelihood of shared lifestyle and event attendance
- users want a concrete next step, not endless messaging
- in Paris, a local, music-based match can feel more relevant than generic swiping

## Core MVP Workflow
1. User signs up and connects music preference data or selects favorite artists/genres manually.
2. User chooses one intent: dating or concert companion.
3. App shows a small set of local profiles in Paris with high music compatibility.
4. User likes, skips, or matches.
5. On match, users can message briefly and propose a concert or meetup.
6. User returns because new high-fit matches are periodically surfaced.

The workflow must prove:
- taste-based matching
- local relevance
- quick path to first interaction

## In Scope
- Paris-only user matching
- account creation and basic profile
- music taste onboarding from connected data or manual selection
- simple compatibility score based on shared artists/genres
- intent selection: dating or concert companion
- swipe or list-based match flow
- basic messaging after match
- lightweight profile fields relevant to music identity
- location filtering within Paris and nearby areas
- basic moderation/reporting
- basic analytics for match and message conversion

## Out of Scope
- band member recruiting
- equipment marketplace
- broad community groups
- artist recommendation engine
- event ticketing or in-app booking
- complex social feeds
- algorithmic discovery across France
- multiple cities at launch
- advanced search and filtering
- verification beyond basic trust controls
- monetization features beyond a simple premium hypothesis
- full dating-app feature parity
- music streaming playback inside the app

## MVP Build Vs Pilot Operations
### Must Build Now
- Music taste onboarding
- Paris-based compatibility matching
- Intent selection
- Match acceptance flow
- Basic messaging
- Basic reporting/blocking
- Minimal profile presentation
- Core analytics

### Manual Or Operational During Pilot
- Seed the first user base in Paris
- Manually review suspicious profiles if needed
- Curate early invites to maintain density
- Manually match-test compatibility logic
- Moderate reported content
- Encourage first meetup outcomes through email or in-app prompts

### Deferred Until After Proof
- Community groups
- Marketplace
- Band member discovery
- Artist recommendations
- Event logistics and ticketing
- Advanced recommendations
- Rich social graph features
- Multi-city expansion

## Business Model Hypothesis
Primary hypothesis:
- freemium dating/social product with a paid tier for more visibility, more likes, or advanced match filtering

Secondary hypothesis later:
- local concert/event partnerships or affiliate revenue

For MVP purposes, monetization should not be optimized before proving:
- users match
- users message
- users return
- users report meaningful outcomes

## Critical Assumptions
- Music taste is a strong enough signal to improve match quality
- Paris has enough density for local matching to feel worthwhile
- Users will import or provide accurate music preference data
- Users will trust a new platform enough to share dating intent
- A small number of matches can create repeat usage
- The product can avoid feeling like a generic dating clone
- The app can generate enough early safety and trust for users to engage

## How To Test Quickly
- Run a concierge pilot in Paris with a limited user cohort
- Recruit music-first singles through local communities and concert audiences
- Ask users to connect music data or manually choose top artists/genres
- Test simple compatibility scoring against user-reported relevance
- Measure whether matches lead to messaging and proposed meetups
- Interview users after the first match to assess perceived fit
- Compare retention against intent clarity and match quality
- Test whether “concert companion” feels less risky than pure dating as an entry point

## Acceptance Criteria
- A user can onboard with music preferences in under 3 minutes
- A user can clearly choose dating or concert companion intent
- The app can show a small set of local compatible matches in Paris
- At least one out of every meaningful cohort test users reports that matches feel more relevant than generic dating apps
- Matched users can exchange messages successfully
- Users can report/block others
- The product can demonstrate repeat usage in a pilot cohort
- The team can identify at least one reliable retention loop

## Risks And Failure Modes
- Not enough density in Paris to make matching feel alive
- Music taste may be too weak alone to drive durable compatibility
- Product may collapse into “dating app with a music skin”
- Users may prefer to use existing apps and simply mention music there
- Trust and safety issues may appear quickly in dating contexts
- Manual curation may be required longer than expected
- The app may succeed for conversation but fail to produce meetups or retention
- Expanding to too many use cases too early will dilute the wedge

## Product Readiness
Status: LIMITED

Blocking Gaps:
- The strength of music taste as a matching signal is unproven in this context [signal_validity]
- Paris density requirements are unknown and may block early match quality [density_risk]
- Trust and safety needs for a dating-adjacent product must be validated before launch [trust_safety]

Required Improvements:
- Run a concierge pilot to validate match relevance and meetup intent [pilot_validation]
- Define a minimum viable trust layer for reporting, blocking, and profile hygiene [trust_controls]
- Test whether the product is stronger as dating-first or concert-companion-first [positioning_test]

## Recommendation
Proceed with a narrow concierge pilot in Paris focused on music-based dating and concert companionship only.

Do not build the broader ecosystem yet.  
Do not include marketplace, band discovery, community groups, or artist recommendations in MVP.

The fastest path to a decision is to prove one thing:
- whether shared music taste creates enough matching value to justify a standalone product

If the pilot fails to show strong match relevance and repeat usage, the project should be revised into a concert-companion utility or rejected as a standalone dating/social product.

## Retained Decisions

- Define the wedge as Paris-only concert-companion matching
- Make concert companion the sole first intent
- Require mandatory music onboarding
- Use top artists, genres, and one identity prompt as the minimum music schema
- Use a hard profile state machine
- Add `pending_review` before any profile becomes visible
- Restrict matching to `active` profiles only
- Include moderator review queue and audit log
- Keep basic messaging after match
- Keep reporting and blocking
- Remove users from matching pending review after report or block
- Keep coarse Paris-level location filtering
- Keep only one specific Paris scene or event context
- Keep one optional manual-only enrichment source, not a product dependency

## Deferred Decisions

- Dating-first mode
- Band member recruiting
- Equipment marketplace
- Broad community groups
- Artist recommendation engine
- Event ticketing or booking
- Multiple cities
- Advanced recommendations
- Rich social graph features
- Multiple external music connectors
- Monetization optimization

## Rejected Recommendations

- Broad music social network launch
- Full dating-app feature parity
- Multiple intents at launch
- Multiple external music connectors in MVP
- General-purpose marketplace in MVP
- Exact-location sharing

## Unresolved Tensions

- Tech recommendation needing arbitration: Define the minimum required onboarding schema for activation: top artists, genres, identity prompt, intent, and Paris scene [quality_assurance]
- Tech recommendation needing arbitration: Clarify that only `active` profiles can appear in match results [scope]
- Tech recommendation needing arbitration: Add a moderator review queue and audit log to the MVP scope [operations]
- Tech recommendation needing arbitration: Specify that report/block actions immediately remove a user from matching pending review [privacy_trust]
- Growth recommendation needing arbitration: Make **music onboarding fields mandatory** before a profile becomes matchable, and specify the minimum set required for activation. [quality_assurance]
- Growth recommendation needing arbitration: Add a **clear activation threshold** for when a profile becomes visible or matchable, based on completed music inputs. [scope]
- Growth recommendation needing arbitration: Remove or clearly defer non-wedge use cases from the MVP framing so the launch is not interpreted as a multi-purpose music platform. [scope]
- Growth recommendation needing arbitration: Add a measurable **first-market motion** tied to founder-led sourcing from venues and communities, with a target volume for the pilot cohort. [market_motion]
- Tech open question: What exact fields are mandatory for a profile to move from `draft` to `pending_review`?
- Tech open question: How many profiles per day can the team manually review during the pilot?
- Tech open question: Should approval be required before first visibility, or only before first match?
- Growth open question: Which exact Paris music scene will be the first wedge?
- Growth open question: What is the minimum viable number of activated users needed before launch is credible?
- Growth open question: Which mandatory music fields are required before activation?

## Applied Changes

- Define the wedge as Paris-only concert-companion matching
- Make concert companion the sole first intent
- Require mandatory music onboarding
- Use top artists, genres, and one identity prompt as the minimum music schema
- Use a hard profile state machine
- Add `pending_review` before any profile becomes visible
- Restrict matching to `active` profiles only
- Include moderator review queue and audit log
- Keep basic messaging after match
- Keep reporting and blocking
- Remove users from matching pending review after report or block
- Keep coarse Paris-level location filtering
- Keep only one specific Paris scene or event context
- Keep one optional manual-only enrichment source, not a product dependency

## Remaining Open Points

- Which exact Paris music scene should be the first wedge?
- What is the minimum viable manual review capacity during pilot operations?
- What exact threshold should move a profile from `pending_review` to `active`?
- Is one optional manual-only enrichment source needed at all, or can the MVP run fully manual?

## Risks

- Not enough density in Paris to create repeated value [density_risk]
- Music compatibility may be too weak a signal to outperform existing dating apps [signal_validity]
- The app may be perceived as a dating app with a music skin rather than a distinct product [positioning_risk]
- Sparse Paris inventory may make the feed look empty or repetitive [density_risk]
- Music data may be incomplete or unreliable, weakening match quality [data_quality]
- Without strong moderation, a dating-adjacent product will attract abuse quickly [trust_controls]
- Manual music data may still be too noisy to produce meaningful compatibility scores [quality_assurance]
- Optional connector data may be sparse or inconsistent, reducing trust in the match engine [quality_assurance]
- Too many profiles may remain stuck in review if the activation threshold is too strict [operations]
- The market is too fragmented for a broad Paris launch to feel alive [density_risk]
- The product may still be perceived as a dating app with a music layer [scope]
- Users may not convert shared taste into actual meetups [demand_validation]
- Manual review may become a bottleneck if invite volume grows faster than expected [operations]
- Weak or inconsistent music input will reduce match quality even if the product works technically [quality_assurance]
- Abuse or spam may bypass review if submission rules are too loose [privacy_trust]
- The chosen Paris scene may be too small to sustain useful matching.
- Users may treat the product like a dating app despite the concert-companion framing.
- Music taste may not be strong enough on its own to drive repeated usage.

## Open Questions

- Is the first wedge **dating** or **concert companion**?
- What minimum number of active users per Paris pocket is needed before the product feels alive?
- What exact music data source will users be most willing to connect or manually enter?
- Which music source is the primary onboarding path: Spotify, manual artists, or both?
- What minimum profile completeness is required before a user can be shown?
- How coarse should location be: city-wide Paris only, arrondissement, or neighborhood?
- What is the minimum required music schema for activation: artists only, or artists plus genres plus prompt?
- Which single music connector, if any, is reliable enough for Paris MVP?
- What threshold should move a profile from pending review to active?
- Which single Paris music scene should be used for the first pilot?
- What minimum cohort size is needed before users reliably see 3–5 relevant matches?
- Does concert-companion intent outperform dating intent in message and meetup conversion?
- What exact fields are mandatory for a profile to move from `draft` to `pending_review`?
- How many profiles per day can the team manually review during the pilot?
- Should approval be required before first visibility, or only before first match?
- Which exact Paris music scene will be the first wedge?
- What is the minimum viable number of activated users needed before launch is credible?
- Which mandatory music fields are required before activation?

## Final Revised PRD

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

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Define the wedge as Paris-only concert-companion matching
- Make concert companion the sole first intent
- Require mandatory music onboarding
- Use top artists, genres, and one identity prompt as the minimum music schema
- Use a hard profile state machine
- Add `pending_review` before any profile becomes visible
- Restrict matching to `active` profiles only
- Include moderator review queue and audit log
- Keep basic messaging after match
- Keep reporting and blocking
- Remove users from matching pending review after report or block
- Keep coarse Paris-level location filtering
- Keep only one specific Paris scene or event context
- Keep one optional manual-only enrichment source, not a product dependency

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- growth_agent: gtm_notes_generated
- tech_agent: architecture_notes_generated
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
- product_agent: arbitration_reconciled
