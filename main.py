import math

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
xPos = 1.5
yPos = 1.5
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
    for i in range(fov+1):
        # New Rotation = old Rotation + Change
        # Radians = Distance of View
        # i - fov/2 = Field of View
        # Radian Formula = m.pi/180 * VALUE
        # 2*m.pi Radians in a full circle
        newRot = rot + m.radians(i - fov/2)
        dx = xPos % 1
        dy = 1 - (yPos % 1)
        #Distance to reach grid point
        dxlength = dy/m.tan(newRot + 1)
        dylength = dx*m.tan(newRot + 1)
        xstepUnit = -1/m.tan(newRot + 1)
        ystepUnit = 1/m.tan(newRot + 1)
        xIntercept = xPos + dx + dy / m.tan(newRot)
        yIntercept = yPos + dx + dx / m.tan(newRot)
        print(ystepUnit)
        # define player position and rotation
        vertAx, vertAy = xPos, yPos
        # calculates side length of fov via trig
        # loop that updates fov constantly
        # renders environment if 1 is detected in matrix
        # draws environment with pygame.draw.line
        # height of object should correlate to distance form object
