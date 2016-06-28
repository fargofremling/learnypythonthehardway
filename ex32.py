# Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# Study Drills
# 1. Take a look at how you used range. Look up the range function to understand it.
# - The range function -- range(start, stop[, step]) -- is used to create lists that 
#   contain arithmetic progressions. It typically used with for loops. 
#   The arguments can only be integers. If the step argument is omitted, it defaults to 1.
#   If the start argument is omitted, it defaults to 0.
# 2. Could you have avoided that for-loop entirely on line 22 and just assigned
#    range(0,6) directly to elements?
# - I don't think so. Based on the answer above, the range function is generally used with 
#   with a for loop. I'm not sure how one would use it without a for loop.
# 3. Find the Python documentation on lists and read about them. What other operations 
#   can you do to lists besides append?
# - More on lists: https://docs.python.org/3/tutorial/datastructures.html
# - .append(x)
# - .extend(x)
# - .insert(i, x)
# - .remove(x)
# - .pop([i])
# - .clear()
# - .index(x)
# - .count(x)
# - .sort(key=None, reverse=False)
# - .reverse()
# - .copy()

# Fun Fact
# A for-loop is able to use a variable that isn't defined yet.
# The variable is defined by the for-loop when it starts, initializing it to the current 
# element of the loop iteration, each time through.