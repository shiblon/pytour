# vim:tw=50

""""With" Statements, and Our Tracker

Now that we've fiddled around a bit with files,
we know that we don't really need to do much more
with those: they're just iterables over lines, or
(if you call |read|), big long strings. We can
work with line iterables or long strings without
hitting the file system, so we'll continue working
with smaller in-code data.

Coming Up

In the upcoming series of exercises and
instructive slides, we'll build all of the pieces
of a weight tracker with charts for your ... cat.
Or dog. Or some other unembarrassing critter or
object that you aren't allergic to.

The idea will be to (eventually) produce a nice
chart to demonstrate to your pet's vet that the
diet is going well. If your pet is a rock, you
might need to take its weight over geologic time
scales to see any progress.

One More Concept

This is chance to take another deep breath before
the plunge. Let's quickly talk about files and
|with| before we do.

When using files, it's usually a good idea to make
sure that they're closed when we're done with
them, even if something goes wrong. An example of
a very common idiom for that is shown in the code,
using |with|. Don't worry too much about how it
works, just get used to seeing it, particularly
when working with files.
"""

__doc__ = """With Statements

The "with" statement sets up a *context*. A
context is an opportunity to do something with a
resource, then have it automatically cleaned up
(or something else) when you're done.

Files are a great and common example of why you
want one: opening the file provides a context -
you work with the file, and when the context
exits, it closes it for you, even if your code has
a fatal error.

Another example is synchronization primitives like
mutexes, which you want to release after you're
done with them.
"""

def main():
    # With a real file you commonly see
    # with open(filename) as f:
    with myfile as f:
        print(f.read())


# Setup for the above.
if __name__ == '__main__':
    import io
    myfile = io.StringIO('''This is a file
full of lines
each containing some text
# some start with comment leaders
most aren't comments''')

    main()
