people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats: 
	print "Not too many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"


dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."


# Study Drills
# 1. What do you think the if does to the code under it?
# - If the condition is true in the if-statement, then the code does the indented statements. 
# - If the condition is not true, then the code skips the indented statements.
# 2. Why does the code under the if need to be indented four spaces?
# - This code is indented, because it is only needed if the statement is true. 
# 3. What happens if it isn't indented?
# - There will be a syntax error and the code will not run.
# 4. What happens if you change the initial values for people, cats, and dogs?
# - Different if-statements would be executed. 