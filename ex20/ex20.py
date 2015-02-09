# Chapter 20 Exercise

# This is an import of a Python feature set called argv, which is the argument variable. This variable holds the arguments passed to the Python script when ran.
from sys import argv

# This line "unpacks" argv so that rather than holding all the arguments, it gets assigned to the specific number of variables being used, in this case two, script & input_file.
script, input_file = argv


# Using the word def creates the function and is followed by the function's name. It also establishes one variable for the function, which in this case is a file "f".
def print_all(f):
    
    # This command prints what is read from the variable file "f".
    print f.read()

# Using the word def creates the function and is followed by the function's name. It also establishes one variable for the function, which in this case is a file "f".
def rewind(f):
    # This command prints what was sought on line 0 from the variable file "f".
    f.seek(0)

# Using the word def creates the function and is followed by the function's name. It also establishes two variables for the function, one of which is a file "f".
def print_a_line(line_count, f):
    
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)


# Chapter 20 Study Drills

# 1. Write English comments for each line to understand what that line does.
#