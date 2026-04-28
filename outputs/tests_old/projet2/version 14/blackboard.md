# Blackboard

## Project Brief

Project Name: SkillBridge

Pitch:
A digital platform designed to help young graduates and career switchers gain practical experience through short-term real-world projects proposed by small companies, startups, and non-profits.

Context:
Many graduates struggle to get hired because they lack professional experience.
At the same time, small organizations often need help on short projects but cannot afford full-time hires or expensive agencies.

The platform aims to connect both sides by allowing organizations to publish short missions (2 to 8 weeks) that candidates can complete remotely or on-site.

Target Users:
- Recent graduates
- Career changers
- Small businesses
- Startups
- Associations / NGOs

Potential Use Cases:
- UX audit for a small startup
- Social media campaign for a local business
- Data cleanup project
- Website redesign
- Market research mission
- Administrative process optimization

Platform Capabilities:
- User profiles
- Project posting
- Matching system
- Messaging
- Deliverable submission
- Feedback and reputation system

Constraints:
- Limited initial budget
- Need to build trust between both sides
- Must avoid becoming a low-quality freelance marketplace
- Legal/employment boundaries may vary depending on country

Challenges:
- Attract enough companies early on
- Ensure project quality
- Prevent abuse from companies looking for free labor
- Create enough value for candidates to stay engaged

Long-term Vision:
Become an alternative path to traditional internships and junior hiring by helping people build credible experience faster.

## Project Brief Source

outputs/project-brief.md

## Workflow Stage

first_pass_final

## Source Version

_Aucun contenu._

## CEO Evaluation

_Aucun contenu._

## Expert Contributions

### Tech Summary

The main technical challenge involves ensuring effective matching of candidates and projects while building a trustworthy platform with limited initial resources. The recommended direction is to adopt a modular monolith approach, using a combination of Django and PostgreSQL, focusing on essential features for the MVP.

## Tech Recommendations

- Clearly define user roles and permissions for candidates and organizations to ensure proper access control in user management.
- Provide detailed requirements for the types of projects organizations can post, including clarity on deliverables and project scope.
- Specify key skills or competencies to be listed in candidate profiles to enhance the matching process.
- Establish criteria for the feedback system to ensure it contributes to building trust without being misused.
- Define how legal compliance will be addressed, especially regarding user agreements and data protection.


## Tech Risks

- The effectiveness of the matching algorithm may be insufficient initially, leading to low user satisfaction.
- Legal complexities regarding employment regulations may limit user engagement or expose the platform to liability.
- Difficulty in attracting quality organizations to post projects could hinder service viability in the initial phase.


## Tech Open Questions

- What specific legal frameworks need to be considered based on the geographical areas of operation?
- How will project quality be monitored and ensured to prevent exploitation by organizations?
- What metrics will be in place to measure user engagement and satisfaction effectively post-launch?


### Growth Summary

The main growth challenge is building trust and attracting an initial base of both candidates and small organizations. The recommended GTM direction focuses on targeting recent graduates through university partnerships, while ensuring a streamlined onboarding process to enhance activation and engagement.

## Growth Recommendations

- Implement a simplified onboarding checklist for candidates to complete their profiles and apply for projects.
- Establish a verification process for organizations posting projects to build trust in the platform.
- Include a clear guideline and standard for project quality and expectations in the project posting feature.
- Develop a feedback mechanism specifically aimed at addressing concerns of candidates about project quality and company practices.
- Introduce a limited-time incentive for organizations that post their first project, such as a discount or feature enhancement, to encourage initial engagement.


## Growth Risks

- The risk of low engagement from organizations if early project quality does not meet expectations, leading to distrust from candidates.
- Potential for candidates to view the platform as a source of underpaid work or free labor, which can hinder long-term trust and platform reputation.
- High churn rate of candidates if they fail to secure projects within a short time after signing up.


## Growth Open Questions

