---
name: remotion-project-intro-video
description: Build a polished Remotion project intro video from a source post, article, repo, or launch note. Use when users want a readable but high-energy explainer video, short project promo, social recap, subtitle file, or animated walkthrough based on verified source materials. Do not use for generic slideshow decks, pure video trimming, or cases where the source content cannot be verified.
---

# Remotion Project Intro Video

Build a project-introduction video in Remotion with strong information hierarchy, visible motion, and external subtitles.

## Input And Output

Input:
- One primary source item such as an X post, blog post, GitHub repo, article, product page, or launch thread
- Any linked sources needed to verify facts
- User constraints on aspect ratio, tone, subtitle language, pacing, or delivery format

Output:
- A working Remotion composition
- A rendered video or a verified render command
- An external subtitle file such as `.srt`
- If voiceover is available or requested, a generated narration audio file and a dubbed render
- Source-backed copy only; no invented project claims

## Workflow

### 1. Verify The Source First

Read the source directly in a browser when possible. If the source is a post, capture the actual post body rather than relying on search snippets.

Do not guess:
- Project facts
- Metrics
- Supported integrations
- Product positioning

If the source cannot be read reliably, stop and ask the user for access or an alternative source.

### 2. Build A Visual Plan Before Coding

Before planning shots, confirm the target video aspect ratio with the user.

Aspect-ratio rules:
- Ask which video ratio should be used before generating the video
- If the user chooses the default, use `3:4`
- Treat `3:4` as the default vertical format for this workflow, not `9:16`
- Keep all layout, subtitle-safe zones, motion paths, and cover exports tied to the selected ratio
- If the user wants multiple delivery ratios, treat the video ratio and cover ratios as separate deliverables

Define a shot list before editing code. For project intro videos, the minimum useful sequence is:
1. Hook shot
2. Problem or premise
3. Product or project reveal
4. Real evidence or demo
5. Why it matters
6. Closing use case or callout

Every shot must have a distinct layout. Avoid repeating the same centered title plus side card composition.

Good variation patterns:
- Full-screen scrolling source capture
- Single focal panel with aggressive zoom
- Split comparison
- Large terminal or code wall
- Metric-led typography scene
- Diagonal or asymmetric collage
- Device-frame close-up
- Full-screen media with floating annotation chips

Before coding or rendering, review the planned shots as still compositions:
- What is the single focal point of this shot
- Where will the eye land first
- Will any title, chip, subtitle-safe area, or UI frame cover important source content
- Does this shot still work if paused on its intended resting frame
- Is the planned crop readable on a phone screen before motion helps it

If the shot fails as a still, do not rely on animation to save it. Fix the layout first.

### 3. Prefer Evidence Over Decorative Text

Use real materials whenever possible:
- Post screenshots
- Repo sections
- Official product pages
- Blog diagrams
- Real terminal output
- Real UI or demo captures

Treat visuals as primary content, not tiny support elements. If a demo visual is present, let it dominate the frame. Use text only to direct attention.

### 4. Make The First Shot Earn Attention

For source-post-based videos, prefer a dynamic opening:
- Scroll the original post vertically
- Use a zoomed crop that follows the reading path
- Add motion that reveals the source instead of showing a static card

Do not include irrelevant browser sidebars, feed rails, or unrelated chrome if the focus is a single post.

### 5. Keep The Video Readable

Optimize for small-screen viewing:
- Large type
- Clear contrast
- Few ideas per shot
- One dominant focal point
- Subtitle-safe lower area

When choosing between "more impressive" and "more readable", keep readability.

Subtitle treatment rules:
- Do not place subtitles hugging the bottom edge
- Place subtitles around the lower-third region, closer to the bottom one-third band than to the absolute bottom safe edge
- Increase subtitle font size by two steps relative to the earlier project baseline; prefer clearly oversized mobile-first subtitles over conservative caption sizing
- Re-check subtitle position and scale on the actual target ratio, because the correct position for `3:4` differs from `9:16`, `4:3`, and `16:9`
- If subtitles compete with UI chrome or lower-third cards, move the other elements first instead of shrinking captions
- Keep displayed subtitles to one line whenever possible in every target aspect ratio
- If a subtitle would wrap in the chosen ratio, split it into two timed subtitle segments at a natural phrase boundary instead of relying on visual line wrapping
- If only one word or a very short tail phrase is pushed onto a second line, split the original subtitle earlier into two balanced segments; do not allow orphan words, orphan particles, or tiny tail phrases to appear alone
- Avoid creating extremely short subtitle segments when splitting; preserve enough duration for each segment to be readable and avoid flicker-like instant disappearance/reappearance
- Do not leave punctuation at the end of any displayed or external subtitle line; trim trailing Chinese and English punctuation after subtitle segmentation while preserving timing

