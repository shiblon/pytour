# vim:tw=50

"""More on Files: Listing Directories

Before we move on, let's do one more thing with
files.

Here, we will list all files in a directory and
stick them into a list before outputting them.

To do this, we import the |listdir| function from
the |os| module. Heed the comment above the
import, though - in the name of education we are
ignoring best practice.

Incidentally, the |os| module has a lot of
interesting stuff in it. It's worth poking around
the documentation when you can.

Finally, note that we are using the |str.join|
method, here, to print out the listing. Here
|join| is called on the _delimiter_, and the list
of strings is an argument. They are then joined
into a single string. Take some time to understand
what's happening.

Exercises

- Change the loop to only output names that end in
  |.py| and contain the word 'exercise'. You may
  find the |and| operator useful for doing this
  (there is also an |or| operator).
"""

__doc__ = """A Note on Imports

It's usually best to import modules, not import
stuff *out* of modules. This makes it easier to
tell where things come from after you've been away
for a while.

We'll ignore that just to show how 'from' and 'as'
work.
"""

from os import listdir
from os.path import join as pathjoin

parent = 'lib/pypyjs/lib_pypy'

all_files = []
for name in listdir(parent):
  if not name.endswith('.py'):
    # Remember: 'continue' means 'jump to the top
    # of the loop again'.
    continue

  all_files.append(pathjoin(parent, name))

print '\n'.join(all_files)
