# vim:tw=50

"""More on Self

When you define a class, you can put data and
methods into it. We have seen that you define
methods by indenting function declarations below
the class declaration, and that they are required
to accept |self| as their first parameter.

But what is |self|, exactly? The short version is
this: |self| is the instance. So, when you do
something like this

  s = Shoe('blue', 4, '6w', 12)
  s.change_color('green')

It's the same as if you had done this (try it!)

  Shoe.change_color(s, 'green')

The |self| in |change_color| is whatever |s| is
holding. It's the instance of |Shoe| that we just
created: the thing on the left of the dot.

As we've seen, the way that you create variables
inside of an instance is just like we do in all
other cases in Python: we assign them. These
variables do not exist before they are assigned,
so in |__init__| you'll typically see a lot of
variable assignments just to set things up.

Note that |self| is only automatically passed in
if you call the function on an **instance**. If
you call it on a **class**, it is not.
"""

class Shoe:
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

  def change_color(self, new_color):
    self.color = new_color

s = Shoe('blue', 4, '6w', 12)
print(s)

s.change_color('red')
print(s)
