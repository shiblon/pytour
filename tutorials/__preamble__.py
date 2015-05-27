# This is intended to be executed in the same environment as the script.
# Among other things, it creates a doctest implementation and cleans up the
# namespace from the previous run.

import sys
import contextlib
import StringIO

class _testmod(object):
  sys = sys
  StringIO = StringIO

  def __init__(self):
    self.failed = 0
    self.succeeded = 0
    for s in self.__find_docstrings():
      self.__test_doc_string(s)

  def __parse_doc_string(self, s):
    # States:
    #   None (found >>>) -> Command [add to collected command
    #   None (default) -> None
    #   Command (found >>>) -> Command [store collected command, store empty result, add to collected command]
    #   Command (found ...) -> Command [add to collected command]
    #   Command (blank) -> None [store collected command, store collected result]
    #   Command (default) -> Result [store collected command, add to collected result]
    #   Result (found >>>) -> Command [store collected result, add to collected command]
    #   Result (empty line) -> None [store collected result]
    #   Result (default) -> Result [add to collected result]
    class Result: pass
    class Command: pass

    # Look for instances of >>> and find the text that follows (allowing ellipses).
    state = None

    commands = []
    results = []
    indentation = None
    collected_result = []
    collected_command = []

    lines = s.split('\n')
    # Add a blank at the end to make states simpler.
    for line in lines + ['']:
      ls = line.lstrip()
      if state is None:
        if ls.startswith('>>> '):
          indentation = line[:len(line) - len(ls)]
          collected_command.append(ls[4:])
          state = Command
      elif state is Command:
        if ls.startswith('>>> '):
          indentation = line[:len(line) - len(ls)]
          commands.append('\n'.join(collected_command))
          results.append(None)
          collected_command = [ls[4:].rstrip('\r\n')]
          collected_result = []
        elif ls.startswith('... '):
          if not line.startswith(indentation + '... '):
            raise ValueError("invalid command contination indentation: %r" % line)
          collected_command.append(ls[4:].rstrip('\r\n'))
        elif not ls:
          commands.append('\n'.join(collected_command))
          results.append(collected_result)
          collected_command = []
          collected_result = []
          state = None
        else:
          if not line.startswith(indentation):
            raise ValueError("invalid result indentation: %v", line)
          commands.append('\n'.join(collected_command))
          collected_command = []
          collected_result = [ls.rstrip('\r\n')]
          state = Result
      elif state is Result:
        if ls.startswith('>>> '):
          indentation = line[:len(line) - len(ls)]
          results.append(collected_result)
          collected_result = []
          collected_command = [ls[4:].rstrip('\r\n')]
          state = Command
        elif not ls:
          results.append(collected_result)
          collected_result = []
          state = None
        else:
          if not line.startswith(indentation):
            raise ValueError("invalid result indentation: %r" % line)
          collected_result.append(ls.rstrip('\r\n'))

    if len(commands) != len(results):
      raise ValueError("invalid doctest - different number of commands from results:\n%r\n%r" % (
        commands, results))

    tests = []
    for c, r in zip(commands, results):
      # See if more than one instance of ellipses made it into any result.
      if r is not None:
        numellipses = sum(1 for x in r if x == '...')
        if numellipses > 1:
          raise ValueError("too many ellipsis lines in result %v", r)
      tests.append({'command': c, 'results': r})

    return tests

  @contextlib.contextmanager
  def __redirect_stdio(self):
    out = self.StringIO.StringIO()
    err = self.StringIO.StringIO()
    old_out, self.sys.stdout = self.sys.stdout, out
    old_err, self.sys.stderr = self.sys.stderr, err
    try:
      yield out, err
    finally:
      self.sys.stdout, self.sys.stderr = old_out, old_err

  def __run_test(self, test, environ={}):
    command = test['command']
    expected = test['results']
    result = ""
    try:
      result = eval(command, environ)
    except SyntaxError, synerr:
      with self.__redirect_stdio() as (out, err):
        try:
          exec command in environ
        except Exception, e:
          print e
        result = out.getvalue() + err.getvalue()

    if expected is None:
      return True

    if result is None and expected is not None:
      print "Failed example:"
      print "\t%s" % command
      print "Expected:"
      for line in expected:
        print "\t%s" % line
      print "Got None"
      return False

    # Now that we have tested for None, we can turn it into a string.
    result = repr(result)
    if result.endswith('\n'):
      result = result[:-1]

    result = result.split('\n')

    expanded_expected = expected
    if len(result) > len(expected) and '...' in expected:
      # Search for ellipses, and expand them to make matching easier.
      loc = expected.index('...')
      expanded_expected = expected[:loc] + ['...'] * (len(result) - loc - 1) + expected[loc+1:]

    failed = True

    if len(result) != len(expanded_expected):
      if len(result) == 0:
        print "Failed example:"
        print "\t%s" % command
        print "Expected:"
        for line in expected:
          print "\t%s" % line
        print "Got nothing"
      elif len(expected) == 0:
        print "Failed example:"
        print "\t%s" % command
        print "Expected nothing"
        print "Got:"
        for line in result:
          print "\t%s" % line
      else:
        print "Failed example:"
        print "\t%s" % command
        print "Expected:"
        for line in expected:
          print "\t%s" % line
        print "Got:"
        for line in result:
          print "\t%s" % line
    else:
      for r, e in zip(result, expanded_expected):
        if r != e and e != '...':
          print "Failed example:"
          print "\t%s" % command
          print "Expected:"
          for line in expected:
            print "\t%s" % line
          print "Got:"
          for line in result:
            print "\t%s" % line
          break
      else:
        failed = False

    return not failed

  def __test_doc_string(self, s):
    tests = self.__parse_doc_string(s)
    environ = globals().copy()

    for t in tests:
      if self.__run_test(t, environ):
        self.succeeded += 1
      else:
        self.failed += 1
        print

  def __find_docstrings(self, vardict=None):
    if vardict is None:
      vardict = globals()

    if '__doc__' in vardict:
      yield vardict['__doc__']

    for val in vardict.itervalues():
      if hasattr(val, '__doc__') and val.__doc__:
        yield val.__doc__

      if type(val) in ('type', 'classobj'):
        for d in self.__find_docstrings(val.__dict__):
          yield d

# Clean up the namespace, make sure that help and _testmod make it where they belong.
from pydoc import help
__builtins__.__dict__['help'] = help
__builtins__.__dict__['_testmod'] = _testmod
_kill = set(vars().keys())
for _k in _kill:
  if _k not in ('__builtins__', '__package__', '__nam__', '__doc__', '_k'):
    del vars()[_k]
del _k
del _kill
# This somehow gets changed to __builtin__. Fixing it here.
__name__ = '__main__'
