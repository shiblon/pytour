# vim:tw=50

"""Regular Expressions

Python, like most other languages these days, has
**regular expression** facilities, but not built
into the language. If you don't know what regular
expressions are, that's a topic all by itself, so
we'll only be covering the barest of the basics
here to show how to use them in Python. More info
can be found here:

http://docs.python.org/2/howto/regex.html

To use regular expressions, you import the |re| module.
You then have access to all of its functions, like
|search|, |match|, and |sub|. There are many others.
Note that |match| almost _never_ does what people think
it should, so ignore it: |search| always works fine.

You can also **compile** your regular expressions
and use them pre-built. This can be more
efficient, and it allows some of their parameters
to be specified outside of the expression, like
|IGNORECASE| instead of |(?i)|. It also makes it
easier to remember parameter order for functions
like |search| and |sub|.

Note that we introduced a new kind of string here,
called a **raw string**. This is a string
specified with |r| in front of it, e.g., |r"I'm
\\raw"|. Raw strings make the |\\| have no
special meaning, so you'll see them used all the
time with regular expressions, and you should
adopt this practice as well.
"""
import re

# When finding things using regular expressions, either
# None or a match object is returned. Since None
# evaluates to False in boolean contexts, you can do
# things like this:
if re.search(r"(?i)kittens", "Kittens on YouTube."):
  print("Kittens found!")

# Match objects also contain information about the
# search, like which groups matched where, etc.
# Here is an alternative approach that first compiles
# the regex and then uses it to extract group
# information.
expr = re.compile(r"^kittens (.*)$", re.IGNORECASE)
match = expr.search("Kittens on YouTube.")
print(match.groups())

# Note that we preface all pattern strings with the
# letter 'r' because raw strings are best for regular
# expression patterns, because they tend to be
# backslash-heavy.
print(re.sub(r"(?i)(\s|.t)", "", "Kittens on YouTube"))

# With date strings:
m = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", "2012-10-31")
print(m.groups())

# Just the year (groups are 1-based when accessed this
# way):
print(m.group(1))
