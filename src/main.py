#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:26:14 2018
main.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

import gameset as gs
import loc as l


active = True
incative = False

def run():
    q = input("Do you want to start a new game?[y/n]\n: ")
    if q == 'y':
        
        cname, age = gs._init()
        cl, level, reputation = gs.level_up(cname, age)
        gs.save(level, age, cname, reputation, cl)

    else:
        level, age, cname, reputation =gs.load_game()
        print(f"\nWelcome back, {cname}.\n")

    l.navigate(cname, level, reputation, age, cl)

run()
