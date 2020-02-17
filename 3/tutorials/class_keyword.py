# vim:tw=50

"""What is a Class, Really?

Everything that is a thing in Python has a class
behind it. That class is like a description,
telling you what its instances are _like_, what
they _contain_, and what they can _do_.

To create your own sort of class in Python, you
use a |class| declaration as shown in the sample
code. The declaration includes the name of your
class, and a list of other classes that you
**inherit** from. If omitted, it assumes you are
inheriting from |object|.

  class MyClassName:

The body of the class, like in other Python
scopes, is indented below the declaration. Take a
look at the sample code. There we define three
**methods**: |__init__|, |__str__|, and
|__repr__|. These are all _special_ methods, since
they start and end with double underscores.
Special methods are used by Python to do lots of
things.

The |__init__| method, for example, is called when
an instance is created. You can see this when we
create |new_shoe|: when you call a class, Python
creates a boring empty instance (with methods),
then passes that to |__init__| so you can fill it
in with more interesting stuff.

Similarly, when you call |str| or |repr| on an
instance, Python will try to call its
corresponding special methods. Take a look and see
if you can tell how it works.
"""

class Shoe:
  """Class docstring - tell what this *is*."""

  def __init__(self, color, lace_holes, us_size, weight_oz):
    """Make a new shoe with the given data."""
    self.color = color
    self.lace_holes = lace_holes
    self.us_size = us_size
    self.weight_oz = weight_oz

  def __repr__(self):
    return "Shoe({!r}, {!r}, {!r}, {!r})".format(
      self.color, self.lace_holes, self.us_size, self.weight_oz)

  def __str__(self):
    # Note how we do *implicit* string
    # concatenation here: if two string constants
    # are right next to each other, they are joined.
    return ("A size {size} {color} shoe "
            "with {holes} lace holes. "
            "It weighs {weight} ounces.".format(
              size=self.us_size,
              color=self.color,
              holes=self.lace_holes,
              weight=self.weight_oz))


# "Shoe" is a class. Let's create a specific
# instance of it and do stuff with it:
new_shoe = Shoe("red", 10, "8.5 children's", 6)
print(repr(new_shoe))
print(new_shoe)
