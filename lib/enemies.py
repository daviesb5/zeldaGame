import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

# Villian Cast
class ZIQA:
    def __init__(self):
        self.ZIQA = pygame.image.load('./sprites/ziqa/s000.png')
        self.ZIQA_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.HEALTH = 300
        self.VULNERABLE = True

class REDLINK:
    def __init__(self):
        self.REDLINK = pygame.image.load('./sprites/red-link/warp01.png')
        self.APPEAR = True
        self.POS = []
        self.SUMMONED = True
        self.HEALTH = 50

# Old Villians

class GANON:
    def __init__(self):
        self.GANON = pygame.image.load('./sprites/ganon.png')
        self.GANON_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.HEALTH = 250
        self.VULNERABLE = True

class BEAST:
    def __init__(self):
        self.BEAST = pygame.image.load('./sprites/beast.png')
        self.PORTAL = False
        self.PORTAL_APPEAR = True
        self.APPEAR = False 
        self.POS = []
        self.SUMMONED = False
        self.HEALTH = 100

class PORTAL:
    def __init__(self):
        self.PORTAL = pygame.image.load('./textures/portal/portal_1.png')
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.FRAME = 0