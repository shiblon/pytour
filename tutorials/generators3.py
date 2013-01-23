# vim:tw=50

"""Generators for Refactoring

Now that we know how to make our own generators,
let's do some refactoring to make use of this idea
and clean up the code a bit. We'll start by
splitting out the |clean_lines| function, which
basically just skips blank lines and comments,
stripping unnecessary space.

This notion of converting one iterator into
another is prevalent in Python. As one rather
common example, the |enumerate| builtin converts
an iterable over items into an iterable over
|(index,item)| pairs. You built something similar
earlier.

Generators make refactoring sequence operations
really easy, even operations that need to remember
something about past elements. Without them,
separating functionality like this would be hard
or sometimes even impossible.

Exercises

- Look carefully at "clean_lines" and make sure
  you understand how it works.

- Use "enumerate" to get line numbers with the
  data, and emit that line number in the
  ValueError message. Note that in string
  formatting, {0} means "the first argument". You
  can put any number in there, so long as it
  matches the position of what you pass to
  |format|. So, you could use |{2}| for the line
  number if you want.
"""

__doc__ = """Refactoring functionality.

Changes: we now clean out comments and blank lines
in a different function, and the error message for
bad dates has the line number in it.

>>> list(parsed_measurements(['2012-10-10 5.4', '2012-10-11 5.3']))
[('2012-10-10', '5.4'), ('2012-10-11', '5.3')]
>>> list(parsed_measurements(['2012-10-10 5.4', '2012-10-09 5.3']))
Traceback (most recent call last):
...
ValueError: Non-increasing (2): 2012-10-10 -> 2012-10-09
"""

def clean_lines(lines):
  for line in lines:
    line = line.strip()
    if not line or line.startswith('#'):
      continue
    yield line


def parsed_measurements(lines):
  last_date = ""
  # TODO:
  # Use 'enumerate(clean_lines(lines))' to get
  # (number, line) pairs. Use the number in the
  # exception message to show on what line the
  # error occurred.
  for line in clean_lines(lines):
    date, measurement = line.split()
    if date <= last_date:
      raise ValueError("Non-increasing: {0} -> {1}".format(
        last_date, date))
    last_date = date
    yield date, measurement


if __name__ == '__main__':
  import doctest
  if not doctest.testmod().failed:
    print "Success!"
