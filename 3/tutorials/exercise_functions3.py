# vim:tw=50

"""Exercise: Functions and If (3)

This time we'll use the |sorted| builtin function,
along with some slicing and |if| statement work,
to make the tests pass.

First, a couple of reminders are in order:

- |sorted| accepts a sequence and returns a sorted
  list.

- Lists can be joined together using |+|, like
  this: |[1, 2] + [3, 4]|.

- Slices can use negative values to indicate
  "distance from the right side", like this: |(0,
  1, 2, 3)[-2:]|, which produces the last two
  elements |(2, 3)| (it means "start at 2 from the
  right and take everything from there"). You may
  want to review slices quickly before diving in.

- The length of a sequence is obtained with |len|.

Exercise

- Write the |kind_of_sorted| function and make the
  tests pass. It accepts one argument: a list, and
  returns that list with _all but the first two
  and last two elements sorted_. The first two and
  last two elements should remain in the same
  place. Hint: what should happen when the list is
  small or empty? How small?

"""

__doc__ = """Kind of Sorted

Write the kind_of_sorted function to pass the tests.
"""


def kind_of_sorted(seq):
  """Sort all but the first two and last two elements."""
  # TODO: Fill this in.


_assert_equal([8,7,2,3,4,5,6,1,0],
              kind_of_sorted([8,7,6,5,4,3,2,1,0]))
_assert_equal([5,4,3,2,1],
              kind_of_sorted([5,4,3,2,1]))
_assert_equal('araginote',
              ''.join(kind_of_sorted(list("aragonite"))))
