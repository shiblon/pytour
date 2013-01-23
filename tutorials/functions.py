# vim:tw=50

"""Functions

We know how to call **functions** like |len| and
|bool| to get information about stuff, so now
we're going to learn how to write our own.

Functions are _defined_ using the |def| statement.
They have a name, a list of argument names in
parentheses, a colon, and are always followed by
an indented code block.

To **return** a value (or values) from a function,
you use the |return| statement. It can return any
kind of value, including tuples, which are
commonly used to return multiple values.

When |return| executes, the function terminates
immediately.

Exercises

- Put a |print| statement into the |swapped| function.
  Call it without assigning its result to anything.

- Change the |ordered| function to use |else|
  instead of relying on the early exit behavior of
  |return|.
"""
# A function that returns its two arguments
# swapped. Note that it returns two values by
# returning a tuple (parentheses optional).
#
def swapped(a, b):
  return b, a

# This one returns the arguments in order.
# Note how it uses the fact that "return" exits
# immediately to get its logic right.
#
def ordered(a, b):
  if a > b:
    return b, a
  return a, b

print "swapping", swapped(10, 20)
print "swapping", swapped('hello', 'aardvark')

print "ordering", ordered('more', 'less')
print "ordering", ordered((1,3,5), (1,2))

# When passing tuples *out* of a function, you can
# "unpack" them into new variables in one step.
x, y = swapped(1, 2)
print "unpacked", x, y

# Wait, why doesn't this work?
print "ordered, swapped", ordered(swapped(1, 2))
