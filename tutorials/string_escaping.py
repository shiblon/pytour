# vim:tw=50

"""String Escaping

There is no difference between |'| and |"| - they both form
equivalent strings. People usually pick one based on preference,
changing only to include quotes inside, like this:

  "Don't touch my quoting."
  'I need to "work", now.'

Occasionally, you need to include both kinds of
quotes inside of a string. In these cases, you can
**escape** quotes using a backslash:

  "This string contains the \\" delimiter."

Strings accept other escape sequences, like |'\n'|, which inserts
a line feed character, making a new line. More
info can be found here:

http://docs.python.org/2/reference/lexical_analysis.html#string-literals

Exercises

- Try creating a string that contains a backslash:
  it will need to be escaped.
"""

__doc__ = """A demonstration of escape sequences.

This multi-line string is delimited with triple
""\", and tells you that by escaping at least one
of them (otherwise the string would end early).
"""

print "This has a double quote \" inside."

print 'This has a single quote \' inside.'

print "This has a second line:\n  And this is it."

print
print __doc__ # Where is the backslash?
