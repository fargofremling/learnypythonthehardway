print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
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
legal_choice = False3
3

def briefcase_options():
    if cash_choice == "1":
        print "Nice, $1,000 is a good chunk of change!"
    elif cash_choice == "2":
        print "Let's see what's in suitcase 2...$5,000! Good choice!"
    elif cash_choice == "3":
        print "With suitcase 3, you can ...well, buy dinner with that $50? Better luck next time."
            
print "Choose your own adventure #2"

print "You are on the Price is Right."
print "The host gives you the option to choose among three briefcases."

suitcase = raw_input("Choose 1, 2 or 3 > ")

if suitcase == "1":
    print """There's $1,000 cash, and a note that says, 
    \"You can keep the cash, or give it up and choose a different briefcase.
    One suitcase has a value greater than $1,000, the other has a lesser value.\""""
    print "1. Keep the $1,000 cash."
    print "2. Give up the $1,000 and pick briefcase #2."
    print "3. Pick briefcase #3 and give up the $1,000."
    
    cash_choice = raw_input("> ")
    
    while legal_choice is False:
        if cash_choice in ["1", "2", "3"]:
#       Why does this list have to be strings? Does raw_input only accept strings?
            briefcase_options()
            break
#           legal_choice = True ^^ which is a better way to break the loop?
        else:
            print "That's not an option. Please choose 1, 2 or 3."
            cash_choice = raw_input("> ")
            briefcase_options()
            continue

elif suitcase == "2":
    print "It's your lucky day! You picked the largest prize of $5,0000!"

elif suitcase == "3": 
    print ("You picked the smallest prize possible, a mere $50. "
    "However, since this is the Price is Right, "
    "and we want our audience members to go home as big winners, "
    "choose another suitcase.")
    
    print "Choose between briefcase 1 or 2."
   
    better_choice = raw_input("> ")
    
    if better_choice == "1":
        print "Much better...$1,000!"

    elif better_choice == "2":
        print "You just increased your winning by 100 times. You won $5,000!"
        
    else: 
        print "Game over, Chump. You didn't choose between 1 oe 2."
        
else:
    print "Game over. You didn't choose among the three suitcases."