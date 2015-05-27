# vim:tw=50

"""'If' Statements

So far we have been computing things and printing
the results. But this is very inflexible. We want
our data to change _behavior_, not just output.

To do that, we use the |if| statement.

The syntax is shown in the example code. The essential
point is that whatever comes between |if| and |:| is an
expression that must evaluate to |True| or |False|.

A True result will cause the entire **indented
block** of code to execute. Otherwise it is
skipped.  If an |else| block is present, it is
executed when the condition is |False|.

Importantly, code blocks are *always* defined by
indentation in Python. Because of this, the
special |pass| keyword is used to mean "do
nothing" where a block is otherwise expected.

Exercises

- Try making the |else| clause execute by changing
  |a| and |b|.

- Add an |elif a == b:| block between |if| and |else|.
  What does it do?

- Move the |print| statement for the string test
  into an |else| clause, and make the |if| clause
  empty using the |pass| keyword as its body. What
  happens?
"""

if "George" < "Mary":
  print "Alphabetic sorting works!"
  print "And we can say more if we want, too!"

if 0 == 1:
  print "Math is busted."
print "This unindented code always runs"
print "because it is not in the 'if' block."

a = 5
b = 10

if a > b:
  pass  # Do nothing.
else:
  print 'Math still works!'