### 6. Apply UI/UX Quality Deliberately

Use strong layout contrast between shots. Pull from advanced UI design guidance when helpful:
- Vary composition, scale, and motion rhythm
- Keep text hierarchy obvious
- Use close-ups and pans instead of shrinking content
- Avoid visually dead slides that only list bullets

### 6d. Prefer A Product-Demo Camera Language

When the user wants the feel of a polished product intro video, structure shots like a guided demo rather than a slideshow.

Prefer this pattern:
- One real interface or source panel as the dominant subject of the shot
- Tight crops, cursor-path motion, highlight boxes, zooms, and pauses that guide the eye
- Small supporting insets only when they clarify the main panel
- Subtitles and narration carrying the explanation while the interface carries the proof

Avoid this pattern:
- Three or four equal-weight cards fighting for attention
- Abstract metric boards replacing the actual product surface
- Large decorative titles that compete with the interface
- Treating every shot like a poster instead of a guided screen walkthrough

### 6b. Keep Copy Project-First

When the source is a post about a project, the video should still be about the project, not about the post.

Use the source post as:
- a hook
- a proof point
- a discovery surface

Do not frame the video as a recap of "this post" unless the user explicitly wants commentary on the post itself.

For project intro videos:
- Open quickly on the project name or core capability
- Keep references to the post minimal
- Let the voiceover and visuals move from source to project as early as possible

### 6c. Write Copy Like A Project Intro, Not A Thread Recap

Short project videos need intro copy that lands the product fast.

Prefer this copy order:
1. What the project is
2. Why this kind of tool is needed in the first place
3. Where in a workflow it is useful
4. What real proof or demo shows it working

Avoid these copy mistakes:
- Opening with commentary about "this post" when the real subject is the project
- Spending the first line on discovery context instead of core capability
- Opening with a contrastive line like "it is not X, it is Y" before the viewer even knows what the project is
- Repeating on-screen labels, subtitles, and narration with the same sentence
- Explaining obvious visuals instead of using the narration to add new information
- Writing slide text as if it were an article paragraph

For the first one or two subtitle lines, explicitly orient the viewer:
- Name the project
- State its category or role
- Give the background problem in plain language
- Mention the most relevant use case or placement in a workflow

Do not try to sound mysterious before orientation. Clarity beats suspense in a product intro.

For on-screen copy:
- Prefer zero or one short headline per shot
- Do not pair a small title with another descriptive paragraph unless the scene truly needs it
- Put the detailed explanation in subtitles or voiceover, not in extra UI blocks

### 7. Always Ship Subtitles

Provide both:
- Burned-in or in-video subtitle treatment for readability
- External subtitle file for editing and dubbing workflows

The external subtitle file should match the intended narration timing closely enough to serve as a dubbing reference.

### 7b. Integrate Voiceover As A First-Class Step

If the project already has a reusable TTS path, do not treat voiceover as a separate manual afterthought. Fold it into the video workflow.

Preferred flow:
1. Finalize the narration script or `.srt`
2. Generate voiceover audio from that approved script
3. Generate a provisional subtitle timeline from the TTS system if it is available
4. Align the subtitle timeline to the final rendered audio with an audio-based aligner such as Whisper when possible
5. Regenerate the project-facing subtitle assets from that aligned timeline
6. Place the audio inside the Remotion project as an imported asset
7. Attach the audio track to the composition
8. Re-check scene durations against the generated audio length
9. Render a dubbed version, not only a silent preview

