# Chapter 10 Exercise

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass

"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Here's a tiny piece of fun code to try out:

# while True:
# for i in ["/","-","|","\\","|"]:
# print "%s\r" % i,

# This "tiny piece of fun code", put the terminal in a infinate loop state, hence commenting it out.


# Chapter 10 Study Drills

# 1. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    
    '''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# A single-triple-quote seems to function the same way as the single-double-quote.

# 2. Combine escape sequences and format strings to create a more complex format.

print "Are you my mother? \nYou\'re not my mothers!"
print "What does this one \fdo?"
print "What about \f now?"
print "Wow, look at that! What does this one \bdo?"
print "Oh, it is a backspace and deletes the space. And \athis versus \a this."
print "Neato! I made the computer make a sound. Do it again! \a"

# 3. Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?

lyric = "Don\'t"

print "%r stop thinking about tomorrow!" % lyric
print "%s stop thinking about tomorrow!" % lyric

#  %r is printing out the raw representation of what was typed, which is going to include the original escape sequences. Remember %r is for debugging, %s is for displaying.
