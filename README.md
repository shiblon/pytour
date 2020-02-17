PyTour
======

An in-browser tour of Python. Suitable for new students, teachers, presenters, etc.

You can use this on the web at http://bouncingchairs.net/pytour3, or you can
clone the source, run server.py locally, and open your browser to the indicated
URL. Give it a try!

As a teacher of a class of varying competencies, I found it invaluable to have
the same thing on the presentation screen that the students had on their own
laptops. It was also nice that those who were comfortable with the material
could forge ahead while those who felt less comfortable at least knew that they
could go back over it any time later that evening.

The presentation is built to be usable on many device sizes, and the slide text
can be moved out of the way to give more space to the presentation code window.
The teacher usually doesn't need the slide text anyway.

Students' progress is saved in browser local storage, so they can move forward
and backward through the slides without losing their work.

You can make a tarball distribution using the maketar.sh script, should you
prefer to distribute it to the students and have them run it locally.

If you hack on the tutorial content (slides and initial code), you can change
it dirctly in the (valid Python!) files under the "tutorials" directory. When
you change those, be sure to run the update_tutorials.py script to update the
data in index.html, where it is expected to be.