- What specific partnerships can be established with universities or career services to enhance initial user acquisition?
- How will the platform handle variations in legal and employment regulations across different countries?
- What measures will be put in place to prevent abuse of the platform by organizations seeking free labor?


## Source PRD

_Aucun contenu._

## Initial PRD

# SkillBridge PRD

## Product Problem
Recent graduates and career switchers struggle to secure employment due to a lack of practical experience. Simultaneously, small organizations require assistance with short-term projects but face budget constraints that prevent them from hiring full-time employees or engaging costly agencies. SkillBridge aims to bridge this gap by connecting these two groups.

## Target Users
1. **Recent Graduates**: Individuals seeking to gain practical experience to enhance employability.
2. **Career Changers**: Professionals looking to transition into new fields who need relevant experience.
3. **Small Businesses**: Organizations requiring help on short projects without the resources for full-time hires.
4. **Startups**: Emerging companies needing specific project support.
5. **Associations/NGOs**: Non-profit organizations seeking assistance for various initiatives.

## Value Proposition
SkillBridge offers a platform that facilitates the connection between candidates and organizations, enabling graduates and career changers to gain valuable experience while assisting small companies and non-profits with their project needs. This creates a win-win situation, providing candidates with work experience and organizations with necessary support.

## Core Workflow
1. **User Registration**: Candidates and organizations create profiles on the platform.
2. **Project Posting**: Organizations post short-term projects detailing requirements and expectations.
3. **Matching System**: The platform suggests suitable candidates based on skills and project needs.
4. **Messaging**: Candidates and organizations communicate directly to clarify project details.
5. **Project Execution**: Candidates work on the project either remotely or on-site.
6. **Deliverable Submission**: Candidates submit work deliverables through the platform.
7. **Feedback and Reputation**: Both parties provide feedback, building a reputation system that enhances trust.

## MVP Scope
- User registration and profile creation for both candidates and organizations
- Project posting capabilities for organizations
- Basic matching system for connecting candidates with projects
- Messaging feature for communication between users
- Simple deliverable submission process
- Feedback mechanism for project completion and user ratings

## Constraints and Key Risks
- **Budget Limitations**: Initial development and operational budget may restrict feature sets and marketing efforts.
- **Trust Building**: Establishing trust between candidates and organizations is critical but challenging in the early stages.
- **Quality Assurance**: Ensuring that projects maintain a standard of quality to differentiate from low-quality freelance platforms.
- **Legal Considerations**: Navigating varying legal/employment regulations depending on the country of operation.

## Success Metrics
- Number of active users (candidates and organizations)
- Number of projects posted and completed
- User satisfaction ratings (candidates and organizations)
- Rate of successful matching between candidates and projects
- Retention rate of candidates using the platform for multiple projects

## Next Product Steps
1. Develop the MVP features as outlined.
2. Design and implement user onboarding processes to encourage profile completion and initial project engagement.
3. Initiate marketing efforts to attract early adopters among both candidates and organizations.
4. Collect user feedback post-launch to iterate and enhance platform functionality and user experience.

## Retained Decisions

_Aucune décision retenue._

## Deferred Decisions

- Tech: Clearly define user roles and permissions for candidates and organizations to ensure proper access control in user management.
- Growth: Implement a simplified onboarding checklist for candidates to complete their profiles and apply for projects.

## Rejected Recommendations

- Tech: Provide detailed requirements for the types of projects organizations can post, including clarity on deliverables and project scope.
- Tech: Establish criteria for the feedback system to ensure it contributes to building trust without being misused.
- Growth: Establish a verification process for organizations posting projects to build trust in the platform.
- Growth: Include a clear guideline and standard for project quality and expectations in the project posting feature.
- Growth: Develop a feedback mechanism specifically aimed at addressing concerns of candidates about project quality and company practices.
- Growth: Introduce a limited-time incentive for organizations that post their first project, such as a discount or feature enhancement, to encourage initial engagement.

