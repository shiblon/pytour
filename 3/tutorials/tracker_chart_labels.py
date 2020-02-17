# vim:tw=50

"""Chart Date Labels

There are no labels on our chart, just lines.
Let's add some labels. This will give us a chance
to use regular expressions a bit to parse our date
strings.

We'll just omit the year and month, placing only the
day on the chart. We will also send a parameter asking
the chart service to supply its own y-axis labels.

A regular expression that you might try is
'^\d+-\d+-', which matches the first two date
components in a string. If you |sub| that with the
empty string, you'll be left with just the last
part: the day.

The above expression works because |'\d'| matches
any digit, |'+'| means "one or more of the
preceding", and |'^'| matches the beginning of the
string. The |'-'| just matches itself.

See http://docs.python.org/2/library/re.html for more details.

Exercises

- Fill in the bit marked |TODO|: get the day out
  of the each date string with a regular
  expression, then join all of the days together
  as specified, with the ||| character. Don't
  forget the URL parameters! The test will pass
  when you have it all right. Try running it first
  to get an idea of what's expected.
"""

__doc__ = """Make this test pass:

>>> data = '''
... 2012-01-01 8.5
... 2012-01-02 8.4
... 2012-01-03 8.1
... 2012-01-04 8.3
... 2012-01-05 8.0
... 2012-01-06 7.9
... '''.split('\\n')
>>> print '\\n'.join(make_chart_url_data(parsed_measurements(data)))
chd=t:8.50,8.40,8.10,8.30,8.00,7.90|8.50,8.49,8.45,8.44,8.39,8.34
chxt=x,y&chxl=0:|01|02|03|04|05|06|
"""

import re

def make_chart_url_data(data):
  """Create chart URL data from (date, measurements, smoothed) triples.

  Returns:
    (data_string, label_string)
  """
  data = list(data)
  datastr = 'chd=t:' + (','.join('%.2f' % x for _, x, _ in data) +
                        '|' +
                        ','.join('%.2f' % x for _, _, x in data))

  # TODO: Let's generate some labels!
  #
  # The label format is
  # "chxt=x&chxl=0:|label|label|...|" Assign the
  # appropriate string to the "labelstr" variable.
  # Use a regular expression to "sub" the year and
  # month away, generating a string with only the
  # day. If you do that inside of a comprehension
  # of some kind, you can then use join to get the
  # | delimiters in there.
  labelstr = ''

  return datastr, labelstr

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
  print ("http://chart.googleapis.com/chart?chs=320x200&cht=lc&chds=a&" +
         "&".join(make_chart_url_data(parsed_measurements(["2012-01-01 8.5",
                                                           "2012-01-02 8.1",
                                                           "2012-01-03 7.5",
                                                           "2012-01-04 8.0",
                                                           "2012-01-05 7.6",
                                                           "2012-01-06 7.7"]))))
