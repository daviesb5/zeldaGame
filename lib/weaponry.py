import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

# Magic Orb
class ORB:
    def __init__(self, X, Y, DIRECTION):
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/orbs/orb1.png'), (25, 25))
        self.POS = [X, Y]
        self.DIRECTION = DIRECTION

# Arrow
class ARROW:
    def __init__(self, X, Y, DIRECTION):
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/arrows/e-01.png'), (25, 25))
        self.POS = [X, Y]
        self.DIRECTION = DIRECTION

# Red-Arrow
class REDARROW:
    def __init__(self, X, Y, DIRECTION):
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/red-arrows/e-01.png'), (25, 25))
        self.POS = [X, Y]
        self.DIRECTION = DIRECTION