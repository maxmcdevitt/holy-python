#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
user.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

from time import sleep
import gameset as gs
import loc

a1 = ['town', 'woods','cave','castle','cottage'
        ,'dungeon','cathedral']

def woods2(cname, level, age, reputation):
    script = [
    "You travel further in the woods and come across a small village.",
    "The people there seem primal and hostile.",]
    for i in script:
        print("\n"+i)
        sleep(2)
    ta6 = input("\nWhat do you do?[stay or travel on]")
    if ta6 == 'stay':
        print("\nWhat do you want to do with the people?"+
              " [talk or kill] ")
        w2q = input("\n: ")
        if w2q == 'talk':
            sleep(2)
            print("You talk to the strangers, they act very nice and welcoming...")
            sleep(3)
            print("You go into one of the tents and see a dead body...")
            sleep(3)
            print("\nThe strangers capture you and everything goes black...")
            sleep(2)
            loc.navigate(cname, reputation, level)
        if w2q == 'kill':
            print("They gave a good fight, but you have succesfully killed the strangers.")
            sleep(2)
            gs.level_up(level, reputation, age, cname)
            loc.navigate(cname, level, reputation, age)


    if ta6 == 'travel on':
        print("\nThe woods opens up, and you see the light...")
        sleep(3)
        gs.level_up(level, reputation, age, cname)
        print("\nWhere do you want to go to now?")
        loc.navigate(cname, level, reputation, age)



def woods(cname, level, reputation, age):
    wq1 = input("\nYou see a dark opening to the woods, do you want to enter? [y/n]\n:: ")
    if wq1 == 'n':
        raise SystemExit
    if wq1 == 'y':
        sleep(2)
        wq2 = input(
"""\nYou are following the path, it's eerie, quiet and
mysterious. Upon further investigation you come upon a fork in the path, do you
go left or right? """)
        if wq2 == 'left':
            sleep(2)
            print("\nYou went left...")
            sleep(2)
            print("\nit becomes darker...")
            sleep(3)
            print("\nOh no you see a mythical dragon!")
            sleep(2)
            reputation = int(reputation)
            if reputation <=0:
                sleep(2)
                print("\nYou have been slain by the dragon:(")
            else:
                print("\nYou slay the dragon!")
                sleep(2)
                print("""\nFurther along you see a treacherous bridge, as you begin
walking closer you see an old man in dark clothes.""")
                sleep(2)
                print(
"""'\nStop. Who would cross this bridge must answer these three questions, ere the
other side he see.'""")
                q2b1 = input("What is your name?")
                if q2b1 != cname:
                    print("That is not your name, you have ben cast off the bridge!")
                    raise SystemExit
                else:
                    q2b2 = input("\nWhat is your favorite color?")
                    q2b3 = input("""\nWhat is the air-speed velocity of an
unladen swallow?\n(Hint, ask the gatekeeper 'an african or
european swallow?'""")
                    if q2b3 == '\nan african or european swallow?'.lower():
                     print("\nThe gatekeeper stammers and makes an exuse, then is cast off the bridge.")

        if wq2 == 'right':
            print("\nYou went right, it is dry, foggy,  and life seems sparse.")
            sleep(2)
            print("\nAs you venture down the path you hear scurried movement and see"+
                  " shadows in the periphery.")
            sleep(2)
            print("\nYou start to get anxious...")
            sleep(2)
            print("\nYou look up and suddenly see tall people draped in dark ragged clothing!")
            sleep(2)
            print(
            """\nOne of them says, "We are the knights of ni, ping, and nee-wom. In order to pass we require a...""")
            sleep(2)
            print("SHRUBBERY!")
            sleep(2)
            print("Your task is to now find a shrubbery, where do you look?")
            sleep(2)
            shrub = ['the cave',' the local shruber',' or search the forest.']
            for s in shrub:
                print('\n['+s+']')
            ans = input("[cave, shrubber, or forest]\n: ")
            if ans == 'cave':
                sleep(2)
                print("\nYou enter the cave...")
                sleep(2)
                print("\nThere is nothing but rocks. (Suprise)")
                sleep(2)
                print("\nYou see writing etched in the wall, it reads"+
                      """ 'Here may be found the last words of Joseph of
                Arathamia. He who is valiant and pure of spirit may find
              the holy grail in the castle of Aaauuuggghhh...'""")
                sleep(2)
                print("The monster appears and kills you. :(")
                raise SystemExit
            if ans == 'shrubber':
                print("\nYou go to the town shrubber.")
                sleep(2)
                print(cname + ": 'Hello I would like to purchase a shrubbery.'")
                sleep(3)
                print("\nShrubber: 'And why do you think I would have that?'")
                sleep(2)
                print(cname + ": 'Becuase you're the shrubber...'")
                sleep(2)
                print("\nShrubber: 'And?'")
                sleep(3)
                print(cname + ": 'What?'")
                sleep(3)
                print("\nShrubber: 'Ok fine I will sell you a shrubbery for...'")
                sleep(2)
                print("\nA CHICKEN!'")
                sleep(2)
                print("\nYou kill the shrubber and take the shrubbery.")
                sleep(2)
                print("\nYou return to the knights of Ni and give them the shrubbery.")
                sleep(2)
                print("\nThey say, 'Thank you for the shrubbery...'")
                sleep(2)
                print(cname +": Can I pass?")
                sleep(2)
                print("Knights of Ni: To pass we need a...")
                sleep(2)
                print("You kill the Knights of Ni.")
                woods2(cname, level, age, reputation)
            if ans == 'forest':
                print("You search around the forest.")
                sleep(2)
                print("You search the forest.")
                sleep(2)
                print("You walk along the path.")
                sleep(2)
                print("Ow! You tripped and fell down a large hole.")
                sleep(2)
                print("It was a rabbit hole.")
                sleep(2)
                print("This isn't very good....")
                loc.navigate(cname, level, reputation)

