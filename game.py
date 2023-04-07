import random as r
import time as t

#loop vars
whilelooper = False
question = ""
#playerstats
playerclass = ''
playerstatslist = []
maxhealth = 0
health = 0
maxmana = 0
mana = 0
damage = 0
minIQ = 0
maxIQ = 0
IQ = 0
playerlevel = 1
XP = 0
levelup = 5
#monsterstats
mon1name = ''
mon2name = ''
mon3name = ''
monsterhealth = [0,0,0]
monsterdamage = [0,0,0]
monsters = {mon1name: monsterhealth[0],
            mon2name: monsterhealth[1],
            mon3name: monsterhealth[2]
            }
monsternames = ['vampire','werewolf','zombie','john barrilaro','margaret thatcher']

def death():
    obituarylist = [name + 'was slain',name + 'was slaughtered',name + 'was torn limb from limb']
    obitchoice = r.randint(0,2)
    print(obituarylist[obitchoice])
    quit()

def tutorial():
    print('blank space for tutorial message')

def XPfunc():
    global XP
    global playerlevel
    global levelup
    XP += playerlevel * 3
    if XP > levelup:
        playerlevel += 1
        levelup *= 3
    print('level =',playerlevel,'XP =',XP,'next level in',levelup-XP,'XP')

def monsterencounterbattle():
    global damage
    global health
    global monsterhealth
    addif = False
    print('damage =',damage)
    battlinloop = False
    print(mon1name,':',monsterhealth[0])
    print(mon2name,':',monsterhealth[1])
    print(mon3name,':',monsterhealth[2])
    while battlinloop == False:
        try:
            battleinput = int(input('choose what enemy to target'))
        except:
            print('please choose the corresponding number to the mosnter')
        else:
            if battleinput > 3 or battleinput < 1:
                print('please choose a number between 1 and 3')
            else:
                print('target selected')
                battlinloop = True
    battlinloop = False
    while battlinloop == False:
        try:
            battleinputaction = int(input('1.attack,2.defend,3.skip'))
        except:
            print('please input the number corresponding to the action')
        else:
            battlinloop = True
    if battleinputaction == 1:
        monsterhealth[battleinput - 1] -= damage
        print(monsterhealth[battleinput - 1])
        print('you attacked monster',battleinput,'!')
    elif battleinputaction == 2:
        monsterdamage[battleinputaction] -= 1
        print('you defended against monster',battleinput,'!')
        if monsterdamage[battleinputaction - 1] < 0:
            monsterdamage[battleinputaction] = 0
    else:
        print('turn skipped... why?')

    if addif == True:
        damage += 1
        addif = False
        print(damage)
    #monster actions

    monsteractionchoice = r.randint(1,3)
    monsterdecision = r.randint(1,2)

    if monsterdecision == 1:
        health -= monsterdamage[monsteractionchoice-1]
        print('monster',monsteractionchoice,'attacked you')
    elif monsterdecision == 2:
        damage-=1
        print('dmaage',damage)
        addif = True
        print('monster',monsteractionchoice,'defended against you')
    else:
        print('the monster skipped its attack because it was dropped on its head as a child')
    #monserterjitjngjngtgtg

    if health < 1:
        print('you died :(')
        death()
    if monsterhealth[0] != '🕱':
        if monsterhealth[0] <= 0:
            print('monster',mon1name,'died')
            monsterhealth[0] = '🕱'
    if monsterhealth[1] != '🕱':
        if monsterhealth[1] <= 0:
            print('monster',mon2name,'died')
            monsterhealth[1] = '🕱'
    if monsterhealth[2] != '🕱':
        if monsterhealth[2] <= 0:
            print('monster',mon3name,'died')
            monsterhealth[2] = '🕱'

    if monsterhealth[0] == '🕱' and monsterhealth[1] == '🕱' and monsterhealth[2] == '🕱':
        print('battle complete!')
        XPfunc()
    else:
        print(addif)
        monsterencounterbattle()
        

