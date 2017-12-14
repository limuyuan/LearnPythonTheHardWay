from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    nexit = raw_input("> ")
    isNumber = "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in nexit
    if isNumber:
        how_much = int(nexit)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        nexit = raw_input("> ")

        if nexit == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif nexit == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif nexit == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif nexit == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    nexit = raw_input("> ")

    if "flee" in nexit:
        start()
    elif "head" in nexit:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    nexit = raw_input("> ")

    if nexit == "left":
        bear_room()

    elif nexit == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
