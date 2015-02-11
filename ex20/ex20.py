# Chapter 20 Exercise

# This is an import of a Python feature set called argv, which is the argument variable. This variable holds the arguments passed to the Python script when ran.
from sys import argv

# This line "unpacks" argv so that rather than holding all the arguments, it gets assigned to the specific number of variables being used, in this case two, script & input_file.
script, input_file = argv


# Using the word def creates the function and is followed by the function's name, in this case print_all. It also establishes one variable for the function, which in this case is a file "f".
def print_all(f):
    
    # This command prints what is read from the variable file "f".
    print f.read()

# Using the word def creates the function and is followed by the function's name, in this case rewind. It also establishes one variable for the function, which in this case is a file "f".
def rewind(f):
    # This command prints what was sought on line 0 from the variable file "f".
    f.seek(0)

# Using the word def creates the function and is followed by the function's name. It also establishes two variables for the function, in this case line_coutn and "f", which is a file.
def print_a_line(line_count, f):
    
    
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# This assigns the variable current_line to 1.
current_line = 1
print_a_line(current_line, current_file)
# This reassigns the variable current_line to 1 + 1, which is 2.
current_line = current_line + 1
print_a_line(current_line, current_file)
# This reassigns the variable current_line to 2 + 1, which is 3.
current_line = current_line + 1
print_a_line(current_line, current_file)


# Chapter 20 Study Drills

# 1. Write English comments for each line to understand what that line does.
#



# 2. Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
# 3. Find each place a function is used, and check its def to make sure that you are giving it the right arguments.
# 4. Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
# A seek() operation moves that pointer to some other part of the file so it can be read or written to at that place.

# 5. Research the shorthand notation += and rewrite the script to use += instead.
# The += creates an augmented assignement statement.  Basically it would be a simplified version of the code rewritten on lines 43 and 46. It is important to note that the when this occurs, rather than creating a new object and assigning that to the target, the old object is modified instead.