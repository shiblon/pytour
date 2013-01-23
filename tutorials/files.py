# vim:tw=50

"""Files

We're getting close to being able to write
something really useful. To do that, we need to
_receive_ data from the outside world, not just
_produce_ it.

If you're running this locally, you can access the
file system on your computer from your Python
code. Let's do something silly and potentially a
bit embarrassing (for lack of volume): let's get
all of the lines of the main code for the program
that makes this tutorial work, and print out the
ones that contain comments.

To do this, we'll use the builtin |open| function.
It takes a filename as an argument and returns a
"file-like" object. In Python-speak, this means it
supports some basic things like |read|, |write|
(if writeable), and _iteration_.

Because file objects are **iterable**, they can be
used as the sequence in a |for| loop. When used
like this, they look like a sequence of lines.

Another tidbit in the code is the use of |lstrip|
and |rstrip| on each line in the file:

- |lstrip|: strip whitespace from the left

- |rstrip|: strip whitespace from the right
  (including newlines)

There is also |strip|, which strips it from both sides.
"""

__doc__ = """Files: Opening the Code"""

f = open('server.py')

for line in f:
  if line.lstrip().startswith('#'):  # ignore leading space
    print line.rstrip()  # strip trailing space, including \n.

f.close()
