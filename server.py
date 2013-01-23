#!/usr/bin/python

import ast
import json
import optparse
import os
import os.path
import pydoc
import random
import runscript
import re
import sys
import threading
import traceback
from wsgiref import simple_server

__author__ = "Chris Monson <shiblon@gmail.com>"

class Redirect(Exception): pass

class App(object):
  def __init__(self, doc_url=""):
    self.doc_url = doc_url

  def __call__(self, environ, start_response):
    status = "200 OK"
    response_body = ""
    response_headers = []
    method = environ.get("REQUEST_METHOD", "GET")

    if not hasattr(self, method):
      status = "405 Method Not Allowed"
      start_response(status, [('Content-Type', 'text/html'),
                              ('Content-Length', str(len(response_body)))])
      return [response_body]

    try:
      headers = {'Content-Type': 'text/html'}
      response_body = getattr(self, method)(environ.get("PATH_INFO", ""),
                                            environ,
                                            headers)
      if response_body is None:
        response_body = ""
      headers['Content-Length'] = str(len(response_body))
      response_headers = headers.items()
    except Redirect, e:
      status = "302 Found"
      response_headers = [('Location', e.message)]
    except:
      status = "500 Internal Server Error"
      response_body = traceback.format_exc()
      print response_body
      response_headers = [('Content-Type', 'text/plain'),
                          ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)
    return [response_body]

  @staticmethod
  def mime_type_from_path(path):
    ext = path.rsplit('.', 1)[-1]
    return {'js': 'application/javascript',
            'css': 'text/css',
            'html': 'text/html',
            'txt': 'text/plain'}.get(ext, 'text/plain')

  def GET(self, path, environ, headers):
    headers['Content-Type'] = self.mime_type_from_path(path)
    if path.startswith('/static/'):
      # Remove dummy path elements starting with VV and remove parent directory
      # references.
      pieces = [p for p in path[1:].split('/') if p != '..' and p[:2] != 'VV']
      return open(os.path.join(*pieces)).read()
    elif path == '/':
      headers['Content-Type'] = 'text/html'
      return open("static/index.html").read()
    elif path == '/doc':
      raise Redirect(self.doc_url)
    elif path == '/tutorials':
      def parse_code_file(fname):
        """Given a filename, return title, description, and code."""
        with open(fname) as f:
          lineiter = f
          # Remove all leading comments (useful for specifying vim or emacs
          # settings without confusing things in the presentation).
          # Also remove leading blank lines. In short, stop when we find a
          # non-comment non-blank.
          for line in lineiter:
            if line.strip() and not re.match(r'^\s*#.*$', line):
              break
          remaining_text = line + ''.join(lineiter)
          match = re.match(r'(?ms)\s*"""(.*?)\n\s*(.*?)"""\s+(.*)$',
                           remaining_text)
          if match:
            # Eval to make sure we handle escaping properly.
            title = ast.literal_eval('"""%s"""' % match.group(1))
            description = ast.literal_eval('"""%s"""' % match.group(2))
            # Strip out '__doc__ =' from the remaining source.
            src = re.sub(r'^(\s*)__doc__\s*=\s*', r'\1', match.group(3))
            return title, description, src
          return "", "", ""
      tutorial_json = ''.join(
        line for line in open(os.path.join("tutorials", "tutorials.json"))
        if line.strip() and not line.lstrip().startswith('//'))
      tutorial_list = json.loads(tutorial_json)
      for i, name in enumerate(tutorial_list):
        fname = os.path.join("tutorials", "%s.py" % name)
        title, description, code = parse_code_file(fname)
        tutorial_list[i] = {"name": name,
                            "index": i,
                            "title": title,
                            "description": description,
                            "code": code}
      headers['Content-Type'] = 'application/json'
      return json.dumps(tutorial_list)
    else:
      return "Could not find file."

  def POST(self, path, environ, headers):
    headers['Content-Type'] = 'application/json'
    try:
      req_size = int(environ.get("CONTENT_LENGTH", 0))
    except ValueError:
      req_size = 0

    req_body = environ["wsgi.input"].read(req_size)
    if not req_body:
      return json.dumps(dict(stdout="", stderr=""))

    out, err = runscript.RunScript(req_body)
    try:
      return json.dumps(dict(stdout=out, stderr=err))
    except Exception, e:
      print "JSON ERROR\n"
      print "OUT:"
      print repr(out)
      print "ERR:"
      print repr(err)
      err = "JSON ERROR - see terminal for info:\n" + traceback.format_exc()
      print err
      return json.dumps(dict(stdout='', stderr=err), ensure_ascii=False)


class NonReverseLookupRequestHandler(simple_server.WSGIRequestHandler):
  def address_string(self):
    # No reverse DNS, please.
    return self.client_address[0]


class DocThread(threading.Thread):
  def __init__(self, port, *args, **kargs):
    self.port = port
    super(DocThread, self).__init__(*args, **kargs)

  def run(self):
    pydoc.serve(self.port)


def main():
  parser = optparse.OptionParser()
  parser.add_option("-p", "--port", type=int, default=8080, dest="port",
                    help="Main port for tutorial")
  parser.add_option("-P", "--docport", type=int, default=8081, dest="docport",
                    help="Pydoc documentation server port")
  parser.add_option("-H", "--host", type=str, default="localhost", dest="host",
                    help=("Host to listen on - change to 0.0.0.0 to "
                          "allow outside connections."))
  options, args = parser.parse_args()

  dirname = os.path.dirname(sys.argv[0])
  if dirname not in ('', '.'):
    os.chdir(dirname)

  display_host = options.host if options.host != '0.0.0.0' else 'localhost'

  print
  if options.host != '0.0.0.0':
    print "  Note - if you want to see this from outside, see the help."
  else:
    print "WARNING: This app is visible from outside of this computer."
    print "         Be aware that arbitrary code can be executed by others."
  print
  print "Tutorial at http://%s:%d/" % (display_host, options.port)

  docthread = DocThread(options.docport)
  docthread.setDaemon(True)
  docthread.start()

  httpd = simple_server.make_server(
    options.host, options.port,
    App(doc_url='http://localhost:{0:d}/'.format(options.docport)),
    handler_class=NonReverseLookupRequestHandler)
  httpd.serve_forever()


if __name__ == '__main__':
  main()
