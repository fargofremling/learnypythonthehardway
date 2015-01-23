# Chapter 6 Exercise

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e


# Chapter 6 Study Drills

# 1. Go through this program and write a comment above each line explaining it.
# 2. Find all the places where a string is put inside a string. There are four places.

# Establishes the variable x, which includes a string and a format character, %d.
x = "There are %d types of people." % 10
# Makes the variable binary = binary.
binary = "binary"
# Established the variable do_not to equal the string "don't".
do_not = "don't"
# Establishes the variable y, which includes a string and two format characters, %s. This represents two instances of string ('binary' and 'don't') inside of a string.
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the variable x.
print x
# Prints the variable y.
print y

# Prints a string with a format character %r, which is the variable x. This is an instance of a string being inside a string.
print "I said: %r." % x
# Prints a string with a format character %s, which is the variable y. This is an instance of a string being inside a string.
print "I also said: '%s'." % y

# Establishes that hilarious equals false.
hilarious = False
# Establishes the variable joke_evaluation is a string that contains a format character of
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints both the variables, which are strings.
print joke_evaluation % hilarious

# Establishes the variable w as a string.
w = "This is the left side of..."
# Establishes the variable w as a string.
e = "a string with a right side."

# Prints both strings.
print w + e


# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# Yes, I'm certain there are four places when a string is inside of a string. However,two of those place happen to be within the same string (see line 37).

# 4. Explain why adding the two strings w and e with + makes a longer string.
# In this case, it isn't really adding two strings. Instead, it is adding two variables, which both happen to be strings. With the print command, it's as if the + sign literally acts as a silent 'and'.