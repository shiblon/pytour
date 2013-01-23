# vim:tw=50

"""Module Docstrings

If the first statement in a file is a string,
Python uses it as documentation. This is called a
**docstring**.

Since documentation usually takes up more than one
line of text, these use the triple-quoting format
discussed earlier.

These strings are available to your program, but
more importantly, they can be used to produce
human-readable documentation for everything you
do. We'll make use of them throughout the rest of
the tutorial.

Exercises

- Try printing the special variable |__doc__|.
"""

__doc__ = """This is a module docstring.

A module is basically a file. All of the code in this
editor makes up a single module, a module that you
define by typing Python statements.
"""

print "This is a module - where's the documentation?"
