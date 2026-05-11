# generative_art.py
# Generative art: softly disrupt a photo with translucent colored shapes
# Each run produces a different result thanks to random
# Inspiration: glitch art / VHS aesthetic

from PIL import Image, ImageDraw
import random

# load the photo and convert it to RGBA so we can use transparency
base = Image.open("my_photo.jpg").convert("RGBA")
width, height = base.size

# make a separate transparent layer to draw the disruptions on
overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# color palette that matches the warm/cool tones of the original image
# each color is (Red, Green, Blue) on a 0–255 scale
palette = [
    (255, 140, 90),    # warm orange
    (255, 200, 120),   # soft yellow
    (180, 100, 140),   # dusty pink
    (90, 130, 200),    # muted blue
    (230, 220, 200),   # cream
    (200, 80, 80),     # faded red
    (120, 180, 220),   # sky blue
]

# how many disruptions to draw total
num_disruptions = 30

# outer loop: place each disruption
for i in range(num_disruptions):
    # pick a random color from the palette
    r, g, b = random.choice(palette)
    # random transparency (90 = very faint, 255 = solid)
    alpha = random.randint(90, 160)
    color = (r, g, b, alpha)

    # random position on the image
    x = random.randint(0, width)
    y = random.randint(0, height)

    # conditional: choose one of three disruption styles
    if i % 3 == 0:
        # style 1: chunky horizontal glitch band
        line_length = random.randint(100, 500)
        thickness = random.randint(3, 15)
        # inner loop: stack lines on top of each other to make a thick band
        for j in range(thickness):
            draw.line([(x, y + j), (x + line_length, y + j)], fill=color)

    elif i % 3 == 1:
        # style 2: a single colored rectangle block
        w = random.randint(30, 180)
        h = random.randint(8, 35)
        draw.rectangle([x, y, x + w, y + h], fill=color)

    else:
        # style 3: scattered pixel noise
        # inner loop: drop 50 little dots near (x, y)
        for j in range(50):
            dx = x + random.randint(-70, 70)
            dy = y + random.randint(-70, 70)
            draw.point((dx, dy), fill=(r, g, b, 200))

# combine the transparent overlay on top of the original photo
result = Image.alpha_composite(base, overlay)

# save the result (convert back to RGB for compatibility)
result.convert("RGB").save("glitched_output.png")
result.show()

print("Done! Saved as glitched_output.png")
