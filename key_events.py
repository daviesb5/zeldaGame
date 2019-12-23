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
w_path = img_path + 'n' + move
a_path = img_path + 'w' + move
s_path = img_path + 's' + move
d_path = img_path + 'e' + move

w_images = [w_path+str(w)+'.png' for w in range(7)]
a_images = [a_path+str(a)+'.png' for a in range(7)]
s_images = [s_path+str(s)+'.png' for s in range(7)]
d_images = [d_path+str(d)+'.png' for d in range(7)]

"""
Old directions: F/B, R/L

# IMAGES FOR LINK ANIMATED WALKING
img_path = './sprites/link/link_'
f_path = img_path + 'f' 
b_path = img_path + 'b'
r_path = img_path + 'r'
l_path =  img_path + 'l'

n_images = [f_path+str(f)+'.png' for f in range(7)]
w_images = [b_path+str(b)+'.png' for b in range(7)]
d_images = [r_path+str(r)+'.png' for r in range(7)] 
a_images = [l_path+str(l)+'.png' for l in range(7)]
"""
# IMAGES FOR WOLF LINK ANIMATED WALKING
img_path = './sprites/wolf/wolf_'
wolf_f_path = img_path + 'f'
wolf_b_path = img_path + 'b'
wolf_r_path = img_path + 'r'
wolf_l_path = img_path + 'l'

wolf_n_images = [wolf_f_path + str(f) + '.png' for f in range(7)]
wolf_w_images = [wolf_b_path + str(b) + '.png' for b in range(7)]
wolf_d_images = [wolf_r_path + str(r) + '.png' for r in range(4)]
wolf_a_images = [wolf_l_path + str(l) + '.png' for l in range(4)]


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
        self.PLAYER.DIRECTION = 'd'

        self.PLAYER.SPRITE_POS = pygame.image.load(s_images[self.counter])
        self.counter = (self.counter + 1) % len(s_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_s_images[self.wolf_counter])
            self.wolf_counter = (self.wolf_counter + 1) % len(wolf_s_images)

    def key_up(self):
        self.PLAYER.PLAYER_POS[1] -= self.movement 
        self.PLAYER.DIRECTION = 'u'

        self.PLAYER.SPRITE_POS = pygame.image.load(w_images[self.counter])
        self.counter = (self.counter + 1) % len(w_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_w_images[self.wolf_counter])
            self.wolf_counter = (self.wolf_counter + 1) % len(wolf_w_images)

    def key_left(self):
        self.PLAYER.PLAYER_POS[0] -= self.movement 
        self.PLAYER.DIRECTION = 'l'

        self.PLAYER.SPRITE_POS = pygame.image.load(a_images[self.counter])
        self.counter = (self.counter + 1) % len(a_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_a_images[self.wolf_counter_lr])
            self.wolf_counter_lr = (self.wolf_counter_lr + 1) % len(wolf_a_images)

    def key_right(self):
        self.PLAYER.PLAYER_POS[0] += self.movement
        self.PLAYER.DIRECTION = 'r'

        self.PLAYER.SPRITE_POS = pygame.image.load(d_images[self.counter])
        self.counter = (self.counter + 1) % len(d_images)

        if self.PLAYER.TRANSFORM:
            self.PLAYER.WOLF  = pygame.image.load(wolf_d_images[self.wolf_counter_lr])
            self.wolf_counter_lr = (self.wolf_counter_lr + 1) % len(wolf_d_images)

    def key_space(self):
        if self.PLAYER.WEAPON:
            new_path = '.sprites/link/'
            melee = '04'
            w_path = new_path + 'n' + melee
            a_path = new_path + 'w' + melee
            s_path = new_path + 's' + melee
            d_path = new_path + 'e' + melee
            """
            # IMAGES FOR LINK ANIMATED WALKING
            img_path = './sprites/link/'
            move = '00'
            w_path = img_path + 'n' + move
            a_path = img_path + 'w' + move
            s_path = img_path + 's' + move
            d_path = img_path + 'e' + move

            w_images = [w_path+str(w)+'.png' for w in range(7)]
            a_images = [a_path+str(a)+'.png' for a in range(7)]
            s_images = [s_path+str(s)+'.png' for s in range(7)]
            d_images = [d_path+str(d)+'.png' for d in range(7)]

            self.PLAYER.PLAYER_INV.remove(self.PLAYER.WEAPON)
            self.PLAYER.WEAPON.PLACED = True

            # DROP WEAPON LOCATION
            if self.PLAYER.DIRECTION == 'd':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] - 1
            elif self.PLAYER.DIRECTION == 'u':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] + 1
            elif self.PLAYER.DIRECTION == 'r':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0] - 1
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1]
            elif self.PLAYER.DIRECTION == 'l':
                    self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0] + 1
                    self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1]
            """
        self.PLAYER.WEAPON = False
    
    def key_w(self):
        self.PLAYER.TRANSFORMING()
