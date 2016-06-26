print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese case. What eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bears eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away."

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.Good job!"
    else: 
        print "The insanitiy rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"

# Study Drill
# Write a completely new game. Maybe you don't like this one, so make your own. 
# This is your computer, do what you want.

print "Choose your own adventure #2"

print "You are on the Price is Right."
print "The host gives you the option to chose among three briefcases."

suitcase = raw_input("Chose 1, 2 or 3 > ")

if suitcase == "1":
    print """There's $1,000 cash, and a note that says, 
    \"You can keep the cash, or give it up and chose a different briefcase.
    One suitcase has a value greater than $1,000, the other has a lesser value.\""""
    print "1. Keep the $1,000 cash"
    print "2. Give up the $1,000 and pick briefcase #2"
    print "3. Give up the $1,000 and pick briefcase #3"
    
    cash_choice = raw_input("> ")
    
    if cash_choice == "1":
        print "Nice, $1,000 is a good chunk of change!"
    elif cash_choice == "2":
        print "Let's see what's in suitcase two...$5,000!"
    else:
        print """Well, maybe you can go to dinner with tht $50?
        Better luck next time."""

elif suitcase == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else: 
        print "The insanitiy rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"