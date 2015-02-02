# Chapter 17 Exercise

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?
in_file = open (from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# Chapter 17 Exercise

# 1. This script is really annoying. There's no need to ask you before doing the copy, and it prints too much out to the screen. Try to make the script more friendly to use by removing features.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s. Ok, done." % (from_file, to_file)

# Got this one down to one line.
indata =  open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()

# 2. See how short you can make the script. I could make this one line long.
# I got the script down from 24 lines of code to 14 lines of code. See Study Drill #1.

# 3. Notice at the end of the What You Should See I used something called cat? It's an old command that "con*cat*enates" files together, but mostly it's just an easy way to print a file to the screen. Type man cat to read about it.
# cat -- concatenate and print files. DESCRIPTION: The cat utility reads files sequentially, writing them to the standardoutput.  The file operands are processed in command-line order.  If file is a single dash (`-') or absent, cat reads from the standard input.  If file is a UNIX domain socket, cat connects to it and then reads it until EOF.  This complements the UNIX domain binding capability available in inetd(8).

# 4. Find out why you had to write out_file.close() in the code.
# The variable out_file was created to open and write into the to_file. The out_file then needs to be closed out after it was written in.

# 5. Go read up on Python's import statement, and start python to try it out. Try importing some things and see if you can get it right. It's alright if you do not.
# Import statements are executed in two steps: (1) find a module, and initialize it if necessary; (2) define a name or names in the local namespace (of the scope where the ``import`` statement occurs). The statement comes in two forms differing on whether it uses the ``from``keyword. The first form (without ``from``) repeats these steps for each identifier in the list. The form with ``from`` performs step (1) once, and then performs step (2) repeatedly.