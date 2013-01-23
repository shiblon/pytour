# vim:tw=50

""""For" Loops

A much more common loop in Python is the |for|
loop, short for "for every". It is much more
convenient than |while| for doing something to
every element of a sequence:

  for variable in sequence:
    body_statements

Every time through the loop, |variable| is
assigned the next element in |sequence|, and
|body_statements| are executed. When there are no
elements left, the statement exits.

Of note is the use of the |in| keyword. But in this
case it is not used merely as a test for containment, it is
used as a way of saying "give me *everything* |in
sequence|, one at a time in |variable|".

Finally, we also revisit the concept of _unpacking
assignment_. Note the loop that says |for i, x in
...|, which is a kind of assignment, one
that happens every time the loop starts; unpacking
works here too.
"""

__doc__ = """For Loops"""

# For loops help you iterate over sequences:

seq = [1, 3, 6, 10]

print "sequence output"
for x in seq:
  print x


# Here's a way to add up all of the numbers in a
# sequence:
s = 0
for x in seq:
  s += x  # Also spelled 's = s + x'
print "sum", s

# Note that you can also do unpacking assignment
# in the loop itself:

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for x, y in pairs:
  print "x:", x, "y:", y
