# vim: tw=50

"""Named and Default Arguments

Functions (or any callable, really) can be defined
to allow some or all of their arguments to have
**default values**. We have already seen this with
the |dict| call, where you can call it without
parameters to create a new empty dictionary, or
you can call it with a list of |(key, value)|
pairs to create a dictionary that is ready to go
with that data.

To define defaults for function arguments, you
assign them where they are declared, thus:

  def myfunc(greeting, name='Compadre'):
    print greeting, name + '!'

In this example, the parameter called |name| has a
default value that will be used if the caller does
not specify it.

With an understanding of defaults, it now makes
sense to mention **named arguments**. When calling a
function, you can specify some or all of the
parameters by name, using |name=value| syntax.
When arguments are named, they no longer need to
appear in order.

Exercise

- Take a careful look at the code examples. Fiddle
  with them until they make sense.

- Named arguments must come last. Try uncommenting
  the final |print_many_args| call and see what
  happens.
"""

# If no name is specified when this is called, the
# default value is used.
def greet(greeting, name='Schätzli'):
  print greeting + ',', name + '!'

# Use the default name.
greet("Grüezi")

# Use our supplied name.
greet("Hello", "Honey")

# Call using named arguments. Note that, when
# naming arguments, order is unimportant.
greet(name='crazy', greeting='Wow')

# Let's accept even more arguments.
def print_many_args(a, b, c, d="D", e="E", f="F"):
  print a, b, c, d, e, f

# Regular call without defaults:
print_many_args("1", "2", "3", e="new_E")

# It's always a good idea to specify default
# arguments by name, every time. Don't do this
# (even though it works just fine):
print_many_args("1", "2", "3", "4", "5")

# This won't work at all, because named arguments
# must come last. Try uncommenting this line and
# see what happens:
# print_many_args("1", b="hello", "2")
