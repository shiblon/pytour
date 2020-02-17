# vim:tw=50

"""A Tale of Truth

The |if| statement executes its code block when
its **condition is True**. This is a nice, simple
rule, but it's actually a lie. Really, it executes
if its condition is **nonzero**.

In a nutshell, a value is "nonzero" if it is
_something_ instead of _nothing_. The special
"nothing" value |None|, for example, always
evaluates to |False|. Some more examples follow:

  False      True
  ------------------------
  0          -5
  []         ['x', 1, ...]
  ()         (4, 2, ...)
  ''         'hi'

Typically, there is only one way for a thing to be
|False| ("zero"), and anything else is |True|
("nonzero").

Exercises

- |True| and |False| are called "Boolean" types,
  after mathematician George Boole. Try calling
  the |bool| builtin to find out whether something
  evaluates to |True| or |False|. For example, try
  |print(bool(0.0))| or a tiny value like
  |print(bool(1e-20))|.

- Try evaluating |bool('0')|. Is it what you
  expected? Why?
"""

empty_list = []
empty_string = ""

if not empty_list:
  print("Yep, the list is empty")

if empty_string:
  print("The string has values")

if [0]:
  print("The list is not empty")
