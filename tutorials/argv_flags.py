# vim:tw=50

"""Command-line arguments and flags.

This particular part might require you to use the
command line to really try it out, but we'll fake
it a bit for you to give you an idea of what's
what.

When invoking your programs from the command line,
you can accept arguments and do things with them.
For example, you might want your tracker to accept
different filenames to generate chart data for
different cats.

To do this, you access |sys.argv|. For optional
parameters, you can (and should) also use the
|argparse| module as shown. It's fairly
straightforward to set up, and then you can just
access things by name. Documentation can be found
here:

http://docs.python.org/2/library/argparse.html#module-argparse

Tracker Concluded

Now you can really go write that tracker program,
and we'll put this particular project concept
behind us in favor of moving on to more advanced
things. But, you have definitely learned enough
already to write useful software with the
language. It might be a good idea to pause, look
over the slides to this point one more time, and
try writing some small programs. Or, you could
just plunge ahead. There's a lot more fun to be had.
"""

import argparse

PRETEND_COMMANDLINE = './tracker.py input.txt --dryrun -o output.url'

def main():
  # Describe what arguments we understand.
  parser = argparse.ArgumentParser(description="Track Kitty's Progress")
  parser.add_argument('input_file', type=str,
                      help=("Input file name; space-separated "
                            "date, measurement values"))
  parser.add_argument('-o', '--output', type=str,
                      help="Output file name")
  parser.add_argument('-n', '--dryrun', action="store_true")
  # We can also pass in a list directly, but
  # called without arguments it imports sys and
  # uses sys.argv.
  args = parser.parse_args()

  print args
  print args.output
  print args.input_file
  print args.dryrun


# Pay no attention to the man behind the curtain.
if __name__ == '__main__':
  # Set up a fake set of arguments, pretending
  # that we were invoked like this:
  import sys
  sys.argv = PRETEND_COMMANDLINE.split()  # Way simplistic, not fully general.
  main()
