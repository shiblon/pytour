# vim:tw=50

"""Getting Help

One function that is built into the interactive
Python interpreter is |help|. This is a very
useful function, because it gives you basic
documentation on just about anything you want.

For this in-browser tutorial, a close (but incomplete)
approximation of the help function is included,
just to give you a feel for what it does.

You can also run "pydoc" from the commandline, or
use the documentation server with this tutorial
using the *Docs* link above (the |__builtin__|
link is particularly useful).

More complete documentation is always available at
http://python.org/doc/, including a nice tutorial.

Exercises

- Go to the *Docs* link and click on
  |__builtin__|.

- Print |help(int)|. Did it output what you expected?

- Import |math| and run |help| on the module.
  Compare with |dir|.
"""

__doc__ = """Getting Help

Help is available by calling the 'help' function.
It can sometimes be more useful than 'dir'.
"""

print "Help for 'len'"
help(len)

print "Help for symbols"
help('symbols')

print "Help for keywords"
help('keywords')
