# vim:tw=50

"""Smoothing Generator

Anyone who has weighed their kitten will know that
weight fluctuates from day to day. What you really
want to know is whether the overall trend is good,
not whether there has been more or less (to put it
delicately) water output that day. You want the
trend smoothed out over time.

Your task: fill in the part marked |TODO| to do
this smoothing without any |if| statements inside
of loops.

To accomplish this, we will again use a generator.
This one will accept an iterable of floating point
values and produce smoothed floating point values
in return. We're doing this sort of in a vacuum,
not taking the nature of our full date-endowed
data into account. We'll run into that again
later.

Meanwhile, there's a nifty new concept hiding out
in the code's doctest: _list comprehensions_. The
gist: you can embed |for| syntax directly into
list construction. Try to understand the
comprehension in the docstring after you finish
the exercise. We'll talk more about it later.

Exercises

- Fill in the part marked |TODO| by following the
  instructions in the comments. Try _not_ to use |if|
  to test for the first run through the loop.
"""

__doc__ = """Smoothing using a generator.

"exponentially_smoothed" applies exponential
smoothing to values. The first smoothed value is
just the value itself. After that, each smoothed
value is calculated to be 10% of the distance to
the new value.

>>> values = [8.2, 8.1, 8.0, 7.8, 7.9, 8.0, 7.5]
>>> ["{0:.2f}".format(x) for x in exponentially_smoothed(values)]
['8.20', '8.19', '8.17', '8.13', '8.11', '8.10', '8.04']
"""

def exponentially_smoothed(numbers):
  """Generate a smoothed sequence for the given numbers.
  """
  # TODO:
  # Fill in the implementation: yield the first value
  # directly, then compute smoothed values by adding
  # 10% of the difference between the current
  # measurement and the previous smoothed value, thus:
  # smoothed += 0.1 * (value - smoothed)


if __name__ == '__main__':
  if not _testmod().failed:
    print "Success!"
