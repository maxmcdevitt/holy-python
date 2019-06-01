#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
castle.py
@author: Max McDevitt
"""
# Released under the GNU General Public License
import script
from gameset import itr, Levels

class Castle(object):
    def __init__(self,cname, age, level, reputation, cl, username, password):
        self.cname,self.age,self.level,self.reputation, self.username, self.password = cname,age,level,reputation, username, password
        self.cl,self.s  = cl, script.csts(cname, level)
        self.l=Levels(self.cname,self.age, self.username, self.password)

    def parse(self):
        itr(self.s, 0, 4)

        itr(self.s, 4, 5)
        q1 = input("\n: ")

        if q1 == '1':
            if self.cl != 5:
                itr(self.s, 5, 9)
            else:
                itr(self.s, 9, 13)
                raise SystemExit
        else:
            if self.cl != 5:
                itr(self.s, 14, 15)
                raise SystemExit
            else:
                itr(self.s, 15, 19)
        itr(self.s, 19, 20)
        q2 = input("\n: ")

        if q2 == '1':
            if self.cl == 5:
                itr(self.s, 23, 25)
            else:
                itr(self.s, 20, 23)
                raise SystemExit
        else:
            itr(self.s, 26, 38)
            if self.cl != 5:
                itr(self.s, 38, 39)
                raise SystemExit
            else:
                itr(self.s, 39, 45)
                self.l.level_up()
