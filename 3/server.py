#!/usr/bin/python

import optparse
import os
import os.path
import sys
import traceback
from wsgiref import simple_server

__author__ = "Chris Monson <shiblon@gmail.com>"

class StatusError(Exception): pass
class Redirect(StatusError): pass
class NotFound(StatusError): pass

class App(object):
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
    except NotFound, e:
      status = "404 Not Found"
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
            'txt': 'text/plain',
            'py': 'text/plain'}.get(ext, 'text/plain')

  def get_root(self, path, environ, headers):
    return open("static/index.html").read()

  def GET(self, path, environ, headers):
    headers['Content-Type'] = self.mime_type_from_path(path)
    if path == '/':
      headers['Content-Type'] = 'text/html'
      return open("static/index.html").read()
    else:
      # Must be a static file:
      # Remove parent directory references.
      pieces = [p for p in path.split('/') if p and p != '..']
      # Add static directory.
      pieces = ["static"] + pieces
      relpath = os.path.join(*pieces)
      if not os.path.exists(relpath):
        raise NotFound(relpath)
      return open(relpath).read()


class NonReverseLookupRequestHandler(simple_server.WSGIRequestHandler):
  def address_string(self):
    # No reverse DNS, please.
    return self.client_address[0]


def main():
  parser = optparse.OptionParser()
  parser.add_option("-p", "--port", type=int, default=8080, dest="port",
                    help="Main port for tutorial")
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
  print
  print "Tutorial at http://%s:%d/" % (display_host, options.port)

  httpd = simple_server.make_server(
    options.host, options.port,
    App(),
    handler_class=NonReverseLookupRequestHandler)
  httpd.serve_forever()


if __name__ == '__main__':
  main()