When voiceover is generated:
- Generate paid or voice-cloned TTS audio at most once per video project by default
- Treat `public/audio/<video-name>-voice.mp3` and its paired `.srt` as cached source assets after they exist
- During visual/layout/timing iterations, reuse the existing voiceover audio and only re-render Remotion, resync captions, or retime scenes
- Never rerun a paid TTS or voice-clone command just because a draft render is being regenerated
- Only regenerate voiceover when the narration script has materially changed and the user explicitly approves the extra TTS call; require a deliberate force flag such as `--force`
- Before running any TTS command, check whether the intended output audio path already exists and report whether it will be reused or regenerated
- Keep the external subtitle file beside the audio
- Verify the burned-in captions still match the spoken script and timing
- Verify the video duration is not shorter than the narration audio
- If the narration is materially longer or shorter than the current cut, retime scenes before calling the video done
- Prefer driving burned-in captions from the aligned or generated subtitle timing, not from an older draft summary line set
- Split subtitle lines by natural punctuation and spoken phrasing; avoid overly long lines and avoid forced multi-line wrapping when a cleaner short segment is possible
- Subtitle splitting must be checked against the actual rendered subtitle width for the selected ratio, not only by character count
- When splitting a long segment, choose balanced semantic chunks rather than leaving a single word, short noun phrase, or short trailing clause as its own segment
- Prefer a slightly earlier semantic split over a layout that creates a lonely second line; the viewer should perceive a stable reading rhythm, not flashing micro-captions
- After splitting subtitle lines, remove trailing punctuation from every subtitle segment in both the external subtitle file and the burned-in caption data
- Check caption safe position after retiming, because longer videos often expose low subtitle placement problems more clearly
- Do not maintain a separate hand-edited timing table for burned-in captions once `voice.srt` or another aligned subtitle source exists; generate the burned-in caption timing from that aligned source
- If shorter on-screen caption phrases are needed, derive them from the aligned subtitle source while preserving the original start and end boundaries or a deterministic proportional split inside those boundaries
- Audit at least one checkpoint after the 20-second mark and one checkpoint in the last third of the video, because subtitle drift often shows up late rather than in the opening shots
- Do not render while subtitle-sync generation is still running; asset generation, alignment, sync, and final render must happen in sequence, not in parallel
- Treat raw TTS event timestamps as provisional only; if an audio-based alignment pass exists in the repo or a related repo, use it before approving timing

For reusable project templates:
- Prefer a simple project-local wrapper that reads `.srt` or text and writes `public/audio/voice.*`
- Reuse the underlying TTS service script when it already exists elsewhere in the user's codebase
- Avoid copying an entire unrelated workflow when only the TTS layer is needed

### 8. Estimate Voiceover Timing When Needed

If the user will generate voiceover separately and does not provide an exact recording length, estimate timing from the script and assume a fairly even AI narration pace.

Use that estimate to:
- Set shot durations
- Avoid holding short lines too long
- Give denser lines or evidence-heavy scenes more time
- Keep subtitle timing aligned with the expected narration rhythm

Do not leave all scenes at identical durations by default. Adjust timing according to copy density, visual complexity, and the amount of reading the viewer must do.

### 8b. Reusable Outro

When the user provides a creator avatar or asks for a reusable video ending, store the asset in the Remotion project's public assets and build the ending as a standalone component rather than hard-coding it into one scene.

For a generic follow outro:
- Use a clean black background unless the user specifies a brand background
- Center the avatar and render it as a circle with a high-contrast border
- Put the call-to-action below the avatar
- Animate the call-to-action with a simple tap, pulse, or ripple effect
- Keep it after narration subtitles unless the user wants spoken outro copy
- Make the outro duration explicit so future videos can reuse or retime it easily

### 8c. Intro Lead-In Before Narration

When the user asks for a short opening pause, do not only add a visual overlay. Treat the lead-in as timeline structure.

For a black-field lead-in:
- Add an explicit lead-in duration constant
- Delay the audio by the same duration
- Delay the official scene timeline by the same duration
- Shift burned-in captions and external subtitle timing by the same duration
- If using a black-to-picture fade, pre-mount the first visual under the black field before narration starts, then finish the fade before or exactly as narration begins; avoid making the first subtitle fade in from black with the overlay
- Fade the black field out over a few frames so the first scene does not hard-cut in
- Keep the pause short unless requested otherwise; around 0.4 to 0.8 seconds works well for short social videos

### 8d. Background Music

When adding background music, treat licensing and mix balance as part of the deliverable, not a decorative afterthought.

Selection rules:
- Prefer official artist/library download pages over reposted audio mirrors
- Confirm the track license and attribution requirements before downloading
- Store the music in the project assets folder with an attribution or license note beside it
- Pick instrumental music that supports the video's mood without vocals or sharp lead melodies competing with narration

Mixing rules:
- Keep background music quiet under narration; a starting Remotion volume around 0.03 to 0.06 is usually safer than 0.1+
- Add fade-in and fade-out envelopes so the music does not hard-cut at the beginning or ending
- Do not move narration, subtitles, or scene timing just to add music
- Render and audit at least one early narration checkpoint and one late checkpoint for speech clarity
- If the music competes with voiceover, reduce volume first rather than compressing or raising the narration unless the user asks for mastering

