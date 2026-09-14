---
name: anti-clutter-product-ui
description: "Use before designing or implementing product UI, user-facing features, admin tools, Electron apps, SaaS workflows, knowledge bases, editors, settings pages, metadata forms, advanced settings, dialogs, side panels, or any screen/function that risks becoming implementation-driven. Enforces user-first product thinking before coding: identify user, job, workflow, frequency, decision, outcome, and necessity; confirm ambiguous product choices with the user; reject unnecessary controls, fields, settings, and features; then verify the rendered UI by screenshot or real inspection."
---

# Anti-Clutter Product UI

Use this skill before changing a product screen or user-facing feature. It is not only a visual cleanup skill. It is a product-thinking gate for deciding what should exist, what should be automated, and what should be shown to users.

## Prime Directive

Design from the user's job, not from the implementation.

Do not expose database fields, service options, prompt hints, indexes, task states, or future extension points just because they exist in code. A feature is only justified if it helps a real user complete a real workflow with less risk, less effort, or better outcome.

## Product Gate Before Code

Before editing UI or feature code, produce a short internal product decision record:

1. User: who uses this screen or feature.
2. Job: what they are trying to accomplish now.
3. Trigger: why they came here at this moment.
4. Frequency: daily, occasional, rare, admin-only, or debug-only.
5. Success: what visible outcome tells the user they are done.
6. Primary path: the shortest path through the task.
7. Non-goals: things the screen should not ask the user to manage.
8. Risk: what breaks if the feature/control is removed, hidden, automated, or moved.

If you cannot state these clearly, do not start coding. Ask the user only for the missing product decision that blocks safe execution.

## Necessity Gate For Every Element

For every proposed visible field, button, label, panel, dialog, menu item, setting, preview, or helper text, ask:

- Does the user need this to complete the current job?
- Is this a user concept or an implementation concept?
- Does this require manual human judgment, or can the system infer it?
- Is this used frequently enough to be visible by default?
- Would removing it make the workflow clearer without reducing user control?
- Is it duplicating what the main editor/body/content already lets the user express?
- Is it only useful for retrieval, prompt engineering, audit, migration, or debugging?

If it does not pass, do not show it by default.

## Ambiguity Confirmation Gate

Ask the user before coding when more than one product direction is defensible and the right answer cannot be inferred from the repo or explicit request.

Ask confirmation for:

- Delete vs hide vs move to a separate workflow.
- Manual form entry vs automatic parsing/derivation.
- Main workflow vs import/parse workflow vs review workflow vs settings.
- User-authored content vs parsed metadata vs database fields vs generated indexes as source of truth.
- Whether existing stored data must remain editable, read-only, migrated, or removed.
- Whether a control is for daily users, reviewers, admins, support, or debugging.
- Any change that removes user-visible capability, alters persisted data semantics, or may make old data unreachable.

Do not ask confirmation for obvious clutter:

- Repeated labels.
- Decorative tags.
- Implementation explanations.
- Broken sizing, unused whitespace, or visibly unbalanced layout.
- Controls that are provably unused or duplicated and can be removed without changing product semantics.

When asking:

- Ask one to three concrete questions.
- State the recommended option first.
- Explain the tradeoff in one sentence.
- Pause only if the answer changes product behavior.

Use this format:

```text
我建议采用 A，因为 ...。这里有一个产品取舍需要你确认：A 是 ...，B 是 ...。你要哪种？
```

If no answer is available and work can continue safely, choose the least destructive option: hide or move UI before deleting data or removing backend support.

## Feature Design Rules

Prefer capabilities that reduce user work rather than exposing more knobs.

Use this order of preference:

1. Automatically derive metadata from user-authored content.
2. Make the user edit the source content directly.
3. Provide a focused command for a specific secondary task.
4. Move rare tasks to a separate review/admin workflow.
5. Only then expose a setting or form field.

Do not build a settings panel to compensate for unclear feature design.

Do not make users manage what the system can reliably parse, infer, validate, or keep as backend metadata.

## Context Engineering Rule

For AI/context products, the rich text/body/source content is usually the user's main control surface.

If users can express the needed context directly in editable content, do not add a separate metadata form for the same idea.

Examples:

- Do not expose keywords if they can be parsed from title, category, and content.
- Do not expose applicable section types unless users explicitly manage a taxonomy.
- Do not expose source document IDs or section IDs as editable fields; use read-only provenance if needed.
- Do not expose usable/enabled booleans unless this is a moderation/review workflow.
- Do not expose freshness dates unless this is a compliance or validity review workflow.
- If images matter, provide an insert/reference action in the editor or an image review flow, not a hidden checkbox list in More Settings.

## UI Structure Rules

The screen should reveal the user's primary task within 3 seconds.

Prefer:

- A quiet header with location and one primary action.
- A left list only when users select among many records.
- One main work canvas that fills available width and height.
- One obvious primary action.
- Secondary actions only if they pass the necessity gate.

Reject:

- A small work card floating in the upper-left while the viewport is mostly empty.
- A form dump built from backend fields.
- A dashboard when the task is editing.
- A permanent preview or metadata panel that is not central to the task.
- Multiple action clusters competing for attention.
- More Settings used as a trash bin for unresolved product decisions.

## Copy Rules

Visible copy must serve the user's task.

Delete:

- Self-evident tags like `事实内容` above a fact editor.
- Implementation explanations like `像生成流程一样编辑事实正文...`.
- Helper text that only explains a confusing layout.
- Paragraphs in headers.
- Repeated nouns already visible in navigation or title.

Keep copy only when it prevents a real mistake, clarifies a non-obvious constraint, or names an action precisely.

## Verification Gate

Before final response for any user-facing UI or feature change:

1. Run the app/page when feasible.
2. Capture or inspect the actual rendered screen.
3. Check whether the primary task fills the workspace and reads clearly.
4. Check whether every visible control passed the product and necessity gates.
5. Check whether ambiguous choices were confirmed or handled by the least destructive default.
6. If the screenshot reveals obvious imbalance or clutter, fix it before reporting completion.

Do not report success only because TypeScript/build passed or a DOM assertion passed. Visual and product judgment are required.

## Failure Patterns To Avoid

Bad:

1. Preserve every backend field as a visible form field.
2. Put leftovers into More Settings.
3. Call it progressive disclosure.
4. Realize later the settings should not exist.

Bad:

1. Fix a control's height.
2. Ignore that the whole work area is squeezed into the corner.
3. Report success because one DOM measurement passed.

Correct:

1. Decide whether the feature/control should exist for the user.
2. Confirm ambiguous product choices before coding.
3. Remove, automate, or relocate non-primary work.
4. Design the minimum task surface.
5. Verify the actual screenshot.
