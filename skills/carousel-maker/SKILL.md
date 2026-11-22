---
name: carousel-maker
description: Turn a product demo, transcript, or screenshots into a source-backed social carousel with editable slide copy, Instagram images, and a LinkedIn PDF.
---

# Carousel Maker

1. Identify the audience and the single outcome the demo can prove. Use the user's brand colors and voice when supplied.
2. List the strongest evidence in the input, including timestamps, quotes, and screenshots. Use original screenshot files when available. Ask for a missing screenshot if it is necessary to establish a claim, or revise the claim to match the evidence.
3. Open with that outcome. Put one decision or action on each middle slide. Pair each demo step with the screenshot that shows it. Finish by showing the result or giving one practical next step.
4. Write an editable deck JSON. Include `label`, optional `background`, `foreground`, and `accent` as hex colors, and a `slides` array. Each slide has `title`, `body`, `source` (timestamp or source note for the editor), and optional `image` (path relative to the JSON file). The renderer includes only the title, body, image, label, and page number in published assets.
5. With Python 3 and Pillow installed, run `python scripts/render.py deck.json exports`, resolving the script from this skill directory. If rendering is unavailable, deliver the deck JSON and caption copy.
6. Review the rendered slides for legibility, visible screenshot details, and whether the close delivers on the cover. Fix overflow by shortening copy. Deliver the deck, numbered 1080×1350 JPEGs, PDF, and platform captions in the response or requested output folder.
