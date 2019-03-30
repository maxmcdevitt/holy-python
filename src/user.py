#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
user.py
@author: Max McDevitt
"""

# Released under the GNU General Public License


import pygame as pg
import sys

class User(object):
    def __init__(self, cwd):
        self.health = 100
        self.position = 1

        self.arrow = pg.image.load(f"{cwd}"+"/arrow.bmp")
        self.bow = pg.image.load(f"{cwd}"+"/bow.bmp")
        
        self.k_rect = self.arrow.get_rect()
        self.y = 0 # Vertical position
        self.x = 1 # Horizontal position

    def move(self):
        for event in pygame.event.get():
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    user.moveup()
                if event.key == K_DOWN:
                    user.movedown()
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    user.movepos = [0,0]
        
    
    def bow(self):

    def arrow(self):