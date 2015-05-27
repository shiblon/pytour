# vim:tw=50

"""Lists

Like tuples, **lists** are sequences of any kind
of value, but unlike tuples, they are **mutable**:
they can change contents and size after being
created. To create a list, use |[]|:

  [1, 2, 3, 4]  # A 4-element list.
  []            # An empty list.

They are indexed in exactly the same way as any
other sequence in Python, via the |[]| notation,
but because they are mutable, you can *change
their size* and *assign values to their
elements*:

  a = [1, 3, 5, 7]
  a[1] = 'hello'  # This works.

Lists have lots of **methods** (functions in their
namespace that you can use to manipulate them),
like |append|:

  a.append(9)  # Add 9 to the end of a.

Exercises

- See the code for examples of how to use lists.
  Play with it a bit.

- Use the |str.join| function to join a list of
  strings together. For example, what does
  |'\\n'.join(["hi", "there"])| do? Try different
  **delimiter strings** (in place of |'\\n'|).
"""

# Create a list using [] notation.
a = [7, 3, 1, 9]
print a
print "a has", len(a), "elements"

# Indexing works as expected.
print "third element", a[2]
print "last element", a[-1]

# List are mutable:
a[3] = "hello"    # Change element 3.
print a

# And you can add to them. There are lots more of these
# operations - see help(list).
a.append("new value")
print a

# Sorting is one of those really useful list things:
a.sort()
print a

# Extending is another:
a.extend(['more', 'values'])
print a