def monsterencountersetup():
    global mon1name
    global mon2name
    global mon3name
    global monsterhealth
    global monsterdamage
    global monsternames
    global playerlevel
    mon1name = r.randint(0,4)
    mon1name = monsternames[mon1name]
    mon2name = r.randint(0,4)
    mon2name = monsternames[mon2name]
    mon3name = r.randint(0,4)
    mon3name = monsternames[mon3name]
    monsterhealth[0] = r.randint(5*playerlevel,10*playerlevel)
    monsterhealth[1] = r.randint(5*playerlevel,10*playerlevel)
    monsterhealth[2] = r.randint(5*playerlevel,10*playerlevel)
    monsterdamage[0] = r.randint(1*playerlevel,3*playerlevel)
    monsterdamage[1] = r.randint(1*playerlevel,3*playerlevel)
    monsterdamage[2] = r.randint(1*playerlevel,3*playerlevel)
    battlinloop = False
    monsterencounterbattle()

def statsetup():
    global maxhealth
    global damage
    global maxmana
    global health
    global mana
    global IQ
    global minIQ
    global maxIQ
    health = maxhealth
    playerstatslist.append(health)
    mana = maxmana
    playerstatslist.append(mana)
    IQ = r.randint(minIQ, maxIQ)
    playerstatslist.append(IQ)

def classstats(playerclass):
    global minIQ
    global maxIQ
    global maxhealth
    global damage
    global maxmana
    if playerclass == 'wizard':
        maxhealth = 10
        damage = 5
        maxmana = 50
        minIQ = r.randint(10,15)
        maxIQ = minIQ + round(minIQ / 2)
    elif playerclass == 'warrior':
        maxhealth = 20
        damage = 10
        maxmana = 10
        minIQ = r.randint(7,12)
        maxIQ = minIQ + round(minIQ / 2)
    elif playerclass == 'nomad':
        maxhealth = 25
        damage = 15
        maxmana = 0
        minIQ = r.randint(3,7)
        maxIQ = minIQ + round(minIQ / 2)
    else:
        maxhealth = 1
        damage = 1
        maxmana = 1
        minIQ = r.randint(0,1)
        maxIQ = minIQ + round(minIQ / 2)
    statsetup()

def rightpath():
    inp = ""
    global playeractions
    global enemyactions
    playeractions = ("finger guns","raise hand","thumbs up")
    enemyactions = ("raise both hands","crouched down","hit the griddy")

    print("you see a man hunched in a ball at the end of the hallway\nhe turns back, stands up and beckons you to take another step")
    while inp != "yes" and inp != "no":
        inp = input("do you wish to start the tutorial for the placeholder section? (heavily reccomended)").lower()
        if inp == "yes":
            print("filler message")
        elif inp != "yes" and inp != "no":
            print("please enter yes or no")

    def rightmain():
        playeract = ""
        actcount = ""
        global playeractions
        global enemyactions
        enemyact = r.choice(enemyactions)
        fingycount = r.randint(2,10)
        print("the monster " + enemyact)
        print("the monster raised",fingycount,"fingers")
        while playeract not in playeractions:
            playeract = input("input an action in response").lower()
            if playeract in playeractions:
                actindex = playeractions.index(playeract)
                enemyact = enemyactions.index(enemyact)
            else:
                print("please input a valid action")
        while type(actcount) == type(0):
            try:
                actcount == input("input the number of fingers to raise")
                print(actcount)
                actcount = str(actcount)
            except:
                print("please input a number you unseasoned chicken wing")
                actcount = ""
            else:
                if actindex == enemyact and actcount == fingycount:
                    print("the monster seemed pleased\nit began to slowly dissapear")
                    exit()
                elif actindex == enemyact:
                    print("it numbers fingy that bad lmao")
                    print("v1 =",actcount,"v2 =",fingycount)
                elif actcount == fingycount:
                    print("cobble wobble gob")
                else:
                    print("the monster seemed displeased\nit charged at you")
                    print("v1 =",actindex,"v2 =",enemyact)
                    death()
    rightmain()

