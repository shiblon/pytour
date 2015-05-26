# vim:tw=50

"""Exercise: For Loops (2)

For loops are fundamental in many languages, but
because of generators, which we'll discuss soon,
you see them even more in Python than elsewhere,
so we're going to pause and practice just a bit
more.

There are a couple of reminders that will probably
help you for this exercise:

- You can unpack _any_ tuple into variables like
  this: |a, b = "my", "tuple"| (recall that
  non-empty tuples can be defined without
  parentheses), which makes assigning multiple
  things at once pretty convenient. This can make
  the iterative |fibonacci| function really easy
  to follow, for example.

- There are special assignment operators that
  allow the expression of things like |a = a + 1|
  to be written as |a += 1| instead.  This pattern
  works for all binary operators, including the
  standard math operators like multiplication,
  division, addition, subtraction, and more.

- You can get a sequence of integers by using the
  |range| function. This can be useful in loops,
  e.g., |for i in range(n):|, which assigns the
  numbers |0| through |n-1| to |i|, one at a time.

Exercises

- Implement |fibonacci| again, but this time with
  |for| loops.
"""

__doc__ = """Loop Exercises

>>> fib = []
>>> for i in range(10):
...   fib.append(fibonacci(i))
>>> fib
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""

def fibonacci(n):
  """Returns nth element of the Fibonacci sequence.
  """
  x0, x1 = 0, 1
  # TODO: Fill me in.
  # Recall that the sequence begins with 1, 1,
  # and every element thereafter is the sum
  # of the preceding two elements. So, keep track of
  # the last two elements when you want the next
  # one (which becomes one of the last two for next
  # time).
  return x1


if __name__ == '__main__':
  import doctest
  if not doctest.testmod().failed:
    print "Success!"
