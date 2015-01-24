# Chapter 8 Exercise

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I Had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
                   
# Chapter 8 Study Drills

# 1. Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.
# No mistakes made.

# 2. Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
# The third phrase has a single quote within the string, in the word didn't. So when the string prints, it will use a double quote to enclose the string resulting in "But it didn't sing.", whereas the other strings did not have single quotes within them, so they were enclosed by single quotes, instead of double. 