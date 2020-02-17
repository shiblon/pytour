# vim:tw=50

"""Histograms and Dictionaries

Suppose we want to know how often the measurement
changed in one direction or another. Let's use a
dictionary. Dictionaries are good for this because
you don't have to know what keys they'll have
before you start. With a list, you do (unless
you're just appending).

We'll take the change in measurement as the key to the
dictionary, and the value will be the number of times
we've seen that change.

A couple of quick reminders: you will need to use
|in| or |not in| to check for the key's existence
before you can get its value to increment it. If
it isn't there, you store it, otherwise you add
one to it.

You will also want to use the |abs| builtin to compute
the absolute value of things (since we don't care
whether the difference is up or down for this
application).

Exercises

- Your job is to fill in the implementation. Keys
  should be in |%.2f| (or |{:.2f}|) format, and
  values are the number of times we've seen the
  key (the absolute difference between adjacent
  measurements).

Bonus Work

- Look up |collections.defaultdict| and use that instead
  to save yourself some code.
"""

__doc__ = """Histogram example.

Measurements are just floating point values. Truncate
differences to at most 2 decimal places. Use the
absolute value of the difference between adjacent
values.

>>> h = histogram([8.0, 8.2, 7.8, 7.9, 8.0, 7.7, 7.9, 7.6])
>>> print "\\n".join("%r: %r" % (k, v) for k, v in sorted(h.iteritems()))
'0.10': 2
'0.20': 2
'0.30': 2
'0.40': 1
"""

def histogram(data):
  """Given an iterable over measurements, produce a difference histogram."""
  # TODO: Implement this, returning a dictionary
  # keyed on strings representing the absolute
  # difference between adjacent measurements. The
  # strings should be formatted {:.2f} as in the
  # doctest above.


if __name__ == '__main__':
  if not _testmod().failed:
    print "Success!"
