# Chapter 18 Exercise

# This one is like the scripts with argv.
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument.
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments.
def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# Chapter 18 Study Drills

# Create a function checklist for later exercise. Write these check on an index card and keep it by you while you complete the rest of these exercises or until you feel you do not need the index card anymore.

# 1. Did you start your fuction definition with 'def'?
# 2. Does your function name have only characters and _ (underscore) characters?
# 3. Did you put an open parenthesis ( right after the function name?
# 4. Did you put your arguments after the parathesis (  separated by commas?
# 5. Did you make each argument unique (meaning no duplicated names)?
# 6. Did you put a close parenthesis and a colon ): after the arguments?
#7. Did you indent all line of code you want in the function four spaces? No more, no less.
# 8. Did you "end" your function by going back to writing with no indent (dedenting we call it)?

# When you run ("use" or "call") a function, check these things:

# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into parenthesis separated by commas?
# 4. Did you end the function call with a ) character?

# "To 'run,' 'call,' or 'use' a function all mean the same thing.