### 8e. Final Project Packaging

After the user confirms a final version, package the video as a named video project instead of leaving it mixed with temporary renders.

Status rules:
- Explicitly distinguish `draft/review render` from `final approved deliverable`
- If the user has not approved the video yet, you may render review files in `out/` and stage research notes under `project/<video-name>/`, but do not describe the work as fully complete
- Once the user approves the final version, the workflow is not complete until packaging, cover generation, metadata generation, and cleanup are all finished
- If the user asks to "make the video" without requesting a draft-only checkpoint, drive the workflow all the way to the final packaged project after the approval loop rather than stopping at a loose render in `out/`
- When presenting a draft, clearly label it as a draft and list the remaining finalization steps

Packaging rules:
- Create `project/<video-name>/` inside the Remotion project
- Put the final approved video directly under `project/<video-name>/`
- Put the final external subtitle file under `project/<video-name>/subtitles/`
- Put music attribution or license notes under `project/<video-name>/licenses/`
- Copy the project-specific video generation skill into `project/<video-name>/skill/` when the skill has become part of the reusable workflow for that video project
- Add a short README or manifest that identifies the final deliverables and where the source assets remain

Cleanup rules:
- Delete intermediate rendered versions for that video after the final version is confirmed
- Delete temporary audit, precheck, postcheck, and review frame folders for that video
- Do not delete source materials such as screenshots, captured demo assets, voiceover audio, aligned SRT files, BGM files, attribution notes, avatar assets, or source code
- Do not delete unrelated sample videos or outputs unless the user explicitly asks
- Before deletion, resolve absolute paths and verify they are inside the intended project output directory

### 8f. Cover And Publishing Metadata

The final video workflow is not complete until the project has a cover image and publishing metadata.

Cover rules:
- Create a cover with the same aspect ratio as the final video
- If the selected video ratio is `3:4`, create the primary cover in `3:4`
- Also export the required cover variants for distribution:
- `3:4` vertical cover
- `4:3` horizontal cover
- `16:9` horizontal cover
- If the project still needs a taller vertical feed cover, also export `9:16`
- Use large, high-contrast title text that remains readable in a small feed thumbnail
- Highlight the strongest viewer-facing hook, not an internal implementation detail
- Use real project visuals or screenshots when possible so the cover matches the video content
- Avoid cluttered multi-line descriptions on the cover; one strong headline plus one short support line is enough
- Export both the editable cover source and the final image directly under `project/<video-name>/`

Metadata rules:
- Store platform-ready metadata in the video project folder, preferably both machine-readable JSON and human-readable Markdown
- Title should optimize for viewer curiosity and clarity
- Tags should optimize for platform discovery and recommendation routing
- Description should expand the project context, use case, and reason to watch without overclaiming
- When a source project has a public open-source repository or official source URL, put that open-source address on the first line of the description
- Include paths to the final video, cover, subtitle, and license notes in the metadata

Completion gate:
- Do not call the video workflow complete if the final approved project is missing any of the following:
- final packaged video under `project/<video-name>/`
- external subtitle file under the project folder
- required cover variants
- publishing metadata
- synced reusable skill under the Remotion project `skill/` directory when this workflow changes
- cleanup of intermediate renders and audit folders for that specific video

### 9. Prevent Common AI Video Mistakes

Before finalizing visuals, explicitly check for these common mistakes:

- Reusing the same generic page screenshot across multiple claims when each claim needs its own matching product visual
- Using a full-page or long screenshot from a lazy-loaded gallery before lower images have actually loaded
- Treating a screenshot filename as proof of content without visually confirming what is inside the crop
- Popups, login prompts, install-app banners, cookie bars, or sticky overlays left inside screenshots
- Browser chrome or sidebars that dilute the subject when the intended visual is a single post or panel
- Text overlays placed on top of dense UI or charts, making both the overlay and the source unreadable
- Too many simultaneous labels, chips, captions, and descriptive blocks on one shot
- A scene "explaining" the picture with text when the picture itself could be enlarged and shown more clearly
- Repeating the same layout skeleton across multiple shots
- Demo visuals rendered too small to read on a phone screen
- On-screen copy repeating what subtitles or voiceover already say
- Modal prompts, app-open nags, sign-in walls, or sticky banners not dismissed before capture
- Decorative gradients, shadows, or labels reducing screenshot contrast instead of supporting it
- Important UI text hidden under titles, chips, or subtitle-safe overlays
- Multiple focal points fighting for attention inside one shot
- Using a low-resolution screenshot when a higher-resolution or tighter crop is available
- Reusing the wrong screenshot for a shot because filenames are misleading or visually similar
- Leaving a large dead zone in the frame where no meaningful subject, motion, or contrast exists

