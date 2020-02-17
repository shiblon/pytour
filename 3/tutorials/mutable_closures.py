# vim:tw=50

"""Mutable Closure Variables

This is fairly advanced, and might take a little
bit of head scratching to understand. Take your
time, it's worth it. If you can understand what
this code is doing, then you definitely understand
scoping in Python.

Let's use our new smoothing generator to change
all of our |(date, measurement)| pairs into
|(date, measurement, smoothed)| triples.

Again, we will use a generator. Yes, they are that
useful. You will therefore see them everywhere you
look, including where there are no generators.
They are like Python's hammer - now go find a
nail.

A quick note: the test for monotonicity
(increasing dates) has been folded into the
clean_lines function. Take a look if you're
interested: this works because dates of the form
yyyy-mm-dd sort properly as strings.

Exercises

- Implement the smoothed_data function (see
  |TODO|) to accept an iterable over (date,
  measurement) pairs, and produce a (date,
  measurement, smoothed) triple for each one.

Note: this is not simple, because the smoothing
generator only expects an iterable over raw data.
We could just change parsed_measurements to emit
triples, but this will provide good closure
practice.

Hint: What happens to the old date and measurement
values at each iteration through the loop? Can you
use them outside?
"""

__doc__ = """Augmenting data smoother.

Here's the test to make pass:
>>> lines = '''
... 2012-01-01 7.6
... 2012-01-02 7.7
... 2012-01-03 7.5
... 2012-01-04 7.3
... 2012-01-05 7.4
... '''.split('\\n')
>>> for triple in smoothed_data(parsed_measurements(lines)):
...   print [str(x) for x in triple]
['2012-01-01 00:00:00', '7.6', '7.6']
['2012-01-02 00:00:00', '7.7', '7.61']
['2012-01-03 00:00:00', '7.5', '7.599']
['2012-01-04 00:00:00', '7.3', '7.5691']
['2012-01-05 00:00:00', '7.4', '7.55219']
"""

import datetime

def smoothed_data(pairs):
  """Accepts pairs of values and produces an iterator over triples."""
  last_values = [None, None]

  def saved_values_iter():
    for d, w in pairs:
      last_values[:] = [d, w]  # Save current data in outer scope before yield.
      yield w

  for smoothed in exponentially_smoothed(saved_values_iter()):
    # TODO:
    # Replace the yield below with a proper
    # implementation. The goal is to yield date,
    # measurement, and smoothed all at the same time.
    # But as we consume the exponentially_smoothed
    # iterator, it also consumes the
    # saved_values_iterator, so we have to get
    # date and measurement from somewhere else...
    yield None, None, None


def exponentially_smoothed(numbers):
  it = iter(numbers)
  smoothed = next(it)
  yield smoothed
  for n in it:
    smoothed += 0.1 * (n - smoothed)
    yield smoothed


def parsed_measurements(lines):
  for line in clean_lines(lines):
    d, w = line.split()
    yield datetime.datetime.strptime(d, '%Y-%m-%d'), float(w)


def clean_lines(lines):
  last_date = ""
  for i, line in enumerate(lines):
    line = line.strip()
    if not line or line.startswith('#'):
      continue
    date = line.split()[0]
    if date <= last_date:
      raise ValueError(
        "Non-incrementing (%d):\n\t%s\n\t%s" % (i, last_line, line))
    last_date = date
    yield line


if __name__ == '__main__':
  if not _testmod().failed:
    print "Success!"
