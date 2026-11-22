"""Generate fictional app screenshots for the public example."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DIRECTORY = Path(__file__).resolve().parent
SCREENS = {
    "episode": ("12:40", "Producer’s note", "Tighten the pause before the answer.", "OPEN"),
    "assignment": ("12:40 to 12:56", "Assigned to Leah", "Tighten the pause before the answer.", "ASSIGNED"),
    "resolved": ("12:40 to 12:56", "Resolved by Leah", "Original edit range saved.", "RESOLVED"),
}

for filename, (timestamp, title, detail, status) in SCREENS.items():
    image = Image.new("RGB", (904, 435), "#D8E4DC")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((20, 20, 883, 414), radius=25, fill="#EFF4F0")
    draw.text((52, 52), "SIGNAL DESK    /    THE QUIET EDIT", font=ImageFont.load_default(size=26), fill="#155E49")
    draw.rounded_rectangle((52, 113, 850, 369), radius=18, fill="#FFFFFF")
    draw.text((81, 139), timestamp, font=ImageFont.load_default(size=30), fill="#155E49")
    draw.text((81, 198), title, font=ImageFont.load_default(size=46), fill="#182B24")
    draw.text((81, 265), detail, font=ImageFont.load_default(size=29), fill="#182B24")
    draw.text((81, 321), status, font=ImageFont.load_default(size=23), fill="#155E49")
    image.save(DIRECTORY / f"{filename}.png")
