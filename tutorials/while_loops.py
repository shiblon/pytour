# vim:tw=50

""""While" Loops

Recursion is powerful, but not always convenient
or efficient for processing sequences.  That's why
Python has **loops**.

A _loop_ is just what it sounds like: you do
something, then you go round and do it again, like
a track: you run around, then you run around again.

Loops let you do repetitive things, like printing
all of the elements of a list, or adding them all
together, without using recursion.

Python supports two kinds. We'll start with
**while loops**.

A |while| statement is like an |if| statement, in
that it executes the indented block if its condition is
|True| (nonzero). But, unlike |if|, it *keeps on
doing it* until the condition becomes |False| or
it hits a |break| statement. Forever.

The code window shows a while loop that prints
every element of a list. There's another one that
adds all of the elements. It does this
without recursion. Check it out.

Exercises

- Look at |print_all|. Why does it eventually
  stop? What is the value of |i| when it does?

- Why does |slicing_print_all| stop? How does it
  work?
"""

__doc__ = """Use while loops to do things repetitively."""

def print_all(seq):
  """Print all elements of seq."""
  i = 0
  while i < len(seq):
    print "item", i, seq[i]
    i = i + 1  # This is also spelled 'i += 1'

def slicing_print_all(seq):
  """Another way of using while - less efficient."""
  while seq:
    print seq[0]
    seq = seq[1:]

def add_all(seq):
  """Add all of the elements of seq."""
  i = 0
  s = 0
  while i < len(seq):
    s += seq[i]
    i += 1
  return s

print "Using indices:"
print_all([1, 5, 8, "hello", 9])

print "Using slices:"
slicing_print_all(range(3))

print "Summing:"
print "sum of all:", add_all(range(1,12))  # Should be 66
