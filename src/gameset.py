#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2019
gameset.py
@author: Max McDevitt
"""

import getpass as gp
import os
from passlib.hash import pbkdf2_sha256
import sqlite3 as lite
from functools import wraps
from time import sleep
from operator import itemgetter

cwd = os.getcwd()

DATABASE_PATH = os.path.join(cwd, "storage")
FILE = DATABASE_PATH+"/users.sqlite3"

def itr(script, s=None, e=None):
    """
    Iterates an iterable given the parameters s (start) and
    e (end).
    """

    if s and e:
        for i in script[s:e]:
#            sleep(3)
            print('\n'+i)
    if s and not e:
        for i in script[s:]:
#            sleep(3)
            print('\n'+i)
    if e and not s:
        for i in script[:e]:
 #           sleep(3)
            print('\n'+i)


def add_user():
    """ Add a user """
    while True:
        username = input("Username: ")
        if username == None or username == " ":
            print("Username can not be empty.\n")

        pass_ = gp.getpass("password: ")
        if pass_== None or pass_ == " ":
            print("Password can not be empty.\n")
        else:
            password = pbkdf2_sha256.hash(pass_)
            password = password.encode('utf-8')
            del pass_
            break
        raise SystemExit

    return username, password

def load_variables(*args):
    options = {"level":0, "age":1, "cname":2, "reputation":3, "cl":4, "username":5, "password":6}
    con = None
    con = lite.connect(FILE)
    x = len(args)
    indices = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM data")
        a = 0
        data = cur.fetchone()
    for i in args:
        if i in options.keys():
            val = options.get(i)
            index = itemgetter(val)(data) if (a<x) else None
            if index == None:
                break
            indices.append(index)
            a+=1
    return indices

def authenticate(f):
    """ compares the given username and password to the ne stored previously  """
    @wraps(f)
    def decoration(*args, **kwargs):
        l = load_variables("username", "password")
        usname, _pass = l[0], l[1]
        username, password = f()
        if pbkdf2_sha256.verify(password, _pass) is False:
            print("Invalid passwprd.")
            raise SystemExit

        while True:
            if username != usname:
                print("Invalid Username or password.")
                raise SystemExit
            else:
                break
    return decoration

@authenticate
def login():
    username = input("Username: ")
    password = gp.getpass("password: ")
    return username, password

def save(level, age, cname, reputation, cl, username=None, password=None):
    """ Saves the attributes and given data into the sql file. """
    con = lite.connect(FILE)
    with con:
        cur = con.cursor()
        cur.execute('drop table if exists data')
        cur.execute('create table data (level TEXT , age INT , cname TEXT , reputation INT , cl INT , username TEXT, password INT)')
        if username and password:
            data = (level, age, cname, reputation, cl, username, password)
            cur.executemany('INSERT INTO data VALUES (?,?,?,?,?,?,?)', (data, ))
            cur.executemany('UPDATE data SET level=?,age=?,cname=?,reputation=?,cl=?,username=?,password=?', (data, ))
        elif username is None and password is None:
            data = (level, age, cname, reputation, cl)
            cur.executemany('INSERT INTO data VALUES (?,?,?,?,?,)', (data, ))
#            cur.executemany('UPDATE data SET level=?, age=?, cname=?, reputation=?, cl=? ', (data, ))

def initialize_new_game():
    """ Starts a fresh game """
    if not os.path.isdir(DATABASE_PATH):
        os.mkdir('storage')

    username, password = add_user()
    level = ""
    reputation = 0
    cname = input("What will your character's name be?\n: ")
    age = input("What will your character's age be?\n: ")
    cl=0
    save(level, age, cname, reputation, cl, username=username, password=password)

    return cname, age, username, password

class Levels(object):
    def __init__(self, cname, age, username, password):
        self.cname, self.age, self.username, self.password = cname, age, username, password
        self.attributes = {
            "dunce" : ["The Dunce...drool and fart?"],
            "jester" : ["The Jester can juggle and do a backflip, nothing particularly helpful though.."],
            "serf" : ["The Serf can raise his pitfork angrily." ],
            "merchant" : ["The Merchant can utilize his secret inventory."],
            "knight" : ["The knight can use his sword and training to be an effective fighter"],
            "blackknight" : ["The Black Knight can use his mastery to defeat even the most fearsome aggresors."],
            "master" : ["He can command his army to do whatever he wants."],
            "wizard" : ["The wizard can cast spells and use magic."],
            "prince" : ["The prince is able to almost anything."],
            "king" : ["The knight is able to do anything."],
            }

        self.lvl = {
                1:{2:'dunce',3: -100},
                2:{2:'jester',3: -70},
                3:{2:'serf', 3:-45},
                4:{2:'merchant', 3:-10},
                5:{2:'knight' ,3:0},
                6:{2:'blackknight',3:10},
                7:{2:'master', 3:30},
                8:{2:'wizard', 3:50},
                9:{2:'prince', 3:75},
                10:{2:'king', 3:100},
                }

    def level_up(self):
        """  Uses a nested dictionary to "level up".
        Takes the two parameters cname and age because it needs to save() after.
        """

        sleep(1)
        for i in range(80):
            i+=1
            print("*"*120)
            sleep(.02)
        _=os.system("clear")

        buf =load_variables("cl")
        cl = buf[-1]
        cl=int(cl)     # cl means current level
        cl+=1

        level=self.lvl[cl][2] # Set level = to the appropritate level
        reputation=self.lvl[cl][3]   # same as above but for reputation.
        print(f"\nCongrats, {self.cname}, you have leveled up, you are now a {level}!\n")


        save(level, self.age, self.cname, reputation, cl, self.username, self.password)

        return cl, level, reputation
