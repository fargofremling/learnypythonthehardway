# Chapter 14 Exercise

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
    Alright, so you said %r about liking me.
    You live in %r. Not sure where that is.
    And you have a %r computer. Nice.
""" % (likes, lives, computer)


# Chapter 14 Study Drills


# 1. Find out what Zork and Adventure were. Try to find a copy and play it.

# Zork is one of the earliest interactive fiction computer games.

# A modern replica of the original game can be found here: http://www.web-adventures.org/cgi-bin/webfrotz?s=ZorkDungeon


# 2. Change the prompt variable to something else entirely.


from sys import argv

script, user_name = argv
cat = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(cat)

print "Where do you live, %s?" % user_name
lives = raw_input(cat)

print "What kind of computer do you have?"
computer = raw_input(cat)

print """
    Alright, so you said %r about liking me.
    You live in %r. Not sure where that is.
    And you have a %r computer. Nice.
    """ % (likes, lives, computer)

# 3. Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.

# I had to comment out this section of the code below, otherwise it would break the earlier portions of the code.


# from sys import argv

# script, cat, user_name = argv
# prompt = '> '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me, %s?" % user_name
# likes = raw_input(prompt)

# print "Where do you live, %s?" % user_name
# lives = raw_input(prompt)

# print "What kind of computer do you have?"
# computer = raw_input(prompt)

# print """
    # Alright, so you said %r about liking me.
    # You live in %r. Not sure where that is.
    # And you have a %r computer. Nice.
    # """ % (likes, lives, computer)



# 4. Make sure you understand how I combined a """ style multiline string with the % format activator as the last print.

# Since the """ form a block string, it makes sense to have the definition of the format character after the close of the block string (i.e. paragraph).