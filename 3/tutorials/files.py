# vim:tw=50

"""Files

We're getting close to being able to write
something really useful. To do that, we need to
_receive_ data from the outside world, not just
_produce_ it.

In this environment, you can access a virtual filesystem
that is part of the in-browser interpreter.
Let's do something silly: let's get
all of the lines of a fake file (created at the
bottom of the code) and print out the ones that
contain comments.

To do this, we would normally use the builtin
|open| function. It takes a filename as an
argument and returns a "file-like" object. In
Python-speak, this means it supports some basic
things like |read|, |write| (if writeable), and
_iteration_. In this example, we use |StringIO|
to create a file-like thing from a string.

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

# Normally we use the open function to open a file.
# In the browser environment, that doesn't work
# as well, so we have provided an in-memory file
# called "myfile".
#
# If you were to open it in regular Python, it
# might look something like this:
# myfile = open('myfile.txt')

def main():
    for line in myfile:
      if line.lstrip().startswith('#'):  # ignore leading space
        print(line.rstrip())  # strip trailing space, including \n.

    myfile.close()


# Setup for the above.
if __name__ == '__main__':
    import io
    myfile = io.StringIO('''This is a file
full of lines
each containing some text
# some start with comment leaders
most aren't comments''')

    main()
