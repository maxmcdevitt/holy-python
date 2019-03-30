"""                         cave                    """
import sys
import time
import gameset as gs
import loc as l

def runcave(cname, level, reputation, age):
    script = [
            "You choose to go to the cave."
            " To you suprise there is an old man with funny clothes near the cave",
            f"{cname}: Who are you?",
                "There are some who call me…",
            "Tim.",
            "Greetings, Tim, the enchanter.",
            f"Greetings, {cname}",
            f"{cname} How do you know my name?",
            f"{cname}: What are you doing here?",
            """To the north there lies a cave, the cave of Caerbannog, where
 in carved in mystic runes upon the very living rock, the last
 words of Olfin Bedwee of Rheged.""",
            "Take us there!",
            """ Follow. But follow only if you be men of valor, for the
 entrance to this cave is guarded by a creature so foul, so cruel
 that no man yet has fought with it and lived! Bones of full 50
 men lie strewn about its lair, so brave knights, if you do doubt
 your courage or your strength, come no further! For death
 awaits you all with nasty big pointy teeth."""]

#    scripta = script.copy()
    scripta = [
        "You travel to the cave...",
        "There he is!",
        cname+": Where ?",
        "Tim: There!",
        cname+": What, behind the rabbit?",
        "Tim: It is the rabbit.",
        cname+": You silly sod. You got us all worked up !",
        """Tim: That’s no ordinary rabbit. That’s the most foul, cruel, and bad
 tempered rodent you ever set eyes on.""",
        """Tim: Listen, that rabbit’s got a viscious streak a mile wide, he’s a
killer.""",
        cname+": Oh, yeah?",
        "Tim: I’m warning you!",
       cname+": Right. Silly little bleeder, one rabbit stew coming right up",
        """Tim: Wait! If you insist on fighting the rabit you must use the
holy hand grenade.""",
        cname+""": Yes, of course! The Holy Hand Grenade of Antioch! 'Tis one of the
sacred relics Brother Maynard carries with him. Brother Maynard!
Bring up the Holy Hand Grenade!""",
        cname+": How does it work?",
        "Maynard: I know not sir.",
        cname+": Consult the book of Arnaments!",
        """Maynard: Armaments, chapter two, verses nine to twenty-one:
And the Lord spake, saying, First shalt thou take out the Holy
Pin. Then, shalt thou count to three. No more. No less."""
        """Three shalt
be the number thou shalt count, and the number of the counting
shall be three. Four shalt thou not count, nor either count thou
two, excepting that thou then proceed to three. Five is right out.
Once the number three, being the third number, be reached, then,
lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who,
being naughty in My sight, shall snuff it.""",
        "Amen",
        cname+": Right!\nOne!... Two!... Five!"
        ,"You have succesfully defeated the rabbit of Caerbannog!"
        ]

    cave = [
        "You enter the cave and see many paths.",
        "You follow one down a deep and dark crevice.",
        "You find nothing of interest at the end.",
        "You suddenly can not remember which way you came."]
    cave1=[
            "It is very narrow and hard to get through",
            "You keep walking until you come across a dead end.",
            "As you turn around you see another rabbit coming torwards you...",
            "You have been killed by therabbit  :("]
    cave2=[
            "You go back through a series of tunnels...",
            "You start to see the end getting near.",
            "Oh no, there is another rabbit!"
            ]

    for i in script:
        x = 0
        x += 1
        time.sleep(3)
        print('\n',i)
        if x == 2:
            raise StopIteration

    for i in scripta[0:-2]:
        x = 0
        x += 1
        time.sleep(4)
        print('\n',i)
        if x == 2:
            raise StopIteration
    with open("/home/i3/python/medieval_game/src/cl.json") as f:
        cl = f.read()
        f.close()
        cl=int(cl)

    gs.load_game()
    if cl == 2:
        print(scripta[-1])
        gs.level_up(level, reputation, age, cname)


    for i in cave:
        x = 0
        x += 1
        time.sleep(3)
        print('\n',i)
        if x == 2:
            raise StopIteration

    a = input("There are two paths available, which one do you take?\n[1,2]\n: ")
    if a == '1':
        for i in cave1:
            x=0
            x+=1
            time.sleep(3)
            print('\n',i)
            if x==2:
                raise StopIteration

    if a =='2':
        for i in cave2:
            x=0
            x+=1
            time.sleep(3)
            print('\n',i)
            if x==2:
                raise StopIteration
        with open("/home/i3/python/medieval_game/src/cl.json") as f:
            cl = f.read()
            f.close()
            cl=int(cl)

        if cl == 3:
            time.sleep(3)
            print("\nYou have killed the rabbit!")
            gs.level_up(level, reputation, age, cname)

        print("\n\tGoing back...")
    l.navigate(cname, level, reputation, age)
