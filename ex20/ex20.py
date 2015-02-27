# Chapter 20 Exercise

# Imports a Python feature set called argv, which is the argument variable. This variable holds the arguments passed to the Python script when ran.
from sys import argv


# "Unpacks" argv so that rather than holding all the arguments, it gets assigned to the specific number of variables being used, in this case two, script & input_file.
script, input_file = argv


# Using the word def creates the function and is followed by the function's name, in this case print_all. It also establishes one variable for the function, which in this case is a file "f".
def print_all(f):
    # Prints what is read from the variable file "f".
    print f.read()


# Using the word def creates the function and is followed by the function's name, in this case rewind. It also establishes one variable for the function, which in this case is a file "f".
def rewind(f):
    # Seeks what is sought on line 0 from the variable file "f".
    f.seek(0)


# Using the word def creates the function and is followed by the function's name. It also establishes two variables for the function, in this case line_coutn and "f", which is a file.
def print_a_line(line_count, f):
    #Prints the variable line_count and reads/prints the line from the file.
    print line_count, f.readline()

# Sets the variable current_file to opening the input_file, which for this example is test.txt.
current_file = open(input_file)

# Prints the string in quotes
print "First let's print the whole file:\n"

# Calls the function print_all, which then prints the contents of the input_file, which in this example is test.txt.
print_all(current_file)

# Prints the string in quotes
print "Now let's rewind, kind of like a tape."

# Calls the function rewind, which seeks to line 0 in the input_file, which in this example is test.txt.
rewind(current_file)

# Prints the string in quotes
print "Let's print three lines:"

# Assigns the variable current_line to 1.
current_line = 1
# Calls the function print_a_line, which then prints the number of the current active line  of the input_file and the contents of that line, which in this example is test.txt. current_line = 1
print_a_line(current_line, current_file)
# Increments the variable current_line to 1 + 1, which is 2. Changed this from current_line = current_line + 1 to the shorthand notation using +=.
current_line += 1
# Calls the function print_a_line, which then prints the number of the current active line  of the input_file and the contents of that line, which in this example is test.txt. current_line = 2
print_a_line(current_line, current_file)
# Increments the variable current_line to 2 + 1, which is 3. Changed this from current_line = current_line + 1 to the shorthand notation using +=.
current_line += 1
# Call the function print_a_line, which then prints the number of the current active line  of the input_file, which in this example is test.txt. current_line = 3
print_a_line(current_line, current_file)


# Chapter 20 Study Drills

# 1. Write English comments for each line to understand what that line does.
# Done. See above.



# 2. Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
# See above, lines 48, 52 and 56.
# When the function print_a_line is called on lines 49, 53 and 57, the function requires two variables of input in order to run. The first variable defined in the function is line_count, and it is satisfied by the variable current_line, since it is passed when the function is called. Therefore, when the function print_a_line is called on lines 49, 53, and 57, the program ends up printing the variable current_line.


# 3. Find each place a function is used, and check its def to make sure that you are giving it the right arguments.
# The function print_all is called on line 35. It requires one variable of a file, which when it is called, it receives current_file. This is the right argument.
# The function rewind is called on line 41. It requires one variable of a file, which when it is called, it receives current_file. This is the right argument.
# The function print_a_line is called on lines 49, 53 and 57. It requires two variable, which it receives each time, current_line and current_file).


# 4. Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
# A seek() operation moves that pointer to some other part of the file so it can be read or written to at that place.



# 5. Research the shorthand notation += and rewrite the script to use += instead.
# The += creates an augmented assignement statement.  Basically it would be a simplified version of the code rewritten on lines 41 and 45 (see above). It is important to note that the when this occurs, rather than creating a new object and assigning that to the target, the old object is modified instead.