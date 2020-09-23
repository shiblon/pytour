# vim:tw=50

"""Variables

A **variable** is a place to remember something.
You assign a value to a variable using the
**assignment operator** (a single |=|) like this:

  a = "hi"

Now the variable |a| contains the string |"hi"|.

In Python, variables spring into existence when they
are _assigned a value_. They do not exist before being
assigned, so accessing one without first assigning it
is an error.

A valid **variable name** can contain letters,
numbers, and the |_| character, but cannot begin
with a number. A variable can contain any kind of
value.

An important note: everything in Python, including
variables, is *case-sensitive*. That means that
the variable |A| is different from the variable |a|.
When spelling things, make sure the case is right!

Exercises

- Try assiging to a variable name that starts with a number
  (like 1eet). See what happens.

- Assign a new variable to an existing one, e.g.,
  |b = a|. Print it.
"""

a = "hi there"  # 'a' now contains a string of text.
print(a)

a = 10  # 'a' now contains an integer number.
print(a)

my_longer_varname = 14
print(my_longer_varname)

# Until assigned, variables cannot be accessed.
print(i_dont_exist)  # Not yet assigned!
