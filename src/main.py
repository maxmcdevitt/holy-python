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
import levels

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
        rl = levels.RunLevels(*arg)        

        locations = {
            "woods" : rl.parse_woods ,
            "cave" : rl.parse_cave ,
            "castle" : rl.parse_castle ,
            "town" : rl.parse_town ,
            "unknown": rl.parse_unknown 
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
                    return locations[dest]()

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
