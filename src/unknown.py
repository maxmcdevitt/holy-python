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
from script import unknown

class Unknown(object):
    def __init__(self, cname, age, level, reputation, cl, username, password):
        self.username = username
        self.password = password
        self.cname = cname
        self.lvl = level
        self.cl = cl
        self.age = age
        self.s = unknown(cname)
        self.l=Levels(self.cname, self.age, self.username, self.password)

    def parse(self):
        itr(self.s, s=0, e=9)
        if self.cl!=6:
            print("\nYou were killed by the guards.\n")
            raise SystemExit
        itr(self.s, s=10, e=-1, t=2)