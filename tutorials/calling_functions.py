# vim:tw=50

"""Calling Functions

Python has a lot of stuff built in that you can
just use. Much of it is exposed through **function
calls**.

A function is called by placing |()| after its
name. If it accepts **arguments**, then they go
inside of the |()|. The |len| function
demonstrated here accepts a single argument: the
thing you want to know the length of.

All Python functions **return a value**. In the
case of |len|, this means that calling it produces
a new value. You can assign that value to a
variable, or print it, or pass it into another
function. Or, you can ignore it and it will go
away.

Exercises

- One important function in Python is |repr|,
  which prints a "representation" of an object.
  Try printing |repr("10")|. See how it differs
  from |repr(10)|.

- Convert the string |"2000"| into an integer
  by calling |int|.
"""

__doc__ = """Calling Functions

Note: If you don't use a return value,
it gets lost.
"""

# Call 'len', ignore (and lose) its value.
len("hi")

# Assign 'length' to the return value of 'len'.
length = len("how long is this anyway?")
print "length =", length

# We can print it directly, too.
print "The length is", len("hi there")

# The repr function can be useful to see what's
# really in a string. It adds quotes for you.
print "Just print:", "Hi there"
print "repr print:", repr("Hi there")
