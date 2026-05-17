# Week 5 - Refactoring assignment
# Same glitch/VHS effect as before, I just now  reorganized into functions
# Inspiration: glitch art / VHS aesthetic from youtube tutorials - also I just like "The Little Prince"

from PIL import Image, ImageDraw      # I VERY MUCH HOPE IT ISN'T A PROBLEM THAT I USED "PIL" AS MY LIBRARY - i can also change it
import random

# the following are TWEAKABLE stuff, change these to play with the outcome of the glitch on the photo

# the photo to glitch a file can be whatever file (although it must be in the same folder as this file)
INPUT_FILE = "my_photo.jpg"

# what the result is saved as
OUTPUT_FILE = "glitched_output.png"

# how many random disruptions to draw on the image
# bigger number = more chaos, smaller = subtle
NUM_DISRUPTIONS = 35

# transparency range for the disruptions, more aesthetic or intentional looking stuff
# 0 = invisible, 255 = solid. lower numbers = softer / more faded
MIN_ALPHA = 70
MAX_ALPHA = 140

# the color palette - swap colors, add new ones, remove some according to what a picture might need
# each color is (R, G, B) on a 0-255 scale / I took inspiration from this website which i found on instagram that one dude did / https://www.glyphr.xyz/
PALETTE = [
    (255, 140, 90),    # warm orange
    (255, 200, 120),   # soft yellow
    (180, 100, 140),   # pink
    (90, 130, 200),    # blue
    (230, 220, 200),   # cream
    (200, 80, 80),     # red
    (120, 180, 220),   # light blue
]

# functions!
# loads the photo and gives back the image + its size
def load_image(path):
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    return img, w, h

#STYLES FOR THE DISTORTION
# style 1: chunky horizontal glitch
def draw_band(draw, x, y, color):
    line_length = random.randint(100, 500)
    thickness = random.randint(3, 15)

    # stack lines on top of each other to make a thick band
    for j in range(thickness):
        draw.line([(x, y + j), (x + line_length, y + j)], fill=color)


# style 2: a single colored rectangle blocky thing
def draw_block(draw, x, y, color):
    w = random.randint(30, 180)
    h = random.randint(8, 35)
    draw.rectangle([x, y, x + w, y + h], fill=color)


# style 3: scattered pixel noise around (x, y)
def draw_dots(draw, x, y, color):
    # drop 50 little dots near the spot
    for j in range(50):
        dx = x + random.randint(-150, 150)
        dy = y + random.randint(-70, 70)
        draw.point((dx, dy), fill=color)


# the main flow of the program
def main():
    # load the photo
    base, width, height = load_image(INPUT_FILE)

    # make a transparent base layer for the disruptions
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # loop and place !one random disruption each time!
    for i in range(NUM_DISRUPTIONS):

        # pick a random color from the palette
        r, g, b = random.choice(PALETTE)

        # random transparency
        alpha = random.randint(MIN_ALPHA, MAX_ALPHA)
        color = (r, g, b, alpha)

        # make sure it is a random spot on the image
        x = random.randint(0, width)
        y = random.randint(0, height)

        # also pick one of the three styles randomly
        if i % 3 == 0:
            draw_band(draw, x, y, color)
        elif i % 3 == 1:
            draw_block(draw, x, y, color)
        else:
            draw_dots(draw, x, y, color)

    # combine overlay on top of the photo ( to figure this overlay stuff out I followed a tutorial/or i guess this is more of a forum post
    # https://stackoverflow.com/questions/68475960/how-to-compose-an-image-using-alpha-composite-but-set-the-opacity-of-the-mask )
    result = Image.alpha_composite(base, overlay)

    # save and show
    result.convert("RGB").save(OUTPUT_FILE)
    result.show()
    print(f"Done! Enjoy the weird distorted picture {OUTPUT_FILE}")


main()
