# vim:tw=50

"""Docstrings

Now that we have defined our own functions, it
makes sense to talk about how to document them
properly.  Earlier, it was briefly mentioned that
comments are not the favored tool for creating
documentation in Python: **docstrings** are.

A string becomes a docstring when it is the first
statement in a module, class, or function, simply
by virtue of its position. It does not need to be
assigned to anything.

The |pydoc| utility and |help| function each
format these docstrings and display them when
requested.

At the command line, for example, you can type

  pydoc list

And get a nice help page made up mostly of module
docstrings.

In this interactive tutorial, you can instead call
|help()| at the bottom of the code to see
something similar in the output window.

Exercises:

- Try running |help()|.

- Try running |help(a_complex_function)|.
"""

__doc__ = """Short description of the module.

A longer description of the module. This docstring can
be accessed in the module-global __doc__ variable.
"""

def a_complex_function(a, b, c):
  """Do a complex operation on a, b, and c.

  This will do amazing things with a, b, and c. Just watch.

  Args:
    a: A boolean value (see above).
    b: A boolean value (again, see above).
    c: A sequence.

  Returns:
    Nothing - awesomeness needs no return value.
  """
  print "Shhh: it's actually not all that complex:"
  print a, b, c
  # No return statement, or an empty return statement,
  # will implicitly return None.

print "Result of a complex function:"
print a_complex_function(True, False, [1,2,3,4])

print "The module docstring:"
print __doc__

print "The function docstring:"
print a_complex_function.__doc__
