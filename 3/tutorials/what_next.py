# vim:tw=50

"""What Next?

You have covered all of the really necessary basic
parts of Python, and that is a lot. Well done! So,
what do you do next? Depending on how comforable
you are with this material, you may want to go
back through the slides one more time, just to
cement things in your mind.

Of course, another next step could be to explore
the more detailed official online Python tutorial:

http://docs.python.org/2/tutorial/

Of particular interest might be a tour of Python's
standard library:

http://docs.python.org/2/tutorial/stdlib.html

Meanwhile, there's a fun little program in the
code window that you are welcome to play with at
your leisure. There are a couple of new concepts
hiding in there, like **decorators** (things
starting with |@| that transform one function into
another), so feel free to look them up if you're
curious.

Other than the decorators, though (of which only
|@classmethod| and |@staticmethod| are used), you
are, with a little time and head-scratching,
completely equipped to understand what is
happening here!

Welcome to Python!
"""

__doc__ = """Sudoku solver, inspired by Peter Norvig.

http://norvig.com/sudoku.html
"""

import random
import re
from math import sqrt

__author__ = "Chris Monson <shiblon@gmail.com>"

def main():
  board = SudokuBoard.fromstring(
  """
    .43   ...   62.
    7..   4.3   ..8
    6..   2.8   ..7

    .75   ...   34.
    ...   ...   ...
    .98   ...   57.

    9..   5.7   ..3
    1..   6.2   ..5
    .87   ...   26.
  """)

  print "Solution:"
  print board.search().pretty_str()


