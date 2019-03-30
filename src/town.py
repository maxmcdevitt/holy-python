"""
town
"""
import loc as l
import gameset as gs
import time


def town(cname, level, reputation, age):
    script = [
            "You come across a lively town!"
            "You are not sure what to do...",
            "You see a peasant working in a field",
            "{cname}: Old woman.",
            "Man",
            "{cname}: Man, sorry. What knight lives in that castle over there?",
            "I'm 37.",
            "{cname}: What?",
            "I'm 37. I'm not old.",
            f"{cname}: Well I can't just call you 'man'.",
            "Well you could say 'Dennis'.",
            f"{cname}: I didn't know you werre called Dennis.",
            "Dennis: Well you didn't bother to find out did you?",
            "After a drawn out dialogue you search around the town some more.",
            "You see a crowd of people and approach them to see what they are looking at",
            "You hear them yell",
            "CROWD:  A witch!  A witch!  A witch!  We've got a witch!  A witch!",
            "VILLAGER #1:  We have found a witch, might we burn her?",
            "CROWD:  Burn her!  Burn!",
            "BEDEMIR:  How do you know she is a witch?",
            "VILLAGER #2:  She looks like one.",
            "BEDEMIR:  Bring her forward.",
            "WITCH:  I'm not a witch.  I'm not a witch.",
            "BEDEMIR:  But you are dressed as one.",
            "WITCH:  They dressed me up like this.",
            "CROWD:  No, we didn't... no.",
            "WITCH:  And this isn't my nose, it's a false one.",
            "BEDEMIR:  Well?",
            "VILLAGER #1:  Well, we did do the nose.",
            "BEDEMIR:  The nose?",
            "VILLAGER #1:  And the hat -- but she is a witch!",
            "CROWD:  Burn her!  Witch!  Witch!  Burn her!",
            "BEDEMIR:  Did you dress her up like this?",
            "CROWD:  No, no... no ... yes.  Yes, yes, a bit, a bit.",
            "VILLAGER #1:  She has got a wart.",
            "BEDEMIR:  What makes you think she is a witch?",
            "VILLAGER #3:  Well, she turned me into a newt.",
            "BEDEMIR:  A newt?",
            "VILLAGER #3:  I got better",
            "BEDEMIR:  Quiet, quiet.  Quiet!  There are ways of telling whether she is a witch.",
            "CROWD:  Are there?  What are they?",
            "BEDEMIR:  Tell me, what do you do with witches?",
            "VILLAGER #2:  Burn!",
            "BEDEMIR:  And what do you burn apart from witches?",
            "VILLAGER #1:  More witches!"+" \nVILLAGER #2:  Wood!",
            "BEDEMIR:  So, why do witches burn?",
            "[pause]",
            "VILLAGER #3:  B--... 'cause they're made of wood...?",
            "BEDEMIR:  Good!",
            "BEDEMIR:  So, how do we tell whether she is made of wood?",
            "VILLAGER #1:  Build a bridge out of her.",
            "BEDEMIR:  Aah, but can you not also build bridges out of stone?"+
            "\nVILLAGER #2:  Oh, yeah.",
            "BEDEMIR:  Does wood sink in water?",
            "VILLAGER #2:  It floats!  It floats!",
            "VILLAGER #1:  Throw her into the pond!",
            "BEDEMIR:  What also floats in water?",
            "Bread!\nApples!\nVery small rocks!\nCider!\nMud!\nChurches --"+
            "churches!\nLead -- lead!",
            f"{cname}: A duck.",
            "CROWD:  Oooh.",
            "BEDEMIR:  Exactly!  So, logically...,",
            "VILLAGER #1:  If... she.. weighs the same as a duck, she's made of wood",
            "BEDEMIR:  And therefore--?",
            "VILLAGER #1:  A witch!",
            "CROWD:  A witch!",
            "BEDEMIR:  We shall use my larger scales!",
            "BEDEMIR:  Who are you who are so wise in the ways of science?",
            f"{cname}: I am {cname}, {level}.",
            "Good Sir knight, will you come with me to Camelo, and join us at the Round Table?",
            "BEDEMIR:  My liege!  I would be honored.",
            f"{cname}:  What is your name?,"
            "BEDEMIR:  Bedemir, my leige.",
            f"{cname}: Then I dub you Sir Bedemir, Knight of the Round Table.",
            "You and Sir Bedimir continue on."
            ]
    for i in script:
        x = 0
        x += 1
        time.sleep(2.5)
        print('\n',i)
        if x == 2:
            raise StopIteration
    gs.level_up(level, reputation, age, cname)

    l.navigate(cname, level, reputation, age)
