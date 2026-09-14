---
name: turn-idea-into-spec
description: "Act as a PM/TM to validate and land a product or feature idea: clarify problems, goals, and users; define MVP scope and acceptance criteria; produce a dev-ready PRD and technical design doc (user flows, requirements, data/API contracts, milestones, risks, launch plan). Trigger on: write PRD, write spec, design doc, tech spec, product requirements, break down tasks, plan milestones, technical design, scope MVP, acceptance criteria, delivery plan, launch plan."
---

# Turn Idea Into Spec — PM/TM Landing & Design Document

Turn "an idea" into "a ready-to-build document + an executable plan."

## Working Principles (must follow)

- Confirm context and goals first; when information is insufficient, state default assumptions and ask the user to confirm.
- Never fabricate: mark unknown business rules, data definitions, dependencies, and metrics as "Assumption / To Be Confirmed" and collect them in Open Questions.
- Deliver a usable v1 first: prioritize a structurally complete, iterable document skeleton, then iteratively fill gaps and polish.
- Output Markdown by default; only write files, execute commands, or access external networks after the user explicitly agrees.

## Quick Entry (when sufficient information is provided)

If the user has already provided: goals, users, scope, constraints, timeline, current state / tech stack — generate the "Design Document v1" directly (using the template below), then run the "Quality Checklist" to fill any gaps.

## Deliverables (default)

Ask the user for their preference first; if no preference is given, default to **single file**:

- Single file: `design-doc.md`
- Multiple files:
  - `00-validation-brief.md` (optional)
  - `10-prd.md`
  - `20-tech-design.md`
  - `30-delivery-plan.md`

## Process (4 phases, any can be skipped)

### Phase 1: Clarification & Scoping (required)

Goal: Determine what to build, what not to build, and why build it now.

Confirm at least 7 items (provide defaults for missing information and ask the user to confirm):

1. One-line goal (user value + business value)
2. Target users / usage scenarios (who uses it, when, and where)
3. Success metrics (how to judge success after launch)
4. Constraints (time / headcount / platform / compliance / dependencies)
5. Scope (MVP must-have / nice-to-have / explicitly out of scope)
6. Current state & integration points (existing systems / data / permissions to integrate with)
7. Top unknowns & risks (Top 3)

Phase output (send to user for confirmation before proceeding):

- Problem / Goals / Non-goals
- MVP Scope (Must / Should / Could)
- Open Questions (prioritized)

### Phase 2: Idea Validation (optional)

Trigger this phase when the user's goal is "validate the idea / decide whether to build it"; skip if the user has already decided to proceed.

Steps:

1. List key assumptions: user, value, feasibility, achievability (time / resources / compliance)
2. Design a minimum validation method for each assumption: interviews / prototype testing / data analysis / A/B experiment
3. Define Go/No-Go thresholds: metric + deadline + owner

Phase output:

- Assumption Map (table)
- Experiment Plan (table)
- Decision recommendation (with rationale, risks, and next steps)

### Phase 3: PRD + Technical Design (core)

Goal: Enable the engineering team to start building immediately.

Recommended writing order: user flows -> requirements -> acceptance criteria -> edge cases / errors -> technical approach -> data / API -> NFR -> testing / release.

Must include:

- User flows and critical paths (text flowchart or mermaid)
- Functional Requirements (FR) and Acceptance Criteria (AC)
- Non-Functional Requirements (NFR: performance / reliability / usability / security / privacy / observability)
- Data & interfaces (data model, API / events, permissions)
- Options & trade-offs (at least 2 options + rationale for the chosen one)
- Failure & fallback (degradation, compatibility, migration, rollback)

Phase output:

- "Design Document v1" (using the template below)

### Phase 4: Delivery Plan (TM perspective)

Goal: Turn the document into an executable plan and task breakdown.

Output:

- Milestones (by week / by phase)
- Work breakdown (Epic / Story / Task)
- Dependencies & blockers (Dependency Map)
- Test plan (unit / integration / E2E / regression / canary verification)
- Launch plan (canary release, rollback, monitoring & alerting, operations support)

---

## Table Templates (ready to reuse)

### Requirements & Acceptance Criteria (recommended)

| ID | User Story | Requirement | Acceptance Criteria | Priority | Notes |
|---:|------------|-------------|---------------------|----------|-------|
| R1 | As a… I want… | … | Given… When… Then… | P0/P1/P2 |  |

