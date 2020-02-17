# vim:tw=50

""""With" Statements, and Our Tracker

Now that we've fiddled around a bit with files and
getting web content, we know that we don't really
need to do much more with those: they're just
iterables over lines, or (if you call |read|), big
long strings. We can work with line iterables or
long strings without hitting the file system or
even the web, so we'll mostly proceed with smaller
in-code data.

Coming Up

In the upcoming series of exercises and
instructive slides, we'll build all of the pieces
of a weight tracker with charts for your ... cat.
Or dog. Or whatever politically correct and
unembarrassing thing that you aren't allergic to.

The idea will be to (eventually) produce a nice
chart to demonstrate to kitteh's vet that the diet
is going well.

One More Concept

This is chance to take another deep breath before
the plunge. Let's quickly talk about files and
|with| before we do.

When using files, it's usually a good idea to make
sure that they're closed when we're done with
them, even if something goes wrong. An example of
a very common idiom for that is shown in the code,
using |with|. Don't worry too much about how it
works, just get used to seeing it, particularly
when working with files.
"""

__doc__ = """With Statements

The "with" statement sets up a *context*. A
context is an opportunity to do something with a
resource, then have it automatically cleaned up
when you're done.

Files are a great and common example of why you
want one: opening the file provides a context -
you work with the file, and when the context
exits, it closes it for you, even if your code has
a fatal error.

Another example is synchronization primitives like
mutexes, which you want to release after you're
done with them.
"""

import os.path

filename = os.path.join("lib", "pypyjs", "lib_pypy", "warnings.py")

with open(filename) as f:
  print f.read()
