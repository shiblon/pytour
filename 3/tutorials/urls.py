# vim:tw=50

"""Opening URLs

The web is like a huge collection of files,
all jamming up the pipes as they fall off the
truck. Let's quickly turn our attention there,
and learn a little more about file objects while
we're at it.

Let's use |urllib|
(http://docs.python.org/2/library/urllib.html) to
open the Google Privacy Policy, so we can keep an
eye on how long it is getting.

The result of urllib.urlopen is a file-like object. It
therefore supports |read|, and it supports line-by-line
iteration. This is classic Python: define a simple
interface, then just make sure you provide the
needed functions. It doesn't have to _be_ a file
to _act_ like a file, and how it acts is all we
care about.

We'll continue in that spirit by writing our code
so that we can accept any iterable over lines,
which also makes it easy to test.

Exercises

- Open the web site as a file object, get all of the
  words by using |str.split| on each line (|help|
  will come in handy), then count and sum up.
"""

__doc__ = """Count the Words

Note that "count_words" does not specify a file
object, but rather something that can look like a
bunch of lines, because that's all it needs.

>>> count_words(['some words here\\n', 'some words there'])
6
"""

import urllib

def count_words(lines):
  """Counts all words in the 'lines' iterable."""
  #
  # TODO: Fill this in.


def main():
  f = urllib.urlopen(
    "https://www.google.com/intl/en/policies/privacy/")
  print count_words(f)  # I get 2571
  f.close()


if __name__ == '__main__':
  if not _testmod().failed:
    print "Success!"
  main()
