# vim:tw=50

"""Iterables and Iterators

It has been mentioned that |for| loops iterate
over any **iterable**, not just any sequence type.
We also had a taste of what iterators do when
discussing generators. Let's expand on that, now.

The concept of iterable is more general than
that of a sequence. In Python terms, an iterable
is anything that can, when asked for it via
|iter|, produce an iterator.

Iterables include such things as lists, tuples,
strings, sets, dictionaries, files, and of course,
generators.

You can obviously use an iterable in a |for| loop,
but that is not all. You can also ask one for an
iterator that you can advance _by hand_. We
haven't done that very much before, so let's do it
now.

An important thing to note about iterators is
that, once partially consumed, they do not rewind.
Looping over a partially-consumed iterator begins
where it last left off.

When an iterator is exhausted, advancing it causes
the builtin |StopIteration| exception to be
raised. |for| loops know how to handle this,
exiting cleanly when it occurs. When advancing
things by hand, you have to be aware of it.

The sample code demonstrates how these work,
including the |StopIteration| exception. Take time
to understand the examples.
"""

import string

# This is a string, and is therefore iterable
#
letters = string.ascii_lowercase
print letters

# So, we can get an iterator from it.
#
letter_iter = iter(letters)
print letter_iter

# And we can call next on it to get a value and advance
# it.
#
print next(letter_iter)
print next(letter_iter)

# Iterators are iterables that return themselves when
# asked for an iterator, so they can also be used in
# "for" loops. Note how it starts where it left off. It
# is already partially consumed.
#
for letter in letter_iter:
  print letter,
print

# Let's advance to the end.
#
item_iter = iter((1,2))
print next(item_iter)
print next(item_iter)

# StopIteration exception!
# "For" loops know how to handle this and exit cleanly
# when they see StopIteration.
#
print next(item_iter)
