# Chapter 13 Exercise

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


# Chapter 13 Study Drills

# 1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.

#Error:

# Traceback (most recent call last):
    # File "ex13.py", line 5, in <module>
    # script, first, second, third = argv
# ValueError: need more than 1 value to unpack

# the argv requires three variables in addition to "script" since that is what was established on line five of the code.

# 2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.

# fewer
# from sys import argv

# script, first = argv

# print "My program is called:", script
# print "My fiance is:", first

# more
#from sys import argv

# script, first, second, third, fourth = argv

# print "This program is called:", script
# print "Our oldest pet's name is:", first
# print "Our second oldest pet is:", second
# print "Our second youngest pet is:", third
# print "Our youngest pet is:", fourth

# 3. Combine raw_input with argv to make a script that gets more input from a user.

# from sys import argv

# script, first, second, third, fourth = argv

# print "This program is called:", script
# print "Our oldest pet's name is:", first
# print "Our second oldest pet is:", second
# print "Our second youngest pet is:", third
# print "Our youngest pet is:", fourth

# petname = raw_input ("What is your pet's name? ")

# print "Is %s a good pet?" % petname

# 4. Remember that modules give you features. Modules. Modules. Remember this because we'll need it later.

# Got it!