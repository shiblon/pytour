# vim:tw=50

"""Comprehensions

So far, we have (almost) always used |for| and
|yield| to transform sequences. We'll keep doing
that, but now in a slightly different, more
compact form: **list comprehensions**.

Consider the |get2| function in the code. Given an
iterable over sequences (like a list of tuples or
strings), it produces an iterator over two
specified pieces of each sequence, and it does it
lazily, outputting and consuming only one element
at a time. It's pretty easy to understand.

But, we can write this even more clearly and
succinctly as a comprehension.

Comprehensions can get pretty complex (and if you
find that yours are, just stop and use a loop -
you'll thank yourself later), but the most common
form is pretty clear and easy to grasp:

  [new_item for item in iterable if condition]

This creates a list from items in |iterable|,
optionally filtering elements out that don't pass
the |if| condition.

There is a **generator comprehension** version of
this, too, using |()| instead of |[]|, and lazily
compues its output just like regular generators.
When generator comprehensions are the only
argument to a function, the parentheses can be
dropped, making them easier to read, as in the
|sorted| example in the code. Run it and see what
it's doing.
"""

def get2(iterable, idx1, idx2):
  for val in iterable:
    yield val[idx1], val[idx2]

a = [('a','b','c'),
     ('d','e','f'),
     ('j','k','l'),
     ('g','h','i'),
     ('m','n','o')]

print("first two")
print(list(get2(a, 0, 1)))
print("first and last")
print(list(get2(a, 0, 2)))

# List comprehension
print("first two - comprehension")
print([(x, y) for x, y, z in a])
print("first and last - filtered")
print([(x, z) for x, y, z in a if x < 'j'])

# Generator comprehension
print("raw generator", ((x, y) for x, y, _ in a))
# Look, Ma! No (additional) parentheses!
print(sorted((x, y) for x, y, _ in a))
