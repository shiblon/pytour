# vim:tw=50

"""Generators, Explained

Let's talk more about what you just did.

When you write a function that has a |yield|
keyword, that function is transformed into an
**iterator generator**, meaning that when you call
it, it creates and returns an iterator that you
can use to get at the values that it yields.

We will talk more about the concept of
**iterators** a little later on, but you should
know that |for| loops actually work with
iterators, not just with sequences. An iterator is
something that you can call |next()| on, and it
will produce a new value until it doesn't have any
more.

The example in the code window illustrates some of
these concepts. Returning a list does just what
you would expect, so printing it shows you a nice
list.

Calling a generator, however, does not return you
a list, but ... something else. That something is
an iterator that you can get values out of
whenever you need a new one. Here we call
|next(...)| on it to get one value at a time, and
we also use it in a |for| loop.
"""

# A perfectly normal function.
#
def get_a_list():
  my_list = []
  for x in range(10):
    my_list.append(x)
  return my_list


# A similar function, but it's really a generator.
#
def get_an_iterator():
  for x in range(10):
    yield x


print("Getting a list:", get_a_list())

my_iter = get_an_iterator()

print("Got ... something:", my_iter)
print("Getting the next value:", next(my_iter))
print("Looping over the rest of it:")
for x in my_iter:
  print(x)
