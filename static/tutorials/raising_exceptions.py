# vim:tw=50

"""Raising Exceptions

We want to build a basic tracker that can plot
data in a nice chart. The exercises are going to
be getting a bit longer, now.

The format that we expect is a file of lines
containing universal (and sortable) date strings,
and a floating point measurement after some space,
as shown in the accompanying code documentation.

We will write a function that takes a file-like
object and produces a list of (date, measurement)
string pairs. If the dates are out of order, it
will **raise** a builtin |ValueError|
**exception**.

This part is new: exceptions are, kind of like
|return|, a way of exiting a function early. But
unlike |return|, they exit *all calling functions,
too*, until the program terminates or the
exception is explicitly handled. They are for
"exceptional" cases, like errors when you can't
really recover because the problem is elsewhere.

We'll get more into them later. For now, the idea
is to use the |raise| keyword, then pass a message
using the |ValueError| exception, which is, of
course, callable.

Exercises

- Fill in the parts marked |# TODO| in the
  parse_measurements function. The description of
  what to do is there. You can test it by running
  it (which executes the doctest at the top of the
  module).
"""

__doc__ = """Parse dates, ensure monotonicity.

We parse this format of "date measurement" entries, ensuring
that the dates are in strictly ascending order.

  2012-11-10 9.6
  2012-11-11 9.5
  2012-11-12 9.4
  2012-11-13 9.1

Blank lines and comment lines are also allowed. See the tests here.

>>> parse_measurements(['  2012-10-10 5.4 \\n',
...                     ' # comment!\\n',
...                     '2012-10-11 5.3'])
['2012-10-10', '5.4']
['2012-10-11', '5.3']
>>> parse_measurements(['2012-10-10 5.4', '2012-10-09 5.3'])
Traceback (most recent call last):
...
ValueError: Non-increasing dates: 2012-10-10 -> 2012-10-09
"""

def parse_measurements(lines):
  """Parse date-measurement entries from lines. See docs above."""
  last_date = ""  # less than all other strings
  for line in lines:
    # TODO:
    # - Strip each line (using line = line.strip())
    # - Skip blanks (continue if not line)
    # - Skip comments (continue if line.startswith('#'))
    # - Use 'split' and unpack into date and measurement
    # - If the date is not greater than the
    #   previously-read date, raise ValueError as shown
    #   in the commented-out code here:
    #
    # raise ValueError(
    #     "Non-increasing dates: %s -> %s" % (last_date, date))
    #
    # - Don't forget to set last_date down at the
    #   bottom, here! (last_date = date).

    print [date, measurement]


if __name__ == '__main__':
  import doctest
  if doctest.testmod().failed == 0:
    print "Success!"
