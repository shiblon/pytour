# vim:tw=50

"""Argument Unpacking

We saw when creating our own function that chaining
simple tuple-returning functions didn't work as
expected. Taking |ordered(swapped(...))| just doesn't
work, because |swapped| returns _one tuple_, and
|ordered| expects _two arguments_. To make the
call, you have to first unpack the result then
send its values separately.

You can do this with an **unpacking assignment**, like this:

  x, y = swapped(3, 6)
  print ordered(x, y)

Fortunately, there is another less cumbersome way
to do it that is more convenient. If you prefix
the argument with |*|, Python will unpack the
value into function arguments in one step:

  print ordered(*swapped(3, 6))

Exercises

- Try calling |ordered(*(3, 2, 1))|. What happens?
  Why?
"""

def swapped(a, b):
  return b, a

def ordered(a, b):
  if a > b:
    return b, a
  return a, b

# You can always do this via unpacking assignment:
x, y = swapped("hi", "there")
print ordered(x, y)

# But this is easier.
print ordered(*swapped(1, 5))

print swapped(*ordered(4, 2))
