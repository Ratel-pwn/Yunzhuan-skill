---
name: deliverable-content-discipline
description: Keep internal reasoning, revision history, rejected alternatives, prompt echoes, and implementation explanations out of user-facing artifacts unless their readers genuinely need them and the user has confirmed their inclusion. Use whenever creating or editing documents, presentations, UI copy, code and comments, reports, messages, configurations, or other deliverables, especially when current requirements replace an earlier direction.
---

# Deliverable Content Discipline

Produce artifacts that express the current intended state cleanly. Treat the conversation, corrections, internal decisions, and working process as control input, not as content to copy into the artifact.

## Separate the work from the deliverable

Keep two layers distinct:

- **Working layer:** reasoning, prior plans, rejected options, user corrections, implementation choices, troubleshooting, and explanations of why something changed. Put this in commentary, review notes, commit or PR text, or the final handoff when useful.
- **Deliverable layer:** only the information its actual reader needs to use, review, approve, operate, or accept the current result.

When a new instruction supersedes an earlier one, rebuild the affected content from the latest approved requirements. Do not make the deliverable narrate the correction unless change history is itself required.

## Default rules

1. State the current truth directly and affirmatively.
2. Do not echo the prompt, the user's criticism, or the fact that an instruction was followed.
3. Do not add explanations merely to prove that an earlier idea was considered and rejected.
4. Do not scatter exclusions or strategic decisions through unrelated sections. If a boundary may be necessary, keep it out of the artifact until the user confirms its reason, wording, and placement; after confirmation, put it once in the natural scope, assumptions, compatibility, or limitations section.
5. Do not add revision commentary to source code. Comments should explain a non-obvious current invariant, constraint, or interface contract, not the conversation that produced it.
6. Do not expose internal product, commercial, staffing, or strategic reasoning in UI copy, customer materials, configuration, sample data, or generated content unless the intended audience needs it.
7. Keep change explanations outside the artifact unless the artifact's purpose is itself a changelog, migration guide, decision record, audit trail, review, tutorial, or explanatory report.

## History and negative-statement gate

Before including wording such as `此前`, `原计划`, `本版本取消`, `不再`, `移除`, `改为`, `根据沟通`, `按要求`, `而不是`, `无需`, `为什么`, `previously`, `removed`, or `no longer`, ask:

1. Does the intended reader need this history to act correctly or avoid a material misunderstanding?
2. Is the statement explicitly required for scope, legal, compliance, audit, migration, compatibility, security, or acceptance purposes?
3. Is this the single best location for it?

If the answer is no, remove the history and write only the current state. If yes, do not insert it yet: pass it through the user-confirmation gate below.

## Required user-confirmation gate

Historical or negative framing and explicit scope-boundary statements require user confirmation before they enter an artifact. Agent judgment can identify a candidate but cannot authorize its inclusion.

Outside the artifact, present:

1. The exact proposed wording.
2. The reader-facing reason it may be necessary.
3. The material misunderstanding, acceptance risk, legal or technical risk it prevents.
4. The single proposed location in the artifact.
5. Whether it replaces or duplicates any existing statement.

Then ask the user to confirm inclusion. A general request to create, revise, or finish the artifact is not confirmation of this candidate. If the user does not respond, gives an ambiguous response, or declines, omit the statement and continue with the current-state wording where possible.

Confirmation is already satisfied only when the user has explicitly reviewed and approved the same substance, reason, and placement. Do not treat a prior broad instruction, inferred preference, or silence as approval.

Never insert the candidate first and ask for approval afterward. The reason for proposing it belongs in the working conversation, not in the artifact.

Example:

- Avoid: `本版本取消此前规划的全部 Agent 能力，项目不再建设 Agent。`
- Prefer in the main narrative: `本项目聚焦 EM2 现有业务系统重构。`
- If an explicit boundary may be materially necessary, propose outside the artifact: `本项目范围不含 Agent 能力建设。` Explain why the reader needs it and where it would appear, then include it once only after user confirmation.

## Application-specific checks

### Documents, proposals, and presentations

- Draft from the current approved requirements, not as a chronological reconciliation of conversations.
- Keep background limited to reader-relevant business or technical context.
- Centralize user-confirmed scope exclusions and assumptions; do not repeat them as defensive disclaimers.
- Do not insert notes about why text, features, sections, or prices were changed unless the requested deliverable is a comparison or revision memo.

### Code, comments, and configuration

- Implement the current design without comments such as `removed because the user asked`, `old approach`, or `we no longer use`.
- Preserve rationale only when it explains a durable technical invariant that future maintainers cannot infer from the code.
- Keep migration history in commits, PRs, ADRs, or changelogs when those records are required.

### UI, messages, and generated content

- Show users the current action, state, consequence, or next step.
- Exclude internal deliberation, prompt wording, rejected concepts, and explanations of compliance with the request.
- Match the amount of rationale to what the recipient needs, not to how much reasoning occurred during production.

## Final artifact review

Before delivery, inspect the artifact itself and verify:

- Every sentence, comment, label, field, and note serves the artifact's intended reader.
- Current requirements are presented as the baseline rather than as a correction to history.
- Process explanations and prompt residue are absent.
- Every negative or historical statement has explicit user confirmation recorded in the working conversation.
- Every scope boundary that explains an exclusion has explicit user confirmation of its reason, wording, and placement.
- Confirmed boundaries appear in one appropriate location and are not repeated.
- Removing an explanation would not reduce correct use, acceptance, safety, compliance, or maintainability.

Report implementation choices, removed material, and reasoning to the user separately when useful. Do not inject that handoff explanation back into the artifact.
