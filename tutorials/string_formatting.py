# vim:tw=50

"""String Formatting

A quick detour is in order, here, since we want to
do interesting things with strings besides
printing out constants.

A string can be *formatted* using the |%| operator
thus:

  "I have %d oranges, but only %d apples" % (5, 3)

What is up with |"%d"| and the |%| operator on a
string? When applied to integers, |%| computes the
_modulus_ (division remainder), but when operating
on a string, it does _substitution_ (for those
familiar with C, this is _printf-style_). Some
examples are in the code window.

There are actually many other format specifiers
(the |%| inside the strings), too many to go into
in this tutorial, but the most common ones are

  - %d: formats an integer (digits)
  - %s: formats anything into a string
  - %r: formats anything using |repr()|

Full documentation is available here:

http://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

The |%|-formatting is old and on its way out, but still
plenty popular and ubiquitous, so understanding it is
worthwhile. |str.format| is pretty neat, so take a look
at the documentation for it when you feel like some
heavy reading:

http://docs.python.org/2/library/string.html#formatstrings

We'll use a bit of both, but |str.format| has many
advantages (including increased clarity), so we'll
gravitate to it over time.
"""

import math

# If you only have one format specifier, and the right
# side is also a string, you can omit the tuple syntax.
print "Hi there, %s!" % "you"

# Integers get to use %d (for "decimal" - %x would be
# "hex").
print "Base 10: %d, Base 16: %x, Base 16: %X" % (30, 30, 30)

# Floating point is %f or %g, and I can never remember
# which one I want, so I go with %f most of the time
# unless it frustrates me enough to dig through the
# docs.
print "A floating point number: %f" % (math.pi)

# You can also specify width and such with numeric
# types.
print "A width-constrained number: %.2f" % (math.pi)

# And, you can get the repr of anything by using %r.
print "The repr of a few things: %r %r %r %r" % ('hi', 26j, 17.4, len)

# There is also a whole new way of formatting strings
# that is really nice and super cool and has loads of
# flexibility and documentation: str.format.
# Definitely look up the docs on this. It has a lot of
# nice features, and it's the Way Of The Future (TM).
print "This is the {0}th time of {1}.".format(17, 30)
