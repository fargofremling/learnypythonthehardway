ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# The split() function called on the string "ten_things" uses the " " as the delimit
# (read: boundary) for separating out the times within the string.
# It also creates a list called "stuff". 
stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# The len() [length] function is being called on the "stuff" list, which determines how many 
# items are in the list.
while len(stuff) != 10:
    
    # The pop() function is being called on the list "more_stuff", which calls up the 
    # last item [-1] in the list and removes it.
    next_one = more_stuff.pop()
    
    print "Adding: ", next_one
    
    # The append() function is being called on the stuff list, which adds a new item
    # to the stuff list. 
    stuff.append(next_one)
    
    # The len() [length] function is being called on the "stuff" list again , which 
    # determines how many items are now in the list.
    print "There are %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy

# The pop() function is being called on the list "mstuff", which calls up the 
# last item in the list [-1] and removes it. In this case, it is corn.
print stuff.pop()

# The join() function is being called with the argument list "stuff" with the iterable
# of " ". This is basically the opposite functionality of the split() function.
print ' '.join(stuff) # what? cool!

# The join() function is being called with the argument list "stuff" and indices 3 and 5 
# with the iterable of "#". 
# This joins the 4th and 6th items in the list with the "#" in between."
print '#'.join(stuff[3:5]) # super stellar!