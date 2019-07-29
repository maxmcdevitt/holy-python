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
from time import sleep
import os

y=['y','yes']
YES = [x.lower() for x in y]

class RunLevels(object):
    def __init__(self,cname, age, level, reputation, cl, username, password):
        self.cname,self.age,self.level,self.reputation,self.username,self.password=cname,age,level,reputation,username,password
        self.cl  = cl
        self.l=Levels(self.cname,self.age, self.username, self.password)
        self.castle_script = script.csts(cname, level)
        self.cave_script = script.cs(cname)
        self.woods_script = script.ws(cname)
        self.unknown_script = script.unknown(cname)
        self.town_script = script.tscript(cname, level)
        self.camelot_script = script.camelot(cname, level)

    def parse_woods(self):
        itr(self.woods_script, 0, 1)
        q1 = input("\n: ")
        if q1 == "left":
            if self.cl > 3:
                itr(self.woods_script, 1, 4)
                itr(self.woods_script, 5, 9)
                input(itr(self.woods_script[9:12]))

            else:
                itr(self.woods_script, 1, 5)
                raise SystemExit

        else:
            pass
        itr(self.woods_script,13,21)
        q2 = input("\n: ")
        if q2 == 'cave':
            itr(self.woods_script, 22, 25)
            raise SystemExit
        elif q2 == 'shrubber':
            itr(self.woods_script, 25, 39)
        elif q2 == 'forest':
            itr(self.woods_script, 41 , 45)
            raise SystemExit

        itr(self.woods_script, 45, 48)

        q3 = input("\n: ")
        if q3 == 'stay':
            itr(self.woods_script, 49, 50)
            q4=input("\n: ")
            if q4=="talk":
                itr(self.woods_script, 52, 54)
            else:
                if self.cl == 1:
                    itr(self.woods_script, 54, 55)
                    self.l.level_up()
                else:
                    print("The strangers have killed you.")
                    raise SystemExit

        elif q3 == 'travel on':
            self.l.level_up()
 

    def parse_cave(self):
        itr(self.cave_script, 0, 15)
        q1 = input("\n: ")
        if q1 in YES:
             pass
        else:
             raise SystemExit

        itr(self.cave_script, 16, 38)
        if self.cl == 2:
            itr(self.cave_script, 38, 39)
            self.l.level_up()
        else:
            itr(self.cave_script, 39, 40)
            raise SystemExit

        itr(self.cave_script, 40, 42)
        q2 = input("\n: ")

        if q2 == '1':
            itr(self.cave_script, 43, 45)
            self.l.level_up()
        else:
            itr(self.cave_script, 44, 46)

        itr(self.cave_script, 46, 48)
        q3 = input("\n: ")
        if q3 == '1':
            itr(self.cave_script, 49, 55)
        else:
            itr(self.cave_script, 55, 60)
            print("The lock quickly rotates to reveal a number!\n")
            sleep(3)
            _=os.system("clear")
            import random
            num = random.randint(10000, 90000)
            num = str(num)
            print(num)
            sleep(2)
            _=os.system("clear")
            q4 = input("What was the number?\n: ")
            if q4 == num:
                itr(self.cave_script, 60, 61)
                self.l.level_up()
            else:
                itr(self.cave_script, 61, 63)
                raise SystemExit


    def parse_town(self):
      itr(self.town_script , 0, 14)
      q1 = input('\n: ')
      if q1 == 1:
          itr(self.town_script, 15, 16)
          raise SystemExit
      else:
          pass
      itr(self.town_script, 14, 15)
      itr(self.town_script , 16)
      self.l.level_up()

    def parse_castle(self):
        itr(self.castle_script, 0, 4)

        itr(self.castle_script, 4, 5)
        q1 = input("\n: ")

        if q1 == '1':
            if self.cl != 5:
                itr(self.castle_script, 5, 9)
            else:
                itr(self.castle_script, 9, 13)
                raise SystemExit
        else:
            if self.cl != 5:
                itr(self.castle_script, 14, 15)
                raise SystemExit
            else:
                itr(self.castle_script, 15, 19)
        itr(self.castle_script, 19, 20)
        q2 = input("\n: ")

        if q2 == '1':
            if self.cl == 5:
                itr(self.castle_script, 23, 25)
            else:
                itr(self.castle_script, 20, 23)
                raise SystemExit
        else:
            itr(self.castle_script, 26, 38)
            if self.cl != 5:
                itr(self.castle_script, 38, 39)
                raise SystemExit
            else:
                itr(self.castle_script, 39, 45)
                self.l.level_up()

    def parse_unknown(self):
        itr(self.unknown_script, s=0, e=9)
        if self.cl!=6:
            print("\nYou were killed by the guards.\n")
            raise SystemExit
        itr(self.unknown_script, s=10, e=-1, t=2)

    def parse_camelot(self):
        pass
