# vim:tw=50

"""Exercise: Recursion (1)

Recursion is a pretty powerful idea. You can do a
lot with it. In fact, you can do so much with it
that some languages (not Python) use it as their
main way of getting things done.

Now you get to practice the idea of recusion with
a simple problem. Before starting, though,
remember these things:

- Start with a *very easy* version of the problem.
  When do you know the answer without having to
  think about it? Write that down first and test
  it.

- Then consider a slightly bigger version of the
  problem. How can you make it a bit smaller and
  use that to get the answer?

You'll get lots of help on this one, so don't
worry.

Exercises

- Write the |add_all| function as described in the
  docstring and its tests. A good base case for
  this is an empty list, which would have a sum of
  |0|. This is outlined in the first |TODO|.

- Now write the recursion. You can use a slice to
  peel off one value and add it to the sum of _the
  rest of the list_. This is outlined in the
  second |TODO|.
"""

__doc__ = """Sum a List With Recursion

>>> add_all([])
0

>>> add_all([1])
1

>>> add_all([3, 4])
7

>>> add_all(range(1, 11))
55
"""

def add_all(seq):
  """Add all elements of a list."""
  # TODO: Write a base case: return 0 if the list
  # is empty. Recall that empty == False in if
  # statements. Or you can test for len(seq) == 0.
  #
  # TODO: Write the recursion. You can either take
  # an element from the front of the list (seq[0])
  # and add it to add_all of the rest, or you can
  # take one from the back (seq[-1]) and add it to
  # the rest, like this:
  # return seq[-1] + add_all(seq[:-1])


import doctest
if doctest.testmod().failed == 0:
  print "Success!"
