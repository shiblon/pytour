# vim:tw=50

"""Real Dates, and Strings to Numbers

So far we have done everything with strings. Now
it's time to start using more interesting and
appropriate objects. We can't very well do math
with strings, after all. And, we might want to
manipulate our dates in more meaningful ways than
strings will allow, like outputting alternate date
formats.

Take a look at the doctest for
|parsed_measurements|. It shows how we should be
able to emit European date formats once we're
done.

We'll convert strings to numbers using |float|,
and strings to dates using the |datetime| module.

Note that |strptime| means "parse this string into
a |datetime|" and |strftime| means "format this
|datetime| into a string". The ugly names are
historical and therefore traditional and sacred.

By the way, we have also started using **named
substitutions** in |str.format|. Check it out.

Exercises

- Fill in the part marked |# TODO|, making
  |measurement| into a float, and |date| into a
  |datetime| object.

Bonus Work

- Convert the final object into a |date| instead
  of a |datetime|, since it doesn't have a time
  component anyway. You may want to look at the
  help for |datetime.datetime|.
"""

__doc__ = """Convert lines 'date measurement' into pairs."""

# Not a module, but seriously? Who wants to type
# "datetime.datetime.stuff" all the time?
# Sometimes breaking the rules makes sense. :-)
from datetime import datetime


def parsed_measurements(lines):
  last_date = ""
  for i, line in enumerate(clean_lines(lines)):
    datestr, measurement = line.split()
    if datestr <= last_date:
      raise ValueError(
        "Non-increasing ({line}): {prev} -> {next}".format(
          line=i+1, prev=last_date, next=datestr))

    # TODO: convert measurement to a float, and
    # use datetime.strptime(datestr, '%Y-%m-%d')
    # to get a real date object called 'date'.
    # Yield those instead.

    last_date = datestr
    yield datestr, measurement


def clean_lines(lines):
  for line in lines:
    line = line.strip()
    if not line or line.startswith('#'):
      continue
    yield line


if __name__ == "__main__":
  lines = ['2012-10-10 5.3', '2012-10-11 5.4']
  _assert_equal(['10/10/2012 5.3', '11/10/2012 5.4'],
                ['{} {}'.format(d.strftime('%d/%m/%Y'), w)
                 for d, w in parsed_measurements(lines)])
