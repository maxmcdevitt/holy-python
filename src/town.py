#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
castle.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

from gameset import itr, Levels
import script


class Town(object):
    def __init__(self, cname, age, level, reputation, cl, username, password):
        self.cname,self.age,self.level,self.reputation =cname,age,level,reputation
        self.cl,self.s  = cl, script.tscript(cname, level)
        self.username, self.password = username, password
        self.l=Levels(self.cname,self.age, self.username, self.password)
    def parse(self):
      itr(self.s , 0, 14)
      q1 = input('\n: ')
      if q1 == 1:
          itr(self.s, 15, 16)
          raise SystemExit
      else:
          pass
      itr(self.s, 14, 15)
      itr(self.s , 16)
      self.l.level_up()
