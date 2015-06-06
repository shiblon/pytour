# vim:tw=50

"""Functions

We know how to call **functions** like |len| and
|bool| to get information about stuff, so now
we're going to learn how to write our own.

Functions are _defined_ using the |def| statement.
They have a name, a list of argument names in
parentheses, a colon, and are always followed by
an indented code block.

To **return** a value from a function, you use the
|return| statement. It can return any kind of
value, including tuples, which are commonly used
to package up and return multiple values.

It is important to note that all functions
return *exactly one value*. If you return multiple
things separated by commas, you are really
returning a single tuple of values. If you don't
return anything, you are implicitly returning the
value |None|. So remember: *functions always
return exactly one value*.

Also note that when |return| executes, the
function *terminates immediately*.

Remember how we talked about understanding a
function call by replacing it with the thing it
returns?See if you can predict what
|times3(times3(2))| becomes by doing the mental
replacement exercise we outlined earlier. The neat
thing is that this time, you can *see* what
|times3| returns because the definition of it is
right there in the code window. There is no need
to pretend.

Exercises

- Put a |print| statement into the |swapped| function.
  Call it without assigning its result to anything.

- Change the |ordered| function to use |else|
  instead of relying on the early exit behavior of
  |return|.

- Figure out why |swapped(swapped(1, 2))| does not
  work - do this by mentally performing replacement
  steps. HINT: every function always returns a
  single value, every time, no exceptions. When
  returning multiple values, the function is really
  returning a single tuple containing those values.
"""
# This is a basic function that accepts one
# argument and returns that argument times 3.
# As a *side effect*, it also prints what it is
# doing.
def times3(x):
  print "Hey - I'm multiplying {} by 3".format(x)
  return x * 3

# Now that times3 is defined, we can call it as
# much as we like:
print times3(12)
print times3(6)

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
