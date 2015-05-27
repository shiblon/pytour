# vim:tw=50

"""Basic Conversions

We have talked about strings and numbers, and alluded a
bit to the fact that we can convert between them.

You can convert between things like numbers and
strings using the appropriate calls, like
|int("200")| or |str(1.1 ** 24)|.

There are a number of these **callables** (things
you can _call_, like functions, using |()|) that
convert between different types. A few are listed
here (there are many more):

  int       float
  complex   str
  list      tuple

Exercises

- Print the result of |5 * 30|.

- Now try it as |str(5) * 30|. What happened?

- What about |"5" * "30"|?

- You can provide a *numeric base* to |int|. Try printing
  |int("FACE", 16)|. This treats |FACE| as a
  hexadecimal value.
"""

# I have a string, but I want a number!
num_str = "  178000 "

# Yup, it's a string:
print repr(num_str)

# Can it be an int?
print int(num_str)  # spaces are stripped first.

# How about a float?
print float(num_str)

# Of course, converting between numbers works:
print float(10)

# But what happens with this?
print int(10.5)

# We can even make complex values from strings:
print complex("-2+3.2j")

# This won't work:
print int("234notanumber")
