#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019

@author: Max McDevitt
"""
# Released under the GNU General Public License

from time import sleep
import  pygame as pg
from pygame.sprite import Sprite

class Fireball(Sprite):
    def __init__(self, screen, cwd):
        super().__init__()
        self.fb = pg.image.load(f"{cwd}"+"/images/fireball.bmp")
        self.screen = screen
        self.f_rect = self.fb.get_rect()
        self.y = float(self.f_rect.y)
        self.x = 1 # Horizontal position

    def update(self):
        """Move the arrow up the screen."""
        self.f_rect = self.f_rect.move(self.x, self.y)
        if self.f_rect.left < 0 or self.f_rect.right > 1366:
            self.x *= -1
        if self.f_rect.top < 0 or self.f_rect.bottom > 500:
            self.y *= -1 

#        self.y += 1                          #         future reference just copy the arrow code from github
                                              #         y +=1 is right just have to make the fireball random and disappear
        # Update the rect position.
        self.f_rect.y = self.y

    def blitme(self):
#       sleep(1)
       self.screen.blit(self.fb , self.f_rect)
#       sleep(1)