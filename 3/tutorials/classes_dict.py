# vim:tw=50

"""Namespace Dictionaries

When |__init__| is called, it is passed a fresh
instance of the class, ready to have new data
added to it. But what is this instance, really?

In a nutshell, it's a _namespace_. Does that sound
familiar? We've seen namespaces before, when we
have _imported modules_. A module is one kind of
namespace in Python, a class is another, and an
instance is still another.

In Python, namespaces are (almost) always
implemented as _dictionaries_. The underlying
dictionary that contains all of their data is
available in the |__dict__| member of the
namespace. Head over the to the code window and
see what happens when you run it.

Something strange has happened here, though. We
can |print(instance.SomeVariable)|, so we might
expect it to be in the instance dictionary, but it
seems to be missing.

It isn't there, but it *is* in the _class
dictionary_. Python, when you try to access a
member of an instance, will _search_ for it,
starting at the instance dictionary, then if it
isn't there, in the class dictionary.

Exercise

- Try changing something in the instance
  dictionary by assigning to, e.g.,
  |instance.__dict__['random']|. Now try printing
  |instance.random|. What happens?
"""

# Three different kinds of namespaces:

import string

class MyTestClass(object):
  """My class docstring."""
  SomeVariable = 'hi there'
  def __init__(self, arg):
    self.arg = arg

instance = MyTestClass('some argument')

# Note that instances can access class variables
# directly, even if they aren't set in __init__.
print(instance.arg)
print(instance.SomeVariable)

# Let's take a look inside of these, now:

print("INSTANCE:------------------------------")
print("\t\n".join("{0}: {1!r}".format(k, v)
                  for k, v in instance.__dict__.items()))

print("CLASS:---------------------------------")
print("\t\n".join("{0}: {1!r}".format(k, v)
                  for k, v in MyTestClass.__dict__.items()))

print("MODULE:--------------------------------")
print("\t\n".join("{0}: {1!r}".format(k, v)
                  for k, v in string.__dict__.items()))

