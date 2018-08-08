#Ejercicio 41

#Fix the error

from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this", "Nice job, you died", "Such a luser"]
    print quips[randint(0,len(quips)-1)]
    exit(0)

death()

print "Select an action (shoot! - dodge! - tell a joke)"
action = raw_input(">")

if action == "shoot!":
    print "You are a killer"

elif action == "dodge!":
    print "You dodged the shot"

elif action == "tell a joke":
    print "Knock Knock... Buh!"

else:
    print "Does not compute"
    return 'central_corridor'

def laser_weapon_armory():
    print "Get the bomb. The code is 3 digits"
    code = "%d%d%d" %(randint(1,9),randint(1,9),randint(1,9))
    guess = raw_input("[keypad]>")
    guesses = 0

    while guess != code and guesses < 3:
        print "BZZZZED"
        guesses += 1
        guess = raw_input("[keypad]>")

    if guess == code:
        print "The container opens"
        return 'the_bridge'

    else:
        print "The lock buzzes one last time"
        return 'death'

def the_bridge():
    print "The bridge of the death"
    action = raw_input(">")
    if action == "throw the bomb":
        print "BOOOOOMBA"

    elif action == "slowly place the bomb":
        print "We are OK"
        return 'escape_pod'

    else:
        print "Does not compute"
        return "the_bridge"

def escape_pod():
    print "This is the last"

    good_pod = randint(1,5)
    guess = raw_input("[pod#]>")
