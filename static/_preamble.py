# This is intended to be executed in the same environment as the script.
# Among other things, it creates a doctest implementation and cleans up the
# namespace from the previous run.

import sys
import contextlib
import StringIO

class _testmod(object):
  sys = sys

  def __init__(self):
    self.failed = 0
    self.succeeded = 0
    for s in self.__find_docstrings():
      self.__test_doc_string(s)

  def __parse_doc_string(self, s):
    # States:
    #   None (found >>>) -> Result [store command]
    #   None (default) -> None
    #   Result (found >>>) -> Result [store collected result, store command]
    #   Result (empty line) -> None [store collected result]
    #   Result (default) -> Result [add to collected result]
    class Result: pass

    # Look for instances of >>> and find the text that follows (allowing ellipses).
    state = None

    commands = []
    results = []
    indentation = None
    collected_result = []

    lines = s.split('\n')
    for line in lines:
      ls = line.lstrip()
      if state is None:
        if ls.startswith('>>> '):
          commands.append(ls[4:])
          indentation = line[:len(line) - len(ls)]
          state = Result
      elif state is Result:
        if ls.startswith('>>> '):
          results.append(collected_result)
          collected_result = []
          commands.append(ls[4:])
          indentation = line[:len(line) - len(ls)]
        elif not ls:
          results.append(collected_result)
          collected_result = []
          state = None
        else:
          if not line.startswith(indentation):
            raise ValueError("invalid result indentation. Expected %r, got %r" % (
              indentation, line[:len(indentation)]))
          collected_result.append(ls.rstrip())
    if state is Result:
      results.append(collected_result)

    if len(commands) != len(results):
      raise ValueError("invalid doctest - different number of commands from results:\n%r\n%r" % (
        commands, results))

    tests = []
    for c, r in zip(commands, results):
      # See if more than one instance of ellipses made it into any result.
      numellipses = sum(1 for x in r if x == '...')
      if numellipses > 1:
        raise ValueError("too many ellipsis lines in result %v", r)
      tests.append({'command': c, 'results': r})

    return tests

  @contextlib.contextmanager
  def __redirect_stdio(self):
    out = StringIO.StringIO()
    err = StringIO.StringIO()
    old_out, self.sys.stdout = self.sys.stdout, out
    old_err, self.sys.stderr = self.sys.stderr, err
    try:
      yield out, err
    finally:
      self.sys.stdout, self.sys.stderr = old_out, old_err

  def __run_test(self, test):
    command = test['command']
    expected = test['results']
    result = ""
    try:
      result = repr(eval(command))
    except SyntaxError, synerr:
      with self.__redirect_stdio() as (out, err):
        try:
          exec(command)
        except Exception, e:
          print e
        result = out.getvalue() + err.getvalue()

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

    for t in tests:
      if self.__run_test(t):
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
