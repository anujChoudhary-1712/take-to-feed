# Render and review

The renderer needs Python 3 and Pillow. In a repository checkout, install the pinned dependency with `python -m pip install -r requirements.txt`. For a standalone skill installation, use `python -m pip install "Pillow==12.2.0"`. Activate a virtual environment first if your Python installation requires it.

From the workspace root, set the paths to your own skill and carousel folders.

```sh
python "$SKILL_DIR/scripts/render.py" "$PROJECT_DIR/deck.json" "$PROJECT_DIR/exports"
```

The deck has a `label`, optional hex colors (`background`, `foreground`, `accent`), and an ordered `slides` array. Each slide has a `title`, `body`, and editorial `source` note. Add `image` when a slide uses a screenshot or illustration. The source note stays in the JSON. The script renders numbered 1080×1350 JPEGs and a PDF with the same pages.

Run the export check to catch missing source images, missing or stale numbered JPEGs, and incorrect dimensions. It also writes a contact sheet. Check the PDF separately for page count and order.

```sh
python "$SKILL_DIR/scripts/check_exports.py" "$PROJECT_DIR/deck.json" "$PROJECT_DIR/exports"
```

Review the cover as a thumbnail, then open each slide at phone size. Check text wrapping, screenshot legibility, contrast, and whether any personal information is visible. Open the PDF and compare its page count and order to the JPEGs. Check that the last slide delivers on the cover and that the caption makes sense with the final assets.

If text crowds out a screenshot, shorten the copy or split the slide. If the screenshot is too small to read, crop closer to the relevant control. After changing the slide count, render into an empty export folder so old JPEGs do not get mixed in with the new deck.