class SudokuBoard(object):
  """Defines a Sudoku board, so we can solve one."""

  def __init__(self):
    """Creates an empty sudoku board, with all squares unconstrained.

    All boards are assumed to be standard 9x9
    boards.  We could do better, but we don't
    bother for this class.
    """
    self.square_size = 3  # large squares on a side
    self.size = self.square_size**2  # squares on a side
    numbers = self.numbers = tuple(xrange(1, self.size + 1))
    rows = self.rows = range(self.size)
    cols = self.cols = range(self.size)
    self.values = dict(((r,c), numbers) for r in rows for c in cols)
    self.number_strings = '.' + ''.join(str(x) for x in self.numbers)

  @staticmethod
  def normalize_puzzle_string(string):
    """Remove superfluous fluff from a sudoku string and prepare it for import

    >>> SudokuBoard.normalize_puzzle_string('..-+5..__4.52230.30')
    '..5....4.5223..3.'
    """
    string = re.sub(r"[\s|+-]+", "", string)
    string = re.sub(r"[0_]", ".", string)
    return string

  @classmethod
  def fromstring(cls, string):
    """Accepts a simple sudoku puzzle string in row-major format.

    [\s-_+] are all ignored, so it can be formatted in ascii art

    args:
      string: a string representing a puzzle
    """
    string = cls.normalize_puzzle_string(string)
    size = int(sqrt(len(string)))
    square_size = int(sqrt(size))
    if size**2 != len(string) or square_size**2 != size:
      raise ValueError("Invalid input string length: %d" % len(string))
    # TODO: remove this constraint for larger puzzles:
    if square_size != 3:
      raise ValueError("Code currently only supports 9x9 puzzles")

    self = cls()
    # Fill in the cells at the places that are specified in the string
    for coords, char in zip(self.cells(), string):
      if char != '.':
        self.assign_value(coords, int(char))

    return self

  def copy(self):
    """Return a copy of this puzzle"""
    new = self.__class__()
    new.values = self.values.copy()
    return new

  def search(self):
    """Searches the puzzle for a solution, returning a *new* puzzle.

    Returns False if it fails.

    This method always searches for the most constrained cell with no fewer
    than two values.  Then it tries one.  Calls eliminate_value, assign_value,
    and itself recursively.
    """
    best_coords = None
    for coords in self.cells():
      size = len(self[coords])
      if size == 1:
        continue
      elif size == 0:
        return False
      elif best_coords is None or size < len(self[best_coords]):
        best_coords = coords

    if best_coords is None:
      return self

    possible_values = list(self[best_coords])
    random.shuffle(possible_values)
    for val in possible_values:
      new_puzzle = self.copy()
      if new_puzzle.assign_value(best_coords, val):
        result = new_puzzle.search()
        if result:
          return result

    return False

  def eliminate_value(self, coords, killval):
    """Removes killval from cell at coords and propagates constraints in place.

    Propagates constraints, in the following way:
      - If the value is not in the specified cell, do nothing.
      - If the elimination results in a singleton, recursively eliminate that
        singleton from all peer cells.
      - If, after doing the recursive elimination, the eliminated value is only
        found in one cell in any given unit, eliminate it from all of that
        cell's peers.  In other words, if I eliminate 3 from a cell, and after
        that's done I find that '3' is only in one cell in that row, then
        eliminate '3' from all cells in that row.
      - If at any time the number of values in a cell goes to zero, this is not
        a valid solution, so we return False.

    args:
      coords: (row, col) of cell to adjust
      killval: the value to be removed from this cell

    returns:
      False if the elimination results in an invalid puzzle, else True.
    """
    if killval not in self[coords]:
      return True

    # Take the value out
    self[coords] = tuple(x for x in self[coords] if x != killval)

    cellvals = self[coords]

    if len(cellvals) == 0:
      return False
    elif len(cellvals) == 1:
      # This is now fully assigned - go ahead and kill it from all peers
      assigned_val = cellvals[0]
      for peer in self.peers_for_cell(coords):
        if not self.eliminate_value(peer, assigned_val):
          return False

    # Now check whether the eliminated value is uniquely found in any cell in
    # any unit.
    for unit in self.units_for_cell(coords):
      unit = list(unit)
      cells_with_killval = tuple(c for c in unit
                                 if killval in self[c] and c != coords)
      if len(cells_with_killval) == 1:
        if not self.assign_value(cells_with_killval[0], killval):
          return False
    return True

  def assign_value(self, coords, goodval):
    """Assigns a value to cell at coords and propagates constraints in place.

    Implemented using eliminate_value.
    """
    cellvals = self[coords]
    for v in cellvals:
      if v != goodval:
        if not self.eliminate_value(coords, v):
          return False
    return True

  def __getitem__(self, key):
    return self.values[key]

  def __setitem__(self, key, val):
    self.values[key] = val

  def __len__(self):
    return len(self.values)

  def cells(self):
    """Returns a row-major iterator over all coordinates in the puzzle

    >>> list(SudokuBoard().cells())[3:12]
    [(0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2)]
    """
    return ((row, col) for row in self.rows for col in self.cols)

  def row_for_cell(self, coords, include_self=False):
    """Iterator over all cells in this cell's row

    args:
      coords: (row, col) of this cell
      include_self: If True, includes given coordinates in output

    >>> s = SudokuBoard()
    >>> list(c for c in s.row_for_cell((5,2)))
    [(5, 0), (5, 1), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    >>> list(c for c in s.row_for_cell((5,2), include_self=True))
    [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    """
    row, col = coords
    return ((row, c) for c in self.cols if include_self or c != col)

  def col_for_cell(self, coords, include_self=False):
    """Iterator over cells in the column containing the given coordinates

    args:
      coords: (row, col) of the cell whose column will be returned
      include_self: If True, includes given coordinates in output

    returns:
      iterator over (row, col) tuples for this column

    >>> s = SudokuBoard()
    >>> list(c for c in s.col_for_cell((3,5)))
    [(0, 5), (1, 5), (2, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    >>> list(c for c in s.col_for_cell((3,5), include_self=True))
    [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    """
    row, col = coords
    return ((r, col) for r in self.rows if include_self or r != row)

  def square_bounds(self, coords):
    """Returns the corners of the square containing this cell.

    The "upper left" is inclusive, the "lower right" is exclusive

    >>> SudokuBoard().square_bounds((4, 3))
    ((3, 3), (6, 6))
    >>> SudokuBoard().square_bounds((2, 6))
    ((0, 6), (3, 9))
    """
    # There are square_size squares of side square_size on a side
    # (e.g. 3 squares of side-length 3 on a side)
    row, col = coords
    r_from = row - (row % self.square_size)
    r_to = r_from + self.square_size
    c_from = col - (col % self.square_size)
    c_to = c_from + self.square_size

    return (r_from, c_from), (r_to, c_to)

  def square_for_cell(self, coords, include_self=False):
    """Iterator over cells in the square containing the given coordinates

    args:
      coords: (row, col) of cell in square
      include_self (False): If true, the given coordinates are included in the
        iteration

    returns:
      iterator over (row, col) coordinate tuples

    >>> s = SudokuBoard()
    >>> list(c for c in s.square_for_cell((1, 1)))
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> list(c for c in s.square_for_cell((8, 7), include_self=True))
    [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    """
    (r_from, c_from), (r_to, c_to) = self.square_bounds(coords)
    for r in range(r_from, r_to):
      for c in range(c_from, c_to):
        if (r, c) != coords or include_self:
          yield r, c

  def units_for_cell(self, coords, include_self=False):
    """Iterator over row, column, and square units containing the given cell.

    args:
      coords: (row, col) of the cells whose units we wish to obtain
      include_self: If true, includes this cell in the output

    returns:
      iterator over iterators, in the following order:
        row
        col
        square

    >>> s = SudokuBoard()
    >>> for unit in s.units_for_cell((1,2)):
    ...   list(unit)
    [(1, 0), (1, 1), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    [(0, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
    >>> for unit in s.units_for_cell((1,2), include_self=True):
    ...   list(unit)
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    # Output the row iterator.
    yield self.row_for_cell(coords, include_self=include_self)
    # Output the column iterator
    yield self.col_for_cell(coords, include_self=include_self)
    # Output the square iterator
    yield self.square_for_cell(coords, include_self=include_self)

  def peers_for_cell(self, coords, include_self=False):
    """Iterator over coordinates of all peers of this cell.

    All values show up exactly once.

    >>> peers = list(SudokuBoard().peers_for_cell((5, 8)))
    >>> peers[:8]
    [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)]
    >>> peers[8:16]
    [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (6, 8), (7, 8), (8, 8)]
    >>> peers[16:]
    [(3, 6), (3, 7), (4, 6), (4, 7)]
    """
    for c in self.row_for_cell(coords, include_self=include_self):
      yield c
    for c in self.col_for_cell(coords, include_self=False):
      yield c
    for c in self.square_for_cell(coords, include_self=False):
      if c[0] != coords[0] and c[1] != coords[1]:
        yield c

  def simple_cell_string(self, values):
    """Returns the simple string value of this cell, '.' for not fully assigned

    >>> s = SudokuBoard()
    >>> s.simple_cell_string((1,2,3))
    '.'
    >>> s.simple_cell_string((2,))
    '2'
    >>> s.simple_cell_string(())
    '!'
    """
    if len(values) == 0:
      return '!'
    elif len(values) == 1:
      return self.number_strings[values[0]]
    else:
      return '.'

  def simple_cell_strings(self):
    """Row-major iterator over cell string values.

    >>> s = SudokuBoard()
    >>> len(tuple(s.simple_cell_strings()))
    81
    >>> tuple(s.simple_cell_strings())[:12]
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.')
    >>> s[1,1] = (3,)
    >>> tuple(s.simple_cell_strings())[:12]
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '3', '.')
    """
    return (self.simple_cell_string(self[r, c]) for r, c in self.cells())

  def pretty_str(self):
    """Produce a nice-looking representation of the board.

    Only shows *fully constrained* values. Cells
    that are not fully defined show up as '.', as
    in simple_cell_strings.
    """
    def row_at_a_time():
      strs = list(self.simple_cell_strings())
      rowstrs = []
      for r in range(self.size):
        row = ''.join(strs[r*self.size:(r+1)*self.size])
        pieces = []
        for c in range(self.square_size):
          pieces.append(row[c*self.square_size:(c+1)*self.square_size])
        yield '   '.join(pieces)
        if (r + 1) % self.square_size == 0:
          yield ''
    return '\n'.join(row_at_a_time())

  def __str__(self):
    def format_cell(values):
      return "".join(self.number_strings[(v in values) * v]
                     for v in self.numbers)

    def columns(row):
      return (format_cell(self[row, c]) for c in self.cols)

    return "\n".join(" ".join(columns(r)) for r in self.rows)

  def __repr__(self):
    return "%s.fromstring('%s')" % (
      self.__class__.__name__,
      "".join(self.simple_cell_strings()))

if __name__ == "__main__":
  main()
  #_testmod()
