#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
user.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

from gameset import itr, Levels
import sys, time, os
import script

y=['y','yes']
yes = [x.lower() for x in y]

class Cave(object):
    def __init__(self, cname, age, level, reputation, cl, username, password):
        self.cname,self.age,self.level,self.reputation =cname,age,level,reputation
        self.cl,self.s  = cl, script.cs(cname)
        self.username, self.password = username, password

    def parse(self):
        """  Parses the script and outputs nicely formatted text. """
        l =Levels(self.cname, self.age, self.username, self.password)

        itr(self.s, 0, 15)
        q1 = input("\n: ")
        if q1 in yes:
             pass
        else:
             raise SystemExit

        itr(self.s, 16, 38)
        if self.cl == 2:
            itr(self.s, 38, 39)
            l.level_up()
        else:
            itr(self.s, 39, 40)
            raise SystemExit

        itr(self.s, 40, 42)
        q2 = input("\n: ")

        if q2 == '1':
            itr(self.s, 43, 45)
            l.level_up()
        else:
            itr(self.s, 44, 46)

        itr(self.s, 46, 48)
        q3 = input("\n: ")
        if q3 == '1':
            itr(self.s, 49, 55)
        else:
            itr(self.s, 55, 60)
            print("The lock quickly rotates to reveal a number!\n")
            time.sleep(3)
            _=os.system("clear")
            import random
            num = random.randint(10000, 90000)
            num = str(num)
            print(num)
            time.sleep(2)
            _=os.system("clear")
            q4 = input("What was the number?\n: ")
            if q4 == num:
                itr(self.s, 60, 61)
                l.level_up()
            else:
                itr(self.s, 61, 63)
                raise SystemExit
