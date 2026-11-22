"""Check a carousel's JPEG exports and create a review contact sheet."""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

SLIDE_SIZE = (1080, 1350)


def check(deck_path, exports):
    deck = json.loads(deck_path.read_text(encoding="utf-8"))
    slides = deck["slides"]
    if not slides:
        raise ValueError("The deck has no slides.")
    expected = [f"{index:02d}.jpg" for index in range(1, len(slides) + 1)]
    actual = {path.name for path in exports.glob("*.jpg") if path.stem.isdecimal()}
    missing = sorted(set(expected) - actual)
    extra = sorted(actual - set(expected))
    if missing or extra:
        raise ValueError(f"Export count or numbering mismatch. Missing: {missing}. Extra: {extra}.")

    columns = min(4, len(slides))
    rows = (len(slides) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 244, rows * 309), "#E9E9E9")
    draw = ImageDraw.Draw(sheet)
    label_font = ImageFont.load_default(size=14)
    for index, (slide, name) in enumerate(zip(slides, expected)):
        source = slide.get("image")
        if source and not (deck_path.parent / source).is_file():
            raise ValueError(f"Slide {index + 1} references a missing image: {source}")
        with Image.open(exports / name) as image:
            if image.format != "JPEG" or image.size != SLIDE_SIZE:
                raise ValueError(f"{name} must be a 1080×1350 JPEG.")
            tile = ImageOps.contain(image.convert("RGB"), (220, 275))
        x = (index % columns) * 244 + 12
        y = (index // columns) * 309 + 12
        sheet.paste(tile, (x, y))
        draw.text((x, y + 280), name, fill="#202020", font=label_font)

    if not (exports / "carousel.pdf").is_file():
        raise ValueError("Missing carousel.pdf.")
    return sheet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", type=Path)
    parser.add_argument("exports", type=Path)
    args = parser.parse_args()
    try:
        sheet = check(args.deck, args.exports)
        output = args.exports / "contact-sheet.png"
        sheet.save(output)
    except (KeyError, OSError, ValueError) as error:
        parser.error(str(error))
    print(output)


if __name__ == "__main__":
    main()
