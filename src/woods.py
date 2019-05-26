#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
user.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

from time import sleep
from gameset import itr, Levels
import script

class Woods(object):
    def __init__(self, cname, age, level, reputation, cl):
        self.cname = cname
        self.lvl = level
        self.cl = cl
        self.age = age
        self.s = script.ws(cname)
        self.l=Levels(self.cname, self.age)

    def parse(self):
        itr(self.s, 0, 1)
        q1 = input("\n: ")
        if q1 == "left":
            if self.cl > 3:
                itr(self.s, 1, 4)
                itr(self.s, 5, 9)
                input(itr(self.s[9:12]))

            else:
                itr(self.s, 1, 5)
                raise SystemExit

        else:
            pass
        itr(self.s,13,21)
        q2 = input("\n: ")
        if q2 == 'cave':
            itr(self.s, 22, 25)
            raise SystemExit
        elif q2 == 'shrubber':
            itr(self.s, 25, 39)
        elif q2 == 'forest':
            itr(self.s, 41 , 45)
            raise SystemExit
        
        itr(self.s, 45, 48)
        
        q3 = input("\n: ")
        if q3 == 'stay':
            itr(self.s, 49, 50)
            q4=input("\n: ")
            if q4=="talk":
                itr(self.s, 52, 54)
            else:
                if self.cl == 1:
                    itr(self.s, 54, 55)
                    self.l.level_up()
                else:
                    print("The strangers have killed you.")
                    raise SystemExit

        elif q3 == 'travel on':
            self.l.level_up()
