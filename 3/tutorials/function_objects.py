# vim:tw=50

"""Function Objects

It's time for another short detour into language
concepts.

Functions in Python are just a form of data like
everything else. They can be assigned to
variables, created and returned from other
functions, etc. This can help us solve some
otherwise thorny problems in a clean way.

When you define a function _inside_ of another
one, this is called a **closure**. It is special
because it can not only see variables that are
defined inside of it, it can also see variables in
the _enclosing function scope_. And since it is
created every time the outer function is called,
you can use this to create new custom functions on
demand.

Look at the example code in the code window. Take
a look at how |make_stuff_printer| defines an
inner function, and then *returns* it. We then
assign it to a variable, and by putting |()| after
it, we *call* it.

Note that you can't actually change the
assignment of outer variables in Python 2 unless
they're global. You can in Python 3 using the
|nonlocal| keyword, but in Python 2 you have to
resort to hackery like assigning to outer list
elements. That was foreshadowing, in case you
missed it.

Exercises

- Study the example code, see if you can predict
  what it will do, then run it.

- Try calling |p()| _twice_ inside of the last
  |for| loop. What does it do? Why?
"""

# This is a function that returns another function.
def make_stuff_printer(stuff):
  # The inner function has access to the "stuff"
  # variable passed into the outer function.
  def stuff_printer():
    print stuff

  # Functions are just objects. If we don't call it,
  # it's just another thing to pass around.
  return stuff_printer

# Create and call a new function.
s = make_stuff_printer("What stuff?")

# s is now a function, created by calling
# make_stuff_printer.
s()

# Let's create a bunch of them.
printers = []
for x in range(10):
  printers.append(make_stuff_printer("stuff %d" % x))

# Now we have a list of functions, all of which will
# output something different.
print printers

# Let's call them all and see if they remember the
# state of the world when they were created.
for p in printers:
  p()
