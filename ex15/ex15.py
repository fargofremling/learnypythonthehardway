# Chapter 15 Exercise

# This is an import of a Python feature set called argv, which is the argument variable. This variable holds the arguments passed to the Python script when ran.
from sys import argv

# This line "unpacks" argv so that rather than holding all the arguments, it gets assigned to the specific number of variables being used.
script, filename = argv

# This assigns the variable txt to the opened filename.
txt = open(filename)

# This prints the following string and the file name.
print "Here's your file %r:" % filename
# This prints what is read from the txt file.
print txt.read()
txt.close()

# This prints the request to type the filename again.
print "Type the filename again:"
# This calls for the user input, which will assign the variable file_again.
file_again = raw_input("> ")

# This assigns the variable txt_again to the opened file_again.
txt_again = open(file_again)

# This prints what is read from the txt file called txt_again.
print txt_again.read()
txt.close()

# Chapter 15 Study Drills

# 1. Above each line, write out in English what that line does.
# See comments above.


# 2. If you are not sure ask someone for help or search online. Many times searching for "python THING" will find answers to what that THING does in Python. Try searching for "python open."
# Sample search result: Open a file, returning an object of the file type described in section File Objects.

# 3. I used the word "commands" here, but commands are also called "functions" and "methods." You will learn about functions and methods later in the book.
# Ok.


# 4. Get rid of the lines 10-15 where you use raw_input and run the script again.

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()


# 5. Use only raw_input and try the script that way. Why is one way of getting the filename would be better than another?

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# 6. Start python to start the Python shell, and use open from the prompt just like in this program. Notice how you can open files and run read on them from within python?

# 7. Have your script also call close() on the txt and txt_again variables. It's important to close files when you are done with them.
# See line 16 and 28 above.     