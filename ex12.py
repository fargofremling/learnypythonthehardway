# Chapter 12 Exercise

age = raw_input ("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input ("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
                 
# Chapter 12 Study Drills

# 1. In Terminal where you normally run python to run your scripts, type pydoc raw_input. Read what it says.

# The output is the following:


# Help on built-in function raw_input in module __builtin__:

# raw_input(...)
# raw_input([prompt]) -> string
    
    # Read a string from standard input.  The trailing newline is stripped.
    # If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    # On Unix, GNU readline is used if enabled.  The prompt string, if given,
    # is printed without a trailing newline before reading.
# (END)


# 2. Get out of pydoc by typing q to quit.

# Done.


# 3. Look online for what the pydoc command does.

# Pydoc is a documentation module that allows Python programmers to access Python's documentation help files, generate HTML pages with documentation specifics, and find the appropriate module for a particular job.

# 4. Use pydoc to also read about open, file, os, and sys. It's alright if you do not understand those; just read through and take notes about interesting things.


# open
# open(...)
# open(name[, mode[, buffering]]) -> file object
    
    # Open a file using the file() type, returns a file object.  This is the
    # preferred way to open a file.  See file.__doc__ for further information.



# file
# class file(object)
# file(name[, mode[, buffering]]) -> file object

# Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
# writing or appending.  The file will be created if it doesn't exist
# when opened for writing or appending; it will be truncated when
# opened for writing.  Add a 'b' to the mode for binary files.
# Add a '+' to the mode to allow simultaneous reading and writing.
# If the buffering argument is given, 0 means unbuffered, 1 means line
# buffered, and larger numbers specify the buffer size.  The preferred way
# to open a file is with the builtin open() function.
# Add a 'U' to mode to open the file for input with universal newline
# support.  Any line ending in the input file will be seen as a '\n'
# in Python.  Also, a file so opened gains the attribute 'newlines';
# the value for this attribute is one of None (no newline read yet),
# '\r', '\n', '\r\n' or a tuple containing all the newline types seen.
# 'U' cannot be combined with 'w' or '+' mode.
# Methods defined here:



# os
# NAME
# os - OS routines for Mac, NT, or Posix depending on what system we're on.

# FILE
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.py

# MODULE DOCS
# http://docs.python.org/library/os

# DESCRIPTION
# This exports:
# - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
# - os.path is one of the modules posixpath, or ntpath
# - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
# - os.curdir is a string representing the current directory ('.' or ':')
# - os.pardir is a string representing the parent directory ('..' or '::')
# - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
# - os.extsep is the extension separator ('.' or '/')
# - os.altsep is the alternate pathname separator (None or '/')

# sys
# NAME
# sys

# FILE
# (built-in)

# MODULE DOCS
# http://docs.python.org/library/sys

# DESCRIPTION
# This module provides access to some objects used or maintained by the
# interpreter and to functions that interact strongly with the interpreter.
    
    # Dynamic objects:
    
    # argv -- command line arguments; argv[0] is the script pathname if known
    # path -- module search path; path[0] is the script directory, else ''
    # modules -- dictionary of loaded modules
    
    # displayhook -- called to show results in an interactive session
    # excepthook -- called to handle any uncaught exception other than SystemExi