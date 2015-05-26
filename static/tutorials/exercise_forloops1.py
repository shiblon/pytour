# vim:tw=50

"""Exercise: For Loops (1)

For loops are pretty handy and compactly defined.
They fit the way that people think when they want
to "do something to everything in this list".

They're also good for making one list from another
one. We'll do that, here.

Sometimes you have a list, and you realy just want
to know which _index_ each value has. For example,
you want to take a sentence and associate a
location to each word.

In this particular case, it is a convenient way of
converting each pair into named variables without
|[]|-indexing.

Exercises

- Write the |enumerator| function, which takes a
  sequence of items and returns a sequence of
  pairs, as described in the TODO. Make the test pass.
"""

__doc__ = """Enumerator Exercise

>>> enumerator("stuff")
[(0, 's'), (1, 't'), (2, 'u'), (3, 'f'), (4, 'f')]
>>> enumerator(['a', 'b', 'c', 'd'])
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
"""


def enumerator(seq):
  """[item, item, ...] -> [(0, item), (1, item), ...]"""
  # TODO: Implement this using a 'for' loop. Create a
  # new list and append elements to it.
  # HINT: The range function is useful for getting a
  # list of indices into a sequence, if you can take
  # its len.


if __name__ == '__main__':
  if not _testmod().failed:
    print "Success!"

  # Note how, when we know we have a list of pairs, we
  # can just unpack them right in the loop statement.
  for i, x in enumerator("a sequence of characters"):
    print i, x
