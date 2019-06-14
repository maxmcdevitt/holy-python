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

def unknown(cname):
    uscript = [
            "You choose to travel to the unknown...", #  0
            "There is a thick fog and shallow water", #  1
            "You cannot see into the murky water", #  2
            "You step along as a snake slithers by", #  3
            "whooooosh", #  4
            "fwump", #  5
            "An arrow comes flying from nowhere and plants itself firmly in your shoe", #  6
            """It reads:
            Concorde! Concorde, speak to me! To whoever finds this
note, I have been imprisoned by my father, who wishes me to marry against my will.
Please, please, please come and rescue me. I am in the tall tower of Swamp Castle.""", #  7
            "You rush to the tower and hastily kill everyone in standing in your way", #  8
            "You go to the tower to find the prisoner", #  9
            "Father:  One day, lad, all this will be yours!", #  10
            "Herbert:  What, the curtains?", #  11
            """Father:  No, not the curtains, lad.  All that you can see!  Stretched
out over the hills and valleys of this land!  This'll be your kingdom,
lad!""", #  12
            "Herbert:  But, Mother--", #  13
            "Father:  Father, I'm Father.", #  14
            "Herbert:  But Father, I don't want any of that.", #  15
            """Father:  Listen, lad.  I've built this kingdom up from nothing.  When
I started here, all there was was swamp.  All the kings said I was
daft to build a castle in a swamp, but I built it all the same,
just to show 'em.""", #  16
            """It sank into the swamp.  So, I built a second one.
That sank into the swamp.  So I built a third one.  That burned down,
fell over, then sank into the swamp.  But the fourth one stayed up.
An' that's what your gonna get, lad -- the strongest castle in these
islands.""", #  17
            "Herbert:  But I don't want any of that -- I'd rather--", #  18
            "Father:  Rather what?!", #  19
            """Herbert:  I'd rather... just...
\n[music]
\n...sing!""", #  20
            """Father:  Stop that, stop that!  You're not going to do a song while
I'm here.  Now listen lad, in twenty minutes you're getting married to
a girl whose father owns the biggest tracts of open land in Britain.""", #  21
            "Herbert:  But I don't want land.", #  22
            "Father:  Listen, Alex,--", #  23
            "Herbert:  Herbert.", #  24
            "Father:  Herbert.  We live in a bloody swamp.  We need all the land we can get.", #  25
            "Herbert:  But I don't like her", #  26
            """Father:  Don't like her?!  What's wrong with her?  She's beautiful,
she's rich, she's got huge... tracts of land.""", #  27
            """Herbert:  I know, but I want the girl that I marry to have...
\na certain...
\nspecial...
\n[music]
\n...something...""", #  28
            """Father:  Cut that out, cut that out.  Look, you're marryin' Princess
Lucky, so you'd better get used to the idea. [smack]  Guards!  Make sure
the Prince doesn't leave this room until I come and get 'im.""", #  29
            "Guard #1:  Not to leave the room even if you come and get him.", #  30
            "Guard #2:  Hic!", #  31
            "Father:  No, no.  Until I come and get 'im.", #  32
            "Guard #1:  Until you come and get him, we're not to enter the room.", #  33
            "Father:  No, no, no.  You stay in the room and make sure 'e doesn't leave.", #  34
            "Guard #1:  And you'll come and get him.", #  35
            "Guard #2:  Hic!", #  36
            "Father:  Right.", #  37
            "Guard #1:  We don't need to do anything, apart from just stop him entering the room.", #  38
            "Father:  No, no.  Leaving the room.", #  39
            "Guard #1:  Leaving the room, yes.", #  40
            "Father:  All right?", #  41
            "Guard #1:  Right.  Oh, if-if-if, uh, if-if-if, uh, if-if-if we...", #  42
            "Father:  Yes, what is it?", #  43
            "Guard #1:  Oh, if-if, oh--", #  44
            "Father:  Look, it's quite simple.", #  45
            "Guard #1:  Uh...", #  46
            "Father:  You just stay here, and make sure 'e doesn't leave the room. All right?", #  47
            "Guard #2:  Hic!", #  48
            "Father:  Right.", #  49
            "Guard #1:  Oh, I remember.  Uh, can he leave the room with us?", #  50
            "Father:  N- No no no.  You just keep him in here, and make sure--", #  51
            "Guard #1:  Oh, yes, we'll keep him in here, obviously.  But if he had to leave and we were--", #  52
            "Father:  No, no, just keep him in here--", #  53
            "Guard #1:  Until you, or anyone else,--", #  54
            "Father:  No, not anyone else, just me--", #  55
            "Guard #1:  Just you.", #  56
            "Guard #2:  Hic!", #  57
            "Father:  Get back.", #  58
            "Guard #1:  Get back.", #  59
            "Father:  Right?", #  60
            "Guard #1:  Right, we'll stay here until you get back.", #  61
            "Father:  And, uh, make sure he doesn't leave.", #  62
            "Guard #1:  What?", #  63
            "Father:  Make sure 'e doesn't leave.", #  64
            "Guard #1:  The Prince?", #  65
            "Father:  Yes, make sure 'e doesn't leave.", #  66
            """Guard #1:  Oh, yes, of course.  I thought you meant him.  Y'know, it
seemed a bit daft, me havin' to guard him when he's a guard.""", #  67
            "Father:  Is that clear?", #  68
            "Guard #2:  Hic!", #  69
            "Guard #1:  Oh, quite clear, no problems.", #  70
            "Father:  Right.\n[starts to leave]\nWhere are you going?", #  71
            "Guard #1:  We're coming with you.", #  72
            "Father:  No no, I want you to stay 'ere and make sure 'e doesn't leave.", #  73
            "Guard #1:  Oh, I see.  Right.", #  74
            "Herbert:  But, Father!", #  75
            "Father:  Shut your noise, you!  And get that suit on!  And no singing!", #  76
            "Guard #2:  Hic!", #  77
            "Father:  Oh, go get a glass of water.", #  78
            f"""{cname}: O fair one, behold your humble servant Sir x.
I have come to take""", #  79
            "(You see that it is actually a boy)", #  80
            "-- oh, I’m terribly sorry.", #  81
            "Herbert: You got my note!", #  82
            f"{cname}: Uh, well, I got A note.", #  83
            "Herbert: :You’ve come to rescue me!", #  84
            f"{cname}: Uh, well, no, you see...", #  85
            "Herbert: I knew that someone would, I knew that somewhere out there...", #  86
            "there must be...\n[music]", #  87
            "...someone...", #  88
            "Father: Stop that, stop that, stop it! Stop it! Who are you?", #  89
            "Herbert: I’m your son!", #  90
            "Father: No, not you.", #  91
            f"{cname}: I’m Sir x, Sir", #  92
            "Herbert: He’s come to rescue me, father.", #  93
            f"{cname}: Well, let’s not jump to conclusions", #  94
            "Father: Did you kill all the guards?", #  95
            f"{cname}: Uh..., oh, yes. Sorry.", #  96
            "Father: They cost fifty pounds each.", #  97
            f"{cname}: Well, I’m awfully sorry, I’m -- I really can explain everything.", #  98
            "Herbert: Don’t be afraid of him, Sir x, I’ve got a rope all ready!", #  99
            "Father: You killed eight wedding guests in all!", #  100
            f"{cname}: Well, you see, the thing is, I thought your son was a lady.", #  101
            "Father: I can understand that.", #  102
            "Herbert: Hurry, Sir x! Hurry!", #  103
            "Father: Shut up! You only killed the bride’s father, that’s all!", #  104
            f"{cname}: Well, I really didn’t mean to...", #  105
            "Father: Didn’t mean to? You put your sword right through his head!", #  106
            f"{cname}: Oh, dear. Is he all right?", #  107
            "Father: You even kicked the bride in the chest! This is going to cost me a fortune!", #  108
            f"""{cname}: Well, I can explain. I was in the forest, um, riding north from Castle
when I got this note you see--""", #  109
            "Father:  Pretty nice castle.  Uh, pretty good pig country....", #  110
            f"{cname}:  Yes.", #  111
            "Herbert:  Hurry, I'm ready!", #  112
            "Father:  Would you, uh, like to come and have a drink?", #  113
            f"{cname}:  Well, that's, uh, awfully nice of you.", #  114
            "Herbert:  I am ready!\n[starts to leave]", #  115
            f"{cname}:  --I mean to be, so understanding.\n[thonk]", #  116
            "Herbert:  Oooh!", #  117
            f"""{cname}:  Um, I think when I'm in this  idiom, I sometimes get a bit,
            uh, sort of carried away.""", #  118
            "Father:  Oh, don't worry about that.", #  119
            "Herbert:  Oooh!\n[splat]", #  120
            """Father:  Well, this is the main hall.  We're going to have all this
knocked through, and made into one big, uh, living room.""", #  121
            "Random:  There he is!", #  122
            "Father:  Oh, bloody hell.", #  123
            f"{cname}:  Ha-ha! etc.", #  124
            "Father:  Hold it, hold it!  Please!", #  125
            f"""{cname}:  Sorry, sorry.  See what I mean, I just get carried away.I really must -- sorry, sorry!  Sorry, everyone.""", #  126
            "Random:  He's killed the best man!", #  127
            """Father:  Hold it, please!  Hold it!  This is Sir Launcelot from the
court of Camelot -- a very brave and influential knight, and my special
guest here today.""", #  128
            f"{cname}:  Hello.", #  129
            "Random:  He killed my auntie!\n[yelling]", #  130
            """Father:  Please, please!  This is supposed to be a happy occasion!
Let's not bicker and argue about who killed who.  We are here today to
witness the union of two young people in the joyful bond of the holy
wedlock.  Unfortunately, one of them, my son Herbert, has just fallen
to his death.  But I think I've not lost a son, so much as... gained
a daughter!  For, since the tragic death of her father--""", #  131
            "Random:  He's not quite dead!", #  132
            "Father:  Since the near fatal wounding of her father--", #  133
            "Random:  He's getting better!", #  134
            """Father:  For, since her own father... who, when he seemed about to
recover, suddenly felt the icy hand of death upon him,...\n[ugh]""", #  135
            "Random:  Oh, he's died!", #  136
            f"""Father:  And I want his only daughter to look upon me... as her own
dad -- in a very real, and legally binding sense.
\n[clapping]
\nAnd I feel sure that the merger -- uh, the union -- between the
Princess and the brave, but dangerous, Sir {cname} of Camelot...""", #  137
            f"{cname}:  What?", #  138
            "Random:  Look!  The dead Prince!", #  139
            "Concorde:  He's not quite dead!", #  140
            "Herbert:  Oh, I feel much better.", #  141
            "Father:  You fell out of the tower, you creep!", #  142
            "Herbert:  No, I was saved at the last minute.", #  143
            "Father:  How?!", #  144
            "Herbert:  Well, I'll tell you...\n[music]", #  145
            "Father:  Not like that!  Not like that!  No, stop it!", #  146
            "Singing:  He's going to tell!  He's going to tell!", #  147
            "Father:  Shut up!", #  148
            """Singing:  He's going to tell!  He's going to tell!
He's going to tell!  He's going to tell!
He's going to tell!  He's going to tell!
He's going to tell!  He's going to tell!
            "Concorde:  Quickly, sir!  This way!""", #  149
            f"{cname}:  No, it's not in my idiom!  I must escape more....(sigh)", #  150
            "Concorde:  Dramatically, sir?", #  151
            f"{cname}:  Dramatically!  Hee!",
   ]

    return uscript

def camelot(cname, level):
    script = [
        "[wind]",
        "[clop clop]",
        "...",
        "[clop clop]",
        f"{cname}: Whoa there!",
        "Guard:  Halt!  Who goes there?",
        f"{cname}: It is I, {level}, {cname}!",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        "Guard: ",
        f"{cname}: ",
        f"{cname}: ",
        f"{cname}: ",
        f"{cname}: ",
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
        f"{cname}: ",