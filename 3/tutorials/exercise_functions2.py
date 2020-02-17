# vim:tw=50

"""Exercise: Functions and If (2)

For this exercise, you get to write the whole
function out, including the name and arguments.
Docstrings are optional, but will produce more
bonus points, wherever you go to get them.
Somewhere other than here.

Exercises

- Write a function |every_other_arg| that accepts
  any number of arguments and returns a list
  containg every other one. Recall that |[::2]|
  will produce every other element of a sequence,
  and |*args| will collect all function arguments
  into a single tuple.
"""

__doc__ = """More Practice with Functions and Branching.
"""

# TODO: write the every_other_arg function to pass
# the tests below.

_assert_equal((0, 2, 4, 6), every_other_arg(0, 1, 2, 3, 4, 5, 6))
_assert_equal((), every_other_arg())
_assert_equal(('goodnight', 'my', 'someone'),
              every_other_arg('goodnight', 0, 'my', 1, 'someone'))