Source-visual matching rules:
- Build a shot-to-source map before rendering: each scene must list the narration claim, the intended source asset, and the exact crop/region being shown
- If a scene discusses a category, model filter, case card, source metadata, or demo result, use a screenshot of that exact feature or a tight crop of the relevant cards
- Do not use one homepage screenshot as the default fallback for all product scenes; repeated screenshots are only acceptable when the crop, focal point, and narration role are clearly different
- For lazy-loaded sites, scroll to the target section, wait for images to load, and capture loaded viewport screenshots instead of relying on a single long screenshot
- Reject any captured web visual that contains blank placeholders, skeleton loaders, broken image icons, or visibly unfinished lazy-loaded content
- During pre-render review, verify that every shot's main image answers the current subtitle/voiceover line without requiring extra explanatory text

Prefer this hierarchy:
1. Let the visual carry the scene
2. Add one short title only if needed
3. Put the detailed explanation in subtitles or voiceover

Before shipping, run this visual sanity check on every shot:
1. Can the viewer tell what the main subject is in under one second
2. Is every visible text layer readable on a phone screen
3. Did we remove overlays and prompts from captured websites
4. Is any on-screen sentence redundant with the subtitle line
5. If we delete the extra label block, does the shot become cleaner
6. Does each screenshot actually match the role assigned to it in the shot plan
7. Is there a large empty area that feels accidental rather than intentionally quiet

### 10. Review The Finished Video Visually

Do not stop after code compiles or the render succeeds. Review the finished video as a viewer.

This is a second-pass review, not the first one. The workflow must include:
1. Pre-render shot review of the planned compositions and intended resting frames
2. Post-render video review of the actual exported frames and motion timing

This review must happen after rendering and should inspect representative frames or the full sequence for:
- Bad stopping points in scroll shots, pans, or zooms
- Mid-transition frames being used like final hero frames
- Dense screenshots landing on awkward crops or large empty areas
- Multiple subjects competing in one frame with no clear focal point
- Visual rhythm issues where a shot pauses in an unattractive or confusing state
- Subtitle-safe regions covering the most important content
- Text or cards becoming partially cut off at the exact frame where the shot settles

Do not review only from code or memory. Extract representative frames from the rendered video when needed, especially for the first shot, any animated source capture, and any shot with dense UI.

For animated source captures, explicitly ask:
1. Did the motion stop on the correct content block
2. Does the resting frame look intentional, or merely like a random frame from the scroll
3. Is there any large dead area, half-visible card, or leftover UI that makes the frame look broken

If the answer to any of these is yes, revise the shot timing, crop, motion path, or layout before treating the video as done.

Minimum review coverage:
- Review every shot before render
- Review every shot after render at least once
- Review the first shot, all animated source captures, and all dense-UI shots with extra care

## Rules

- Never invent facts not present in verified sources.
- Never leave the first shot static if the source itself can be animated.
- Never crop source visuals so tightly that key context disappears, or so loosely that the subject becomes unreadable.
- Never reuse the same base layout for all shots.
- Prefer pan, zoom, parallax, and reveal motion over decorative particle effects.
- If online visuals are available, use them before resorting to abstract filler graphics.
- If Remotion can express the sequence directly, stay in Remotion. Only bring in another tool when the task depends on timeline editing features Remotion cannot practically cover.

## When To Consider A Second Tool

Consider adding another video tool only if one of these is true:
- The task depends on heavy source-video trimming across many clips
- Beat-synced cut editing is the main requirement
- The user needs rapid assembly from many existing video files rather than designed motion scenes

Even then, keep Remotion responsible for title cards, branded frames, subtitle burn-in, and structured explainer scenes.

## Example

Input:
- X post announcing an open-source security project
- GitHub repo
- Official launch blog
- Need: 9:16 video with Chinese subtitles and no voiceover generation

Output:
- Remotion composition with a scrolling post opener, product explanation shots, repo and blog close-ups, real CLI output, and an `.srt` subtitle file
