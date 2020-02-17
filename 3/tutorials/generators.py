# vim:tw=50

"""Generators

It's head-exploding time!

We recently wrote a function that, given lines
with dates and measurements, splits them up,
makes sure they only move forward, and prints them
out.

Printing is nice, but not impressively useful or
exciting. We want to _transform_ this data
(eventually into a chart), not just output it.

Instead of printing, the function can be made more
generally useful by returning a list. In fact,
that's what we've done here. Take a look and see
what it's doing. Keep in mind that in order to do
this, even though the file is read incrementally,
and the consumer may only need things one at a
time, the entire dataset must be in memory for
this to work.

Let's fix that using one of Python's more powerful
and elegant constructs: the **iterator generator**.
By placing a "yield" keyword in the function, the
function is changed to not merely return a single
value, but to return an _iterable_ that can
produce _all yielded values_ one at a time, when
asked. Recall that |for| loops work with
iterables, as does the |list| builtin.

Exercises

- Replace the code as described in the TODO
  sections and see how it works (and notice that
  we changed the name of the function to reflect
  what it returns).

- Write a |for| loop in the main code (replace the
  use of |_testmod| if you want) that
  outputs the result of |parsed_measurements(...)|
  with some lines of your own.
"""

__doc__ = """Some notes on 'parsed_measurements'.

This passes right now. Your job is to convert the
function to a generator and keep it passing.
"""


def parsed_measurements(lines):
  # TODO:
  # Remove this values list. Just kill it.
  values = []
  last_date = ""  # less than all other strings
  for line in lines:
    line = line.strip()
    if not line or line.startswith('#'):
      continue

    date, measurement = line.split()
    if date <= last_date:
      raise ValueError("Non-increasing: %s -> %s" % (last_date, date))

    # TODO:
    # Replace this line with
    #   yield date, measurement
    # And remove the return statement completely.
    # Then step back, run it, and see if you can figure
    # out what is going on.
    values.append((date, measurement))
  return values


if __name__ == '__main__':
  _assert_equal([('2012-10-10', '5.4'), ('2012-10-11', '5.3')],
                list(parsed_measurements(['2012-10-10 5.4',
                                          '2012-10-11 5.3'])))
