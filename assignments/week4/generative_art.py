# Each run of the code should produce a bit of a different result thanks to random
# Inspiration: glitch art / VHS aesthetic, I also watched youtube tutorials mainly to make something of a glitch effect

#PIL library which i found online and was recommended to me, it is for loading the images and letting me edit them and draw shapes on top
from PIL import Image, ImageDraw
import random

# loading the photo and converting it to RGBA so we can use transparency
#base.size gives the dimensions so i can pick random spots on the picture
base = Image.open("my_photo.jpg").convert("RGBA")
width, height = base.size

# make a separate transparent layer to draw the disruptions on, so im not really changing the picture just a layer on top of it
overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# color palette that matches the warm/cool tones of the original image
# each color is (Red, Green, Blue) on a 0–255 scale - i just googled what were good colours that I liked in this format and used them
palette = [
    (255, 140, 90),    # warm orange
    (255, 200, 120),   # soft yellow
    (180, 100, 140),   # pink
    (90, 130, 200),    # blue
    (230, 220, 200),   # cream
    (200, 80, 80),     # red
    (120, 180, 220),   # blue
]

# how many disruptions to draw total, this is very cool, because i can change it and more random stuff will appear!
num_disruptions = 50

# loop for placing one disruption each time, counts from 0 to 29
for i in range(num_disruptions):
    # pick a random color from the palette
    r, g, b = random.choice(palette)
    # random transparency (90 = very mild, 255 = solid)
    alpha = random.randint(90, 160)
    color = (r, g, b, alpha)

    # random position on the image for the disruption
    x = random.randint(0, width)
    y = random.randint(0, height)

    # I used ai for this because I could not figure it out : )
    # i like that I can swap colours and the palette by changing num_disruptions and the alpha range for bolder and softer colours.
    # also what I found  to be cool is that i can lock things ot certain regions like only disrupt the top half - Y=random.randint(0, height // 2)
    # conditional: choose one of three disruption styles - i wanted to do light lines, but didn't figure that out unfortunately
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
        # style 3: scattered pixel noise for cool effect
        # inner loop: drop 50 little dots near (x, y)
        for j in range(50):
            dx = x + random.randint(-150, 150)
            dy = y + random.randint(-70, 70)
            draw.point((dx, dy), fill=(r, g, b, 200))

# combine the transparent overlay on top of the original photo - alpha_composite is what merges the transparent overlay on top of the photo.
result = Image.alpha_composite(base, overlay)

# save the result (convert back to RGB for compatibility)
result.convert("RGB").save("glitched_output.png")
result.show()

print("Done! Saved as glitched_output.png")
