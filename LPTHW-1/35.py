#Ejercicio 36

from sys import exit

#Version de prueba

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input(">")
    if "0" in next or "1" in next:
        how_much = int(next)

    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, you are not greedy, you win"
        exit(0)

    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of honey"
    print "The fat bear is in fron of another door"

    while True:
        next = raw_input(">")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off")

        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door, you can go through it now"

        elif next == "open door" and bear_moved:
            gold_room()

        else:
            print "I got no idea what that means"

def cthulu_room():
    print "Here you see the great evil Cthulu"
    print "He, it whatever"

    next = raw_input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulu_room()

def dead(why):
    print why, "good job"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is a door to your right and left"

    next = raw_input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()

    else:
        dead("Ya acabo mijos")

start()
