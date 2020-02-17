# vim:tw=50

"""Strings

Strings basically contain text.  They are
delimited, as was seen in the "Hello" example,
with quote marks.

There are four fundamental quote styles:

  "Double-quotes"

  'Single-quotes'

  ""\"Three double quotes make
  multi-line strings.""\"

  '''Three single quotes
  work the same way.'''

Exercises

- Run the program and note the indentation
  problem. Fix it.
"""

__doc__ = """Multi-line Strings

Such strings are often used to write documentation
for modules, functions, and classes.
"""

print('Single-quoted string.')  # single quotes work
print("Double-quoted string.")  # double quotes, too
print('''Multi-line strings may not do what you think,
         particularly with indentation.''')
