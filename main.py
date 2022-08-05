import pygame
from pygame.locals import *
import math as m

# set screen dimensions and fps cap
fps = 30
size = width, height = 400, 400
windowSize = pygame.display.set_mode(size)
white = (255, 255, 255)

# construct environment as matrix
environment = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

# initialize fov, x/ypos and rotation variables
fov = 60
xPos = 1
yPos = 1
rot = 0

# initialize sensitivity and movement speed variables
sensitivity = 1
movementSpeed = 1

# create movement directions

# initialize precision variable (how frequently objects are checked for in a given ray)
precision = 0.02

# fps cap and movement
clock = pygame.time.Clock()

# raycasting engine
running = True
while running:
    pygame.init()
    clock.tick(fps)
    pygame.display.set_caption('FPS - ' + str(round(clock.get_fps())))
    for event in pygame.event.get():
        # pygame.draw.rect(windowSize, white, (200, 150, 100, 50))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            exit()
    # loop that applies to all values within the players fov
    for i in range(fov):
        print('i')
        # define player position and rotation

        # calculates side length of fov via trig
        # loop that updates fov constantly
        # renders environment if 1 is detected in matrix
    # draws environment with pygame.draw.line
        # height of object should correlate to distance form object
