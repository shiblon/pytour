import re
import sys

from browser import console, document
from browser import html


_PREAMBLE_LENGTH = {.PREAMBLE_LENGTH} # fill in from controllers.js.
_EXC_LINE_NO = re.compile(r'\bline (\d+)$', re.MULTILINE)


class __out__:
    out_el = document.getElementById('output')

    def __init__(self, el_class='stdout'):
        self.el_class = el_class
        self.last_text = None

    def write(self, text):
        if text == self.last_text:
            console.log('Repeated text found, not sending to output window.')
            return 0

        # TODO: figure out why brython repeats errors when stdout/stderr are
        # overridden like this.
        self.last_text = text

        if self.el_class == 'stderr':
            def line_rewrite(match):
                console.log('in match');
                if not match: return
                lno = int(match.group(1))
                if lno < _PREAMBLE_LENGTH:
                    return 'line {}'.format(lno)
                return 'line {}'.format(lno - _PREAMBLE_LENGTH + 1)

            console.log('before', text)
            try:
                text = _EXC_LINE_NO.sub(line_rewrite, text)
            except Exception as e:
                console.error(e)
            console.log('after', text)

        # TODO: if an exception, look for lines greater than preamble length,
        # and update offset.
        self.out_el <= html.PRE(text, Class=' '.join(['output-entry', self.el_class]))
        return len(text)


sys.stdout = __out__('stdout')
sys.stderr = __out__('stderr')
