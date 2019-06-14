#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2019
main.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

import os, getpass
import gameset as gs
from woods import Woods
from cave import Cave
from castle import Castle
from town import Town
from unknown import Unknown


YES = [x.lower() for x in ['yes', 'y']]
NO = [x.lower() for x in ['no', 'n']]


cwd = os.getcwd()

class Main(object):
    """
    Overly Complex Program
    """

    def start(self):
        """
        Iinitializes the game.
        """

        q = input("Do you want to start a new game?[y/n]\n: ")

        if q in YES:
            cname, age, username, password = gs.initialize_new_game()
            l = gs.Levels(cname, age, username, password)
            cl, level, reputation = l.level_up()

        else:
            gs.login()
            l = gs.load_variables("level", "age", "cname", "reputation", "cl", "username", "password")
            level,age,cname,reputation,cl,username,password=l[0],l[1],l[2],l[3],l[4],l[5],l[6]
        gs.save(level, age, cname, reputation, cl, username, password)

        return cname, age, level, reputation, cl, username, password

    def locs(self, cname, age, level, reputation, cl, username, password):
        """
        Acts as a portal to locations
        """
        arg = [cname, age, level, reputation, cl, username, password]
        woods = Woods(*arg)
        cave = Cave(*arg)
        castle = Castle(*arg)
        town = Town(*arg)
        unknown = Unknown(*arg)

        locations = {
            "woods" : woods,
            "cave" : cave,
            "castle" : castle,
            "town" : town,
            "unknown": unknown
        }
        while True:
            q = input("\nDo you want to travel? ")
            if q in NO:
                raise SystemExit

            if q in YES:
                print("Where do you want to travel to?")
                for k in locations.keys():
                    print(k.title())
                dest = input('\n: ')
                if dest in locations.keys():
                    return locations[dest].parse()
            elif q in NO:
                raise SystemExit

            elif q not in YES or q not in NO:
                print("That is not a location, try again.")
                pass

    def run(self):
        arg = self.start()
        self.locs(*arg)


if __name__ == "__main__":
    main = Main()
    while True:
        main.run()
