#Paweł Gałka 11.08
import sys
import pygame as pygame
import pygame.gfxdraw
import random, math, time, copy
from pygame.locals import *
random.seed()

#colors
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
ORANGE  = (255, 128, 0)
YELLOW  = (255, 255, 0)
PURPLE  = (102, 0, 101)
NAVY    = (13, 200, 255)
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
BEIGE = (229, 255, 204)

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE, NAVY]
BGCOLOR = BEIGE

#game settings

FPS = 120
WIDTH = 640
HEIGHT = 480
TEXT = 20
BALLRADIUS = WIDTH//32
BALLSIZE = 2*BALLRADIUS
BALLHEIGHT = 9
STARTX = WIDTH/2
STARTY = HEIGHT - BALLSIZE
ROWS = 14
COLS = 16
EMPTY = 0
FULL = 1
STARTLAYERS = 5

global display
display = pygame.display.set_mode((WIDTH, HEIGHT))  # tuple width,height
pygame.display.set_caption("BUBBLE SHOOTER")  # change title of window
display.convert()

