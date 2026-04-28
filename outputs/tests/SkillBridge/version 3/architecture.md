## Architecture Notes

**Macro Architecture Choice:**
The SkillBridge MVP will utilize a centralized web application architecture with a relational database backend for robust data management and security.

**Primary Technical Dependency or Constraint:**
Establishing a legal-compliance framework is essential for validating user interactions and project submissions, affecting both trust and viability.

**Structural Technical Decisions:**
1. **User Profile and Project Posting Management:** 
   - Build a centralized user management module that allows for role-based access control for both graduates and companies, ensuring compliant data handling.
2. **Manual Quality Review Process**: 
   - Implement a manual review step in the project posting workflow to verify project legitimacy and compliance with user safety, maintaining quality before matching.
3. **Basic Matching Algorithm**: 
   - Develop a simplistic keyword matching system that connects graduates and projects based on skills and requirements without over-engineering complex algorithms initially.

**Recommended Implementation Approach:**
- Focus on creating a phased development plan that allows for rapid testing of the core user flows (profile creation, project posting, and basic matching) with iterative user feedback.
  
**What Must Be Built Now:**
- User profile module for both graduates and organizations including relevant data fields.
- Project posting functionality with a manual quality review backend.
- Basic messaging system for candidate-organization communication.
- Essential feedback collection system to evaluate project completion.

**What Can Be Handled Manually or Operationally First:**
- Legal compliance checks can start as manual processes to validate project legitimacy rather than automated, allowing flexibility to adapt as requirements become clearer.
  
**Main Modules or Components:**
1. **User Management Module**: Handles registration, authentication, and role-specific access.
2. **Project Management Module**: Allows organizations to post projects and undergo manual review.
3. **Matching Engine**: Simple keyword-based matching logic to connect suitable candidates to projects based on skill alignment.
4. **Messaging System**: Facilitates communication between graduates and organizations.
5. **Feedback and Reputation Module**: Gathers feedback post-project completion to build trustworthiness.

**Critical Data or Workflow States:**
- User registration state: Ensure data is collected per compliance standards.
- Project submission state: Must allow for reviews and audit trails before public posting.
- Matching outcome state: Responsible for maintaining data integrity and accurate record-keeping for feedback.

**Minimum Reliability, Data, Permission, or Control Requirements:**
- User data must comply with applicable data protection regulations (e.g., GDPR) to ensure trust.
- Project postings must be verified manually to avoid low-quality or exploitative projects.
- Establish a fail-safe for feedback submissions to handle disputes or concerns.

**Control Points, Internal Tools, or Support Needs:**
- Manual review dashboard for checking project submissions and ensuring compliance.
- Reporting tools for tracking project statuses, user feedback, and overall usage metrics.
- A feedback loop mechanism that allows users to report issues with projects or experiences.

**Diagram Blueprint:**
- **Main System Blocks**: User Management, Project Management, Matching Engine, Messaging System, Feedback Module
- **Main Flows Between Blocks**: User Registration → User Profiles; Project Posting → Manual Review → Project Approval → Matching Engine → Feedback Collection → Reputation
- **External Actors or Systems**: Graduates, Companies, Manual Reviewers
- **Admin or Operations Control Points**: Manual Review Dashboard, Compliance Reporting Tool

## Review Summary
The key feasibility challenge for SkillBridge lies in ensuring legal compliance for project-based interactions, which is essential for maintaining user trust. The recommended approach is to build a minimum viable platform focusing on user profiles, project posting with manual review, and a basic matching system, while handling legal checks manually in the initial phase.

## Critical Assumptions
- Graduates are willing to engage in short-term projects without formal contracts.
- Companies will find value in utilizing the platform as a trusted source for project-based assistance.
- The manual review process of project postings will prevent exploitation and maintain quality.
- The basic matching process will sufficiently meet initial user needs for successful project engagement.
- Feedback mechanisms will provide valid insights to improve the platform continually.

## Requested Changes
- Include explicit criteria for what constitutes a legitimate project during the manual review process.
- Clarify legal obligations and potential data sensitivity issues regarding user data and project outcomes.
- Implement a mechanism to track project outcomes and gather success metrics for both parties.

## Risks
- Lack of clear legal frameworks may discourage potential users from engaging.
- Over-reliance on the manual review process may create bottlenecks and slow down platform growth.
- Risk of low-quality projects harming the platform’s reputation if not adequately filtered.
- Manual operations for legal compliance might not scale as user participation increases.
- Absence of adequate user acquisition strategies may lead to insufficient initial traction.

## Open Questions
- What specific legal frameworks need to be in place for each target country to mitigate compliance risks?
- How will we define success in the feedback system to ensure it is beneficial for both graduates and companies?
- What manual processes will need to be implemented to manage compliance effectively?
- How can we incentivize organizations to post quality projects from the start?
- What metrics will be vital for assessing project quality and user satisfaction in the MVP phase?

## Why This Could Fail Even With Good Execution
Even with competent execution, if the foundational assumptions about legal compliance and trustworthiness are incorrect or misaligned with user expectations, the platform may fail to attract and retain users, leading to a lack of projects and engagement.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- Uncertainty about the legal frameworks applicable to project-based work. 
- Insufficient clarity around compliance requirements for sensitive user data.

Required Improvements:
- [legal_navigability] Establish foundational legal frameworks to ensure compliance and trust regarding project-based work.
- [user_acquisition] Develop specific outreach strategies for attracting both recent graduates and organizations.