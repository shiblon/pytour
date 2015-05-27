# vim:tw=50

"""More on Special Methods

We did some work with the |Shoe| class previously.
Let's explore that some more.

Every method of a class takes |self| as its first
parameter. You don't have to pass it in: Python
does that for you. You can actually name it
anything you want, but the universally accepted
convention is to call it |self|, so you should,
as well. But, more on that later. For now, let's talk
about special methods.

There are a *lot* of special methods you can write
to change the behavior of your class. For example,
if you want your class instances to be _iterable_,
you can define the |__iter__| method to return an
iterator. If you want it to be _indexable_ using
|[]|, you would define one or more of the
|__getitem__|, |__setitem__|, or |__delitem__|
methods. There are ways to make instances look
like numbers (e.g., |__add__|, and |__lt__|),
sequences (e.g., |__nonzero__| and |__len__|), and
even functions (by defining |__call__|). A full
list is here:

http://docs.python.org/2/reference/datamodel.html#special-method-names

Exercises

- Make |Shoe| iterable by adding an |__iter__|
  method that emits each shoe characteristic, one
  at a time.  Print it in a |for| loop. *Hint:* if
  |__iter__| is a generator, calling it will
  return an iterator.
"""

class Shoe(object):
  """Class docstring - tell what this *is*."""

  def __init__(self, color, lace_holes, us_size, weight_oz):
    """Make a new shoe with the given data."""
    self.color = color
    self.lace_holes = lace_holes
    self.us_size = us_size
    self.weight_oz = weight_oz

  def __str__(self):
    return "Shoe({!r}, {!r}, {!r}, {!r})".format(
      self.color, self.lace_holes, self.us_size, self.weight_oz)

  # We can set one method to be equal to another.
  # TODO: try removing this and see what happens.
  __repr__ = __str__

# "Shoe" is a class. Let's create a specific
# instance of it and do stuff with it:
new_shoe = Shoe("red", 10, "8.5 children's", 6)
print repr(new_shoe)
print new_shoe
