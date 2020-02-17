#!/usr/bin/env python

"""Update the tutorials in the index.html file."""

import cgi
import contextlib
import HTMLParser
import json
import os
import os.path
import re
import sys

class ContentDivParser(HTMLParser.HTMLParser):
  def __init__(self):
    HTMLParser.HTMLParser.__init__(self)
    self._content_depth = 0
    self.start_pos = None
    self.end_pos = None

  def error(self):
    if self.start_pos is None or self.end_pos is None:
      return True
    return False

  def handle_starttag(self, tag, attrs):
    if tag != 'div' or self.end_pos:
      return

    if not self.start_pos and dict(attrs).get('id') == 'chapter-contents':
      start_line, start_offset = self.getpos()
      taglines = self.get_starttag_text().splitlines()
      if len(taglines) == 1:
        self.start_pos = (start_line, start_offset + len(taglines[0]))
      else:
        self.start_pos = (start_line + len(taglines) - 1, len(taglines[-1]))

    if self.start_pos:
      self._content_depth += 1

  def handle_endtag(self, tag):
    if tag != 'div' or not self.start_pos or self.end_pos or not self._content_depth:
      return

    self._content_depth -= 1

    if not self._content_depth:
      self.end_pos = self.getpos()


def content_lines(tutorials_path):
  tutorials = json.load(open(os.path.join(tutorials_path, '__tutorials__.json')))
  tutorials.insert(0, '__preamble__')

  yield '<!-- Contents of this div are machine-generated.'
  yield '     Edit files in tutorials/ and run update_tutorials.py'
  yield '     To change these chapter contents.'
  yield '-->'

  available_chapters = set(x[:-3] for x in os.listdir(tutorials_path) if x.endswith('.py'))

  for chapter in tutorials:
    if chapter in available_chapters:
      available_chapters.remove(chapter)
    yield '<div name="{}">'.format(chapter)
    start = False
    for line in open(os.path.join(tutorials_path, "{}.py".format(chapter))):
      if not start and re.search(r'^\s*(?:#.*)?$', line):
        continue
      start = True
      yield '  ' + cgi.escape(line.rstrip())
    yield '</div>'

  print "Not using the following chapters:"
  for c in sorted(available_chapters):
    print "  " + c

def main():
  project_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
  tutorials_path = os.path.join(project_dir, 'tutorials')
  static_dir = os.path.join(project_dir, 'static')
  index_path = os.path.join(static_dir, 'index.html')

  original_html = open(index_path).read()
  with contextlib.closing(ContentDivParser()) as parser:
    with open(index_path) as f:
      parser.feed(f.read())
      if parser.error():
        raise ValueError("failed to find properly-closed div with id='chapter-contents'")
      start = parser.start_pos
      end = parser.end_pos

  html_lines = original_html.splitlines()

  # If the tags are on the same line, this is pretty easy.
  start_line, start_offset = start
  end_line, end_offset = end
  start_line -= 1
  end_line -= 1

  before = html_lines[:start_line] + [html_lines[start_line][:start_offset]]
  after = [html_lines[end_line][end_offset:]] + html_lines[end_line+1:]

  new_content = '\n'.join(before + list(('  ' + x).rstrip()
                                        for x in content_lines(tutorials_path)) + after)
  with open(index_path, 'wt') as f:
    print >>f, new_content

if __name__ == "__main__":
  main()
