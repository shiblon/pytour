# vim:tw=50

"""Exercise: Functions and If (1)

Now we have enough tools to do something more
interesting! Let's remind ourselves of how |if|
and **slicing** work.

For this and later exercises, you will fill in the
code marked |# TODO:| to make the doctests pass.
Remember that you can use |[::-1]| to get a
reversed sequence using a slice.

First try running the code without changes. What
fails?

Exercises

- Write the body for the function |reverse_a| by
  replacing the |TODO| comment with real code. If
  the string |s| starts with the letter |"a"|,
  return it reversed. Otherwise return it
  unchanged. You may want to use
  |s.startswith('a')| instead of |s[0] == 'a'| so
  that the function will also work on empty
  strings.
"""

__doc__ = """Functions and branching exercise (1)

Make these tests pass:

>>> reverse_a("a silly thing")
'gniht yllis a'

>>> reverse_a("not so silly")
'not so silly'

>>> reverse_a("")
''
"""

def reverse_a(s):
  """Return s reversed if it starts with a, not reversed otherwise."""
  # TODO: Fill this in.


if _testmod().failed == 0:
  print "Success!"
