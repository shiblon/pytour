# vim:tw=50

"""Exceptions

We have mentioned that a |for| loop knows when to
stop looping by intercepting the |StopIteration|
exception. We can also do that by hand.

In fact, we can write an equivalent |while| loop
by first creating an iterator, then calling |next|
within a |try|/|except| block that breaks the loop
when it gets a |StopIteration| exception.

Observe the |try|/|except| block in the code.
Statements that might raise an exception are in
the |try| block.  You can then handle those
exceptions in the |except| part, and there can be
more than one of these, e.g., if you want to do
different things for different exceptions.

The |Type as value| syntax is how we get at the
actual exception data, if we want it. Here we
discard it (in which case, we could have left off
|as e| altogether and just said |except
StopIteration:|).

Exercises

- Try printing |e| and |repr(e)|. See what it looks like.

- Try removing the |try|/|except| block in the
  |while| loop and just printing. What happens?

- Inside of |call_ponies|, Wrap the call to
  |print_ponies| in a |try|/|except| block that
  catches the exception and prints it out instead
  of terminating immediately.
"""
for x in "A pony, for me?":
  print(x)
print

# Equivalent to the above is this "while" loop.
#
range_iter = iter("No pony for you today.")
while True:
  try:
    print(next(range_iter))
  except StopIteration as e:
    break  # end the loop early and cleanly
print
# Clean exit!

# Now for a more general exception raising/catching
# example.
#
def print_ponies(number):
  if number < 0:
    # This is not in a "try" block - so it causes
    # the function to terminate immediately.
    raise ValueError("You have a debt of {n} ponies.".format(n=number))
  print("You have {n} ponies".format(n=number))

def call_ponies(number):
  print_ponies(number)
  print("No pony errors!")

call_ponies(10)
call_ponies(-2)
