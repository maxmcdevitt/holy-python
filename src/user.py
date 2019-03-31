#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
user.py
@author: Max McDevitt
"""

# Released under the GNU General Public License

import pygame as pg
import sys, os
from pygame.sprite import Sprite

global cwd
cwd = os.getcwd()

class Bow(Sprite):
    def __init__(self, screen):
        super().__init__()

        self.bow = pg.image.load(f"{cwd}"+"/images/bow.bmp")
        self.screen = screen
        self.rect = self.bow.get_rect()

        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center =  float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False        
    
    def center_bow(self):
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the bow's position, based on movement flags."""
        # Update the bow's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= 1
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the bow at its current location."""
        self.screen.blit(self.bow, self.rect)

class Arrow(Bow):
    def __init__(self, screen):
        super().__init__(screen)
        self.y = float(self.rect.y)
        self.arrow = pg.image.load(f"{cwd}"+"/images/arrow.bmp")
        self.screen = screen
        self.b = Bow(screen)
        self.arect = self.b.rect

    def update(self):
        """Move the arrow up the screen."""
        # Update the decimal position of the bullet.
        self.y -= 3
        # Update the rect position.
        self.rect.y = self.y
    def blitme(self):
        self.screen.blit(self.arrow, self.arect.center) #TODO: Fix this <