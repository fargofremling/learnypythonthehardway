# Branches and Functions

from sys import exit

def gold_room():

    print "This room is full of gold. How many gold bars do you take?"
    
    choice = raw_input("> ")
    
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else: 
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        dead("Nice, you're not greedy; you win!")
    else:
        dead("You greedy bastard!")
    
def bear_room():
    
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear? Take honey or taunt bear?"
    
    bear_moved = False
    
    while True:
        choice = raw_input("> ").lower()
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can open the door now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():

    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insanse."
    print "Do you flee for your life or fight for your life?"
    
    choice = raw_input("> ").lower()
    
    if "flee" in choice:
        start()
    elif "fight" in choice:
        dead("Silly, you; you can't fight Cthulhu! You're dead!!")
    else:
        cthulhu_room()
        
def dead(why):

    print why, "Good job!"
    exit(0)
    
def start():

    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    choice = raw_input("> ").lower()
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.:")
        
start()
