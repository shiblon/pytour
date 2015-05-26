# vim:tw=50

"""Sorting, Keys, and Lambda

The histogram dictionary is nice, but it is not sorted
(well, it is in the doctest). Let's talk about sorting.

All lists have a |sort| method. If you call it, e.g.,

  mylist.sort()

It will sort the list in place.

You can also use the builtin |sorted| function, which
takes any sequence (not just a list) and produces a new
sorted sequence from it. The code has some examples.

Note: |sort| and |sorted| accept several optional
parameters. One of the most interesting is |key|. If
you create a function that produces a key given one of
the values in your sequence, it will use that key to
determine order instead of the value itself. For
example, to sort a list of numbers backwards, the
key might be described as "take the negative".

In our example, we specify that function using a
|lambda|. Lambdas are basically one-line functions
that accept some arguments and evaluate exactly
one expression, which they return, e.g.:

  myfunc = lambda x: x+10
  myfunc(2) == 12  # True
"""
import collections

def histogram(data):
  # When an item is not present, defaultdict uses
  # the callable you pass it to create and insert
  # a new value. In this case, 0.
  hist = collections.defaultdict(int)
  diter = iter(data)
  last = next(diter)
  for val in diter:
    hist["%.2f" % abs(val-last)] += 1
    last = val
  return hist


hist = histogram([10, 10.2, 10.4, 10.2, 10.1, 10.0, 9.5, 9.8, 8.7])
print "Raw:"
print hist

# Now try sorting it.
print "Sorted:"
for k, v in sorted(hist.items()):
  print "%s: %d" % (k, v)

# Now try sorting it with a weird key (string reversal):
print "Weirdly sorted:"
for k, v in sorted(hist.items(), key=lambda x: x[0][::-1]):
  print "%s: %d" % (k, v)
