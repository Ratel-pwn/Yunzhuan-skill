---
name: ppt-content-planner
description: Create PPT content plans, slide outlines, and Kimi-ready markdown for presentation decks. Use this when the user asks to plan PPT content, structure slides, write slide-by-slide markdown, reorganize deck sections, or prepare presentation content for another tool to style. For this skill, markdown must contain only content that should appear on slides. Do not include speaker notes, teaching suggestions, page goals, commentary to the user, layout advice, or decorative image guidance inside the markdown body.
---

# PPT Content Planner

Use this skill when the user wants:
- PPT content planning
- slide-by-slide markdown
- restructuring a presentation
- a Kimi-ready or template-ready PPT outline
- page content only, without styling implementation

## Hard Rules

Markdown output must contain only slide-visible content.

Never put these into the markdown body:
- speaker notes
- training delivery advice
- "这一页的目标"
- "培训里的表达建议"
- "讲课时可以强调"
- "建议怎么讲"
- any commentary addressed to the user instead of the audience
- styling advice
- decorative or atmospheric image suggestions

If the user wants speaking notes, provide them separately in normal chat, never mixed into the markdown body.

## Allowed Markdown Content

Allowed inside markdown:
- slide numbers or sections
- slide titles and subtitles
- bullet points that belong on slides
- examples, prompts, checklists, tables, labels, and summaries that should appear on slides
- business-relevant image planning, but only in a dedicated final image section

## Image Planning Rule

Only plan images that are part of the presentation content:
- product screenshots
- workflow screenshots
- result screenshots
- case screenshots
- business diagrams if explicitly requested

Do not plan:
- decorative backgrounds
- abstract tech images
- mood images
- generic embellishment

When listing images, say exactly what should be shown.

Do not place image notes inside each slide's main content section.

Use this structure instead:
- main slide planning sections contain text content only
- all image requirements are collected once at the end in a dedicated section such as:
  `# 三、需要放真实业务相关图片的页面`

Inside the main slide-planning body, do not add:
- `### 配图`
- image bullets
- screenshot notes
- picture placeholders

## Structure Rule

Prefer this separation:
1. content that belongs on slides
2. optional speaking notes outside markdown only if the user asks

If unsure whether a sentence belongs on the slide, exclude it from markdown.

## Output Style

Default to concise, structured markdown.

For each slide, prefer:
- title
- optional subtitle
- content bullets or grouped sections

Avoid bloated prose paragraphs unless the user explicitly wants denser slide copy.

## Self-Check Before Finalizing

Before returning markdown, verify:
- every line could plausibly appear on a slide
- no presenter-only commentary is mixed in
- image planning appears only in one dedicated final section, not inside slide content sections
- image placeholders are business-relevant only
- the structure matches the user's requested flow
