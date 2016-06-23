people = 30
cars = 40
trucks = 15

# if the cars variable value is greater than the people variable value,
# continue to the indented code below.
if cars > people:
# the above condition of more cars than people is met, so print the following statement.
    print "We should take the cars."
# if the first condition is not met, and the cars variable value is less
# than the people variable value, continue to the indented code below.
elif cars < people:
# the above condition of less cars than people is met, so print the following statement.
    print "We should not take the cars."
# the above two conditions (cars is not greater than or less than people, 
# therefore cars and people are equal) were not met,
# so continue to the indented code below.
else:
    print "We can't decide."

# if the truck variable value is greater than the car variable value,
# continue to the indented code below.
if trucks > cars:
# the above condition of more trucks than cars is met, so print the following statement.
    print "That's too many trucks."
# if the first condition is not met, and the truck variable value is
# less than the car variable value, continue to the indented code below.
elif trucks < cars:
# the above condition of fewer trucks than cars is met, so print the following statement.
    print "Maybe we could take the trucks."
# the above two conditions (trucks is not greater than or less than cars, 
# therefore trucks and cars are equal) were not met,
# so continue to the indented code below.
else:
    print "We still can't decide."

# if the people variable value is greater than the truck variable value,
# continue to the indented code below.
if people > trucks:
# the above condition is met, so print the following statement.
    print "Alright, let's just take the trucks."
# the above conditions (there are more people than trucks) was not met,
# so continue to the indented code below.
else:
    print "Fine, let's stay home then."

# Study Drills
# 1. Try to guess what elif and else are doing.
# - Elif and else provide alternatives to the if condition, if it is not met. 
# 2. Change the numbers of cars, people and trucks and then trace through each if-statement to see what will be printed.
# - As the number of cars, people and trucks change, the conditions change and the associated statements are printed.
# 3. Above each line write an English description of what the line does.
# - See code above.