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
from user import Arrow, Bow
import functions as func
from pygame.sprite import Group


def main():
    pg.init()
    cwd = os.getcwd()
    k = Knight(cwd)

    screen = pg.display.set_mode((1366, 768))

    background = pg.image.load('images/bg.jpg').convert()

    bow = Bow(screen)
    arrow = Arrow(screen)
    arrows = Group()

    while 1:
        func.check_events(screen,bow,arrows)
        k.move(cwd)
        bow.update()
        func.update_arrows(screen, bow, arrows)
        screen.blit(background, (0, 0))        #draw the background
        screen.blit(k.knight, k.k_rect)
        for arrow in arrows.sprites():
            arrow.blitme()
        bow.blitme()
        
        pg.display.flip()

if __name__ == '__main__': 
    main()