# vim:tw=50

"""Recursion

With an understanding of how to write and call
functions, we can now combine the two concepts in
a really nifty way called **recursion**. For
seasoned programmers, this concept will not be at
all new - please feel free to move on. Everyone
else: strap in.

Python functions, like those in many programming
languages, are _recurrent_: they can "call
themselves".

A |def| is really a sort of template: it tells you
*how something is to be done*. When you call it,
you are making it do something *specific*, because
you are providing all of the needed data as
arguments.

From inside of the function, you can call that
same template with something specific *and
different* - this is recursion.

For example, look at the |factorial| function in
the code window.

It starts with a **base case**, which is usually a
really easy version of the problem, where you know
the answer right away. For non-easy versions of the
problem, it then defines a **recursion**, where
it calls itself with a smaller version of the
problem and uses that to compute the answwer.

Exercises

- Uncomment the |print| statements inside of |factorial|
  (above and below |smaller_problem|) to see what
  is happening.
"""

__doc__ = """Introduction to Recursion

The "factorial" of something is formed by
multiplying all of the integers from 1 to the
given number, like this:

  factorial(5) == 5 * 4 * 3 * 2 * 1

You can do this recursively by noting that, e.g.,

  factorial(5) == 5 * factorial(4)

This can't go forever, because we know that

  factorial(1) == 1

See below.
"""

def factorial(n):
  if n <= 1:
    return n
  # print "before recursion", n
  smaller_problem = factorial(n - 1)
  # print "after recursion", n
  return n * smaller_problem


# This gets big fast
print "2! =", factorial(2)
print "7! =", factorial(7)
print "20! =", factorial(20)
