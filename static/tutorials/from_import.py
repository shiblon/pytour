# vim:tw=50

"""More on Importing

Some of the functionality you want in Python may
only be available via **packages**, which are
containers for modules. Or, you may just not want
to type the |.| all the time. For example, you may
want to access |math.pi| a lot, but that is a lot
of typing for a short and common symbol.

When importing, you can choose which pieces you
want imported using the |from ... import ...| syntax:

  from math import pi, e

This imports the symbols |pi| and |e| from the
|math| module into the current **global
namespace** so you can just use them without extra
typing.

You can also use |*| in place of a name, which
imports everyting the module knows about. *You
should rarely, if ever do this*, but when you
need it, it's there for you.
"""

__doc__ = """From ... import ...

To import just one thing from a module or package,
see below.
"""

from math import pi, e

print "I know the digits of 'pi' just fine:", pi
print
print "Another beautiful, naturally occurring number:", e
