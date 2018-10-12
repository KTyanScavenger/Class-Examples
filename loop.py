#Kyla Ryan
#10/12/18


##loops=0
##while True:
##    print("i have looped",loops,"times")
##    loops+=1
##    if loop==10000:
##        break

##count=0
##while True:
##    count+=1
##    if count>100:
##        break
##    if count==5 or count==25 or count==50:
##        continue
##    print (count)
##input("/n/n press enter to exit")
##
##i=0
##while i<=1000:
##
##    print("looping")
##    i+=1

##i="enter"
##while i=="enter":
##    print("looping")
##    x=input("do you want to keep looping yes or no ")
##    if x=="yes":
##        continue
##    else:
##        i=" "

##print("Your lone hero is surrounded by a massive army of trolls.")
##print("Their decaying green bodies stretch out, melting into the horizon.")
##print("Your hero unshethes his sword for the last firght of his life. \n")
##
##
##
##health=10
##trolls=0
##damage=3
##
##while health<=0:
##    trolls+=1
##    health-=damage
##    print("Your hero swings and defeats and evil troll,"\
##          "but, takes ", damage, "damage points. \n")
##    print("Your hero fought valiantly and defeated", trolls, "trolls.")
##    print("But alas, your hero is no more.")
##    input("\n\n Press the exit key to exit.")

import random          
mHealth=100
pHealth=100
win=0
choice=input("Fight or Flee!: ")

while choice=="fight":
    pDamage= random.randrange(0,25)
    mDamage= random.randrange(0,25)
    mHealth-= pDamage
    if pDamage==0:
        print("You missed!")
    elif pDamage<=10:
        print("Low damage! You did ", pDamage,"Monster Health is now", mHealth-pDamage)
    elif pDamage>10:
        print("Great damage! You did ", pDamage, mHealth-pDamage)
    
    if mHealth>0:
        pHealth-=mDamage
        print("The monster is still alive, it hit you for",mDamage, "damage."+
              "Your health is now: ",pHealth-mDamage)
        
    if mHealth<=0:
        print("The monster is dead!")
        win=1
        break
    elif pHealth<=0:
        print("You have died.")
        win=0
        break
    elif pHealth>=0 or mHealth>=0:
        print("You have", pHealth,"health.")
        print("The monster has", mHealth,"health.")
        choice=input("Fight or Flee!: ")
        if choice!="fight" or choice!="flee":
            print("Not sure what that is.")
        choice="attack"
        continue
    else:
        continue

if choice=="flee":
    print("You are a coward!")
    win=0
if win==0:
    print("Game Over.")
else:
    print("You won!")
