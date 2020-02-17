# vim:tw=50

"""Slicing

You can get or set the individual elements of a
sequence by using |[]| to index into it. But this
is just a special case of **slicing**.

Slicing allows you to specify a _range_ of
elements in a sequence, even for assignment where
the underlying sequence is mutable.

The most basic slice is |[start:end]| where
|start| is *inclusive*, and |end| is *exclusive*:
|[2:6]| takes everything starting at element |2|,
up to *but not including* element |6|.

There is an extended syntax with two colons, as
well: |[start:end:step]| means you want to take
everything in [start,end), but you only want every
step-th element.

As a quick note, the |range| function can be used
to quickly produce a list of numbers, and its
arguments are similar to those of slices.

Exercises

- Try the |range| function with 1, 2, or 3
  arguments.  See what it does.

- Try reversing a list using slice notation (Hint:
  copy the list with a negative step count).

- Try taking every third element of the reversed
  list.

"""
# The range(10) function produces all numbers in [0,10)
# (like slices, the right endpoint is excluded).
numbers = range(10)
print numbers

# A simple slice.
print "3:8", numbers[3:8]

# A slice containing one element.
print "2:3", numbers[2:3]  # just one element

# But it's really useful because you can assign to
# it.
numbers[2:3] = [11, 12, 13, 14]
print numbers

# Even an empty slice is useful for assignment:
a = [1, 2, 5, 6]
a[2:2] = [3, 4]
print "Assigned to empty slice and got", a

# If you omit one of the slice numbers, it defaults to
# the corresponding endpoint. Negative values work,
# too.
print "from the beginning to 4", numbers[:4]
print "all but the last two", numbers[:-2]
print "from 3 to the end", numbers[3:]

print "everything - a complete copy", numbers[:]

print "every other element", numbers[::2]
