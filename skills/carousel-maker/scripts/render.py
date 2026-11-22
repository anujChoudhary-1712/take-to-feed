"""Render a carousel deck as 4:5 JPEGs and a multipage PDF."""

import argparse
import json
from pathlib import Path
from textwrap import dedent

from PIL import Image, ImageDraw, ImageFont, ImageOps

SIZE = (1080, 1350)
MARGIN = 88
WIDTH = SIZE[0] - 2 * MARGIN
PUNCTUATION = str.maketrans({"–": "-", "—": "-", "…": "..."})


def wrap(draw, content, font, width):
    lines = []
    line = ""
    for word in content.translate(PUNCTUATION).split():
        if draw.textlength(word, font=font) > width:
            raise ValueError(f"Word is too wide: {word}")
        candidate = f"{line} {word}".strip()
        if draw.textlength(candidate, font=font) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    return "\n".join([*lines, line])


def draw_copy(draw, content, y, size, color):
    font = ImageFont.load_default(size=size)
    wrapped = wrap(draw, content, font, WIDTH)
    box = draw.multiline_textbbox((MARGIN, y), wrapped, font=font, spacing=14)
    draw.multiline_text((MARGIN, y), wrapped, font=font, fill=color, spacing=14)
    return box[3]


def slide_image(deck, slide, number, directory):
    background = deck.get("background", "#F4F0E8")
    foreground = deck.get("foreground", "#182B24")
    accent = deck.get("accent", "#155E49")
    image = Image.new("RGB", SIZE, background)
    draw = ImageDraw.Draw(image)
    label = ImageFont.load_default(size=29)
    draw.text((MARGIN, 76), deck["label"].translate(PUNCTUATION).upper(), fill=accent, font=label)
    draw.line((MARGIN, 136, SIZE[0] - MARGIN, 136), fill=accent, width=3)
    title_end = draw_copy(draw, slide["title"], 205, 78, foreground)
    body_end = draw_copy(draw, slide["body"], title_end + 34, 38, foreground)

    if body_end > 1150:
        raise ValueError(f"Slide {number}: shorten the copy before exporting.")
    if slide.get("image"):
        available_height = 1160 - body_end - 42
        if available_height < 340:
            raise ValueError(f"Slide {number}: shorten the copy to make room for the screenshot.")
        with Image.open(directory / slide["image"]) as screenshot:
            fitted = ImageOps.contain(ImageOps.exif_transpose(screenshot), (WIDTH, available_height))
            image.paste(fitted.convert("RGB"), (MARGIN, body_end + 42))
    draw.line((MARGIN, 1220, SIZE[0] - MARGIN, 1220), fill=accent, width=3)
    draw.text((MARGIN, 1250), f"{number:02d} / {len(deck['slides']):02d}", fill=accent, font=label)
    return image


def main():
    parser = argparse.ArgumentParser(description=dedent(__doc__))
    parser.add_argument("deck", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    deck = json.loads(args.deck.read_text(encoding="utf-8"))
    if not deck["slides"]:
        parser.error("The deck must have at least one slide.")
    try:
        pages = [
            slide_image(deck, slide, number, args.deck.parent)
            for number, slide in enumerate(deck["slides"], start=1)
        ]
    except (KeyError, OSError, ValueError) as error:
        parser.error(str(error))
    args.output.mkdir(parents=True, exist_ok=True)
    for number, page in enumerate(pages, start=1):
        page.save(args.output / f"{number:02d}.jpg", quality=92)
    pages[0].save(
        args.output / "carousel.pdf", save_all=True, append_images=pages[1:], resolution=144
    )


if __name__ == "__main__":
    main()
