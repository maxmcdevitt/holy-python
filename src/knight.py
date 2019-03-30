#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019

@author: Max McDevitt
"""

# Released under the GNU General Public License


import pygame


class Knight(object):

    def __init__(self, cwd):
        self.health = 100
        self.position = 1
        self.knight = pygame.image.load(f"{cwd}"+"/images/knight.bmp")
        self.k_rect = self.knight.get_rect()
        self.y = 0 # Vertical position
        self.x = 1 # Horizontal position

    def move(self, cwd):
        self.k_rect = self.k_rect.move(self.x, self.y)
        if self.k_rect.left < 0 or self.k_rect.right > 1366:
            self.x *= -1
        if self.k_rect.top < 0 or self.k_rect.bottom > 400:
            self.y *=-1