import contextlib
import new
import StringIO
import sys
import traceback

__author__ = "Chris Monson <shiblon@gmail.com>"

@contextlib.contextmanager
def ScriptContext(fake_filename = '<string>'):
  """Create a context (module) in which we can exec a script.

  This changes sys.stdout, sys.stderr, sys.argv, and sys.modules to make
  scripts look more like they're running in their own environment. It is, of
  course, imperfect, but it catches a lot of common cases and provides a
  (relatively) sane 'help' function implementation.

  Args:
    fake_filename: to be used as sys.argv[0]

  Yields:
    A module that you can use in exec, e.g., exec s in module.__dict__
  """
  original_out = sys.stdout
  original_err = sys.stderr
  original_argv = sys.argv
  original_main = sys.modules['__main__']

  outio = StringIO.StringIO()
  errio = StringIO.StringIO()

  try:
    new_module = new.module("__main__")

    sys.argv = [fake_filename] + original_argv[1:]
    sys.modules["__main__"] = new_module
    sys.stdout = outio
    sys.stderr = errio

    import __builtin__
    new_module.__builtins__ = __builtin__

    # Replace the "help" function to not use a pager - this messes up the
    # server. We'll just have it print to stdout.
    import pydoc
    def new_help(thing=None):
      if thing is None:
        thing = new_module

      if isinstance(thing, basestring):
        strings = {'symbols': pydoc.Helper().listsymbols,
                   'modules': pydoc.Helper().listmodules,
                   'keywords': pydoc.Helper().listkeywords,
                   'topics': pydoc.Helper().listtopics}
        f = strings.get(thing)
        if f is None:
          print >>sys.stderr, ("Can't get help for '%s' in the online "
                               "interpreter.\nPlease use the interactive "
                               "interpreter instead." % thing)
        else:
          f()
      else:
        print >>outio, pydoc.plain(pydoc.TextDoc().document(thing))
    new_help.__name__ = 'help'
    new_help.__doc__ = help.__doc__
    new_module.__dict__['help'] = new_help

    def debug(*args, **kargs):
      print >>original_err, args, kargs

    new_module.__dict__['_debug'] = debug

    yield new_module
  except Exception, e:
    print >>original_err, "INTERNAL ERROR:\n" + traceback.format_exc()
  finally:
    sys.modules['__main__'] = original_main
    sys.stdout = original_out
    sys.stderr = original_err
    sys.argv = original_argv

def RunScript(code):
  """Exec the given code and return strings for stdout and stderr."""
  with ScriptContext() as script_module:
    try:
      exec code in script_module.__dict__
    except:
      # Get exception output as close to exec as possible.
      # We don't take the first entry in the traceback because it just contains
      # "exec". Everything after that is the submitted code.
      try:
        etype, evalue, tb = sys.exc_info()
        traceback.print_exception(etype,
                                  evalue,
                                  tb.tb_next,  # one frame up
                                  file=sys.stderr)
      finally:
        del tb  # break circular references when using exc_info

    return sys.stdout.getvalue(), sys.stderr.getvalue()
