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
        level=""
        reputation=0
        age,cname= gs._init()
        level, reputation = gs.level_up(level, reputation, age, cname)
        gs.save(level, age, cname, reputation)
    else:
        level, age, cname, reputation =gs.load_game()
        print(f"Welcome back, {cname.title()}.")
    l.navigate(cname, level, reputation, age)
run()
