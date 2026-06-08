# Assignment 8 - Pygame animation with a class
# I used the cover of "The Bends" by Radiohead (my favourite album)
# The goal was just to make the image move, so i made a bunch of copies of the
# album cover bounce around the screen like the old DVD logo.
# Built on top of the dino.py / Dino class example from class.

import pygame
import random

# --- some settings at the top ---
WIDTH = 700
HEIGHT = 500
IMAGE_FILE = "the_bends.jpg"
NUM_COVERS = 5          # how many album covers bounce around
BG_COLOR = (10, 10, 10)  # almost black background


# --- the class for one bouncing album cover ---
# this is basically the Dino class from class: it has an image and a position,
# a move() method and a draw() method.
class Album:
    def __init__(self, image, x, y, speed_x, speed_y):
        self.image = image
        self.x = x
        self.y = y
        # speed in each direction - how many pixels it moves per frame
        self.speed_x = speed_x
        self.speed_y = speed_y
        # i store the width/height so i know when it hits the edges
        self.width = image.get_width()
        self.height = image.get_height()

    def move(self):
        # add the speed to the position to move it
        self.x += self.speed_x
        self.y += self.speed_y

        # bounce off the left/right walls by flipping the horizontal speed
        if self.x < 0 or self.x + self.width > WIDTH:
            self.speed_x = -self.speed_x
        # bounce off the top/bottom walls by flipping the vertical speed
        if self.y < 0 or self.y + self.height > HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        # blit just copies the image onto the screen at the current position
        screen.blit(self.image, (self.x, self.y))


# --- a small helper that builds one random album cover ---
# i made this a function so the random stuff is in one place.
# it loads the image, scales it to a random size, and gives it a random
# position and random speed, then returns a new Album object.
def make_random_album():
    # load the image (convert() makes it draw faster - we use convert() and not
    # convert_alpha() because a jpg has no transparency)
    picture = pygame.image.load(IMAGE_FILE).convert()

    # random size between 60 and 120 pixels so they're not all the same
    size = random.randint(60, 120)
    picture = pygame.transform.scale(picture, (size, size))

    # random starting position (kept a bit away from the edges)
    start_x = random.randint(0, WIDTH - size)
    start_y = random.randint(0, HEIGHT - size)

    # random speed - i pick from a small range and avoid 0 so they always move
    speed_x = random.choice([-3, -2, -1, 1, 2, 3])
    speed_y = random.choice([-3, -2, -1, 1, 2, 3])

    return Album(picture, start_x, start_y, speed_x, speed_y)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Bends - bouncing covers")

    # clock keeps the animation running at a steady speed (looked this up,
    # without it the covers move way too fast)
    clock = pygame.time.Clock()

    # build a list of random album covers - this is the "multiple instances" part.
    # same idea as the Car holding a list of Wheels in class.
    albums = []
    for i in range(NUM_COVERS):
        albums.append(make_random_album())

    # the main loop - same structure as the pygame example from class
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False

        # fill the background fresh each frame so the old positions get cleared
        screen.fill(BG_COLOR)

        # move and draw every album cover
        for album in albums:
            album.move()
            album.draw(screen)

        # show everything we just drew
        pygame.display.flip()

        # run at 60 frames per second
        clock.tick(60)

    pygame.quit()


main()
