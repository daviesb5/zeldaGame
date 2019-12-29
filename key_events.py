import pygame
import sys

"""
Lib for all key events
"""

"""
Compass directions: N/S, E/W
"""
# IMAGES FOR LINK ANIMATED WALKING
img_path = './sprites/link/'
move = '00'
n_path = img_path + 'n' + move
w_path = img_path + 'w' + move
s_path = img_path + 's' + move
e_path = img_path + 'e' + move

"""
Note: Range of 10 means images go from ?000 to ?009. Having a range of 11 renders the last image ?0010, which returns an error.
"""
n_images = [n_path+str(n)+'.png' for n in range(10)]
w_images = [w_path+str(w)+'.png' for w in range(10)]
s_images = [s_path+str(s)+'.png' for s in range(10)]
e_images = [e_path+str(e)+'.png' for e in range(10)]

"""
Old directions: F/B, R/L

# IMAGES FOR LINK ANIMATED WALKING
img_path = './sprites/link/link_'
f_path = img_path + 'f' 
b_path = img_path + 'b'
r_path = img_path + 'r'
l_path =  img_path + 'l'

n_images = [f_path+str(f)+'.png' for f in range(7)]
n_images = [b_path+str(b)+'.png' for b in range(7)]
e_images = [r_path+str(r)+'.png' for r in range(7)] 
w_images = [l_path+str(l)+'.png' for l in range(7)]

# IMAGES FOR WOLF LINK ANIMATED WALKING
img_path = './sprites/wolf/wolf_'
wolf_f_path = img_path + 'f'
wolf_b_path = img_path + 'b'
wolf_r_path = img_path + 'r'
wolf_l_path = img_path + 'l'

wolf_n_images = [wolf_f_path + str(f) + '.png' for f in range(7)]
wolf_n_images = [wolf_b_path + str(b) + '.png' for b in range(7)]
wolf_e_images = [wolf_r_path + str(r) + '.png' for r in range(4)]
wolf_w_images = [wolf_l_path + str(l) + '.png' for l in range(4)]
"""

class KeyEvents:
    def __init__(self, PLAYER):
        self.PLAYER = PLAYER
        self.counter = 0
        self.wolf_counter = 0
        self.wolf_counter_lr = 0
        self.movement = .25
        self.orbs = []

    def global_events(self):
        if self.PLAYER.TRANSFORM:
            self.movement =  .5
        else:
            self.movement = .25

    def quit(self):
        pygame.quit()
        sys.exit()

    def key_down(self):
        self.PLAYER.PLAYER_POS[1] += self.movement
        self.PLAYER.DIRECTION = 's'

        self.PLAYER.SPRITE_POS = pygame.image.load(s_images[self.counter])
        self.counter = (self.counter + 1) % len(s_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_s_images[self.wolf_counter])
            self.wolf_counter = (self.wolf_counter + 1) % len(wolf_s_images)

    def key_up(self):
        self.PLAYER.PLAYER_POS[1] -= self.movement 
        self.PLAYER.DIRECTION = 'n'

        self.PLAYER.SPRITE_POS = pygame.image.load(n_images[self.counter])
        self.counter = (self.counter + 1) % len(n_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_n_images[self.wolf_counter])
            self.wolf_counter = (self.wolf_counter + 1) % len(wolf_n_images)

    def key_left(self):
        self.PLAYER.PLAYER_POS[0] -= self.movement 
        self.PLAYER.DIRECTION = 'w'

        self.PLAYER.SPRITE_POS = pygame.image.load(w_images[self.counter])
        self.counter = (self.counter + 1) % len(w_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_w_images[self.wolf_counter_lr])
            self.wolf_counter_lr = (self.wolf_counter_lr + 1) % len(wolf_w_images)

    def key_right(self):
        self.PLAYER.PLAYER_POS[0] += self.movement
        self.PLAYER.DIRECTION = 'e'

        self.PLAYER.SPRITE_POS = pygame.image.load(e_images[self.counter])
        self.counter = (self.counter + 1) % len(e_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_e_images[self.wolf_counter_lr])
            self.wolf_counter_lr = (self.wolf_counter_lr + 1) % len(wolf_e_images)

    def key_space(self):
        if self.PLAYER.HAS_SWORD:
            nen_path = '.sprites/link/'
            melee = '04'
            n_path = nen_path + 'n' + melee
            w_path = nen_path + 'w' + melee
            s_path = nen_path + 's' + melee
            e_path = nen_path + 'e' + melee
            melee += 1
            
            n_images = [n_path+str(w)+'.png' for w in range(7)]
            w_images = [w_path+str(a)+'.png' for a in range(7)]
            s_images = [s_path+str(s)+'.png' for s in range(7)]
            e_images = [e_path+str(d)+'.png' for d in range(7)]

            """
            # IMAGES FOR LINK ANIMATED WALKING
            img_path = './sprites/link/'
            move = '00'
            n_path = img_path + 'n' + move
            w_path = img_path + 'w' + move
            s_path = img_path + 's' + move
            e_path = img_path + 'e' + move

            n_images = [n_path+str(w)+'.png' for w in range(7)]
            w_images = [w_path+str(a)+'.png' for a in range(7)]
            s_images = [s_path+str(s)+'.png' for s in range(7)]
            e_images = [e_path+str(d)+'.png' for d in range(7)]

            self.PLAYER.PLAYER_INV.remove(self.PLAYER.WEAPON)
            self.PLAYER.WEAPON.PLACED = True

            # DROP WEAPON LOCATION
            if self.PLAYER.DIRECTION == 's':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] - 1
            elif self.PLAYER.DIRECTION == 'w':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] + 1
            elif self.PLAYER.DIRECTION == 'd':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0] - 1
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1]
            elif self.PLAYER.DIRECTION == 'a':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0] + 1
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1]
            """
        self.PLAYER.WEAPON = False
    
    """
    def key_w(self):
        self.PLAYER.TRANSFORMING()
    """