# vim:tw=50

"""Argument Packing

You can _unpack_ sequences into arguments when you
call functions, e.g., |ordered(*(3, 1))|, but you
can _also_ define functions to accept **packed
arguments** in a tuple.

Take a look at |star_ordered| and |star_mixed|,
for example. Here we use the |*| notation to
indicate that we want to receive all of the
unnamed arguments as a tuple.

When you accept |*args| (or |*whatever|), you can
place it at the end of a regular argument list, as
shown in the accompanying |mixed_args|. It cannot
be followed by regular arguments.

Exercises

- Try calling |star_ordered| with more than 2 arguments.
  What happens?

- The builtin |min| function returns either the
  smallest of its arguments or the smallest item
  in a sequence, depending on how it is called.
  Implement your own |myMax| function that works
  similarly, but returns the largest item.

- Play around with |sorted|. See what happens when
  you pass it a string, or a tuple, or a list.
"""

# Here, '*args' means "take all arguments and
# stick them into the 'args' tuple in order".
#
# Also, 'sorted' is a handy function - it takes
# any sequence and returns a sorted list.
#
def star_ordered(*args):
  return sorted(args)

print "ordered:", star_ordered(6, 3)

# You can mix regular and star parameters, if the
# star ones come last.
#
def star_mixed(a, b, *others):
  print a, b, others

# Note how the arguments are printed.
star_mixed("hi", "there,", "what's", "your", "name?")
