# vim:tw=50

"""Math, Modules, and Namespaces

We know how to do basic things like addition and
multiplication, but how do we get at more
interesting things like sines and cosines?

Python comes with "batteries included", which means you
can get a lot of functionality with just the basic
installation. But that functionality is not all
available unless you ask for it by **importing modules**.

Here we import |math| and start to use some of the
things inside of it. Note how we use the |.|
operator to access things _inside_ of the |math|
module. This works for any kind of **namespace**
in Python (something that contains other named
things); a module is just one of several kinds of
namespaces.

Exercises

- The |dir| function gives you a _directory_ of a
  namespace. Print |dir(math)| and see what you
  can find in there.

- Compute |math.sin(math.pi)|. Did it give you the
  answer you expected? How close was it? (Hint:
  |1e-3| is |0.001|).
"""

__doc__ = """Importing Modules, Doing Math"""

import math

# My favorite constants.
print math.pi
print math.e

# Another important one (a square root).
print math.sqrt(2)
