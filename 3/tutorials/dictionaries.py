# vim:tw=50

"""Dictionaries

Sequences are very useful, but they just hold
collections of stuff. Also, they're typically all
about order (|set| being an obvious exception).

**Dictionaries** (type |dict|), on the other hand, give
a name to every piece of data within them. That
name can be a string, or a number, or even a tuple
(with the "hashable" caveat, but that's a
different discussion).  The name is called a
"key".

Dictionaries are typically created with with |{}|
notation, with each element being a |key: value| pair.
You can also create a dictionary by calling |dict|.

To access an element of a dictionary, use the |[]|
indexing notation, but instead of a number, give it a
key. Note that slices are meaningless for dictionaries,
and therefore are not supported.

Unlike |list| and |tuple|, when iterating over or
otherwise outputting a dictionary, order is
_undefined_ and _unreliable_. Don't count on order.

Exercises

- There is a lot of content in the code - read
  through it and see if you can guess what it will
  output before running it.
"""

number_of_children = {"John": 6,
                      "Mary": 2}  # Empty is also allowed.
print "After initialization:", number_of_children
print "John has", number_of_children["John"], "children"

# You can also create new items with index assignment:
number_of_children["George"] = 12
print "Added George:", number_of_children
print

# There are many useful methods in dictionaries.
print number_of_children.keys()   # list of keys
print number_of_children.values() # list of values
print number_of_children.items()  # list of key,value pairs
print

# The 'in' operator always applies to the keys,
# never the values.
print "George" in number_of_children # True
print "Simon" in number_of_children  # False
print

# Using the dict type to create a dictionary:
d1 = dict()
d1["key1"] = "value1"
print d1

# You can also create a dictionary from a sequence
# of key/value pairs using the dict callable type:
d2 = dict([("K1", "v1"), ("K2", "V2")])
print d2
