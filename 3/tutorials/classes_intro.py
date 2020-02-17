# vim:tw=50

"""Classes are Types

Let's move on to **classes**. We've been using
them already without directly talking about it, so
let's get down to what they really are.

In general, you can think of a class as a
**type**. This is, of course, merely a useful
fiction because it hides subtlety, but it is still
a great way to think about it, because classes
allow you to create a bunch of things that are the
same _kind_ or _type_ of thing. We'll learn how to
make our own types in the coming slides.

Calling a class makes a new **instance** of it.
If you think of a class as a blueprint for, say, a
house, an instance is the actual house you build
by following the plan.

Some basic properties of classes are demonstrated
in the example code by looking at |ValueError|,
which is a class we've seen and used before.
You've seen a lot of other classes already, such
as |list|, |tuple|, |dict|, |int|, |float|, and
others. We've been referring to them as
"callables", because they are, but that's because
_all_ classes are callable: calling one creates an
instance.
"""

# What is this type of thing anyway?
print("What's a ValueError class?")
print(" ", repr(ValueError))

# Make a new instance of ValueError by calling it.
ex = ValueError("My super informative error message")

# What is this?
# Note how "repr" in this case shows you how to
# make one, which can be really useful.
print("What's a ValueError instance?")
print(" ", repr(ex))

print("What (non-special) stuff is inside of it?")
print("  " + "\n  ".join(x for x in dir(ex) if x[:2] != '__'))

# Now, there are various ways of getting at the
# message:
print("args:   \t", ex.args)
print("with_tb:\t", ex.with_traceback)
print("str:    \t", str(ex))

# But "str" just calls the __str__ method:
print("__str__:\t", ex.__str__())

# And since it has a __str__ method, print can use
# it directly:
print("Bare:   \t", ex)

