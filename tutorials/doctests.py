# vim:tw=50

"""Docstrings as Tests

With an understanding of docstrings, we can now
take advantage of a very cool facility in Python
called **doctests**.

Unit tests can be a real pain to write, because
you have to force yourself to switch gears when in
the code-writing zone. Doctests help to make it
easier to write simple tests _while you write
your documentation_.

The idea is simply this: you write, inside of the
docstring, a short "interpreter session": you
write down something that you could type in the
interactive interpreter, followed by the results
you would see after it executes. You can then
easily test whether that actually happens or not.

Doctests are run by importing |doctest| and
running |doctest.testmod()|.

We'll use doctests for the rest of the tutorials
to help with the exercises and to show how things
work.

Exercises

- Make |less_than_five| pass by making its
  implementation match its documentation.

- Make the module doctest fail. You can do
  anything (like saying that |True| produces
  |False|).
"""

__doc__ = """A testable module.

What follows is a doctest. We basically mimic the
Python interactive interpreter prompts >>> and ..., and
show expected output below them.

>>> less_than_five(3)
True
"""

def less_than_five(a):
  """Return True if a < 5.

  >>> less_than_five(10)
  False
  >>> less_than_five(5)
  False
  >>> less_than_five(2)
  True
  """
  return a <= 5

# Actually run the doctests:
print "Running tests - no news is good news:"

import doctest
doctest.testmod()
