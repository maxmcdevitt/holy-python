#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019

@author: Max McDevitt
"""
import os, json

global cwd
cwd = os.getcwd()


import json, os
from time import sleep

def _init():
    """ Starts a fresh game """
    try:
        open(cwd+'/storage/charactername.json')
    except FileNotFoundError:
        os.mkdir('storage')

    cname = input("What will your character's name be?: ")

    with open(cwd+'storage/charactername.json', 'w') as db:
        json.dump(cname, db)

    age = input("What will your character's age be?\n::")

    with open(cwd+'storage/age.json','w') as f:
        json.dump(age,f)

    with open(cwd+'storage/cl.json','w') as f:
        cl=0
        json.dump(cl,f)

    return age,cname


def load_game():
    with open('/home/i3/python/medieval_game/src/level.json') as f:
        level = f.read()
        f.close()
    with open("/home/i3/python/medieval_game/src/age.json") as f:
        age = f.read()
        f.close()
    with open('/home/i3/python/medieval_game/src/reputation.json') as f:
        reputation = f.read()
        f.close()
    with open('/home/i3/python/medieval_game/src/charactername.json') as f:
        cname = f.read()
        f.close()
    with open("/home/i3/python/medieval_game/src/reputation.json") as f:
        reputation = f.read()
        f.close()

    return level, age, cname, reputation


def save(level, age, cname, reputation):
    with open('/home/i3/python/medieval_game/src/level.json','w') as f:
        json.dump(level, f)
    with open('/home/i3/python/medieval_game/src/age.json','w') as f:
        f.write(age)
        f.close()
    with open('/home/i3/python/medieval_game/src/charactername.json','w') as f:
        f.write(cname)
        f.close()
    with open('/home/i3/python/medieval_game/src/reputation.json','w') as f:
        json.dump(reputation, f)


def dunce():
    print("\nThe Dunce is a dirty and smelly creature of the land,"+
          " abnormally so compared to the common serf. Since the Dunce"+
          " has a reputation of -75 he is not well"+
          " liked.")
    q = input(f"\nDo you want to see the Dunce's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print("The Dunce...drool and fart?")


def jester():
    print("The Jester has lingered around since the carnival left him. "+
            "He is a trveling comedic performer who earns a wage by"+
            " making a fool out of himself.")
    q = input("\nDo you want to see the Jester's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        power="The Jester can juggle and do a backflip, nothing"
        power+=" particularly helpful though..."
        print(power)

def serf():
    print("\nThe serf is just the common peasant here in the medieval land.")
    time.sleep(2)
    print("\nThe serf owns a a small crop farm to pay taxes.")
    q = input("\nDo you want to see the Serf's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print("\nThe Serf can raise his pitfork angrily.")


def merchant():
    print("\nThe Merchant trades his items and is reasonbly wealthy.")
    q = input("\nDo you want to see the Merchant's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print("The Merchant can utilize his secret inventory.")


def knight():
    print("\nThe knight is the standary military grunt.")
    q = input("\nDo you want to see the Knight's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        power="\nThe knight can use his sword and training to be an "
        power+="effective fighter."
        print(power)


def blackknight():
    print("\nThe Black Knight is like the knight... except black."+
          " He is a master of combat and is well respected by his "+
          "peers.")
    q = input("\nDo you want to see the Black Knight's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        power="\nThe Black Knight can use his mastery to defeat even the "
        power+="most fearsome aggresors."
        print(power)

def grandmaster():
    print("\nThe Grandmaster is the head of the military order of knighthood." +
    "He is at the highest level of military achievement.")
    q = input("\nDo you want to see the Grand Master's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print("\The Grand Master can command his army of knights.")


def duke():
    print("\nThe Duke is a high ranking official in the nobility. He is" +
          " granted the title of soveirgn leader over his area of choice.")

    power="\nThe Duke commands the local military and has "
    power+="ordinance over his area."
    q = input("\nDo you want to see the Duke's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print(power)


def pope():
    print("\nThe pope is the leader of the clergy.")
    power="\nThe Pope holds power over the church and can influence diplomacy"
    power+=" and society."
    q = input("\nDo you want to see the Pope's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print(power)


def king():
    print("\nThe kind is the omnipotent and revered ruler of all the land.")
    power ="\nThe king can do anything."
    q = input("\nDo you want to see the King's powers?\n[yes/no]: ")
    if q == "yes" or q == 'y':
        print(power)

def level_up(level, reputation, age, cname):
    print(f"Congrats, {cname}, you have leveled up!\n")
    print("*"*80)
    file1="/home/i3/python/medieval_game/src/cl.json"

    lvl = {
            1:{1:dunce, 2:'dunce',3: -100},
            2:{1:jester, 2:'jester',3: -70},
            3:{1:serf, 2:'serf', 3:-45},
            4:{1:merchant, 2:'merchant', 3:-10},
            5:{1:knight, 2:'knight' ,3:0},
            6:{1:blackknight, 2:'blackknight',3:10},
            7:{1:grandmaster, 2:'grandmaster', 3:30},
            8:{1:duke, 2:'duke', 3:50},
            9:{1:pope, 2:'pope', 3:75},
            10:{1:king, 2:'king', 3:100},
            }

    while True:
        try:
            with open (file1) as f:
                cl = f.read()
                f.close()
        except FileNotFoundError:
            cl=0

        cl=int(cl)     # cl means current level
        cl+=1
        lvl.get(cl)[1]() # Call the appropriate function
        level=lvl[cl][2] # Set level = to the appropritate level
        reputation=lvl[cl][3]   # same as above but for reputation.
        with open(file1, 'w') as f:
            json.dump(cl, f)
        save(level, age, cname, reputation)
        break
    return level, reputation
