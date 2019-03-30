#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
graphics_main.py
@author: Max McDevitt
"""

# Released under the GNU General Public License

VERSION = "1"

import sys, os
from knight import Knight
import pygame as pg

def main():
    pg.init()
    cwd = os.getcwd()
    k = Knight(cwd)

    screen = pg.display.set_mode((1366, 768))

    background = pg.image.load('images/bg.jpg').convert()


    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        k.move(cwd)
        screen.blit(background, (0, 0))        #draw the background
        screen.blit(k.knight, k.k_rect)
        pg.display.flip()

if __name__ == '__main__': 
    main()