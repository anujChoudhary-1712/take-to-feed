# Take to Feed

Social media skills for Claude Code and Codex. Turn a product demo, transcript, or idea into a carousel or short-form video, then use performance data to decide what to try next.

## Install

Install all four skills with the Skills CLI.

```sh
npx skills add anujChoudhary-1712/take-to-feed --skill '*'
```

To install one, replace `'*'` with the skill name, such as `carousel-maker`. For a manual install, copy the entire skill folder into your agent's skills directory so its guides, assets, and scripts stay together.

## Pick a skill

| Skill | What to ask your agent | Guide and templates |
| --- | --- | --- |
| `social-hooks` | “Give me three openings for this demo. Show the first visual for each and score them against the payoff.” | [Workflow](skills/social-hooks/references/hook-workflow.md) · [Hook sheet](skills/social-hooks/assets/starter/hooks.md) |
| `carousel-maker` | “Turn this transcript and these screenshots into a five-slide carousel. Export Instagram JPEGs and a LinkedIn PDF.” | [Setup](skills/carousel-maker/references/project-setup.md) · [Templates](skills/carousel-maker/assets/starter) · [Render and review](skills/carousel-maker/references/render-and-review.md) |
| `short-form-video` | “Make a 30-second reel plan from this talking-head take and product recording. Include the cut points, captions, and cover copy.” | [Production guide](skills/short-form-video/references/production-guide.md) · [Editing and rendering](skills/short-form-video/references/editing-stack.md) · [Script and edit templates](skills/short-form-video/assets/starter) |
| `content-experiments` | “Plan a test of these two carousel covers. Use saves per reach at 72 hours and log what we should try next.” | [Experiment guide](skills/content-experiments/references/experiment-guide.md) · [Experiment log](skills/content-experiments/assets/starter/experiment.md) |

Carousel Maker renders locally with Python and Pillow. Short-Form Video uses Whisper for speech timing and Remotion or HyperFrames for rendering in a compatible project. Content Experiments uses the metrics you provide or can access through an authorized analytics tool.

## Set up a local content workspace

Copy the [brand brief template](examples/brand-brief.md) into your workspace. Keep shared voice and visual preferences there, and save each post's sources, drafts, and references with that post.

```text
social-content/
├── brand.md
├── carousels/
│   └── podcast-review/
│       ├── brief.md, references.md, deck.json, captions.md
│       └── sources/, assets/, exports/
├── reels/
│   └── podcast-review/
│       ├── script.md, edit-plan.md, cuts.json
│       └── raw/, screen/, sources/, exports/
└── experiments/
    └── podcast-review-cover/
        └── experiment.md
```

For a new demo, choose the moment that shows the outcome, draft hooks around it, and use the same evidence in the carousel or reel. Keep links, filenames, and timestamps in the draft so you can check claims while reviewing. Once the post is live, log the result in the experiment folder.

## Follow the Signal Desk example

Start with one fictional product demo and carry its evidence through all four skills.

| Step | Input and output |
| --- | --- |
| Write the hook | Read the [demo transcript](examples/demo/transcript.md) and compare the three options in the [filled hook sheet](examples/demo/hooks.md). The winning line opens both posts. |
| Build the carousel | Inspect the [editable deck](examples/demo/deck.json), [contact sheet](examples/demo/exports/contact-sheet.png), [LinkedIn PDF](examples/demo/exports/carousel.pdf), and [platform captions](examples/demo/captions.md). |
| Edit the reel | Follow the [runnable reel project](examples/demo/reel) with sample media and faster-whisper timings. Compare the [Remotion MP4](examples/demo/reel/reel.mp4) and [HyperFrames MP4](examples/demo/reel/reel-hyperframes.mp4). |
| Review a cover test | Read the [experiment log](examples/demo/experiment/experiment.md) and [sample analytics](examples/demo/experiment/analytics.csv) to see why a higher rate can still be inconclusive. |

### Rebuild the carousel

Run from the repository root.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python examples/demo/make-fixtures.py
.venv/bin/python skills/carousel-maker/scripts/render.py examples/demo/deck.json examples/demo/exports
.venv/bin/python skills/carousel-maker/scripts/check_exports.py examples/demo/deck.json examples/demo/exports
```

The [editorial guide](skills/carousel-maker/references/editorial-guide.md) shows how to adapt the slide sequence for a tutorial, case study, or research brief.

## License

[MIT](LICENSE)
