import pygame
from pygame.locals import *
import math as m

#set screen dimensions and fps cap

#construct environmet as matrix

#initialize fov, x/ypos and rotation variables

#initialize sensitivity and movement speed variables

#create movement directions

#initialize precision variable (how frequently objects are checked for in a given ray)

#fps cap and movement

#raycasting engine
    #loop that applies to all values within the players fov
        #define player position and rotation
        #calculates side length of fov via trig
        #loop that updates fov constantly
            #renders environment if 1 is detected in matrix
        #draws environment with pygame.draw.line
        #height of object should correlate to distance form object (the further away an object is the smaller it will be)