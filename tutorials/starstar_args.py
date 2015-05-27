# vim: tw=50

"""Named Argument (Un)packing

You can unpack sequences into function arguments
by prefixing them with |*|, and you can accept
arguments as tuples in your own functions by
specifying a |*args| parameter. These work based
on **argument position** - everything is sent and
received in order.

In much the same way, you can unpack a dictionary
into **named arguments** using the |**| prefix,
and your functions can accept _otherwise
unspecified_ named arguments in a dictionary using
the |**kargs| notation, as shown in the code
window.

Note that function parameters must be _defined_ in a
particular order: positional first, then |*args|, then
|**kargs|. Similarly, they must be _sent_ in a
particular order: positional first, then named.

Exercises

- The |dict| callable creates a dictionary either
  from a sequence of |key, value| pairs or from
  its named arguments (the names become keys in
  the new dictionary). Create and print a
  dictionary using |dict| and named arguments.

- Now try to specify both a sequence of pairs and
  named arguments. What happens?

- Try calling |dict| with another dictionary and
  some named parameters. What happens?
"""

def takes_two(first, second):
  print "first:", first
  print "second:", second

# You can unpack a dictionary into named
# arguments with **:
#
takes_two(**{'first': 'the first thing',
             'second': 'the second thing'})

# You can also define a function that accepts
# unknown named arguments in a dictioary. Any name
# that is not 'prefix', 'name', or 'suffix', will
# end up in kargs.
#
def accepts_keys(prefix, name, suffix='', **kargs):
  print "The Famous", prefix, name + ',', suffix
  print "Extra Info:", kargs

accepts_keys("Dr.", "Batman", "PhD.", sidekick="Postdoc Robin")
accepts_keys(name="Mata Hari", role="Spy", prefix='Ms',
             interrogator="Sir Basil Thompson")

# You can also accept both types of arguments:
#
def accepts_everything(a, b, *args, **kargs):
  print a, b, args, kargs

accepts_everything(1, 2, 3, 4, 5, x='time', y='money')
