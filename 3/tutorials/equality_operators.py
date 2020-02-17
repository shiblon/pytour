# vim:tw=50

"""Equality

Things are **equal** to each other if they have the
_same values_. In Python, testing for equality is
done using the |==| operator, and inequality is
tested with |!=|. As you might expect, |10 !=
"10"| (one is an integer, the other is a string),
but |10 == 5 + 5| (both sides are integers with
the same value).

With variables, things get a little bit more
interesting. Suppose you have two index cards,
each with the number |5| on them. Each card is a
_variable_, and the "5" written on them is their
_value_. Because they have the same values, they
are **equal** in the |==| sense: they contain the
same data. But they are not the same card.

Now suppose I write "5" on one card, show it to
you, and say "This is |a|".  Then I show you _the
same card again_, but say, "This is |b|". In this
case, |a| and |b| are equal in the |is| sense:
they are not only equal (|a == b|), they are also referring
to the same card (|a is b|).

This normally does not matter much, but you will
use it when testing for Python's special "nothing"
value called |None|.

Exercises

- There are other comparison operators, and they
  do what you'd expect, even on strings and other
  sequences. Experiment with |<|, |<=|, |>|, and
  |>=| - see what happens when you print something
  like |5 < 7| or |'hello' >= 'hello there'|.
"""

print("Strings are not equal to integers.")
print("10" != 10)   # True
print(10 == 5 + 5)  # True

print("Variable assignment satisfies 'is'")
a = 1543
b = a

print(a == b)    # Obviously true - same data.
print(a != a+1)  # Indeed.
print(a is b)    # Also true. Assignment satisfies 'is'.

# Performing an operation on data like integers or
# strings produces a *new thing*, even if the data is
# the same.
print("Same data, not same thing.")
b = a + 0

print(a == b)    # Still true.
print(a is b)    # No longer true in some implementations!

print("not None:", a is not None)  # A very common kind of test.
c = None
print(c is not None)  # False