def leftpath():
    
    def eventone():
        print("nothing happened")
        
    def eventtwo():
        global fear
        print("you here a noise from beyond the door")
        fear += 1
        print("fear increased")
        
    def eventthree():
       global fear
       if fear > 0:
           fear -= 1
           print("you suddenly feel more relaxed\nfear decreased")
       else:
            print("nothing happened")

    def eventfour():
       inp = ''
       while inp != "yes" and "no":
           inp = input("you hear a noise form behind you, do you wish to turn back? ")
           if inp == "yes":
               print(r.choice(["you look behind you, nothing was there", "you look behind you, you thought you saw something; but it was probably just a shadow"]))           
    steps = 0
    maxsteps = 9
    global fear
    fear = 0
    inp = ""
    ques = ""
    repeat = False
    while inp != "yes" and inp != "no":
        print(inp)
        inp = input("do you wish to start the tutorial for the hallway section?")
        if inp == "yes":
            print("filler tutorial message")
        elif inp != "no" and inp != "yes":
            print("please input yes or no")
            
    while ques != "yes" or ques != "no":
        if repeat == False:
            ques = input("at the end of a hallway lies a door, do you wish to approach? ").lower()
            repeat = True
        else:
            ques = input("do you wish to take another step").lower()
        if ques == "yes":
            print("you stepped closer")
            steps+=1
            print("you are",maxsteps-steps,"away from the door")
            ranevent = r.randint(1,4)
            if ranevent == 1:
                eventone()
            elif ranevent == 2:
                eventtwo()
            elif ranevent == 3:
                eventthree()
            else:
                eventfour()
        elif ques == "no":
            print("you lay still but it seems to be the only option")
            print("you are",maxsteps-steps,"steps away from the door")
        else:
            print("please input yes or no")

def intro():
    global classlooper
    global whilelooper
    print('you slowly awaken in a small dark room\nyou try to remember your name, you try to remember your age but alas you cant')
    name = input('input your name: ')
    playerstatslist.append(name)
    gender = input('input your gender: ')
    playerstatslist.append(gender)
    while whilelooper == False:
        playerclass = input('input your class (wizard, warrior, nomad or jimmy kimmel) ').lower()
        playerstatslist.append(playerclass)
        classes = ["wizard","warrior","nomad","jimmy kimmel"]
        if playerclass not in classes:
            print('input one of the available classes, did you make a typo?')
            playerclass = ''
        else:
            print('character creation complete')
            whilelooper = True
            classstats(playerclass)
    print('you suddenly remember everything about yourself like this is some cliche character creation segment\nStats:\n')
    for st in playerstatslist:
        print(st)
    print('you hear a creek coming from the door infront of you')
    for waiting in range(4):
        t.sleep(1)
        print('.')
    print('the door opens revealing a massive monster!')
    positivechoicelist = ['yes','yeah','yes sir','yeah','yeah!']
    negativechoicelist = ['no','nope','nah']
    whilelooper = False
    while whilelooper == False:
        choice = input('do you wish to start the combat tutorial?').lower()
        if choice in positivechoicelist:
            tutorial()
            whilelooper = True
        elif choice in negativechoicelist:
            print('tutorial skipped')
            whilelooper = True
        else:
            print('please enter a common word that means "yes" or "no"')
    monsterencountersetup()
    print("you went through the door. You're presented with a forked hallway")
    while question != "left" or question != "right":
        ques = input("do you wish to go left or right").lower()
        if ques == "left":
            print("you went left")
            leftpath()
        elif ques == "right":
            print("you went right")
            rightpath()
        else:
            print("please input left or right")
        
intro()



