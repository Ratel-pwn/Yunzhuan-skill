---
name: user-first-compact-ui
description: Apply user-first information hierarchy and concise product copy when building, revising, or reviewing interfaces. Use for crowded screens, redundant panels or labels, slogan-like AI copy, unclear actions, progressive disclosure, large-document usability, and visual QA.
---

# User-First Compact UI

## Operating Rule

Design from the user's immediate workflow, not from feature inventory. Before editing UI, state the user action, the needed result, and the smallest surface that supports it.

## Hard Rules

- Remove duplicate labels, headings, subtitles, counters, and helper text. If two elements say the same thing, keep the one that best supports scanning.
- Do not add explanatory copy unless it changes a user's next action. Empty states may explain what to do; configured states should not repeat obvious instructions.
- Do not spend vertical space on metadata that can fit beside the title or primary action.
- Keep primary actions near the object they affect. If a rule list has an add button, place counts and add action in the same row when space allows.
- Prefer progressive disclosure for configuration. Put secondary lists, rules, and settings behind a button or modal when they are not the user's main working surface.
- Do not render unbounded document content in one area. Paginate, virtualize, cap visible text, or otherwise bound scroll surfaces for long documents.
- Make list items operational. If a result points to a document location, clicking it must navigate to and highlight that location when possible.
- Use existing project components and design patterns before inventing new UI.
- Treat angry or blunt user feedback as product evidence. Extract the concrete usability failure and fix it; do not defend the prior implementation.

## UI Edit Workflow

1. Identify the user's primary path for this screen.
2. Mark each visible text block as action, state, label, metadata, or decoration.
3. Delete decoration and merge duplicate labels or metadata.
4. Put state counts next to the relevant title or primary action instead of giving them their own row.
5. Bound every scrollable or potentially large content area.
6. Implement with existing components.
7. Build and visually inspect the result at the target screen size.
8. If the screenshot shows repeated meaning, unused space, or a second explanation of the same thing, revise before reporting completion.

## Modal Checklist

- One title only.
- No eyebrow plus title if they repeat the same concept.
- Header row should carry count/status and the primary action together.
- Body should be the list, form, or empty state only.
- Footer should only contain dismissal or commit actions.
- Empty state should be short and should not duplicate the title.

## Default-Screen Gate

For a substantial screen change, identify the primary working object and the action the user came to perform. Keep this decision in working notes; do not turn it into a slogan in the product.

- Decide what is visible on entry, what opens on selection, and what belongs behind a secondary control. A feature being implemented does not justify showing it by default.
- When a board, editor, canvas, or document is the primary object, let it dominate the initial screen. Start record lists, inspectors, tutorials, history, and settings closed unless the task needs simultaneous comparison. Do not force every product into a single-pane layout.
- A collapsed surface needs a clear entry, a close action, preserved unsaved input, and accessible focus behavior. Verify the full task remains possible with the new disclosure pattern.
- Remove redundant regions from the layout and markup. Shrinking text, lowering contrast, adding whitespace, or hiding duplicate controls with CSS does not resolve competing information.

## Product-Copy Gate

Write labels for objects, actions, and necessary state. Use the user's language consistently. Decorative English eyebrows, inspirational taglines, conceptual manifestos, and explanations of obvious controls need a concrete task reason to remain.

- Avoid habitual contrast formulas such as “不是……而是……”, “不仅……更是……”, and “not X, but Y” in product slogans and delivery commentary. State the actual action or outcome directly. Legitimate comparisons and safety distinctions remain valid when they convey necessary information.
- Replace “每一枚棋子都有自己的故事” with a functional label such as “来源记录”, or omit it when context already identifies the source. Prefer “保存记录” to a paragraph explaining the philosophy of recording.
- Keep consequential information: data loss, unsaved input, simulation status, cost, consent, and recovery actions. Place it once at the point of decision; do not scatter the same warning across the page or hide it only in help.

## Observable Acceptance

Inspect the actual default state, one selected/open state, and a narrow-screen state. Name the dominant object and competing regions from the screenshot, not from the source code. If the user must read introductory prose to identify the next action, revise the screen.

For clutter complaints, compare visible regions and repeated meanings before/after. Exercise open → act → close, keyboard dismissal/focus return, draft preservation, and any hidden primary workflow. A build/test pass does not establish visual clarity. Report what was removed or moved and the observed behavior; avoid self-awarded adjectives or another design manifesto.
