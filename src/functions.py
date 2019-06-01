#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
functions.py
@author: Max McDevitt
"""

# Released under the GNU General Public License

import sys
from scoreboard import Scoreboard
from time import sleep
import pygame as pg
from user import Arrow
from pygame.locals import *



def check_keydown_events(event, screen, bow, arrows):
    """Respond to keypresses."""
    if event.key == K_RIGHT:
        bow.moving_right = True
    elif event.key == K_LEFT:
        bow.moving_left = True
    elif event.key == K_SPACE:
        fire_arrow( screen, bow, arrows)
    elif event.key == K_q:
        sys.exit()
        
def check_keyup_events(event, bow):
    """Respond to key releases."""
    if event.key == K_RIGHT:
        bow.moving_right = False
    elif event.key == K_LEFT:
        bow.moving_left = False

def check_events(screen,bow, arrows):
    """Respond to keypresses and mouse events."""
    for event in pg.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            check_keydown_events(event,  screen, bow, arrows)
        elif event.type == KEYUP:
            check_keyup_events(event, bow)
            
def fire_arrow( screen, bow, arrows):
    """Fire a arrow, if limit not reached yet."""
    # Create a new arrow, add to arrows group.
    if len(arrows) < 1:
        new_arrow = Arrow(screen, bow)
        arrows.add(new_arrow)

def update_arrows(screen, bow, arrows):
    """Update position of arrows, and get rid of old arrows."""
    # Update arrow positions.
    arrows.update()

    # Get rid of arrows that have disappeared.
    for arrow in arrows.copy():
        if arrow.rect.bottom <= 0:
            arrows.remove(arrow)

def update_fbs(screen, bow, knight, fbs, arrows):
    """Update position of fireballs, and get rid of old fireballs."""
    # Update arrow positions.
    fbs.update()

    # Get rid of fireballs that have disappeared.
    for fb in fbs.copy():
        if fb.rect.bottom <= 0:
            fb.remove(fb)
    check_fb_bow_collisions(screen, bow,  fbs, arrows)

def win(screen):
    pg.font.init()
    font = pg.font.Font(None, 36)
    
    while range(900):
        bg = (250,250,250)
        msg = font.render("You Win!!!", 1, (10, 10, 10))
        textpos = msg.get_rect()
        textpos.centerx = textpos.centerx
        screen.fill(bg)
        sleep(.5)
        screen.blit(msg, (50,50))
        sleep(.5)
        screen.fill(bg)
#        bg.blit(msg, 50)
        pg.display.flip()
             
        
def check_arrow_knight_collision(screen, bow, knight, arrow):
    """Respond to arrow-knight collisions."""
    # Remove any arrows that have collided.
    global sb
    sb = Scoreboard(screen)
    collisions = knight.k_rect.colliderect(arrow.arrow.get_rect())
#    pg.sprite.groupcollide(arrows, knight.k_rect, True, True)
    health = 100
    if collisions:
        health - 5
#        arrows.remove(arrow)
        sb.show_health(health)
    if knight.health == 0:
        win(screen)

def check_fb_bow_collisions(screen, bow, fbs, arrows):
    """Respond to arrow-knight collisions."""
    # Remove any arrows that have collided.
    collisions = pg.sprite.groupcollide(fbs, bow, True, True)
    
    if collisions:
        bow.health - 20
#    if len(bow) == 0:
#        lose()
#        raise SystemExit
        # If the entire fleet is destroyed, start a new level.



def bow_hit(screen, bow, arrows):
    """Respond to bow being hit by knight."""
    bows_left= 3
    if bows_left > 0:
        # Decrement bows_left.    font = pygame.font.Font(None, 36)

        bows_left -= 1
    else:
        raise SystemExit
    # Empty the list of  and arrows.
    arrows.empty()
    
    # center the bow.
    bow.center_bow()
    sleep(0.5)