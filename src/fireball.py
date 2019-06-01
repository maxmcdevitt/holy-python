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
    def __init__(self, screen, knight):
        """Create a fb object, at the ship's current position."""
        super(Fireball, self).__init__()
        self.screen = screen

        # Create fb rect at (0, 0), then set correct position.
        self.rect = pg.Rect(0, 0, 3, 3)
        self.rect.centerx = knight.rect.centerx
        self.rect.top = knight.rect.top
        
        # Store a decimal value for the fb's position.
        self.y = float(self.rect.y)

        self.speed_factor = 4

    def update(self):
        # Update the decimal position of the fb.
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_fb(self):
        """Draw the fb to the screen."""
        pg.draw.rect(self.screen, (60,60,60), self.rect)