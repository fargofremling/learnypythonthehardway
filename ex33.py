# While Loops

print "Original Lesson Code"

i = 0
numbers = []
 
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
print "The numbers: "

for num in numbers:
    print num

# Study Drills
# 1. Convert this while-loop to a function that you can call, and replace 6 in the test 
# (i < 6) with a variable.
# 2. Use this function to rewrite the script to try different numbers.
# 3. Add another variable to the function arguments that you can pass in that lets 
# you change the + 1 on line 8 so you can change how much it increments by.
# 4. Write it to use for-loops and range. Do you need the incrementor in the middle anymore?
# What happens if you do not get rid of it?

print "\n"
print "Study Drill 1 & 2"

i = 0
numbers = []

def while_loop():

    global i
    
    print "How many numbers would you like to add to our list?"

    input = raw_input("> ")
     
#   HOW DO I CHANGE A INPUT STRING INTO AN INTEGER???
    while i < int(input):
        print "At the top i is %d" % i
        numbers.append(i)
    
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

while_loop()
    
print "The numbers: "

for num in numbers:
    print num

print "\n"
print "Study Drill 3"

i = 0
numbers = []

def while_loop():

    global i
    
    print "How many numbers would you like to add to our list?"

    input = raw_input("> ")
    
    print "By how much should each number increase?"
    
    increase = raw_input("> ")
     
    # It's necessary to multiply input by increase, so the while loop iterates
    # the expected number of times.
    while i < (int(input)*int(increase)):
        print "At the top i is %d" % i
        numbers.append(i)
    
        i += int(increase)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

while_loop()
    
print "The numbers: "

for num in numbers:
    print num

print "\n"
print "Study Drill 4"

i = 0
numbers = []

def for_loop():

    global i
    
    print "How many numbers would you like to add to our list?"

    input = raw_input("> ")
    
    print "By how much should each number increase?"
    
    increase = raw_input("> ")
     
    # It's necessary to multiply input by increase, so the while loop iterates
    # the expected number of times.
    for i in range (0, (int(input)*int(increase)), int(increase)):
    
#     while i < (int(input)*int(increase)):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % (i + int(increase))

for_loop()
    
print "The numbers: "

for num in numbers:
    print num