import sys
import contextlib
import StringIO

# This is intended to be executed in the same environment as the script.
# Among other things, it creates a doctest implementation and cleans up the
# namespace from the previous run.

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
    #   Command (found >>>) -> Command [add to collected command]
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
          if line[:len(line) - len(ls)] != indentation:
            raise ValueError("invalid command continuation indentation: %r" % line)
          collected_command.append(ls[4:].rstrip('\r\n'))
        elif ls.startswith('... '):
          if not line.startswith(indentation + '... '):
            raise ValueError("invalid command contination indentation: %r" % line)
          collected_command[-1] += '\n' + ls[4:].rstrip('\r\n')
        elif not ls:
          commands.append(collected_command)
          results.append(None)
          collected_command = []
          collected_result = []
          state = None
        else:
          if not line.startswith(indentation):
            raise ValueError("invalid result indentation: %v", line)
          commands.append(collected_command)
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
      yield old_out, old_err, out, err
    finally:
      self.sys.stdout, self.sys.stderr = old_out, old_err

  def __format_exc(self):
    def extract_tb(tb, limit=None):
      def getline(filename, lineno, *args):
        if filename.startswith('<'):
          return None
        return open(filename).readlines()[lineno-1]
      frame_info = []
      n = 0
      inTopLevel = False
      while tb is not None and (limit is None or n < limit):
        f = tb.tb_frame
        lineno = tb.tb_lineno
        co = f.f_code
        filename = co.co_filename
        name = co.co_name
        if not inTopLevel and name == '<module>':
          inTopLevel = True
        line = getline(filename, lineno, f.f_globals)
        if inTopLevel and filename == '<string>':
          if '__lines__' in globals():
            if len(__lines__) >= lineno:
              line = __lines__[lineno-1]
        if line: line = line.strip()
        else: line = None
        frame_info.append((filename, lineno, name, line))
        tb = tb.tb_next
        n = n+1
      return frame_info

    def format_list(entries):
      formatted = []
      for filename, lineno, name, line in entries:
        item = '  File {!r}, line {}, in {}\n'.format(filename, lineno, name)
        if line:
          item += '    {}\n'.format(line.strip())
        formatted.append(item)
      return formatted

    t, e, tb = self.sys.exc_info()
    lastline = '{}: {}'.format(t.__name__, e.message)
    entries = ["Traceback (most recent call last):\n"] + format_list(extract_tb(tb)) + [lastline]
    return ''.join(entries)

  def __run_test(self, test, environ={}):
    command = test['command']
    expected = test['results']
    with self.__redirect_stdio() as (old_out, old_err, out, err):
      for cmdstr in command:
        failed = False
        try:
          result = eval(cmdstr, environ)
          if result:
            print repr(result)
        except SyntaxError, synerr:
          try:
            exec cmdstr in environ
          except Exception:
            print >>err, self.__format_exc()
            failed = True
        except Exception:
          print >>err, self.__format_exc()
          failed = True
        finally:
          result = out.getvalue() + err.getvalue()
        if failed:
          break

    if result is None:
      result = ''

    if result.endswith('\n'):
      result = result[:-1]

    result = result.split('\n')

    if expected is None:
      expected = []

    expanded_expected = expected
    if len(result) > len(expected) and '...' in expected:
      # Search for ellipses, and expand them to make matching easier.
      loc = expected.index('...')
      expanded_expected = expected[:loc] + ['...'] * (len(result) - loc - 1) + expected[loc+1:]

    failed = True

    def format_failure(command, expected, result):
      def format_lines(lines):
        out = []
        for line in lines:
          # Some "lines" are multi-line commands (like loops).
          out.extend('\t{}'.format(l) for l in line.split('\n'))
        return out

      lines = ["Failed example:"]
      lines.extend(format_lines(command))
      if not expected:
        lines.append("Expected nothing")
      else:
        lines.append("Expected:")
        lines.extend(format_lines(expected))
      if not result:
        lines.append("Got nothing")
      else:
        lines.append("Got:")
        lines.extend(format_lines(result))
      return '\n'.join(lines)

    if len(result) != len(expanded_expected):
      print format_failure(command, expected, result)
    else:
      for r, e in zip(result, expanded_expected):
        if r != e and e != '...':
          print format_failure(command, expected, result)
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
__name__ = '__main__'
