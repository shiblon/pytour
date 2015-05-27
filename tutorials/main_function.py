# vim:tw=50

"""Main Functions

Python just takes your code and starts doing what
it says, from top to bottom. When you run the code
in the window here, Python just reads it top to
bottom and executes it. When it encounters things
like |def|, it knows to save them for later so you
can call them. But if it encounters code that it
can execute right away, it just does it.

It does this not only when running your program, but
also _when importing modules_. Folks running |import
foo| don't typically expect a lot of work to be done
when they do that - they're providing the work, the
module should just provide the tools.

So, modules should not typically do anything other
than provide variables and |def| and |class|
statements for other code to use. But, it can
still be useful to "run" module code by itself,
like with |doctest|.

We can, it turns out, have it both ways. A very
common idiom is to check the module's |__name__|
to determine whether it is being imported or not,
and to act accordingly. That idiom is shown here.

A bit of free advice: *always do this* in real
code.

Exercises

- Print |__name__|.

- Now |import math| and print |math.__name__|.
"""

__doc__ = """Main Functions Demo

When writing your code, it's a good idea to have
as little in the module's global namespace as
possible. This is typically accomplished by
testing the module's __name__ and providing a main
function where all of the work is really done.

See below: we test __name__ == '__main__'. If it
does, we are not being imported, so we execute the
main function. Otherwise we do nothing (and just
provide stuff for other people to use).
"""


def main():
  print "Here is where we do the *real* work."


if __name__ == '__main__':
  main()