## Unresolved Tensions

- Tech recommendation needing arbitration: Provide detailed requirements for the types of projects organizations can post, including clarity on deliverables and project scope.
- Tech recommendation needing arbitration: Specify key skills or competencies to be listed in candidate profiles to enhance the matching process.
- Tech recommendation needing arbitration: Establish criteria for the feedback system to ensure it contributes to building trust without being misused.
- Tech recommendation needing arbitration: Define how legal compliance will be addressed, especially regarding user agreements and data protection.
- Growth recommendation needing arbitration: Establish a verification process for organizations posting projects to build trust in the platform.
- Growth recommendation needing arbitration: Include a clear guideline and standard for project quality and expectations in the project posting feature.
- Growth recommendation needing arbitration: Develop a feedback mechanism specifically aimed at addressing concerns of candidates about project quality and company practices.
- Growth recommendation needing arbitration: Introduce a limited-time incentive for organizations that post their first project, such as a discount or feature enhancement, to encourage initial engagement.
- Tech open question: What specific legal frameworks need to be considered based on the geographical areas of operation?
- Tech open question: How will project quality be monitored and ensured to prevent exploitation by organizations?
- Tech open question: What metrics will be in place to measure user engagement and satisfaction effectively post-launch?
- Growth open question: What specific partnerships can be established with universities or career services to enhance initial user acquisition?
- Growth open question: How will the platform handle variations in legal and employment regulations across different countries?
- Growth open question: What measures will be put in place to prevent abuse of the platform by organizations seeking free labor?

## Applied Changes

_Aucun changement appliqué._

## Remaining Open Points

- Tech: Specify key skills or competencies to be listed in candidate profiles to enhance the matching process.
- Tech: Define how legal compliance will be addressed, especially regarding user agreements and data protection.
- Tech: What specific legal frameworks need to be considered based on the geographical areas of operation?
- Tech: How will project quality be monitored and ensured to prevent exploitation by organizations?
- Tech: What metrics will be in place to measure user engagement and satisfaction effectively post-launch?
- Growth: What specific partnerships can be established with universities or career services to enhance initial user acquisition?
- Growth: How will the platform handle variations in legal and employment regulations across different countries?
- Growth: What measures will be put in place to prevent abuse of the platform by organizations seeking free labor?
- Tech recommendation needing arbitration: Provide detailed requirements for the types of projects organizations can post, including clarity on deliverables and project scope.
- Tech recommendation needing arbitration: Specify key skills or competencies to be listed in candidate profiles to enhance the matching process.
- Tech recommendation needing arbitration: Establish criteria for the feedback system to ensure it contributes to building trust without being misused.
- Tech recommendation needing arbitration: Define how legal compliance will be addressed, especially regarding user agreements and data protection.
- Growth recommendation needing arbitration: Establish a verification process for organizations posting projects to build trust in the platform.
- Growth recommendation needing arbitration: Include a clear guideline and standard for project quality and expectations in the project posting feature.
- Growth recommendation needing arbitration: Develop a feedback mechanism specifically aimed at addressing concerns of candidates about project quality and company practices.
- Growth recommendation needing arbitration: Introduce a limited-time incentive for organizations that post their first project, such as a discount or feature enhancement, to encourage initial engagement.
- Tech open question: What specific legal frameworks need to be considered based on the geographical areas of operation?
- Tech open question: How will project quality be monitored and ensured to prevent exploitation by organizations?
- Tech open question: What metrics will be in place to measure user engagement and satisfaction effectively post-launch?
- Growth open question: What specific partnerships can be established with universities or career services to enhance initial user acquisition?
- Growth open question: How will the platform handle variations in legal and employment regulations across different countries?
- Growth open question: What measures will be put in place to prevent abuse of the platform by organizations seeking free labor?

## Risks

