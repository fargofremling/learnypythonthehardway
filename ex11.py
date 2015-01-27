# Chapter 11 Exercise

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Chapter 11 Study Drills

# 1. Go online and find out what Python's raw_input does.

# "raw_input" is a prompt that allows a user to actually enter input into a program.

#2. Can you find other ways to use it? Try some of the samples you find.

# This is the original example I found.
name = raw_input('Enter your name : ')
print ("Hi %s, Let us be friends!" % name);

# I have modified it to fit the formatting of the example problem.
print "What is your name?",
my_name = raw_input()

print "Hi %s, Let us be friends!" % (my_name);

#3. Write another "form" like this to ask some other questions.

print "What is your name?",
your_name = raw_input ()
print "Nice to meet you %s!" % your_name
print "What is your favorite color?",
color = raw_input ()
print "That's so interesting that your favorite colors is %s, %s; so is mine!" % (color, your_name)

#4. Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?

# The escape backlash "\" is present in the printout on the original exercise because the formatter character used was %r, which this character is used for debugging programs. However, if the %s (string) formatter character is used instead, like below, it will result in the program printing the desired output withouth show the escape backslash.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)