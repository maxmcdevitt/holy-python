#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:26:14 2018
castle.py
@author: Max McDevitt
"""
# Released under the GNU General Public License


import time
import loc
import gameset as gs

def killspree(cname, level, reputation, age):
    print("\nYou take out you sword and stab and slash everyone in sight.")
    time.sleep(2)
    print("\nA fleet of guards arrive...")
    with open("/home/i3/python/medieval_game/src/cl.json") as f:
        cl = f.read()
        f.close()
        cl=int(cl)

    if cl < 4:
        print("The guards have killed you...")
        time.sleep(2)
        loc.navigate(cname, level, reputation)
    else:
        print("\nYou have killed the guards!")
        time.sleep(2)
        print("\nAnd everyone else...")
        time.sleep(2)
        print("\nThere is nothing but a pile of dead bodies now...")
        time.sleep(2)
        gs.level_up(level, reputation, age, cname)
        loc.navigate(cname, level, reputation)


def settle(cname, level, reputation, age):
    time.sleep(2)
    print("\nYou choose to settle in one of the local camp")
    time.sleep(2)
    print("\nYou see a armed knight in your path...")
    time.sleep(2)
    print(f"\n{cname}: You fight with the strength of many men, Sir Knight.")
    time.sleep(2)
    print("\nKnight: No response")
    time.sleep(2)
    print(f"{cname}: I am {cname}.")
    time.sleep(2)
    print("\nKnight: No response.")
    time.sleep(2)
    print(f"\n{cname}: You have proved yourself worthy, Sir Knight. (Tries to pass)")
    time.sleep(2)
    print("\nKnight: None shall poss.")
    time.sleep(2)
    print(f"\n{cname}: What?")
    time.sleep(2)
    print("\nNone shall pass!")
    time.sleep(2)
    print(f"\n{cname}: I have no quarrel with you, good Sir Knight, but I shall pass.")
    time.sleep(2)
    print("\nKnight: Then you shall die!")
    with open("/home/i3/python/medieval_game/src/cl.json") as f:
        cl = f.read()
        f.close()
        cl=int(cl)
    if cl < 4:
        time.sleep(2)
        print("\nThe Knight has killed you...")
        loc.navigate(cname, level, reputation, age)
    else:
        time.sleep(2)
        print("\nYou have cut off the Knight's right arm.")
        time.sleep(2)
        print(f"\n{cname}: Now stand aside worthy adversary!")
        time.sleep(2)
        print("\nKnight: Tis' but a scratch!")
        time.sleep(2)
        print(f"\nA scratch? You arm's off!")
        time.sleep(2)
        print(f"\nknight: I've had worse...\n{time.sleep(1)}Come on you pansy")
        time.sleep(1.5)
        print("\nYou effectively dismember the rest of the knights limbs...")
        time.sleep(2)
        gs.level_up(level, reputation, age, cname)

def castle1(cname, level, reputation, age):
    time.sleep(2)
    print("\nYou enter the castle. It is enormous and full of people.")
    time.sleep(2)
    print("\nThere are many guards here.")
    time.sleep(2)
    print("\nWhat do you wish to do now?")
    time.sleep(1)
    castq2 = input("\n1 [killing spree]\n2 [settle in with the people]\n: ")
    if castq2 == '1':
        killspree(cname, level, reputation, age)
    if castq2 == '2':
        settle(cname, level, reputation, age)

def castle(cname, level, reputation, age):
    print("\nYou knock on the large wooden door.")
    time.sleep(2)
    print("\nGuard: Who goes there?")
    time.sleep(2)
    print(f'\n{cname.title()}:it is I, {cname}.')
    time.sleep(2)
    print("\nGuard: What is your buisness here?")
    castq = input("Do you\n1[lie]\nor\n2['tell truth']\n: ")
    with open("/home/i3/python/medieval_game/src/cl.json") as f:
        cl = f.read()
        f.close()
        cl=int(cl)

    if castq == '1':
        reputation = int(reputation)
        if cl >=3:
            print(f"\n{cname}: ...well")
            time.sleep(2)
            print(f"{cname}: ..umm..")
            time.sleep(2)
            print(f"\n{cname}: Let's just say I am very important.")
            time.sleep(1.5)
            print("\nGuard: 'On you go then!'")
            castle1(cname, level, reputation, age)
        else:
            print(f"\n{cname}: Step aside you detestable inferior, I am a man of great importance.")
            time.sleep(2)
            print("\nYou have been taunted by the guard, he warns you:")
            time.sleep(1)
            print("'Leave now or I shall taunt you a second time.'")
            time.sleep(2)
            print("\nFilled with embarassment, you now leave.")
            loc.navigate(cname, level, reputation, age)
    if castq == '2':
        time.sleep(2)
        print("\nI am here to seek civilization.")
        if cl <= 3:
            print(f"Guard: Hah you are but a {level}! Leave at once!\n")
            loc.navigate(cname, level, reputation)
        else:
            time.sleep(2)
            print("\nOn you go then...")
            castle1(cname, level, reputation, age)


