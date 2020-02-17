# vim:tw=50

"""Tuples

You have already seen one kind of sequence: the
string. Strings are a sequence of one-character
strings - they're strings all the way down.  They
are also **immutable**: once you have defined one,
it can never change.

Another immutable seqeunce type in Python is the
**tuple**. You define a tuple by separating values
by commas, thus:

  10, 20, 30  # This is a 3-element tuple.

They are usually set apart with parentheses, e.g.,
|(10, 20, 30)|, though these are not always
required (the empty tuple |()|, however, does
require parentheses). It's usually best to just
use them.

Tuples, as is true of every other Python sequence,
support **indexing**, accessing a single element
with the |[]| notation:

  print my_tuple[10]  # Get element 10.

Exercises

- Create a one-element tuple and print it out,
  e.g., |a = 4,| (the trailing comma is required).

- Try comparing two tuples to each other using
  standard comparison operators, like |<| or |>=|.
  How does the comparison work?
"""

# A basic tuple.
a = 1, 3, 'hey', 2
print a

# Usually you see them with parentheses:
b = (1, 3, 'hey', 2)
print b
print "b has", len(b), "elements"

# Indexing is easy:
print "first element", b[0]
print "third element", b[2]

# Even from the right side (the 'back'):
print "last element", b[-1]
print "penultimate", b[-2]

# Parentheses are always required for the empty
# tuple:
print "empty", ()

# And single-element tuples have to have a comma:
print "singleton", (5,)  # A tuple
print "not a tuple", (5)   # A number

# They are immutable, though: you can't change
# them.
b[1] = 'new value'  # oops
