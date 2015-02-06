# Chapter 21 Exercise

def add(a, b):
    print"ADDING %d + %d" % (a, b)
    return a + b

def subract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a-b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just fuctions!"

age = add(30, 5)
height = subract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Chapter 21 Study Drills

# If you aren't really sure what return does, try writing a few of your own functions and have them return some values. You can return anything that you can put to the right of an =.

trying_this = multiply(9, 9)
print "My example should return %d." % trying_this
