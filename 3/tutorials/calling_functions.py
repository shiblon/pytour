# vim:tw=50

"""Calling Functions

Python has a lot of stuff built in that you can
just use. Much of it is exposed through **functions**.
You have already seen a common one: |print|.

A function is _called_ by placing |()| after its
name. If it accepts **arguments**, then they go
inside of the |()|. The |len| function
demonstrated here accepts a single argument: the
thing you want to know the length of.

  x = len("hello")  # x gets the value 5

All Python functions **return a value**. In the
case of |len|, this means that calling it produces
a new value as above. You can assign that value to
a variable, or print it, or pass it into another
function. Or, you can ignore it and it will go
away.

To understand how function calls work, it helps
to think of calling a function as *replacing it
with the return value*. In the example above, that
means that the entire call, from the name |len| to
the closing paren, is replaced with the length of
"hello", which is 5.

When you see a function call anywhere and want to
understand what it means, you can imagine working
from the inside out, left to right, replacing
calls with the values they return.

  x = len([1, 2, len('hi')])
  # innermost is len('hi') - replace it:

  x = len([1, 2, 2])
  # next is len([1, 2, 2]) - replace it:

  x = 3
  # No more calls - we're done.

If you ever see a statement or expression that has
function calls in it, you can understand what is
going on by following the above procedure in your
mind: replace the innermost, calls with values
(they can be pretend values - we're imagining for
the sake of understanding, here). Then work to the
right, then work outward and do it again until
there are no calls left.

Functions are very important in all of computer
science, so taking the time to understand what is
happening right now is very useful for what's
coming up.

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
print("length =", length)

# We can print it directly, too.
print("The length is", len("hi there"))

# The repr function can be useful to see what's
# really in a string. It adds quotes for you.
print("Just print:", "Hi there")
print("repr print:", repr("Hi there"))
