import pygame.image
from grid import *

class LINK:
    def __init__(self):
        self.SPRITE_POS = pygame.image.load('./sprites/link/s000.png')
        self.PLAYER_POS = [0, 0]
        self.PLAYER_INV = []
        self.WEAPON = False
        self.HAS_SWORD = False
        self.HAS_ARROW = False
        self.HEALTH = 100
        self.MANA = 200
        self.DIRECTION = 's'
        self.TRANSFORM = False
        self.CUR_DIRECTION = 's'
        """
        self.WOLF = pygame.image.load('./sprites/wolf/wolf_f0.png')
        """
        
    """
    # Turn into Wolf
    def TRANSFORMING(self):
        self.TRANSFORM = not self.TRANSFORM
    """

"""
class MIDNA:
    def __init__(self):
        self.SPRITE_POS = pygame.transform.scale(pygame.image.load('./sprites/midna.png'), (50, 75))
        self.APPEARED = False
"""