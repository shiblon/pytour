from html import escape
import re
import sys

from browser import console, document, window
from browser import html


def help(*args, **kargs):
    print("help() not implemented in this environment", file=sys.stderr)


_PREAMBLE_LENGTH = {.PREAMBLE_LENGTH} # fill in from controllers.js.
_EXC_LINE_NO = re.compile(r'\bline (\d+)', re.MULTILINE)


def _assert_equal(want, got):
    if want != got:
        print("assert_equal failed: want:\n\t{!r}\ngot:\n\t{!r}".format(want, got), file=sys.stderr)


def _assert_raises(errtype, call, *args, **kargs):
    try:
        call(*args, **kargs)
        print("assert_raises failed: no exception thrown, {} expected".format(errtype), file=sys.stderr)
    except Exception as e:
        if not isinstance(e, errtype):
            print("assert_raises failed: want error type {!r}, got\n{}".format(errtype, e), file=sys.stderr)
        return


class __out__:
    out_el = document.getElementById('output')

    def __init__(self, el_class='stdout'):
        self.el_class = el_class
        self.last_text = None

    def write(self, text):
        if self.el_class == 'stderr' and text == self.last_text:
            console.log('Repeated text found, not sending to output window.')
            return 0

        # TODO: figure out why brython repeats errors when stdout/stderr are
        # overridden. We usually get 3 repeats.
        self.last_text = text

        if self.el_class == 'stderr':
            def line_rewrite(match):
                if not match: return
                lno = int(match.group(1))
                if lno < _PREAMBLE_LENGTH:
                    return 'line preamble:{}'.format(lno)
                return 'line {}'.format(lno - _PREAMBLE_LENGTH + 1)

            text = _EXC_LINE_NO.sub(line_rewrite, text)

        # TODO: if an exception, look for lines greater than preamble length,
        # and update offset.
        self.out_el <= html.PRE(escape(text), Class=' '.join(['output-entry', self.el_class]))
        return len(text)


sys.stdout = __out__('stdout')
sys.stderr = __out__('stderr')
