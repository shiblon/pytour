# vim:tw=50

"""Make Chart Data

Let's do something fun, now. We'll use the (now
deprecated, of course) Google Image Charts
to generate a graph from our smoothed data.

http://developers.google.com/chart/image/docs/data_formats

To do this, we'll have our Python code produce a
URL of a chart image.

Note that the code is shorter because date strings are
actually fine for our needs, the smoothing
implementation is folded into the parser, and some
well-placed comprehensions replace a few lines of
logic. It's a good idea to take some time to
understand the changes, particularly since some of
them are _bad exmaples_, in that they make clear
code much less clear by trying to do too much on
one line.

You are already equipped to understand all of it,
but may need a moment to noodle it all precisely
because these are examples of not-so-readable
Python. Remember when you code, you are writing
for a human audience as well as a computer.

To generate a chart URL, we need to provide values
in a comma-separated list with some additional
parameters. The basic parameters are provided
in the main() function, as are the basic data
lines.

Exercises

- Fill in the part marked TODO, then paste the URL
  into your browser.
"""

__doc__ = """Pass these tests:

>>> data = '''
... 2012-01-01 8.5
... 2012-01-02 8.4
... 2012-01-03 8.1
... 2012-01-04 8.3
... 2012-01-05 8.0
... 2012-01-06 7.9
... '''.split('\\n')
>>> make_chart_url_data(parsed_measurements(data))
'8.50,8.40,8.10,8.30,8.00,7.90|8.50,8.49,8.45,8.44,8.39,8.34'
"""

def make_chart_url_data(data):
  """Create chart URL data from (date, measurement, smoothed) triples."""
  # TODO:
  # Data format is n,n,n,n,n|n,n,n,n,n,n
  # Where | separates different plots, and 'n' is a
  # value within a plot.
  #
  # return two plot sequences, one for
  # measurements and the other for smoothed measurements.
  # Note that this will require storage of some kind.
  # You can either store the data as a list and iterate
  # over it twice, or you can incrementally create two
  # lists while iterating over it once.
  #
  # Note that you can assign some of the pieces of each
  # item to _ to show you are ignoring them.
  #
  # Make use of str.join (where the string is the
  # separator), e.g.,
  # ','.join("{0:.2f}.format(x) for x in some_sequence)
  # This joins the sequence in the argument with the
  # string on which join is called.


def parsed_measurements(lines):
  splits = ((d, float(w)) for d, w in (x.split() for x in clean_lines(lines)))
  d, w = next(splits)
  smoothed = w
  yield d, w, smoothed
  for d, w in splits:
    smoothed += 0.1 * (w - smoothed)
    yield d, w, smoothed


def clean_lines(lines):
  lines = (y for y in (x.strip() for x in lines) if y and y[0] != '#')
  last_line = ""
  for i, line in enumerate(lines):
    if line <= last_line:
      raise ValueError(
        "Non-incrementing (%d):\n\t%s\n\t%s" % (i+1, last_line, line))
    last_line = line
    yield line


if __name__ == '__main__':
  if not _testmod().failed:
    print "Success!"
  print ("http://chart.googleapis.com/chart?chs=320x200&cht=lc&chds=a&chd=t:" +
         make_chart_url_data(parsed_measurements(["2012-01-01 8.5",
                                                  "2012-01-02 8.1",
                                                  "2012-01-03 7.5",
                                                  "2012-01-04 8.0",
                                                  "2012-01-05 7.6",
                                                  "2012-01-06 7.7"])))