### Assumptions & Validation (Phase 2)

| Assumption | Why risky | Validation method | Success bar | Owner | Due |
|-----------|-----------|-------------------|-------------|-------|-----|

### API / Events (Phase 3)

| Name | Type | Request/Schema | Response/Effect | Auth | Errors/Retry |
|------|------|----------------|-----------------|------|--------------|

### Milestones (Phase 4)

| Milestone | Scope | Output | Owner | Start | End | Risk |
|-----------|-------|--------|-------|-------|-----|------|

---

## Design Document Template (Markdown)

> By default, generate a single `design-doc.md`. If the user prefers multiple files, split by section into the corresponding files.

# <Project/Feature Name> Design Document

- Owner: <PM/TM/Tech Lead>
- Status: Draft / Review / Approved
- Last Updated: YYYY-MM-DD
- Related Links: <PRD / Prototype / Board / Meeting Notes>

## 1. Background & Problem

- Current state: …
- Problem: …
- Why now: …

## 2. Goals & Success Metrics

- Goals: …
- Metric definitions: …
- Target values & timeline: …

## 3. Non-goals

- Out of scope for this iteration: …
- Explicitly rejected requirements: …

## 4. Users & Scenarios

- Target users: …
- Typical scenarios: …
- Key constraints: …

## 5. Scope (MVP Scope)

- Must (P0): …
- Should (P1): …
- Could (P2): …

## 6. User Flows (Critical Paths)

- Primary flow: …
- Alternative / exception flows: …

## 7. Requirements & Acceptance Criteria (FR + AC)

(Use the "Requirements & Acceptance Criteria" table)

## 8. Interaction & UI/UX

- Pages / entry points: …
- States & feedback: loading / empty state / error / insufficient permissions / success: …
- If a prototype exists: follow the prototype; if not: describe in text to an implementable level of detail.

## 9. Technical Approach Overview

- Option A: …
- Option B: …
- Decision: … (key trade-offs: cost / risk / scalability / team familiarity)

## 10. Data & Interfaces

### 10.1 Data Model

- Entities: …
- Fields: …
- Relationships: …
- Read/write paths: …

### 10.2 API / Events / Permissions

(Use the "API / Events" table; at minimum specify: authentication, idempotency, error codes / retry strategy)

## 11. Non-Functional Requirements (NFR)

- Performance: latency / throughput / capacity assumptions; load test plan (if needed)
- Reliability: degradation / rate limiting / timeout / retry / circuit breaker
- Security / Privacy: least privilege, sensitive data handling, audit trail
- Observability: logging, metrics, tracing, alert thresholds

## 12. Error Handling & Edge Cases

- Input validation: …
- Failure retry & idempotency: …
- Compatibility & migration: …

## 13. Test Plan

- Unit tests: …
- Integration tests: …
- E2E / regression: …
- Canary verification checklist: …

## 14. Release, Canary & Rollback

- Release steps: …
- Canary strategy: …
- Rollback strategy: …
- Monitoring dashboard & alerts: …

## 15. Milestones & Work Breakdown

- Milestone table (Phase 4)
- Backlog (organized as Epic -> Story -> Task; label dependencies and Definition of Done)

## 16. Risks & Mitigations

- Risk 1: … -> Mitigation: …
- Risk 2: … -> Mitigation: …

## 17. Open Questions (To Be Confirmed)

- Q1: …
- Q2: …

## 18. Decision Log

- YYYY-MM-DD: Decided on …, because …

---

## Quality Checklist (mandatory before delivery)

1. Every P0 requirement has Acceptance Criteria (AC) that are testable.
2. Critical flows include handling for exceptions / empty states / insufficient permissions / failure retries.
3. API / events specify authentication, idempotency, error codes, and retry strategy.
4. NFR items are concrete: at minimum provide metrics / assumptions / validation approach.
5. Release / canary / rollback plans are executable; monitoring and alerts are actionable.
6. All "Assumption / To Be Confirmed" items in the document are captured in Open Questions, sorted by priority.

## Example Trigger Prompts (reference for users)

- "I have an idea I want to validate and then produce a PRD + technical design doc."
- "Help me land this requirement: <description>. Include acceptance criteria, API contracts, data model, milestones, and risks."
- "I need to write a design doc (design doc / tech spec) — output in Markdown, fill in edge cases and rollback plans to a dev-ready standard."
