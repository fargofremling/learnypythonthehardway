# Chapter 19 Exercise

# Using the word def creates the function and is followed by the function's name. It also establishes two variables for the function.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # This prints the first line of the output of the function, which is a string that has a digit formatiting character for one of the variables defined in the function.
    print "You have %d cheeses!" % cheese_count
    # This prints the second line of the output of the function, which is a string that has a digit formatiting character for the other variable defined in the function.
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # This prints the third line of the output of the function, which is a string.
    print "Man that's enough for a party!"
    # This prints the fourth line of the output of the function, which is a string and puts a blank line at the end of the output of the function.
    print "Get a blanket. \n"

# Prints a string explaining how the function is run.
print "We can just give the function numbers directly:"
# This passes the two integers directly into the variables of the function.
cheese_and_crackers(20, 30)

# Prints a string explaining how the function is run.
print "OR, we can use variables from our script:"
# This sets the first variable.
amount_of_cheese = 10
# This sets the second variable.
amount_of_crackers = 50

# This passes the two variables in lines 22 and 24 into the function.
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# Prints a string explaining how the function is run.
print "We can even do math inside too:"

# This passes two addition equations directly into the two variables of the function.
cheese_and_crackers(10 + 20, 5 + 6)

# Prints a string explaining how the function is run.
print "And we can combine the two, variables and math:"
# This passes two variables into the function, but the variables are those defined globally outside of the function (Lines 22 & 24) and adds an integer to each of those variables.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Chapter 19 Study Drills

# 1. Go back through the script and type a comment above each line explaining in English what it does.
# See above.

# 2. Start at the bottom and read each line backward, saying all the important characters.
# Done.

# 3. Write at least one more function of your own design, and run it 5 different ways.
def pets(dogs, cats):
    print "You have adopted %d dogs." % dogs
    print "And you have adopted %d cats." % cats
    print "That means you have", dogs + cats, "pets in total!"
    print "You are a true pet hero!\n"

# Option 1
pets(2,2)

# Option 2
dogs = 2
cats = 1
pets(dogs,cats)

# Option 3
pets(3 + 3, 4 + 4)

# Option 4
pets(dogs + 1, cats + 1)

# Option 5
print "How many dogs do you have?"
dogs = int(raw_input())
print "How many cats do you have?"
cats = int(raw_input())
pets(dogs, cats)


