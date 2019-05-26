def ws(cname):
    woods_script = [
            """You are following the path, it's eerie, quiet and
mysterious. Upon further investigation you come upon a
fork in the path, do you go left or right?""",   #0
            "You went left...",                                         #1
            "It becomes darker...",                                     #2
            "There is a dragon in the path!",                           #3
            "You have been killed by the dragon",                       #4
            "You slay the dragon!",                                     #5
            """Further along you see a treacherous bridge, as you begin
walking closer you see an old man in dark clothes. """,         #6
            "Stop. Who would cross this bridge must answer these three questions, " #7
            "ere the other side he see.",                               #8
            "What is your name?\n: ",#9
            "What is your favorite color?\n: ",#10
            "What is the air-speed velocity of an unladen swallow?\n: ",#11
            "Oh no the gatekeeper accidentally threw himself off the bridge",#12
            "You went right, it is dark and foggy.",#13
            "As you walk down the path you think you hear scurried movement near you",#14
            "You look up and suddenly see tall people draped in dark ragged clothing!",#15
            "One of them says, 'We are the knights of ni, ping, and nee-wom.",  #16
            "In order to pass we require a...'",#17
            "SHRUBBERY!",#18
            "Your task is to now find a shrubbery, where do you look?",# 19
            "You have three options\nthe cave, \nthe shrubber, \nor the forest",#20
            "[cave, shrubber, or forest]",#21
            "You enter the cave...",#22
            "There is nothing but rocks. (Suprise)",#23
            """You see writing etched in the wall, it reads
            'Here may be found the last words of Joseph of
Arathamia. He who is valiant and pure of spirit may find
the holy grail in the castle of Aaauuuggghhh...'""", #24
            "The monster appears and kills you",#25
            "You go to the town shrubber.",#26
            f"{cname}: 'Old crone!  Is there anywhere in this town where we could buy a shrubbery?'",#27
            "Shrubber: 'Who sent you?'",#28
            f"{cname} : 'The Knights Who Say Nee.",#29
            "Shrubber: 'Agh!  No!  Never!  We have no shrubberies here.'",#30
            f"{cname}: 'If you do not tell us where we can buy a shrubbery, my friend and I will say... we will say... `nee'.'",#31
            "Shrubber: Agh!  Do your worst!",#32
            f"{cname}:  Very well!  If you will not assist us voluntarily,... nee!'",#33
            "Shrubber: That's it, that's it, you've got it.",#34
            "You return to the knights of Ni and give them the shrubbery.",#35
            "Knights of Ni: 'Thank you for the shrubbery...'",#36
            f"{cname}: 'Can I pass?'",#37
            "Knights of Ni: To pass we need a...",#38
            "You kill the Knights of Ni.",#39
            "You search around the forest.",#40
            "You search the forest.",#41
            "You walk along the path.",#42
            "Ow! You tripped and fell down a large hole.",#43
            "It was a rabbit hole.",#44
            "This isn't very good....",#45
            "You travel further in the woods and come across a small village.",#46
            "The people there seem primal and hostile.",#47
            "What do you do? [Stay or travel on])",#48
            ": ",#49
            "What do you want to do with the people? [talk or kill]", # Stay  50
            ": ",# 51
            "You talk to the strangers, they act very nice and welcoming...", #talk  52
            "You go into one of the tents and see a dead body...",# 53
            "The strangers kill you :(",# 54
            "They gave a good fight, but you have succesfully killed the strangers.", #kill 55
            ]
    return woods_script

