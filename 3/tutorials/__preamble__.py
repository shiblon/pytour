import sys
from browser import document
from browser import html


class __out__:
    out_el = document.getElementById('output')

    def __init__(self, el_class='stdout'):
        self.el_class = el_class

    def write(self, b):
        self.out_el <= html.PRE(b, Class=' '.join(['outputEntry', self.el_class]))

sys.stdout = __out__('stdout')
sys.stderr = __out__('stderr')