- The effectiveness of the matching algorithm may be insufficient initially, leading to low user satisfaction.
- Legal complexities regarding employment regulations may limit user engagement or expose the platform to liability.
- Difficulty in attracting quality organizations to post projects could hinder service viability in the initial phase.
- The risk of low engagement from organizations if early project quality does not meet expectations, leading to distrust from candidates.
- Potential for candidates to view the platform as a source of underpaid work or free labor, which can hinder long-term trust and platform reputation.
- High churn rate of candidates if they fail to secure projects within a short time after signing up.

## Open Questions

- What specific legal frameworks need to be considered based on the geographical areas of operation?
- How will project quality be monitored and ensured to prevent exploitation by organizations?
- What metrics will be in place to measure user engagement and satisfaction effectively post-launch?
- What specific partnerships can be established with universities or career services to enhance initial user acquisition?
- How will the platform handle variations in legal and employment regulations across different countries?
- What measures will be put in place to prevent abuse of the platform by organizations seeking free labor?

## Final Revised PRD

# SkillBridge PRD

## Product Problem
Recent graduates and career switchers struggle to secure employment due to a lack of practical experience. Simultaneously, small organizations require assistance with short-term projects but face budget constraints that prevent them from hiring full-time employees or engaging costly agencies. SkillBridge aims to bridge this gap by connecting these two groups.

## Target Users
1. **Recent Graduates**: Individuals seeking to gain practical experience to enhance employability.
2. **Career Changers**: Professionals looking to transition into new fields who need relevant experience.
3. **Small Businesses**: Organizations requiring help on short projects without the resources for full-time hires.
4. **Startups**: Emerging companies needing specific project support.
5. **Associations/NGOs**: Non-profit organizations seeking assistance for various initiatives.

## Value Proposition
SkillBridge offers a platform that facilitates the connection between candidates and organizations, enabling graduates and career changers to gain valuable experience while assisting small companies and non-profits with their project needs. This creates a win-win situation, providing candidates with work experience and organizations with necessary support.

## Core Workflow
1. **User Registration**: Candidates and organizations create profiles on the platform.
2. **Project Posting**: Organizations post short-term projects detailing requirements and expectations.
3. **Matching System**: The platform suggests suitable candidates based on skills and project needs.
4. **Messaging**: Candidates and organizations communicate directly to clarify project details.
5. **Project Execution**: Candidates work on the project either remotely or on-site.
6. **Deliverable Submission**: Candidates submit work deliverables through the platform.
7. **Feedback and Reputation**: Both parties provide feedback, building a reputation system that enhances trust.

## MVP Scope
- User registration and profile creation for both candidates and organizations.
- Project posting capabilities for organizations with clear guidelines on project content and expectations.
- Basic matching system for connecting candidates with projects based on listed skills and competencies.
- Messaging feature for communication between users.
- Simple deliverable submission process.
- Feedback mechanism that allows both candidates and organizations to rate each other.

## Constraints and Key Risks
- **Budget Limitations**: Initial development and operational budget may restrict feature sets and marketing efforts.
- **Trust Building**: Establishing trust between candidates and organizations is critical but challenging in the early stages.
- **Quality Assurance**: Ensuring that projects maintain a standard of quality to differentiate from low-quality freelance platforms.
- **Legal Considerations**: Navigating varying legal/employment regulations depending on the country of operation.

## Success Metrics
- Number of active users (candidates and organizations).
- Number of projects posted and completed.
- User satisfaction ratings (candidates and organizations).
- Rate of successful matching between candidates and projects.
- Retention rate of candidates using the platform for multiple projects.

## Next Product Steps
1. Develop the MVP features as outlined.
2. Design and implement user onboarding processes to encourage profile completion and initial project engagement.
3. Initiate marketing efforts to attract early adopters among both candidates and organizations.
4. Collect user feedback post-launch to iterate and enhance platform functionality and user experience.
5. Establish a verification process for organizations posting projects to foster trust.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

_Aucune décision._

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