def cs(cname):
    cave_script = [
            "You choose to go to the cave.",
            " To you suprise there is an old man with funny clothes near the cave",
            f"{cname}: Who are you?",
            "There are some who call me…",
            "Tim.",
            "Greetings, Tim, the enchanter.",
            f"Greetings, {cname}",
            f"{cname} How do you know my name?",
            "Tim: I know many things...",
            f"{cname}: What are you doing here?", # 10
            "Tim: To protect a sacrosanct artifact.",
            """Tim: To the north there lies a cave, the cave of Caerbannog, where
in carved in mystic runes upon the very living rock, the last
words of Olfin Bedwee of Rheged.""",
            f"{cname}: Take us there!",
            """Tim: Follow. But follow only if you be men of valor, for the
entrance to this cave is guarded by a creature so foul, so cruel
that no man yet has fought with it and lived! Bones of full 50
men lie strewn about its lair, so brave knights, if you do doubt
your courage or your strength, come no further! For death
awaits you all with nasty big pointy teeth.""",
            "Do you travel to the cave?", # 15
            "You travel to the cave...",
            "Tim: There he is!",
            f"{cname}: Where ?",
            "Tim: There!",
            f"{cname}: What, behind the rabbit?", # 20
            "Tim: It is the rabbit.",
            f"{cname}: You silly sod. You got us all worked up !",
            """Tim: That’s no ordinary rabbit. That’s the most foul, cruel, and bad
tempered rodent you ever set eyes on.""",
            """Tim: Listen, that rabbit’s got a viscious streak a mile wide, he’s a
killer.""",
            f"{cname}: Oh, yeah?",
            "Tim: I’m warning you!",
            f"{cname}: Right. Silly little bleeder, one rabbit stew coming right up",
            """Tim: Wait! If you insist on fighting the rabit you must use the
holy hand grenade.""",
            f"""{cname}: Yes, of course! The Holy Hand Grenade of Antioch! 'Tis one of the
sacred relics Brother Maynard carries with him. Brother Maynard!
Bring up the Holy Hand Grenade!""",
            f"{cname}: How does it work?", # 30
            "Maynard: I know not sir.",
            f"{cname}: Consult the book of Arnaments!",
            """Maynard: Armaments, chapter two, verses nine to twenty-one:
And the Lord spake, saying, First shalt thou take out the Holy
Pin. Then, shalt thou count to three. No more. No less.""",
            """Three shalt
be the number thou shalt count, and the number of the counting
shall be three.""",
            """Four shalt thou not count, nor either count thou
two, excepting that thou then proceed to three.""",
            """Five is right out.
Once the number three, being the third number, be reached, then,
lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who,
being naughty in My sight, shall snuff it.""",
            "All: Amen",
            f"{cname}: Right!\nOne!... Two!... Five!", # 38
            "You have succesfully defeated the rabbit of Caerbannog!", # 39
            "You forgot to let go of the grenade :(",

            "Tim: For years there have been rumors of treasure.", # 41
            "What kind of treasure? (1)\n Why don't you go then? (2)",

            ###### 1 ########
            "Tim: Treasure of a wizard who once wandered the cave.", # 43
            f"{cname}: Huh guess I'll check it out.",
            ######## 2 ########
            "Tim: I have traveled far enough, whatever you do henceforth, is up to you.", # 45
            #########################

            "You enter the cave...",
            "There is a split in the path.",
            "Which one do you take?\n left path (1)\nor right path (2)", # 48
                    #### first path #####
            "You follow one down a deep and dark crevice.", # 49
            "It is very narrow and hard to get through",
            "You search for hours but do not find anything in the cave.",
            "You hear something behind you...",
            "It's the legendary Black Beast of aaauuugh!",
            f"""As the horrendous Black Beast lunged forward, escape
for {cname} seemed hopeless.  When, suddenly, the
programmer suffered a fatal heart attack.""",
            "The textual peril was no more.  The Quest could continue.", # 55
            ######################################

                ##### 2nd path #########

            "You travel down the second path...",
            "You come across an abandoned camp.",
            "You see a skeleton of what you beleive was the wizard.",
            "You check out the camp",
            "There is a box with a lock on it", # 60
            "Congrats! The box opens and there is a wand inside!",
            "That was wrong, the lock starts to move and the rabbit reappears from the dead.",
            "You have died :(",
           ]
    return cave_script


