# vim:tw=50

"""Exercise: Recursion (2)

Now we'll do something a little bit more
interesting. We'll implement the Fibonacci
sequence.

The Fibonacci sequence shows up in lots of
interesting places:

http://en.wikipedia.org/wiki/Fibonacci_number

In a nutshell, every number in the sequence is
found by adding the previous two numbers, making a
sequence like this:

  1 1 2 3 5 8 13 21 ...

The base case for this is "elements 0 and 1 get
value 1". After that it's just "sum the previous
two to get the next one."

Exercises

- Implement a function that returns the nth
  Fibonacci number. A base case has been provided;
  you fill in the recursion. Hint: you need
  |fibonacci| values for |n-1| and |n-2| to get
  your answer.

Bonus Work

- Implement a function |binary_search(value,
  sequence)| that does binary search on an ordered
  sequence by calling itself on smaller and
  smaller slices.
"""

__doc__ = """Compute the Nth Fibonacci Number.

>>> fibonacci(0)
1

>>> fibonacci(6)
13

>>> fibonacci(7)
21
"""

def fibonacci(n):
  """Compute the nth Fibonacci number."""
  if n <= 1:
    return 1
  # TODO: Fibonacci sequence




if _testmod().failed == 0:
  print "Success!"
