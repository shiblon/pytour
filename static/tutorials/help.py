# vim:tw=50

"""Getting Help

One function that is built into the interactive
Python interpreter is |help|. This is a very
useful function, because it gives you basic
documentation on just about anything you want.

For this in-browser tutorial, the *help* function
is included, just to give you a feel for what it
does.

You can also run "pydoc" from the commandline, or
access http://python.org/doc/ directly or from the
link above.

Exercises

- Go to the *Docs* link, find Python 2.x, Library
  Reference, and click on
  |Built-in Functions| (direct link here: https://docs.python.org/2/library/functions.html).

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