def csts(cname, level):
    castle_script = [
            "You knock on the large wooden door.",      # 0
            "Guard: Who goes there?",                   # 1
            f"{cname}: It is I, {cname}.",              # 2
            "Guard: What is your buisness here?",       # 3
            "Do you\n1[lie]\nor\n2['tell truth']",      # 4
            f"{cname}: ...well",                        # 5
            f"{cname}: ..umm..",                        # 6
            f"\n{cname}: Let's just say I am very important.", #7
            "Guard: 'On you go then!'",                         # 8
            f"\n{cname}: Step aside you detestable inferior, I am a man of great importance.", # 9
            "You have been taunted by the guard, he warns you:", # 10
            "Leave now or I shall taunt you a second time.'", # 11
            "Filled with embarassment, you now leave.", # 12
            "I am here in seek of civilization.", # 13
            f"Guard: Hah you are but a {level}! Leave at once!", # 14
            "On you go then...",
            "You enter the castle. It is enormous and full of people.",
            "There are many guards here.",
            "What do you wish to do now?",
            "1 [killing spree]2 [settle in with the people]",   # 19
            "You take out you sword and stab and slash everyone in sight.",
            "A fleet of guards arrive...",
            "The guards have killed you...",
            "You have killed the guards!",
            "And everyone else...",
            "There is nothing but a pile of dead bodies now...",
            "You choose to settle in one of the local camp",
            "You see a armed knight in your path...",
            f"{cname}: You fight with the strength of many men, Sir Knight.",
            "Knight: No response",
            f"{cname}: I am {cname}.",   # 30
            "Knight: No response.",
            f"{cname}: You have proved yourself worthy, Sir Knight. Tries to pass",
            "Knight: None shall poss.",
            f"{cname}: What?",
            "None shall pass!",
            f"{cname}: I have no quarrel with you, good Sir Knight, but I shall pass.",
            "Knight: Then you shall die!", # 37
            "The Knight has killed you...",
            "You have cut off the Knight's right arm.",
            f"{cname}: Now stand aside worthy adversary!", # 40
            "Knight: Tis' but a scratch!",
            f"A scratch? You arm's off!",
            f"knight: I've had worse...",
            "Come on you pansy",
            "You effectively dismember the rest of the knights limbs...",
            ]
    return castle_script

def tscript(cname, level):
        tscript = [
            "You come across a lively town!",
            "You are not sure what to do...",
            "You see a peasant working in a field",
            f"{cname}: Old woman.",
            "Man",
            f"{cname}: Man, sorry. What knight lives in that castle over there?",
            "I'm 37.",
            f"{cname}: What?",
            "I'm 37. I'm not old.",
            f"{cname}: Well I can't just call you 'man'.",
            "Well you could say 'Dennis'.",
            f"{cname}: I didn't know you werre called Dennis.",
            "Dennis: Well you didn't bother to find out did you?",
            "Do you fight the old man (1)or leave (2)", # 13
            "After a drawn out dialogue you search around the town some more.",
            "You kill the old man\n the people in the town did not approve and have exiled you.",
            "You see a crowd of people and approach them to see what they are looking at",
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
            "VILLAGER #1:  More witches!\nVILLAGER #2:  Wood!",
            "BEDEMIR:  So, why do witches burn?",
            "[pause]",
            "VILLAGER #3:  B--... \'cause they're made of wood...?",
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
            "A duck (1)\nsuasage (2) \n or frogs (3)\n: ",
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
            "Good Sir knight, will you come with me to Camelot, and join us at the Round Table?",
            "BEDEMIR:  My liege!  I would be honored.",
            f"{cname}:  What is your name?,",
            "BEDEMIR:  Bedemir, my leige.",
            f"{cname}: Then I dub you Sir Bedemir, Knight of the Round Table.",
            "You and Sir Bedimir continue on."
            ]
        return tscript

def unknown():
    sript = [
        "You travel to the unknown...",
        "There is a thick fog and shallow water",
        "You cannot see into the murky water",
        "You step along as a snake slithers by",
        "Trudging through the murky waters you find an abandoned crate.",
        "You look inside and there is a note that says,",
        "''",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    return script