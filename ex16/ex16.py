# Chapter 16 Exercise

# This is an import of a Python feature set called argv, which is the argument variable. This variable holds the arguments passed to the Python script when ran.
from sys import argv

# This line "unpacks" argv so that rather than holding all the arguments, it gets assigned to the specific number of variables being used, in this case, two.
script, filename = argv
# This prints the following string and the file name.

# This prints the following string and the file name.
print "We're going to erase %r." % filename
# This prints the instructions for if the user wants to escape the script, since CTRL-C is the keyboard interrupt command.
print "If you don't want that, hit CTRL-C (^C)."
# This prints the instructions for if the user wants to proceed with erasing the file.
print "If you do want that, hit RETURN."

# This is the prompt for the user to provide their answer (input).
raw_input("?")

# This prints to tell the user that the file is being opened.
print "Opening the file..."
# This command actually opens the file in the write mode.
target = open(filename, 'w')

# This prints to tell the user that the file is being truncated.
print   "Truncating the file. Goodbye!"
# This command actually truncates the file.
target.truncate()

# This prints to tell the user to enter three lines of text.
print "Now I'm going to ask you for three lines."

# This sets the variable line1 to whatever the user inputs.
line1 = raw_input("line 1: ")
# This sets the variable line2 to whatever the user inputs.
line2 = raw_input("line 2: ")
# This sets the variable line3 to whatever the user inputs.
line3 = raw_input("line 3: ")

# This tells the user that the script is going to print the three lines in the new file.
print "I'm going to write these to the file."

# This is the single line as discussed in Study Drill #3 that replace the commented out lines below.
target.write(line1 + "\n" + line2 + "\n" + line3)

# This writes line1 in the file.
# target.write(line1)
# This writes a new line in the file.
# target.write("\n")
# This writes line2 in the file.
# target.write(line2)
# This writes a new line in the file.
# target.write("\n")
# This writes line3 in the file.
# target.write(line3)
# This writes a new line in the file.
# target.write("\n")

# This tells the user that the file is being closed.
print "And finally, we close it."
# This actually closes the file.
target.close()

# Chapter 16 Study Drills

# 1. If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.
# See above.

# 2. Write a script similar to the last exercise that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

target.close()

# 3. There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
# See above.

# 4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
# The default mode of opening a file is just read. So if we want to write in a file, we must explicitly pass the 'w' parameter, so that the file can be written in.

# 5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python's open function and see if that's true.
# I tried running the program with line 28, which is the truncate line, and the script still ran without any issues. I also looked at pydoc open, and it did not specifically say that truncate was necessary. So my guess is that the command target.truncate is not necessary when opening a file in write 'w' mode.