# Local project setup

Keep one folder per carousel. A dated slug is handy when you make multiple decks on the same topic. Reuse an existing workspace if it already has a place for content.

```text
social-content/
├── brand.md                         # optional shared voice and design notes
└── carousels/
    └── 2026-11-22-podcast-review/
        ├── brief.md                 # audience, goal, angle, and platform
        ├── references.md            # source and inspiration index
        ├── sources/                 # transcript, original screenshots, source notes
        ├── assets/                  # cropped or redacted files used in deck.json
        ├── deck.json                # editable slide copy, image paths, and evidence
        ├── captions.md              # per-platform copy and image descriptions
        └── exports/                 # generated JPEGs and PDF
```

From the workspace root, set `SKILL_DIR` to the installed `carousel-maker` directory. For a checkout of this repository, use `skills/carousel-maker`.

```sh
SKILL_DIR="skills/carousel-maker"
PROJECT_DIR="social-content/carousels/2026-11-22-podcast-review"
mkdir -p "$PROJECT_DIR/sources" "$PROJECT_DIR/assets"
cp -n "$SKILL_DIR"/assets/starter/* "$PROJECT_DIR/"
```

Put originals in `sources/`. Use descriptive filenames such as `demo-transcript.md` and `review-assigned-00m12s.png`. Keep the cropped or redacted versions in `assets/`. Write image paths relative to `deck.json`, for example `assets/review-assigned.png`.

Record reusable preferences in `brand.md`, such as tone, color values, approved terminology, and visual examples. Record the references used for this specific post in `references.md`. Include a local path or link, the detail worth carrying forward, and which slide it informs. Treat a competitor carousel as inspiration for structure or pacing. Use original copy and illustrations.

For revisions, edit `deck.json` and `captions.md` in the same project. Use a new export folder if you need to retain a prior version or changed the slide count. Review materials for confidential content before adding a project to a public repo.
